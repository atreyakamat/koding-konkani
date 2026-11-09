"""Module 9 — Standard library and data (EP 81-86)."""

MODULE = {"id": 9, "name": "Standard library and data", "range": "81–86", "colours": "Cream + Tomato"}
EPISODES = []
NEXT_AFTER = ("Next: EP 87 · Capstone 1: Expense tracker design", "Module nine is done! Next time: we start our capstone project, an expense tracker.")

EPISODES.append(dict(
    n=81, title="Dates and times", spoken="dates and times",
    yt="Python Dates and Times: datetime, strftime, strptime", thumb="DATES + TIMES",
    vis="Xecxec reading a wall calendar and a pocket watch at the same time",
    goals=["create dates and datetimes", "add and subtract time with timedelta", "format and parse text with strftime and strptime"],
    tags=["python datetime", "python strftime", "python strptime", "python timedelta"],
    hash=["#python", "#datetime"],
    analogy="a wall calendar and a pocket watch: one knows the day, the other knows the minute, and both can count forward",
    c_title="Calendar and clock",
    c_pts=["date holds a day; datetime holds a day and a time", "timedelta is a length of time you can add", "strftime writes text; strptime reads text"],
    intro="Birthdays, deadlines, timers. Python's datetime module handles them all, without mistakes.",
    concept="The datetime module has three main tools. A date holds a year, a month and a day. A datetime also holds hours, minutes and seconds. A timedelta is a length of time, such as thirty days, which you can add to a date, or get by subtracting two dates. To turn a date into text, use strftime, with a format string such as percent d percent B. To read text into a date, use strptime, with the same kind of format. Think of a wall calendar and a pocket watch, both able to count forward.",
    A=dict(file="dates.py", label="Dates and timedelta", on="create a date, format it, and add thirty days",
           src='''
from datetime import date, datetime, timedelta

d = date(2025, 1, 15)
print(d)
print(d.year, d.month, d.day)
print(d.strftime("%d %B %Y"))
print(d.strftime("%A"))
later = d + timedelta(days=30)
print(later)
print((later - d).days)
''',
           narr="[HL 1] Import date, datetime and timedelta. [HL 3] A date. The fifteenth of January, twenty twenty five. [HL 4] Printing gives year, month, day. [HL 5] Parts are available as attributes. [HL 6] Strftime formats it. Percent d is the day, percent B the month name, percent Y the year. [HL 7] Percent A is the weekday name. Wednesday. [HL 8] Add a timedelta of thirty days. [HL 9] The fourteenth of February. [HL 10] And subtracting two dates gives a timedelta. Its days are thirty."),
    mem=dict(label="Dates are objects", on="The names d and later tied to two separate date objects; adding a timedelta builds a new one", names=["d", "later"], **{"from": "A"},
             narr="Here is the picture. The name d is tied to one date object. The name later is tied to a different date object. Adding a timedelta did not change d. Dates are immutable. Every calculation builds a new date, and the old one stays exactly as it was."),
    B=dict(file="times.py", label="Parsing text", on="strptime reads text into a datetime",
           src='''
from datetime import datetime

text = "2025-03-09 18:30"
t = datetime.strptime(text, "%Y-%m-%d %H:%M")
print(t.hour, t.minute)
print(t.strftime("%I:%M %p"))
end = datetime(2025, 3, 9, 20, 0)
print(end - t)
print(t < end)
''',
           narr="[HL 1] Import datetime. [HL 3] A date and time, written as text. [HL 4] Strptime reads the text, using a format that matches it exactly. Year, month, day, hour, minute. [HL 5] Now the parts are numbers. Eighteen thirty. [HL 6] Strftime writes it back, in twelve hour style. Six thirty PM. [HL 7] A second datetime, built from numbers. [HL 8] Subtract, and we get a timedelta. One hour, thirty minutes. [HL 9] And datetimes compare with less than. True."),
    term="2025-01-15, then 2025 1 15, 15 January 2025, Wednesday, 2025-02-14, 30. Then 18 30, 06:30 PM, 1:30:00, True.",
    recap=["date holds a day; datetime holds a day and a time.", "timedelta is a length of time; add it, or get it by subtracting.", "strftime turns a date into text.", "strptime turns text into a date; the format must match."],
    bug=dict(title="the wrong format string", trim=1, file="parse.py", wrong='''
from datetime import datetime

d = datetime.strptime("15/01/2025", "%Y-%m-%d")
''', fixed='''
from datetime import datetime

d = datetime.strptime("15/01/2025", "%d/%m/%Y")
print(d.date())
''', wrong_note="the text uses slashes, the format uses dashes", fixed_note="the format matches the text",
             why="strptime needs a format that matches the text exactly, character for character. A different order or different separators raise a ValueError.",
             narr="Bug of the Day. The text is fifteen slash one slash twenty twenty five. The format says year dash month dash day. They do not match. Value error, time data does not match format. The format must describe the text exactly. Day slash month slash year is percent d, slash, percent m, slash, percent Y."),
    pun="Why did the datetime break up with the string? They could never agree on a format.",
    task="count the days", challenge="Print the number of days between 1 January 2025 and 31 December 2025.",
    answer="(date(2025, 12, 31) - date(2025, 1, 1)).days, which is 364.",
    shorts=[
        ("date and datetime", "A date holds a year, a month and a day. A datetime holds a time as well, hours, minutes and seconds. Create one with numbers, such as date, twenty twenty five, one, fifteen. Printing gives a tidy year, month, day.", "date(2025, 1, 15)", "Dates are objects."),
        ("timedelta", "A timedelta is a length of time. Add timedelta of thirty days to a date, and you get a later date. Subtract two dates, and you get a timedelta, with a days attribute. Python handles months and leap years for you.", "d + timedelta(days=30)", "Python counts days for you."),
        ("strftime", "Strftime turns a date into text. Percent d is the day. Percent B is the month name. Percent Y is the year. Percent A is the weekday. Mix them, and you can write the date in any style you like.", "d.strftime(\"%d %B %Y\")", "strftime writes text."),
        ("strptime", "Strptime does the opposite. It reads text into a datetime, using a format that must match exactly. Slashes in the text need slashes in the format. A mismatch raises a value error, time data does not match format.", "ValueError: does not match format", "The format must match."),
        ("Pun and challenge", "Why did the datetime break up with the string? They could never agree on a format. Your challenge. Print the number of days between the first of January and the thirty first of December, twenty twenty five. Use two dates.", "Challenge: days in 2025", "Subtract two dates."),
    ],
))

EPISODES.append(dict(
    n=82, title="random and math", spoken="random and math",
    yt="Python random and math Modules Explained", thumb="RANDOM + MATH",
    vis="Xecxec rolling a die while a calculator hums nearby",
    goals=["pick random numbers and items", "make random results repeatable with a seed", "use math functions such as sqrt, ceil and gcd"],
    tags=["python random", "python math module", "python random seed", "python randint randrange"],
    hash=["#python", "#random"],
    analogy="a dice and a calculator: one gives surprises, the other gives certainty",
    c_title="Surprise and certainty",
    c_pts=["random.randint(a, b) includes both a and b", "random.seed(n) makes the sequence repeat", "math has sqrt, ceil, floor, pi and more"],
    intro="Games need surprises, and science needs exact answers. Two modules, one for each.",
    concept="The random module gives surprises. Randint takes two numbers and includes both ends. Choice picks one item from a list. Shuffle mixes a list in place. Sample picks several different items. The numbers are only pseudo random, which means they follow a recipe. Seed the recipe with a number, and you get the same sequence every time. That is how we keep our examples repeatable. The math module gives certainty, with functions such as square root, ceiling, floor and gcd.",
    A=dict(file="rand.py", label="Seeded randomness", on="dice, choice, shuffle and sample, repeatable with a seed",
           src='''
import random

random.seed(7)
print(random.randint(1, 6))
print(random.randint(1, 6))
print(random.choice(["tea", "chai", "coffee"]))
items = [1, 2, 3, 4, 5]
random.shuffle(items)
print(items)
print(random.sample(range(1, 50), 3))
''',
           narr="[HL 1] Import random. [HL 3] The seed. With the same seed, the same numbers appear on every run. [HL 4] A die roll, one to six. Both ends are possible. [HL 5] Another roll. [HL 6] Choice picks one item from the list. [HL 7] A list of five numbers. [HL 8] Shuffle mixes it in place. [HL 9] The shuffled list. [HL 10] Sample picks three different numbers from one to forty nine. Remove the seed line, and every run would give different answers."),
    mem=dict(label="Shuffle changes the same list", on="The name items tied to one list; shuffle reorders that very list instead of making a new one", names=["items"], **{"from": "A"},
             narr="Here is the picture. The name items is tied to one list. Shuffle does not build a new list. It mixes the very same list in place. So the name items, tied to that list, now sees the new order. That is why shuffle returns nothing. It changes the list that you already hold."),
    B=dict(file="maths.py", label="The math module", on="exact functions and constants",
           src='''
import math

print(math.sqrt(144))
print(math.ceil(4.2), math.floor(4.8))
print(round(math.pi, 4))
print(math.gcd(12, 18))
print(math.isclose(0.1 + 0.2, 0.3))
print(math.factorial(5))
''',
           narr="[HL 1] Import math. [HL 3] Square root. Twelve point zero. [HL 4] Ceil rounds up, floor rounds down. Five and four. [HL 5] Pi, rounded to four places. Three point one four one six. [HL 6] The greatest common divisor of twelve and eighteen. Six. [HL 7] Is close compares floats safely. True. [HL 8] And factorial of five is one hundred twenty."),
    term="Two dice and a drink, a shuffled list and three numbers; the same every run. Then 12.0, 5 4, 3.1416, 6, True, 120.",
    recap=["random.randint(a, b) includes both a and b.", "random.seed(n) makes the sequence repeat.", "choice, shuffle and sample work on lists.", "math gives sqrt, ceil, floor, gcd, pi and isclose."],
    bug=dict(title="randint includes both ends", kind="output", file="dice.py", wrong='''
import random

random.seed(5)
rolls = {random.randint(1, 3) for _ in range(30)}
print(sorted(rolls))
''', fixed='''
import random

random.seed(5)
rolls = {random.randrange(1, 3) for _ in range(30)}
print(sorted(rolls))
''', wrong_note="the programmer wanted only 1 and 2", fixed_note="randrange leaves out the end, like range",
             why="randint includes both ends, but range, and randrange, stop before the end. Pick the one that matches the numbers you want.",
             narr="Bug of the Day. We wanted rolls of one or two. We wrote randint of one comma three, and three shows up as well. No error. Randint includes both ends. Range does not, and neither does randrange. Use randrange of one comma three, and the three disappears."),
    pun="Why did the random number refuse to join the team? It could not commit.",
    task="a random password", challenge="Use random.choice to build a four letter password from the letters abcdef. Seed the generator so the answer repeats.",
    answer="random.seed(1); \"\".join(random.choice(\"abcdef\") for _ in range(4)).",
    shorts=[
        ("randint", "Randint of one comma six rolls a die. Remember, it includes both ends, so a six is possible. Choice picks one item from a list. Shuffle mixes a list in place, and sample picks several different items.", "random.randint(1, 6)", "Both ends are included."),
        ("Seed", "Random numbers follow a recipe. Seed the recipe with random dot seed, and a number, and you get the same sequence on every run. Perfect for tests, and for videos like this one. Remove the seed, and every run is different.", "random.seed(7)", "Seeds make it repeatable."),
        ("math module", "The math module gives exact answers. Square root, ceil to round up, floor to round down, gcd for the greatest common divisor, and pi. Import math once, and write math dot, and the name.", "math.sqrt, math.ceil, math.pi", "Import math."),
        ("The off by one", "A sneaky one. You want rolls of one or two, and write randint one comma three. Three still appears, because randint includes both ends. Randrange stops before the end, like range. Choose the right one.", "randint(1,3) can return 3", "Check your ends."),
        ("Pun and challenge", "Why did the random number refuse to join the team? It could not commit. Your challenge. Use random dot choice to build a four letter password from the letters a to f. Seed the generator first, so your answer repeats.", "Challenge: random password", "Build a password."),
    ],
))

EPISODES.append(dict(
    n=83, title="collections (Counter, defaultdict, deque)", spoken="collections, counter, default dict and deque",
    yt="Python collections: Counter, defaultdict and deque", thumb="COLLECTIONS",
    vis="Xecxec sorting shells into piles, with a queue of customers behind",
    goals=["count items with Counter", "group items with defaultdict", "use a deque as a queue"],
    tags=["python collections", "python counter", "python defaultdict", "python deque"],
    hash=["#python", "#collections"],
    analogy="three handy tools in a drawer: a tally counter, a sorting tray, and a ticket queue",
    c_title="Three handy tools",
    c_pts=["Counter counts how often each item appears", "defaultdict makes missing keys for you", "deque adds and removes at both ends quickly"],
    intro="Counting words, grouping names, running a queue. The collections module has a tool for each.",
    concept="The collections module has smarter containers. A Counter counts how many times each item appears, and most common gives the top ones. A defaultdict is a dictionary that creates a missing key for you, with a default such as an empty list, so grouping needs no if statement. A deque is a double ended queue. It adds and removes at both ends quickly, which a list cannot do at the front. Think of three handy tools in a drawer. A tally counter, a sorting tray, and a ticket queue.",
    A=dict(file="coll.py", label="Counter and defaultdict", on="count words, then group them by length",
           src='''
from collections import Counter, defaultdict

words = "tea chai tea coffee tea chai".split()
counts = Counter(words)
print(counts)
print(counts.most_common(1))
groups = defaultdict(list)
for w in words:
    groups[len(w)].append(w)
print(dict(groups))
''',
           narr="[HL 1] Import the two tools. [HL 3] Six words. [HL 4] Counter counts each word in one step. [HL 5] Tea three times, chai twice, coffee once. [HL 6] Most common one gives the top entry. Tea, three. [HL 7] A defaultdict whose missing keys start as an empty list. [HL 8] Loop over the words. [HL 9] Group each word by its length. No if statement is needed, because a missing key is created for us. [HL 10] Three letter words, four letter words, and one six letter word."),
    mem=dict(label="A Counter is a dictionary", on="The name counts tied to one Counter object holding a number for each word", names=["counts"], **{"from": "A"},
             narr="Here is the picture. The name counts is tied to one Counter object. A Counter is a special dictionary. Each word is a key, and its value is how many times the word appeared. It has all the powers of a dictionary, plus extras such as most common."),
    B=dict(file="queue.py", label="A queue with deque", on="add and remove at both ends",
           src='''
from collections import deque

queue = deque(["Asha", "Ravi"])
queue.append("Meera")
queue.appendleft("VIP")
print(queue)
print(queue.popleft())
print(queue.pop())
queue.rotate(1)
print(list(queue))
''',
           narr="[HL 1] Import deque. [HL 3] A queue with two people. [HL 4] Append adds at the back. [HL 5] Appendleft adds at the front. Fast, unlike a list. [HL 6] The queue, front to back. VIP, Asha, Ravi, Meera. [HL 7] Popleft removes from the front. VIP goes first. [HL 8] Pop removes from the back. Meera. [HL 9] Rotate moves everyone one step to the right. [HL 10] Ravi is now first, then Asha."),
    term="The counter, then tea 3, then the groups by length. Then the queue, VIP, Meera, and Ravi then Asha.",
    recap=["Counter counts items; most_common gives the top ones.", "defaultdict creates missing keys with a default.", "deque is fast at both ends.", "A deque is not a list: no slices."],
    bug=dict(title="slicing a deque like a list", trim=1, file="slice.py", wrong='''
from collections import deque

d = deque([10, 20, 30, 40])
print(d[1:3])
''', fixed='''
from collections import deque

d = deque([10, 20, 30, 40])
print(list(d)[1:3])
''', wrong_note="a deque does not accept slices", fixed_note="convert to a list first",
             why="A deque is built for the two ends. It supports index access, but not slices, and indexing in the middle is slow. Convert to a list when you need slices.",
             narr="Bug of the Day. We slice a deque like a list. Type error, sequence index must be integer, not slice. A deque is built for working at the two ends. Indexing the middle is slow, and slices are not allowed. When you need them, make a list first, and slice that."),
    pun="Why did the deque get a promotion? It was great at working both ends.",
    task="count letters", challenge="Use Counter on the string \"banana\" and print the two most common letters.",
    answer="Counter(\"banana\").most_common(2) gives [('a', 3), ('n', 2)].",
    shorts=[
        ("Counter", "A Counter counts how many times each item appears. Give it a list of words, and it returns each word with its count. Most common of one gives the top word. Counting by hand with a dictionary takes five lines. This takes one.", "Counter(words)", "Counter counts for you."),
        ("defaultdict", "A defaultdict creates missing keys for you. Say defaultdict of list, and a missing key starts as an empty list. Grouping words by length needs no if statement. Just append, and the key appears by itself.", "defaultdict(list)", "No more key checks."),
        ("deque", "A deque is a double ended queue. Append and pop work at the back. Appendleft and popleft work at the front, and they are fast, unlike a list. Use it for queues, such as customers waiting in a line.", "deque + popleft()", "Fast at both ends."),
        ("No slices", "A deque is not a list. Slice it, and Python says, type error, sequence index must be integer, not slice. A deque is made for the two ends, and the middle is slow. Make a list first, then slice the list.", "TypeError: not slice", "Convert to a list."),
        ("Pun and challenge", "Why did the deque get a promotion? It was great at working both ends. Your challenge. Use Counter on the string banana. Print the two most common letters. Which letter wins, and how many times does it appear?", "Challenge: Counter on banana", "Count the letters."),
    ],
))

EPISODES.append(dict(
    n=84, title="Fetching web data (requests, JSON from an API)", spoken="fetching web data, requests and JSON from an API",
    yt="Python: Fetch Data from a Web API (requests and JSON)", thumb="WEB API",
    vis="Xecxec sending a paper plane to a far-away tower and waiting for the reply",
    goals=["read JSON that an API returns", "know what requests.get looks like", "always set a timeout"],
    tags=["python requests", "python json api", "python requests timeout", "python fetch data from api"],
    hash=["#python", "#api"],
    analogy="posting a letter and waiting for the reply: if the other side never answers, you need a deadline",
    c_title="Ask, wait, read",
    c_pts=["You send a request, and an API sends back text", "That text is usually JSON; json.loads turns it into a dict", "Always give a timeout"],
    intro="Weather, jokes, prices. Many websites hand out data as JSON. Today we read it, and learn why a timeout matters.",
    concept="An API is a web address that returns data instead of a page. You send a request, and the answer usually comes back as JSON text. Turn it into a dictionary with json dot loads, or with the response's json method. The popular requests package does the sending. One thing matters more than any other. Always set a timeout. Without it, if the other side never answers, your program waits forever. Think of posting a letter and waiting for a reply. If nobody answers, you need a deadline. In this episode, the answers are recorded responses, so the lesson works offline.",
    A=dict(file="api.py", label="Reading a recorded response", on="turn JSON text into a dictionary",
           src='''
import json

# recorded response (saved earlier from a weather API)
raw = '{"city": "Panaji", "temp_c": 31, "tags": ["humid", "sunny"]}'
data = json.loads(raw)
print(data["city"], data["temp_c"])
print(data["tags"][0])
print(type(data).__name__)
''',
           ref=[("What the live request looks like (needs the requests package and internet)", "import requests\n\nresponse = requests.get(\"https://example.com/weather?city=Panaji\", timeout=5)\nresponse.raise_for_status()\ndata = response.json()")],
           narr="[HL 1] Import json. [HL 3] A comment says this is a recorded response. The real answer would arrive over the internet, but ours was saved earlier, so it works for everyone. [HL 4] The raw text is JSON. [HL 5] Json loads turns it into a dictionary. [HL 6] Read the city and the temperature. Panaji, thirty one. [HL 7] A list inside the dictionary. The first tag is humid. [HL 8] And the type is dict. With requests, the same last step is response dot json. Check the on screen code for the live version."),
    mem=dict(label="JSON becomes a dictionary", on="The name data tied to a dictionary holding text, a number and a list", names=["data"], **{"from": "A"},
             narr="Here is the picture. The name data is tied to one dictionary. Its keys are city, temp c and tags. The values are text, a number, and a list. JSON objects become dictionaries, JSON lists become lists, and JSON numbers and text become Python numbers and strings. After loading, you work with ordinary Python objects."),
    B=dict(file="todos.py", label="Looping over recorded data", on="list of JSON items, ticked or not",
           src='''
import json

recorded = [
    '{"id": 1, "title": "Learn Python", "done": true}',
    '{"id": 2, "title": "Build a bot", "done": false}',
]
for text in recorded:
    item = json.loads(text)
    mark = "x" if item["done"] else " "
    print(f"[{mark}] {item['title']}")
''',
           narr="[HL 1] Import json. [HL 3] A list of recorded responses. [HL 4] The first item. In JSON, true is lower case. [HL 5] The second item. [HL 7] Loop over them. [HL 8] Load each into a dictionary. JSON true becomes Python True. [HL 9] Pick an x, or a space. [HL 10] Print the mark and the title. One is ticked, one is not."),
    term="Panaji 31, humid, dict. Then the two to-do lines.",
    recap=["An API returns data, usually as JSON text.", "json.loads turns JSON text into dicts and lists.", "requests.get(url, timeout=5) sends the request.", "Always set a timeout, or your program may wait forever."],
    bug=dict(title="no timeout, so the script hangs", kind="hang", file="wait.py", wrong='''
import socket

server = socket.socket()
server.bind(("127.0.0.1", 0))
server.listen(1)
port = server.getsockname()[1]

client = socket.create_connection(("127.0.0.1", port))
print("connected, waiting for a reply")
print(client.recv(10))
print("never reached")
''', fixed='''
import socket

server = socket.socket()
server.bind(("127.0.0.1", 0))
server.listen(1)
port = server.getsockname()[1]

client = socket.create_connection(("127.0.0.1", port))
client.settimeout(1)
print("connected, waiting for a reply")
try:
    print(client.recv(10))
except TimeoutError:
    print("timed out, giving up")
''', wrong_note="the server never answers, and we wait forever", fixed_note="a timeout turns waiting into an error we can handle",
             why="Network calls without a timeout can wait forever when the other side is slow or silent. A timeout turns that into an error you can catch.",
             narr="Bug of the Day. This is a small stand in for a web server that never answers. We connect fine, and then wait for a reply. Nothing arrives, and the program hangs, with no error. In real code, requests dot get without a timeout does the same. Set a timeout, catch the timeout error, and decide what to do next."),
    pun="Why did the request give up? It was tired of waiting for a response.",
    task="read a field", challenge="From the recorded JSON text '{\"name\": \"Asha\", \"scores\": [90, 85]}', print the name and the average score.",
    answer="data = json.loads(text); print(data[\"name\"], sum(data[\"scores\"]) / len(data[\"scores\"])).",
    shorts=[
        ("What is an API", "An API is a web address that returns data instead of a page. You send a request, and get an answer, usually as JSON text. Weather, jokes, prices, many services offer one. Your program can ask, and use the answer.", "request -> JSON answer", "APIs give data."),
        ("JSON to dict", "Json dot loads turns JSON text into Python. A JSON object becomes a dictionary. A JSON list becomes a list. True becomes True with a capital T. After that, you use data city, like any dictionary.", "json.loads(text)", "JSON becomes a dict."),
        ("requests", "The requests package sends the web request. Write requests dot get, with the address, and timeout equals five. Call raise for status to catch errors, then response dot json to get the data. It needs pip install, and the internet.", "requests.get(url, timeout=5)", "requests sends it."),
        ("The silent hang", "Here is the bug. You call get without a timeout, and the server never answers. Your program waits forever, with no error. Always set a timeout. Then a slow server becomes an error you can catch, and a message you can show.", "no timeout = waits forever", "Always set a timeout."),
        ("Pun and challenge", "Why did the request give up? It was tired of waiting for a response. Your challenge. Take this JSON text, with a name, and a list of two scores. Load it, and print the name and the average of the scores.", "Challenge: average score", "Load and average."),
    ],
))

EPISODES.append(dict(
    n=85, title="pathlib and os", spoken="pathlib and os",
    yt="Python pathlib: Work with Files and Folders the Right Way", thumb="PATHLIB",
    vis="Xecxec following a trail of footprints through folders to a file",
    goals=["build paths with pathlib", "read, write and list files", "avoid hard-coded paths"],
    tags=["python pathlib", "python os path", "python glob files", "python file path windows"],
    hash=["#python", "#pathlib"],
    analogy="a street address that works on every map: you build it from pieces, instead of writing the full road by hand",
    c_title="Paths as objects",
    c_pts=["Path(\"a\") / \"b\" joins pieces with the right slash", "p.exists(), p.read_text(), p.write_text()", "glob finds files by pattern"],
    intro="Windows uses backslashes, Mac and Linux use slashes. Pathlib makes your code work on all of them.",
    concept="Pathlib gives you a Path object for every file and folder. Join pieces with the slash operator, and Python uses the right separator for the computer it is running on. A Path can tell you its name, its stem, its suffix and its parent. It can check if it exists, read text, write text, and list the files in a folder with glob. Think of a street address that works on every map, built from pieces. And never write a full path like C colon backslash Users by hand, because it will break on another computer.",
    A=dict(file="paths.py", label="Path objects", on="build a path, and ask it questions",
           files={"notes.txt": "Baga\nColva\n"},
           src='''
from pathlib import Path

p = Path("notes.txt")
print(p.exists())
print(p.stem, p.suffix)
print(p.read_text().splitlines())
log = Path("data") / "log.txt"
print(log.as_posix())
print(log.parent.name, log.name)
''',
           narr="[HL 1] Import Path. [HL 3] A path to a file. [HL 4] Does it exist? True. [HL 5] The stem is the name without the extension. The suffix is the extension. Notes, and dot txt. [HL 6] Read text gives the content in one step, with no open and no close. Two lines. [HL 7] The slash operator joins pieces, so the separator is always right for your computer. [HL 8] As posix shows the path with forward slashes, the same everywhere. [HL 9] The parent is the folder. The name is the last part."),
    c2=dict(label="Build, do not type", on="Folder pieces snap together into a path; a Windows computer and a Linux computer each use their own separator", narr="Here is the idea. You never write the separator yourself. You give Path the pieces, and the slash operator joins them. On Windows, Python joins with a backslash. On Mac and Linux, with a slash. The same code works on both. A path typed by hand, such as C colon backslash Users backslash Asha, only works on one computer, and often only for one person.", anim="Folder blocks labelled data and log.txt snap together with a slash symbol; two computers show different separators from the same code"),
    B=dict(file="folder.py", label="Listing and writing", on="glob, stat, write_text and iterdir",
           files={"data/a.txt": "aa\n", "data/b.txt": "bbbb\n"},
           src='''
from pathlib import Path

folder = Path("data")
for f in sorted(folder.glob("*.txt")):
    print(f.name, f.stat().st_size)
out = folder / "new.txt"
out.write_text("hello")
print(out.exists())
print(sorted(p.name for p in folder.iterdir()))
''',
           narr="[HL 1] Import Path. [HL 3] A folder called data. [HL 4] Glob finds every file that ends in dot txt. Sorted gives a steady order. [HL 5] The name, and the size in bytes. A dot txt has three, b dot txt has five. [HL 6] A new path inside the folder. [HL 7] Write text creates the file. [HL 8] It exists now. True. [HL 9] Iterdir lists everything in the folder. Now there are three files."),
    term="True, notes .txt, the two lines, data/log.txt, data log.txt. Then a.txt 3, b.txt 5, True, and the three file names.",
    recap=["Path objects know their name, stem, suffix and parent.", "The slash operator joins pieces with the right separator.", "read_text, write_text, exists and glob save many lines.", "Never hard-code a full path."],
    bug=dict(title="a hard-coded Windows path", file="read.py", files={"notes.txt": "Baga\n"}, wrong='''
with open("C:\\\\Users\\\\Asha\\\\notes.txt") as f:
    print(f.read())
''', fixed='''
from pathlib import Path

folder = Path(__file__).parent
print((folder / "notes.txt").read_text().strip())
''', wrong_note="that exact path exists only on Asha's computer", fixed_note="the path is built from the script's own folder",
             why="A full path typed by hand works only on the computer that has exactly that folder. Build the path from something your program knows, such as its own folder.",
             narr="Bug of the Day. The path says C colon, Users, Asha, notes. It works on Asha's laptop. On any other computer, with another user name, or on a Mac, there is no such folder. File not found error. Build the path from where your script lives, with pathlib, and it works anywhere."),
    pun="Why did the path get lost? It was hard-coded to the wrong address.",
    task="list your pictures", challenge="Print the names of all dot png files in a folder called images, sorted, using pathlib.",
    answer="for f in sorted(Path(\"images\").glob(\"*.png\")): print(f.name).",
    shorts=[
        ("Path objects", "Pathlib gives you a Path object for every file. It knows its name, its stem, its suffix and its folder. It can check if it exists, and read its text in one line, with no open and no close.", "Path(\"notes.txt\").read_text()", "Paths are objects."),
        ("The slash", "Join path pieces with the slash operator. Path of data, slash, log dot txt. Python uses a backslash on Windows, and a slash on Mac and Linux. The same code works on every computer. Never type the separator yourself.", "Path(\"data\") / \"log.txt\"", "Slash joins pieces."),
        ("glob", "Glob finds files by pattern. Path of data, dot glob, star dot txt, gives every text file in the folder. Wrap it in sorted for a steady order. Each item is a Path, with its own name and size.", "folder.glob(\"*.txt\")", "Find files by pattern."),
        ("Hard-coded path", "A path like C colon, Users, Asha, notes dot txt only works on one computer. On any other, you get file not found error. Build the path from your script's own folder instead, and your program works everywhere.", "FileNotFoundError on other PCs", "Never hard-code paths."),
        ("Pun and challenge", "Why did the path get lost? It was hard-coded to the wrong address. Your challenge. Print the names of all the dot png files in a folder called images. Use pathlib, and glob, and sort the names.", "Challenge: list .png files", "Use glob and sorted."),
    ],
))

EPISODES.append(dict(
    n=86, title="Command-line scripts (sys.argv, argparse)", spoken="command-line scripts, sys dot argv and argparse",
    yt="Python Command-Line Scripts: sys.argv and argparse", thumb="COMMAND LINE",
    vis="Xecxec typing a command with two options into a dark terminal",
    goals=["read arguments from sys.argv", "build a tidy command line with argparse", "handle a missing argument"],
    tags=["python sys.argv", "python argparse", "python command line script", "python indexerror list index out of range"],
    hash=["#python", "#cli"],
    analogy="a restaurant order: the dish and the extras are given when you order, not after you sit down",
    c_title="Arguments from outside",
    c_pts=["sys.argv is a list: script name first, then arguments", "Every argument arrives as text", "argparse adds help, defaults and types"],
    intro="Real tools take their input from the command line. Today our scripts will too.",
    concept="When you type python greet dot py Asha three, Python stores the words in sys dot argv. It is a list. The first item is the script name, and the rest are your arguments, always as text. For small scripts, that is enough. For bigger ones, the argparse module handles names, types, defaults, and a free help message. Think of a restaurant order. The dish and the extras are given when you order, not after you sit down. In this episode we simulate the command inside the script, so it runs on any computer.",
    A=dict(file="greet.py", label="sys.argv", on="read arguments from the list",
           src='''
import sys

print(sys.argv)
sys.argv = ["greet.py", "Asha", "3"]
name = sys.argv[1]
times = int(sys.argv[2])
for _ in range(times):
    print("Hello", name)
''',
           ref=[("The real command", "python greet.py Asha 3        (Windows)\npython3 greet.py Asha 3       (Mac and Linux)")],
           narr="[HL 1] Import sys. [HL 3] Run with no arguments, the list holds only the script name. [HL 4] To simulate the real command, python greet dot py Asha three, we set the list ourselves. Normally, Python fills it in. [HL 5] Item one is the name. Index zero is the script. [HL 6] Item two is the count. It arrives as text, so we convert it with int. [HL 7] A loop. [HL 8] Hello Asha, three times. The real commands for Windows and for Mac are shown on screen."),
    c2=dict(label="Words become a list", on="A typed command splits into words that fill the argv list, with the script name at index zero", narr="Here is what happens. You type a command. The terminal splits it at the spaces into words. Python stores the words in the list sys dot argv. Index zero is the script name. Index one is the first argument. Index two is the second. All of them are text, even if they look like numbers. So convert with int or float when you need a number.", anim="A typed command splits into word blocks that drop into list slots labelled 0, 1 and 2"),
    B=dict(file="cli.py", label="argparse", on="named options, types and defaults",
           src='''
import argparse

parser = argparse.ArgumentParser(description="Greet someone")
parser.add_argument("name")
parser.add_argument("--times", type=int, default=1)
args = parser.parse_args(["Asha", "--times", "2"])
for _ in range(args.times):
    print("Hello", args.name)
print(parser.parse_args(["Ravi"]).times)
''',
           narr="[HL 1] Import argparse. [HL 3] Create a parser, with a description. It writes the help message for you. [HL 4] A required argument, name. [HL 5] An option, times, as an integer, with a default of one. [HL 6] Parse the arguments. Normally this reads the real command line. Here we pass a list, to test. [HL 7] Loop over the number of times. [HL 8] Hello Asha, twice. [HL 9] Without the option, the default is used. One."),
    term="The script name list, then Hello Asha three times. Then Hello Asha twice, then 1.",
    recap=["sys.argv is a list: script name first, then the arguments.", "Arguments are always text; convert with int or float.", "argparse gives names, types, defaults and --help.", "Check the length before reading an argument."],
    bug=dict(title="a missing argument", file="greet.py", wrong='''
import sys

name = sys.argv[1]
print("Hello", name)
''', fixed='''
import sys

if len(sys.argv) < 2:
    print("Usage: python greet.py NAME")
else:
    print("Hello", sys.argv[1])
''', wrong_note="we ran it without a name", fixed_note="check the length first, and show usage",
             why="sys.argv holds only the script name when you give no arguments, so index one does not exist. Check the length first, and show a friendly usage line.",
             narr="Bug of the Day. We run the script with no name. The list holds only the script name, so index one does not exist. Index error, list index out of range. Check the length of sys dot argv first, and print a usage line. Better still, use argparse, which checks for you."),
    pun="Why did the script go to the restaurant? It wanted to take an argument.",
    task="add up arguments", challenge="Write a script that adds up all the numbers given on the command line, using sys.argv.",
    answer="print(sum(int(a) for a in sys.argv[1:])). Remember to skip index zero.",
    shorts=[
        ("sys.argv", "When you type python greet dot py Asha, Python stores the words in sys dot argv. It is a list. Index zero is the script name. Index one is the first argument, Asha. Everything arrives as text.", "sys.argv[1]", "Arguments are in a list."),
        ("Text to number", "Every command line argument is text, even three. To use it as a number, convert it. Int of sys dot argv two gives the integer. Forget this, and a loop that wants a number will fail with a type error.", "int(sys.argv[2])", "Convert with int."),
        ("argparse", "For bigger scripts, use argparse. Add an argument called name, and an option dash dash times, with type int and a default. It reads the command line for you, and writes the help message too.", "parser.add_argument(...)", "argparse does the work."),
        ("Missing argument", "You run the script with no name, and Python says, index error, list index out of range. The list holds only the script name. Check the length of sys dot argv first, and print a usage line. Or let argparse check it.", "IndexError: list index out of range", "Check the length."),
        ("Pun and challenge", "Why did the script go to the restaurant? It wanted to take an argument. Your challenge. Write a script that adds up all the numbers given on the command line. Use sys dot argv, skip index zero, and convert each one to an int.", "Challenge: add up arguments", "Sum the arguments."),
    ],
))
