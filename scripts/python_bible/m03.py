"""Module 3 — Strings, lists, tuples (EP 23-32)."""

MODULE = {"id": 3, "name": "Strings, lists, tuples", "range": "23–32", "colours": "Mint + DarkBlue"}
EPISODES = []
NEXT_AFTER = ("Next: EP 33 · Dictionaries", "Module three is done! Next time: dictionaries, where every value has its own label.")

EPISODES.append(dict(
    n=23, title="String methods", spoken="string methods",
    yt="Python String Methods: upper, strip, split, replace", thumb="STRING TOOLKIT",
    vis="Xecxec holding a toolbox whose tools are labelled upper, strip, split and replace",
    goals=["clean and change text with string methods", "split text into words and join it back", "know that string methods return new strings"],
    tags=["python string methods", "python split join", "python strip", "strings are immutable"],
    hash=["#strings", "#stringmethods"],
    analogy="a tailor shop: the tailor never changes your old shirt, they hand you a new one that fits",
    c_title="Methods are tools on a string",
    c_pts=["Write the string, a dot, the method name, brackets", "upper, lower and strip clean text", "Methods return a new string; the old one stays"],
    intro="Strings come with a toolbox. Today we open it, and learn the tools that you use most often.",
    concept="A method is a tool that belongs to a value. You write the string, a dot, the method name and brackets. Upper makes capitals. Lower makes small letters. Strip removes spaces at the ends. Replace swaps one piece of text for another. Think of a tailor shop. The tailor never changes your old shirt. They hand you a new shirt that fits. Every string method returns a new string, and leaves the old one alone.",
    A=dict(file="methods.py", label="Four string methods", on="strip, upper, lower and replace on one string",
           src='''
text = "  Goa Beach  "
print(text.strip())
print(text.upper())
print(text.lower())
print(text.replace("Goa", "Baga"))
print(len(text.strip()))
''',
           narr="[HL 1] A string with two spaces at each end. [HL 2] Strip removes the spaces at both ends. We get Goa Beach, with nothing around it. [HL 3] Upper makes every letter a capital. The spaces are still there. [HL 4] Lower makes every letter small. [HL 5] Replace swaps Goa for Baga. Case matters, so Goa must match exactly. [HL 6] And the length of the stripped text is nine.",
           label2="Reading the output", narr2="Predict first. [TRACK text=  Goa Beach  ] Look at the original name text. It never changes. Every line made a new string. The old one, with its spaces and its capitals, is exactly as it was. That one fact explains the bug of the day."),
    mem=dict(label="Methods make new strings", on="Two tags, line and parts, tied to a string and to a list of words", names=["line", "parts"], **{"from": "B"},
             narr="Look at the picture after the split. The name line is still tied to the original string, fish curry rice. The name parts is tied to a new list that holds three words. Splitting did not touch the first string. It created a new object, a list, and tied parts to it. We meet lists properly in two episodes."),
    B=dict(file="words.py", label="Split and join", on="split a sentence into words, then join them with dashes",
           src='''
line = "fish curry rice"
parts = line.split()
print(parts)
print(len(parts))
print("-".join(parts))
''',
           narr="[HL 1] A string with three words. [HL 2] Split cuts the string at the spaces, and gives a list of the pieces. [HL 3] The list prints inside square brackets, with each word in quotes. [HL 4] There are three words. [HL 5] Join does the reverse. It glues the pieces together, with the string before the dot placed between them. Fish dash curry dash rice."),
    term="The list of three words, then three, then fish dash curry dash rice.",
    recap=["A method is a tool written after a dot, like text.upper().", "strip, upper, lower and replace clean and change text.", "split cuts a string into a list and join glues a list into a string.", "String methods return new strings and never change the old one."],
    bug=dict(title="strings cannot be changed in place", file="methods.py", wrong='''
name = "goa"
name[0] = "G"
''', fixed='''
name = "goa"
name = name.capitalize()
print(name)
''', wrong_note="we try to change one letter", fixed_note="make a new string instead",
             why="Strings are immutable, so no letter can be changed in place; build a new string and tie the name to it.",
             narr="Bug of the Day. We try to change the first letter of the string. Python says, type error. A str object does not support item assignment. Strings are immutable. Their letters can never be changed in place. Instead, make a new string with a method like capitalize, and tie the name to it."),
    pun="Why did the string go to the tailor? It needed a new method, not a change.",
    task="clean text and make a heading", challenge="Take the text \"  keep coding  \", strip the spaces, and print it in capital letters.",
    answer="Use print(\"  keep coding  \".strip().upper()), which shows KEEP CODING.",
    shorts=[
        ("String methods", "A method is a tool that belongs to a value. You write the string, a dot, the method name, and brackets. Upper makes capitals. Lower makes small letters. Strip removes spaces from the ends. Replace swaps one piece of text for another. These four tools clean almost any text. You use them in nearly every program.", "TEXT.UPPER()", "Four tools for text."),
        ("Split and join", "Split and join are partners. Split cuts a string at its spaces, and gives you a list of words. Join does the reverse. It glues a list of words into one string, with a separator you choose between them. So split a sentence, work on each word, and join it back. That small recipe powers search, counting and cleaning.", "SPLIT · JOIN", "Cut and glue."),
        ("New string every time", "Here is the key fact about string methods. They never change the original string. Upper does not make your old string uppercase. It returns a brand new string. The old one keeps its capitals, its spaces, everything. To keep the new version, tie it to a name. Text equals text dot strip. That is the pattern to follow.", "TEXT = TEXT.STRIP()", "Methods return new strings."),
        ("Item assignment error", "A common bug. You want to change one letter of a string, so you write name, bracket zero, equals G. Python says, type error, str object does not support item assignment. Strings are immutable. You can never change a letter in place. Make a new string with a method like capitalize, and tie your name to it.", "TYPEERROR: ITEM ASSIGNMENT", "Strings are immutable."),
        ("Pun and challenge", "Why did the string go to the tailor? It needed a new method, not a change. Your challenge. Take the text keep coding, with two spaces on each side. Strip the spaces, and print it in capital letters. You can chain the two methods in one line, one after the other. Post your answer in the comments below.", "STRIP, THEN UPPER", "Try two methods."),
    ],
))

EPISODES.append(dict(
    n=24, title="Indexing and slicing", spoken="indexing and slicing",
    yt="Python Indexing and Slicing: word[1:4]", thumb="INDEX AND SLICE",
    vis="Xecxec holding a long word with numbered boxes under each letter, from 0 at the left",
    goals=["pick one character with an index", "use negative indexes from the end", "cut a piece with a slice"],
    tags=["python string indexing", "python slicing", "negative index python", "indexerror"],
    hash=["#slicing", "#indexing"],
    analogy="a row of beach huts, each with a number painted on the door, starting from zero",
    c_title="Positions in a string",
    c_pts=["Every character has a position, starting at 0", "Negative positions count from the end", "word[start:stop] cuts a slice and stops before stop"],
    intro="Every character in a string has an address. Today we learn to pick characters and slices by position.",
    concept="Every character in a string has a position, called an index. It starts at zero. Think of a row of beach huts, each with a number on the door. The first hut is zero. You pick one with square brackets. Negative numbers count from the end, so minus one is the last character. A slice cuts a piece. Start, colon, stop. It includes the start, and stops before the stop, just like range.",
    A=dict(file="slice.py", label="Index and slice", on="one letter, the last letter, and three slices of Palolem",
           src='''
word = "Palolem"
print(word[0])
print(word[-1])
print(word[1:4])
print(word[:3])
print(word[3:])
''',
           narr="[HL 1] The word Palolem has seven letters, with positions zero to six. [HL 2] Position zero is the first letter, P. [HL 3] Minus one is the last letter, m. [HL 4] A slice from one to four takes positions one, two and three. That is a, l, o. The four is not included. [HL 5] Leaving out the start means, from the beginning. Pal. [HL 6] Leaving out the stop means, to the end. O, l, e, m.",
           label2="Reading the output", narr2="Predict first. [TRACK word=Palolem] Print zero gives P. Minus one gives m. One to four gives alo. Up to three gives Pal. From three gives olem. The two halves, Pal and olem, together make Palolem again, with the o shared at position three."),
    mem=dict(label="Slices make new strings", on="The name word tied to the string Palolem", names=["word"], **{"from": "A"},
             narr="Here is the one name we have. Word is tied to the string Palolem. Indexing and slicing do not change that string. Every slice makes a new string, and prints it, and forgets it, unless we tie a name to it. The original string is untouched. That fits with what we learned in the last episode."),
    B=dict(file="reverse.py", label="Steps and reverse", on="a third number in the slice sets the step",
           src='''
word = "Palolem"
print(word[::-1])
print(word[::2])
print(len(word))
''',
           narr="[HL 1] The same word. [HL 2] A slice can have a third number, the step. A step of minus one walks backwards. So the word prints reversed, m, e, l, o, l, a, P. [HL 3] A step of two takes every second letter, positions zero, two, four, six. P, l, l, m. [HL 4] The length is seven. The last valid index is always the length minus one."),
    term="Melolap, reversed, then P l l m, then seven.",
    recap=["Indexes start at zero.", "Negative indexes count from the end, with minus one as the last.", "A slice word[start:stop] stops before the stop.", "The last valid index is the length minus one."],
    bug=dict(title="an index too far", file="slice.py", wrong='''
word = "Palolem"
print(word[7])
''', fixed='''
word = "Palolem"
print(word[6])
''', wrong_note="Palolem has indexes 0 to 6", fixed_note="the last index is 6",
             why="A string of length 7 has indexes 0 to 6, so index 7 does not exist; the last valid index is always the length minus one.",
             narr="Bug of the Day. Palolem has seven letters, but the last index is six, because we start at zero. We ask for index seven. Python says, index error, string index out of range. The fix is to count from zero. Or use minus one, to always get the last letter, whatever the length."),
    pun="Why did the string stay calm in the slicing class? It knew where to cut.",
    task="print the first three and last three letters", challenge="Print the first three letters and the last three letters of the word \"Calangute\".",
    answer="Use word = \"Calangute\", then print(word[:3]) for Cal and print(word[-3:]) for ute.",
    shorts=[
        ("Positions start at zero", "Every character in a string has a position, called an index. The first one is zero, not one. So the word Palolem has indexes zero to six. Pick one with square brackets. Word, bracket zero, gives P. Think of a row of beach huts, numbered from zero. This is the same in almost every programming language, so learn it once.", "WORD[0]", "Counting from zero."),
        ("Negative indexes", "Negative indexes count from the end. Minus one is the last character. Minus two is the second last. So word, bracket, minus one, gives m, whatever the length of the word. It is the easiest way to grab the last letter, and you never need to count. Use negative indexes whenever you care about the end of a string.", "WORD[-1]", "Count from the end."),
        ("Slices", "A slice cuts a piece of a string. Word, bracket, one, colon, four, gives positions one, two and three. The start is included, and the stop is not, just like range. Leave out the start, and it begins at the beginning. Leave out the stop, and it runs to the end. One tool, many pieces, and the original is untouched.", "WORD[1:4]", "Start included, stop not."),
        ("Index error", "Here is the classic out of range bug. Palolem has seven letters, so the indexes are zero to six. Ask for index seven, and Python says, index error, string index out of range. The last index is always the length minus one. Or just use minus one. When you see this error, count again, starting from zero.", "INDEXERROR: OUT OF RANGE", "Count from zero."),
        ("Pun and challenge", "Why did the string stay calm in the slicing class? It knew where to cut. Your challenge. Take the word Calangute. Print the first three letters using a slice. Then print the last three letters, using a negative index inside the slice. Remember, you can leave out the start or the stop. Post your two answers in the comments.", "FIRST 3 AND LAST 3", "Try slicing."),
    ],
))

EPISODES.append(dict(
    n=25, title="Lists", spoken="lists",
    yt="Python Lists for Beginners: Create, Index, append", thumb="MEET THE LIST",
    vis="Xecxec carrying a basket with four beach names, each on a numbered card",
    goals=["create a list with square brackets", "read and change items by index", "add an item with append"],
    tags=["python lists", "python list append", "python list index", "list append returns none"],
    hash=["#lists", "#datastructures"],
    analogy="a shopping basket: you can add things, look at the first item, and swap one for another",
    c_title="A list holds many values",
    c_pts=["Square brackets and commas make a list", "Items have indexes, starting at 0", "Lists can be changed in place"],
    intro="So far every name held one value. Today we meet the list, a name that holds many.",
    concept="A list holds many values in one name. Square brackets, with commas between the items. Think of a shopping basket. You can add things, look at the first one, and swap one for another. Items have indexes, starting at zero, just like the letters of a string. But there is one big difference. Unlike strings, lists can be changed in place. Append adds a new item at the end.",
    A=dict(file="beaches.py", label="Making a list", on="a list of three beaches, then append a fourth",
           src='''
beaches = ["Baga", "Colva", "Anjuna"]
print(beaches)
print(beaches[0])
print(len(beaches))
beaches.append("Palolem")
print(beaches)
''',
           narr="[HL 1] A list of three beaches, in square brackets. [HL 2] Printing it shows the brackets and the commas. [HL 3] Index zero is the first item, Baga. [HL 4] Len counts the items. Three. [HL 5] Append adds a new item at the end. It changes the list itself. [HL 6] Print again, and the list now has four beaches.",
           label2="Reading the output", narr2="Predict first. First, the list of three. Then Baga. Then three. [TRACK beaches=Palolem] After the append, the same list now ends with Palolem. No new list was made. We changed the one list that the name beaches points at."),
    mem=dict(label="One name, one list object", on="The name beaches tied to one list holding four strings", names=["beaches"], **{"from": "A"},
             narr="Here is the picture. One name, beaches, tied to one list object. Inside the list are four string objects. When we appended Palolem, the list object grew. The name stayed tied to the same list. This is the big difference from strings and numbers. A list can change without being replaced."),
    B=dict(file="marks_list.py", label="Change an item", on="replace one mark and find the average",
           src='''
marks = [72, 85, 90]
marks[1] = 88
print(marks)
print(round(sum(marks) / len(marks), 1))
''',
           narr="[HL 1] A list of three marks. [HL 2] Assign to index one, and the second item changes from eighty five to eighty eight. This works on a list, but fails on a string. [HL 3] The list prints with the new value. [HL 4] Sum adds all the items, two hundred fifty. Len gives three. Divided, and rounded to one decimal, we get eighty three point three."),
    term="The list with eighty eight in the middle, then eighty three point three.",
    recap=["A list holds many values in square brackets.", "Items have indexes from zero, and negative indexes work too.", "A list can be changed in place, by index or by append.", "len, sum and max work on lists."],
    bug=dict(title="append returns None", kind="output", file="beaches.py", wrong='''
beaches = ["Baga", "Colva"]
beaches = beaches.append("Palolem")
print(beaches)
''', fixed='''
beaches = ["Baga", "Colva"]
beaches.append("Palolem")
print(beaches)
''', wrong_note="the result of append is saved in the name", fixed_note="call append and keep the list",
             why="append changes the list in place and returns None, so tying the name to its result replaces the list with None.",
             narr="Bug of the Day. We add Palolem, and print the list. It prints None. Why? Append changes the list in place, and returns nothing, which Python calls None. We tied the name to that nothing. The list is lost. Just call append on its own line, and keep the name pointing at the list."),
    pun="Why did the list never feel lonely? It always had items to keep it company.",
    task="make a list of 3 foods and add one", challenge="Make a list of three foods, add a fourth with append, and print the list and its length.",
    answer="Use food = [\"fish\", \"rice\", \"curry\"], food.append(\"prawns\"), then print(food) and print(len(food)). The length is 4.",
    shorts=[
        ("What is a list?", "A list holds many values in one name. You use square brackets, with commas between the items. Beaches equals bracket Baga, Colva, Anjuna, close bracket. Think of a shopping basket. You can add things, look at the first thing, and swap things. Lists are everywhere in Python, from names of students to marks on a test. Learn them well.", "[\"BAGA\", \"COLVA\"]", "A basket of values."),
        ("Index and length", "Items in a list have indexes, just like the letters of a string. The first item is index zero. Beaches, bracket zero, gives Baga. Beaches, bracket, minus one, gives the last item. And len of beaches counts the items. If you know how strings work, you already know most of lists. The rules are the same, so it is easy.", "BEACHES[0] · LEN(BEACHES)", "Same rules as strings."),
        ("Lists can change", "Here is the big difference from strings. A list can be changed in place. Assign to an index, and that item is replaced. Call append, and a new item is added at the end. The name stays tied to the same list object the whole time. The list itself grows or changes. That is what we mean when we say, a list is mutable.", "MARKS[1] = 88", "Lists are mutable."),
        ("Append returns None", "Here is a famous trap. You write beaches equals beaches dot append, Palolem. Then you print, and it says None. Append changes the list in place and returns nothing, which Python calls None. You tied the name to that nothing, and lost your list. Just call append on its own line. Do not save its result, ever.", "X = A.APPEND(1) → NONE", "Do not save append."),
        ("Pun and challenge", "Why did the list never feel lonely? It always had items to keep it company. Your challenge. Make a list of three foods you love. Add a fourth with append. Then print the list, and print its length. The length should now say four. Try printing just the last item, using a negative index. Share your list in the comments.", "A LIST OF FOODS", "Try a list."),
    ],
))

EPISODES.append(dict(
    n=26, title="List methods", spoken="list methods",
    yt="Python List Methods: insert, pop, remove", thumb="LIST METHODS",
    vis="Xecxec pulling an item out of a basket with a claw while another item drops in",
    goals=["add items with insert", "take items out with pop and remove", "check membership with in, and use count and index"],
    tags=["python list methods", "python insert pop remove", "python list remove error", "valueerror list remove"],
    hash=["#lists", "#listmethods"],
    analogy="a queue at a fish stall: someone can join at a place, the last person can leave, or you can ask a named person to leave",
    c_title="Changing a list",
    c_pts=["insert(i, x) puts x at position i", "pop() takes the last item out and gives it back", "remove(x) deletes the first x"],
    intro="Lists can grow, shrink and reorder. Today we learn the methods that do it.",
    concept="Lists come with methods that change them. Insert puts an item at a chosen position. Pop takes the last item out, and gives it back to you. Remove deletes the first item with a given value. Think of a queue at a fish stall. Someone can join at any place. The last person can leave. Or you can ask a named person to leave. All of these change the same list in place.",
    A=dict(file="queue.py", label="insert, pop and remove", on="a food list that grows and shrinks",
           src='''
food = ["fish", "rice"]
food.insert(1, "curry")
print(food)
last = food.pop()
print(last)
print(food)
food.remove("fish")
print(food)
''',
           narr="[HL 1] A list of two foods. [HL 2] Insert curry at position one. Everything from position one moves along. [HL 3] The list is now fish, curry, rice. [HL 4] Pop takes the last item out, and returns it. We tie it to the name last. [HL 5] Rice. [HL 6] The list has lost its last item. [HL 7] Remove deletes the first item equal to fish. [HL 8] Only curry is left.",
           label2="Reading the output", narr2="Predict first. [TRACK last=rice] First print, fish, curry, rice. Then rice, the popped item. Then fish, curry. Then curry alone. Pop gave us a value back, so we could keep it. Remove gave us nothing back. It just deleted."),
    mem=dict(label="The popped value gets its own name", on="food tied to a list of one item; last tied to the string rice", names=["food", "last"], **{"from": "A"},
             narr="Here is the picture after the code. Food is tied to a list with one item, curry. Last is tied to the string rice, which pop handed back. The string rice was removed from the list, but it still exists, because we tied a name to it. If we do not, Python removes it."),
    B=dict(file="check.py", label="count, index and in", on="questions you can ask a list",
           src='''
food = ["fish", "curry", "fish", "rice"]
print(food.count("fish"))
print(food.index("rice"))
print("curry" in food)
''',
           narr="[HL 1] A list with fish twice. [HL 2] Count tells us how many times fish appears. Two. [HL 3] Index tells us the position of rice. Zero, one, two, three. So three. [HL 4] And the word in asks a yes or no question. Is curry in the list? True. Use in before remove, to be safe."),
    term="Two, then three, then True.",
    recap=["insert puts an item at a chosen position.", "pop takes the last item out and returns it.", "remove deletes the first matching item.", "Use the word in to check before you remove."],
    bug=dict(title="removing something that is not there", file="queue.py", wrong='''
food = ["fish", "rice"]
food.remove("prawn")
''', fixed='''
food = ["fish", "rice"]
if "prawn" in food:
    food.remove("prawn")
print(food)
''', wrong_note="prawn is not in the list", fixed_note="check with in first",
             why="remove raises a ValueError when the item is not in the list, so check with the word in first.",
             narr="Bug of the Day. We ask the list to remove prawn, but prawn is not in the list. Python says, value error, x not in list. Remove does not quietly skip a missing item. It stops the program. Use the word in to check first, and only remove if the item is there."),
    pun="Why did the list get kicked out of the queue? It kept popping up at the end.",
    task="insert, pop and print", challenge="Start with [\"a\", \"b\", \"c\"]. Insert \"x\" at position 1, pop the last item, and print the list.",
    answer="Use letters.insert(1, \"x\") and letters.pop(), then print(letters), which shows ['a', 'x', 'b'].",
    shorts=[
        ("Insert and append", "Append adds an item at the end of a list. Insert adds an item at any position you choose. Food dot insert, one, curry puts curry at position one, and everything after it moves along by one place. Both methods change the list in place. Use append when order does not matter, and insert when it does. Print the list to see the result.", "FOOD.INSERT(1, \"CURRY\")", "Add at any place."),
        ("Pop", "Pop takes an item out of a list, and gives it back to you. With no number, it takes the last item. With a number, it takes the item at that position. So you can save the popped value in a name. That is useful for undo buttons, stacks, and queues. The list gets shorter, and you keep the item you took out.", "LAST = FOOD.POP()", "Take one out."),
        ("Remove and in", "Remove deletes the first item that equals a value. Food dot remove, fish, finds the first fish and deletes it. If the item is not there, Python raises an error. So check first with the word in. The question, is prawn in food, gives True or False. Use it in an if, and remove only when it is safe.", "\"FISH\" IN FOOD", "Check before you remove."),
        ("Value error", "Here is the bug. You call remove on something that is not in the list. Python says, value error, x not in list. Remove does not quietly skip a missing item. It stops your program. The fix is easy. Write an if with the word in, and only remove when the item is really there. Make it a habit for every remove.", "VALUEERROR: X NOT IN LIST", "Guard your remove."),
        ("Pun and challenge", "Why did the list get kicked out of the queue? It kept popping up at the end. Your challenge. Start with the list a, b, c. Insert x at position one. Pop the last item. Then print the list. Can you predict the answer before you run it? Write your prediction in the comments, then run the code to check.", "INSERT, POP, PRINT", "Try the list methods."),
    ],
))

EPISODES.append(dict(
    n=27, title="Looping with enumerate and zip", spoken="enumerate and zip",
    yt="Python enumerate and zip: Loop Like a Pro", thumb="ENUMERATE + ZIP",
    vis="Xecxec zipping two lists together like a jacket zip",
    goals=["loop over a list directly", "number items with enumerate", "walk two lists together with zip"],
    tags=["python enumerate", "python zip", "python loop over list", "modify list while looping"],
    hash=["#enumerate", "#zip"],
    analogy="a class register: each student has a roll number, and each roll number has a mark beside it",
    c_title="Better loops over lists",
    c_pts=["for item in list visits every item", "enumerate adds a counter", "zip pairs up two lists"],
    intro="Lists and loops are best friends. Today we meet two helpers that make list loops neat.",
    concept="You can loop over a list directly. For item in the list. No index needed. When you also want the position, use enumerate. It gives you a counter and the item together. When you have two lists that go together, use zip. It pairs them up, one from each. Think of a class register. Each student has a roll number, and each roll number has a mark beside it.",
    A=dict(file="enum.py", label="Numbering items", on="enumerate gives a counter and an item",
           src='''
beaches = ["Baga", "Colva", "Anjuna"]
for i, beach in enumerate(beaches, start=1):
    print(i, beach)
''',
           narr="[HL 1] A list of three beaches. [HL 2] Enumerate hands us two things each round, a counter and an item. We tie them to i and beach. Start equals one makes the count begin at one, not zero. [HL 3] Print both. One, Baga. Two, Colva. Three, Anjuna.",
           label2="Reading the output", narr2="Predict first. [TRACK i=1] Round one, i is one and beach is Baga. [TRACK i=3] Round three, i is three and beach is Anjuna. Without enumerate, you would have to keep your own counter. This is shorter, and it is hard to get wrong."),
    mem=dict(label="Two loop names", on="After the loop, i tied to 3 and beach tied to the string Anjuna", names=["i", "beach"], **{"from": "A"},
             narr="Look at the end state. After the loop, i is tied to the int three, and beach is tied to the string Anjuna. Both names were retied each round. The list itself was never touched. The beach name points to the same string that sits at the end of the list. No copy was made."),
    B=dict(file="zip_demo.py", label="Two lists together", on="zip pairs a name with its mark",
           src='''
names = ["Asha", "Ravi"]
marks = [88, 92]
for name, mark in zip(names, marks):
    print(name, "scored", mark)
''',
           narr="[HL 1] A list of names. [HL 2] And a list of marks, in the same order. [HL 3] Zip pairs them up. Round one gives Asha and eighty eight. Round two gives Ravi and ninety two. [HL 4] Print a sentence for each pair. If the lists have different lengths, zip stops at the shorter one."),
    term="Asha scored eighty eight. Ravi scored ninety two.",
    recap=["for item in list visits each item without an index.", "enumerate gives a counter and the item together.", "zip walks two lists in step.", "Do not change a list while you loop over it."],
    bug=dict(title="changing a list while looping", kind="output", file="enum.py", wrong='''
nums = [2, 4, 6, 8]
for n in nums:
    if n % 2 == 0:
        nums.remove(n)
print(nums)
''', fixed='''
nums = [2, 4, 6, 8]
for n in nums.copy():
    if n % 2 == 0:
        nums.remove(n)
print(nums)
''', wrong_note="the list shrinks while the loop walks it", fixed_note="loop over a copy",
             why="Removing items shifts the later items left, so the loop skips some; looping over a copy lets the original change safely.",
             narr="Bug of the Day. We want to remove every even number. All four are even, so the list should be empty. But it prints four and eight. Why? When we remove an item, the rest shift left. The loop moves on and skips the next one. Never change a list while looping over it. Loop over a copy instead, and change the original."),
    pun="Why did the list love enumerate? It finally got a number of its own.",
    task="print a numbered list of foods", challenge="Make a list of three foods, and print them numbered 1, 2, 3 using enumerate.",
    answer="Use for i, food in enumerate(foods, start=1): print(i, food).",
    shorts=[
        ("Loop over a list", "You can loop directly over a list. For beach in beaches. Python hands you each item in turn, and you never need an index. It reads like English, and it is hard to get wrong. Use this form whenever you only need the items. If you also need their position, there is a helper for that, and it is called enumerate.", "FOR BEACH IN BEACHES", "No index needed."),
        ("Enumerate", "When you need both the position and the item, use enumerate. For i, beach in enumerate of beaches. Each round gives you a counter and an item together. By default the counter starts at zero. Write start equals one to begin at one. It replaces the counter that you keep by hand. It is much safer.", "FOR I, X IN ENUMERATE(L)", "Count as you loop."),
        ("Zip", "When two lists go together, use zip. Names and marks, in the same order. For name, mark in zip of names, marks. Round one gives the first name and the first mark. Round two gives the second of each. Zip stops at the shorter list. Think of a class register, with names on one side and marks on the other.", "ZIP(NAMES, MARKS)", "Two lists in step."),
        ("The skipping bug", "A sneaky bug. You loop over a list, and remove items while you loop. The list shrinks, the items shift left, and the loop skips the next one. Four even numbers, and two are left behind, with no error at all. Loop over a copy instead, and change the original list. The fix is just dot copy.", "FOR N IN NUMS.COPY():", "Loop over a copy."),
        ("Pun and challenge", "Why did the list love enumerate? It finally got a number of its own. Your challenge. Make a list of three foods. Print them numbered one, two, three, using enumerate. Remember to set start equals one. Otherwise your list starts at zero. Then try with five foods, and check that your code still works. Share your code in the comments.", "A NUMBERED MENU", "Try enumerate."),
    ],
))

EPISODES.append(dict(
    n=28, title="Copying lists", spoken="copying lists",
    yt="Python Copying Lists: Why b = a Is Not a Copy", thumb="IS IT A COPY?",
    vis="Xecxec holding two name tags, A and B, both tied to the same list",
    goals=["see that b = a ties a second name to the same list", "make a real copy with copy() or a slice", "check with the is operator"],
    tags=["python copy list", "python alias list", "python shallow copy", "mutable lists python"],
    hash=["#copy", "#lists"],
    analogy="one house with two name boards: a visitor who repaints the house changes it for both names",
    c_title="One list, two names",
    c_pts=["b = a gives a second name to the same list", "copy() or a[:] makes a new list", "is checks if two names point to the same object"],
    intro="This is one of the most important ideas in Python, and it explains many strange bugs. Today we learn what copying really means.",
    concept="When you write b equals a, Python does not copy the list. It ties a second name to the same list. Think of one house with two name boards. A visitor who repaints the house changes it for both names. To make a real copy, call the copy method, or take a slice of everything. The is operator asks, are these two names tied to the very same object?",
    A=dict(file="alias.py", label="Two names, one list", on="b = a, then change b and look at a",
           src='''
a = [1, 2, 3]
b = a
b.append(4)
print(a)
print(a is b)
''',
           narr="[HL 1] A list of three numbers, tied to the name a. [HL 2] Now b equals a. This does not copy the list. It ties a second name, b, to the same list. [HL 3] We append four through the name b. [HL 4] And print a. The list printed through a also has the four. [HL 5] The is operator confirms it. A and b are tied to one object.",
           label2="Reading the output", narr2="Predict first. [TRACK b=1] We only changed b. But a prints one, two, three, four. Then, True. There is only one list, and two names for it. Anything that changes the list through one name shows up through the other."),
    mem=dict(label="Two names, one list", on="Two tags, a and b, with arrows to the same list object", names=["a", "b"], **{"from": "A"},
             narr="Here is the picture, and it is the most important one in this module. Two name tags, a and b, and two arrows that point at one list object. There is one list, holding one, two, three, four. Both names lead to it. That is why a change through b shows up in a. Remember this picture whenever lists behave oddly."),
    B=dict(file="copy_demo.py", label="Real copies", on="copy() and a slice both make a new list",
           src='''
a = [1, 2, 3]
b = a.copy()
c = a[:]
b.append(4)
print(a, b, c)
print(a is b)
''',
           narr="[HL 1] The original list. [HL 2] The copy method makes a brand new list with the same items. [HL 3] A slice with no start and no stop does the same job. [HL 4] Now we append four to b only. [HL 5] The original and c are untouched. Only b has the four. [HL 6] And is gives False. These are three separate lists."),
    term="A is one, two, three. B has the four. C is one, two, three. Then False.",
    recap=["b = a ties a second name to the same list.", "Changing the list through one name shows through the other.", "copy() and a[:] make a real, separate list.", "is tells you whether two names share one object."],
    bug=dict(title="b equals a is not a copy", kind="output", file="alias.py", wrong='''
a = [1, 2, 3]
b = a
b.append(4)
print(a)
''', fixed='''
a = [1, 2, 3]
b = a.copy()
b.append(4)
print(a)
''', wrong_note="we meant to leave a alone", fixed_note="b is a real copy",
             why="b = a only gives the same list a second name, so changing b changes a; use a.copy() to get an independent list.",
             narr="Bug of the Day. We wanted a copy, so we could change b and keep a safe. But a changed too. Because b equals a is not a copy. It is a second name for the same list. Call the copy method instead, and b becomes its own list. Now a stays exactly as it was."),
    pun="Why did the two names get along so well? They were pointing at the same thing.",
    task="make a safe copy and change it", challenge="Make a = [10, 20, 30]. Make a copy b, append 40 to b, and print both lists.",
    answer="Use b = a.copy() and b.append(40), then print(a, b), which shows [10, 20, 30] [10, 20, 30, 40].",
    shorts=[
        ("b equals a", "When you write b equals a, and a is a list, Python does not copy the list. It gives the same list a second name. There is still only one list. Think of one house with two name boards. If someone repaints the house, both names show the new colour. This one idea explains a very large share of strange bugs in Python programs.", "B = A", "Not a copy."),
        ("Two names, one list", "Here is the proof. A is a list of one, two, three. B equals a. Append four through b. Now print a, and it shows four as well. The is operator says True. A and b are two arrows pointing to one list. Anything you change through one name shows through the other. It is not a bug, it is how names work.", "A IS B → TRUE", "One object, two names."),
        ("A real copy", "To make a real copy of a list, call its copy method. B equals a dot copy. Or take a slice of everything, a bracket colon bracket. Either way, Python builds a brand new list with the same items. Now a and b are independent. Changing b does not touch a. Use copy whenever you need to change a list and keep the original safe.", "B = A.COPY()", "Make it independent."),
        ("The shared list bug", "A classic bug. You want a safe copy, so you write b equals a. You change b, and a changes too. No error, just wrong data. The fix is the copy method. B equals a dot copy. Now b is its own list, and a stays exactly as it was. Always ask yourself, do I need a second name, or a second list?", "A CHANGED?! USE COPY()", "Name or copy?"),
        ("Pun and challenge", "Why did the two names get along so well? They were pointing at the same thing. Your challenge. Make a list a, with ten, twenty, thirty. Make a real copy called b. Append forty to b only. Then print both lists. Check that a still has three items, and b has four. Post your result in the comments, please.", "COPY, CHANGE, PRINT", "Try a safe copy."),
    ],
))

EPISODES.append(dict(
    n=29, title="Tuples and unpacking", spoken="tuples and unpacking",
    yt="Python Tuples and Unpacking Explained", thumb="TUPLES",
    vis="Xecxec holding a sealed gift box labelled (15, 73) that cannot be opened and changed",
    goals=["make a tuple with round brackets", "unpack a tuple into names", "know that a tuple cannot be changed"],
    tags=["python tuples", "python tuple unpacking", "immutable tuple", "tuple item assignment error"],
    hash=["#tuples", "#unpacking"],
    analogy="a sealed envelope with a fixed set of papers inside: you can read them, but you cannot swap one",
    c_title="A fixed list",
    c_pts=["A tuple uses round brackets", "It can be read like a list but never changed", "Unpacking ties each item to its own name"],
    intro="Lists can change. Sometimes you want a collection that cannot. Today we meet the tuple.",
    concept="A tuple is like a list that cannot change. It uses round brackets. You can read items by index, count them with len, and loop over them. But you cannot assign to an item, append, or remove. Think of a sealed envelope. You can read the papers, but you cannot swap one. Unpacking is a neat trick. Write several names on the left, and Python ties one item to each name.",
    A=dict(file="point.py", label="Make and unpack", on="a tuple of latitude and longitude, unpacked",
           src='''
spot = (15, 73)
print(spot)
print(spot[0])
lat, lon = spot
print(lat, lon)
''',
           narr="[HL 1] A tuple with two numbers, in round brackets. [HL 2] Printing it shows the brackets. [HL 3] Index zero works, just like a list. Fifteen. [HL 4] Unpacking. Two names on the left, one tuple on the right. Python ties lat to the first item, and lon to the second. [HL 5] Print both names. Fifteen, seventy three.",
           label2="Reading the output", narr2="Predict first. [TRACK lat=15] The tuple prints with brackets. Then fifteen. Then lat and lon, fifteen and seventy three. Unpacking made two names from one tuple. The number of names must match the number of items. Otherwise Python raises an error."),
    mem=dict(label="A tuple and its unpacked names", on="Names spot, lat and lon tied to a tuple and two ints", names=["spot", "lat", "lon"], **{"from": "A"},
             narr="Here is the picture. Spot is tied to a tuple object holding fifteen and seventy three. Lat and lon are tied to the same two int objects that sit inside the tuple. Unpacking did not copy the numbers. It just tied a new name to each one. The tuple itself can never change."),
    B=dict(file="rest.py", label="Unpacking with a star", on="a star name collects the rest of the items",
           src='''
marks = (72, 85, 90)
low, mid, high = marks
print(low, high)
first, *rest = marks
print(first, rest)
''',
           narr="[HL 1] A tuple of three marks. [HL 2] Unpack into three names. Low, mid and high. [HL 3] Print the first and the last. Seventy two, ninety. [HL 4] A star in front of a name means, collect whatever is left, into a list. First gets seventy two. Rest gets eighty five and ninety. [HL 5] Print both. The rest is a list."),
    term="Seventy two, ninety, then seventy two and a list with eighty five and ninety.",
    recap=["A tuple uses round brackets and cannot be changed.", "Index, len and loops work on tuples.", "Unpacking ties each item to its own name.", "A star name collects the leftover items into a list."],
    bug=dict(title="changing a tuple item", file="point.py", wrong='''
spot = (15, 73)
spot[0] = 20
''', fixed='''
spot = (15, 73)
spot = (20, spot[1])
print(spot)
''', wrong_note="we try to change one item", fixed_note="build a new tuple",
             why="Tuples are immutable, so an item cannot be assigned; build a new tuple and tie the name to it.",
             narr="Bug of the Day. We try to change the first number of the tuple. Python says, type error. A tuple object does not support item assignment. Tuples are sealed. If you need a different tuple, build a new one, and tie the name to it. If you need to change items often, use a list instead."),
    pun="Why did the tuple refuse to change? It was already set in its ways.",
    task="unpack a tuple of three", challenge="Make rgb = (255, 128, 0). Unpack it into r, g and b, and print the three names.",
    answer="Use r, g, b = rgb and then print(r, g, b), which shows 255 128 0.",
    shorts=[
        ("What is a tuple?", "A tuple is like a list that cannot change. It uses round brackets. You can read items by index, count them with len, and loop over them. But you cannot assign to an item, or append, or remove. Use a tuple when the values belong together and should never change, like a latitude and longitude. It tells every reader, this is fixed.", "(15, 73)", "A list that is sealed."),
        ("Unpacking", "Unpacking is a lovely trick. Write several names on the left, and a tuple on the right. Python ties the first name to the first item. It ties the second name to the second item, and continues like this. Lat, comma, lon, equals spot. Two names, two values, one line. The number of names must match the number of items, or Python raises an error.", "LAT, LON = SPOT", "Many names, one line."),
        ("The star name", "A star in front of a name means, collect everything that is left. First, comma, star rest, equals a tuple of three marks. First gets the first mark. Rest gets a list of the others. This is useful when you only care about the head of a collection, and want the tail as a bundle. It works with lists too.", "FIRST, *REST = MARKS", "Collect the leftovers."),
        ("Tuples are sealed", "Here is the bug. You try to change one item of a tuple. Spot, bracket zero, equals twenty. Python says, type error, tuple object does not support item assignment. Tuples are immutable. They are sealed on purpose. Build a new tuple if you need different values. Or use a list, if the values must change often. Pick the right tool.", "TYPEERROR: TUPLE ITEM", "Sealed on purpose."),
        ("Pun and challenge", "Why did the tuple refuse to change? It was already set in its ways. Your challenge. Make a tuple called rgb, holding two fifty five, one twenty eight, and zero. Unpack it into three names, r, g and b. Then print the three names on one line. You should see the three numbers, in order. Post your code in the comments.", "UNPACK THREE COLOURS", "Try unpacking."),
    ],
))

EPISODES.append(dict(
    n=30, title="Sorting", spoken="sorting",
    yt="Python Sorting: sort(), sorted() and key", thumb="SORT IT",
    vis="Xecxec lining up pebbles from smallest to biggest",
    goals=["sort a list in place with sort()", "make a sorted copy with sorted()", "sort by a rule using key="],
    tags=["python sort", "python sorted", "python sort key", "sort returns none"],
    hash=["#sorting", "#lists"],
    analogy="lining up students by height: you can reorder the real line, or just write down a sorted copy on paper",
    c_title="Two ways to sort",
    c_pts=["list.sort() reorders the list itself", "sorted(list) returns a new sorted list", "key= sorts by a rule, reverse=True flips the order"],
    intro="Putting things in order is a job every program needs. Today we learn Python's two sorting tools.",
    concept="Python has two ways to sort. The sort method reorders the list itself, in place, and returns nothing. The sorted function leaves the original alone, and gives you a new sorted list. Think of lining up students by height. You can move the real students, or you can write a sorted copy on paper. Reverse equals True flips the order. And key lets you sort by a rule.",
    A=dict(file="sorting.py", label="sort and sorted", on="sort in place; sorted makes a new list",
           src='''
nums = [30, 5, 12, 8]
nums.sort()
print(nums)
print(sorted([3, 1, 2], reverse=True))
print(nums)
''',
           narr="[HL 1] A list of four numbers, not in order. [HL 2] Sort reorders the list itself, smallest to biggest. [HL 3] Printing it shows five, eight, twelve, thirty. [HL 4] Sorted builds a new list, from a different list, and reverse equals True makes it biggest first. [HL 5] The nums list is still in its sorted order. Sorted did not touch it.",
           label2="Reading the output", narr2="Predict first. [TRACK nums=30] The first print shows five, eight, twelve, thirty. The second shows three, two, one. The third shows the same as the first. Sort changed the list in place. Sorted gave us a separate list, and left the original alone."),
    mem=dict(label="In-place sorting", on="The name nums tied to one list; sort reorders that same list", names=["nums"], **{"from": "A"},
             narr="Here is the picture. Nums is tied to one list. When we call sort, that same list is reordered, and the name stays tied to it. Nothing new is made. Sorted, on the other hand, builds a second list. In this program, we gave that new list no name, so Python forgot it after the print."),
    B=dict(file="key_demo.py", label="Sort by a rule", on="sorting words alphabetically and by length",
           src='''
words = ["banana", "fig", "apple"]
print(sorted(words))
print(sorted(words, key=len))
''',
           narr="[HL 1] A list of three words. [HL 2] Sorted with no options puts words in alphabetical order. Apple, banana, fig. [HL 3] With key equals len, Python measures each word first, and sorts by that number. Fig has three letters, apple five, banana six. Notice that we wrote len with no brackets. We hand Python the tool, and Python uses it on each item."),
    term="Apple, banana, fig. Then fig, apple, banana.",
    recap=["list.sort() sorts in place and returns None.", "sorted() returns a new list and leaves the original alone.", "reverse=True gives the biggest first.", "key= sorts by a rule, like len."],
    bug=dict(title="sort returns None", kind="output", file="sorting.py", wrong='''
nums = [3, 1, 2]
result = nums.sort()
print(result)
''', fixed='''
nums = [3, 1, 2]
result = sorted(nums)
print(result)
''', wrong_note="the result of sort is saved", fixed_note="sorted returns the new list",
             why="list.sort() sorts in place and returns None, so saving its result gives None; use sorted() when you want a new list back.",
             narr="Bug of the Day. We sort the list and save the result. We print it, and get None. Sort changes the list in place, and returns nothing, just like append. If you want a new sorted list to save, use the sorted function. Or call sort on its own line, and keep using the original list."),
    pun="Why was the list so organised? It always knew its place in line.",
    task="sort marks high to low", challenge="Sort the list [64, 91, 72, 88] from highest to lowest and print it.",
    answer="Use print(sorted([64, 91, 72, 88], reverse=True)), which shows [91, 88, 72, 64].",
    shorts=[
        ("Sort in place", "The sort method puts a list in order, right where it is. Nums dot sort, with brackets, and the list is reordered, smallest to biggest. The same list object changes. Sort returns nothing, so you do not save its result. Use it when you do not need the old order any more, and you want the list itself sorted.", "NUMS.SORT()", "Reorder the list."),
        ("Sorted makes a copy", "The sorted function is different. It takes any list, and gives you a new sorted list. The original stays in its old order. Use it when you need both the old and the new order. Also use it for a sorted view for printing. Add reverse equals True, and the biggest item comes first. Sorted never changes the original.", "SORTED(NUMS)", "A new sorted list."),
        ("Sort by a rule", "The key option sorts by a rule. Sorted of words, key equals len, sorts words by their length. Fig has three letters, apple five, banana six. Python measures each word with len, then sorts by those numbers. Notice there are no brackets after len. You hand Python the tool, and Python uses it on each item in turn.", "KEY=LEN", "Sort by length."),
        ("Sort returns None", "Another None bug. You write result equals nums dot sort, and print the result. It says None. Sort changes the list in place and returns nothing, just like append. If you want a new sorted list to save, use the sorted function instead. Or call sort on its own line, and keep using the same list name afterwards.", "X = A.SORT() → NONE", "Use sorted to save."),
        ("Pun and challenge", "Why was the list so organised? It always knew its place in line. Your challenge. Take the list sixty four, ninety one, seventy two, eighty eight. Sort it from the highest to the lowest. Print the result. You should see ninety one first. Try it with sort, and then with sorted. Which one is easier to print? Tell us in the comments.", "HIGH TO LOW", "Try sorting."),
    ],
))

EPISODES.append(dict(
    n=31, title="2D lists", spoken="two-dimensional lists",
    yt="Python 2D Lists: Lists of Lists Explained", thumb="LISTS OF LISTS",
    vis="Xecxec standing on a chessboard-like grid of numbers",
    goals=["build a list of lists", "read and change one cell with two indexes", "loop over rows and cells"],
    tags=["python 2d list", "python nested list", "python grid", "list multiplication bug"],
    hash=["#2dlist", "#grid"],
    analogy="a cinema seating chart: a row number and a seat number find one seat",
    c_title="A grid of values",
    c_pts=["A 2D list is a list of lists", "board[row][col] picks one cell", "Loop rows with an outer loop and cells with an inner loop"],
    intro="Tables, boards and grids are everywhere. Today we build them from lists inside lists.",
    concept="A two dimensional list is a list whose items are lists. Each inner list is a row. Think of a cinema seating chart. A row number and a seat number find one seat. In Python, board, bracket, row, bracket, column. The first bracket picks the row. The second picks the item in that row. You loop over a grid with an outer loop for rows and an inner loop for cells.",
    A=dict(file="board.py", label="Rows and cells", on="a 2 by 3 grid, one row, one cell, one change",
           src='''
board = [[1, 2, 3], [4, 5, 6]]
print(board[0])
print(board[1][2])
board[0][0] = 9
print(board)
''',
           narr="[HL 1] A list with two items, and each item is a list of three numbers. Two rows, three columns. [HL 2] Board bracket zero is the whole first row. [HL 3] Board bracket one, bracket two. Row one, column two. The six. [HL 4] Assign to a cell, and that one number changes. [HL 5] Print the whole board, and the nine sits at the start of row zero.",
           label2="Reading the output", narr2="Predict first. [TRACK board=9] The first print is one, two, three. The second is six. The third shows the grid with nine at the top left. Rows come first, columns second. Say it aloud while you type, row, then column."),
    mem=dict(label="Lists inside a list", on="One name, board, tied to a list of two row lists", names=["board"], **{"from": "A"},
             narr="Here is the picture. One name, board, tied to one outer list. The outer list holds two arrows, one for each row. Each row is its own list, with its own numbers. A grid in Python is not a flat block. It is a list that points at other lists. That fact matters for the bug of the day."),
    B=dict(file="grid_total.py", label="Loop over a grid", on="an outer loop for rows, an inner loop for cells",
           src='''
board = [[1, 2, 3], [4, 5, 6]]
total = 0
for row in board:
    for cell in row:
        total = total + cell
print(total)
''',
           narr="[HL 1] The same board. [HL 2] A running total, starting at zero. [HL 3] The outer loop walks over the rows. Each row is a list. [HL 4] The inner loop walks over the cells of that row. [HL 5] Add each cell to the total. [HL 6] After all six cells, the total is twenty one. This is the accumulator pattern, inside a nested loop."),
    term="Twenty one.",
    recap=["A 2D list is a list of lists.", "board[row][col] picks one cell, row first.", "An outer loop walks rows and an inner loop walks cells.", "Never build a grid by multiplying a list of lists."],
    bug=dict(title="rows that share one list", kind="output", file="board.py", wrong='''
grid = [[0] * 3] * 3
grid[0][0] = 1
print(grid)
''', fixed='''
grid = []
for row in range(3):
    grid.append([0] * 3)
grid[0][0] = 1
print(grid)
''', wrong_note="the multiply makes three names for one row", fixed_note="build each row separately",
             why="Multiplying a list of lists repeats the same inner list three times, so all rows are one object; build each row separately.",
             narr="Bug of the Day. We build a three by three grid of zeros, and set the top left cell to one. But three cells changed, one in every row. Multiplying a list repeats the same inner list three times. All three rows are one list. Build each row separately in a loop, and each row gets its own list."),
    pun="Why did the 2D list never get lost? It always knew its row and column.",
    task="make a 3 by 3 grid and change the middle", challenge="Build a 3 by 3 grid of zeros using a loop. Set the middle cell to 5 and print the grid.",
    answer="Build grid with grid.append([0] * 3) three times, then grid[1][1] = 5 and print(grid), which shows [[0, 0, 0], [0, 5, 0], [0, 0, 0]].",
    shorts=[
        ("A list of lists", "A two dimensional list is a list whose items are lists. Each inner list is a row. Board equals bracket, bracket one, two, three, close, comma, bracket four, five, six, close, close. Two rows, three columns. Use it for tables, boards, seating charts, or anything laid out in rows and columns. Python has no special grid type, only lists inside lists.", "[[1, 2, 3], [4, 5, 6]]", "A grid of values."),
        ("Row, then column", "To pick one cell of a grid, use two indexes. Board, bracket one, bracket two. The first bracket picks the row. The second picks the item inside that row. Row one, column two, gives six. Say row first, column second, every time, until it feels natural. You can assign to a cell too, and only that one number changes.", "BOARD[1][2]", "Two brackets, one cell."),
        ("Loop over a grid", "To visit every cell, use two loops. The outer loop walks over the rows. The inner loop walks over the cells in that row. Add each cell to a total, and you get the sum of the whole grid. This is the accumulator pattern, inside a nested loop. The same shape works for printing, searching, and counting cells.", "FOR ROW IN BOARD:", "Rows, then cells."),
        ("Rows that share", "Here is a famous trap. You build a grid with bracket zero times three, close bracket, times three. You set one cell to one, and three cells change. The multiply repeated the same row three times. All the rows are one list. Build each row in a loop instead, and every row is its own separate list.", "[[0]*3]*3 SHARES ROWS", "Build rows separately."),
        ("Pun and challenge", "Why did the two D list never get lost? It always knew its row and column. Your challenge. Build a three by three grid of zeros, using a loop. Make the middle cell equal to five. Then print the whole grid. Remember the middle is row one, column one, because we count from zero. Share your grid in the comments below.", "THE MIDDLE CELL", "Try a grid."),
    ],
))

EPISODES.append(dict(
    n=32, title="Mini project: Marks tracker", spoken="the marks tracker mini project",
    yt="Python Mini Project: Marks Tracker With Lists", thumb="MARKS TRACKER",
    vis="Xecxec holding a report card with a pencil and a list of marks",
    goals=["collect marks from the user into a list", "find the highest mark and the average", "guard against dividing by zero"],
    tags=["python mini project", "python marks tracker", "python average list", "zerodivisionerror"],
    hash=["#project", "#lists"],
    analogy="a teacher's register: collect the marks, find the topper, then work out the class average",
    c_title="Planning the tracker",
    c_pts=["Ask for each mark and append it to a list", "Use max, sum and len for the results", "Guard the average against an empty list"],
    intro="Time for a second project. Today we build a marks tracker with a list.",
    concept="Here is the plan. Ask the user for three marks, and append each one to a list. Then report the marks, the highest one, and the average. We use the tools from this module. A loop, a list, append, and the built in functions max, sum and len. And one important guard. An average of an empty list divides by zero. We see that in the bug of the day.",
    A=dict(file="tracker.py", label="The tracker", on="collect three marks, then report",
           src='''
marks = []
for n in range(3):
    marks.append(int(input("Mark: ")))
print("Marks:", marks)
print("Highest:", max(marks))
print("Average:", round(sum(marks) / len(marks), 1))
''',
           stdin="72\n85\n90\n",
           narr="[HL 1] An empty list to collect the marks. [HL 2] A loop that runs three times. [HL 3] Ask for a mark, convert it with int, and append it to the list. [HL 4] Print the whole list. [HL 5] Max finds the highest mark. [HL 6] Sum divided by len is the average. Round makes it neat, to one decimal.",
           label2="Reading the output", narr2="Predict first. The user types seventy two, eighty five and ninety. [TRACK n=2] After the loop, the list holds all three. The highest is ninety. The average is two hundred forty seven divided by three, which rounds to eighty two point three."),
    mem=dict(label="A list that grew", on="The name marks tied to a list of three ints", names=["marks"], **{"from": "A"},
             narr="Here is the end state. The name marks is tied to one list, holding the three ints that the user typed. We started with an empty list, and appended once in each round. The list grew each time, but the name never moved. Max, sum and len all read this same list."),
    B=dict(file="pass_count.py", label="Counting passes", on="count how many marks are 40 or above",
           src='''
marks = [72, 35, 90, 28, 64]
passed = 0
for m in marks:
    if m >= 40:
        passed = passed + 1
print("Passed:", passed, "of", len(marks))
print("Top:", max(marks), "Lowest:", min(marks))
''',
           narr="[HL 1] Five marks. [HL 2] A counter, starting at zero. [HL 3] Loop over the marks. [HL 4] If a mark is forty or more, [HL 5] count one more pass. [TRACK passed=3] Three marks passed. [HL 6] Print the passes out of the total. [HL 7] And the top and lowest marks, with max and min."),
    term="Passed three of five. Top ninety, lowest twenty eight.",
    recap=["Start with an empty list and append in a loop.", "max, min, sum and len work on lists of numbers.", "A counter with an if counts how many pass a test.", "Check for an empty list before you divide by its length."],
    bug=dict(title="average of an empty list", file="tracker.py", wrong='''
marks = []
print(sum(marks) / len(marks))
''', fixed='''
marks = []
if marks:
    print(sum(marks) / len(marks))
else:
    print("No marks yet")
''', wrong_note="the list has no items", fixed_note="check the list first",
             why="An empty list has length zero, and dividing by zero raises an error; test the list before you divide.",
             narr="Bug of the Day. The list is empty, so len is zero. The sum is zero, and dividing by zero is a zero division error. Python says, division by zero. Check the list first. An empty list counts as False, so a plain if marks does the job. Then print a friendly message instead of crashing."),
    pun="Why did the marks tracker get top marks? It always added up.",
    task="add a Failed count to the tracker", challenge="Extend the pass counter: also print how many marks are below 40.",
    answer="Add failed = len(marks) - passed and print(\"Failed:\", failed). With the sample marks it prints Failed: 2.",
    shorts=[
        ("The tracker plan", "Let us build a marks tracker. Start with an empty list. A loop asks for three marks, and appends each one. Then we print the whole list, the highest mark with max, and the average with sum divided by len. It uses the loop, the list, and the built in functions you already know. Plan on paper first, then type it.", "A MARKS TRACKER", "Our second project."),
        ("Max, min, sum, len", "Four built in functions do the heavy work on a list of numbers. Max gives the biggest. Min gives the smallest. Sum adds everything. Len counts the items. Sum divided by len is the average. You do not need a loop for any of them. Learn these four, and a list of marks becomes a mini report in four lines.", "MAX · MIN · SUM · LEN", "Four helpers."),
        ("Count the passes", "To count passes, use a counter. Start at zero. Loop over the marks. If a mark is forty or more, add one. After the loop, the counter says how many passed. Pair it with len, and you can print, passed three of five. This is the same counter pattern from the loop patterns episode, now on a list.", "PASSED = PASSED + 1", "A counter on a list."),
        ("Divide by zero", "Here is the bug that crashes trackers. The list is empty, so len is zero. Sum divided by len is a division by zero, and Python raises a zero division error. Check the list first. An empty list counts as False, so a simple if marks is enough. Then print a friendly message, and the program survives.", "ZERODIVISIONERROR", "Guard the average."),
        ("Pun and challenge", "Why did the marks tracker get top marks? It always added up. Your challenge. Take the pass counter program, and extend it. Also print how many marks are below forty. You can count them with a second counter, or subtract the passes from the length. Which way is shorter? Post your improved version in the comments below, and show your output.", "COUNT THE FAILS", "Extend the tracker."),
    ],
))
