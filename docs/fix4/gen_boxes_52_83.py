"""Memory boxes data for the blank memory-boxes scenes of EP52-83 (+ Hanoi / showdown bars traces).

Every number comes from the scene's own narration / on-screen text / code, or from a gcc probe
(EP61 offsets 0/32/36 and sizeof 40, EP64 sizes 12 and 8 with offsets, EP71 bytes E8 03 00 00).
Output: boxes_52_83.json  { "EP.scene": {"frames": [...]} }
"""
import json, sys


def c(value, name=None, index=None, address=None, mark=None, lost=None):
    d = {"value": str(value)}
    if name is not None: d["name"] = name
    if index is not None: d["index"] = index
    if address is not None: d["address"] = str(address)
    if mark is not None: d["mark"] = mark
    if lost is not None: d["lost"] = str(lost)
    return d


def g(cells, name=None, tags=None, cols=None, ruler=None):
    d = {}
    if name: d["name"] = name
    if tags: d["tags"] = tags
    if cols: d["cols"] = cols
    if ruler: d["ruler"] = ruler
    d["cells"] = cells
    return d


def f(groups, label=None, badges=None, arrows=None, arrange=None, joiners=None):
    d = {}
    if label: d["label"] = label
    if badges: d["badges"] = badges
    if arrange: d["arrange"] = arrange
    if joiners: d["joiners"] = joiners
    d["groups"] = groups
    if arrows: d["arrows"] = [{"from": a, "to": b} for a, b in arrows]
    return d


D = {}


def put(ep, sc, frames):
    D[f"{ep}.{sc}"] = {"frames": frames}


# ---------------------------------------------------------------- EP52
def street(first_filled=False):
    def row(start):
        cells = []
        for i in range(8):
            addr = start + i
            if first_filled and addr == 1000:
                cells.append(c("19", address=addr, mark="hl"))
            elif first_filled and 1001 <= addr <= 1003:
                cells.append(c("·", address=addr, mark="hl"))
            else:
                cells.append(c("?", address=addr))
        return g(cells)
    return [row(1000), row(1008)]

put(52, 3, [
    f(street(), label="RAM = a long street of tiny houses", badges=["1 box = 1 byte"]),
    f(street(True), label="int age = 19 takes houses 1000-1003", badges=["1 box = 1 byte"]),
])

row_a = lambda stage: g([
    c("19", name="age", address=1000, mark="hl") if stage >= 1 else c("?", address=1000),
    c("·", address=1001, mark="hl") if stage >= 1 else c("?", address=1001),
    c("·", address=1002, mark="hl") if stage >= 1 else c("?", address=1002),
    c("·", address=1003, mark="hl") if stage >= 1 else c("?", address=1003),
    c("A", name="grade", address=1004, mark="hl") if stage >= 2 else c("?", address=1004),
    c("gap", address=1005, mark="zero"),
    c("gap", address=1006, mark="zero"),
    c("gap", address=1007, mark="zero"),
])
row_b = lambda stage: g([c("8.5", name="cgpa", address=1008, mark="hl")] + [c("·", address=1009 + i, mark="hl") for i in range(7)]
                        if stage >= 3 else [c("?", address=1008 + i) for i in range(8)])
put(52, 4, [
    f([row_a(1), row_b(0)], label="int age: 4 bytes, address = first house = 1000", badges=["&age = 1000"]),
    f([row_a(2), row_b(0)], label="char grade: 1 byte at 1004", badges=["&grade = 1004"]),
    f([row_a(2), row_b(3)], label="double cgpa: 8 bytes, 1008-1015", badges=["&cgpa = 1008"]),
])

put(52, 8, [
    f([g([c("8.5", name="cgpa", address="...FB90"),
          c("A", name="grade", address="...FB9B"),
          c("19", name="age", address="...FB9C")])],
      label="Hex counts 0-9 then A-F (F = 15)", badges=["cgpa ...FB90", "grade ...FB9B", "age ...FB9C"]),
    f([g([c("8.5", name="cgpa", address="...FB90"),
          c("A", name="grade", address="...FB9B", mark="hl"),
          c("19", name="age", address="...FB9C", mark="hl")])],
      label="9B and 9C are next-door neighbours", badges=["compiler picks the order"]),
])

# ---------------------------------------------------------------- EP53
put(53, 3, [
    f([g([c(19, name="age", address=1000)]), g([c("?", name="p", address=2000)], name="holds an address")],
      label="p is a pointer: it holds an address", badges=["pointer = 8 bytes"]),
])
put(53, 4, [
    f([g([c(19, name="age", address=1000)]), g([c("?", name="p", address=2000)])],
      label="p is empty, waiting for an address"),
    f([g([c(19, name="age", address=1000)]), g([c(1000, name="p", address=2000, mark="hl")])],
      label="p = &age puts 1000 into p", badges=["p = &age"], arrows=[("1:0", "0:0")]),
])

# ---------------------------------------------------------------- EP54
put(54, 3, [
    f([g([c(10, name="fish", address=1000)])], label="fish holds 10 at address 1000"),
    f([g([c(10, name="fish", address=1000)]), g([c(1000, name="p", address=2000)])],
      label="p holds 1000, so the arrow goes to fish", arrows=[("1:0", "0:0")]),
    f([g([c(10, name="fish", address=1000, mark="hl")]), g([c(1000, name="p", address=2000)])],
      label="*p: read the address, go there, look inside = 10", arrows=[("1:0", "0:0")]),
])
put(54, 4, [
    f([g([c(10, name="fish", address=1000)]), g([c(1000, name="p", address=2000)]), g([c("?", name="copy", address=1004)])],
      label="int copy = *p; follow the arrow", arrows=[("1:0", "0:0")]),
    f([g([c(10, name="fish", address=1000)]), g([c(1000, name="p", address=2000)]), g([c(10, name="copy", address=1004, mark="hl")])],
      label="copy gets 10, fish still has 10", arrows=[("1:0", "0:0")]),
])
put(54, 8, [
    f([g([c(30, name="fish", address=1000), c("?", name="next", address=1004)]), g([c(1000, name="p", address=2000)])],
      label="Both panels start here: p points at fish = 30", arrows=[("1:0", "0:0")]),
    f([g([c(31, name="fish", address=1000, mark="hl", lost=30), c("?", name="next", address=1004)]), g([c(1000, name="p", address=2000)])],
      label="(*p)++ : follow the arrow, then add 1", badges=["(*p)++"], arrows=[("1:0", "0:0")]),
    f([g([c(30, name="fish", address=1000), c("?", name="next", address=1004)]), g([c(1000, name="p", address=2000)])],
      label="*p++ : starts the same, p = 1000", badges=["*p++"], arrows=[("1:0", "0:0")]),
    f([g([c(30, name="fish", address=1000), c("?", name="next", address=1004, mark="hl")]), g([c(1004, name="p", address=2000, mark="hl", lost=1000)])],
      label="*p++ moves p to the neighbour; fish stays 30", badges=["*p++"], arrows=[("1:0", "0:1")]),
])

# ---------------------------------------------------------------- EP55
main_frame = lambda x=5, y=9: g([c(x, name="x", address=1000), c(y, name="y", address=1004)], name="main")
put(55, 3, [
    f([main_frame()], label="main gets a stack frame: x = 5, y = 9"),
    f([main_frame(), g([c(5, name="a", address=3000), c(9, name="b", address=3004), c("?", name="temp", address=3008)], name="swap")],
      label="swap(x, y) copies 5 and 9 into a and b", badges=["call by value"]),
    f([main_frame(), g([c(9, name="a", address=3000, mark="hl", lost=5), c(5, name="b", address=3004, mark="hl", lost=9), c(5, name="temp", address=3008)], name="swap")],
      label="swap swaps the copies", badges=["call by value"]),
    f([main_frame()], label="swap ends, frame gone: x is still 5, y is still 9"),
])
swap_ptr = lambda temp="?", marks=None: g([c(1000, name="a", address=3000), c(1004, name="b", address=3004), c(temp, name="temp", address=3008, mark=marks)], name="swap")
put(55, 4, [
    f([main_frame(), g([c(1000, name="a", address=3000), c(1004, name="b", address=3004), c("?", name="temp", address=3008)], name="swap")],
      label="main sends &x = 1000 and &y = 1004; a and b point back",
      badges=["call by reference"], arrows=[("1:0", "0:0"), ("1:1", "0:1")]),
])
put(55, 5, [
    f([main_frame(), swap_ptr(5, "hl")], label="1/3  temp = *a  (temp gets 5)", badges=["1/3"], arrows=[("1:0", "0:0")]),
    f([g([c(9, name="x", address=1000, mark="hl", lost=5), c(9, name="y", address=1004)], name="main"), swap_ptr(5)],
      label="2/3  *a = *b  (x becomes 9)", badges=["2/3"], arrows=[("1:1", "0:1"), ("1:0", "0:0")]),
    f([g([c(9, name="x", address=1000), c(5, name="y", address=1004, mark="hl", lost=9)], name="main"), swap_ptr(5)],
      label="3/3  *b = temp  (y becomes 5)", badges=["3/3"], arrows=[("1:1", "0:1")]),
    f([g([c(9, name="x", address=1000), c(5, name="y", address=1004)], name="main")],
      label="swap ends: x = 9, y = 5. The real boxes changed!"),
])

# ---------------------------------------------------------------- EP56
marks4 = lambda hl=None: g(
    [c(v, index=i, address=1000 + 4 * i, mark="hl" if hl == i else None) for i, v in enumerate((72, 85, 91, 64))],
    name="marks[4]", ruler={"each": "1 byte", "total": "4 bytes = 1 int"})
put(56, 3, [
    f([marks4(0), g([c(1000, name="p", address=2000)])], label="p points at the first box: *p = 72", arrows=[("1:0", "0:0")]),
    f([marks4(1), g([c(1004, name="p", address=2000, lost=1000)])], label="p++ jumps a whole int: 1004, *p = 85", badges=["+1 element = +4 bytes"], arrows=[("1:0", "0:1")]),
    f([marks4(3), g([c(1012, name="p", address=2000, lost=1004)])], label="p + 2 more ints = 8 bytes: 1012, *p = 64", badges=["+n elements = +4n bytes"], arrows=[("1:0", "0:3")]),
])
word3 = lambda: g([c(ch, index=i, address=2000 + i) for i, ch in enumerate("GOA")], name="char word[3]")
put(56, 4, [
    f([word3(), g([c(2000, name="c", address=3000)])], label="char pointer: 1 byte per step", badges=["char +1", "int +4", "double +8"], arrows=[("1:0", "0:0")]),
    f([word3(), g([c(2001, name="c", address=3000, lost=2000)])], label="c++ : 2001", badges=["char +1", "int +4", "double +8"], arrows=[("1:0", "0:1")]),
    f([word3(), g([c(2002, name="c", address=3000, lost=2001)])], label="c++ : 2002", badges=["char +1", "int +4", "double +8"], arrows=[("1:0", "0:2")]),
])

# ---------------------------------------------------------------- EP57
marks5 = lambda hl=None: g(
    [c(v, index=i, address=1000 + 4 * i, mark="hl" if hl == i else None) for i, v in enumerate((72, 85, 91, 64, 88))],
    name="marks[5]")
put(57, 3, [
    f([marks5(0), g([c(1000, name="marks"), c(1000, name="&marks[0]")])],
      label="The name marks decays to the address of the first element", badges=["array decay"], arrows=[("1:0", "0:0"), ("1:1", "0:0")]),
])
put(57, 4, [
    f([marks5(2), g([c(1008, name="marks + 2")])], label="marks + 2 : walk two ints, address 1008", arrows=[("1:0", "0:2")]),
    f([marks5(2), g([c(1008, name="marks + 2"), c(91, name="*(marks + 2)")])], label="*(marks + 2) knocks on 1008 and finds 91", arrows=[("1:0", "0:2")]),
    f([marks5(2), g([c(1008, name="marks + 2"), c(91, name="*(marks + 2)"), c(91, name="marks[2]")])], label="marks[2] means exactly the same thing", badges=["a[i] = *(a + i)"], arrows=[("1:0", "0:2")]),
])

# ---------------------------------------------------------------- EP58
town = lambda: g([c(ch, index=i, mark="stop" if ch == "\\0" else None) for i, ch in enumerate(["M", "a", "p", "u", "s", "a", "\\0"])], name="char town[] (stack, 7 bytes)")
baga = lambda: g([c(ch, index=i, mark="stop" if ch == "\\0" else None) for i, ch in enumerate(["B", "a", "g", "a", "\\0"])], name="\"Baga\" (read-only, padlocked)")
put(58, 3, [
    f([town()], label="char town[] = \"Mapusa\": your own wooden sign, you can change letters", badges=["7 bytes"]),
    f([town(), baga(), g([c("addr of B", name="beach")], name="const char *beach (stack, 8 bytes)")],
      label="beach points at read-only \"Baga\": read it, never change it", badges=["const = our promise"], arrows=[("2:0", "1:0")]),
])
walker = lambda i: g([c(ch, index=k, mark=("hl" if k == i else ("stop" if ch == "\\0" else None))) for k, ch in enumerate(["B", "a", "g", "a", "\\0"])], name="\"Baga\"")
put(58, 4, [
    f([walker(0), g([c("B", name="*p")], name="p")], label="p at B : *p = B", arrows=[("1:0", "0:0")]),
    f([walker(1), g([c("a", name="*p")], name="p")], label="p++ : *p = a", arrows=[("1:0", "0:1")]),
    f([walker(2), g([c("g", name="*p")], name="p")], label="p++ : *p = g", arrows=[("1:0", "0:2")]),
    f([walker(3), g([c("a", name="*p")], name="p")], label="p++ : *p = a", arrows=[("1:0", "0:3")]),
    f([walker(4), g([c("\\0", name="*p", mark="stop")], name="p")], label="*p is \\0 : the stop sign", arrows=[("1:0", "0:4")]),
])

# ---------------------------------------------------------------- EP59
bus = lambda: g([c(42, name="bus", address=1000)])
ptr_p = lambda: g([c(1000, name="p", address=2000)])
ptr_pp = lambda: g([c(2000, name="pp", address=3000)])
put(59, 3, [
    f([bus()], label="int bus = 42 at 1000"),
    f([bus(), ptr_p()], label="p holds 1000: p points to bus", arrows=[("1:0", "0:0")]),
    f([bus(), ptr_p(), ptr_pp()], label="int **pp holds 2000: pp points to p", arrows=[("1:0", "0:0"), ("2:0", "1:0")]),
])
chain = lambda hl: f(
    [g([c(42, name="bus", address=1000, mark="hl" if hl == 3 else None)]),
     g([c(1000, name="p", address=2000, mark="hl" if hl == 2 else None)]),
     g([c(2000, name="pp", address=3000, mark="hl" if hl == 1 else None)])],
    arrows=[("1:0", "0:0"), ("2:0", "1:0")])
fr = [chain(1), chain(2), chain(3)]
fr[0]["label"] = "pp alone = 2000, the address of p"
fr[1]["label"] = "*pp : one hop, lands on p = 1000"
fr[2]["label"] = "**pp : two hops, lands on bus = 42"
put(59, 4, fr)

main_p = lambda big="NULL", lost=None, mk=None: g(
    [c(12, name="x"), c(30, name="y", mark=mk), c(big, name="big", lost=lost, mark=("hl" if lost else None))], name="main")
func_p = lambda: g([c("&big", name="slot"), c("&x", name="a"), c("&y", name="b")], name="point_to_bigger")
put(59, 8, [
    f([main_p(), func_p()], label="slot points at big, a at x, b at y",
      arrows=[("1:0", "0:2"), ("1:1", "0:0"), ("1:2", "0:1")]),
    f([main_p("&y", "NULL"), func_p()], label="30 is bigger: *slot = b stores &y into big",
      arrows=[("1:0", "0:2"), ("0:2", "0:1")]),
    f([main_p("&y", None, "hl")], label="Back in main: *big = 30", arrows=[("0:2", "0:1")]),
])

# ---------------------------------------------------------------- EP60
code_area = lambda: g([c("add", address="0x401500"), c("sub", address="0x401520")], name="code area (made-up addresses)")
put(60, 3, [
    f([code_area(), g([c("0x401500", name="f")], name="stack")], label="f points at add", arrows=[("1:0", "0:0")]),
    f([code_area(), g([c("0x401520", name="f", mark="hl", lost="0x401500")], name="stack")], label="f = sub : the arrow swings to sub", arrows=[("1:0", "0:1")]),
])

# ---------------------------------------------------------------- EP61
s1_cells = lambda hl=None: g([
    c("30 bytes", name="name", address="+0", mark="hl" if hl == 0 else None),
    c("4 bytes", name="rollNo", address="+32", mark="hl" if hl == 1 else None),
    c("4 bytes", name="percentage", address="+36", mark="hl" if hl == 2 else None)], name="s1")
put(61, 5, [
    f([s1_cells()], label="s1 is one block: name, rollNo, percentage side by side", badges=["typically 40 bytes"]),
    f([s1_cells(1)], label="s1.rollNo : start of s1, then jump to rollNo", badges=["typically 40 bytes"]),
])

# ---------------------------------------------------------------- EP62
card = lambda i, nm, roll, marks, hl=None, lost=None: g([
    c(nm, name="name"), c(roll, name="rollNo"),
    c(marks, name="marks", mark=("hl" if hl else None), lost=lost)], name=f"cls[{i}]")
put(62, 3, [
    f([card(0, "Anya", 1, "78.0"), card(1, "Rohan", 2, "64.5"), card(2, "Sneha", 3, "91.0")],
      label="A row of lockers; each holds a whole ID card"),
    f([card(0, "Anya", 1, "78.0"), card(1, "Rohan", 2, "64.5", hl=True), card(2, "Sneha", 3, "91.0")],
      label="cls[1].marks : pick the card, then the field", badges=["cls[1].marks"]),
])
put(62, 4, [
    f([g([c("&cls[1]", name="p")]), card(1, "Rohan", 2, "64.5")],
      label="p points at the whole struct cls[1]", arrows=[("0:0", "1:0")]),
    f([g([c("&cls[1]", name="p")]), card(1, "Rohan", 2, "64.5", hl=True)],
      label="p->marks : go to the struct, take its marks", badges=["(*p).marks = p->marks"], arrows=[("0:0", "1:0")]),
])

# ---------------------------------------------------------------- EP64
def order(upto):
    bytes_ = [("size", "size"), ("pad", "pad"), ("pad", "pad"), ("pad", "pad"),
              ("qty", "qty"), ("qty", "qty"), ("qty", "qty"), ("qty", "qty"),
              ("type", "type"), ("pad", "pad"), ("pad", "pad"), ("pad", "pad")]
    cells = []
    for i, (v, _) in enumerate(bytes_[:upto]):
        cells.append(c(v, index=i, mark=("zero" if v == "pad" else "hl")))
    return g(cells, name="struct Order")
put(64, 3, [
    f([order(4)], label="size at byte 0; qty must start at a multiple of 4, so bytes 1-3 are padding"),
    f([order(8)], label="qty takes bytes 4-7"),
    f([order(12)], label="type at byte 8, then padding up to a multiple of 4", badges=["6 useful + 6 padding = 12"]),
])
pk = [("qty", 0), ("qty", 1), ("qty", 2), ("qty", 3), ("size", 4), ("type", 5), ("pad", 6), ("pad", 7)]
packed = lambda upto: g([c(v, index=i, mark=("zero" if v == "pad" else "hl")) for v, i in pk[:upto]], name="struct Packed")
put(64, 4, [
    f([packed(4)], label="Biggest member first: qty in bytes 0-3"),
    f([packed(8)], label="size at 4, type at 5, 2 bytes of padding", badges=["8 bytes", "4 bytes saved"]),
])

# ---------------------------------------------------------------- EP65
put(65, 3, [
    f([g([c(1, name="room")], name="STACK: main")], label="main's frame holds room"),
    f([g([c(1, name="room")], name="STACK: main"), g([c(5, name="local")], name="STACK: visit (on top)")], label="visit's frame goes on top: local = 5", badges=["stack = fast, small"]),
    f([g([c(1, name="room")], name="STACK: main")], label="visit returns: its plate is removed, local is gone", badges=["Windows ~1 MB", "Linux ~8 MB"]),
])
put(65, 4, [
    f([g([c("→ crate", name="godown")], name="STACK"), g([c(500, name="crate")], name="HEAP"), g([c(0, name="global_count")], name="GLOBAL")],
      label="malloc rents a crate; godown holds its address", badges=["stack: locals", "heap: malloc", "global: whole run"],
      arrows=[("0:0", "1:0")]),
    f([g([c("→ crate", name="godown")], name="STACK"), g([c(500, name="crate", mark="zero")], name="HEAP (crate returned)"), g([c(0, name="global_count")], name="GLOBAL")],
      label="free(godown) hands the crate back", badges=["stack: locals", "heap: malloc", "global: whole run"]),
])

# ---------------------------------------------------------------- EP66
blk = lambda vals, mark=None: g([c(v, index=i, address=f"0x{0x5000 + 4 * i:x}", mark=mark) for i, v in enumerate(vals)], name="heap block", ruler={"each": "4 bytes", "total": "12 bytes"})
put(66, 3, [
    f([g([c(3, name="n"), c("0x5000", name="marks")], name="stack"), blk(["?", "?", "?"])],
      label="n * sizeof(int) = 3 * 4 = 12 bytes", arrows=[("0:1", "1:0")]),
])
put(66, 4, [
    f([g([c(3, name="n"), c("0x5000", name="marks")], name="stack"), blk([60, 70, 80])], label="Fill the boxes: 60, 70, 80", arrows=[("0:1", "1:0")]),
    f([g([c(3, name="n"), c("0x5000", name="marks")], name="stack"), blk([60, 70, 80], mark="zero")],
      label="free(marks): block returned, but marks still holds 0x5000", arrows=[("0:1", "1:0")]),
    f([g([c(3, name="n"), c("NULL", name="marks", mark="hl", lost="0x5000")], name="stack"), blk([60, 70, 80], mark="zero")],
      label="marks = NULL : nobody can use the old address by mistake"),
])

# ---------------------------------------------------------------- EP67
put(67, 3, [
    f([g([c("?", index=i) for i in range(3)], name="malloc(3 * sizeof(int)) : not cleaned")], label="malloc: a rented room that was not cleaned"),
    f([g([c("?", index=i) for i in range(3)], name="malloc(3 * sizeof(int)) : not cleaned"), g([c(0, index=i, mark="zero") for i in range(3)], name="calloc(3, sizeof(int)) : all zero")],
      label="calloc cleans every byte to zero"),
])
bk = lambda vals, base, name, mark=None: g([c(v, index=i, address=f"0x{base + 4 * i:x}", mark=mark) for i, v in enumerate(vals)], name=name)
put(67, 4, [
    f([g([c("0x5000", name="basket")], name="stack"), bk([10, 20], 0x5000, "heap block")], label="basket holds 2 ints at 0x5000", arrows=[("0:0", "1:0")]),
    f([g([c("0x5000", name="basket")], name="stack"), bk([10, 20, "?", "?"], 0x5000, "heap block")], label="Case A: free space after it, stretched in place, same address", badges=["Case A"], arrows=[("0:0", "1:0")]),
    f([g([c("0x5000", name="basket"), c("0x6000", name="bigger")], name="stack"), bk([10, 20], 0x5000, "old block", "zero"), bk([10, 20, "?", "?"], 0x6000, "new block")],
      label="Case B: no room, new block at 0x6000, 10 and 20 copied, old block freed", badges=["Case B"], arrows=[("0:1", "2:0")]),
    f([g([c("0x6000", name="basket", mark="hl", lost="0x5000"), c("0x6000", name="bigger")], name="stack"), bk([10, 20], 0x5000, "old block", "zero"), bk([10, 20, "?", "?"], 0x6000, "new block")],
      label="Always use the address realloc returns: basket moves to 0x6000", badges=["Case B"], arrows=[("0:0", "2:0")]),
])

# ---------------------------------------------------------------- EP68
put(68, 3, [
    f([g([c("0x5000", name="p")], name="leaky() frame"), g([c("?")], name="heap block")], label="malloc inside a function, no free", arrows=[("0:0", "1:0")]),
    f([g([c("?", address="0x5000", mark="hl")], name="heap block")], label="LEAK: the frame is gone, nobody can free me", badges=["leak"]),
])
put(68, 4, [
    f([g([c("0x7000", name="ticket")], name="stack"), g([c(101, address="0x7000")], name="heap block")], label="ticket points at a block holding 101", arrows=[("0:0", "1:0")]),
    f([g([c("0x7000", name="ticket", mark="hl")], name="stack"), g([c(101, address="0x7000", mark="zero")], name="heap block (returned)")],
      label="free(ticket): ticket still holds 0x7000, a dangling pointer", badges=["use after free"], arrows=[("0:0", "1:0")]),
])
put(68, 5, [
    f([g([c("0x7000", name="p")], name="stack"), g([c(101, address="0x7000", mark="zero")], name="heap block (returned)"), g([c("0x7000", mark="hl")], name="ledger of returned blocks")],
      label="free(p) the first time: the ledger notes 0x7000", arrows=[("0:0", "1:0")]),
    f([g([c("0x7000", name="p")], name="stack"), g([c(101, address="0x7000", mark="zero")], name="heap block (returned)"), g([c("0x7000", mark="hl"), c("0x7000", mark="hl")], name="ledger of returned blocks")],
      label="free(p) again: the same entry twice, the ledger is corrupted", badges=["double free"], arrows=[("0:0", "1:0")]),
])

# ---------------------------------------------------------------- EP69
put(69, 4, [
    f([g([c("NULL", name="fp")], name="FILE *fp"), g([c("diary.txt", name="file"), c("0", name="position")], name="file handle")],
      label="fp is only a pointer; the handle lives inside C"),
    f([g([c("→ handle", name="fp", mark="hl")], name="FILE *fp"), g([c("diary.txt", name="file"), c("0", name="position")], name="file handle")],
      label="fopen gives fp the handle: which file, where we are", arrows=[("0:0", "1:0")]),
])

# ---------------------------------------------------------------- EP71
put(71, 3, [
    f([g([c("1", index=0), c("0", index=1), c("0", index=2), c("0", index=3)], name="text file: '1' '0' '0' '0'")],
      label="As text: four characters, converted back when read", badges=["readable"]),
    f([g([c("1", index=0), c("0", index=1), c("0", index=2), c("0", index=3)], name="text file: '1' '0' '0' '0'"),
       g([c("E8", index=0, mark="hl"), c("03", index=1, mark="hl"), c("00", index=2, mark="hl"), c("00", index=3, mark="hl")], name="binary file: int 1000, 4 raw bytes")],
      label="As an int: the bytes exactly as they sit in memory", badges=["junk in Notepad", "loads instantly"]),
])

# ---------------------------------------------------------------- EP77
stk = lambda frames_: g([c(v, name=n) for n, v in frames_], name="call stack (bottom to top)")
M = ("main", "-")
H3 = ("hanoi", "3,A,C,B")
H2 = ("hanoi", "2,A,B,C")
H1 = ("hanoi", "1,A,C,B")
H0 = ("hanoi", "0,A,B,C")
put(77, 7, [
    f([stk([M, H3])], label="main calls hanoi(3): frame pushed"),
    f([stk([M, H3, H2])], label="hanoi 3 calls hanoi 2: pushed on top"),
    f([stk([M, H3, H2, H1])], label="hanoi 2 calls hanoi 1: pushed on top"),
    f([stk([M, H3, H2, H1, H0])], label="hanoi 1 calls hanoi 0: five frames deep, returns at once", badges=["depth 5 (with main)"]),
    f([stk([M, H3, H2, H1])], label="hanoi 0 popped. hanoi 1 prints: Move 1: disc 1 from A to C"),
    f([stk([M, H3, H2])], label="hanoi 1 finished, popped. hanoi 2 prints: Move 2: disc 2 from A to B"),
])

# ---------------------------------------------------------------- EP83
SLOTS = 5
def stack_cells(vals, hl=None):
    return g([c(vals[i] if i < len(vals) else "·", index=i, mark=("hl" if hl == i else (None if i < len(vals) else "zero"))) for i in range(SLOTS)], name="stack[5]")
def top_cell(t): return g([c(t, name="top")])
put(83, 4, [
    f([stack_cells([]), top_cell(-1)], label="top = -1 : empty", badges=["ST1"]),
    f([stack_cells([10], 0), top_cell(0)], label="push 10 : top = 0", badges=["ST2"], arrows=[("1:0", "0:0")]),
    f([stack_cells([10, 20, 30, 40, 50], 4), top_cell(4)], label="push 20, 30, 40, 50 : top = 4, full", badges=["ST3"], arrows=[("1:0", "0:4")]),
    f([stack_cells([10, 20, 30, 40, 50], 4), top_cell(4)], label="push 60 ? No room: stack overflow, refuse it", badges=["overflow"], arrows=[("1:0", "0:4")]),
    f([stack_cells([10, 20, 30, 40], 3), top_cell(3)], label="pop : 50 comes out first (last in, first out)", badges=["ST5"], arrows=[("1:0", "0:3")]),
    f([stack_cells([]), top_cell(-1)], label="pop 40, 30, 20, 10 ... pop again? Stack underflow", badges=["underflow"]),
])

def ring(vals, frontidx=None, rearidx=None, free=()):
    cells = []
    for i in range(SLOTS):
        v = vals.get(i)
        cells.append(c(v if v is not None else "·", index=i, mark=("zero" if v is None else None)))
    return g(cells, name="queue[5] (circular)")
put(83, 6, [
    f([ring({0: 10, 1: 20, 2: 30}), g([c(0, name="front"), c(2, name="rear")])], label="enqueue 10, 20, 30 : they line up from index 0", badges=["Q1"], arrows=[("1:0", "0:0"), ("1:1", "0:2")]),
    f([ring({1: 20, 2: 30}), g([c(1, name="front", lost=0, mark="hl"), c(2, name="rear")])], label="dequeue : 10 leaves from the front, front moves to index 1", badges=["Q2"], arrows=[("1:0", "0:1"), ("1:1", "0:2")]),
    f([ring({1: 20, 2: 30, 3: 40}), g([c(1, name="front"), c(3, name="rear", lost=2, mark="hl")])], label="enqueue 40 : it goes to index 3", badges=["Q3"], arrows=[("1:0", "0:1"), ("1:1", "0:3")]),
    f([ring({1: 20, 2: 30, 3: 40}), g([c(1, name="front"), c(4, name="rear")])], label="Reached the end of the array with free space at the start?", badges=["Q4"], arrows=[("1:0", "0:1"), ("1:1", "0:4")]),
    f([ring({1: 20, 2: 30, 3: 40}), g([c(1, name="front"), c(0, name="rear", mark="hl", lost=4)])], label="Wrap around to index 0, like a Ferris wheel: circular queue", badges=["Q5"], arrows=[("1:0", "0:1"), ("1:1", "0:0")]),
])

json.dump(D, open(sys.argv[1] if len(sys.argv) > 1 else "boxes_52_83.json", "w"), indent=1, ensure_ascii=False)
print(len(D), "scenes:", ", ".join(sorted(D, key=lambda k: tuple(map(int, k.split("."))))))
