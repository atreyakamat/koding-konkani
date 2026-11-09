"""Module 4 — Dicts, sets, comprehensions (EP 33-40)."""

MODULE = {"id": 4, "name": "Dicts, sets, comprehensions", "range": "33–40", "colours": "Butter + DarkBlue"}
EPISODES = []
NEXT_AFTER = ("Next: EP 41 · Defining functions", "Module four is done! Next time: functions, your own reusable tools.")

EPISODES.append(dict(
    n=33, title="Dictionaries", spoken="dictionaries",
    yt="Python Dictionaries: Keys and Values for Beginners", thumb="KEYS AND VALUES",
    vis="Xecxec holding a fish-market price board with names on the left and prices on the right",
    goals=["store labelled data in a dictionary", "read, add and change values by key", "handle a missing key"],
    tags=["python dictionary", "python dict keys values", "keyerror python", "python dict basics"],
    hash=["#dictionary", "#dict"],
    analogy="a fish-market price board: you look up the fish by name and read its price",
    c_title="Look things up by name",
    c_pts=["A dict holds key and value pairs", "You read a value with its key", "Keys are unique; adding an existing key replaces its value"],
    intro="Lists find things by position. Today we find things by name, with the dictionary.",
    concept="A dictionary stores pairs. A key, a colon, and a value. Curly brackets hold the pairs, with commas between them. Think of a fish market price board. You look up the fish by name, and read its price. You never need to know the position. Keys are unique. If you add a key that already exists, its value is replaced. Ask for a key that is not there, and Python raises a key error.",
    A=dict(file="prices.py", label="Make and read a dictionary", on="three fish prices, one lookup, one new key",
           src='''
fish_price = {"pomfret": 350, "prawns": 500, "mackerel": 120}
print(fish_price["prawns"])
fish_price["tuna"] = 400
print(fish_price)
print(len(fish_price))
''',
           narr="[HL 1] A dictionary with three pairs. Each key is a fish name, and each value is a price. [HL 2] Square brackets with a key look up the value. Prawns is five hundred. [HL 3] Assign to a new key, and the pair is added. [HL 4] Print the whole dictionary. The new pair is at the end. [HL 5] Len counts the pairs. Four."),
    mem=dict(label="One dictionary object", on="The name fish_price tied to one dict holding four key and value pairs", names=["fish_price"], **{"from": "A"},
             narr="Here is the picture. One name, fish price, tied to one dictionary object. Inside, each key points at a value. Pomfret points at three hundred fifty, prawns at five hundred, and so on. Like a list, a dictionary changes in place. Adding tuna did not make a new dictionary. It grew the one we had."),
    B=dict(file="update.py", label="Change and delete", on="replace a price, delete a pair, test a key with in",
           src='''
fish_price = {"pomfret": 350, "prawns": 500}
fish_price["pomfret"] = 380
del fish_price["prawns"]
print(fish_price)
print("prawns" in fish_price)
''',
           narr="[HL 1] A smaller dictionary. [HL 2] Assign to an existing key, and its value is replaced. Pomfret now costs three hundred eighty. [HL 3] The del statement removes a pair. Prawns is gone. [HL 4] Print what is left. [HL 5] The word in checks keys. Is prawns a key? False. Use in to check before you look up."),
    term="Only pomfret is left, at three hundred eighty. Then False.",
    recap=["A dictionary stores key and value pairs in curly brackets.", "Read a value with dict[key]; assign to a key to add or change a pair.", "del removes a pair and in checks for a key.", "Keys are unique, so a repeated key replaces the old value."],
    bug=dict(title="a key that is not there", file="prices.py", wrong='''
fish_price = {"pomfret": 350, "prawns": 500}
print(fish_price["crab"])
''', fixed='''
fish_price = {"pomfret": 350, "prawns": 500}
if "crab" in fish_price:
    print(fish_price["crab"])
else:
    print("No crab today")
''', wrong_note="crab is not a key", fixed_note="check with in first",
             why="Looking up a key that does not exist raises a KeyError, so check with in before you read.",
             narr="Bug of the Day. We ask for the price of crab, but crab is not a key. Python says, key error, crab. The last line names the missing key. Check with the word in before you read. Then give a friendly message when the key is missing. Next episode, we meet a shorter way, called get."),
    pun="Why did the dictionary win the quiz? It knew every key to the answer.",
    task="a price board with three items", challenge="Make a dictionary of three drinks and their prices. Print the price of one, then add a fourth drink.",
    answer="Use drinks = {\"tea\": 20, \"coffee\": 30, \"lime\": 25}, print(drinks[\"tea\"]), then drinks[\"juice\"] = 40.",
    shorts=[
        ("What is a dictionary?", "A dictionary stores pairs. Each pair has a key and a value. Curly brackets, key, colon, value, with commas between the pairs. Think of a fish market price board. You look up the fish by name, and read the price. You never need to know the position. Dictionaries are how Python models labelled data, such as a student's name, age and marks.", "{\"KEY\": VALUE}", "Look up by name."),
        ("Read, add, change", "Three actions cover most dictionary work. To read, write the dictionary, then the key in square brackets. To add, assign to a new key. To change, assign to an existing key, and the old value is replaced. Keys are unique, so there is only ever one pair for each key. Try all three with your own fish prices.", "PRICES[\"TUNA\"] = 400", "Read, add, change."),
        ("Check with in", "The word in checks whether a key exists. Is prawns in the dictionary? True or False. It only looks at keys, not values. Use it before you read a key you are not sure about. It saves your program from crashing, and it lets you print a friendly message when the key is missing. Check first, then read.", "\"PRAWNS\" IN PRICES", "Does the key exist?"),
        ("Key error", "The classic dictionary bug. You ask for a key that is not there. Python says, key error, and shows the missing key on the last line. A dictionary will not guess, and will not return nothing. Check with in first, or use the get method, which you will meet in the next episode. Read the missing key, and check its spelling.", "KEYERROR: 'CRAB'", "Missing key."),
        ("Pun and challenge", "Why did the dictionary win the quiz? It knew every key to the answer. Your challenge. Make a dictionary of three drinks and their prices. Print the price of one drink. Then add a fourth drink to the dictionary, and print the whole thing. Check that the length is four. Post your drinks menu in the comments below.", "A DRINKS MENU", "Try a dictionary."),
    ],
))

EPISODES.append(dict(
    n=34, title="Dictionary methods and looping", spoken="dictionary methods and looping",
    yt="Python Dictionary Methods: get, items, keys, values", thumb="LOOP THE DICT",
    vis="Xecxec reading a long price board line by line with a magnifying glass",
    goals=["read safely with get", "loop over keys, values and items", "avoid changing a dictionary while looping"],
    tags=["python dict get", "python dict items", "loop through dictionary python", "runtimeerror dictionary changed"],
    hash=["#dictionary", "#loops"],
    analogy="walking along the price board: you can read the names, the prices, or both together",
    c_title="Safe reads and loops",
    c_pts=["get(key, default) never raises an error", "items() gives key and value together", "keys() and values() give one side each"],
    intro="Dictionaries have a few methods that make life easier. Today we read safely, and walk through every pair.",
    concept="Four methods cover most dictionary work. Get reads a key, and gives a default if the key is missing, so no error. Items gives key and value pairs together. Keys gives the keys. Values gives the values. Think of walking along the price board. You can read the names, the prices, or both together. A for loop over a dictionary walks over its keys by default.",
    A=dict(file="loopdict.py", label="get, items, keys, values", on="a safe read and a walk through the pairs",
           src='''
prices = {"pomfret": 350, "prawns": 500}
print(prices.get("prawns"))
print(prices.get("crab", 0))
for fish, price in prices.items():
    print(fish, price)
print(list(prices.keys()))
print(list(prices.values()))
''',
           narr="[HL 1] A dictionary with two fish. [HL 2] Get with a key that exists gives its value, five hundred. [HL 3] Get with a missing key gives the default we choose. Zero. No error. [HL 4] Items gives each pair. We unpack them into fish and price. [HL 5] Print each pair. [HL 6] Keys gives the keys, and list turns them into a list. [HL 7] Values does the same for the values."),
    mem=dict(label="Views, not copies", on="The name prices tied to a dict; keys() and values() read from it", names=["prices"], **{"from": "A"},
             narr="Here is a useful detail. Prices is one dictionary object. The methods keys, values and items do not copy it. They give a live view of the same dictionary. We wrapped them in list to get a plain list to print. If you change the dictionary, the view changes too. That also explains the bug of the day."),
    B=dict(file="total_price.py", label="Loop over values", on="add all the prices; then loop over the keys",
           src='''
prices = {"pomfret": 350, "prawns": 500, "mackerel": 120}
total = 0
for price in prices.values():
    total = total + price
print("Total:", total)
for fish in prices:
    print(fish)
''',
           narr="[HL 1] A dictionary with three fish. [HL 2] A running total. [HL 3] Loop over the values only. [HL 4] Add each price to the total. [HL 5] Three hundred fifty, plus five hundred, plus one hundred twenty, makes nine hundred seventy. [HL 6] A plain for loop over a dictionary gives its keys. [HL 7] So this prints each fish name."),
    term="Total, nine hundred seventy. Then pomfret, prawns and mackerel.",
    recap=["get returns a default instead of raising a KeyError.", "items gives key and value together, keys and values give one side.", "A plain for loop over a dictionary walks over its keys.", "Do not add or remove keys while looping over a dictionary."],
    bug=dict(title="changing a dictionary while looping", file="loopdict.py", wrong='''
prices = {"pomfret": 350, "prawns": 500}
for fish in prices:
    prices["crab"] = 450
''', fixed='''
prices = {"pomfret": 350, "prawns": 500}
for fish in list(prices):
    prices["crab"] = 450
print(prices)
''', wrong_note="a key is added inside the loop", fixed_note="loop over a list of the keys",
             why="Adding or removing keys while looping changes the size of the dictionary being walked, so Python stops with a RuntimeError; loop over a list copy of the keys instead.",
             narr="Bug of the Day. We add a new key while looping over the dictionary. Python says, runtime error, dictionary changed size during iteration. Python cannot walk a dictionary that keeps growing. Loop over a list of the keys instead. That list is a snapshot, so you are free to change the dictionary itself."),
    pun="Why did the dictionary love loops? It could finally read every entry.",
    task="sum the values of a dictionary", challenge="Make marks = {\"maths\": 80, \"science\": 90, \"english\": 70} and print their total with a loop.",
    answer="Use total = 0, then for m in marks.values(): total = total + m, then print(total). It prints 240.",
    shorts=[
        ("Safe reads with get", "The get method reads a key safely. Prices dot get, crab, comma, zero. If crab exists, you get its value. If not, you get the default, zero, and no error. It is shorter than checking with in, and it is easy to read. Use get whenever a missing key is a normal case, and not a mistake in your program.", "PRICES.GET(\"CRAB\", 0)", "No more key errors."),
        ("Items", "To walk through every pair, loop over items. For fish, comma, price, in prices dot items. Each round gives you a key and its value together, already unpacked into two names. Print them, add them, compare them, whatever you need. It is the standard way to loop over a dictionary, and it reads almost like English. Try it today.", "FOR K, V IN D.ITEMS():", "Keys and values together."),
        ("Keys and values", "Sometimes you only need one side. Keys gives the names. Values gives the prices. Loop over values to add up all the prices, without caring about the fish names. A plain for loop over a dictionary gives its keys, so for fish in prices is the same as for fish in prices dot keys. Pick the shortest form that reads well.", "D.KEYS() · D.VALUES()", "One side at a time."),
        ("Changed size", "The loop bug for dictionaries. You add a key while looping over the dictionary. Python says, runtime error, dictionary changed size during iteration. It cannot walk something that keeps growing. The fix is to loop over a list of the keys instead. That list is a snapshot, so you can change the real dictionary safely inside the loop.", "RUNTIMEERROR: CHANGED SIZE", "Loop over a snapshot."),
        ("Pun and challenge", "Why did the dictionary love loops? It could finally read every entry. Your challenge. Make a dictionary of marks, maths eighty, science ninety, english seventy. Print the total of the marks with a loop over the values. You should get two hundred forty. Then try printing each subject with its mark, using items. Share your code in the comments.", "ADD UP THE VALUES", "Try dictionary loops."),
    ],
))

EPISODES.append(dict(
    n=35, title="Sets", spoken="sets",
    yt="Python Sets: Unique Items and Set Operations", thumb="SETS",
    vis="Xecxec sorting shells into a bucket where duplicates vanish",
    goals=["make a set and see that duplicates disappear", "add items and test membership quickly", "combine sets with |, & and -"],
    tags=["python sets", "python set operations", "python union intersection", "empty set python"],
    hash=["#sets", "#python"],
    analogy="a guest list: each name appears once, and you can quickly ask, is this person on the list?",
    c_title="A bag of unique values",
    c_pts=["A set keeps each value once", "Sets have no order and no index", "| & - combine sets like Venn diagrams"],
    intro="Lists allow repeats, and dictionaries need keys. Today we meet the set, a bag of unique values.",
    concept="A set holds unique values. Duplicates disappear. It has no order, so no index either. Think of a guest list. Each name appears once, and you can quickly ask, is this person on the list? Sets also do maths, like Venn diagrams. A bar gives everything in either set. An ampersand gives what is in both. A minus gives what is in the first but not the second.",
    A=dict(file="sets.py", label="Make a set", on="duplicates vanish; add and test membership",
           src='''
fish = {"pomfret", "prawns", "pomfret"}
print(len(fish))
fish.add("crab")
print(sorted(fish))
print("prawns" in fish)
''',
           narr="[HL 1] A set with three items, but pomfret appears twice. [HL 2] The length is two, because the duplicate vanished. [HL 3] Add puts a new item in. [HL 4] Sets have no order, so we use sorted to print them in a stable order. [HL 5] The word in asks, is prawns in the set? True, and sets answer very fast."),
    mem=dict(label="A set holds each object once", on="The name fish tied to a set of three strings", names=["fish"], **{"from": "A"},
             narr="Here is the picture. One name, fish, tied to one set object. Inside are three strings, each one once. The duplicate pomfret never made it in. A set is like a dictionary with only keys, and no values. That is why membership tests are fast, and why the items have no index."),
    B=dict(file="setops.py", label="Union, intersection, difference", on="a | b, a & b and a - b",
           src='''
a = {1, 2, 3}
b = {3, 4}
print(a | b)
print(a & b)
print(a - b)
''',
           narr="[HL 1] A set of one, two, three. [HL 2] And a set of three, four. [HL 3] The bar is the union. Everything in either set, with no repeats. One, two, three, four. [HL 4] The ampersand is the intersection. Only what is in both. Just three. [HL 5] The minus is the difference. What is in a but not in b. One and two."),
    term="One, two, three, four. Then three. Then one, two.",
    recap=["A set keeps each value once and has no order.", "add puts an item in and in tests membership quickly.", "| gives everything, & gives what is shared, - gives what is left.", "Use set() for an empty set, because {} is an empty dictionary."],
    bug=dict(title="curly brackets make a dictionary", kind="output", file="sets.py", wrong='''
empty = {}
print(type(empty))
''', fixed='''
empty = set()
print(type(empty))
''', wrong_note="empty curly brackets", fixed_note="use set()",
             why="Empty curly brackets create an empty dictionary, not an empty set; call set() to make an empty set.",
             narr="Bug of the Day. We want an empty set, so we write empty curly brackets. We print the type, and it says dict. Empty curly brackets make an empty dictionary. For an empty set, call the set function with nothing inside. Then the type says set. Only sets with items can use curly brackets."),
    pun="Why did the set refuse to repeat itself? It only liked unique experiences.",
    task="remove duplicates from a list", challenge="Turn the list [3, 1, 3, 2, 1] into a set and print how many unique numbers there are.",
    answer="Use print(len(set([3, 1, 3, 2, 1]))), which shows 3.",
    shorts=[
        ("What is a set?", "A set is a bag of unique values. Put a value in twice, and only one copy stays. A set has no order, so it has no index either. Think of a guest list. Each name appears once. Make one with curly brackets and commas, or by calling set on a list. It is the quickest way to remove duplicates from your data.", "{1, 2, 2, 3} → {1, 2, 3}", "Unique values only."),
        ("Fast membership", "Sets are very fast at one job. Is this value in the set? The word in answers at once, even if the set has a million items. A list would have to check each item, one by one. So when you have many values and you keep asking, is it in there, use a set. It is a small change with a big effect.", "\"PRAWNS\" IN FISH", "Fast yes or no."),
        ("Set maths", "Sets do maths like Venn diagrams. A bar gives the union, everything in either set. An ampersand gives the intersection, only what both sets share. A minus gives the difference, what is in the first set but not the second. With these three, you can answer questions like, who joined both classes, in two short lines. Try it yourself.", "A | B · A & B · A - B", "Venn diagrams in code."),
        ("Empty set trap", "Here is a trap. You write empty equals curly brackets, expecting an empty set. But empty curly brackets make an empty dictionary. Print its type, and it says dict. To make an empty set, call set with nothing inside. Only sets that have items can use curly brackets. Remember this whenever you start with nothing at all.", "{} IS A DICT", "Use set()."),
        ("Pun and challenge", "Why did the set refuse to repeat itself? It only liked unique experiences. Your challenge. Take the list three, one, three, two, one. Turn it into a set. Print how many unique numbers there are. You should see three. Then print the set itself, using sorted so it appears in order. Share your answer in the comments below.", "COUNT UNIQUE NUMBERS", "Try a set."),
    ],
))

EPISODES.append(dict(
    n=36, title="Nested data", spoken="nested data",
    yt="Python Nested Data: Dicts of Lists and Lists of Dicts", thumb="DATA IN DATA",
    vis="Xecxec opening Russian-doll style boxes, each with a list or a dictionary inside",
    goals=["put lists inside dictionaries and dictionaries inside lists", "read deep values with chained brackets", "build records as a list of dictionaries"],
    tags=["python nested dictionary", "list of dictionaries python", "python json like data", "keyerror nested"],
    hash=["#nesteddata", "#dictionary"],
    analogy="a restaurant menu: the menu has sections, each section has dishes, and each dish has a price",
    c_title="Containers inside containers",
    c_pts=["A dict value can be a list or another dict", "A list item can be a dict", "Chain the brackets from the outside in"],
    intro="Real data is rarely flat. Today we put containers inside containers, and read the data back out.",
    concept="Containers can hold containers. A dictionary value can be a list, or another dictionary. A list item can be a dictionary. Think of a restaurant menu. The menu has sections. Each section has dishes. Each dish has a price. To read deep values, chain the brackets from the outside in. Menu, bracket mains, bracket one. This shape is exactly what you will meet in JSON files and web data.",
    A=dict(file="menu.py", label="A dictionary of lists", on="sections of a menu, each with a list of dishes",
           src='''
menu = {"starters": ["fish fry", "bhaji"], "mains": ["fish curry", "xacuti"]}
print(menu["mains"])
print(menu["mains"][1])
menu["desserts"] = ["bebinca"]
print(len(menu))
''',
           narr="[HL 1] A dictionary. Each key is a section, and each value is a list of dishes. [HL 2] Menu bracket mains gives the whole list. [HL 3] Add another bracket, and you pick one dish. Index one, xacuti. [HL 4] Add a new section with a list of one dish. [HL 5] The dictionary now has three sections."),
    mem=dict(label="Objects pointing at objects", on="The name menu tied to a dict whose values are lists", names=["menu"], **{"from": "A"},
             narr="Here is the picture. One name, menu, tied to one dictionary. Each value in that dictionary is an arrow to a list object. And each list holds arrows to string objects. Nested data is just arrows that point at other objects. To read a deep value, you follow the arrows, one bracket at a time."),
    B=dict(file="students.py", label="A list of dictionaries", on="each student is one record",
           src='''
students = [{"name": "Asha", "marks": 88}, {"name": "Ravi", "marks": 92}]
for s in students:
    print(s["name"], s["marks"])
print(students[1]["name"])
''',
           narr="[HL 1] A list with two items, and each item is a dictionary. Each dictionary is one student record. [HL 2] Loop over the list. Each round, s is one dictionary. [HL 3] Pick its name and marks by key. Asha, eighty eight. Ravi, ninety two. [HL 4] Or reach in directly. Index one is the second student. Then the key name. Ravi."),
    term="Asha eighty eight. Ravi ninety two. Then Ravi again.",
    recap=["A dictionary value can be a list or another dictionary.", "A list item can be a dictionary, which makes a record.", "Chain the brackets from the outside in.", "Check that each key exists before you go deeper."],
    bug=dict(title="a missing key deep inside", file="menu.py", wrong='''
menu = {"starters": ["fish fry"], "mains": ["fish curry"]}
print(menu["drinks"][0])
''', fixed='''
menu = {"starters": ["fish fry"], "mains": ["fish curry"]}
drinks = menu.get("drinks", [])
if drinks:
    print(drinks[0])
else:
    print("No drinks listed")
''', wrong_note="there is no drinks section", fixed_note="get with a default, then check",
             why="The first bracket fails with a KeyError when the key is missing, so read with get and a default before going deeper.",
             narr="Bug of the Day. We reach for the first drink, but there is no drinks section. Python says, key error, drinks. The error happens at the first bracket, before the index is even tried. Read with get and a default empty list, then check the list is not empty, before you go deeper."),
    pun="Why did the data feel so deep? It had layers upon layers.",
    task="read a score from a nested dictionary", challenge="Given data = {\"asha\": {\"maths\": 80, \"science\": 90}}, print Asha's science mark.",
    answer="Use print(data[\"asha\"][\"science\"]), which shows 90.",
    shorts=[
        ("Containers in containers", "Containers can hold other containers. A dictionary value can be a list. A list item can be a dictionary. Think of a restaurant menu. The menu has sections, each section has dishes, and each dish has a price. Real data is almost always shaped like this. Learn to read it, and web data, files, and records will all start to look familiar.", "{\"MAINS\": [\"CURRY\"]}", "Data inside data."),
        ("Chain the brackets", "To read a deep value, chain the brackets from the outside in. Menu, bracket mains, picks the list of main dishes. Add another bracket, and you pick one dish from that list. Each bracket takes one step deeper. If you get lost, print the pieces one at a time. Every step gives you something simpler to look at.", "MENU[\"MAINS\"][1]", "One bracket, one step."),
        ("A list of records", "A list of dictionaries is the most common shape for data. Each dictionary is one record, like one student, with a name and marks. Loop over the list, and in each round pick the fields by key. Add a new student by appending a new dictionary. It is a tiny database, and you already know how to read it.", "[{\"NAME\": \"ASHA\"}, ...]", "Records in a list."),
        ("Nested key error", "Here is the bug. You reach into a nested dictionary, but the first key is missing. Python says, key error, drinks, before it even looks at the index. Use get with a default, like an empty list, then check that it is not empty before you go deeper. Defensive reads save you from crashes on real data.", "KEYERROR: 'DRINKS'", "Guard each step."),
        ("Pun and challenge", "Why did the data feel so deep? It had layers upon layers. Your challenge. You have a dictionary called data, and inside it a key asha, holding another dictionary with maths eighty and science ninety. Print Asha's science mark. Use two sets of brackets, outside in. You should see ninety. Share your answer in the comments below.", "READ A NESTED MARK", "Try nested data."),
    ],
))

EPISODES.append(dict(
    n=37, title="List comprehensions", spoken="list comprehensions",
    yt="Python List Comprehensions: One-Line Loops", thumb="ONE-LINE LOOPS",
    vis="Xecxec feeding a list into a machine that outputs a new list, labelled [n * n for n in nums]",
    goals=["build a list in one line with a comprehension", "filter with if at the end", "put the if/else before the for"],
    tags=["python list comprehension", "python comprehension if else", "python one liner", "syntaxerror comprehension"],
    hash=["#comprehension", "#lists"],
    analogy="a juice stall: fruit goes in, a rule is applied, and a glass comes out for each fruit",
    c_title="A loop that builds a list",
    c_pts=["[expression for item in list]", "Add if at the end to filter", "Keep it short enough to read"],
    intro="Loops that build lists are so common that Python has a shortcut. Today we meet the list comprehension.",
    concept="A list comprehension builds a list in one line. Square brackets. First, what you want for each item. Then, for, the item, in, the source list. Think of a juice stall. Fruit goes in, a rule is applied, and a glass comes out for each fruit. Add an if at the end to keep only some items. Keep comprehensions short. If a line is hard to read, write the loop out in full instead.",
    A=dict(file="squares.py", label="Build and filter", on="squares of every number, and only the even ones",
           src='''
nums = [1, 2, 3, 4, 5]
squares = [n * n for n in nums]
print(squares)
evens = [n for n in nums if n % 2 == 0]
print(evens)
''',
           narr="[HL 1] A list of five numbers. [HL 2] Read it left to right. For each n in nums, make n times n. The result is a new list of squares. [HL 3] One, four, nine, sixteen, twenty five. [HL 4] Add an if at the end to filter. Keep n only when it divides by two. [HL 5] Two and four."),
    mem=dict(label="Comprehensions make new lists", on="nums, squares and evens each tied to their own list", names=["nums", "squares", "evens"], **{"from": "A"},
             narr="Here is the picture. Nums, squares and evens each point at their own list object. A comprehension never changes the source list. It builds a brand new one. Nums is exactly as it was. That is what makes comprehensions safe. You never change the list while you walk over it."),
    B=dict(file="words_comp.py", label="Methods inside", on="make capitals and lengths from a list of words",
           src='''
words = ["fish", "crab", "prawn"]
caps = [w.upper() for w in words]
lengths = [len(w) for w in words]
print(caps)
print(lengths)
''',
           narr="[HL 1] A list of three words. [HL 2] For each word, call upper. We get a list of capital words. [HL 3] For each word, take its length. A list of numbers. [HL 4] Print the capital words. [HL 5] Print the lengths. Four, four, five. Any expression can go at the front, a method call, a sum, a call to len."),
    term="Fish, crab, prawn in capitals, then four, four, five.",
    recap=["[expression for item in list] builds a new list.", "Add if at the end to keep only some items.", "An if and else together go before the for.", "If a comprehension is hard to read, use a normal loop."],
    bug=dict(title="else in the wrong place", file="squares.py", wrong='''
nums = [1, 2, 3, 4]
labels = [n if n % 2 == 0 for n in nums]
''', fixed='''
nums = [1, 2, 3, 4]
labels = [n if n % 2 == 0 else 0 for n in nums]
print(labels)
''', wrong_note="an if without an else before the for", fixed_note="if and else both before the for",
             why="An if that picks between two values needs its else, and both sit in front of the for; a filter if without else goes at the end.",
             narr="Bug of the Day. We try to keep even numbers, and use zero for the rest. We wrote an if with no else before the for. Python says, syntax error, expected else after if expression. A choice between two values needs both if and else, before the for. A simple filter goes at the end, with no else."),
    pun="Why did the comprehension get a short job title? It did everything in one line.",
    task="double every number in a list", challenge="Use a list comprehension to double each number in [1, 2, 3, 4] and print the result.",
    answer="Use print([n * 2 for n in [1, 2, 3, 4]]), which shows [2, 4, 6, 8].",
    shorts=[
        ("One-line loops", "A list comprehension builds a list in one line. Square brackets, then what you want for each item, then for, the item, in, the source list. Nums squared looks like n times n, for n in nums. It replaces a three line loop with a single line. Read it from left to right, like a sentence, and it makes perfect sense.", "[N * N FOR N IN NUMS]", "A loop in one line."),
        ("Filter with if", "Add an if at the end to keep only some items. Square brackets, n, for n in nums, if n modulo two equals zero. Only the even numbers make it into the new list. The source list is never changed. The if is a filter, and it has no else. It is a neat way to pick the items you want from a long list.", "[N FOR N IN NUMS IF N % 2 == 0]", "Keep only what you want."),
        ("Keep it readable", "Comprehensions are great, but do not overuse them. If a comprehension needs two loops, three conditions, and a function call, it is too long. Write a normal loop instead. Your future self will thank you. A good rule is that you should read the line once, and understand it. Short and clear beats clever, every time. Remember that.", "SHORT AND CLEAR", "Do not be too clever."),
        ("If and else placement", "Here is the syntax trap. You want even numbers, and zero for the rest. You write an if, with no else, before the for. Python says, syntax error, expected else after if expression. A choice between two values needs both if and else, before the for. A plain filter if goes at the end, and has no else.", "SYNTAXERROR: EXPECTED ELSE", "Placement matters."),
        ("Pun and challenge", "Why did the comprehension get a short job title? It did everything in one line. Your challenge. Use a list comprehension to double every number in the list one, two, three, four. Print the new list. You should see two, four, six, eight. Then add an if, to double only the numbers above two. Post your one-liner in the comments below.", "DOUBLE THEM ALL", "Try a comprehension."),
    ],
))

EPISODES.append(dict(
    n=38, title="Dict and set comprehensions", spoken="dictionary and set comprehensions",
    yt="Python Dict and Set Comprehensions", thumb="DICT + SET COMPS",
    vis="Xecxec feeding names into a machine that outputs key and value pairs",
    goals=["build a dictionary in one line", "build a set in one line", "notice that duplicate keys overwrite each other"],
    tags=["python dict comprehension", "python set comprehension", "duplicate keys python", "comprehension keys"],
    hash=["#comprehension", "#dictionary"],
    analogy="a name-badge printer: each name goes in, and a badge with the name and its length comes out",
    c_title="Curly bracket comprehensions",
    c_pts=["{key: value for ...} builds a dict", "{item for ...} builds a set", "A repeated key keeps only the last value"],
    intro="Lists are not the only things you can build in one line. Today we build dictionaries and sets the same way.",
    concept="A dictionary comprehension uses curly brackets and a colon. Key, colon, value, for, the item, in, the source. A set comprehension uses curly brackets without a colon. Think of a name badge printer. Each name goes in, and a badge with the name and its length comes out. Keys must be unique, so if two items make the same key, the later one overwrites the earlier one.",
    A=dict(file="dictcomp.py", label="Dictionary comprehensions", on="name to length, and number to square",
           src='''
names = ["Asha", "Ravi", "Maya"]
lengths = {n: len(n) for n in names}
print(lengths)
squares = {n: n * n for n in range(1, 4)}
print(squares)
''',
           narr="[HL 1] A list of three names. [HL 2] The curly brackets and the colon make a dictionary. For each name, the key is the name, and the value is its length. [HL 3] Each name has four letters. [HL 4] Another one. For each number from one to three, the key is the number, and the value is its square. [HL 5] One, four, nine."),
    mem=dict(label="Two new dictionaries", on="lengths and squares each tied to their own dict", names=["lengths", "squares"], **{"from": "A"},
             narr="Here is the picture. Lengths is tied to one dictionary, with names as keys. Squares is tied to another, with numbers as keys. The list of names is untouched. Each comprehension created a brand new dictionary. Dictionary keys must be unique. If two items give the same key, the later pair replaces the earlier one."),
    B=dict(file="setcomp.py", label="Set comprehensions", on="first letters, with duplicates removed",
           src='''
words = ["fish", "crab", "fig", "fish"]
letters = {w[0] for w in words}
print(sorted(letters))
print(len(letters))
''',
           narr="[HL 1] A list of four words, with fish twice. [HL 2] Curly brackets, with no colon, make a set. For each word, take its first letter. [HL 3] Print them in order, with sorted. The letters c and f, with no repeats. [HL 4] Only two letters. The set removed the duplicates for us."),
    term="C and f, then two.",
    recap=["{key: value for ...} builds a dictionary.", "{item for ...} builds a set.", "Keys are unique, so a repeated key overwrites the earlier pair.", "Comprehensions never change the source list."],
    bug=dict(title="duplicate keys overwrite", kind="output", file="dictcomp.py", wrong='''
words = ["fish", "crab", "fig"]
first = {w[0]: w for w in words}
print(first)
''', fixed='''
words = ["fish", "crab", "fig"]
first = {w: w[0] for w in words}
print(first)
''', wrong_note="fish and fig both give the key f", fixed_note="the word itself is the unique key",
             why="Two words with the same first letter make the same key, and the later pair replaces the earlier one, so one word is lost.",
             narr="Bug of the Day. We use the first letter as the key. Fish and fig both start with f. The second one overwrites the first. Our dictionary has only two pairs, and fish is lost. No error, only missing data. Pick a key that is unique, like the whole word, and nothing is lost."),
    pun="Why did the set comprehension skip the party? It heard everyone would be repeated.",
    task="build a dictionary of squares", challenge="Build a dictionary mapping 1 to 5 to their squares, in one line, and print it.",
    answer="Use print({n: n * n for n in range(1, 6)}), which shows {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}.",
    shorts=[
        ("Dictionary comprehension", "A dictionary comprehension builds a dictionary in one line. Curly brackets, a key, a colon, a value, then for, the item, in, the source. Names to lengths becomes n, colon, len of n, for n in names. It is the same idea as a list comprehension, with curly brackets and a colon. Use it to turn one list into a lookup table.", "{N: LEN(N) FOR N IN NAMES}", "Lookup tables in one line."),
        ("Set comprehension", "A set comprehension looks like a dictionary one, but with no colon. Curly brackets, an expression, then for. Take the first letter of every word, and a set keeps each letter just once. So you get the unique first letters, in one short line. Wrap it in sorted if you want a stable order for printing. It is that simple.", "{W[0] FOR W IN WORDS}", "Unique results in one line."),
        ("Keys must be unique", "Remember that dictionary keys are unique. In a comprehension, if two items give the same key, the later pair overwrites the earlier one. There is no warning. So when you choose the key, ask yourself, can two items ever give the same key? If so, pick a different key, or a list as the value. Unique keys protect your data, so choose them with care.", "SAME KEY, LAST WINS", "Keys are unique."),
        ("Lost fish", "A quiet bug. You build a dictionary using the first letter of each word as the key. Fish and fig both start with f. The second one overwrites the first. Your dictionary has two pairs, not three, and fish is lost, with no error. Choose a key that is unique, like the whole word, and nothing disappears.", "FISH WAS OVERWRITTEN", "Check your keys."),
        ("Pun and challenge", "Why did the set comprehension skip the party? It heard everyone would be repeated. Your challenge. In one line, build a dictionary that maps the numbers one to five to their squares. Print it. You should see one maps to one, two maps to four, and so on up to twenty five. Use a dictionary comprehension. Share your line in the comments.", "SQUARES IN A DICT", "Try a dict comprehension."),
    ],
))

EPISODES.append(dict(
    n=39, title="Counting with dicts", spoken="counting with dictionaries",
    yt="Python Counting With Dictionaries and Counter", thumb="COUNT WITH DICTS",
    vis="Xecxec making tally marks next to each letter of the word banana",
    goals=["count items with a dictionary", "start a new key with get(key, 0)", "use Counter for the same job"],
    tags=["python count with dictionary", "python counter", "python get default", "frequency count python"],
    hash=["#counter", "#dictionary"],
    analogy="a tally sheet: each time you see a letter, you add one mark next to it",
    c_title="Tally with a dictionary",
    c_pts=["Keys are the things, values are the counts", "A new key must start at 0", "get(key, 0) + 1 does it in one line"],
    intro="One of the most useful jobs for a dictionary is counting. Today we count letters, and learn the pattern.",
    concept="Counting is a classic dictionary job. The keys are the things you count. The values are the counts. Think of a tally sheet. Each time you see a letter, you add one mark next to it. But a new letter has no mark yet. You must start it at zero, or one. The get method with a default zero does this in one line. And Python has a ready made helper called Counter.",
    A=dict(file="count.py", label="Counting letters", on="count the letters of banana with if and else",
           src='''
text = "banana"
counts = {}
for ch in text:
    if ch in counts:
        counts[ch] = counts[ch] + 1
    else:
        counts[ch] = 1
print(counts)
''',
           narr="[HL 1] The text, banana. [HL 2] An empty dictionary for the tallies. [HL 3] Loop over each letter. [HL 4] If we have seen the letter before, [HL 5] add one to its count. [HL 6] Otherwise, [HL 7] this is the first time, so start its count at one. [HL 8] Print the tallies. B once, a three times, n twice."),
    mem=dict(label="Counts stored in a dictionary", on="counts tied to a dict from letters to ints", names=["counts"], **{"from": "A"},
             narr="Here is the picture. Counts is tied to one dictionary. Each key is a letter, and each value is an int tally. When we added one, the tag inside the dictionary moved to a new int. The dictionary kept its shape, and only the numbers changed. This is how most word counts and letter counts are built."),
    B=dict(file="getcount.py", label="get and Counter", on="the same count with get, then with Counter",
           src='''
from collections import Counter
text = "banana"
counts = {}
for ch in text:
    counts[ch] = counts.get(ch, 0) + 1
print(counts)
print(Counter(text).most_common(1))
''',
           narr="[HL 1] Counter lives in a toolbox called collections. We import it. [HL 2] The text. [HL 3] An empty dictionary. [HL 4] Loop over the letters. [HL 5] Get the current count, or zero if the letter is new, and add one. Two lines of the earlier version became one. [HL 6] Same result. [HL 7] Counter does the whole job in one call. Most common, one, gives the top letter and its count. A, three."),
    term="The same tallies, then a, three.",
    recap=["Keys are the things being counted and values are the counts.", "A new key must have a starting value before you add to it.", "counts.get(key, 0) + 1 is the one-line pattern.", "Counter from collections counts for you."],
    bug=dict(title="no starting value", file="count.py", wrong='''
counts = {}
for ch in "goa":
    counts[ch] += 1
''', fixed='''
counts = {}
for ch in "goa":
    counts[ch] = counts.get(ch, 0) + 1
print(counts)
''', wrong_note="the key g does not exist yet", fixed_note="get with a default of zero",
             why="counts[ch] += 1 reads the key before it exists, which raises a KeyError; get with a default gives a starting value.",
             narr="Bug of the Day. We try to add one to a count that does not exist yet. Python says, key error, g. The plus equals line reads the old count first, and a brand new letter has none. Use get with a default of zero, and the first time gives zero plus one. Then every later time just adds one more."),
    pun="Why did the dictionary count on everyone? It never lost track.",
    task="count the vowels in a word", challenge="Count how many times each letter appears in \"coconut\" and print the dictionary.",
    answer="Use counts = {} with counts[ch] = counts.get(ch, 0) + 1 in a loop. It prints {'c': 2, 'o': 2, 'n': 1, 'u': 1, 't': 1}.",
    shorts=[
        ("Counting with a dictionary", "Counting is a classic dictionary job. The keys are the things you count. The values are the counts. Think of a tally sheet, where you add a mark for each letter you see. Loop over the text, and for each letter, add one to its count. At the end, the dictionary shows how many times each letter appeared. It is the base of every word counter.", "LETTER → COUNT", "A tally sheet in code."),
        ("The if and else way", "The simple way to count is with if and else. If the letter is already a key, add one to its count. Otherwise, this is the first time, so set its count to one. It is clear and easy to read, and it works. Many beginners start here, and that is a perfectly good way to learn the idea.", "IF CH IN COUNTS: ... ELSE: ...", "The clear way."),
        ("The get way", "The shorter way uses get. Counts of ch equals counts dot get, ch, zero, plus one. Get returns the current count, or zero if the letter is new. Then we add one, and save it back. Two lines become one. This is the pattern you will see in most real Python code, so learn to read it, and to write it.", "COUNTS.GET(CH, 0) + 1", "One line to count."),
        ("Key error on a new key", "The bug. You write counts of ch, plus equals one, but the key does not exist yet. Python says, key error. The line tries to read the old count first, and a brand new letter has none. Use get with a default of zero, and the first time works. Every key needs a starting value before you add to it.", "KEYERROR: 'G'", "Start at zero."),
        ("Pun and challenge", "Why did the dictionary count on everyone? It never lost track. Your challenge. Count how many times each letter appears in the word coconut. Use a dictionary and a loop. Print the final dictionary. You should see c twice, and o twice. Then try the Counter helper from the collections module, and check that you get the same answer. Share your result below.", "COUNT THE LETTERS", "Try counting."),
    ],
))

EPISODES.append(dict(
    n=40, title="Mini project: Word counter", spoken="the word counter mini project",
    yt="Python Mini Project: Word Counter", thumb="WORD COUNTER",
    vis="Xecxec reading a page of text with a magnifying glass and a tally sheet",
    goals=["split text into words and count each one", "make counting case-insensitive with lower()", "print the results in order and find the most common word"],
    tags=["python word counter", "python mini project", "python word frequency", "python lower split"],
    hash=["#project", "#wordcounter"],
    analogy="a library assistant: read a page, tally every word, and report the favourite",
    c_title="Planning the word counter",
    c_pts=["Read a line of text and make it lowercase", "Split it into words and count each", "Print the counts in order and the most common word"],
    intro="Time for a project that puts the whole module together. Today we build a word counter.",
    concept="Here is the plan. Read a line of text. Make it lowercase, so The and the count as one word. Split it into words. Count each word in a dictionary. Then print the counts in alphabetical order, and name the most common word. It uses strings, lists, dictionaries and loops. And one new trick, max with a key, to find the biggest count.",
    A=dict(file="wordcount.py", label="The word counter", on="count the words of a typed line",
           src='''
text = input("Text: ")
words = text.lower().split()
counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1
for word in sorted(counts):
    print(word, counts[word])
print("Most common:", max(counts, key=counts.get))
''',
           stdin="The sea the sand The sun\n",
           narr="[HL 1] Ask for a line of text. [HL 2] Make it lowercase, then split it into words. Chaining methods like this is common. [HL 3] An empty dictionary for the counts. [HL 4] Loop over the words. [HL 5] The counting pattern, with get. [HL 6] Loop over the sorted keys, so the output is alphabetical. [HL 7] Print each word and its count. [HL 8] Max over the dictionary finds the key with the biggest count. Key equals counts dot get, says, compare by the count."),
    mem=dict(label="Words and their counts", on="words tied to a list; counts tied to a dict from word to count", names=["words", "counts"], **{"from": "A"},
             narr="Here is the end state. Words is tied to a list of six lowercase words. Counts is tied to a dictionary with four keys, because the repeated words were merged. The word the has the count three. The list kept every word, and the dictionary kept the tallies. Two different shapes for two different questions."),
    B=dict(file="unique.py", label="Unique words with a set", on="how many words, and how many are unique",
           src='''
text = "the sea the sand the sun"
words = text.split()
print(len(words), "words")
print(len(set(words)), "unique")
''',
           narr="[HL 1] A fixed sentence. [HL 2] Split into a list. [HL 3] The length of the list is every word, counting repeats. Six. [HL 4] Wrap the list in set, and the repeats vanish. The length is the number of unique words. Four. Sets and dictionaries are two different tools for similar questions."),
    term="Six words, then four unique.",
    recap=["Make the text lowercase before you split it.", "split() turns a sentence into a list of words.", "counts.get(word, 0) + 1 tallies each word.", "max(counts, key=counts.get) finds the most common word."],
    bug=dict(title="capital and small letters counted apart", kind="output", file="wordcount.py", wrong='''
text = "The sea the sand"
counts = {}
for word in text.split():
    counts[word] = counts.get(word, 0) + 1
print(counts)
''', fixed='''
text = "The sea the sand"
counts = {}
for word in text.lower().split():
    counts[word] = counts.get(word, 0) + 1
print(counts)
''', wrong_note="The and the are different strings", fixed_note="lower() before split()",
             why="Strings are case sensitive, so The and the are two different keys; make the text lowercase before you count.",
             narr="Bug of the Day. The word the appears twice, once with a capital T. Our dictionary treats them as two different words, each with a count of one. Strings are case sensitive. Call lower before split, and the two become one word, with a count of two."),
    pun="Why did the word counter never get bored? It always had a lot to say.",
    task="count words in your own sentence", challenge="Run the word counter on your own sentence, and also print how many unique words it has.",
    answer="Reuse wordcount.py and add print(len(counts), \"unique words\") at the end.",
    shorts=[
        ("The word counter plan", "Let us build a word counter. Read a line of text. Make it lowercase, so capital letters do not matter. Split it into words. Count each word in a dictionary. Then print the counts in alphabetical order, and name the most common word. It uses strings, lists, dictionaries, and loops, so it is a perfect project to finish the module.", "BUILD A WORD COUNTER", "A project for the whole module."),
        ("Lower, then split", "The first two steps are one line. Text dot lower, dot split. Lower makes every letter small, so The and the become the same word. Split cuts the text at the spaces, and gives a list of words. Chaining methods like this is very common in Python. Read it left to right, one step at a time.", "TEXT.LOWER().SPLIT()", "Chain the methods."),
        ("The most common word", "To find the most common word, use max on the dictionary, with key equals counts dot get. Normally, max would compare the keys, the words, alphabetically. The key option tells it to compare by the count instead. So you get the word with the biggest count. It is a very short answer to a very useful question.", "MAX(COUNTS, KEY=COUNTS.GET)", "The winner of the count."),
        ("Case matters", "Here is the quiet bug. The word the appears twice, once with a capital T. Your dictionary treats The and the as two different words, each with a count of one. There is no error, only a wrong answer. Strings are case sensitive. Call lower before you split, and the two become one word with a count of two.", "THE ≠ THE", "Lower it first."),
        ("Pun and challenge", "Why did the word counter never get bored? It always had a lot to say. Your challenge. Run the word counter on a sentence of your own, with at least ten words. Then add a line that prints how many unique words there are. You can use the length of the dictionary. Share your sentence and your answer in the comments below.", "COUNT YOUR OWN WORDS", "Try your own text."),
    ],
))
