"""Print each [HL n] cue next to the code line it highlights, for manual review."""
import importlib, re, sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
m = importlib.import_module(sys.argv[1])
only = {int(x) for x in sys.argv[2:]}
for e in m.EPISODES:
    if only and e["n"] not in only:
        continue
    for key in ("A", "B"):
        p = e.get(key)
        if not p:
            continue
        lines = p["src"].strip("\n").split("\n")
        print(f"== EP{e['n']} {key} {p['file']}")
        for hl, txt in re.findall(r"\[HL (\d+)\]\s*([^\[]*)", p["narr"]):
            i = int(hl)
            code = lines[i - 1] if i <= len(lines) else "<<PAST END>>"
            print(f"  {i:>2} | {code[:46]:<46} | {txt.strip()[:70]}")
