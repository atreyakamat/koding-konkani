import re
# Python course, Module 0 (EP1-4)
import data_cpp as C
MOD = dict(module=0, mod_name="Welcome & setup", bgacc="Peach + Tomato")
TC, CS, CE, MB, TM, BG, PC, CH, OU = C.TC, C.CS, C.CE, C.MB, C.TM, C.BG, C.PC, C.CH, C.OU

def std_scenes(*a, **k):
    sc = C.std_scenes(*a, **k)
    for s in sc:
        if s["tpl"] == BG:
            s["anim"] = "Butter banner drops in with a buzzer; wrong code shakes; the Python error lines appear in tomato; the fix slides in and the terminal turns mint with a ding"
        if s["tpl"] == TM:
            s["anim"] = "Dark-blue terminal: the command types with key-tick, output prints in mint with a ding"
    return sc

EP1_CODE = '''print("Hello, Goa!")
print("Keep coding, says Xecxec!")'''
EP1_BUG = 'print("Hello, Goa!)'
EP1_FIX = 'print("Hello, Goa!")'

EP1 = dict(ep=1, title="Hello, Python!", prereq="none", **MOD,
 goals=["write and run a first Python program", "use print() to show text on the screen", "know that text goes inside quotes"],
 yt=dict(title="Hello, Python! Your First Program | Python Programming EP 01",
   desc="Write and run your very first Python program with Xecxec the crab. No experience needed, just bring curiosity.",
   tags=["python", "python for beginners", "python tutorial", "hello world python", "print function", "koding konkani", "learn programming", "class 11 computer science", "first year engineering", "coding in goa"],
   thumb_text="HELLO, PYTHON!", thumb_visual="in tomato on peach; Xecxec waving a claw at a dark-blue terminal card showing Hello, Goa!; thin black border and drop shadow.",
   chapters={1: "Intro", 2: "What is Python?", 3: "print line by line", 4: "How Python runs your file", 5: "Run it in your head", 6: "Run it", 7: "Recap", 8: "Bug of the Day", 10: "Challenge", 11: "Next episode"}),
 files=[dict(name="hello.py", source=EP1_CODE, scene="3, 5")],
 scenes=std_scenes((1, "HELLO, PYTHON!"),
   "Welcome to Koding Konkani! I am your narrator, and this little crab is Xecxec. In this series you will learn Python from zero. Today, we write our very first program.",
   ("What is Python", '"What is Python?": three numbered lines and a fish-curry recipe card on the right', "Lines spring in one by one with a pop; the recipe card slides in from the right",
    "Python is a programming language. You write instructions in plain text, and Python reads them from top to bottom and does what they say. Think of a recipe card for fish curry. The card is your code, and Python is the cook who follows it, step by step. Python is popular because its words look almost like English, so beginners can read it from day one."),
   ("print line by line", "`hello.py`: the 2-line first program, line 1 is the star",
    "[HL 1] This is the whole first program. The word print is a function. It shows something on the screen. The round brackets hold what to show. The quotes mean, this is text. Hello, Goa is the text. [HL 2] A second line prints the sign-off. Python runs line one, then line two, always in order."),
   ("How Python runs your file", "Three boxes: your file, Python, the screen; arrows between them",
    "Three boxes appear left to right; arrows draw on between them with a whoosh; the screen box lights up when text arrives",
    "Here is the journey. Your file goes to Python. Python reads line one, runs it, then reads line two, runs it. The text appears on the screen. There is no separate building step. Python reads and runs at the same time. That is why a mistake shows up the moment Python reaches that line.", CS),
   ("Run it in your head", "`hello.py` again, with the output panel on the right",
    "[HL 1] When this line runs, Hello, Goa appears. [HL 2] Then the next line prints underneath. Each print starts on a fresh line on its own. Change the words inside the quotes and the output changes too. Try your own name. Before you run it, predict the output. Two lines. The second says, Keep coding, says Xecxec. Predicting before running is the habit that makes you fast."),
   ("Run it", "Terminal: `python hello.py`",
    "Save the file as hello dot py. In the terminal, type python, space, hello dot py. There it is. Our first program. On some Macs and Linux machines, the command is python three."),
   ("Bug of the Day", "BUG OF THE DAY: a missing closing quote",
    "Bug of the Day. We forgot the closing quote. Python says, syntax error, unterminated string literal. It even shows an arrow under where the text starts. Add the quote, and it runs. Whenever you see unterminated, count your quotes."),
   ("I would tell you a Python joke, but I forgot to close the quote.", "I would tell you a Python joke, but I forgot to close the quote."),
   ("Task card: print your name, then your favourite beach", "Your challenge: print your name on one line, and your favourite beach on the next. Comment your answer below."),
   ("Next: EP 02 · Installing Python and running scripts", "Next time: installing Python and running scripts properly. Keep coding, says Xecxec!")),
 bug=dict(file="hello.py", intro="the closing quote is missing", wrong=EP1_BUG, fix_intro="closing quote added", fixed=EP1_FIX, expect=["SyntaxError: unterminated string literal"],
   why="Every opening quote needs a closing quote of the same kind, otherwise Python cannot tell where the text ends."),
 pun="\"I would tell you a Python joke, but I forgot to close the quote.\"",
 challenge="Print your name on one line and your favourite beach on the next.",
 answer="Use two print lines, for example Atreya, then Palolem.",
 answer_code='print("Atreya")\nprint("Palolem")',
 shorts=[
  dict(id="S1", title="The smallest Python program", built=[3], hook="One line is a whole program.", script="One line is a whole program. Print, brackets, quotes. That is a working Python program. Everything you learn next is built on it.", on="THE SMALLEST PYTHON PROGRAM", caption="Your first Python line.", tags=["python", "learntocode", "kodingkonkani", "beginners", "goa"]),
  dict(id="S2", title="Python reads top to bottom", built=[4], hook="Line one, then line two.", script="Line one, then line two. Python reads your file from top to bottom and runs each line in order. No waiting, and no separate build step.", on="PYTHON READS TOP TO BOTTOM", caption="How Python runs your code.", tags=["python", "interpreter", "programming", "kodingkonkani", "coding"]),
  dict(id="S3", title="What does print do?", built=[3, 5], hook="A function with one job.", script="A function with one job. print shows text on the screen. Put words in quotes and they appear exactly as written. Each print starts on a fresh line.", on="PRINT(\"TEXT\")", caption="print explained slowly.", tags=["python", "print", "helloworld", "kodingkonkani", "coding"]),
  dict(id="S4", title="The missing quote", built=[8], hook="One missing character, one angry Python.", script="One missing character, one angry Python. Forget the closing quote and Python says, unterminated string literal. Count your quotes.", on="UNTERMINATED STRING LITERAL", caption="Quotes come in pairs.", tags=["python", "bugfix", "syntaxerror", "kodingkonkani", "coding"]),
  dict(id="S5", title="Pun and challenge", built=[9, 10], hook="Python jokes need closing quotes.", script="Python jokes need closing quotes. I would tell you one, but I forgot to close the quote. Your challenge: print your name, then your favourite beach. Full video: EP 1.", on="PRINT YOUR NAME + YOUR BEACH", caption="Try the challenge.", tags=["python", "codingchallenge", "kodingkonkani", "programmingjokes", "goa"]),
 ])

EP2_CODE = '''fish = 3
price = 120
print("Fish:", fish)
print("Total:", fish * price)'''
EP2_BUG = 'fish = 3\nPrint("Fish:", fish)'
EP2_FIX = 'fish = 3\nprint("Fish:", fish)'

EP2 = dict(ep=2, title="Installing Python and running scripts", prereq="EP 01", **MOD,
 goals=["install Python and check it with python --version", "tell the REPL from a script file", "run a script with python file.py"],
 yt=dict(title="Install Python and Run Your First Script | Python Programming EP 02",
   desc="Set up Python and VS Code on Windows, Mac or Linux, then run scripts with Xecxec.",
   tags=["install python", "python setup", "vs code python", "run python script", "python for beginners", "koding konkani", "python tutorial", "class 11 computer science", "coding in goa", "learn python"],
   thumb_text="SET UP PYTHON", thumb_visual="in tomato on peach; Xecxec raising both claws beside a terminal showing python --version; thin black border and drop shadow.",
   chapters={1: "Intro", 2: "What you need", 3: "Install and check", 4: "REPL versus script", 5: "A script with numbers", 6: "Run it", 7: "Recap", 8: "Bug of the Day", 10: "Challenge", 11: "Next episode"}),
 files=[dict(name="fish.py", source=EP2_CODE, scene="5")],
 scenes=std_scenes((2, "SET UP PYTHON"),
   "Welcome back! Last time we ran one program. Today we set up your computer so you can run your own. It takes about ten minutes, and you only do it once.",
   ("What you need", '"What you need": three numbered lines and a kitchen analogy card', "Lines spring in one by one with a pop; the kitchen card slides in with a chopping board, a stove and a chef",
    "You need three things. Python itself. An editor, where you type, like VS Code. And a terminal, where you give commands. Think of a kitchen. Python is the stove, the editor is the chopping board, and the terminal is you, giving the orders. Do not worry if the names sound strange. By the end of today, you will have typed every one of these commands yourself."),
   ("Install and check", "Install steps for Windows, Mac and Linux, shown as three tabs",
    "Go to python dot org, open Downloads, and install the latest version. On Windows, tick the box that says, add Python to PATH. On a Mac, run the installer. On Linux, Python is usually already there. Then open a terminal and type python, space, dash dash version. If a number appears, you are ready. On some Macs and Linux machines, the command is python three."),
   ("REPL versus script", "Two boxes: the REPL, one line and an answer at once; a script, many lines in a saved .py file",
    "Two boxes pop in side by side; in the left box a line types and its answer appears at once; in the right box a saved file runs top to bottom",
    "Python has two ways to run code. In the REPL, you type one line and get the answer at once. It is great for tiny tests. In a script, you save many lines in a file that ends in dot py, and run the whole file. We will mostly use scripts, because you can keep them, fix them, and run them again.", CS),
   ("A script with numbers", "`fish.py`: two names, a label and a total",
    "[HL 1] [TRACK fish=3] Make a name called fish, and put three in it. [HL 2] [TRACK price=120] A name called price, one hundred twenty. [HL 3] Print a label, then the value. Print puts a space between the things for you. [HL 4] And Python does the maths: fish times price. Three times one hundred twenty is three hundred sixty."),
   ("Run it", "Terminal: `python fish.py`",
    "Save the file as fish dot py. In the terminal, type python, space, fish dot py. Fish, three. Total, three hundred sixty. Always check that you are in the same folder as the file."),
   ("Bug of the Day", "BUG OF THE DAY: print with a capital P",
    "Bug of the Day. We wrote print with a capital P. Python says, name error, Print is not defined. And it even asks, did you mean print, with a small p? Python is case sensitive. Capital P and small p are different names. Fix the letter, and it works."),
   ("Why did the snake get lost in the folder? It kept running the wrong dot py.", "Why did the snake get lost in the folder? It kept running the wrong dot py."),
   ("Task card: install, check the version, run fish.py, change the price", "Your challenge: install Python, check the version, and run fish dot py. Then change the price and run it again."),
   ("Next: EP 03 · How Python reads your code", "Next: how Python reads your code. Keep coding, says Xecxec!")),
 bug=dict(file="fish.py", intro="print is spelled with a capital P", wrong=EP2_BUG, fix_intro="small p", fixed=EP2_FIX, expect=["NameError: name 'Print' is not defined", "Did you mean: 'print'?"],
   why="Python treats upper and lower case as different letters, so Print and print are two different names."),
 pun="\"Why did the snake get lost in the folder? It kept running the wrong .py.\"",
 challenge="Install Python, check the version, run fish.py, then change the price and run it again.",
 answer="Change price = 120 to price = 150 and run again: the total becomes 450.",
 answer_code=EP2_CODE.replace("price = 120", "price = 150"),
 shorts=[
  dict(id="S1", title="What you need for Python", built=[2], hook="Three tools, ten minutes.", script="Three tools, ten minutes. Python, an editor and a terminal. Python is the stove, VS Code is the chopping board, and the terminal is you, giving the orders.", on="3 TOOLS FOR PYTHON", caption="Set up Python in three steps.", tags=["python", "setup", "beginners", "kodingkonkani", "goa"]),
  dict(id="S2", title="Check your install", built=[3], hook="Is Python really installed?", script="Is Python really installed? Open the terminal and type python, dash dash version. A number means you are ready. On some machines, the command is python three.", on="PYTHON --VERSION", caption="One command to check.", tags=["python", "terminal", "setup", "kodingkonkani", "learntocode"]),
  dict(id="S3", title="REPL versus script", built=[4], hook="Two ways to run Python.", script="Two ways to run Python. The REPL runs one line at a time, great for tiny tests. A script is a saved dot py file that runs from top to bottom. Use scripts for real programs.", on="REPL OR SCRIPT?", caption="REPL or script?", tags=["python", "repl", "script", "kodingkonkani", "coding"]),
  dict(id="S4", title="Print is not defined", built=[8], hook="One capital letter breaks everything.", script="One capital letter breaks everything. Write Print with a capital P and Python says, name error, Print is not defined. Python is case sensitive, so use a small p.", on="NAMEERROR: PRINT IS NOT DEFINED", caption="Python is case sensitive.", tags=["python", "bugfix", "nameerror", "kodingkonkani", "coding"]),
  dict(id="S5", title="Pun and challenge", built=[9, 10], hook="A snake lost in a folder.", script="A snake lost in a folder. Why? It kept running the wrong dot py. Your challenge: run fish dot py, change the price, and run it again. Full video: EP 2.", on="RUN FISH.PY + CHANGE THE PRICE", caption="Do the challenge.", tags=["python", "codingchallenge", "kodingkonkani", "programmingjokes", "goa"]),
 ])

EP3_CODE = '''age = 17
if age >= 18:
    print("You can vote.")
else:
    print("Not yet.")
print("Done.")'''
EP3_BUG = '''age = 17
if age >= 18:
    print("You can vote.")
  else:
    print("Not yet.")'''
EP3_FIX = '''age = 17
if age >= 18:
    print("You can vote.")
else:
    print("Not yet.")'''

EP3 = dict(ep=3, title="How Python reads your code", prereq="EP 02", **MOD,
 goals=["explain that Python runs lines in order, top to bottom", "see that indentation is part of the code", "write a first if and else with a correct indent"],
 yt=dict(title="How Python Reads Your Code: Lines and Indentation | Python Programming EP 03",
   desc="Learn why Python cares about spaces at the start of a line, with Xecxec.",
   tags=["python indentation", "python syntax", "if else python", "python for beginners", "koding konkani", "python tutorial", "class 11 computer science", "coding in goa", "learn python", "indentationerror"],
   thumb_text="SPACES MATTER", thumb_visual="in tomato on peach; Xecxec shaking his shell beside a code card with indent guide lines; thin black border and drop shadow.",
   chapters={1: "Intro", 2: "Top to bottom", 3: "Indentation", 4: "The two rooms", 5: "Follow the path", 6: "Run it", 7: "Recap", 8: "Bug of the Day", 10: "Challenge", 11: "Next episode"}),
 files=[dict(name="age.py", source=EP3_CODE, scene="3, 5")],
 scenes=std_scenes((3, "SPACES MATTER"),
   "Today we learn why Python cares about spaces at the start of a line. In many languages they are decoration. In Python, they are part of the code.",
   ("Top to bottom", '"Top to bottom": three numbered lines and a family-tree analogy card', "Lines spring in with a pop; the family-tree card slides in with parents and indented children",
    "Python reads from top to bottom. When a line ends with a colon, the lines below it, moved four spaces to the right, belong to it. Like a family tree: the children are drawn indented under their parent. Four spaces is the standard, and your editor will add them when you press the tab key."),
   ("Indentation", "`age.py`: a decision with an indented line; faint guide lines show the indent",
    "[HL 1] First a name, age, holding seventeen. [HL 2] This line asks a question: is age greater than or equal to eighteen? It ends with a colon. [HL 3] This line is moved four spaces to the right. That says, I belong to the if. It only runs if the answer is yes."),
   ("The two rooms", "Two coloured rooms: the if room and the else room; a door arrow between them",
    "Two rooms pop in side by side; a yes-arrow lights the if room and a no-arrow lights the else room; only one room glows at a time",
    "Think of two rooms. The if room runs when the answer is yes. The else room runs when it is no. Only one room is entered. After that, we step back out to the left, and the program carries on. Just remember: the colon opens a room, and the indent shows who lives inside.", CS),
   ("Follow the path", "`age.py` again with the path highlighted and the output panel on the right",
    "[TRACK age=17] [HL 2] Seventeen is not greater than or equal to eighteen. So the answer is no. [HL 4] Python skips the if room and goes to else. [HL 5] Not yet appears. [HL 6] This last line is not indented, so it is outside both rooms, and it always runs. Done. Predict first: what changes if age is twenty? You can vote, then Done."),
   ("Run it", "Terminal: `python age.py`",
    "Run it. Not yet. Done. Change age to twenty and run again. Now you see, you can vote, and then, done."),
   ("Bug of the Day", "BUG OF THE DAY: else indented two spaces",
    "Bug of the Day. We put else two spaces in, instead of lining it up with if. Python says, indentation error, unindent does not match any outer indentation level. The fix: line else up exactly under if."),
   ("Python programmers are never lost. They just have a bad indent of direction.", "Python programmers are never lost. They just have a bad indent of direction."),
   ("Task card: Eligible or Too young; test with 16, 18 and 20", "Your challenge: change the program so it prints Eligible for age eighteen or more, and Too young otherwise. Test it with sixteen, eighteen and twenty."),
   ("Next: EP 04 · Comments and reading a traceback", "Next: comments, and how to read an error message. Keep coding, says Xecxec!")),
 bug=dict(file="age.py", intro="else is indented two spaces, if is at the left edge", wrong=EP3_BUG, fix_intro="else lined up under if", fixed=EP3_FIX, expect=["IndentationError: unindent does not match any outer indentation level"],
   why="Python uses indentation to decide which lines belong together, so else must line up exactly under its if."),
 pun="\"Python programmers are never lost. They just have a bad indent of direction.\"",
 challenge="Change the program so it prints Eligible for age 18 or more and Too young otherwise. Test with 16, 18 and 20.",
 answer="Use if age >= 18 with print Eligible, and else with print Too young; 16 gives Too young, 18 and 20 give Eligible.",
 answer_code='''age = 16
if age >= 18:
    print("Eligible")
else:
    print("Too young")''',
 shorts=[
  dict(id="S1", title="Spaces are code", built=[2], hook="In Python, spaces matter.", script="In Python, spaces matter. Python uses indentation to know which lines belong together. Four spaces is the standard.", on="SPACES ARE CODE", caption="Indentation in 30 seconds.", tags=["python", "indentation", "beginners", "kodingkonkani", "coding"]),
  dict(id="S2", title="The two rooms", built=[4], hook="If room, else room.", script="If room, else room. The colon opens a room, and the indent shows who lives inside. Only one room runs. Then Python steps back out and carries on.", on="IF ROOM + ELSE ROOM", caption="Two rooms, one runs.", tags=["python", "ifelse", "coding", "kodingkonkani", "learntocode"]),
  dict(id="S3", title="Follow the path", built=[5], hook="Which line prints?", script="Which line prints? With age seventeen, the answer is no, so else runs. The last line is not indented, so it always runs.", on="WHICH LINE PRINTS?", caption="Trace the path.", tags=["python", "trace", "learntocode", "kodingkonkani", "coding"]),
  dict(id="S4", title="IndentationError", built=[8], hook="Two spaces too few.", script="Two spaces too few. Put else in the wrong place and Python says, unindent does not match any outer indentation level. Line it up under if.", on="INDENTATIONERROR", caption="Line them up.", tags=["python", "bugfix", "indentationerror", "kodingkonkani", "coding"]),
  dict(id="S5", title="Pun and challenge", built=[9, 10], hook="A bad indent of direction.", script="A bad indent of direction. Python programmers are never lost, they just have one. Your challenge: print Eligible or Too young, and test with sixteen, eighteen and twenty. Full video: EP 3.", on="ELIGIBLE OR TOO YOUNG?", caption="Try it.", tags=["python", "challenge", "kodingkonkani", "programmingjokes", "goa"]),
 ])

EP4_CODE = '''# Xecxec counts the beach shacks
shacks = 12
open_shacks = 9
print("Shacks:", shacks)
print("Open:", open_shacks)
print("Closed:", shacks - open_shacks)'''
EP4_BUG = '''shacks = 12
print("Shacks:", shack)'''
EP4_FIX = '''shacks = 12
print("Shacks:", shacks)'''

EP4 = dict(ep=4, title="Comments and reading a traceback", prereq="EP 03", **MOD,
 goals=["write a comment with #", "read a traceback from the bottom up", "fix a NameError caused by a typo"],
 yt=dict(title="Comments and How to Read Python Errors | Python Programming EP 04",
   desc="Learn to write comments and to read a Python traceback without panic, with Xecxec.",
   tags=["python comments", "python traceback", "nameerror", "python for beginners", "koding konkani", "python tutorial", "class 11 computer science", "coding in goa", "learn python", "python errors"],
   thumb_text="READ THE ERROR", thumb_visual="in tomato on peach; Xecxec holding a magnifying glass over a traceback with the last line circled; thin black border and drop shadow.",
   chapters={1: "Intro", 2: "Comments", 3: "A small program", 4: "Names as tags", 5: "Reading the output", 6: "Run it", 7: "Recap", 8: "Bug of the Day", 10: "Challenge", 11: "Next module"}),
 files=[dict(name="shacks.py", source=EP4_CODE, scene="3, 5")],
 scenes=std_scenes((4, "READ THE ERROR"),
   "Today, two small skills that you will use every single day: writing comments, and reading error messages without panic.",
   ("Comments", '"Comments": three numbered lines and a sticky-notes analogy card', "Lines spring in with a pop; the sticky-notes card slides in with a recipe book and yellow notes",
    "A comment is a sticky note in your code. It starts with a hash sign. Python ignores it completely, but the next human reads it, and that human might be you, next month. Good comments say why you did something. The code already shows what it does."),
   ("A small program", "`shacks.py`: a comment and two names; the comment line glows",
    "[HL 1] This line starts with a hash, so it is a comment. Python skips it. [HL 2] Twelve shacks. [HL 3] Nine are open. Notice the name, open underscore shacks. Names can have underscores but no spaces. [HL 4] Print the label and the total. [HL 5] Print how many are open. [HL 6] And closed is shacks minus open shacks, which is three."),
   ("Names as tags", "Two name tags, shacks and open_shacks, tied by arrows to the values 12 and 9",
    "Two tags pop in with their arrows to the values; when Python reads a name, the arrow glows and the value lights up",
    "In Python, a name is like a tag tied to a value. Shacks is a tag on twelve. Open underscore shacks is a tag on nine. When you write shacks, Python follows the tag to find the value. Remember this picture. It will explain a lot of puzzles later.", MB),
   ("Reading the output", "`shacks.py` again with the output panel on the right",
    "[HL 6] [TRACK shacks=12] [TRACK open_shacks=9] Python follows both tags, twelve and nine, subtracts, and prints three. Comments explain why you did something. Predict first: what would closed print if only five shacks were open? Seven. Always predict before you run."),
   ("Run it", "Terminal: `python shacks.py`",
    "Run it. Shacks, twelve. Open, nine. Closed, three. The comment never shows up in the output, because Python skipped it."),
   ("Bug of the Day", "BUG OF THE DAY: a typo in a name",
    "Bug of the Day. Read a traceback from the bottom. The last line says it all: name error, shack is not defined. Did you mean shacks? The line above shows where it happened: line two. We typed shack, but our tag is called shacks. Fix the spelling, and it works."),
   ("I put a comment on my code that said: this works. The traceback disagreed.", "I put a comment on my code that said: this works. The traceback disagreed."),
   ("Task card: a comment, boys and girls, print the total", "Your challenge: write a program with a comment, two names called boys and girls, and print the total."),
   ("Next: Module 1 · Variables, types and input", "Module zero is done! Next: variables and names in depth. Keep coding, says Xecxec!")),
 bug=dict(file="shacks.py", intro="shack is typed instead of shacks", wrong=EP4_BUG, fix_intro="spelling fixed", fixed=EP4_FIX, expect=["NameError: name 'shack' is not defined", "Did you mean: 'shacks'?"],
   why="Read a traceback from the bottom: the last line names the error and often suggests the fix, and the line above it shows where it happened."),
 pun="\"I put a comment on my code that said: this works. The traceback disagreed.\"",
 challenge="Write a program with a comment, two names (boys and girls) and print the total.",
 answer="Use boys = 20 and girls = 18, then print Total with boys + girls, which gives 38.",
 answer_code='''# Total students in my class
boys = 20
girls = 18
print("Total:", boys + girls)''',
 shorts=[
  dict(id="S1", title="Sticky notes for code", built=[2], hook="The line Python ignores.", script="The line Python ignores. A hash makes a comment. Python skips it, but humans read it. Explain why, not what.", on="# COMMENTS", caption="Comment your code.", tags=["python", "comments", "beginners", "kodingkonkani", "coding"]),
  dict(id="S2", title="Names are tags", built=[4], hook="A name is a tag on a value.", script="A name is a tag on a value. Shacks is a tag on twelve. When you write shacks, Python follows the tag to find the value.", on="NAMES ARE TAGS", caption="Names as tags.", tags=["python", "variables", "coding", "kodingkonkani", "learntocode"]),
  dict(id="S3", title="Underscores in names", built=[3], hook="open_shacks, not open shacks.", script="open underscore shacks, not open shacks. Names can have underscores, but never spaces. Pick names that say what they hold.", on="OPEN_SHACKS", caption="Name things well.", tags=["python", "naming", "learntocode", "kodingkonkani", "coding"]),
  dict(id="S4", title="Read a traceback", built=[8], hook="Start at the bottom.", script="Start at the bottom. The last line names the error. The line above says where. Python often suggests the fix, so read it.", on="READ FROM THE BOTTOM", caption="Bottom first.", tags=["python", "traceback", "nameerror", "kodingkonkani", "bugfix"]),
  dict(id="S5", title="Pun and challenge", built=[9, 10], hook="A comment that lied.", script="A comment that lied. I wrote, this works, and the traceback disagreed. Your challenge: boys plus girls, print the total. Full video: EP 4.", on="BOYS + GIRLS = ?", caption="Try it.", tags=["python", "challenge", "kodingkonkani", "programmingjokes", "goa"]),
 ])

EPS = [EP1, EP2, EP3, EP4]

RECAP = {
 1: ("Recap: four ideas on one card", "Let us recap. One: Python reads your file from top to bottom. Two: print shows text on the screen, and the text goes in quotes. Three: every opening quote needs a closing quote. And remember the journey: your file goes to Python, and the answer appears on the screen. Pause the video, and say those ideas out loud, once, slowly."),
 2: ("Recap: four steps on one card", "Recap time. One: you need Python, an editor and a terminal. Two: check Python with python, dash dash version. Three: save your code in a file that ends in dot py. Four: run it with python, a space, and the file name. If any step fails, do not panic. Read the message, check the spelling, and try again. Every programmer does this, every single day."),
 3: ("Recap: four ideas on one card", "Recap. One: Python reads top to bottom. Two: a colon opens a room, and the lines moved four spaces to the right live inside it. Three: only one of if and else runs, and then Python steps back out. Four: if the indent is wrong, you get an indentation error. Say these four ideas out loud. That is a lot already. Well done."),
 4: ("Recap: four rules on one card", "Recap. One: a comment starts with a hash, and Python ignores it. Two: a name is a tag tied to a value. Three: read a traceback from the bottom. Four: the last line names the error, and often suggests the fix. Say these four rules out loud, and you can handle most beginner errors. Try it on the shacks program, line by line."),
}
for _e in EPS:
    on, narr = RECAP[_e["ep"]]
    _e["scenes"].insert(6, dict(tpl=CS, name="Recap", on=on, anim="Four recap lines tick in one by one with a pop; Xecxec nods after each tick", narr=narr, min=30))

# scenes using Code explain must have a code file mapped to them; otherwise use Concept slide
for _e in EPS:
    _mapped = set()
    for _f in _e["files"]:
        _mapped |= {int(x) for x in re.findall(r"\d+", _f.get("scene", ""))}
    for _i, _s in enumerate(_e["scenes"], 1):
        if _s["tpl"] == CE and _i not in _mapped:
            _s["tpl"] = CS
            _s["anim"] = "Three tabs (Windows, Mac, Linux) switch with a pop; the active steps tick in one by one" if "Install" in _s["name"] else "Lines spring in one by one with a pop; the explanation card slides in from the right"
