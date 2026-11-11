"""Generate strict Bible markdown (the format scripts/bible_to_json.py parses) from episode data.
Code outputs and compiler/interpreter errors are produced by really running the code."""
import math, os, re, subprocess, tempfile, textwrap

WPS = 1.8          # slow-narrator words per second (Piper length_scale 1.12)
SHORT_WPS = 2.0

def words(t):
    t = re.sub(r"\[(?:HL \d+|TRACK [^\]]+)\]", " ", t)
    return len(t.split())

def mmss(s):
    return f"{s // 60}:{s % 60:02d}"

def run_cpp(name, source, stdin=None):
    d = tempfile.mkdtemp()
    open(os.path.join(d, name), "w").write(source + "\n")
    exe = os.path.join(d, "a.out")
    c = subprocess.run(["g++", "-std=c++17", "-Wall", "-Wextra", name, "-o", exe], cwd=d, capture_output=True, text=True)
    if c.returncode != 0:
        return False, c.stderr.strip(), ""
    r = subprocess.run([exe], cwd=d, input=stdin, capture_output=True, text=True, timeout=10)
    return True, c.stderr.strip(), r.stdout.rstrip("\n")

def run_py(name, source, stdin=None):
    d = tempfile.mkdtemp()
    open(os.path.join(d, name), "w").write(source + "\n")
    r = subprocess.run(["python3", name], cwd=d, input=stdin, capture_output=True, text=True, timeout=10)
    err = re.sub(r'File "[^"]*[/\\]' + re.escape(name) + '"', 'File "' + name + '"', r.stderr.strip())
    if r.returncode != 0:
        return False, err, r.stdout.rstrip("\n")
    return True, err, r.stdout.rstrip("\n")

def runner(lang):
    return run_cpp if lang == "cpp" else run_py

def trim_err(lang, err, maxlines=8):
    lines = err.splitlines()
    return "\n".join(lines[:maxlines])

def scene_lengths(ep):
    out = []
    for s in ep["scenes"]:
        if s["tpl"] == "Pun card":
            out.append(max(4, math.ceil(words(s["narr"]) / WPS)))
        else:
            w = words(s["narr"])
            out.append(max(s.get("min", 15), math.ceil(w / WPS / 5) * 5))
    return out

def build_episode(ep, lang, label):
    run = runner(lang)
    fence = "cpp" if lang == "cpp" else "python"
    lens = scene_lengths(ep)
    starts = [sum(lens[:i]) for i in range(len(lens))]
    total = sum(lens)
    ep["_total"] = total
    ep["_lens"] = lens
    ep["_starts"] = starts
    n = ep["ep"]
    L = []
    L.append(f"## EP {n:02d} — {ep['title']}\n")
    L.append(f"**Module {ep['module']} · {ep['mod_name']} · {mmss(total)} · {ep['bgacc']} · Prerequisite: {ep['prereq']}**\n")
    L.append("**Learning goals:** " + "; ".join(ep["goals"]) + ".\n")
    yt = ep["yt"]
    chapters = " · ".join(f"{mmss(starts[i - 1])} {lab}" for i, lab in sorted(yt["chapters"].items()))
    L.append("### YouTube\n")
    L.append(f"- **Title:** {yt['title']}")
    L.append(f"- **Description:** {yt['desc']} {chapters}")
    L.append(f"- **Tags:** {', '.join(yt['tags'])}")
    L.append(f"- **Thumbnail:** big text \"{yt['thumb_text']}\" {yt['thumb_visual']}\n")
    L.append("### Scene list\n")
    L.append("| # | Start | Length | Template | On screen | Animation & SFX |")
    L.append("| --- | --- | --- | --- | --- | --- |")
    for i, s in enumerate(ep["scenes"]):
        L.append(f"| {i + 1} | {mmss(starts[i])} | {mmss(lens[i])} | {s['tpl']} | {s['on']} | {s['anim']} |")
    L.append("")
    L.append("### Narration script\n")
    for i, s in enumerate(ep["scenes"]):
        L.append(f"**[{i + 1} · {s['name']}]** {s['narr']}\n")
    L.append("### Code shown\n")
    for k, f in enumerate(ep["files"], 1):
        ok, err, out = run(f["name"], f["source"], f.get("stdin"))
        f["_ok"], f["_err"], f["_out"] = ok, err, out
        L.append(f"File {k}: `{f['name']}`" + (f" (scene {f['scene']})" if f.get("scene") else "") + "\n")
        L.append(f"```{fence}\n{f['source']}\n```\n")
        if f.get("stdin"):
            L.append(f"Run with input: {f['stdin'].strip()}\n")
        L.append("**Expected output:**\n")
        L.append(f"```text\n{out}\n```\n")
    b = ep["bug"]
    L.append("### Bug of the Day\n")
    L.append(f"Wrong code ({b['intro']}):\n")
    L.append(f"```{fence}\n{b['wrong']}\n```\n")
    ok, err, out = run(b["file"], b["wrong"], b.get("stdin"))
    b["_ok"], b["_err"] = ok, err
    tool = "GCC output" if lang == "cpp" else "Python output"
    if b.get("mode") == "runtime":
        tool = "GCC and program output"
        parts = []
        if err:
            parts.append(trim_err(lang, err))
        if b.get("stdin"):
            parts.append("Input: " + b["stdin"].strip())
        parts.append("Output when run:\n" + out)
        body = "\n".join(parts)
    else:
        body = trim_err(lang, err) if not ok else "(no error)"
    L.append(f"{tool}:\n")
    L.append(f"```text\n{body}\n```\n")
    L.append(f"Fixed code ({b['fix_intro']}):\n")
    L.append(f"```{fence}\n{b['fixed']}\n```\n")
    ok2, err2, out2 = run(b["file"], b["fixed"], b.get("stdin"))
    b["_fok"], b["_fout"], b["_ferr"] = ok2, out2, err2
    if b.get("show_fixed_out"):
        L.append("Output of the fixed code:\n")
        L.append(f"```text\n{out2}\n```\n")
    L.append(f"**Why:** {b['why']}\n")
    L.append("### Pun & challenge\n")
    L.append(f"- **Pun:** {ep['pun']}")
    L.append(f"- **Challenge:** {ep['challenge']}")
    L.append(f"- **Challenge answer:** {ep['answer']}\n")
    L.append(f"### Shorts for EP {n:02d}\n")
    for s in ep["shorts"]:
        sl = max(20, round(words(s["script"]) / SHORT_WPS) + 2)
        s["_len"] = sl
        built = ", ".join(str(x) for x in s["built"])
        word = "scenes" if len(s["built"]) > 1 else "scene"
        L.append(f"**{s['id']} · {s['title']}** — {mmss(sl)} · built from {word} {built}\n")
        L.append(f"- **Hook (first 1.5s):** \"{s['hook']}\"")
        L.append(f"- **Script:** {s['script']}")
        L.append(f"- **On-screen text:** {s['on']}")
        L.append(f"- **Caption + hashtags:** {s['caption']} " + " ".join("#" + t for t in s["tags"]) + "\n")
    return "\n".join(L)

def build_module(title, intro, eps, lang):
    parts = [f"# {title}\n", intro + "\n"]
    for e in eps:
        parts.append(build_episode(e, lang, ""))
    return "\n".join(parts)
