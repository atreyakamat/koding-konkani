# Module 0 — Welcome & setup

Episodes 1–4 · Peach + Tomato · Python 3.13

## EP 01 — Hello, Python!

**Module 0 · Welcome & setup · 5:08 · Peach + Tomato · Prerequisite: none**

**Learning goals:** write and run a first Python program; use print() to show text on the screen; know that text goes inside quotes.

### YouTube

- **Title:** Hello, Python! Your First Program | Python Programming EP 01
- **Description:** Write and run your very first Python program with Xecxec the crab. No experience needed, just bring curiosity. 0:00 Intro · 0:20 What is Python? · 1:00 print line by line · 1:40 How Python runs your file · 2:10 Run it in your head · 2:50 Run it · 3:10 Recap · 3:45 Bug of the Day · 4:33 Challenge · 4:53 Next episode
- **Tags:** python, python for beginners, python tutorial, hello world python, print function, koding konkani, learn programming, class 11 computer science, first year engineering, coding in goa
- **Thumbnail:** big text "HELLO, PYTHON!" in tomato on peach; Xecxec waving a claw at a dark-blue terminal card showing Hello, Goa!; thin black border and drop shadow.

### Scene list

| # | Start | Length | Template | On screen | Animation & SFX |
| --- | --- | --- | --- | --- | --- |
| 1 | 0:00 | 0:20 | Title card | EP 01 · HELLO, PYTHON! | Tomato title card: EP sticker thuds in, title stamps with a whoosh, Xecxec scuttles in and waves; thud, whoosh, claw-click, sting |
| 2 | 0:20 | 0:40 | Concept slide | "What is Python?": three numbered lines and a fish-curry recipe card on the right | Lines spring in one by one with a pop; the recipe card slides in from the right |
| 3 | 1:00 | 0:40 | Code explain | `hello.py`: the 2-line first program, line 1 is the star | Code types in with key-tick; butter [HL n] highlight sweeps line by line with marker-swipe; explanation card on the right |
| 4 | 1:40 | 0:30 | Concept slide | Three boxes: your file, Python, the screen; arrows between them | Three boxes appear left to right; arrows draw on between them with a whoosh; the screen box lights up when text arrives |
| 5 | 2:10 | 0:40 | Code explain | `hello.py` again, with the output panel on the right | Same code; the output panel fills line by line with a ding per output line; [TRACK] cards update |
| 6 | 2:50 | 0:20 | Terminal | Terminal: `python hello.py` | Dark-blue terminal: the command types with key-tick, output prints in mint with a ding |
| 7 | 3:10 | 0:35 | Concept slide | Recap: four ideas on one card | Four recap lines tick in one by one with a pop; Xecxec nods after each tick |
| 8 | 3:45 | 0:40 | Bug of the Day | BUG OF THE DAY: a missing closing quote | Butter banner drops in with a buzzer; wrong code shakes; the Python error lines appear in tomato; the fix slides in and the terminal turns mint with a ding |
| 9 | 4:25 | 0:08 | Pun card | I would tell you a Python joke, but I forgot to close the quote. | Full tomato screen, card flips in with a rimshot, Xecxec snaps his claw |
| 10 | 4:33 | 0:20 | Challenge | Task card: print your name, then your favourite beach | Task card pops in; checklist ticks with a pop; Xecxec holds a tiny pen |
| 11 | 4:53 | 0:15 | Outro | Next: EP 02 · Installing Python and running scripts | Next-episode card slides up with a whoosh; right side stays empty for end-screen elements; sign-off text types in |

### Narration script

**[1 · Title]** Welcome to Koding Konkani! I am your narrator, and this little crab is Xecxec. In this series you will learn Python from zero. Today, we write our very first program.

**[2 · What is Python]** Python is a programming language. You write instructions in plain text, and Python reads them from top to bottom and does what they say. Think of a recipe card for fish curry. The card is your code, and Python is the cook who follows it, step by step. Python is popular because its words look almost like English, so beginners can read it from day one.

**[3 · print line by line]** [HL 1] This is the whole first program. The word print is a function. It shows something on the screen. The round brackets hold what to show. The quotes mean, this is text. Hello, Goa is the text. [HL 2] A second line prints the sign-off. Python runs line one, then line two, always in order.

**[4 · How Python runs your file]** Here is the journey. Your file goes to Python. Python reads line one, runs it, then reads line two, runs it. The text appears on the screen. There is no separate building step. Python reads and runs at the same time. That is why a mistake shows up the moment Python reaches that line.

**[5 · Run it in your head]** [HL 1] When this line runs, Hello, Goa appears. [HL 2] Then the next line prints underneath. Each print starts on a fresh line on its own. Change the words inside the quotes and the output changes too. Try your own name. Before you run it, predict the output. Two lines. The second says, Keep coding, says Xecxec. Predicting before running is the habit that makes you fast.

**[6 · Run it]** Save the file as hello dot py. In the terminal, type python, space, hello dot py. There it is. Our first program. On some Macs and Linux machines, the command is python three.

**[7 · Recap]** Let us recap. One: Python reads your file from top to bottom. Two: print shows text on the screen, and the text goes in quotes. Three: every opening quote needs a closing quote. And remember the journey: your file goes to Python, and the answer appears on the screen. Pause the video, and say those ideas out loud, once, slowly.

**[8 · Bug of the Day]** Bug of the Day. We forgot the closing quote. Python says, syntax error, unterminated string literal. It even shows an arrow under where the text starts. Add the quote, and it runs. Whenever you see unterminated, count your quotes.

**[9 · Pun]** I would tell you a Python joke, but I forgot to close the quote.

**[10 · Challenge]** Your challenge: print your name on one line, and your favourite beach on the next. Comment your answer below.

**[11 · Outro]** Next time: installing Python and running scripts properly. Keep coding, says Xecxec!

### Code shown

File 1: `hello.py` (scene 3, 5)

```python
print("Hello, Goa!")
print("Keep coding, says Xecxec!")
```

**Expected output:**

```text
Hello, Goa!
Keep coding, says Xecxec!
```

### Bug of the Day

Wrong code (the closing quote is missing):

```python
print("Hello, Goa!)
```

Python output:

```text
File "hello.py", line 1
    print("Hello, Goa!)
          ^
SyntaxError: unterminated string literal (detected at line 1)
```

Fixed code (closing quote added):

```python
print("Hello, Goa!")
```

**Why:** Every opening quote needs a closing quote of the same kind, otherwise Python cannot tell where the text ends.

### Pun & challenge

- **Pun:** "I would tell you a Python joke, but I forgot to close the quote."
- **Challenge:** Print your name on one line and your favourite beach on the next.
- **Challenge answer:** Use two print lines, for example Atreya, then Palolem.

### Shorts for EP 01

**S1 · The smallest Python program** — 0:20 · built from scene 3

- **Hook (first 1.5s):** "One line is a whole program."
- **Script:** One line is a whole program. Print, brackets, quotes. That is a working Python program. Everything you learn next is built on it.
- **On-screen text:** THE SMALLEST PYTHON PROGRAM
- **Caption + hashtags:** Your first Python line. #python #learntocode #kodingkonkani #beginners #goa

**S2 · Python reads top to bottom** — 0:20 · built from scene 4

- **Hook (first 1.5s):** "Line one, then line two."
- **Script:** Line one, then line two. Python reads your file from top to bottom and runs each line in order. No waiting, and no separate build step.
- **On-screen text:** PYTHON READS TOP TO BOTTOM
- **Caption + hashtags:** How Python runs your code. #python #interpreter #programming #kodingkonkani #coding

**S3 · What does print do?** — 0:20 · built from scenes 3, 5

- **Hook (first 1.5s):** "A function with one job."
- **Script:** A function with one job. print shows text on the screen. Put words in quotes and they appear exactly as written. Each print starts on a fresh line.
- **On-screen text:** PRINT("TEXT")
- **Caption + hashtags:** print explained slowly. #python #print #helloworld #kodingkonkani #coding

**S4 · The missing quote** — 0:20 · built from scene 8

- **Hook (first 1.5s):** "One missing character, one angry Python."
- **Script:** One missing character, one angry Python. Forget the closing quote and Python says, unterminated string literal. Count your quotes.
- **On-screen text:** UNTERMINATED STRING LITERAL
- **Caption + hashtags:** Quotes come in pairs. #python #bugfix #syntaxerror #kodingkonkani #coding

**S5 · Pun and challenge** — 0:20 · built from scenes 9, 10

- **Hook (first 1.5s):** "Python jokes need closing quotes."
- **Script:** Python jokes need closing quotes. I would tell you one, but I forgot to close the quote. Your challenge: print your name, then your favourite beach. Full video: EP 1.
- **On-screen text:** PRINT YOUR NAME + YOUR BEACH
- **Caption + hashtags:** Try the challenge. #python #codingchallenge #kodingkonkani #programmingjokes #goa

## EP 02 — Installing Python and running scripts

**Module 0 · Welcome & setup · 5:19 · Peach + Tomato · Prerequisite: EP 01**

**Learning goals:** install Python and check it with python --version; tell the REPL from a script file; run a script with python file.py.

### YouTube

- **Title:** Install Python and Run Your First Script | Python Programming EP 02
- **Description:** Set up Python and VS Code on Windows, Mac or Linux, then run scripts with Xecxec. 0:00 Intro · 0:20 What you need · 1:00 Install and check · 1:40 REPL versus script · 2:15 A script with numbers · 2:55 Run it · 3:15 Recap · 3:55 Bug of the Day · 4:44 Challenge · 5:04 Next episode
- **Tags:** install python, python setup, vs code python, run python script, python for beginners, koding konkani, python tutorial, class 11 computer science, coding in goa, learn python
- **Thumbnail:** big text "SET UP PYTHON" in tomato on peach; Xecxec raising both claws beside a terminal showing python --version; thin black border and drop shadow.

### Scene list

| # | Start | Length | Template | On screen | Animation & SFX |
| --- | --- | --- | --- | --- | --- |
| 1 | 0:00 | 0:20 | Title card | EP 02 · SET UP PYTHON | Tomato title card: EP sticker thuds in, title stamps with a whoosh, Xecxec scuttles in and waves; thud, whoosh, claw-click, sting |
| 2 | 0:20 | 0:40 | Concept slide | "What you need": three numbered lines and a kitchen analogy card | Lines spring in one by one with a pop; the kitchen card slides in with a chopping board, a stove and a chef |
| 3 | 1:00 | 0:40 | Concept slide | Install steps for Windows, Mac and Linux, shown as three tabs | Three tabs (Windows, Mac, Linux) switch with a pop; the active steps tick in one by one |
| 4 | 1:40 | 0:35 | Concept slide | Two boxes: the REPL, one line and an answer at once; a script, many lines in a saved .py file | Two boxes pop in side by side; in the left box a line types and its answer appears at once; in the right box a saved file runs top to bottom |
| 5 | 2:15 | 0:40 | Code explain | `fish.py`: two names, a label and a total | Same code; the output panel fills line by line with a ding per output line; [TRACK] cards update |
| 6 | 2:55 | 0:20 | Terminal | Terminal: `python fish.py` | Dark-blue terminal: the command types with key-tick, output prints in mint with a ding |
| 7 | 3:15 | 0:40 | Concept slide | Recap: four steps on one card | Four recap lines tick in one by one with a pop; Xecxec nods after each tick |
| 8 | 3:55 | 0:40 | Bug of the Day | BUG OF THE DAY: print with a capital P | Butter banner drops in with a buzzer; wrong code shakes; the Python error lines appear in tomato; the fix slides in and the terminal turns mint with a ding |
| 9 | 4:35 | 0:09 | Pun card | Why did the snake get lost in the folder? It kept running the wrong dot py. | Full tomato screen, card flips in with a rimshot, Xecxec snaps his claw |
| 10 | 4:44 | 0:20 | Challenge | Task card: install, check the version, run fish.py, change the price | Task card pops in; checklist ticks with a pop; Xecxec holds a tiny pen |
| 11 | 5:04 | 0:15 | Outro | Next: EP 03 · How Python reads your code | Next-episode card slides up with a whoosh; right side stays empty for end-screen elements; sign-off text types in |

### Narration script

**[1 · Title]** Welcome back! Last time we ran one program. Today we set up your computer so you can run your own. It takes about ten minutes, and you only do it once.

**[2 · What you need]** You need three things. Python itself. An editor, where you type, like VS Code. And a terminal, where you give commands. Think of a kitchen. Python is the stove, the editor is the chopping board, and the terminal is you, giving the orders. Do not worry if the names sound strange. By the end of today, you will have typed every one of these commands yourself.

**[3 · Install and check]** Go to python dot org, open Downloads, and install the latest version. On Windows, tick the box that says, add Python to PATH. On a Mac, run the installer. On Linux, Python is usually already there. Then open a terminal and type python, space, dash dash version. If a number appears, you are ready. On some Macs and Linux machines, the command is python three.

**[4 · REPL versus script]** Python has two ways to run code. In the REPL, you type one line and get the answer at once. It is great for tiny tests. In a script, you save many lines in a file that ends in dot py, and run the whole file. We will mostly use scripts, because you can keep them, fix them, and run them again.

**[5 · A script with numbers]** [HL 1] [TRACK fish=3] Make a name called fish, and put three in it. [HL 2] [TRACK price=120] A name called price, one hundred twenty. [HL 3] Print a label, then the value. Print puts a space between the things for you. [HL 4] And Python does the maths: fish times price. Three times one hundred twenty is three hundred sixty.

**[6 · Run it]** Save the file as fish dot py. In the terminal, type python, space, fish dot py. Fish, three. Total, three hundred sixty. Always check that you are in the same folder as the file.

**[7 · Recap]** Recap time. One: you need Python, an editor and a terminal. Two: check Python with python, dash dash version. Three: save your code in a file that ends in dot py. Four: run it with python, a space, and the file name. If any step fails, do not panic. Read the message, check the spelling, and try again. Every programmer does this, every single day.

**[8 · Bug of the Day]** Bug of the Day. We wrote print with a capital P. Python says, name error, Print is not defined. And it even asks, did you mean print, with a small p? Python is case sensitive. Capital P and small p are different names. Fix the letter, and it works.

**[9 · Pun]** Why did the snake get lost in the folder? It kept running the wrong dot py.

**[10 · Challenge]** Your challenge: install Python, check the version, and run fish dot py. Then change the price and run it again.

**[11 · Outro]** Next: how Python reads your code. Keep coding, says Xecxec!

### Code shown

File 1: `fish.py` (scene 5)

```python
fish = 3
price = 120
print("Fish:", fish)
print("Total:", fish * price)
```

**Expected output:**

```text
Fish: 3
Total: 360
```

### Bug of the Day

Wrong code (print is spelled with a capital P):

```python
fish = 3
Print("Fish:", fish)
```

Python output:

```text
Traceback (most recent call last):
  File "fish.py", line 2, in <module>
    Print("Fish:", fish)
    ^^^^^
NameError: name 'Print' is not defined. Did you mean: 'print'?
```

Fixed code (small p):

```python
fish = 3
print("Fish:", fish)
```

**Why:** Python treats upper and lower case as different letters, so Print and print are two different names.

### Pun & challenge

- **Pun:** "Why did the snake get lost in the folder? It kept running the wrong .py."
- **Challenge:** Install Python, check the version, run fish.py, then change the price and run it again.
- **Challenge answer:** Change price = 120 to price = 150 and run again: the total becomes 450.

### Shorts for EP 02

**S1 · What you need for Python** — 0:20 · built from scene 2

- **Hook (first 1.5s):** "Three tools, ten minutes."
- **Script:** Three tools, ten minutes. Python, an editor and a terminal. Python is the stove, VS Code is the chopping board, and the terminal is you, giving the orders.
- **On-screen text:** 3 TOOLS FOR PYTHON
- **Caption + hashtags:** Set up Python in three steps. #python #setup #beginners #kodingkonkani #goa

**S2 · Check your install** — 0:20 · built from scene 3

- **Hook (first 1.5s):** "Is Python really installed?"
- **Script:** Is Python really installed? Open the terminal and type python, dash dash version. A number means you are ready. On some machines, the command is python three.
- **On-screen text:** PYTHON --VERSION
- **Caption + hashtags:** One command to check. #python #terminal #setup #kodingkonkani #learntocode

**S3 · REPL versus script** — 0:20 · built from scene 4

- **Hook (first 1.5s):** "Two ways to run Python."
- **Script:** Two ways to run Python. The REPL runs one line at a time, great for tiny tests. A script is a saved dot py file that runs from top to bottom. Use scripts for real programs.
- **On-screen text:** REPL OR SCRIPT?
- **Caption + hashtags:** REPL or script? #python #repl #script #kodingkonkani #coding

**S4 · Print is not defined** — 0:20 · built from scene 8

- **Hook (first 1.5s):** "One capital letter breaks everything."
- **Script:** One capital letter breaks everything. Write Print with a capital P and Python says, name error, Print is not defined. Python is case sensitive, so use a small p.
- **On-screen text:** NAMEERROR: PRINT IS NOT DEFINED
- **Caption + hashtags:** Python is case sensitive. #python #bugfix #nameerror #kodingkonkani #coding

**S5 · Pun and challenge** — 0:20 · built from scenes 9, 10

- **Hook (first 1.5s):** "A snake lost in a folder."
- **Script:** A snake lost in a folder. Why? It kept running the wrong dot py. Your challenge: run fish dot py, change the price, and run it again. Full video: EP 2.
- **On-screen text:** RUN FISH.PY + CHANGE THE PRICE
- **Caption + hashtags:** Do the challenge. #python #codingchallenge #kodingkonkani #programmingjokes #goa

## EP 03 — How Python reads your code

**Module 0 · Welcome & setup · 5:03 · Peach + Tomato · Prerequisite: EP 02**

**Learning goals:** explain that Python runs lines in order, top to bottom; see that indentation is part of the code; write a first if and else with a correct indent.

### YouTube

- **Title:** How Python Reads Your Code: Lines and Indentation | Python Programming EP 03
- **Description:** Learn why Python cares about spaces at the start of a line, with Xecxec. 0:00 Intro · 0:20 Top to bottom · 0:55 Indentation · 1:35 The two rooms · 2:05 Follow the path · 2:45 Run it · 3:05 Recap · 3:40 Bug of the Day · 4:28 Challenge · 4:48 Next episode
- **Tags:** python indentation, python syntax, if else python, python for beginners, koding konkani, python tutorial, class 11 computer science, coding in goa, learn python, indentationerror
- **Thumbnail:** big text "SPACES MATTER" in tomato on peach; Xecxec shaking his shell beside a code card with indent guide lines; thin black border and drop shadow.

### Scene list

| # | Start | Length | Template | On screen | Animation & SFX |
| --- | --- | --- | --- | --- | --- |
| 1 | 0:00 | 0:20 | Title card | EP 03 · SPACES MATTER | Tomato title card: EP sticker thuds in, title stamps with a whoosh, Xecxec scuttles in and waves; thud, whoosh, claw-click, sting |
| 2 | 0:20 | 0:35 | Concept slide | "Top to bottom": three numbered lines and a family-tree analogy card | Lines spring in with a pop; the family-tree card slides in with parents and indented children |
| 3 | 0:55 | 0:40 | Code explain | `age.py`: a decision with an indented line; faint guide lines show the indent | Code types in with key-tick; butter [HL n] highlight sweeps line by line with marker-swipe; explanation card on the right |
| 4 | 1:35 | 0:30 | Concept slide | Two coloured rooms: the if room and the else room; a door arrow between them | Two rooms pop in side by side; a yes-arrow lights the if room and a no-arrow lights the else room; only one room glows at a time |
| 5 | 2:05 | 0:40 | Code explain | `age.py` again with the path highlighted and the output panel on the right | Same code; the output panel fills line by line with a ding per output line; [TRACK] cards update |
| 6 | 2:45 | 0:20 | Terminal | Terminal: `python age.py` | Dark-blue terminal: the command types with key-tick, output prints in mint with a ding |
| 7 | 3:05 | 0:35 | Concept slide | Recap: four ideas on one card | Four recap lines tick in one by one with a pop; Xecxec nods after each tick |
| 8 | 3:40 | 0:40 | Bug of the Day | BUG OF THE DAY: else indented two spaces | Butter banner drops in with a buzzer; wrong code shakes; the Python error lines appear in tomato; the fix slides in and the terminal turns mint with a ding |
| 9 | 4:20 | 0:08 | Pun card | Python programmers are never lost. They just have a bad indent of direction. | Full tomato screen, card flips in with a rimshot, Xecxec snaps his claw |
| 10 | 4:28 | 0:20 | Challenge | Task card: Eligible or Too young; test with 16, 18 and 20 | Task card pops in; checklist ticks with a pop; Xecxec holds a tiny pen |
| 11 | 4:48 | 0:15 | Outro | Next: EP 04 · Comments and reading a traceback | Next-episode card slides up with a whoosh; right side stays empty for end-screen elements; sign-off text types in |

### Narration script

**[1 · Title]** Today we learn why Python cares about spaces at the start of a line. In many languages they are decoration. In Python, they are part of the code.

**[2 · Top to bottom]** Python reads from top to bottom. When a line ends with a colon, the lines below it, moved four spaces to the right, belong to it. Like a family tree: the children are drawn indented under their parent. Four spaces is the standard, and your editor will add them when you press the tab key.

**[3 · Indentation]** [HL 1] First a name, age, holding seventeen. [HL 2] This line asks a question: is age greater than or equal to eighteen? It ends with a colon. [HL 3] This line is moved four spaces to the right. That says, I belong to the if. It only runs if the answer is yes.

**[4 · The two rooms]** Think of two rooms. The if room runs when the answer is yes. The else room runs when it is no. Only one room is entered. After that, we step back out to the left, and the program carries on. Just remember: the colon opens a room, and the indent shows who lives inside.

**[5 · Follow the path]** [TRACK age=17] [HL 2] Seventeen is not greater than or equal to eighteen. So the answer is no. [HL 4] Python skips the if room and goes to else. [HL 5] Not yet appears. [HL 6] This last line is not indented, so it is outside both rooms, and it always runs. Done. Predict first: what changes if age is twenty? You can vote, then Done.

**[6 · Run it]** Run it. Not yet. Done. Change age to twenty and run again. Now you see, you can vote, and then, done.

**[7 · Recap]** Recap. One: Python reads top to bottom. Two: a colon opens a room, and the lines moved four spaces to the right live inside it. Three: only one of if and else runs, and then Python steps back out. Four: if the indent is wrong, you get an indentation error. Say these four ideas out loud. That is a lot already. Well done.

**[8 · Bug of the Day]** Bug of the Day. We put else two spaces in, instead of lining it up with if. Python says, indentation error, unindent does not match any outer indentation level. The fix: line else up exactly under if.

**[9 · Pun]** Python programmers are never lost. They just have a bad indent of direction.

**[10 · Challenge]** Your challenge: change the program so it prints Eligible for age eighteen or more, and Too young otherwise. Test it with sixteen, eighteen and twenty.

**[11 · Outro]** Next: comments, and how to read an error message. Keep coding, says Xecxec!

### Code shown

File 1: `age.py` (scene 3, 5)

```python
age = 17
if age >= 18:
    print("You can vote.")
else:
    print("Not yet.")
print("Done.")
```

**Expected output:**

```text
Not yet.
Done.
```

### Bug of the Day

Wrong code (else is indented two spaces, if is at the left edge):

```python
age = 17
if age >= 18:
    print("You can vote.")
  else:
    print("Not yet.")
```

Python output:

```text
File "age.py", line 4
    else:
         ^
IndentationError: unindent does not match any outer indentation level
```

Fixed code (else lined up under if):

```python
age = 17
if age >= 18:
    print("You can vote.")
else:
    print("Not yet.")
```

**Why:** Python uses indentation to decide which lines belong together, so else must line up exactly under its if.

### Pun & challenge

- **Pun:** "Python programmers are never lost. They just have a bad indent of direction."
- **Challenge:** Change the program so it prints Eligible for age 18 or more and Too young otherwise. Test with 16, 18 and 20.
- **Challenge answer:** Use if age >= 18 with print Eligible, and else with print Too young; 16 gives Too young, 18 and 20 give Eligible.

### Shorts for EP 03

**S1 · Spaces are code** — 0:20 · built from scene 2

- **Hook (first 1.5s):** "In Python, spaces matter."
- **Script:** In Python, spaces matter. Python uses indentation to know which lines belong together. Four spaces is the standard.
- **On-screen text:** SPACES ARE CODE
- **Caption + hashtags:** Indentation in 30 seconds. #python #indentation #beginners #kodingkonkani #coding

**S2 · The two rooms** — 0:20 · built from scene 4

- **Hook (first 1.5s):** "If room, else room."
- **Script:** If room, else room. The colon opens a room, and the indent shows who lives inside. Only one room runs. Then Python steps back out and carries on.
- **On-screen text:** IF ROOM + ELSE ROOM
- **Caption + hashtags:** Two rooms, one runs. #python #ifelse #coding #kodingkonkani #learntocode

**S3 · Follow the path** — 0:20 · built from scene 5

- **Hook (first 1.5s):** "Which line prints?"
- **Script:** Which line prints? With age seventeen, the answer is no, so else runs. The last line is not indented, so it always runs.
- **On-screen text:** WHICH LINE PRINTS?
- **Caption + hashtags:** Trace the path. #python #trace #learntocode #kodingkonkani #coding

**S4 · IndentationError** — 0:20 · built from scene 8

- **Hook (first 1.5s):** "Two spaces too few."
- **Script:** Two spaces too few. Put else in the wrong place and Python says, unindent does not match any outer indentation level. Line it up under if.
- **On-screen text:** INDENTATIONERROR
- **Caption + hashtags:** Line them up. #python #bugfix #indentationerror #kodingkonkani #coding

**S5 · Pun and challenge** — 0:20 · built from scenes 9, 10

- **Hook (first 1.5s):** "A bad indent of direction."
- **Script:** A bad indent of direction. Python programmers are never lost, they just have one. Your challenge: print Eligible or Too young, and test with sixteen, eighteen and twenty. Full video: EP 3.
- **On-screen text:** ELIGIBLE OR TOO YOUNG?
- **Caption + hashtags:** Try it. #python #challenge #kodingkonkani #programmingjokes #goa

## EP 04 — Comments and reading a traceback

**Module 0 · Welcome & setup · 4:53 · Peach + Tomato · Prerequisite: EP 03**

**Learning goals:** write a comment with #; read a traceback from the bottom up; fix a NameError caused by a typo.

### YouTube

- **Title:** Comments and How to Read Python Errors | Python Programming EP 04
- **Description:** Learn to write comments and to read a Python traceback without panic, with Xecxec. 0:00 Intro · 0:15 Comments · 0:45 A small program · 1:25 Names as tags · 1:55 Reading the output · 2:35 Run it · 2:55 Recap · 3:30 Bug of the Day · 4:18 Challenge · 4:38 Next module
- **Tags:** python comments, python traceback, nameerror, python for beginners, koding konkani, python tutorial, class 11 computer science, coding in goa, learn python, python errors
- **Thumbnail:** big text "READ THE ERROR" in tomato on peach; Xecxec holding a magnifying glass over a traceback with the last line circled; thin black border and drop shadow.

### Scene list

| # | Start | Length | Template | On screen | Animation & SFX |
| --- | --- | --- | --- | --- | --- |
| 1 | 0:00 | 0:15 | Title card | EP 04 · READ THE ERROR | Tomato title card: EP sticker thuds in, title stamps with a whoosh, Xecxec scuttles in and waves; thud, whoosh, claw-click, sting |
| 2 | 0:15 | 0:30 | Concept slide | "Comments": three numbered lines and a sticky-notes analogy card | Lines spring in with a pop; the sticky-notes card slides in with a recipe book and yellow notes |
| 3 | 0:45 | 0:40 | Code explain | `shacks.py`: a comment and two names; the comment line glows | Code types in with key-tick; butter [HL n] highlight sweeps line by line with marker-swipe; explanation card on the right |
| 4 | 1:25 | 0:30 | Memory boxes | Two name tags, shacks and open_shacks, tied by arrows to the values 12 and 9 | Two tags pop in with their arrows to the values; when Python reads a name, the arrow glows and the value lights up |
| 5 | 1:55 | 0:40 | Code explain | `shacks.py` again with the output panel on the right | Same code; the output panel fills line by line with a ding per output line; [TRACK] cards update |
| 6 | 2:35 | 0:20 | Terminal | Terminal: `python shacks.py` | Dark-blue terminal: the command types with key-tick, output prints in mint with a ding |
| 7 | 2:55 | 0:35 | Concept slide | Recap: four rules on one card | Four recap lines tick in one by one with a pop; Xecxec nods after each tick |
| 8 | 3:30 | 0:40 | Bug of the Day | BUG OF THE DAY: a typo in a name | Butter banner drops in with a buzzer; wrong code shakes; the Python error lines appear in tomato; the fix slides in and the terminal turns mint with a ding |
| 9 | 4:10 | 0:08 | Pun card | I put a comment on my code that said: this works. The traceback disagreed. | Full tomato screen, card flips in with a rimshot, Xecxec snaps his claw |
| 10 | 4:18 | 0:20 | Challenge | Task card: a comment, boys and girls, print the total | Task card pops in; checklist ticks with a pop; Xecxec holds a tiny pen |
| 11 | 4:38 | 0:15 | Outro | Next: Module 1 · Variables, types and input | Next-episode card slides up with a whoosh; right side stays empty for end-screen elements; sign-off text types in |

### Narration script

**[1 · Title]** Today, two small skills that you will use every single day: writing comments, and reading error messages without panic.

**[2 · Comments]** A comment is a sticky note in your code. It starts with a hash sign. Python ignores it completely, but the next human reads it, and that human might be you, next month. Good comments say why you did something. The code already shows what it does.

**[3 · A small program]** [HL 1] This line starts with a hash, so it is a comment. Python skips it. [HL 2] Twelve shacks. [HL 3] Nine are open. Notice the name, open underscore shacks. Names can have underscores but no spaces. [HL 4] Print the label and the total. [HL 5] Print how many are open. [HL 6] And closed is shacks minus open shacks, which is three.

**[4 · Names as tags]** In Python, a name is like a tag tied to a value. Shacks is a tag on twelve. Open underscore shacks is a tag on nine. When you write shacks, Python follows the tag to find the value. Remember this picture. It will explain a lot of puzzles later.

**[5 · Reading the output]** [HL 6] [TRACK shacks=12] [TRACK open_shacks=9] Python follows both tags, twelve and nine, subtracts, and prints three. Comments explain why you did something. Predict first: what would closed print if only five shacks were open? Seven. Always predict before you run.

**[6 · Run it]** Run it. Shacks, twelve. Open, nine. Closed, three. The comment never shows up in the output, because Python skipped it.

**[7 · Recap]** Recap. One: a comment starts with a hash, and Python ignores it. Two: a name is a tag tied to a value. Three: read a traceback from the bottom. Four: the last line names the error, and often suggests the fix. Say these four rules out loud, and you can handle most beginner errors. Try it on the shacks program, line by line.

**[8 · Bug of the Day]** Bug of the Day. Read a traceback from the bottom. The last line says it all: name error, shack is not defined. Did you mean shacks? The line above shows where it happened: line two. We typed shack, but our tag is called shacks. Fix the spelling, and it works.

**[9 · Pun]** I put a comment on my code that said: this works. The traceback disagreed.

**[10 · Challenge]** Your challenge: write a program with a comment, two names called boys and girls, and print the total.

**[11 · Outro]** Module zero is done! Next: variables and names in depth. Keep coding, says Xecxec!

### Code shown

File 1: `shacks.py` (scene 3, 5)

```python
# Xecxec counts the beach shacks
shacks = 12
open_shacks = 9
print("Shacks:", shacks)
print("Open:", open_shacks)
print("Closed:", shacks - open_shacks)
```

**Expected output:**

```text
Shacks: 12
Open: 9
Closed: 3
```

### Bug of the Day

Wrong code (shack is typed instead of shacks):

```python
shacks = 12
print("Shacks:", shack)
```

Python output:

```text
Traceback (most recent call last):
  File "shacks.py", line 2, in <module>
    print("Shacks:", shack)
                     ^^^^^
NameError: name 'shack' is not defined. Did you mean: 'shacks'?
```

Fixed code (spelling fixed):

```python
shacks = 12
print("Shacks:", shacks)
```

**Why:** Read a traceback from the bottom: the last line names the error and often suggests the fix, and the line above it shows where it happened.

### Pun & challenge

- **Pun:** "I put a comment on my code that said: this works. The traceback disagreed."
- **Challenge:** Write a program with a comment, two names (boys and girls) and print the total.
- **Challenge answer:** Use boys = 20 and girls = 18, then print Total with boys + girls, which gives 38.

### Shorts for EP 04

**S1 · Sticky notes for code** — 0:20 · built from scene 2

- **Hook (first 1.5s):** "The line Python ignores."
- **Script:** The line Python ignores. A hash makes a comment. Python skips it, but humans read it. Explain why, not what.
- **On-screen text:** # COMMENTS
- **Caption + hashtags:** Comment your code. #python #comments #beginners #kodingkonkani #coding

**S2 · Names are tags** — 0:20 · built from scene 4

- **Hook (first 1.5s):** "A name is a tag on a value."
- **Script:** A name is a tag on a value. Shacks is a tag on twelve. When you write shacks, Python follows the tag to find the value.
- **On-screen text:** NAMES ARE TAGS
- **Caption + hashtags:** Names as tags. #python #variables #coding #kodingkonkani #learntocode

**S3 · Underscores in names** — 0:20 · built from scene 3

- **Hook (first 1.5s):** "open_shacks, not open shacks."
- **Script:** open underscore shacks, not open shacks. Names can have underscores, but never spaces. Pick names that say what they hold.
- **On-screen text:** OPEN_SHACKS
- **Caption + hashtags:** Name things well. #python #naming #learntocode #kodingkonkani #coding

**S4 · Read a traceback** — 0:20 · built from scene 8

- **Hook (first 1.5s):** "Start at the bottom."
- **Script:** Start at the bottom. The last line names the error. The line above says where. Python often suggests the fix, so read it.
- **On-screen text:** READ FROM THE BOTTOM
- **Caption + hashtags:** Bottom first. #python #traceback #nameerror #kodingkonkani #bugfix

**S5 · Pun and challenge** — 0:20 · built from scenes 9, 10

- **Hook (first 1.5s):** "A comment that lied."
- **Script:** A comment that lied. I wrote, this works, and the traceback disagreed. Your challenge: boys plus girls, print the total. Full video: EP 4.
- **On-screen text:** BOYS + GIRLS = ?
- **Caption + hashtags:** Try it. #python #challenge #kodingkonkani #programmingjokes #goa
