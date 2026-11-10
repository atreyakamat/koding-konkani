import re, gen, data_py_m1 as M
intro = "Episodes 5–12 · Pastel Blue + Tomato · Python 3.13"
md = gen.build_module("Module 1 — Variables, types and input", intro, M.EPS, "python")
# parser reads "Run with input" from the prose BEFORE the code fence
md = re.sub(r"(File \d+: `[^`]+`[^\n]*\n\n)(```python\n(?:(?!```).)*?\n```\n\n)(Run with input: [^\n]*\n\n)", lambda m: m.group(1) + m.group(3).replace("Run with input: ", "Input: ") + m.group(2), md, flags=re.S)
open("py_m01.md", "w").write(md)
for e in M.EPS:
    print(e["ep"], e["_total"], gen.mmss(e["_total"]), e["_lens"])
    b = e["bug"]
    print("   bug ok?", b["_ok"], "fixed ok?", b["_fok"])
    for f in e["files"]: print("   file ok", f["_ok"])
    for s in e["shorts"]: print("   ", s["id"], s["_len"], len(s["hook"].split()))
    for i,s in enumerate(e["scenes"],1):
        w=gen.words(s["narr"])
        print("   sc",i,s["tpl"],w,round(w/e["_lens"][i-1],2))
