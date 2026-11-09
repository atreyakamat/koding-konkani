"""Module 1 — Variables, types, input, operators (EP 5-12)."""

MODULE = {"id": 1, "name": "Variables, types, input, operators", "range": "5–12", "colours": "PastelBlue + Tomato"}
EPISODES = []
NEXT_AFTER = ("Next: EP 13 · if and else", "Module one is done! Next time: making decisions with if and else.")

EPISODES.append(dict(
    n=5, title="Variables and names", spoken="variables and names",
    yt="Python Variables and Names for Beginners", thumb="NAMES, NOT BOXES",
    vis="Xecxec holding two name tags, one tied to a string and one to a number, on a pastelBlue card",
    goals=["create names with = and read them back", "follow the naming rules", "reassign a name and swap two names"],
    tags=["python variables", "variable naming rules", "assignment in python", "nameerror"],
    hash=["#variables", "#names"],
    analogy="a beach-shack signboard: the board is the name, the shack is the value",
    c_title="Variables and names",
    c_pts=["A name is tied to a value with =", "Rules: letters, digits, underscore; no spaces", "Capital and small letters are different"],
    intro="Welcome back! Last time we met names as tags. Today we learn how to make them, how to name them well, and how to change what they point at.",
    concept="A variable is a name tied to a value. You write the name, an equals sign, and the value. Think of a beach shack. The signboard is the name, and the shack is the value. The sign can be moved to a different shack later. The rules are simple. Use letters, digits and underscores. Never start with a digit, and never use spaces. Capital and small letters count as different names.",
    A=dict(file="beach.py", label="Making names", on="two names and a changed value",
           src='''
beach = "Calangute"
visitors = 120
visitors = visitors + 30
print(beach, visitors)
''',
           narr="[HL 1] A name called beach, tied to the text Calangute. [HL 2] A name called visitors, tied to one hundred twenty. [HL 3] Now we reuse the name. Python reads visitors, adds thirty, and ties the name to the new answer, one hundred fifty. The old value is simply left behind. [HL 4] Print both names. Python shows Calangute, then one hundred fifty.",
           label2="Reading it again", narr2="Predict first. What does print show? The beach name, then the new number. [TRACK visitors=150] The name visitors points at one hundred fifty now. The equals sign does not mean equal in the maths way. It means, tie this name to that value."),
    mem=dict(label="Names tied to objects", on="Two name tags, beach and visitors, tied by arrows to the text and the number", names=["beach", "visitors"], **{"from": "A"},
             narr="Here is what Python holds after the code runs. The name beach is tied to the text Calangute. The name visitors is tied to the number one hundred fifty. The old value, one hundred twenty, has no name on it any more. Python tidies it away. Remember the picture: names are tags, and the objects are the things they point at."),
    B=dict(file="swap.py", label="Swap two names", on="swapping what two names point at",
           src='''
left = "fish"
right = "curry"
left, right = right, left
print(left, right)
''',
           narr="[HL 1] [TRACK left=fish] Left points at fish. [HL 2] [TRACK right=curry] Right points at curry. [HL 3] Now the swap. Python reads both names on the right side first, then ties them back in the opposite order. [TRACK left=curry] Left now points at curry. [TRACK right=fish] Right now points at fish. [HL 4] So the print shows, curry fish. No third name was needed."),
    term="It prints curry fish. The two names traded places.",
    recap=["A variable is a name tied to a value with the equals sign.", "Names use letters, digits and underscores, never start with a digit, and have no spaces.", "Reusing a name ties it to a new value.", "Capital and small letters are different names."],
    bug=dict(title="using a name before it exists", wrong='''
print(total)
total = 10
''', fixed='''
total = 10
print(total)
''', wrong_note="print comes before the assignment", fixed_note="assign first, then use",
             why="Python runs lines from top to bottom, so a name must be tied to a value before any line reads it.",
             narr="Bug of the Day. We print total before we ever make it. Python says, name error, total is not defined. Python reads from the top, and at line one the name does not exist yet. Move the assignment above the print, and it works."),
    pun="I named my variable after a crab. It keeps scuttling to a new value.",
    task="make two names, swap them, print them", challenge="Make two names, city and friend, then swap them and print both.",
    answer="Use city = \"Panjim\" and friend = \"Asha\", then city, friend = friend, city and print(city, friend), which shows Asha Panjim.",
    shorts=[
        ("A name is a tag", "A name is a tag, not a box. You write the name, an equals sign, and a value, and Python ties the two together. Beach equals Calangute makes a tag called beach on the text Calangute. Later you can move that tag to a new value. If no name points at the old value any more, Python quietly tidies it away. That is all a variable really is.", "NAMES ARE TAGS", "A variable explained in one picture."),
        ("Naming rules", "Four rules for good names. Use letters, digits and underscores. Never start a name with a digit. Never use spaces, so write open underscore shacks, not open shacks. And remember that capital and small letters are different, so Beach and beach are two different names. Pick a name that says what the value is. Then you can read your code later.", "NAMING RULES", "Name things well."),
        ("Reuse a name", "Watch this line. Visitors equals visitors plus thirty. Python first reads the old value, one hundred twenty, and adds thirty. Only then does it tie the name to the answer, one hundred fifty. So the right side runs first, and the left side receives the result. The equals sign means tie, not equal. That one idea clears up most of the confusion for beginners.", "VISITORS = VISITORS + 30", "Read the right side first."),
        ("Name before value", "A very common first bug. You print a name before you ever make it. Python reads from the top. At that line the name does not exist yet. You get a name error, name total is not defined. The fix is simple. Put the assignment above the print. Always make a name first, then use it, and this bug disappears.", "NAMEERROR: NAME NOT DEFINED", "Make it first, then use it."),
        ("Pun and challenge", "I named my variable after a crab. It keeps scuttling to a new value. Now your challenge. Make two names, city and friend, with any values you like. Then swap them with one single line, and print both. Remember, Python can swap two names without needing a third helper name. Write your answer in the comments, and see who can do it fastest.", "SWAP TWO NAMES", "Try the swap."),
    ],
))

EPISODES.append(dict(
    n=6, title="Numbers: int and float", spoken="numbers, int and float",
    yt="Python Numbers: int and float Explained", thumb="INT OR FLOAT?",
    vis="Xecxec balancing a whole number 3 and a decimal 120.5 on a see-saw labelled int and float",
    goals=["tell a whole number (int) from a decimal (float)", "do arithmetic with both", "see why decimals can print a surprising tail"],
    tags=["python int float", "python numbers", "floating point python", "round function"],
    hash=["#numbers", "#float"],
    analogy="fish at the market: you count whole fish, but you weigh the catch in kilograms with decimals",
    c_title="Two kinds of numbers",
    c_pts=["int is a whole number, like 3", "float has a decimal point, like 120.5", "Maths on both just works"],
    intro="Today we meet the two kinds of numbers in Python. One counts whole things. The other measures things with decimals.",
    concept="Python has two main kinds of numbers. An int is a whole number, like three fish. A float has a decimal point, like one hundred twenty and a half rupees. Think of the fish market. You count the fish as whole numbers, but you weigh them in kilograms, with decimals. You can mix both in one sum. Python gives you a float whenever a float is involved.",
    A=dict(file="prices.py", label="int and float in code", on="a whole number, a decimal and their product",
           src='''
fish = 3
price = 120.5
total = fish * price
print(total)
print(type(fish))
print(type(price))
''',
           narr="[HL 1] Fish is three, a whole number, so an int. [HL 2] Price is one hundred twenty and a half. The decimal point makes it a float. [HL 3] We multiply. An int times a float gives a float. [HL 4] Print the total. [HL 5] The type function tells us the type of the object that a name points at. [HL 6] And again for price. Int first, then float.",
           label2="Reading the output", narr2="Predict first. Three times one hundred twenty and a half is three hundred sixty one and a half. [TRACK total=361.5] The total is a float, so it keeps its decimal part. Then the two type lines print, int and float. Notice that the type belongs to the value, not to the name."),
    mem=dict(label="Names and their number objects", on="Three tags, fish, price and total, tied to an int, a float and a float", names=["fish", "price", "total"], **{"from": "A"},
             narr="Look at the picture. Fish is tied to an int, three. Price is tied to a float, one hundred twenty and a half. Total is tied to a new float, three hundred sixty one and a half. Python made that new object when it multiplied. The type is stored with the object, not with the name."),
    B=dict(file="round.py", label="Division and rounding", on="division always gives a float; round tidies decimals",
           src='''
people = 4
share = 1000 / people
print(share)
print(type(share))
print(round(1234.5678, 2))
''',
           narr="[HL 1] [TRACK people=4] Four people. [HL 2] [TRACK share=250.0] A thousand divided by four. Division with a slash always gives a float, even when the answer looks whole. [HL 3] So it prints two hundred fifty point zero. [HL 4] The type is float. [HL 5] The round function cuts a number to the places you ask for. Two places cuts the number to two digits after the point. The answer is one thousand two hundred thirty four point five seven."),
    term="Two hundred fifty point zero, the word float, then one thousand two hundred thirty four point five seven.",
    recap=["An int is a whole number and a float has a decimal point.", "An int mixed with a float gives a float.", "Division with a slash always gives a float.", "The round function tidies a float to the places you choose."],
    bug=dict(title="zero point one plus zero point two", kind="output", wrong='''
print(0.1 + 0.2)
''', fixed='''
print(round(0.1 + 0.2, 2))
''', wrong_note="a sum that looks simple", fixed_note="round to two places",
             why="Computers store decimals in binary, so some decimals are stored as close values, not exact ones; round before showing a result.",
             narr="Bug of the Day. Zero point one plus zero point two should be zero point three. Python prints zero point three, then a long tail ending in four. This is not a Python mistake. Computers store decimals in binary, and some decimals cannot be stored exactly. So round the answer before you show it, and you get a clean zero point three."),
    pun="Why did the float get invited to every party? It always brings the extra point.",
    task="print a bill split with two decimals", challenge="Split a bill of 1250.50 rupees among 3 friends and print each share rounded to 2 decimals.",
    answer="Write print(round(1250.50 / 3, 2)), which shows 416.83.",
    shorts=[
        ("Two kinds of numbers", "Python has two kinds of numbers. An int is a whole number, like three fish. A float has a decimal point, like one hundred twenty and a half rupees. You can mix them in one sum, and Python gives you a float whenever a float is in the sum. Whole things get ints, and measured things get floats. Simple as that.", "INT OR FLOAT?", "int and float in 40 seconds."),
        ("Division is a float", "A small surprise. Ten divided by two is five, but Python prints five point zero. Division with a single slash always gives a float, even when the answer looks whole. That is on purpose. A division can give a decimal, so Python always gives a float. Remember it when you print.", "1000 / 4 = 250.0", "Slash always gives a float."),
        ("What is type?", "The type function tells you the type of the object that a name points at. Type of three says int. Type of one hundred twenty and a half says float. The type belongs to the value, not to the name. So the same name can point at an int now, and a float later. Use type whenever you are unsure what you are holding.", "TYPE(3) = INT", "Check the type."),
        ("Point one plus point two", "Zero point one plus zero point two is not zero point three in Python. It prints zero point three, then a long tail ending in four. Computers store decimals in binary, and some decimals cannot be stored exactly. It is not a bug in Python. The fix is easy. Round the answer to two places before you show it.", "0.1 + 0.2 = ?", "Floats are close, not exact."),
        ("Pun and challenge", "Why did the float get invited to every party? It always brings the extra point. Your challenge. Split a bill of twelve fifty and fifty paise among three friends. Print each share, rounded to two decimals. Use division with a slash, then the round function. Write your answer in the comments, and check it twice.", "SPLIT THE BILL", "Try the bill split."),
    ],
))

EPISODES.append(dict(
    n=7, title="Strings", spoken="strings",
    yt="Python Strings: Quotes, len, + and *", thumb="TEXT IN QUOTES",
    vis="Xecxec holding a long ribbon of letters labelled Hello, Xecxec in quote marks",
    goals=["write text with single or double quotes", "count characters with len", "join strings with + and repeat them with *"],
    tags=["python strings", "string concatenation", "len function", "typeerror"],
    hash=["#strings", "#text"],
    analogy="a string of beads: each character is one bead, and len counts the beads",
    c_title="Text is a string",
    c_pts=["Text in quotes is a string", "len counts the characters", "+ joins strings and * repeats them"],
    intro="Programs are full of words. Today we learn how Python keeps text, how to count it, and how to join it.",
    concept="Text in Python is called a string. You put it inside quotes, single or double, as long as both ends match. Think of a string of beads. Each character is one bead. The len function counts the beads. You can join two strings with a plus sign, and repeat one with a star. The plus sign joins text, and the star repeats it.",
    A=dict(file="greet.py", label="Join and repeat", on="a name, a greeting, len and repeat",
           src='''
name = "Xecxec"
greeting = "Hello, " + name
print(greeting)
print(len(name))
print("ha" * 3)
''',
           narr="[HL 1] The name is the text Xecxec, in double quotes. [HL 2] Now we join. Hello, comma, space, plus the name, makes one longer string. Mind the space inside the quotes. [HL 3] Print it. [HL 4] The len function counts the characters in Xecxec. Six. [HL 5] And a string times three repeats it three times.",
           label2="Reading the output", narr2="Predict first. [TRACK greeting=Hello, Xecxec] The greeting reads Hello, Xecxec. Next, six. Last, ha ha ha, with no spaces, because we did not put any in. A string is just a row of characters, and plus and star make new rows."),
    mem=dict(label="Strings are objects", on="Two tags, name and greeting, tied to two string objects", names=["name", "greeting"], **{"from": "A"},
             narr="Here is the picture. The name tag points at the string Xecxec. The greeting tag points at a new string, Hello, Xecxec. Joining did not change the old string. It made a new one. Strings never change in place. You use that fact in a few episodes."),
    B=dict(file="quotes.py", label="Single and double quotes", on="single quotes, an apostrophe inside double quotes, and len",
           src='''
a = 'Goa'
b = "It's Goa"
print(a)
print(b)
print(len(b))
''',
           narr="[HL 1] Single quotes work. [HL 2] This text has an apostrophe inside it. So we wrap it in double quotes, and the apostrophe is safe. [HL 3] Goa prints. [HL 4] The text with the apostrophe prints. [HL 5] And len counts every character, spaces and the apostrophe too. That is eight. Choose the quote style that lets you type the text without a clash."),
    term="Goa, then the text with the apostrophe, then eight.",
    recap=["Text in quotes is a string.", "Single and double quotes both work, as long as the ends match.", "The len function counts every character, spaces included.", "Plus joins strings and star repeats them."],
    bug=dict(title="adding a string and a number", wrong='''
beaches = 5
print("Beaches: " + beaches)
''', fixed='''
beaches = 5
print("Beaches:", beaches)
''', wrong_note="the plus sign meets a number", fixed_note="print with a comma",
             why="Plus joins two strings or adds two numbers, but it cannot mix a string and a number; pass both to print with a comma instead.",
             narr="Bug of the Day. We try to add text and a number. Python says, type error. It can only concatenate a string, not an int, to a string. Plus joins text to text, or adds number to number. It does not guess. Give print both values with a comma instead, and Python handles the rest."),
    pun="Why did the string go to the beach? It wanted to catch some waves in its quotes.",
    task="join two strings and repeat one", challenge="Make two names, first and last. Print them joined with a space between. Then print the first name three times.",
    answer="Use first = \"Asha\" and last = \"Naik\", then print(first + \" \" + last) and print(first * 3), which show Asha Naik and AshaAshaAsha.",
    shorts=[
        ("What is a string?", "Text in Python is called a string. You put it inside quotes, single or double, and both ends must match. Hello is a string. A name is a string. Even a number inside quotes is a string, and not a number any more. Think of a string of beads, where every character is one bead. That is why we call it a string.", "A STRING IS TEXT", "Strings in 40 seconds."),
        ("Count with len", "The len function counts the characters in a string. Len of Xecxec is six, one for each letter. Spaces count too, and so do commas and apostrophes. So len of the text with the apostrophe is eight. Use len when you need to know how long a word is. Say the characters out loud as you count. Then you do not miscount.", "LEN(\"XECXEC\") = 6", "Counting characters."),
        ("Join and repeat", "Two string tricks. A plus sign joins two strings into one longer string, so Hello comma space plus Xecxec makes Hello, Xecxec. A star repeats a string, so ha times three makes ha ha ha with no spaces. Joining and repeating never change the old strings. They make brand new ones every single time. Try both in your own file and see.", "\"HA\" * 3", "Plus joins, star repeats."),
        ("String plus number", "Very common bug. You write text plus a number, and Python says type error. It can only concatenate a string, not an int, to a string. Plus joins text to text, or adds number to number. It does not guess. The easy fix is to give print both values with a comma. Then print does the joining for you.", "TYPEERROR: STR + INT", "Plus will not guess."),
        ("Pun and challenge", "Why did the string go to the beach? It wanted to catch some waves in its quotes. Now your challenge. Make two names, first and last. Print them joined with a space between them. Then print the first name three times in a row. Use plus for the joining and star for the repeating. Share your answer in the comments.", "JOIN + REPEAT", "Try joining strings."),
    ],
))

EPISODES.append(dict(
    n=8, title="Input from the user", spoken="input from the user",
    yt="Python input(): Ask the User a Question", thumb="ASK THE USER",
    vis="Xecxec holding a speech bubble that says Your name? beside a blinking cursor",
    goals=["read text typed by the user with input()", "use the answer in a later line", "know that input always gives a string"],
    tags=["python input", "user input python", "input function", "string concatenation"],
    hash=["#input", "#userinput"],
    analogy="a beach-shack order pad: the waiter asks, you answer, and the answer is written down as text",
    c_title="Asking questions",
    c_pts=["input() shows a question and waits", "The answer comes back as a string", "Save the answer in a name"],
    intro="So far our programs talk, but they never listen. Today your program asks a question and waits for an answer.",
    concept="The input function shows a question on the screen, then waits. You type an answer and press Enter. Python hands the answer back. Think of a waiter at a beach shack. The waiter asks a question and writes your answer on a pad. Your answer comes back as text, always. Even if you type a number, it arrives as a string. Save it in a name, and it is yours to use.",
    A=dict(file="ask.py", label="Ask two questions", on="two questions, two answers, two replies",
           src='''
name = input("Your name? ")
beach = input("Favourite beach? ")
print("Hello,", name)
print(name, "loves", beach)
''',
           stdin="Asha\nPalolem\n",
           narr="[HL 1] The input function shows the question in brackets, and waits. Whatever you type is tied to the name called name. [HL 2] A second question, and a second name. [HL 3] We greet the person by name. [HL 4] And print both answers in one line. The program now feels like a conversation.",
           label2="Reading the output", narr2="Predict first. Say the user types Asha, then Palolem. [TRACK name=Asha] The first answer goes into name. [TRACK beach=Palolem] The second goes into beach. The screen shows, Hello, Asha. Then, Asha loves Palolem. Run it with your own answers, and the output changes."),
    mem=dict(label="Typed text becomes a string", on="Two tags, word and its answer, tied to a string object", names=["word"], **{"from": "B"},
             narr="Here is what input gives back. Whatever the user types, the answer is a string object. The name word is tied to the string crab. If the user types a number, it is still a string of digits. Remember this. It causes the bug of the day."),
    B=dict(file="double.py", label="Input is always a string", on="repeat the typed word and count its characters",
           src='''
word = input("Word? ")
print(word * 2)
print(len(word))
''',
           stdin="crab\n",
           narr="[HL 1] [TRACK word=crab] We ask for a word. The user types crab. [HL 2] A string times two repeats the text. So we get crabcrab. [HL 3] The len function counts the characters, four. Here is the key point. Anything you type with input is text. Even when you type a number."),
    term="You type crab and press Enter. It prints crabcrab, then four.",
    recap=["input shows a question and waits for the user.", "The answer comes back as a string, always.", "Save the answer in a name so you can use it later.", "A number typed by the user is still text until you convert it."],
    bug=dict(title="five plus three is fifty three", kind="output", file="add.py", wrong='''
a = input("First: ")
b = input("Second: ")
print(a + b)
''', stdin="5\n3\n", fixed='''
a = input("First: ")
b = input("Second: ")
print(int(a) + int(b))
''', wrong_note="the user types 5 and 3", fixed_note="convert with int first",
             why="input always returns a string, and plus joins strings, so the digits are joined instead of added; int() turns them into numbers first.",
             narr="Bug of the Day. The user types five, then three. Our program prints fifty three, not eight. Why? Input gives strings. Plus joins strings. So the text five and the text three are joined. Wrap each answer in int, and Python adds the numbers. We look at int in four episodes."),
    pun="Why did the program wait so patiently? It had too much input.",
    task="ask for a name and a number, then print both", challenge="Ask the user for their city and their favourite number, then print both in one sentence.",
    answer="Use city = input(\"City? \") and number = input(\"Number? \"), then print(city, \"and\", number). Input stays as text, which is fine for printing.",
    shorts=[
        ("Make your program listen", "Until now your program only talked. The input function lets it listen. It shows a question on the screen, then waits. You type an answer and press Enter. Python gives the answer back, and you save it in a name. Name equals input, open bracket, your question in quotes, close bracket. That is how every quiz and every form begins.", "INPUT(\"QUESTION\")", "Make your program listen."),
        ("Input is always text", "Here is the surprise about input. Whatever the user types comes back as a string. Even if they type a number, you get the characters of that number, as text. Type four two, and you get the string four two, not the number. So you cannot do maths with it yet. First convert it. You learn how very soon.", "INPUT ALWAYS GIVES TEXT", "Typed numbers are text."),
        ("Use the answer", "Look at this program. Name equals input, your name question. Then print, hello, comma, name. The answer from the user is tied to a name, so you can use it anywhere below. Ask once, use many times. You can even ask two questions, save both answers, and print them in one sentence. Try it with your own name.", "NAME = INPUT(...)", "Ask once, use many times."),
        ("Five plus three is fifty three", "A famous beginner bug. The user types five and three, and your program prints fifty three. Why? Input gives strings, and plus joins strings. So the text five and the text three are joined into fifty three. The fix is to wrap each answer in int, so Python adds numbers instead. Always convert before you do maths.", "\"5\" + \"3\" = \"53\"", "Input gives strings."),
        ("Pun and challenge", "Why did the program wait so patiently? It had too much input. Your challenge. Ask the user for their city and for their favourite number. Then print both in one sentence, like, I love city and number. Do not worry about maths today, because we are only printing. Post your answer in the comments below.", "ASK TWO QUESTIONS", "Try two questions."),
    ],
))

EPISODES.append(dict(
    n=9, title="Operators", spoken="operators",
    yt="Python Operators: + - * / // % **", thumb="SEVEN OPERATORS",
    vis="Xecxec wearing a tool belt holding seven symbols: plus, minus, star, slash, double slash, percent, double star",
    goals=["use + - * / for arithmetic", "use // and % for whole-number division and remainder", "use ** for powers and avoid ^"],
    tags=["python operators", "floor division", "modulo python", "power operator"],
    hash=["#operators", "#maths"],
    analogy="a school bus: floor division counts the full buses, and the remainder counts the students left standing",
    c_title="Seven operators",
    c_pts=["+ - * / are the maths you know", "// gives whole-number division, % gives the remainder", "** is power; ^ is something else"],
    intro="Python is a very good calculator. Today we learn seven symbols that do all the maths you need.",
    concept="An operator is a symbol that does a job. Plus, minus, star and slash you know. Two more are useful. Double slash divides and drops the decimal part. Percent gives the remainder. And double star raises to a power. Think of a school bus with ten seats. Floor division counts the full buses. The remainder counts the students left standing. Seven symbols, and you are ready.",
    A=dict(file="ops.py", label="The seven operators", on="one number and seven results",
           src='''
total = 17
print(total + 3)
print(total - 3)
print(total * 3)
print(total / 3)
print(total // 3)
print(total % 3)
print(2 ** 5)
''',
           narr="[HL 1] Total is seventeen. [HL 2] Plus three gives twenty. [HL 3] Minus three gives fourteen. [HL 4] Star three gives fifty one. [HL 5] The slash gives a float, five point six six six and a long tail. [HL 6] Double slash drops the decimal part, so five. [HL 7] Percent keeps what is left over, so two. [HL 8] And two double star five is two to the power five, thirty two.",
           label2="Reading the output", narr2="Predict first. [TRACK total=17] Seventeen is the starting value. Seventeen divided by three is five, with two left over. That is why double slash gives five and percent gives two. Together they split a number into whole groups and a remainder."),
    mem=dict(label="One name, many results", on="The name total tied to the int 17", names=["total"], **{"from": "A"},
             narr="Look at what Python holds after the run. Only one name, total, tied to seventeen. All the other results were printed and forgotten, because we never gave them a name. If you want to keep a result, tie it to a name. We do that in the next program."),
    B=dict(file="bus.py", label="Buses and standing students", on="floor division and remainder together",
           src='''
students = 47
seats = 10
buses = students // seats
left = students % seats
print("Full buses:", buses)
print("Standing:", left)
''',
           narr="[HL 1] [TRACK students=47] Forty seven students. [HL 2] [TRACK seats=10] Ten seats per bus. [HL 3] [TRACK buses=4] Double slash gives the full buses. Four. [HL 4] [TRACK left=7] Percent gives the rest. Seven students have no seat in those four buses. [HL 5] Print the buses. [HL 6] Print the standing students."),
    term="Full buses, four. Standing, seven.",
    recap=["Plus, minus, star and slash are the usual arithmetic.", "Double slash gives the whole part and percent gives the remainder.", "Double star raises a number to a power.", "The caret symbol is not power in Python."],
    bug=dict(title="the caret is not a power", kind="output", file="power.py", wrong='''
print(2 ^ 3)
''', fixed='''
print(2 ** 3)
''', wrong_note="the caret instead of a power", fixed_note="double star",
             why="In Python the caret is a bit operator called XOR, not a power; use ** for powers.",
             narr="Bug of the Day. We want two to the power three, which is eight. In maths class, the caret means power. In Python, it does something else. It works on binary digits. We get one, with no error at all. Use double star for powers, and you get eight. Watch for bugs that run quietly."),
    pun="Why was the remainder so calm? It never let the division get to it.",
    task="find buses and remainder with // and %", challenge="A van seats 7 people. For 30 people, print how many full vans there are and how many people are left over.",
    answer="Use print(30 // 7) for 4 full vans and print(30 % 7) for 2 people left over.",
    shorts=[
        ("Seven operators", "Python is a very good calculator. Plus, minus, star and slash do the usual arithmetic. Double slash gives the whole part of a division. Percent gives the remainder. And double star raises a number to a power. That is seven symbols. Learn these seven, and you can do almost any calculation that appears in beginner programs. Practise them one by one.", "7 OPERATORS", "The seven symbols."),
        ("Floor division and remainder", "Seventeen divided by three is five, with two left over. Python gives you both pieces. Double slash gives the five, the whole groups. Percent gives the two, the remainder. Think of a bus with three seats. Five buses are full, and two students still stand. Use these two together whenever you split things into groups. They are a very handy pair.", "17 // 3 = 5 · 17 % 3 = 2", "Groups and leftovers."),
        ("The slash gives a float", "Here is a small detail. Ten divided by two with a single slash gives five point zero, not five. A slash always gives a float, even when the answer looks whole. If you want a whole number, use the double slash. So ten double slash two gives plain five. Pick the operator that matches the answer you want.", "10 / 2 = 5.0", "Slash versus double slash."),
        ("The caret trap", "In maths class, the caret means power. In Python, two caret three does not give eight. It gives one, and there is no error at all. The caret is a different operation called XOR. For a power, use double star. Two double star three gives eight. Bugs that run quietly are the hardest ones to spot, so remember this.", "2 ^ 3 = 1 ?!", "Caret is not power."),
        ("Pun and challenge", "Why was the remainder so calm? It never let the division get to it. Your challenge. A van seats seven people, and thirty people want to travel. Print how many full vans there are, then print how many people are left over. Use double slash and percent. Write your two answers in the comments, and show your code.", "VANS AND LEFTOVERS", "Try the van sum."),
    ],
))

EPISODES.append(dict(
    n=10, title="f-strings and formatting", spoken="f-strings and formatting",
    yt="Python f-strings: Print Values the Easy Way", thumb="F-STRINGS",
    vis="Xecxec pointing at the letter f in front of a string with curly brackets glowing",
    goals=["put values inside text with f-strings", "do a small calculation inside curly brackets", "format decimals and align columns"],
    tags=["python f-strings", "string formatting python", "format decimals python", "print formatting"],
    hash=["#fstrings", "#formatting"],
    analogy="a printed bill with blank spaces: the f tells Python to fill the spaces with real values",
    c_title="Fill in the blanks",
    c_pts=["Put f before the opening quote", "Write values inside curly brackets", "Add a format after a colon, like :.2f"],
    intro="Joining text and numbers with commas works, but there is a neater way. Today we meet f-strings, the favourite tool of Python programmers.",
    concept="An f-string is a string with the letter f in front. Inside it, curly brackets hold names or sums. Python fills them in. Think of a printed bill with blank spaces. The f tells Python to fill the blanks with real values. After a colon inside the brackets, you can add a format. A colon, dot, two, f means, show two decimal places. Neat bills, no extra effort.",
    A=dict(file="fstr.py", label="f-strings in action", on="a value, a sum and a two-decimal format",
           src='''
fish = 3
price = 120.5
print(f"Fish: {fish}")
print(f"Total: {fish * price}")
print(f"Total: {fish * price:.2f}")
''',
           narr="[HL 1] Fish is three. [HL 2] Price is one hundred twenty and a half. [HL 3] The f before the quote turns the string into an f-string. The curly brackets hold the name fish, and Python puts the value in. [HL 4] Brackets can hold a sum too. Python works it out first. [HL 5] After the colon, dot two f says, show two decimal places. So we get three hundred sixty one point five zero.",
           label2="Reading the output", narr2="Predict first. [TRACK fish=3] The first line says, Fish, three. The second says, Total, three hundred sixty one point five. The third says, Total, three hundred sixty one point five zero. The same number, shown with two decimals. That is the colon format at work."),
    mem=dict(label="Values stay in their names", on="Two name tags, fish and price, tied to an int and a float", names=["fish", "price"], **{"from": "A"},
             narr="Nothing changes in memory when we print. Fish stays tied to the int three. Price stays tied to the float one hundred twenty and a half. The f-string builds a brand new string for each print line, and then that string is gone. The names and values you made are untouched."),
    B=dict(file="receipt.py", label="A neat receipt", on="aligning a name and an amount in columns",
           src='''
item = "Fish thali"
cost = 249.5
qty = 2
print(f"{item:<12}|{cost:>8.2f}|")
print(f"{'Total':<12}|{cost * qty:>8.2f}|")
''',
           narr="[HL 1] [TRACK item=Fish thali] The item name. [HL 2] [TRACK cost=249.5] The cost. [HL 3] [TRACK qty=2] The quantity. [HL 4] Less than twelve pads the text on the right to twelve spaces. Greater than eight pads the number on the left, with two decimals. The bars let us see the columns. [HL 5] The total uses a sum inside the brackets. Notice the single quotes inside the double quotes, so the quotes do not clash."),
    term="Two neat lines, with the bars lined up under each other.",
    recap=["Put f before the opening quote to make an f-string.", "Curly brackets hold names or small sums.", "Colon, dot, two, f shows two decimals.", "Less than and greater than set the alignment."],
    bug=dict(title="forgetting the f", kind="output", file="hello.py", wrong='''
name = "Asha"
print("Hello, {name}")
''', fixed='''
name = "Asha"
print(f"Hello, {name}")
''', wrong_note="no f before the quote", fixed_note="f added",
             why="Without the f prefix the curly brackets are plain characters, so Python prints them exactly as typed.",
             narr="Bug of the Day. We forgot the f. Python does not complain. It prints Hello, curly bracket name curly bracket, exactly as typed, because without the f the brackets are just characters. Add the f in front of the opening quote, and Python fills in the name. When you see curly brackets in your output, check for the f."),
    pun="Why did the f-string get promoted? It always knew what to fill in.",
    task="print a bill line with two decimals", challenge="Make price = 99.5 and qty = 3. Then print a line like Total: 298.50. Use an f-string with two decimals.",
    answer="Use print(f\"Total: {price * qty:.2f}\"), which shows Total: 298.50.",
    shorts=[
        ("What is an f-string?", "An f-string is a string with the letter f in front of the opening quote. Inside it, curly brackets hold names or small sums, and Python fills them in. So f, quote, Hello comma, curly name curly, quote, prints Hello and the real name. It is neater than joining with plus, and you never need to convert numbers first.", "F\"HELLO {NAME}\"", "The friendliest way to print."),
        ("A sum inside the brackets", "You can put a calculation inside the curly brackets. Fish times price, inside the brackets, and Python works it out, then puts the answer in the text. You do not need a separate name for the answer. Short programs look much tidier this way. Try it with your own numbers, and watch Python do the sum in the middle of a sentence.", "{FISH * PRICE}", "Maths inside the text."),
        ("Two decimals", "After a colon inside the brackets, you can add a format. Colon, dot, two, f means show two decimal places. So three hundred sixty one point five becomes three hundred sixty one point five zero. This is perfect for money. It only changes how the number looks. The number itself stays exactly the same in the program.", "{TOTAL:.2F}", "Money with two decimals."),
        ("Forgot the f", "Here is the quiet bug. You write print, quote, Hello, curly name curly, quote, but you forget the f. Python does not complain. It prints the curly brackets exactly as typed, with the word name between them. Whenever you see curly brackets in your output, check the front of the string. One small letter fixes it, and the magic returns.", "NO F, NO MAGIC", "Check the f."),
        ("Pun and challenge", "Why did the f-string get promoted? It always knew what to fill in. Your challenge. Make price equal ninety nine point five, and qty equal three. Then print a line that says Total, colon, and the answer with two decimals, using an f-string. The answer should have a zero at the end. Write your code in the comments.", "PRINT A NEAT TOTAL", "Try the f-string."),
    ],
))

EPISODES.append(dict(
    n=11, title="Booleans and comparisons", spoken="booleans and comparisons",
    yt="Python Booleans: True, False and ==", thumb="TRUE OR FALSE?",
    vis="Xecxec holding a green TRUE card in one claw and a red FALSE card in the other",
    goals=["use comparison operators to get True or False", "tell == from =", "store a comparison in a name"],
    tags=["python booleans", "python comparison operators", "equals vs assignment", "syntaxerror"],
    hash=["#booleans", "#comparisons"],
    analogy="a bouncer at a beach club who only answers yes or no: are you eighteen or older?",
    c_title="Yes or no answers",
    c_pts=["A boolean is True or False", "Compare with == != < > <= >=", "One equals sign ties a name; two compare"],
    intro="Computers make decisions with yes or no answers. Today we meet True and False, and the symbols that produce them.",
    concept="A boolean is a value that is either True or False. Python makes one whenever you compare two things. Double equals asks, are these the same? Not equals, less than, greater than, and their or equal versions ask other questions. Think of a bouncer at a beach club. The bouncer only says yes or no. One equals sign ties a name to a value. Two equals signs ask a question.",
    A=dict(file="compare.py", label="Comparisons", on="a comparison saved in a name",
           src='''
age = 17
adult = age >= 18
print(adult)
print(age == 17)
print(age != 17)
''',
           narr="[HL 1] Age is seventeen. [HL 2] Greater than or equal to eighteen is a question. The answer is False, and we tie that answer to the name adult. [HL 3] Printing adult shows False. [HL 4] Double equals asks, is age seventeen? That is True. [HL 5] Not equals asks, is age different from seventeen? That is False.",
           label2="Reading the output", narr2="Predict first. [TRACK adult=False] The adult name holds False. The first print is False. The second is True. The third is False. Each comparison gives back a boolean, and a boolean is a value like any other. You can save it, print it, and use it in decisions."),
    mem=dict(label="A boolean is an object too", on="Two tags, age and adult, tied to an int and a bool", names=["age", "adult"], **{"from": "A"},
             narr="Here is the picture. Age is tied to the int seventeen. Adult is tied to a bool, False. A boolean is an object like any number or string. Its type is bool, and it has only two possible values, True and False. Write them with a capital first letter."),
    B=dict(file="beaches.py", label="Comparing text and chains", on="comparing strings, and a chained comparison",
           src='''
beach = "Palolem"
print(beach == "Palolem")
print(beach == "palolem")
print(5 < 10 < 20)
''',
           narr="[HL 1] A name tied to Palolem. [HL 2] The same text on both sides, so True. [HL 3] A small letter p is a different character. So this comparison is False. Python is case sensitive for text too. [HL 4] Python even lets you chain. Five is less than ten, and ten is less than twenty. Both are true, so the answer is True."),
    term="True, then False, then True.",
    recap=["A boolean is True or False, with a capital first letter.", "Comparison operators give back booleans.", "One equals sign ties a name; two equals signs compare.", "Text comparisons are case sensitive."],
    bug=dict(title="one equals sign instead of two", file="compare.py", wrong='''
age = 17
if age = 18:
    print("Adult")
''', fixed='''
age = 17
if age == 18:
    print("Adult")
''', wrong_note="a single equals inside the if", fixed_note="double equals compares",
             why="A single equals ties a name to a value, so it cannot be used as a question; double equals compares two values.",
             narr="Bug of the Day. Inside the if we wrote one equals sign. Python says, syntax error, invalid syntax. It even guesses what you meant, maybe you meant double equals. One equals sign is an instruction, tie this name to that value. A question needs two. Fix it, and the program runs."),
    pun="Why did the boolean break up with the string? It only wanted a True relationship.",
    task="print whether a score passes", challenge="Make score = 55 and print True or False for score >= 40, and print whether score == 55.",
    answer="Use print(score >= 40) which shows True, and print(score == 55) which also shows True.",
    shorts=[
        ("True or False", "A boolean is a value that is either True or False. Python gives you one every time you compare two things. Is seventeen bigger than eighteen? False. Is seventeen equal to seventeen? True. The first letter is always a capital. A boolean is a value like any other. You can save it in a name and print it.", "TRUE OR FALSE", "Booleans in 40 seconds."),
        ("Six comparison symbols", "Six symbols make comparisons. Double equals asks, are they the same. Not equals asks, are they different. Less than and greater than compare size. Less than or equal, and greater than or equal, include the same number too. Each one gives back True or False. Learn these six, and you are ready for decisions with if and else.", "== != < > <= >=", "Six ways to ask."),
        ("One equals or two", "One equals sign and two equals signs are very different. One equals sign ties a name to a value. It is an instruction. Two equals signs ask a question, are these the same, and give True or False. Say it in your head, equals means tie, double equals means ask. This tiny difference is behind many beginner bugs, so learn it now.", "= TIES · == ASKS", "Tie or ask?"),
        ("Invalid syntax", "Here is the bug. You write if age equals eighteen with one equals sign. Python says syntax error, invalid syntax. It even adds a hint, maybe you meant double equals. The if line needs a question, and one equals sign is an instruction, not a question. Use two equals signs, and the program runs. Read the hint, it is very friendly.", "SYNTAXERROR: MAYBE ==", "Python gives a hint."),
        ("Pun and challenge", "Why did the boolean break up with the string? It only wanted a True relationship. Your challenge. Make score equal fifty five. Print whether score is at least forty, and print whether score equals fifty five. You should see two words, in capital letters. Try changing score to thirty, and run again. Post your code in the comments.", "COMPARE A SCORE", "Try the comparisons."),
    ],
))

EPISODES.append(dict(
    n=12, title="Type conversion", spoken="type conversion",
    yt="Python Type Conversion: int(), float(), str()", thumb="CHANGE THE TYPE",
    vis="Xecxec turning a string 42 into a number with a crank labelled int()",
    goals=["convert text to numbers with int() and float()", "convert numbers to text with str()", "read a ValueError when text is not a number"],
    tags=["python type conversion", "int float str python", "valueerror python", "input to number"],
    hash=["#typeconversion", "#int"],
    analogy="a currency counter: the same value, written in a different note",
    c_title="Changing types",
    c_pts=["int() makes a whole number", "float() makes a decimal", "str() makes text"],
    intro="Input gives text, and maths needs numbers. Today we learn how to change one type into another, and what happens when it goes wrong.",
    concept="Python has three conversion tools. The int function makes a whole number. The float function makes a decimal. The str function makes text. Think of a currency counter. The value is the same, but it is written on a different note. The conversion makes a new object. The old one is left as it was. If the text cannot be a number, Python raises an error.",
    A=dict(file="convert.py", label="int, float and str", on="three conversions in three lines",
           src='''
text = "42"
number = int(text)
print(number + 8)
print(float("3.5") * 2)
print(str(7) + " beaches")
''',
           narr="[HL 1] The name text is tied to the string forty two. [HL 2] The int function makes a new object, the number forty two, tied to number. [HL 3] Now plus eight works. It prints fifty. [HL 4] The float function turns three point five text into a float, and times two gives seven point zero. [HL 5] The str function turns seven into text, so plus can join it with the word beaches.",
           label2="Reading the output", narr2="Predict first. [TRACK number=42] The first print is fifty. The second is seven point zero. The third is, seven beaches. In every line, a conversion makes a new value. We never changed the original text."),
    mem=dict(label="Convert makes a new object", on="The name text tied to a string, and number tied to an int", names=["text", "number"], **{"from": "A"},
             narr="Here is the picture. The name text is still tied to the string forty two. The name number is tied to a brand new int, forty two. They look alike when printed, but they are different objects of different types. A string can join, and an int can add. Conversion is how you move between the two."),
    B=dict(file="age_next.py", label="Convert input", on="convert typed text to a number, then add one",
           src='''
age = int(input("Age? "))
print("Next year:", age + 1)
''',
           stdin="17\n",
           narr="[HL 1] [TRACK age=17] Read this from the inside out. First input asks the question. The answer arrives as the string seventeen. Then int turns that string into the number seventeen. [HL 2] Now plus one works, and Next year, eighteen prints. This pattern, int wrapped around input, is how every program reads a number."),
    term="You type seventeen. It prints, Next year, eighteen.",
    recap=["int(), float() and str() convert between types.", "Conversion makes a new object and leaves the old one alone.", "Wrap int around input() to read a number.", "Text that is not a number raises a ValueError."],
    bug=dict(title="int of a word", file="convert.py", wrong='''
count = int("abc")
''', fixed='''
count = int("42")
''', wrong_note="the text is not a number", fixed_note="the text holds digits",
             why="int() can only convert text that looks like a whole number, so a word raises a ValueError.",
             narr="Bug of the Day. We ask int to turn the word abc into a number. Python says, value error, invalid literal for int. The text must look like a whole number. Digits are fine. Letters are not. The last line tells you the exact text that failed, which makes the bug easy to find. Fix the text, and it works."),
    pun="Why did the string go to therapy? It had trouble converting its feelings into numbers.",
    task="read a number and print double", challenge="Ask the user for a number with input, then print double that number using int().",
    answer="Use n = int(input(\"Number? \")) and print(n * 2). If the user types 21, it prints 42.",
    shorts=[
        ("Three conversion tools", "Python has three conversion tools. The int function makes a whole number. The float function makes a decimal. The str function makes text. Each one gives you a brand new object, and leaves the old one as it was. So int of the string forty two gives the number forty two. Learn these three, and you can move between types easily.", "INT · FLOAT · STR", "Change the type."),
        ("Read a number", "Here is the pattern every program uses to read a number. Age equals int, open bracket, input, open bracket, the question, close bracket, close bracket. Input asks and gives text. Int turns the text into a number. Then you can add, compare and multiply as much as you like. Read it from the inside out, and it makes sense.", "INT(INPUT(...))", "The read-a-number pattern."),
        ("A new object", "When you convert, Python makes a new object. The name text still points at the string forty two. The name number points at a new int, forty two. They print the same, but they behave differently. A string can join with another string. An int can do maths. Pick the type that does the job you need.", "TEXT 42 → NUMBER 42", "Conversion makes a new value."),
        ("Value error", "What if the text is not a number? Int of the word abc does not work. Python says value error, invalid literal for int. The text must look like a whole number, so digits are fine, and letters are not. The last line shows the exact text that failed. Check what your user typed, and the bug becomes easy to see.", "VALUEERROR: INVALID LITERAL", "Letters are not digits."),
        ("Pun and challenge", "Why did the string go to therapy? It had trouble converting its feelings into numbers. Your challenge. Ask the user for a number. Then print double that number. Remember, input gives text, so convert it with int first. If the user types twenty one, your program should print forty two. Share your code in the comments, please.", "DOUBLE THE NUMBER", "Try the conversion."),
    ],
))
