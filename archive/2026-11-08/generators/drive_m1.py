import sys, importlib
sys.path.insert(0, ".")
import gen, data_cpp_m1 as d
for e in d.EPS:
    if "stdin" not in e["files"][0] and False: pass
intro = "Episodes 5–12 · Pastel Blue + Tomato · g++ 13.3, -std=c++17 -Wall -Wextra"
md = gen.build_module("Module 1 — Variables and types", intro, d.EPS, "cpp")
open("cpp_m01.md", "w").write(md)
for e in d.EPS:
    tot = e["_total"]
    nar = sum(gen.words(s["narr"]) for s in e["scenes"])
    print(e["ep"], gen.mmss(tot), tot, "words", nar, [ (l) for l in e["_lens"]])
    b = e["bug"]
    print("   bug wrong ok:", b["_ok"], "| fixed ok:", b["_fok"], "| fixed warn:", bool(b.get("_ferr")))
    for f in e["files"]:
        print("   file", f["name"], f["_ok"], repr(f["_err"][:80]))
    norm=lambda t:t.replace("\u2018","'").replace("\u2019","'")
    miss = [x for x in b.get("expect", []) if x not in norm(b["_err"])]
    if miss: print("   MISSING expect", miss)
