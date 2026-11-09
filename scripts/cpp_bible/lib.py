"""Helpers that build illustration data for the C++ Bible.

Every helper returns a plain dict. Numbers that can be computed are computed here
(sizes, addresses, bar-sort traces), so nobody types them by hand.
Schema: docs/cpp-bible/ILLUSTRATIONS.md
"""
from __future__ import annotations

import re

# Sizes in bytes on a 64-bit machine with GCC (libstdc++).
SIZES = {
    "bool": 1, "char": 1, "signed char": 1, "unsigned char": 1, "short": 2, "int": 4, "unsigned": 4,
    "unsigned int": 4, "long": 8, "long long": 8, "size_t": 8, "float": 4, "double": 8,
    "std::string": 32, "string": 32, "std::vector<int>": 24, "vector<int>": 24,
}
REGION_BASE = {"stack": 0x1000, "heap": 0x5000, "static": 0x9000}


def size_of(type_: str) -> int:
    t = re.sub(r"^(constexpr|const) ", "", type_.strip())
    if t.endswith("*") or t.endswith("&"):
        return 8
    if t.startswith("std::unique_ptr"):
        return 8
    if t.startswith("std::shared_ptr"):
        return 16
    if t in SIZES:
        return SIZES[t]
    raise KeyError(f"unknown size for type {type_!r}: pass bytes=")


def _align(addr: int, n: int) -> int:
    n = min(n, 8)
    return (addr + n - 1) // n * n


def mem(boxes: list, arrows: list | None = None, caption: str = "") -> dict:
    """Memory-boxes illustration.

    box = (name, type, value) or (name, type, value, region) or dict(name=, type=, value=, bytes=, region=)
    Array: type "int[3]" with value "1, 2, 3" expands to name[0], name[1], name[2] in one row.
    A pointer box with value None gets the address of its arrow target.
    arrow = (from_name, to_name, label)
    """
    out: list[dict] = []
    cursor = dict(REGION_BASE)
    for b in boxes:
        if isinstance(b, dict):
            d = dict(b)
        else:
            d = dict(zip(("name", "type", "value", "region"), b))
        region = d.get("region", "stack")
        m = re.fullmatch(r"(.+)\[(\d+)\]", d["type"])
        if m:
            elem, count = m.group(1), int(m.group(2))
            vals = [v.strip() for v in str(d["value"]).split(",")]
            assert len(vals) == count, f"{d['name']}: {len(vals)} values for {count} elements"
            n = d.get("bytes", size_of(elem))
            for i, v in enumerate(vals):
                addr = _align(cursor[region], n)
                out.append({"id": f"{d['name']}[{i}]", "name": f"{d['name']}[{i}]", "type": elem, "value": v,
                            "bytes": n, "addr": f"0x{addr:04X}", "region": region})
                cursor[region] = addr + n
            continue
        n = d.get("bytes") or size_of(d["type"])
        addr = _align(cursor[region], n)
        out.append({"id": d["name"], "name": d["name"], "type": d["type"], "value": d.get("value"),
                    "bytes": n, "addr": f"0x{addr:04X}", "region": region})
        cursor[region] = addr + n
    by_id = {x["id"]: x for x in out}
    arr: list[dict] = []
    for a in arrows or []:
        f, t, label = a
        assert f in by_id and t in by_id, f"arrow {a} names a box that does not exist"
        arr.append({"from": f, "to": t, "label": label})
        if by_id[f]["value"] is None:
            by_id[f]["value"] = by_id[t]["addr"]
    for x in out:
        assert x["value"] is not None, f"box {x['id']} has no value"
        x["value"] = str(x["value"])
    return {"kind": "memory", "addressesAreIllustrative": True, "caption": caption, "boxes": out, "arrows": arr}


def flow(steps: list[tuple[str, str]], caption: str = "") -> dict:
    """Left-to-right (or top-to-bottom) steps: (label, detail)."""
    return {"kind": "flow", "caption": caption,
            "steps": [{"id": f"s{i + 1}", "label": l, "detail": d} for i, (l, d) in enumerate(steps)]}


def graph(nodes: list[tuple], edges: list[tuple], layout: str = "row", caption: str = "") -> dict:
    """nodes (id, label[, sub]); edges (from, to[, label]); layout row | column | tree."""
    ns = [{"id": n[0], "label": n[1], "sub": (n[2] if len(n) > 2 else "")} for n in nodes]
    ids = {n["id"] for n in ns}
    es = []
    for e in edges:
        assert e[0] in ids and e[1] in ids, f"edge {e} names a node that does not exist"
        es.append({"from": e[0], "to": e[1], "label": e[2] if len(e) > 2 else ""})
    return {"kind": "graph", "layout": layout, "caption": caption, "nodes": ns, "edges": es}


def table(headers: list[str], rows: list[list[str]], caption: str = "") -> dict:
    for r in rows:
        assert len(r) == len(headers), f"row {r} has the wrong number of cells"
    return {"kind": "table", "caption": caption, "headers": headers, "rows": rows}


def callstack(steps: list[tuple[list[str], str]], caption: str = "") -> dict:
    """steps: ([frame, frame, ...] bottom first, note). A frame is like 'main()' or 'fact(n=3)'."""
    return {"kind": "callstack", "caption": caption,
            "steps": [{"step": i + 1, "frames": f, "note": n} for i, (f, n) in enumerate(steps)]}


def trace(algorithm: str, array: list[int]) -> dict:
    """Bar-chart trace for bubble, selection or insertion sort. 'array' is the state BEFORE the step."""
    a = list(array)
    steps: list[dict] = []

    def add(compare=None, swap=None, sorted_=None):
        s = {"step": len(steps) + 1, "array": list(a)}
        if compare:
            s["compare"] = list(compare)
        if swap:
            s["swap"] = list(swap)
        s["sorted"] = list(sorted_ or [])
        steps.append(s)

    n = len(a)
    if algorithm == "bubble":
        done: list[int] = []
        for end in range(n - 1, 0, -1):
            for i in range(end):
                add(compare=(i, i + 1), sorted_=done)
                if a[i] > a[i + 1]:
                    add(compare=(i, i + 1), swap=(i, i + 1), sorted_=done)
                    a[i], a[i + 1] = a[i + 1], a[i]
            done = [end] + done
        done = [0] + done
        add(sorted_=done)
    elif algorithm == "selection":
        done = []
        for i in range(n - 1):
            m = i
            for j in range(i + 1, n):
                add(compare=(m, j), sorted_=done)
                if a[j] < a[m]:
                    m = j
            if m != i:
                add(compare=(i, m), swap=(i, m), sorted_=done)
                a[i], a[m] = a[m], a[i]
            done = done + [i]
        add(sorted_=done + [n - 1])
    elif algorithm == "insertion":
        for i in range(1, n):
            j = i
            while j > 0:
                add(compare=(j - 1, j), sorted_=list(range(i)))
                if a[j - 1] > a[j]:
                    add(compare=(j - 1, j), swap=(j - 1, j), sorted_=list(range(i)))
                    a[j - 1], a[j] = a[j], a[j - 1]
                    j -= 1
                else:
                    break
        add(sorted_=list(range(n)))
    else:
        raise ValueError(algorithm)
    assert a == sorted(a)
    return {"kind": "trace", "algorithm": algorithm, "caption": "", "steps": steps,
            "counters": {"compares": sum(1 for s in steps if "compare" in s and "swap" not in s),
                         "swaps": sum(1 for s in steps if "swap" in s)}}
