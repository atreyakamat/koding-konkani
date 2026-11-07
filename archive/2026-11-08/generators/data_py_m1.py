import re
# Python course, Module 1 (EP5-12)
import data_py as P
MOD1 = dict(module=1, mod_name="Variables, types and input", bgacc="Pastel Blue + Tomato")
TC, CS, CE, MB, TM, BG, PC, CH, OU = P.TC, P.CS, P.CE, P.MB, P.TM, P.BG, P.PC, P.CH, P.OU
std_scenes = P.std_scenes

def S(id, title, built, hook, script, on, caption, tags):
    return dict(id=id, title=title, built=built, hook=hook, script=script, on=on, caption=caption, tags=tags)

def chapters(*labels):
    # labels for scenes 2..6, then Recap is 7, Bug 8, Challenge 10, Next 11
    d = {1: "Intro"}
    for i, l in enumerate(labels, 2):
        d[i] = l
    d.update({6: labels[4], 7: "Recap", 8: "Bug of the Day", 10: "Challenge", 11: "Next episode"})
    return d

TAGS = lambda *t: list(t) + ["koding konkani", "learn programming", "class 11 computer science", "coding in goa"]

# ---------------------------------------------------------------- EP5
E5_CODE = '''# Xecxec keeps score
fish = 3
price = 120
total = fish * price
fish = 5
print("Total:", total)
print("Fish now:", fish)'''
E5_BUG = 'print("Total:", total)\ntotal = 360'
E5_FIX = 'total = 360\nprint("Total:", total)'

EP5 = dict(ep=5, title="Variables and names", prereq="EP 04", **MOD1,
 goals=["create a variable with = and give it a good name", "explain that a name is a tag tied to a value", "see that changing fish later does not change total"],
 yt=dict(title="Variables and Names in Python | Python Programming EP 05",
   desc="Learn what a variable really is in Python, and why changing one name does not change another, with Xecxec the crab.",
   tags=TAGS("python variables", "python for beginners", "python tutorial", "assignment in python", "python names", "nameerror"),
   thumb_text="VARIABLES", thumb_visual="in tomato on pastel blue; Xecxec holding two name tags tied to the numbers 3 and 120; thin black border and drop shadow.",
   chapters=chapters("What is a variable?", "Make three names", "Tags on values", "Follow the values", "Run it")),
 files=[dict(name="variables.py", source=E5_CODE, scene="3, 5")],
 scenes=std_scenes((5, "VARIABLES"),
   "Welcome back to Koding Konkani! Module one starts today. Every program needs to remember things, like a score or a price. Today we learn how Python remembers, using variables.",
   ("What is a variable", '"What is a variable?": three numbered lines and a name-tag analogy card', "Lines spring in one by one with a pop; the name-tag card slides in from the right",
    "A variable is a name for a value. You write the name, an equals sign, and the value. Python stores the value, and ties the name to it, like a tag on a fish crate. Equals here does not mean the same as in maths. It means, tie this name to that value. Pick names that say what they hold, like fish and price, not x and y."),
   ("Make three names", "`variables.py`: five assignments, then two prints; line 4 is the star",
    "[HL 2] [TRACK fish=3] The name fish is tied to three. [HL 3] [TRACK price=120] The name price is tied to one hundred twenty. [HL 4] [TRACK total=360] Now Python works out fish times price, which is three hundred sixty, and ties total to it. The right side is worked out first, and then the name is tied. Python works out the number once, right there. It does not remember the formula."),
   ("Tags on values", "Three name tags, fish, price and total, tied by arrows to the values 3, 120 and 360",
    "Three tags pop in with arrows to the values; the fish arrow later swings from 3 to 5 while the total arrow stays on 360",
    "Look at the picture. Fish points at three. Price points at one hundred twenty. Total points at three hundred sixty. When you write fish equals five, Python moves only the fish arrow. It now points at five. The total arrow stays on three hundred sixty, because that number was worked out earlier. A name is a tag, and tags can be moved to other values.", MB),
   ("Follow the values", "`variables.py` again with the output panel on the right",
    "[HL 5] [TRACK fish=5] Line five ties fish to a new value, five. [HL 4] Line four does not run again. So total is still three hundred sixty. [HL 6] The first print shows, Total, three hundred sixty. [HL 7] The second print shows, Fish now, five. Predict before you run. If total changed with fish, it would be six hundred. It does not. Python runs lines once, in order."),
   ("Run it", "Terminal: `python variables.py`",
    "Run it. Total, three hundred sixty. Fish now, five. Total did not follow fish. Change the price and run it again, and see which numbers move."),
   ("Bug of the Day", "BUG OF THE DAY: using a name before it exists",
    "Bug of the Day. We print total on line one, before we tie it to a value on line two. Python says, name error, name total is not defined. Python reads from the top, and at line one, total does not exist yet. Swap the two lines, and it works. Always create a name before you use it."),
   ("My variable and I broke up. I assigned it a new value.", "My variable and I broke up. I assigned it a new value."),
   ("Task card: swap two variables without losing a value", "Your challenge: make two variables, a equals one and b equals two, and swap them. After the swap, a is two and b is one. Comment your answer below."),
   ("Next: EP 06 · Numbers: int and float", "Next time: numbers, whole and decimal. Keep coding, says Xecxec!")),
 bug=dict(file="vb.py", intro="total is printed on line 1, before it is created on line 2", wrong=E5_BUG, fix_intro="the lines are swapped", fixed=E5_FIX, expect=["NameError: name 'total' is not defined"],
   why="Python runs top to bottom, so a name must be tied to a value before any line uses it."),
 pun="\"My variable and I broke up. I assigned it a new value.\"",
 challenge="Make a = 1 and b = 2, then swap them so that a is 2 and b is 1.",
 answer="Use a third name: temp = a, then a = b, then b = temp; or in one line, a, b = b, a. Both give a = 2 and b = 1.",
 answer_code='a = 1\nb = 2\ntemp = a\na = b\nb = temp\nprint(a, b)',
 shorts=[
  S("S1", "What is a variable?", [2], "A name tied to a value.", "A name tied to a value. Write the name, an equals sign, and the value. Python stores the value and ties the name to it, like a tag on a fish crate.", "VARIABLE = NAME + VALUE", "Variables in 30 seconds.", ["python", "variables", "beginners", "kodingkonkani", "goa"]),
  S("S2", "Equals is not maths", [3], "Equals does not mean equal.", "Equals does not mean equal. It means, tie this name to that value. Python works out the right side first, then ties the name on the left.", "= MEANS TIE THE NAME", "What equals really means.", ["python", "assignment", "learntocode", "kodingkonkani", "coding"]),
  S("S3", "Names are movable tags", [4], "Move the tag, not the number.", "Move the tag, not the number. Fish points at three. Say fish equals five, and the tag swings to five. The total tag stays where it was.", "FISH MOVES, TOTAL STAYS", "Names are tags.", ["python", "memory", "variables", "kodingkonkani", "coding"]),
  S("S4", "Name is not defined", [8], "Use a name before it exists.", "Use a name before it exists, and Python says, name error, name total is not defined. Python reads from the top, so create the name first.", "NAMEERROR: NAME NOT DEFINED", "Create it before you use it.", ["python", "bugfix", "nameerror", "kodingkonkani", "coding"]),
  S("S5", "Pun and challenge", [9, 10], "My variable and I broke up.", "My variable and I broke up. I assigned it a new value. Your challenge: swap two variables, a and b, without losing a value. Full video: EP 5.", "SWAP A AND B", "Try the swap challenge.", ["python", "codingchallenge", "kodingkonkani", "programmingjokes", "goa"]),
 ])

# ---------------------------------------------------------------- EP6
E6_CODE = '''cups = 3
tea = 12.5
bill = cups * tea
print("Bill:", bill)
print(type(cups), type(tea))
print(8 / 2)'''
E6_BUG = 'total = 0.1 + 0.2\nassert total == 0.3, "total should be 0.3"'
E6_FIX = 'total = 0.1 + 0.2\nassert round(total, 2) == 0.3, "total should be 0.3"\nprint(total)\nprint(round(total, 2))'

EP6 = dict(ep=6, title="Numbers: int and float", prereq="EP 05", **MOD1,
 goals=["tell an int from a float and check with type()", "know that / always gives a float", "use round() when decimal noise matters"],
 yt=dict(title="Numbers in Python: int and float | Python Programming EP 06",
   desc="Whole numbers, decimals, and why 0.1 plus 0.2 is not quite 0.3, with Xecxec the crab.",
   tags=TAGS("python int float", "python numbers", "python for beginners", "python tutorial", "floating point", "python round"),
   thumb_text="INT OR FLOAT?", thumb_visual="in tomato on pastel blue; Xecxec between a whole-number crate marked 3 and a decimal crate marked 12.5; thin black border and drop shadow.",
   chapters=chapters("Two kinds of numbers", "Cups of tea", "Why 0.1 + 0.2 is odd", "Follow the types", "Run it")),
 files=[dict(name="numbers.py", source=E6_CODE, scene="3, 5")],
 scenes=std_scenes((6, "INT OR FLOAT?"),
   "Welcome back! Last time we tied names to values. Today the values are numbers. Python has two kinds, and knowing which is which saves you from strange answers.",
   ("Two kinds of numbers", '"Two kinds of numbers": three numbered lines and a crates analogy card', "Lines spring in with a pop; the card shows a whole-fish crate and a weighing scale",
    "Python has two main kinds of numbers. An int is a whole number, like three or one hundred. A float has a decimal point, like twelve point five. Think of counting fish, and weighing fish. Counting gives whole numbers. Weighing gives decimals. Python decides the kind from how you write the number, so three is an int, and three point zero is a float."),
   ("Cups of tea", "`numbers.py`: cups, tea, bill, and three prints",
    "[HL 1] [TRACK cups=3] Cups is the whole number three. [HL 2] [TRACK tea=12.5] Tea is twelve point five, so it is a float. [HL 3] [TRACK bill=37.5] Bill is cups times tea. An int times a float always gives a float, so we get thirty seven point five. [HL 4] Print the label and the bill. [HL 5] The type function tells us the kind of each value. [HL 6] And what about eight divided by two?"),
   ("Why 0.1 + 0.2 is odd", "Two boxes: whole numbers are exact; decimals are close; a warning card shows 0.30000000000000004",
    "Two cards pop in side by side; the decimal card wobbles and shows 0.30000000000000004 in tomato",
    "Whole numbers are exact. Decimals are not always. A computer stores floats in binary, and some decimals, like point one, cannot be written exactly in binary. So point one plus point two gives point three, followed by a tiny tail of zeros and a four. This is not a Python bug. Every language does it. When it matters, use the round function.", CS),
   ("Follow the types", "`numbers.py` again with the output panel on the right",
    "[HL 4] Three times twelve point five is thirty seven point five. [HL 5] The type of cups is int. The type of tea is float. [HL 6] Here is the surprise. Eight divided by two prints four point zero, not four. The slash always gives a float, even when the answer looks whole. Predict first, then check. Slash means a float. Always."),
   ("Run it", "Terminal: `python numbers.py`",
    "Run it. Bill, thirty seven point five. Class int, class float. And four point zero. Try changing cups to a float, and see what happens to the types."),
   ("Bug of the Day", "BUG OF THE DAY: an assert that fails on decimals",
    "Bug of the Day. We check that point one plus point two equals point three, using assert. Python says, assertion error, total should be point three. The sum has a tiny tail, so the check fails. Fix it by rounding to two places first. Never compare decimals with a plain equals check."),
   ("Zero point one plus zero point two walked into a bar and ordered zero point three. The bartender said: close enough.", "Zero point one plus zero point two walked into a bar and ordered zero point three. The bartender said: close enough."),
   ("Task card: a bill with a float price; print its type", "Your challenge: set price to nineteen point five and quantity to four. Print the total and its type."),
   ("Next: EP 07 · Strings", "Next time: strings, which is how Python handles text. Keep coding, says Xecxec!")),
 bug=dict(file="numbug.py", intro="an exact comparison of 0.1 + 0.2 with 0.3", wrong=E6_BUG, fix_intro="rounded to two places before comparing", fixed=E6_FIX, show_fixed_out=False, expect=["AssertionError: total should be 0.3"],
   why="Floats are stored in binary and carry tiny errors, so compare rounded values instead of exact ones."),
 pun="\"0.1 plus 0.2 walked into a bar and ordered 0.3. The bartender said: close enough.\"",
 challenge="Set price = 19.5 and quantity = 4, then print the total and its type.",
 answer="total = price * quantity gives 78.0, and type(total) is float.",
 answer_code='price = 19.5\nquantity = 4\ntotal = price * quantity\nprint(total)\nprint(type(total))',
 shorts=[
  S("S1", "Int versus float", [2], "Counting or weighing?", "Counting or weighing? Whole numbers are ints, like three. Decimals are floats, like twelve point five. Python decides from how you write it.", "INT OR FLOAT?", "Two kinds of numbers.", ["python", "int", "float", "kodingkonkani", "beginners"]),
  S("S2", "Ask for the type", [5], "Not sure what it is? Ask.", "Not sure what it is? Ask. The type function tells you. Cups gives class int. Tea gives class float. Check before you guess.", "TYPE(CUPS)", "Check with type.", ["python", "type", "learntocode", "kodingkonkani", "coding"]),
  S("S3", "Slash gives a float", [5], "Eight divided by two is four point zero.", "Eight divided by two is four point zero. The slash always gives a float, even when the answer looks whole.", "8 / 2 = 4.0", "Slash is always a float.", ["python", "division", "float", "kodingkonkani", "coding"]),
  S("S4", "The assert that failed", [8], "Point one plus point two fails.", "Point one plus point two is not exactly point three. Python says, assertion error. Round to two places before you compare decimals.", "ASSERTIONERROR", "Round before you compare.", ["python", "bugfix", "assertionerror", "kodingkonkani", "coding"]),
  S("S5", "Pun and challenge", [9, 10], "Close enough, said the bartender.", "Close enough, said the bartender. Point one plus point two ordered point three. Your challenge: price nineteen point five, quantity four, print the total and its type. Full video: EP 6.", "PRINT THE TOTAL + ITS TYPE", "Try the challenge.", ["python", "codingchallenge", "kodingkonkani", "programmingjokes", "goa"]),
 ])

# ---------------------------------------------------------------- EP7
E7_CODE = '''name = "Xecxec"
beach = 'Palolem'
print(len(name))
print(name + " loves " + beach)
print("ha" * 3)
print(name[0], name[-1])'''
E7_BUG = 'age = 5\nprint("Xecxec is " + age + " years old")'
E7_FIX = 'age = 5\nprint("Xecxec is", age, "years old")'

EP7 = dict(ep=7, title="Strings", prereq="EP 06", **MOD1,
 goals=["write text with single or double quotes", "join strings with + and repeat them with *", "pick one character with an index, including -1"],
 yt=dict(title="Strings in Python: Join, Repeat and Index | Python Programming EP 07",
   desc="Work with text in Python: length, joining, repeating and picking letters, with Xecxec the crab.",
   tags=TAGS("python strings", "python string indexing", "python for beginners", "python tutorial", "string concatenation", "typeerror"),
   thumb_text="STRINGS", thumb_visual="in tomato on pastel blue; Xecxec threading beads that spell XECXEC on a string; thin black border and drop shadow.",
   chapters=chapters("Text is a string", "Four string tricks", "Numbered letters", "Follow the letters", "Run it")),
 files=[dict(name="strings.py", source=E7_CODE, scene="3, 5")],
 scenes=std_scenes((7, "STRINGS"),
   "Welcome back! So far we used numbers. Today we work with text. In Python, a piece of text is called a string, and it comes with some handy tricks.",
   ("Text is a string", '"Text is a string": three numbered lines and a bead-necklace analogy card', "Lines spring in with a pop; the card shows letters threaded on a string like beads",
    "A string is text inside quotes. You can use double quotes or single quotes, as long as the pair matches. A string is like a necklace of beads, where each bead is one character. Spaces and symbols count as beads too. Python can count the beads, join two necklaces, repeat one, or pick a single bead."),
   ("Four string tricks", "`strings.py`: name, beach, and four prints",
    "[HL 1] [TRACK name=Xecxec] A name tied to the string Xecxec. [HL 2] Single quotes work too, so beach is Palolem. [HL 3] The length function counts the beads. Xecxec has six. [HL 4] Plus joins strings together. Notice the spaces inside the quotes, they are part of the text. [HL 5] Star repeats a string, so ha times three is hahaha. [HL 6] Square brackets pick a letter by its position."),
   ("Numbered letters", "The word XECXEC as six boxes numbered 0 to 5 on top and -6 to -1 below",
    "Six letter boxes pop in; numbers 0 to 5 count along the top, and -1 to -6 count backwards along the bottom",
    "Each letter has a position number, called an index. Counting starts at zero, not one. So X is zero, E is one, and C is five, the last one. Python also counts from the end. Minus one is the last letter, minus two is the one before it. Using a number outside the word gives an error, so stay inside the bead count.", CS),
   ("Follow the letters", "`strings.py` again with the output panel on the right",
    "[HL 3] The length is six. [HL 4] Xecxec loves Palolem, joined into one string. [HL 5] Hahaha. [HL 6] Index zero is the first letter, X. Index minus one is the last letter, C. They print with a space between them. Predict first. What would name at index two print? The answer is C. Zero, one, two."),
   ("Run it", "Terminal: `python strings.py`",
    "Run it. Six. Xecxec loves Palolem. Hahaha. And X, then C. Now change the beach to your favourite beach, and run it again."),
   ("Bug of the Day", "BUG OF THE DAY: joining a string and an int",
    "Bug of the Day. We try to join text and a number with plus. Python says, type error, can only concatenate str, not int, to str. Plus joins strings only. Fix it by giving print each piece separated by commas. Print adds the spaces for you."),
   ("A string walked into a bar and asked for a slice. The bartender said: only with an index.", "A string walked into a bar and asked for a slice. The bartender said: only with an index."),
   ("Task card: print the first and last letters of your name", "Your challenge: store your name in a variable. Print its length, its first letter, and its last letter."),
   ("Next: EP 08 · Input from the user", "Next time: asking the user a question with input. Keep coding, says Xecxec!")),
 bug=dict(file="sb.py", intro="a string is joined to an int with +", wrong=E7_BUG, fix_intro="print gets the pieces separated by commas", fixed=E7_FIX, expect=['TypeError: can only concatenate str (not "int") to str'],
   why="Plus joins two strings, so a number must be given to print separately or turned into text first."),
 pun="\"A string walked into a bar and asked for a slice. The bartender said: only with an index.\"",
 challenge="Store your name in a variable, then print its length, its first letter and its last letter.",
 answer="With name = \"Atreya\", print(len(name)), print(name[0]) and print(name[-1]) give 6, A and a.",
 answer_code='name = "Atreya"\nprint(len(name))\nprint(name[0])\nprint(name[-1])',
 shorts=[
  S("S1", "A string is a necklace", [2], "Text is a necklace of beads.", "Text is a necklace of beads. A string is text in quotes, and each character is one bead. Python can count, join, repeat or pick them.", "STRING = TEXT IN QUOTES", "Strings explained.", ["python", "strings", "beginners", "kodingkonkani", "goa"]),
  S("S2", "Join and repeat", [3, 5], "Plus joins. Star repeats.", "Plus joins. Star repeats. Name plus loves plus beach makes one sentence. And ha times three makes hahaha.", "+ JOINS, * REPEATS", "Two string tricks.", ["python", "strings", "concatenation", "kodingkonkani", "coding"]),
  S("S3", "Count from zero", [4], "The first letter is number zero.", "The first letter is number zero. X is zero, E is one, C is five. And minus one counts from the end.", "INDEX STARTS AT 0", "Zero is the first.", ["python", "indexing", "learntocode", "kodingkonkani", "coding"]),
  S("S4", "Cannot concatenate", [8], "You cannot add text and a number.", "You cannot add text and a number. Python says, type error, can only concatenate str to str. Give print the pieces with commas.", "TYPEERROR: CONCATENATE", "Plus joins strings only.", ["python", "bugfix", "typeerror", "kodingkonkani", "coding"]),
  S("S5", "Pun and challenge", [9, 10], "A string asked for a slice.", "A string asked for a slice. The bartender said, only with an index. Your challenge: print your name's length, first letter and last letter. Full video: EP 7.", "LENGTH, FIRST, LAST", "Try it.", ["python", "codingchallenge", "kodingkonkani", "programmingjokes", "goa"]),
 ])

# ---------------------------------------------------------------- EP8
E8_CODE = '''beaches = input("How many beaches? ")
print("Beaches:", beaches)
print(beaches + beaches)
print(int(beaches) + 1)'''
E8_BUG = 'beaches = input("How many beaches? ")\nprint("Total:", beaches * 2.5)'
E8_FIX = 'beaches = int(input("How many beaches? "))\nprint("Total:", beaches * 2.5)'

EP8 = dict(ep=8, title="Input from the user", prereq="EP 07", **MOD1,
 goals=["ask the user a question with input()", "know that input() always gives back a string", "turn the answer into a number with int()"],
 yt=dict(title="Input in Python: Ask the User a Question | Python Programming EP 08",
   desc="Use input() to talk to your user, and learn why the answer is always text, with Xecxec the crab.",
   tags=TAGS("python input", "python user input", "python for beginners", "python tutorial", "input function", "typeerror"),
   thumb_text="ASK THE USER", thumb_visual="in tomato on pastel blue; Xecxec holding a speech bubble with a question mark toward a terminal prompt; thin black border and drop shadow.",
   chapters=chapters("Programs that listen", "Ask and answer", "Always a string", "Follow the answer", "Run it")),
 files=[dict(name="ask.py", source=E8_CODE, stdin="3\n", scene="3, 5")],
 scenes=std_scenes((8, "ASK THE USER"),
   "Welcome back! Until now our programs knew everything in advance. Today they ask. With input, your program can wait for the user to type an answer.",
   ("Programs that listen", '"Programs that listen": three numbered lines and a shop-counter analogy card', "Lines spring in with a pop; the card shows a shopkeeper asking a customer a question",
    "The input function pauses the program and waits. Whatever you write inside the brackets is shown as the question, called the prompt. The user types an answer and presses enter. Think of a shopkeeper asking, how many fish? The customer answers, and the shopkeeper writes it down. You can call input as many times as you like, once for each question."),
   ("Ask and answer", "`ask.py`: one input line and three prints",
    "[HL 1] [TRACK beaches=3] Input shows the question, then waits. The answer is tied to the name beaches. Here the user typed three. [HL 2] Print shows it. [HL 3] Now plus joins beaches to itself. [HL 4] And int turns the text into a real number before adding one."),
   ("Always a string", "A speech bubble reading 3 turns into a text card marked str; an int() machine turns it into a number card",
    "A speech bubble drops in with the answer; it lands as a text card; the int machine turns it into a number card with a ding",
    "Here is the big surprise. Input always gives back a string, even when the user types digits. The character three is not the number three. That is why plus joined the text, and gave thirty three. To do maths, wrap the input in int, which turns text into a whole number. Or use float, if decimals are allowed.", CS),
   ("Follow the answer", "`ask.py` again with the output panel on the right",
    "[HL 1] The user types three. Python gets the text three. [HL 2] Print shows beaches, three. [HL 3] Plus joins the text, so we get thirty three. It is text plus text. [HL 4] Int converts the text to the number three. Add one, and we get four. Predict first. Without int, would beaches plus one work? No. Text plus a number is an error."),
   ("Run it", "Terminal: `python ask.py`, then the user types 3",
    "Run it. The question appears and waits. We type three and press enter. Beaches, three. Thirty three. Four. Python waited for us, and then carried on."),
   ("Bug of the Day", "BUG OF THE DAY: multiplying the text from input",
    "Bug of the Day. The user types four. Beaches is the text four. We multiply it by two point five. Python says, type error, can't multiply sequence by non-int of type float. Text can be repeated by a whole number, but not a decimal. Wrap input in int, and the maths works."),
   ("I asked Python for input. It waited. So did I. We are still waiting.", "I asked Python for input. It waited. So did I. We are still waiting."),
   ("Task card: ask for a price, convert it, print it with tax", "Your challenge: ask the user for a price. Convert it with float, then print the price plus ten percent."),
   ("Next: EP 09 · Operators", "Next time: operators, the maths symbols of Python. Keep coding, says Xecxec!")),
 bug=dict(file="ib.py", stdin="4\n", intro="beaches is the text from input, run with input: 4", wrong=E8_BUG, fix_intro="int() added around input", fixed=E8_FIX, show_fixed_out=True, expect=["TypeError: can't multiply sequence by non-int of type 'float'"],
   why="input() always returns a string, and a string can only be repeated by a whole number, so convert the answer with int() first."),
 pun="\"I asked Python for input. It waited. So did I. We are still waiting.\"",
 challenge="Ask the user for a price, convert it with float, then print the price plus ten percent.",
 answer="price = float(input(\"Price? \")) then print(price * 1.1); an input of 100 gives 110.00000000000001 or about 110.",
 answer_code='price = float(input("Price? "))\nprint(price * 1.1)',
 shorts=[
  S("S1", "Programs that listen", [2], "Your program can ask questions.", "Your program can ask questions. Input shows a prompt, waits, and returns what the user typed. Press enter, and it carries on.", "INPUT() = ASK + WAIT", "Ask the user.", ["python", "input", "beginners", "kodingkonkani", "goa"]),
  S("S2", "Input is always text", [4], "The number three is not three.", "The number three is not three. Input always gives back a string, even when the user types digits. Plus will join them, not add them.", "INPUT GIVES A STRING", "Always text.", ["python", "input", "strings", "kodingkonkani", "coding"]),
  S("S3", "Wrap it in int", [3, 5], "One word fixes the maths.", "One word fixes the maths. Wrap input in int, and the text becomes a real number you can add or multiply.", "INT(INPUT())", "Convert the answer.", ["python", "int", "learntocode", "kodingkonkani", "coding"]),
  S("S4", "Cannot multiply sequence", [8], "Text times two point five.", "Text times two point five fails. Python says, can't multiply sequence by non-int of type float. Convert the input first.", "TYPEERROR: SEQUENCE", "Convert before maths.", ["python", "bugfix", "typeerror", "kodingkonkani", "coding"]),
  S("S5", "Pun and challenge", [9, 10], "Python waited. So did I.", "Python waited. So did I. Your challenge: ask for a price, convert it with float, and print the price plus ten percent. Full video: EP 8.", "PRICE PLUS 10%", "Try it.", ["python", "codingchallenge", "kodingkonkani", "programmingjokes", "goa"]),
 ])

# ---------------------------------------------------------------- EP9
E9_CODE = '''shacks = 17
tables = 5
print(shacks // tables)
print(shacks % tables)
print(2 ** 10)
print(shacks / tables)
print(-17 // 5)'''
E9_BUG = 'print(2 ^ 0.5)'
E9_FIX = 'print(2 ** 0.5)'

EP9 = dict(ep=9, title="Operators", prereq="EP 08", **MOD1,
 goals=["use + - * / // % and ** correctly", "explain floor division and remainder with tables and shacks", "know that ^ is not the power operator"],
 yt=dict(title="Operators in Python: // % and ** | Python Programming EP 09",
   desc="The maths symbols of Python, including floor division, remainder and power, with Xecxec the crab.",
   tags=TAGS("python operators", "floor division python", "modulo python", "python power", "python for beginners", "python tutorial"),
   thumb_text="// % **", thumb_visual="in tomato on pastel blue; Xecxec juggling the symbols // % and ** like beach balls; thin black border and drop shadow.",
   chapters=chapters("The seven operators", "Tables and shacks", "Floor division", "Follow the maths", "Run it")),
 files=[dict(name="ops.py", source=E9_CODE, scene="3, 5")],
 scenes=std_scenes((9, "// % **"),
   "Welcome back! You know plus, minus and times. Today we meet the other operators, including two that surprise most beginners: floor division and remainder.",
   ("The seven operators", '"The seven operators": three numbered lines and a calculator analogy card', "Lines spring in with a pop; the card shows a calculator with seven keys lighting up",
    "Python has seven maths operators. Plus, minus and times work as you expect. Slash divides and gives a float. Double slash is floor division, which keeps only the whole part. Percent gives the remainder. And double star raises to a power. Think of a calculator with a few extra keys. Today we learn the extra ones."),
   ("Tables and shacks", "`ops.py`: shacks, tables and five prints",
    "[HL 1] [TRACK shacks=17] Seventeen guests. [HL 2] [TRACK tables=5] Five tables. [HL 3] Floor division gives three. Each table seats three full groups. [HL 4] Percent gives the remainder, two. Two guests are left standing. [HL 5] Double star is power. Two to the power ten is one thousand twenty four. [HL 6] Plain slash gives three point four, a float."),
   ("Floor division", "A number line from -5 to 5 with 17 / 5 and -17 / 5 marked; a floor arrow steps down to the next whole number",
    "A number line slides in; a dot lands on 3.4 and a floor arrow steps left to 3; another dot lands on -3.4 and the floor arrow steps left to -4",
    "Floor division rounds the answer down, towards the smaller number. Seventeen divided by five is three point four, and the floor is three. Now the surprise. Minus seventeen divided by five is minus three point four, and down from there is minus four, not minus three. Down means more negative, not closer to zero. Remember that, and negative numbers stop being scary.", CS),
   ("Follow the maths", "`ops.py` again with the output panel on the right",
    "[HL 3] Seventeen floor divided by five is three. [HL 4] Seventeen percent five is two, because five times three is fifteen and two is left. [HL 5] One thousand twenty four. [HL 6] Three point four. [HL 7] Minus four, because floor goes down. Predict before you run. The last line is the tricky one. Did you say minus three? Check the number line."),
   ("Run it", "Terminal: `python ops.py`",
    "Run it. Three. Two. One thousand twenty four. Three point four. Minus four. Change shacks to twenty, and predict all five answers first."),
   ("Bug of the Day", "BUG OF THE DAY: caret is not power",
    "Bug of the Day. We try to square root two, using caret. Python says, type error, unsupported operand types for caret, int and float. In Python, caret is a different operator, used on bits. Power is double star. Two to the power point five is the square root of two."),
   ("Why did floor division break up with the slash? It was tired of the remainders.", "Why did floor division break up with the slash? It was tired of the remainders."),
   ("Task card: 100 minutes into hours and minutes", "Your challenge: turn one hundred thirty five minutes into hours and minutes, using floor division and remainder."),
   ("Next: EP 10 · f-strings and formatting", "Next time: f-strings, the neat way to print values. Keep coding, says Xecxec!")),
 bug=dict(file="ob.py", intro="caret used for power", wrong=E9_BUG, fix_intro="double star used for power", fixed=E9_FIX, show_fixed_out=True, expect=["TypeError: unsupported operand type(s) for ^: 'int' and 'float'"],
   why="The caret is the bitwise XOR operator in Python; use ** for powers."),
 pun="\"Why did floor division break up with the slash? It was tired of the remainders.\"",
 challenge="Turn 135 minutes into hours and minutes using // and %.",
 answer="135 // 60 gives 2 hours and 135 % 60 gives 15 minutes, so print 2 and 15.",
 answer_code='minutes = 135\nprint(minutes // 60)\nprint(minutes % 60)',
 shorts=[
  S("S1", "Floor division", [4], "Seventeen shared among five tables.", "Seventeen guests, five tables. Double slash gives three, the whole groups. Percent gives two, the guests left over.", "// AND % ", "Quotient and remainder.", ["python", "operators", "beginners", "kodingkonkani", "goa"]),
  S("S2", "The remainder", [3, 5], "What is left over?", "What is left over? Percent gives the remainder. Seventeen percent five is two, because five times three is fifteen.", "17 % 5 = 2", "Remainder explained.", ["python", "modulo", "learntocode", "kodingkonkani", "coding"]),
  S("S3", "Floor goes down", [4, 5], "Minus seventeen floor five is minus four.", "Minus seventeen floor divided by five is minus four, not minus three. Floor goes down, towards the smaller number.", "-17 // 5 = -4", "Floor means down.", ["python", "floordivision", "negativenumbers", "kodingkonkani", "coding"]),
  S("S4", "Caret is not power", [8], "Caret does not mean power.", "Caret does not mean power in Python. Two caret point five gives a type error. Use double star for powers.", "2 ** 0.5, NOT 2 ^ 0.5", "Use double star.", ["python", "bugfix", "typeerror", "kodingkonkani", "coding"]),
  S("S5", "Pun and challenge", [9, 10], "Tired of the remainders.", "Floor division broke up with the slash. It was tired of the remainders. Your challenge: turn one hundred thirty five minutes into hours and minutes. Full video: EP 9.", "135 MINUTES = ? H ? M", "Try it.", ["python", "codingchallenge", "kodingkonkani", "programmingjokes", "goa"]),
 ])

# ---------------------------------------------------------------- EP10
E10_CODE = '''name = "Xecxec"
fish = 3
price = 119.5
total = fish * price
print(f"{name} bought {fish} fish")
print(f"Total: {total:.2f}")
print(f"{fish * 2} fish in two trips")'''
E10_BUG = 'price = 119.5\nfish = 3\ntotal = fish * price\nprint(f"Total: {total:.2d}")'
E10_FIX = 'price = 119.5\nfish = 3\ntotal = fish * price\nprint(f"Total: {total:.2f}")'

EP10 = dict(ep=10, title="f-strings and formatting", prereq="EP 09", **MOD1,
 goals=["put values inside text with an f-string and {}", "format decimals with :.2f", "run a small expression inside the braces"],
 yt=dict(title="f-strings in Python: Print Values Neatly | Python Programming EP 10",
   desc="The cleanest way to put values into text, including two-decimal prices, with Xecxec the crab.",
   tags=TAGS("python f-strings", "python string formatting", "python for beginners", "python tutorial", "format decimals python", "valueerror"),
   thumb_text="F-STRINGS", thumb_visual="in tomato on pastel blue; Xecxec pouring values into curly braces on a text card marked f; thin black border and drop shadow.",
   chapters=chapters("Fill in the blanks", "Fish bill", "Format codes", "Follow the template", "Run it")),
 files=[dict(name="fstring.py", source=E10_CODE, scene="3, 5")],
 scenes=std_scenes((10, "F-STRINGS"),
   "Welcome back! Printing with commas works, but it gets messy. Today we learn f-strings, the neat way to put values inside a sentence.",
   ("Fill in the blanks", '"Fill in the blanks": three numbered lines and a bill-template analogy card', "Lines spring in with a pop; the card shows a bill with blank spaces being filled in",
    "An f-string is a template with blanks. Put the letter f right before the opening quote. Then write curly braces wherever a value should go. Python fills each blank with the value inside. It is like a printed bill with blank spaces for the name and the total. And if you forget the f, Python prints the braces as plain text, with no error."),
   ("Fish bill", "`fstring.py`: three names and three f-string prints",
    "[HL 1] [TRACK name=Xecxec] A name. [HL 2] [TRACK fish=3] A count. [HL 3] [TRACK price=119.5] A price with a decimal. [HL 4] [TRACK total=358.5] The total, three hundred fifty eight point five. [HL 5] The f before the quote turns on the blanks. Name and fish are filled in from their values. [HL 6] After a colon inside the braces, we add a format code. Point two f means, two digits after the decimal point."),
   ("Format codes", "A braces card: {total:.2f} split into the value, the colon and the format code",
    "The card {total:.2f} pops in; three pieces light up one by one: the name, the colon, and .2f; a result card shows 358.50",
    "Look inside the braces. The name comes first, then a colon, then the format code. Point two f means, show a float with two decimals. So three fifty eight point five prints as three fifty eight point five zero. That is perfect for money. Use d for whole numbers, but never for a float, or Python complains. You can also put a small expression inside the braces, like fish times two.", CS),
   ("Follow the template", "`fstring.py` again with the output panel on the right",
    "[HL 5] Python fills the blanks. Xecxec bought three fish. [HL 6] The total prints as three fifty eight point five zero, with two decimals. [HL 7] The braces can hold a calculation. Fish times two is six, so we get, six fish in two trips. Predict first. What would the format code point one f print for the total? Three fifty eight point five."),
   ("Run it", "Terminal: `python fstring.py`",
    "Run it. Xecxec bought three fish. Total, three fifty eight point five zero. Six fish in two trips. Change the price, and watch the total follow."),
   ("Bug of the Day", "BUG OF THE DAY: the d format code on a float",
    "Bug of the Day. We used the format code point two d on a float. Python says, value error, unknown format code d for object of type float. The d code is for whole numbers only. For a float, use point two f, and the bill prints correctly."),
   ("Why did the f-string cry? Someone forgot it at the start.", "Why did the f-string cry? Someone forgot it at the start."),
   ("Task card: a receipt line with two decimals", "Your challenge: print a receipt line in one f-string, showing a name, a quantity and a total with two decimals."),
   ("Next: EP 11 · Booleans and comparisons", "Next time: booleans, the yes and no of Python. Keep coding, says Xecxec!")),
 bug=dict(file="fb.py", intro="the integer code d is used on a float", wrong=E10_BUG, fix_intro="d replaced by f", fixed=E10_FIX, show_fixed_out=True, expect=["ValueError: Unknown format code 'd' for object of type 'float'"],
   why="The d code formats whole numbers; floats need f, as in :.2f."),
 pun="\"Why did the f-string cry? Someone forgot it at the start.\"",
 challenge="Print a receipt line with a name, a quantity and a total with two decimals, all in one f-string.",
 answer="For example print(f\"{item}: {qty} x {price:.2f} = {total:.2f}\") with item = \"Fish\", qty = 3, price = 119.5.",
 answer_code='item = "Fish"\nqty = 3\nprice = 119.5\ntotal = qty * price\nprint(f"{item}: {qty} x {price:.2f} = {total:.2f}")',
 shorts=[
  S("S1", "Fill in the blanks", [2], "A sentence with blanks.", "A sentence with blanks. Put f before the quote, and write curly braces where values go. Python fills them in.", "F\"HELLO {NAME}\"", "f-strings in 30 seconds.", ["python", "fstrings", "beginners", "kodingkonkani", "goa"]),
  S("S2", "Two decimals for money", [4], "Make money look like money.", "Make money look like money. Inside the braces, add colon, point two f. Three fifty eight point five prints with two decimals.", "{TOTAL:.2F}", "Two decimals.", ["python", "formatting", "learntocode", "kodingkonkani", "coding"]),
  S("S3", "Maths inside braces", [5], "Braces can do maths.", "Braces can do maths. Put fish times two inside them, and Python prints six. No extra variable needed.", "{FISH * 2}", "Expressions inside.", ["python", "fstrings", "coding", "kodingkonkani", "tips"]),
  S("S4", "Unknown format code", [8], "Use d on a float, and it fails.", "Use the d code on a float, and Python says, value error, unknown format code d. Floats need f.", "VALUEERROR: CODE D", "d is for whole numbers.", ["python", "bugfix", "valueerror", "kodingkonkani", "coding"]),
  S("S5", "Pun and challenge", [9, 10], "The f-string cried.", "The f-string cried because someone forgot it at the start. Your challenge: print a receipt line with name, quantity and total in one f-string. Full video: EP 10.", "ONE-LINE RECEIPT", "Try it.", ["python", "codingchallenge", "kodingkonkani", "programmingjokes", "goa"]),
 ])

# ---------------------------------------------------------------- EP11
E11_CODE = '''age = 17
hours = 6
print(age >= 18)
print(age == 17)
print(age != 17)
print(age >= 16 and hours > 4)
print(not (age > 20))
print(type(True))'''
E11_BUG = 'age = 17\nprint(age = 17)'
E11_FIX = 'age = 17\nprint(age == 17)'

EP11 = dict(ep=11, title="Booleans and comparisons", prereq="EP 10", **MOD1,
 goals=["compare values with == != < > <= >=", "combine answers with and, or and not", "tell = (assign) from == (compare)"],
 yt=dict(title="Booleans and Comparisons in Python | Python Programming EP 11",
   desc="True, False and the symbols that produce them, with Xecxec the crab.",
   tags=TAGS("python booleans", "python comparison operators", "python and or not", "python for beginners", "python tutorial", "typeerror"),
   thumb_text="TRUE OR FALSE", thumb_visual="in tomato on pastel blue; Xecxec holding a green TRUE sign and a red FALSE sign; thin black border and drop shadow.",
   chapters=chapters("Yes or no", "Six comparisons", "Combining answers", "Follow the answers", "Run it")),
 files=[dict(name="checks.py", source=E11_CODE, scene="3, 5")],
 scenes=std_scenes((11, "TRUE OR FALSE"),
   "Welcome back! A program often needs to answer a question with yes or no. In Python, those two answers are called booleans, and today we learn how to produce them.",
   ("Yes or no", '"Yes or no": three numbered lines and a traffic-light analogy card', "Lines spring in with a pop; the card shows a green light for True and a red light for False",
    "A boolean has only two possible values, True and False, both with a capital first letter. Comparisons produce them. Is age at least eighteen? The answer is True or False. Think of a traffic light with only green and red. Booleans are what make programs decide, which is exactly what we use in the next module."),
   ("Six comparisons", "`checks.py`: age, hours, and six prints; the comparison operators glow",
    "[HL 1] [TRACK age=17] Age is seventeen. [HL 2] [TRACK hours=6] Hours is six. [HL 3] Greater than or equal to eighteen. Seventeen is not, so False. [HL 4] Double equals asks, are they equal? Yes, so True. Notice, two equals signs. One equals ties a name. Two equals compares. [HL 5] Not equal gives False."),
   ("Combining answers", "Three logic cards: and needs both True, or needs one True, not flips the answer",
    "Three cards pop in; for each, two lamps light green or red and the result lamp follows the rule with a ding",
    "You can combine answers. And needs both sides to be True. Or needs at least one side True. Not flips an answer, True becomes False and False becomes True. So, age at least sixteen and hours more than four, is True and True, which is True. Not of False is True. Use brackets to keep your meaning clear.", CS),
   ("Follow the answers", "`checks.py` again with the output panel on the right",
    "[HL 3] False. [HL 4] True. [HL 5] False. [HL 6] Seventeen is at least sixteen, and six is more than four, so both are True, and the answer is True. [HL 7] Age greater than twenty is False, and not flips it to True. [HL 8] The type of True is class bool. Predict each answer before you run."),
   ("Run it", "Terminal: `python checks.py`",
    "Run it. False, True, False, True, True. And class bool. Change age to twenty one, and predict the new answers first."),
   ("Bug of the Day", "BUG OF THE DAY: one equals sign inside print",
    "Bug of the Day. We wrote age equals seventeen inside print. Python reads that as a keyword argument. It says, type error, print got an unexpected keyword argument age. One equals sign assigns. Two equals signs compare. Use double equals, and Python prints True."),
   ("Why did the boolean go to the party? It wanted to be True to itself.", "Why did the boolean go to the party? It wanted to be True to itself."),
   ("Task card: is a number even and positive?", "Your challenge: set n to ten. Print whether n is even and also greater than zero."),
   ("Next: EP 12 · Type conversion", "Next time: type conversion, turning one kind of value into another. Keep coding, says Xecxec!")),
 bug=dict(file="cb.py", intro="a single = inside print", wrong=E11_BUG, fix_intro="== used to compare", fixed=E11_FIX, show_fixed_out=True, expect=["TypeError: print() got an unexpected keyword argument 'age'"],
   why="A single = assigns and a double == compares; inside brackets a single = is read as a keyword argument."),
 pun="\"Why did the boolean go to the party? It wanted to be True to itself.\"",
 challenge="Set n = 10, then print whether n is even and also greater than zero.",
 answer="print(n % 2 == 0 and n > 0) prints True for n = 10.",
 answer_code='n = 10\nprint(n % 2 == 0 and n > 0)',
 shorts=[
  S("S1", "True or False", [2], "Only two possible answers.", "Only two possible answers. A boolean is True or False. Comparisons produce them, and decisions depend on them.", "TRUE OR FALSE", "Booleans in 30 seconds.", ["python", "boolean", "beginners", "kodingkonkani", "goa"]),
  S("S2", "Equals versus double equals", [3], "One equals ties. Two equals asks.", "One equals ties a name to a value. Two equals asks, are they equal? Mixing them up is a classic beginner bug.", "= TIES, == ASKS", "Assign or compare?", ["python", "comparison", "learntocode", "kodingkonkani", "coding"]),
  S("S3", "And, or, not", [4, 5], "Three words that combine answers.", "Three words that combine answers. And needs both True. Or needs one True. Not flips the answer.", "AND / OR / NOT", "Logic in a minute.", ["python", "logic", "coding", "kodingkonkani", "tips"]),
  S("S4", "Unexpected keyword", [8], "One equals sign inside print.", "One equals sign inside print. Python says, type error, unexpected keyword argument age. Use double equals to compare.", "TYPEERROR: KEYWORD ARGUMENT", "Use ==.", ["python", "bugfix", "typeerror", "kodingkonkani", "coding"]),
  S("S5", "Pun and challenge", [9, 10], "True to itself.", "The boolean went to the party because it wanted to be True to itself. Your challenge: print whether ten is even and greater than zero. Full video: EP 11.", "EVEN AND POSITIVE?", "Try it.", ["python", "codingchallenge", "kodingkonkani", "programmingjokes", "goa"]),
 ])

# ---------------------------------------------------------------- EP12
E12_CODE = '''text = "42"
number = int(text)
price = float("19.5")
print(number + 8)
print(price * 2)
print(str(number) + " fish")
print(int(7.9))
print(bool(0), bool("Goa"))'''
E12_BUG = 'text = "abc"\nnumber = int(text)\nprint(number)'
E12_FIX = 'text = "42"\nnumber = int(text)\nprint(number)'

EP12 = dict(ep=12, title="Type conversion", prereq="EP 11", **MOD1,
 goals=["convert with int(), float(), str() and bool()", "know that int() cuts the decimal part instead of rounding", "read a ValueError from a bad conversion"],
 yt=dict(title="Type Conversion in Python: int, float, str, bool | Python Programming EP 12",
   desc="Turn one kind of value into another, safely, and finish Module 1 with Xecxec the crab.",
   tags=TAGS("python type conversion", "python int float str", "python casting", "python for beginners", "python tutorial", "valueerror"),
   thumb_text="CONVERT IT", thumb_visual="in tomato on pastel blue; Xecxec turning a text card marked 42 into a number card through a machine; thin black border and drop shadow.",
   chapters=chapters("Four converters", "Converting in code", "What gets cut", "Follow the values", "Run it")),
 files=[dict(name="convert.py", source=E12_CODE, scene="3, 5")],
 scenes=std_scenes((12, "CONVERT IT"),
   "Welcome back! This is the last episode of Module one. We have met ints, floats, strings and booleans. Today we learn to turn one into another.",
   ("Four converters", '"Four converters": three numbered lines and a currency-exchange analogy card', "Lines spring in with a pop; the card shows a currency exchange counter with four windows",
    "Python gives you four converters, named after the types they make. Int makes a whole number. Float makes a decimal. Str makes text. And bool makes True or False. Like a currency exchange, you hand over one kind of value and get another kind back. The original stays as it was. Conversion makes a new value."),
   ("Converting in code", "`convert.py`: text, number, price and five prints",
    "[HL 1] [TRACK text=42] The text forty two, in quotes. [HL 2] [TRACK number=42] Int turns it into the number forty two. [HL 3] [TRACK price=19.5] Float turns the text nineteen point five into a decimal. [HL 4] Now we can add. Forty two plus eight is fifty. [HL 5] Nineteen point five times two is thirty nine point zero. [HL 6] Str turns the number back into text, so we can join it with fish."),
   ("What gets cut", "A number line with 7.9; int() drops straight down to 7; bool() cards show 0 as False and Goa as True",
    "A dot lands on 7.9 and drops straight down to 7 with a thud; then two bool cards flip: zero turns False, Goa turns True",
    "Two details catch people out. First, int does not round. It simply cuts off the decimal part, so seven point nine becomes seven. If you want rounding, use the round function. Second, bool follows a simple rule. Zero and empty text are False. Everything else is True, so the word Goa is True. And if the text is not a real number, the conversion fails.", CS),
   ("Follow the values", "`convert.py` again with the output panel on the right",
    "[HL 4] The text became a number, so we get fifty. [HL 5] Thirty nine point zero. [HL 6] Forty two fish. [HL 7] Seven, not eight. The decimal part is cut. [HL 8] Bool of zero is False. Bool of the word Goa is True. Predict first. What would int of minus seven point nine give? Minus seven. Int cuts towards zero."),
   ("Run it", "Terminal: `python convert.py`",
    "Run it. Fifty. Thirty nine point zero. Forty two fish. Seven. False, True. Change the text to a word, and see what happens in the next scene."),
   ("Bug of the Day", "BUG OF THE DAY: converting text that is not a number",
    "Bug of the Day. We ask int to convert the text abc. Python says, value error, invalid literal for int with base ten, abc. The conversion needs text that looks like a whole number. Fix the text, and it works. Check the input before you convert it."),
   ("I tried to convert my cat to an int. Python said: invalid literal.", "I tried to convert my cat to an int. Python said: invalid literal."),
   ("Task card: ask for a number as text and double it", "Your challenge: set text to the string twelve point five. Convert it to a float, double it, and print the answer."),
   ("Next: Module 2 · EP 13 · if and else", "Module one is done! Next: if and else, where programs start to decide. Keep coding, says Xecxec!")),
 bug=dict(file="tb.py", intro="int() is given the text abc", wrong=E12_BUG, fix_intro="the text is a valid whole number", fixed=E12_FIX, show_fixed_out=True, expect=["ValueError: invalid literal for int() with base 10: 'abc'"],
   why="int() only accepts text that looks like a whole number, so check or clean the text before converting it."),
 pun="\"I tried to convert my cat to an int. Python said: invalid literal.\"",
 challenge="Set text = \"12.5\", convert it to a float, double it and print the answer.",
 answer="float(text) * 2 gives 25.0.",
 answer_code='text = "12.5"\nvalue = float(text)\nprint(value * 2)',
 shorts=[
  S("S1", "Four converters", [2], "Four functions, four types.", "Four functions, four types. Int, float, str and bool. Hand over one kind of value, get another kind back.", "INT FLOAT STR BOOL", "Convert in 30 seconds.", ["python", "typeconversion", "beginners", "kodingkonkani", "goa"]),
  S("S2", "Int cuts, never rounds", [5], "Seven point nine becomes seven.", "Seven point nine becomes seven. Int cuts off the decimal part, it does not round. Want rounding? Use round.", "INT(7.9) = 7", "Cut, not round.", ["python", "int", "learntocode", "kodingkonkani", "coding"]),
  S("S3", "Truthy and falsy", [4, 5], "Zero is False. Goa is True.", "Zero is False. Empty text is False. Everything else is True, so the word Goa is True.", "BOOL(0) = FALSE", "What is True?", ["python", "bool", "coding", "kodingkonkani", "tips"]),
  S("S4", "Invalid literal", [8], "Convert the word abc.", "Convert the word abc with int, and Python says, value error, invalid literal. Only text that looks like a whole number works.", "VALUEERROR: INVALID LITERAL", "Check before converting.", ["python", "bugfix", "valueerror", "kodingkonkani", "coding"]),
  S("S5", "Pun and challenge", [9, 10], "My cat is not an int.", "I tried to convert my cat to an int. Python said, invalid literal. Your challenge: convert twelve point five from text to a float and double it. Full video: EP 12.", "TEXT TO FLOAT, THEN DOUBLE", "Try it.", ["python", "codingchallenge", "kodingkonkani", "programmingjokes", "goa"]),
 ])

EPS = [EP5, EP6, EP7, EP8, EP9, EP10, EP11, EP12]

RECAP = {
 5: ("Recap: four ideas on one card", "Recap time. One: a variable is a name tied to a value, and equals does the tying. Two: Python works out the right side first, once, and does not remember the formula. Three: changing fish moves only the fish tag. Four: create a name before you use it. Say these four ideas out loud, then try changing price and predicting the new total."),
 6: ("Recap: four ideas on one card", "Recap. One: an int is a whole number, and a float has a decimal point. Two: the type function tells you which one you have. Three: slash always gives a float, even for eight divided by two. Four: decimals carry a tiny error, so round before you compare. Say these four ideas out loud, and you are ready for text."),
 7: ("Recap: four ideas on one card", "Recap. One: a string is text inside matching quotes. Two: plus joins strings, and star repeats them. Three: the first letter has index zero, and minus one is the last. Four: plus cannot join text and a number. Say these four ideas out loud, then print the first and last letters of your own name."),
 8: ("Recap: four ideas on one card", "Recap. One: input shows a prompt, waits, and returns what the user typed. Two: the answer is always a string, even if it looks like a number. Three: wrap it in int or float before doing maths. Four: text times a decimal is a type error. Say these four ideas out loud, then ask your own question."),
 9: ("Recap: five operators on one card", "Recap. One: slash divides and always gives a float. Two: double slash keeps the whole part, and rounds down. Three: percent gives the remainder. Four: double star is power, and caret is something else. And remember, minus seventeen floor five is minus four. Say these out loud, and try a few of your own numbers."),
 10: ("Recap: four ideas on one card", "Recap. One: an f-string starts with f before the quote, and uses braces for values. Two: after a colon in the braces, you can add a format code. Three: point two f gives two decimals, and d is for whole numbers only. Four: you can put a small calculation inside the braces. Say these four ideas out loud, then rewrite an old print with an f-string."),
 11: ("Recap: four ideas on one card", "Recap. One: a boolean is True or False. Two: double equals compares, and single equals assigns. Three: and needs both sides True, or needs one, and not flips the answer. Four: comparisons like greater than or equal give a boolean. Say these four ideas out loud, then predict each answer on the screen before you run it."),
 12: ("Recap: four converters on one card", "Recap. One: int, float, str and bool convert one kind of value to another. Two: int cuts the decimal part and does not round. Three: bool of zero or empty text is False, and everything else is True. Four: converting text that is not a number gives a value error. That is the end of Module one. Say these ideas out loud, and give yourself a clap."),
}
for _e in EPS:
    on, narr = RECAP[_e["ep"]]
    _e["scenes"].insert(6, dict(tpl=CS, name="Recap", on=on, anim="Four recap lines tick in one by one with a pop; Xecxec nods after each tick", narr=narr, min=30))

for _e in EPS:
    _mapped = set()
    for _f in _e["files"]:
        _mapped |= {int(x) for x in re.findall(r"\d+", _f.get("scene", ""))}
    for _i, _s in enumerate(_e["scenes"], 1):
        if _s["tpl"] == CE and _i not in _mapped:
            _s["tpl"] = CS
            _s["anim"] = "Lines spring in one by one with a pop; the explanation card slides in from the right"
