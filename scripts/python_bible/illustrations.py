"""Structured illustration specs for the Python Bible (Concept slide scenes, scene 4).

One entry per episode that has a drawn explanation. Rules: docs/python-bible/ILLUSTRATIONS.md.
Validated by scripts/check_illustrations.py. Grid: 12 columns (0-11) by 6 rows (0-5).
"""
from __future__ import annotations


def O(id: str, shape: str, text: str, colour: str, col: int, row: int, w: int = 2, h: int = 1) -> dict:
    return {"id": id, "shape": shape, "text": text, "colour": colour, "col": col, "row": row, "w": w, "h": h}


def A(id: str, src: str, dst: str, colour: str = "ink", text: str = "") -> dict:
    return {"id": id, "shape": "arrow", "text": text, "colour": colour, "from": src, "to": dst}


def S(t: float, do: str, target: str, sfx: str = "", **kw) -> dict:
    d = {"t": t, "do": do, "target": target}
    if sfx:
        d["sfx"] = sfx
    d.update(kw)
    return d


def flow(*pairs):
    return list(pairs)


ILL: dict[int, dict] = {}

# ---- M2
ILL[13] = dict(objects=[
    O("q", "box", "temperature > 30 ?", "butter", 4, 0, 4), O("yes", "box", "Hot day, Drink water", "mint", 1, 2, 4),
    O("no", "box", "Pleasant day", "peach", 7, 2, 4), O("end", "box", "Enjoy the beach", "pastelBlue", 4, 4, 4),
    A("a1", "q", "yes", text="True"), A("a2", "q", "no", text="False"), A("a3", "yes", "end"), A("a4", "no", "end")],
    steps=[S(0.0, "show", "q", "pop"), S(0.1, "show", "yes"), S(0.1, "show", "no"), S(0.1, "show", "end"), S(0.25, "glow", "q", "ding"),
           S(0.4, "draw", "a1", "whoosh"), S(0.4, "draw", "a2"), S(0.45, "glow", "yes", "ding"), S(0.45, "dim", "no"), S(0.7, "draw", "a3", "whoosh"), S(0.7, "draw", "a4"), S(0.8, "glow", "end", "ding")])
ILL[15] = dict(objects=[
    O("r1", "card", "True and True gives True", "mint", 1, 0, 6), O("r2", "card", "True and False gives False", "peach", 1, 1, 6),
    O("r3", "card", "False and True gives False", "peach", 1, 2, 6), O("r4", "card", "False and False gives False", "peach", 1, 3, 6),
    O("f", "card", "Falsy values", "butter", 8, 0, 3, 1),
    O("z1", "token", "0", "cream", 8, 1, 1), O("z2", "token", "empty text", "cream", 9, 1, 2), O("z3", "token", "empty list", "cream", 8, 2, 2), O("z4", "token", "None", "cream", 10, 2, 1)],
    steps=[S(0.0, "show", "r1", "pop"), S(0.08, "show", "r2", "pop"), S(0.16, "show", "r3", "pop"), S(0.24, "show", "r4", "pop"),
           S(0.3, "glow", "r1", "ding"), S(0.4, "glow", "r2"), S(0.5, "glow", "r3"), S(0.6, "glow", "r4"),
           S(0.7, "show", "f", "pop"), S(0.72, "show", "z1"), S(0.74, "show", "z2"), S(0.76, "show", "z3"), S(0.78, "show", "z4"),
           S(0.82, "cross", "z1", "buzzer"), S(0.86, "cross", "z2", "buzzer"), S(0.9, "cross", "z3", "buzzer"), S(0.94, "cross", "z4", "buzzer")])
ILL[19] = dict(objects=[O(f"c{r}{c}", "box", f"row {r + 1}, col {c + 1}", "cream", 3 + c * 2, 1 + r * 2, 2) for r in range(2) for c in range(3)],
    steps=[S(0.0, "show", "c00", "pop")] + [S(0.0, "show", f"c{r}{c}") for r in range(2) for c in range(3) if (r, c) != (0, 0)] +
          [S(0.15 + 0.12 * i, "glow", f"c{r}{c}", "key-tick") for i, (r, c) in enumerate([(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2)])])
ILL[22] = dict(objects=[
    O("ask", "box", "Ask for a guess", "butter", 4, 0, 4), O("low", "box", "Too low", "peach", 0, 2, 3), O("high", "box", "Too high", "peach", 4, 2, 3),
    O("ok", "box", "Correct, break", "mint", 8, 2, 3), O("back", "box", "Loop again", "pastelBlue", 4, 4, 4),
    A("a1", "ask", "low"), A("a2", "ask", "high"), A("a3", "ask", "ok"), A("a4", "low", "back"), A("a5", "high", "back")],
    steps=[S(0.0, "show", "ask", "pop"), S(0.05, "show", "low"), S(0.05, "show", "high"), S(0.05, "show", "ok"), S(0.05, "show", "back"),
           S(0.2, "glow", "ask", "ding"), S(0.3, "draw", "a1", "whoosh"), S(0.3, "draw", "a2"), S(0.35, "glow", "low"), S(0.5, "draw", "a4", "whoosh"), S(0.5, "draw", "a5"), S(0.55, "glow", "back"),
           S(0.7, "draw", "a3", "whoosh"), S(0.75, "glow", "ok", "chime"), S(0.75, "dim", "high")])

# ---- M5
_call = dict(objects=[
    O("call", "box", "answer = double(4)", "butter", 0, 4, 4), O("def", "box", "def double(n): return n * 2", "cream", 6, 1, 5),
    O("body", "box", "return 8", "mint", 6, 3, 3), A("a1", "call", "def"), A("a2", "body", "call", "tomato", "back with 8")],
    steps=[S(0.0, "show", "call", "pop"), S(0.05, "show", "def"), S(0.05, "show", "body"), S(0.2, "draw", "a1", "whoosh"), S(0.35, "glow", "def", "ding"),
           S(0.5, "glow", "body", "key-tick"), S(0.7, "draw", "a2", "whoosh"), S(0.85, "glow", "call", "ding")])
ILL[41] = _call
ILL[50] = _call
ILL[43] = dict(objects=[
    O("c1", "card", 'greet("Asha")', "cream", 0, 1, 3), O("c2", "card", 'greet("Ravi", "Namaste")', "cream", 4, 1, 4), O("c3", "card", 'greet(greeting="Hi", name="Meera")', "cream", 4, 3, 4),
    O("d", "token", "default: Hello", "butter", 0, 3, 3)],
    steps=[S(0.0, "show", "c1", "pop"), S(0.0, "show", "c2"), S(0.0, "show", "c3"), S(0.0, "show", "d"), S(0.2, "glow", "d", "ding"), S(0.3, "glow", "c1"),
           S(0.5, "dim", "d"), S(0.55, "glow", "c2", "ding"), S(0.75, "glow", "c3", "ding")])
ILL[44] = dict(objects=[
    O("v1", "token", "1", "butter", 0, 1, 1), O("v2", "token", "2", "butter", 1, 2, 1), O("v3", "token", "3", "butter", 2, 1, 1), O("net", "box", "numbers = (1, 2, 3)", "mint", 4, 1, 4),
    O("lst", "card", "[10, 20]", "cream", 0, 4, 3), O("p1", "box", "a = 10", "peach", 6, 3, 2), O("p2", "box", "b = 20", "peach", 6, 4, 2)],
    steps=[S(0.0, "show", "v1", "pop"), S(0.0, "show", "v2"), S(0.0, "show", "v3"), S(0.15, "move", "v1", "whoosh", to=[4, 1]), S(0.15, "move", "v2", to=[5, 1]), S(0.15, "move", "v3", to=[6, 1]),
           S(0.3, "show", "net", "pop"), S(0.5, "show", "lst", "pop"), S(0.65, "flip", "lst", "whoosh"), S(0.75, "show", "p1", "ding"), S(0.85, "show", "p2", "ding")])
ILL[46] = dict(objects=[
    O("t1", "token", "1", "butter", 0, 2, 1), O("t2", "token", "2", "butter", 0, 3, 1), O("t3", "token", "3", "butter", 0, 4, 1), O("t4", "token", "4", "butter", 0, 5, 1),
    O("tr", "box", "n * 2", "lilac", 3, 3, 2), O("gate", "box", "keep if even", "mint", 7, 3, 3), O("out", "card", "[2, 4]", "cream", 9, 5, 2)],
    steps=[S(0.0, "show", "tr", "pop"), S(0.0, "show", "gate"), S(0.05, "show", "t1"), S(0.05, "show", "t2"), S(0.05, "show", "t3"), S(0.05, "show", "t4"),
           S(0.25, "move", "t1", "whoosh", to=[3, 2]), S(0.4, "move", "t1", to=[7, 2]), S(0.5, "move", "t2", to=[7, 3]), S(0.6, "cross", "t3", "buzzer"), S(0.7, "show", "out", "ding")])
ILL[47] = dict(objects=[
    O("f1", "box", "factorial(1) = 1", "mint", 4, 0, 4), O("f2", "box", "factorial(2) = 2 * factorial(1)", "butter", 4, 1, 4), O("f3", "box", "factorial(3) = 3 * factorial(2)", "butter", 4, 2, 4),
    O("f4", "box", "factorial(4) = 4 * factorial(3)", "butter", 4, 3, 4), O("f5", "box", "factorial(5) = 5 * factorial(4)", "butter", 4, 4, 4)],
    steps=[S(0.0, "show", "f5", "pop"), S(0.12, "show", "f4", "pop"), S(0.24, "show", "f3", "pop"), S(0.36, "show", "f2", "pop"), S(0.48, "show", "f1", "pop"),
           S(0.55, "glow", "f1", "ding"), S(0.62, "hide", "f1", "pop"), S(0.7, "hide", "f2", "pop"), S(0.78, "hide", "f3", "pop"), S(0.86, "hide", "f4", "pop"), S(0.94, "glow", "f5", "chime")])
ILL[48] = dict(objects=[
    O("sig", "box", "def area(width: float, height: float) -> float:", "cream", 1, 1, 10), O("doc", "box", '"""Return the area of a rectangle."""', "cream", 1, 3, 10),
    O("n1", "label", "hint for a parameter", "butter", 2, 0, 3), O("n2", "label", "hint for the result", "butter", 8, 0, 3), O("n3", "label", "docstring", "butter", 4, 5, 3),
    A("a1", "n1", "sig"), A("a2", "n2", "sig"), A("a3", "n3", "doc")],
    steps=[S(0.0, "show", "sig", "pop"), S(0.0, "show", "doc"), S(0.2, "show", "n1", "pop"), S(0.25, "draw", "a1", "marker-swipe"), S(0.5, "show", "n2", "pop"), S(0.55, "draw", "a2", "marker-swipe"),
           S(0.75, "show", "n3", "pop"), S(0.8, "draw", "a3", "marker-swipe")])
ILL[49] = dict(objects=[
    O("fn", "card", "double", "cream", 0, 1, 2), O("apply", "box", "apply(func, value)", "butter", 5, 1, 4), O("call", "card", "double(5)", "cream", 0, 4, 2), O("num", "token", "10", "mint", 5, 4, 1)],
    steps=[S(0.0, "show", "fn", "pop"), S(0.0, "show", "apply"), S(0.2, "move", "fn", "whoosh", to=[5, 2]), S(0.4, "glow", "apply", "ding"), S(0.55, "show", "call", "pop"),
           S(0.75, "flip", "call", "pop"), S(0.85, "show", "num", "ding")])

# ---- M6
ILL[52] = dict(objects=[O("d", "box", "Diary", "cream", 4, 0, 4, 3), O("p1", "token", "Day 1", "butter", 4, 1, 1), O("p2", "token", "Day 2", "butter", 5, 1, 1),
    O("w", "label", 'open("log.txt", "w")', "tomato", 0, 4, 4), O("a", "label", 'open("log.txt", "a")', "mint", 6, 4, 4), O("p3", "token", "Day 3", "mint", 6, 1, 1)],
    steps=[S(0.0, "show", "d", "pop"), S(0.05, "show", "p1"), S(0.05, "show", "p2"), S(0.25, "show", "w", "pop"), S(0.35, "hide", "p1", "whoosh"), S(0.35, "hide", "p2"),
           S(0.6, "show", "a", "pop"), S(0.7, "show", "p1"), S(0.7, "show", "p2"), S(0.8, "show", "p3", "ding")])
ILL[53] = dict(objects=[O("prog", "box", "Program", "cream", 0, 2, 3), O("file", "box", "notes.txt", "butter", 8, 2, 3), O("lock", "token", "open", "tomato", 6, 1, 1),
    A("a1", "prog", "file", text="with open"), A("a2", "file", "prog", text="text")],
    steps=[S(0.0, "show", "prog", "pop"), S(0.0, "show", "file"), S(0.2, "draw", "a1", "whoosh"), S(0.3, "show", "lock", "key-tick"), S(0.5, "draw", "a2", "whoosh"),
           S(0.75, "hide", "lock", "ding")])
ILL[54] = dict(objects=[O("l1", "box", "line 1: n = int(text)", "cream", 0, 1, 4), O("l2", "box", "line 2: print(n)", "cream", 0, 2, 4), O("ex", "box", "except ValueError", "mint", 6, 2, 4),
    O("next", "box", "program continues", "pastelBlue", 6, 4, 4), O("bolt", "token", "error", "tomato", 4, 1, 1), A("a1", "bolt", "ex"), A("a2", "ex", "next")],
    steps=[S(0.0, "show", "l1", "pop"), S(0.0, "show", "l2"), S(0.0, "show", "ex"), S(0.0, "show", "next"), S(0.2, "show", "bolt", "buzzer"), S(0.3, "shake", "l1"), S(0.35, "dim", "l2"),
           S(0.5, "draw", "a1", "whoosh"), S(0.6, "glow", "ex", "ding"), S(0.8, "draw", "a2", "whoosh"), S(0.9, "glow", "next")])
ILL[55] = dict(objects=[O("fn", "box", "function set_age", "cream", 0, 3, 3), O("ex", "box", "except ValueError", "mint", 4, 0, 4), O("pass", "box", "no match: program stops", "peach", 8, 3, 3),
    A("a1", "fn", "ex", "tomato", "raise ValueError"), A("a2", "fn", "pass", "tomato", "other error")],
    steps=[S(0.0, "show", "fn", "pop"), S(0.0, "show", "ex"), S(0.0, "show", "pass"), S(0.25, "draw", "a1", "buzzer"), S(0.4, "glow", "ex", "ding"), S(0.6, "draw", "a2", "whoosh"), S(0.75, "glow", "pass", "buzzer")])
ILL[56] = dict(objects=[O("b1", "box", "1. your own folder", "cream", 1, 0, 4), O("b2", "box", "2. standard library", "cream", 1, 2, 4), O("b3", "box", "3. installed packages", "cream", 1, 4, 4),
    O("hit", "token", "found", "mint", 7, 2, 2), A("a1", "b1", "b2"), A("a2", "b2", "b3")],
    steps=[S(0.0, "show", "b1", "pop"), S(0.0, "show", "b2"), S(0.0, "show", "b3"), S(0.2, "glow", "b1", "key-tick"), S(0.4, "draw", "a1", "whoosh"), S(0.5, "glow", "b2", "key-tick"),
           S(0.55, "draw", "a2", "whoosh"), S(0.65, "show", "hit", "ding"), S(0.7, "dim", "b3")])
ILL[57] = dict(objects=[O("left", "card", "run directly: __name__ is __main__", "mint", 0, 1, 5, 2), O("right", "card", "imported: __name__ is shape", "peach", 6, 1, 5, 2),
    O("g1", "token", "guarded line runs", "butter", 1, 4, 4), O("g2", "token", "guarded line skipped", "cream", 7, 4, 4)],
    steps=[S(0.0, "show", "left", "pop"), S(0.0, "show", "right"), S(0.3, "flip", "left", "pop"), S(0.4, "show", "g1", "ding"), S(0.6, "flip", "right", "pop"), S(0.7, "show", "g2"), S(0.7, "dim", "g2")])
ILL[58] = dict(objects=[O("p1", "box", "project one: requests 2.x", "mint", 0, 1, 4), O("p2", "box", "project two: requests 3.x", "lilac", 5, 1, 4), O("g", "box", "global Python (unchanged)", "cream", 2, 4, 6)],
    steps=[S(0.0, "show", "g", "pop"), S(0.3, "show", "p1", "pop"), S(0.6, "show", "p2", "pop"), S(0.85, "glow", "g")])
ILL[59] = dict(objects=[O("h", "card", "name, marks", "butter", 0, 0, 4), O("r1", "card", "Asha, 80", "cream", 0, 2, 4), O("r2", "card", "Ravi, 92", "cream", 0, 3, 4),
    O("d1", "card", '{"name": "Asha", "marks": "80"}', "mint", 6, 2, 5), O("d2", "card", '{"name": "Ravi", "marks": "92"}', "mint", 6, 3, 5)],
    steps=[S(0.0, "show", "h", "pop"), S(0.1, "show", "r1"), S(0.1, "show", "r2"), S(0.3, "move", "r1", "whoosh", to=[6, 2]), S(0.4, "flip", "r1", "pop"), S(0.45, "show", "d1"),
           S(0.6, "move", "r2", "whoosh", to=[6, 3]), S(0.7, "flip", "r2", "pop"), S(0.75, "show", "d2")])
ILL[60] = dict(objects=[O("load", "box", "load", "pastelBlue", 0, 1, 3), O("change", "box", "change", "butter", 4, 1, 3), O("save", "box", "save", "mint", 8, 1, 3),
    O("file", "card", "contacts.json", "cream", 4, 4, 3), A("a1", "load", "change"), A("a2", "change", "save"), A("a3", "save", "load", text="next run")],
    steps=[S(0.0, "show", "file", "pop"), S(0.1, "show", "load"), S(0.1, "show", "change"), S(0.1, "show", "save"), S(0.3, "draw", "a1", "whoosh"), S(0.5, "draw", "a2", "whoosh"),
           S(0.7, "draw", "a3", "whoosh"), S(0.85, "glow", "file", "ding")])

# ---- M7
ILL[61] = dict(objects=[O("c1", "box", "names: Asha, Ravi, Meera", "cream", 0, 0, 5), O("c2", "box", "marks: 91, 78, 85", "cream", 6, 0, 5),
    O("pair", "label", "match by position", "butter", 4, 2, 4),
    O("f1", "card", "Student: Asha, 91", "mint", 1, 4, 3), O("f2", "card", "Student: Ravi, 78", "mint", 4, 4, 3), O("f3", "card", "Student: Meera, 85", "mint", 7, 4, 3)],
    steps=[S(0.0, "show", "c1", "pop"), S(0.0, "show", "c2"), S(0.25, "show", "pair", "pop"), S(0.5, "hide", "c1", "whoosh"), S(0.5, "hide", "c2"), S(0.5, "hide", "pair"),
           S(0.6, "show", "f1", "pop"), S(0.7, "show", "f2", "pop"), S(0.8, "show", "f3", "pop")])
ILL[67] = dict(objects=[O("an", "box", "Animal: name, eat()", "butter", 4, 0, 4), O("dog", "box", "Dog: bark()", "mint", 1, 3, 3), O("cat", "box", "Cat: meow()", "lilac", 8, 3, 3),
    A("a1", "an", "dog", text="inherits"), A("a2", "an", "cat", text="inherits")],
    steps=[S(0.0, "show", "an", "pop"), S(0.3, "show", "dog", "pop"), S(0.3, "show", "cat"), S(0.5, "draw", "a1", "whoosh"), S(0.5, "draw", "a2"), S(0.8, "glow", "dog", "ding")])
ILL[68] = dict(objects=[O("dog", "box", "Dog: speak()", "mint", 1, 3, 4), O("an", "box", "Animal: speak(), eat()", "butter", 1, 0, 4), O("s", "token", "search: eat", "tomato", 6, 3, 2), A("a1", "dog", "an", text="not here, look up")],
    steps=[S(0.0, "show", "an", "pop"), S(0.0, "show", "dog"), S(0.2, "show", "s", "pop"), S(0.4, "shake", "dog", "buzzer"), S(0.6, "draw", "a1", "whoosh"), S(0.8, "glow", "an", "ding")])
ILL[70] = dict(objects=[O("vault", "box", "_marks = 91 (private)", "darkBlue", 8, 2, 3), O("clerk", "box", "property: check first", "butter", 4, 2, 3),
    O("ok", "card", "set marks = 95", "mint", 0, 1, 3), O("bad", "card", "set marks = -5", "peach", 0, 3, 3)],
    steps=[S(0.0, "show", "vault", "pop"), S(0.0, "show", "clerk"), S(0.25, "show", "ok", "pop"), S(0.35, "move", "ok", "whoosh", to=[4, 1]), S(0.45, "stamp", "ok", "stamp"),
           S(0.55, "show", "bad", "pop"), S(0.65, "move", "bad", "whoosh", to=[4, 3]), S(0.75, "cross", "bad", "buzzer")])

# ---- M8
ILL[74] = dict(objects=[O("fn", "box", "def countdown(n): ... yield n ...", "cream", 1, 1, 6, 2), O("bm", "token", "bookmark", "tomato", 7, 1, 1), O("t1", "token", "3", "butter", 8, 4, 1),
    O("t2", "token", "2", "butter", 9, 4, 1), O("t3", "token", "1", "butter", 10, 4, 1)],
    steps=[S(0.0, "show", "fn", "pop"), S(0.1, "show", "bm"), S(0.25, "show", "t1", "pop"), S(0.3, "glow", "bm", "key-tick"), S(0.5, "show", "t2", "pop"), S(0.55, "glow", "bm", "key-tick"),
           S(0.75, "show", "t3", "pop"), S(0.8, "glow", "bm", "key-tick")])
ILL[75] = dict(objects=[O("shelf", "box", "[n * n ...] five boxes ready", "cream", 0, 1, 5, 2), O("belt", "box", "(n * n ...) one box at a time", "mint", 6, 1, 5, 2),
    O("sum", "card", "sum meter: 55", "butter", 6, 4, 4)],
    steps=[S(0.0, "show", "shelf", "pop"), S(0.3, "show", "belt", "pop"), S(0.5, "glow", "belt", "key-tick"), S(0.65, "glow", "belt", "key-tick"), S(0.8, "show", "sum", "ding")])
ILL[76] = dict(objects=[O("wrap", "box", "wrapper", "butter", 3, 1, 5, 3), O("orig", "box", "hello (original)", "cream", 4, 2, 3), O("name", "label", "name: hello", "tomato", 0, 0, 3)],
    steps=[S(0.0, "show", "orig", "pop"), S(0.0, "show", "name"), S(0.3, "show", "wrap", "whoosh"), S(0.5, "move", "name", "whoosh", to=[3, 0]), S(0.7, "glow", "wrap", "ding")])
ILL[77] = dict(objects=[O("dial", "box", "repeat(3): dial = 3", "butter", 0, 0, 4), O("gift", "card", "hello", "cream", 0, 3, 2), O("mach", "box", "decorator", "lilac", 5, 2, 3),
    O("wrapped", "card", "hello (wrapped)", "mint", 9, 3, 2)],
    steps=[S(0.0, "show", "dial", "pop"), S(0.15, "glow", "dial", "ding"), S(0.25, "show", "mach", "pop"), S(0.35, "show", "gift", "pop"), S(0.5, "move", "gift", "whoosh", to=[5, 3]),
           S(0.7, "move", "gift", to=[9, 3]), S(0.8, "show", "wrapped", "ding")])
ILL[78] = dict(objects=[O("in", "box", "door in: __enter__", "mint", 0, 2, 3), O("room", "box", "with block", "cream", 4, 2, 3), O("out", "box", "door out: __exit__", "mint", 8, 2, 3),
    O("err", "token", "error", "tomato", 5, 0, 2), A("a1", "in", "room"), A("a2", "room", "out"), A("a3", "err", "out", "tomato")],
    steps=[S(0.0, "show", "in", "pop"), S(0.0, "show", "room"), S(0.0, "show", "out"), S(0.2, "glow", "in", "ding"), S(0.3, "draw", "a1", "whoosh"), S(0.5, "show", "err", "buzzer"),
           S(0.6, "draw", "a3", "whoosh"), S(0.75, "draw", "a2"), S(0.85, "glow", "out", "ding")])
ILL[79] = dict(objects=[O("j1", "box", "int", "peach", 0, 2, 2), O("j2", "box", "str", "peach", 3, 2, 2), O("j3", "box", "float", "peach", 6, 2, 2), O("s", "token", '"a"', "butter", 6, 0, 1),
    O("mypy", "box", "mypy checker", "lilac", 9, 2, 2)],
    steps=[S(0.0, "show", "j1", "pop"), S(0.0, "show", "j2"), S(0.0, "show", "j3"), S(0.25, "show", "s", "pop"), S(0.4, "move", "s", "whoosh", to=[6, 2]), S(0.6, "show", "mypy", "pop"), S(0.75, "cross", "s", "buzzer")])
ILL[80] = dict(objects=[O("t1", "card", "test_small", "cream", 0, 1, 3), O("t2", "card", "test_negative", "cream", 4, 1, 3), O("t3", "card", "test_text", "cream", 8, 1, 3), O("t4", "card", "test_bug", "cream", 4, 3, 3),
    O("msg", "label", "3 != 5", "peach", 8, 4, 2)],
    steps=[S(0.0, "show", "t1", "pop"), S(0.0, "show", "t2"), S(0.0, "show", "t3"), S(0.0, "show", "t4"), S(0.2, "tick", "t1", "ding"), S(0.35, "tick", "t2", "ding"), S(0.5, "tick", "t3", "ding"),
           S(0.7, "cross", "t4", "buzzer"), S(0.8, "show", "msg", "pop")])

# ---- M9
ILL[85] = dict(objects=[O("p1", "token", "data", "butter", 0, 1, 2), O("p2", "token", "log.txt", "butter", 3, 1, 2), O("joined", "card", "data/log.txt", "mint", 1, 3, 4),
    O("win", "box", "Windows: data\\log.txt", "pastelBlue", 6, 3, 5), O("lin", "box", "Mac and Linux: data/log.txt", "pastelBlue", 6, 4, 5)],
    steps=[S(0.0, "show", "p1", "pop"), S(0.0, "show", "p2"), S(0.3, "move", "p1", "whoosh", to=[1, 3]), S(0.3, "move", "p2", to=[3, 3]), S(0.5, "show", "joined", "stamp"),
           S(0.7, "show", "win", "pop"), S(0.85, "show", "lin", "pop")])
ILL[86] = dict(objects=[O("cmd", "card", "python greet.py Asha 3", "darkBlue", 1, 0, 8),
    O("s0", "box", "0: greet.py", "cream", 1, 3, 3), O("s1", "box", "1: Asha", "cream", 4, 3, 3), O("s2", "box", "2: 3", "cream", 7, 3, 3)],
    steps=[S(0.0, "show", "cmd", "key-tick"), S(0.4, "show", "s0", "pop"), S(0.55, "show", "s1", "pop"), S(0.7, "show", "s2", "pop"), S(0.85, "glow", "s2", "ding")])

# ---- M10
ILL[87] = dict(objects=[O("list", "card", "list of Expense cards", "butter", 4, 2, 4), O("add", "box", "add", "mint", 0, 0, 3), O("show", "box", "list", "mint", 8, 0, 3),
    O("sum", "box", "summary", "mint", 0, 4, 3), O("save", "box", "save", "mint", 8, 4, 3),
    A("a1", "add", "list"), A("a2", "list", "show"), A("a3", "list", "sum"), A("a4", "list", "save")],
    steps=[S(0.0, "show", "list", "pop"), S(0.2, "show", "add"), S(0.3, "draw", "a1", "whoosh"), S(0.4, "show", "show"), S(0.5, "draw", "a2", "whoosh"), S(0.6, "show", "sum"), S(0.7, "draw", "a3", "whoosh"),
           S(0.8, "show", "save"), S(0.9, "draw", "a4", "whoosh")])
ILL[88] = dict(objects=[O("scale", "box", "float: 0.29 * 100 = 28.999999", "peach", 0, 1, 5), O("coins", "box", "cents: 29 whole coins", "mint", 6, 1, 5), O("x", "token", "lost 1 cent", "tomato", 1, 4, 3)],
    steps=[S(0.0, "show", "scale", "pop"), S(0.3, "show", "x", "buzzer"), S(0.5, "show", "coins", "pop"), S(0.7, "hide", "x"), S(0.85, "glow", "coins", "ding")])
ILL[89] = dict(objects=[O("rope", "box", "your code", "cream", 1, 1, 9), O("net", "box", "tests (safety net)", "mint", 1, 4, 9), O("fall", "token", "red cross card", "tomato", 5, 0, 2)],
    steps=[S(0.0, "show", "rope", "pop"), S(0.0, "show", "net"), S(0.3, "shake", "rope", "buzzer"), S(0.45, "show", "fall", "pop"), S(0.6, "move", "fall", "whoosh", to=[5, 3]), S(0.8, "glow", "net", "ding")])
ILL[90] = dict(objects=[O("web", "box", "web: Flask", "pastelBlue", 0, 1, 3), O("data", "box", "data: pandas", "mint", 4, 1, 3), O("game", "box", "games: pygame", "lilac", 8, 1, 3),
    O("auto", "box", "automation: scripts", "butter", 2, 4, 3), O("test", "box", "testing: pytest", "apricot", 7, 4, 3)],
    steps=[S(0.1, "show", "web", "pop"), S(0.1, "glow", "web", "key-tick"), S(0.3, "show", "data", "pop"), S(0.3, "glow", "data", "key-tick"), S(0.5, "show", "game", "pop"), S(0.5, "glow", "game", "key-tick"),
           S(0.7, "show", "auto", "pop"), S(0.7, "glow", "auto", "key-tick"), S(0.9, "show", "test", "pop"), S(0.9, "glow", "test", "key-tick")])
