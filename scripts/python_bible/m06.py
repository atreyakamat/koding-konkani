"""Module 6 — Files, exceptions, modules, pip, venv (EP 51-60)."""

MODULE = {"id": 6, "name": "Files, exceptions, modules, pip, venv", "range": "51–60", "colours": "Peach + DarkBlue"}
EPISODES = []
NEXT_AFTER = ("Next: EP 61 · Why classes?", "Module six is done! Next time: why we need classes, and how they keep our data tidy.")

NOTES = {"notes.txt": "Baga\nColva\nAnjuna\n"}
FILEFLOW = "Arrows run from the program box to a file box and back; a lock icon appears while the file is open and clears when it is closed"

EPISODES.append(dict(
    n=51, title="Reading files", spoken="reading files",
    yt="Python Reading Files: open, read, readlines", thumb="READ A FILE",
    vis="Xecxec opening a folder and reading a paper labelled notes.txt",
    goals=["open a text file and read it", "loop over the lines of a file", "close the file when done"],
    tags=["python read file", "python open function", "python readlines", "filenotfounderror"],
    hash=["#files", "#readfile"],
    analogy="a library book: you open it, read it, and return it to the shelf when you are done",
    c_title="Programs and files",
    c_pts=["open(name) opens a file for reading", "read() gives all the text as one string", "close() returns the file to the system"],
    intro="So far our data vanished when the program ended. Today we read data from a file on disk.",
    concept="A file is a named piece of data on your disk. Open takes the file name, and gives you a file object. Read gives you all the text as one string. Think of a library book. You open it, read it, and return it when you are done. Calling close tells the system you have finished. You can also loop over a file, line by line. The file must be in the folder where the program runs, or you must give its path.",
    A=dict(file="readfile.py", label="Open, read, close", on="read all of notes.txt into one string",
           files=NOTES,
           src='''
f = open("notes.txt")
text = f.read()
f.close()
print(text)
print(len(text))
''',
           narr="[HL 1] Open the file by name. We get a file object, tied to f. [HL 2] Read gives all the text as one string. Three lines, with new line characters between them. [HL 3] Close the file. We have our text now. [HL 4] Print it. Baga, Colva, Anjuna. An extra blank line follows, because the last line ends with a new line, and print adds another. [HL 5] Eighteen characters in all, new lines included."),
    mem=dict(label="The file text is a string", on="The name text tied to one string containing the whole file", names=["text"], **{"from": "A"},
             narr="Here is the picture. Once the file is closed, only the string remains. The name text is tied to one string, holding all three lines and their new line characters. The file object f is finished. It was only a doorway to the disk. After read, all the data lives in the string, and we can use it like any other text."),
    B=dict(file="lines.py", label="Line by line", on="loop over a file; readlines gives a list",
           files=NOTES,
           src='''
f = open("notes.txt")
for line in f:
    print(line.strip())
f.close()
lines = open("notes.txt").readlines()
print(len(lines))
print(lines[0].strip())
''',
           narr="[HL 1] Open the file. [HL 2] A for loop over a file gives one line at a time. [HL 3] Each line still ends with a new line. Strip removes it, so the print is tidy. [HL 4] Close. [HL 5] Readlines gives a list with one string per line. [HL 6] Three lines. [HL 7] The first line, stripped. Baga."),
    term="Baga, Colva, Anjuna. Then three. Then Baga again.",
    recap=["open(name) gives a file object, and read() gives its text.", "A for loop over a file gives one line at a time.", "Lines end with a new line character, so use strip().", "Close the file when you are finished."],
    bug=dict(title="the file name is wrong", file="readfile.py", files=NOTES, wrong='''
f = open("note.txt")
print(f.read())
''', fixed='''
f = open("notes.txt")
print(f.read())
f.close()
''', wrong_note="note.txt is a typo", fixed_note="the real name notes.txt",
             why="Python can only open a file that exists in the folder it is running from, so a wrong name or a wrong folder gives a FileNotFoundError.",
             narr="Bug of the Day. We open note dot txt, but the file is called notes dot txt. Python says, file not found error, the system cannot find the file specified, and shows the exact name it tried. Check the spelling, and check that you are running the program from the folder that holds the file."),
    pun="Why did the file get promoted? It always knew how to open up.",
    task="read a file and count its lines", challenge="Read notes.txt and print how many lines it has.",
    answer="Use lines = open(\"notes.txt\").readlines() and print(len(lines)), which prints 3.",
    shorts=[
        ("Open and read", "To read a file, call open with its name. You get a file object. Call read on it, and you get all the text as one string. Then close the file. Think of a library book. You open it, read it, and return it. The file must be in the folder where your program runs, so check your folder first.", "OPEN · READ · CLOSE", "Reading a text file."),
        ("Line by line", "For big files, read one line at a time. A for loop over the file gives you each line in turn. Each line ends with a new line character, so call strip before you print it. Or call readlines, to get all the lines as a list. Both ways let you process a file without loading everything as one big string.", "FOR LINE IN F:", "One line at a time."),
        ("Strip the newline", "Why does print show a blank line after each file line? Each line ends with a new line character, and print adds another. The fix is strip. Line dot strip removes the new line, along with spaces at both ends. Use it whenever you read lines from a file, and your output will look just right.", "LINE.STRIP()", "Tidy the lines."),
        ("File not found", "The first file bug everyone meets. You open a file, and Python says, file not found error, no such file or directory. Check two things. Is the name spelled exactly right? And is your program running from the folder that holds the file? The error even shows the name Python tried. Compare it with your real file.", "FILENOTFOUNDERROR", "Check name and folder."),
        ("Pun and challenge", "Why did the file get promoted? It always knew how to open up. Your challenge. Make a text file called notes dot txt, with three lines of beach names. Write a program that opens it, reads the lines, and prints how many there are. You should see three. Then print each line in capital letters. Share your code in the comments.", "COUNT THE LINES", "Try reading a file."),
    ],
))

EPISODES.append(dict(
    n=52, title="Writing files", spoken="writing files",
    yt="Python Writing Files: w and a Modes", thumb="WRITE A FILE",
    vis="Xecxec writing a diary entry with a feather pen",
    goals=["write text to a file with mode w", "add to a file with mode a", "avoid wiping a file by accident"],
    tags=["python write file", "python append file", "python file modes", "w mode overwrites"],
    hash=["#files", "#writefile"],
    analogy="a diary: w means tear out all the pages and start fresh, a means add a new page at the end",
    c_title="Three modes",
    c_pts=["r reads (the default)", "w writes and wipes the old content", "a appends to the end"],
    intro="Reading is only half the story. Today we write data to a file, and learn which mode to pick.",
    concept="Open takes a second argument, the mode. R is read, the default. W is write. It creates the file if needed, and wipes whatever was there. A is append. It adds to the end and keeps what was there. Think of a diary. Write mode tears out all the pages and starts fresh. Append mode adds a new page at the end. Write puts text in with the write method. It does not add new lines for you.",
    A=dict(file="write.py", label="Write mode", on="write two lines, then read them back",
           src='''
f = open("log.txt", "w")
f.write("Day 1\\n")
f.write("Day 2\\n")
f.close()
print(open("log.txt").read())
''',
           narr="[HL 1] Open log dot txt in write mode. If the file is missing, Python creates it. [HL 2] Write a line. The slash n at the end is a new line character. Write does not add one for us. [HL 3] Another line. [HL 4] Close the file. This saves everything to disk. [HL 5] Read it back and print. Day one, Day two. The extra blank line is the final new line."),
    c2=dict(label="Write versus append", on="Two diaries: with w the old pages are torn out; with a a new page is added at the end", narr="Here is the difference, in pictures. A diary with three pages. Open it in write mode, and every old page is torn out, before you write a single word. Open it in append mode, and the old pages stay, and your new text goes after them. Write is for starting over. Append is for adding. Pick carefully.", anim="A diary with pages; w tears all pages out in a puff, a adds one new page at the end with a pop"),
    B=dict(file="append.py", label="Append mode", on="add a line without losing the old ones",
           files={"log.txt": "Day 1\nDay 2\n"},
           src='''
f = open("log.txt", "a")
f.write("Day 3\\n")
f.close()
print(open("log.txt").read().count("Day"))
''',
           narr="[HL 1] Open the existing log in append mode. [HL 2] Write one more line. It goes after the lines that are already there. [HL 3] Close. [HL 4] Read the file back, and count the word Day. Three. All three days are there. The earlier lines survived, because append never wipes."),
    term="Three.",
    recap=["Mode r reads, w writes and wipes, a appends.", "write() does not add a new line for you.", "Close the file so the data is saved.", "Use a to add to a file and keep what is there."],
    bug=dict(title="write mode wipes the old file", kind="output", file="append.py", files={"log.txt": "Day 1\nDay 2\n"}, wrong='''
f = open("log.txt", "w")
f.write("Day 3\\n")
f.close()
print(open("log.txt").read())
''', fixed='''
f = open("log.txt", "a")
f.write("Day 3\\n")
f.close()
print(open("log.txt").read())
''', wrong_note="the mode is w", fixed_note="the mode is a",
             why="Mode w empties the file as soon as it is opened, so the old lines are lost; mode a keeps them and adds to the end.",
             narr="Bug of the Day. The log had Day one and Day two. We open it to add Day three, but we use write mode. Only Day three is left. Write mode empties the file the moment you open it. For adding, use append mode. The old lines stay, and the new line goes at the end."),
    pun="Why did the diary hate write mode? It always lost its past.",
    task="add a line to a file", challenge="Append the line \"Day 4\" to log.txt and print the file.",
    answer="Open log.txt with mode \"a\", write \"Day 4\\n\", close, then print(open(\"log.txt\").read()).",
    shorts=[
        ("Write mode", "To write a file, open it with a second argument, the mode. W means write. If the file does not exist, Python creates it. If it does exist, Python wipes it clean first. Then call write with your text. Remember that write does not add a new line, so put slash n at the end of each line yourself.", "OPEN(\"F.TXT\", \"W\")", "Create and fill a file."),
        ("Append mode", "To add to a file without losing its content, use append mode. Open with the letter a. Everything you write goes to the end of the file, and the old lines stay exactly as they were. Use it for logs, where you keep adding entries. It is the safe mode when you are not sure whether the file already holds something precious.", "OPEN(\"F.TXT\", \"A\")", "Add, never wipe."),
        ("New lines", "Write does not add a new line. If you write two strings, they join on one line. To start a new line, add the slash n character at the end of the string. Slash n is one character, the new line. Think of it as pressing the Enter key inside your text. Forget it, and your whole file becomes a single long line.", "F.WRITE(\"DAY 1\\N\")", "Add your own newline."),
        ("Write wipes the file", "A painful bug. You want to add a line to an old log, so you open it in write mode. The moment the file opens, everything inside is wiped. Only your new line is left. There is no warning, and no undo. Use append mode to add. Use write only when you really want to start from nothing.", "\"W\" EMPTIES THE FILE", "Pick the right mode."),
        ("Pun and challenge", "Why did the diary hate write mode? It always lost its past. Your challenge. Make a file called log dot txt with two lines in it. Then write a program that adds a line, Day four, to the end of that file, using append mode. Print the whole file afterwards, and check that all lines are there. Share your code in the comments.", "ADD A LINE", "Try append mode."),
    ],
))

EPISODES.append(dict(
    n=53, title="The with statement", spoken="the with statement",
    yt="Python with open(): The Safe Way to Use Files", thumb="WITH OPEN",
    vis="Xecxec holding a door that closes by itself after he walks through",
    goals=["use with to close files automatically", "read and write inside a with block", "see why forgetting close can lose data"],
    tags=["python with statement", "python with open", "python context manager basics", "close file python"],
    hash=["#with", "#files"],
    analogy="an automatic door: it closes behind you, even if you forget",
    c_title="Files that close themselves",
    c_pts=["with open(...) as f: opens the file for the block", "The file closes when the block ends", "It closes even if an error happens inside"],
    intro="Forgetting to close a file is a classic mistake. Today we learn a form that cannot forget.",
    concept="The with statement opens a file, and closes it for you when the block ends. Think of an automatic door. It closes behind you, even if you forget. Write with open, the name, as f, and a colon. The indented block can use f. When the block ends, even through an error, Python closes the file. Closing matters, because text you write may sit in a buffer, and only reaches the disk when the file is closed.",
    A=dict(file="withread.py", label="with and read", on="read inside a with block, then check closed",
           files=NOTES,
           src='''
with open("notes.txt") as f:
    text = f.read()
print(text.upper())
print(f.closed)
''',
           narr="[HL 1] The with line. Open the file, and tie it to f, for the block. [HL 2] Inside the block, read the text. [HL 3] The block has ended, so Python has already closed the file. We use the text we saved. Capital letters. [HL 4] The closed attribute confirms it. True. We never wrote close ourselves."),
    c2=dict(label="Open, use, auto-close", on="A timeline: with opens the file, the block runs, the file closes, even if an error arrow appears in the middle", narr="Here is the timeline. The with line opens the file. The block runs. When the block ends, the file is closed. Now imagine an error in the middle of the block. Without with, the close line would never run. With with, Python still closes the file on the way out. That is why with is the standard way to work with files.", anim=FILEFLOW),
    B=dict(file="withwrite.py", label="with and write", on="write, then read back, both in with blocks",
           src='''
with open("out.txt", "w") as f:
    f.write("Hello\\n")
with open("out.txt") as f:
    print(f.read().strip())
''',
           narr="[HL 1] Open for writing, inside with. [HL 2] Write one line. When this block ends, the file is closed and saved. [HL 3] Open the same file for reading, in a new with. [HL 4] Read it, strip the new line, and print. Hello. Two with blocks, and no close in sight."),
    term="Hello.",
    recap=["with open(...) as f: closes the file when the block ends.", "It closes even when an error happens inside.", "Write inside the block, and the data is saved when it ends.", "Prefer with over open and close."],
    bug=dict(title="forgetting to close", kind="output", file="withwrite.py", wrong='''
f = open("out.txt", "w")
f.write("Hello")
print(repr(open("out.txt").read()))
''', fixed='''
with open("out.txt", "w") as f:
    f.write("Hello")
print(repr(open("out.txt").read()))
''', wrong_note="the file is never closed", fixed_note="with closes and saves it",
             why="Written text waits in a buffer until the file is closed or flushed, so reading before closing can show an empty file.",
             narr="Bug of the Day. We write Hello, and read the file straight back. It shows empty quotes. The text was still waiting in a buffer, because we never closed the file. Use with, and the file is closed when the block ends, so the text reaches the disk. Then reading it back works."),
    pun="Why did the file love with? It never had to say goodbye.",
    task="read a file safely", challenge="Use with to read notes.txt and print its first line.",
    answer="Use with open(\"notes.txt\") as f: and print(f.readline().strip()). It prints Baga.",
    shorts=[
        ("The with statement", "The with statement opens a file, and closes it for you. With open, the name, as f, and a colon. Everything indented below can use f. When the block ends, Python closes the file automatically. It is like an automatic door, that closes behind you. You never have to remember to call close yourself.", "WITH OPEN(...) AS F:", "Files that close themselves."),
        ("Even when errors happen", "Here is the hidden power of with. If an error happens inside the block, Python still closes the file on the way out. Without with, an error in the middle can skip your close line, and leave the file open. With with, the cleanup always happens. That makes your programs safer, and the code shorter at the same time.", "ALWAYS CLOSES", "Safe cleanup."),
        ("Why closing matters", "When you write to a file, the text may wait in a buffer in memory. It reaches the disk when the file is closed. If you forget, another program, or even your own next line, may see an empty file. Closing is not just tidiness. It is how your data is really saved. With does it for you every time.", "CLOSE = SAVE", "Buffers explained."),
        ("The empty read", "A strange bug. You write Hello to a file, then read it straight back, and see empty quotes. The text was still waiting in the buffer, because you never closed the file. Use a with block for the writing. When the block ends, the file is closed, the data is saved, and the read finds your text.", "REPR(...) → ''", "Close before reading."),
        ("Pun and challenge", "Why did the file love with? It never had to say goodbye. Your challenge. Use a with block to open notes dot txt, and read its first line. Print that line without the extra new line. You should see Baga. Then try printing every line in capital letters, with a loop, still inside the with block. Share your code below.", "FIRST LINE WITH WITH", "Try with open."),
    ],
))

EPISODES.append(dict(
    n=54, title="try and except", spoken="try and except",
    yt="Python try and except: Handle Errors", thumb="CATCH THE ERROR",
    vis="Xecxec holding a safety net under a falling red ERROR block",
    goals=["catch an error with try and except", "catch specific exception types", "use else and finally"],
    tags=["python try except", "python exception handling", "python finally else", "bare except python"],
    hash=["#exceptions", "#tryexcept"],
    analogy="a safety net under a trapeze: if the artist falls, the net catches them, and the show goes on",
    c_title="A safety net for errors",
    c_pts=["try runs the risky code", "except handles one kind of error", "finally always runs at the end"],
    intro="Errors do not always mean a bug. A user can type anything. Today we learn to catch errors, and keep the program running.",
    concept="Put the risky code in a try block. If an error happens, Python jumps to a matching except block, instead of stopping. Name the error type, such as ValueError. Think of a safety net under a trapeze. If the artist falls, the net catches them, and the show goes on. Else runs when no error happened. Finally runs always, error or not. Catch only the errors you expect.",
    A=dict(file="tryex.py", label="Catching a ValueError", on="int of a bad string inside try",
           src='''
try:
    n = int("abc")
    print(n)
except ValueError:
    print("Not a number")
print("Program continues")
''',
           narr="[HL 1] The try block starts. [HL 2] This line fails, because abc is not a number. Python raises a value error, and jumps out of the try block at once. [HL 3] So this print is skipped. [HL 4] Except value error matches. [HL 5] Our message prints. [HL 6] And the program carries on. Without the net, it would have stopped at line two."),
    c2=dict(label="Where Python jumps", on="Flow: try block with a failing line; arrow jumps to the matching except; both rejoin before the next line", narr="Look at the path. Python enters the try block, and runs line by line. At the failing line, it stops, and jumps to the except that matches the error type. After the except block, both paths rejoin, and the program continues with the next line. Lines after the failing one, inside the try block, are skipped.", anim="A path enters a box, a lightning bolt hits one line, and the path jumps to a separate box before rejoining"),
    B=dict(file="finally.py", label="else and finally", on="three inputs, three outcomes",
           src='''
for text in ["5", "x", "0"]:
    try:
        print(10 // int(text))
    except ValueError:
        print("bad number")
    except ZeroDivisionError:
        print("zero!")
    else:
        print("ok")
    finally:
        print("done", text)
''',
           narr="[HL 1] [TRACK text=5] We try three inputs. [HL 3] Ten divided by the number. [HL 4] A bad number is a value error. [HL 6] Zero is a zero division error. Two except blocks, two different messages. [HL 8] Else runs only if nothing went wrong. [HL 10] Finally runs every time. For five, we see two, ok, done five. For x, bad number, done x. For zero, zero, done zero."),
    term="Two, ok, done five. Bad number, done x. Zero, done zero.",
    recap=["try runs risky code and except handles an error.", "Name the exception type you expect.", "else runs when there was no error and finally always runs.", "Catch specific errors, not everything."],
    bug=dict(title="a bare except hides the real bug", kind="output", file="tryex.py", wrong='''
try:
    print(totl)
except:
    print("Please enter a number")
''', fixed='''
total = 5
try:
    print(total)
except ValueError:
    print("Please enter a number")
''', wrong_note="except with no type catches the typo too", fixed_note="the typo is fixed and only ValueError is caught",
             why="A bare except catches every error, including your own typos, so it hides the real cause and shows a misleading message; catch specific types.",
             narr="Bug of the Day. We misspelled total. That is a name error. But the bare except catches it, and prints, please enter a number. A misleading message, and the real bug is hidden. Never use except with no type. Catch the specific error you expect, such as value error, and let other errors show themselves."),
    pun="Why did the exception go to therapy? It could not handle it.",
    task="catch a ValueError", challenge="Ask for a number with input, convert it with int, and print Not a number if the conversion fails.",
    answer="Use try: n = int(input(\"Number? \")) except ValueError: print(\"Not a number\").",
    shorts=[
        ("try and except", "Put risky code in a try block. If an error happens, Python jumps to a matching except block instead of stopping. Try, int of abc, except value error, print not a number. Now the program survives. Think of a safety net under a trapeze. The artist might fall, but the show goes on. Use it for input, files, and anything unpredictable.", "TRY: ... EXCEPT:", "A safety net."),
        ("Catch the right error", "Name the error type in the except line. Except value error catches only value errors. Other errors still stop the program, and show their traceback, which is what you want. A traceback tells you what went wrong. Catch only the errors you expect, and know how to handle. Let the surprises show themselves, so you can fix them.", "EXCEPT VALUEERROR:", "Be specific."),
        ("Else and finally", "Two helpers complete the pattern. Else runs only when the try block finished without an error. Finally runs every time, error or not. Use it for cleanup, like closing a file. The order is try, except, else, finally. Together they let you describe every outcome clearly, and make sure the important cleanup is never skipped.", "TRY · EXCEPT · ELSE · FINALLY", "Four parts."),
        ("The bare except trap", "A dangerous habit. You write except with no type. It catches every error, including your own typos. You misspell a name, and your program says, please enter a number, which has nothing to do with the real problem. Always name the error type. Let the unexpected errors show themselves, so that you can find and fix the real bug.", "EXCEPT: HIDES BUGS", "Always name the type."),
        ("Pun and challenge", "Why did the exception go to therapy? It could not handle it. Your challenge. Ask the user for a number with input. Convert it with int, inside a try block. If the conversion fails, print not a number, instead of crashing. Test it with the word abc, and with the number twelve. Share your code in the comments below.", "A SAFE NUMBER READER", "Try try and except."),
    ],
))

EPISODES.append(dict(
    n=55, title="Raising and custom exceptions", spoken="raising and custom exceptions",
    yt="Python raise and Custom Exceptions", thumb="RAISE YOUR OWN",
    vis="Xecxec raising a red flag labelled ValueError",
    goals=["raise an exception with raise", "read the message with as e", "define your own exception type"],
    tags=["python raise", "python custom exception", "python exception order", "except order python"],
    hash=["#exceptions", "#raise"],
    analogy="a referee: when a rule is broken, the referee blows the whistle and stops the play",
    c_title="Blowing the whistle",
    c_pts=["raise stops the function with an error", "except ... as e gives you the error object", "A custom exception is a class that extends Exception"],
    intro="Python raises errors for you. Today we raise our own, when our rules are broken.",
    concept="You can raise an error yourself. Raise, an exception type, and a message. It stops the function, and travels to the nearest matching except. Think of a referee. When a rule is broken, the referee blows the whistle and stops the play. Except as e gives you the error object, so you can print its message. For your own kind of error, make a class that extends Exception. It needs only one line.",
    A=dict(file="raiseit.py", label="Raise a ValueError", on="set_age rejects a negative age",
           src='''
def set_age(age):
    if age < 0:
        raise ValueError("age cannot be negative")
    return age
try:
    set_age(-5)
except ValueError as e:
    print("Error:", e)
print(set_age(20))
''',
           narr="[HL 1] A function that sets an age. [HL 2] If the age is negative, [HL 3] raise a value error, with a message. The function stops right here. [HL 4] Otherwise, return the age. [HL 5] We try. [HL 6] A bad value. [HL 7] Except value error as e catches it, and ties the error to e. [HL 8] Printing e shows our message. [HL 9] A good age goes straight through, and prints twenty."),
    c2=dict(label="The error travels up", on="A raise inside a function; the arrow leaves the function and lands in the except block of the caller", narr="Here is what raise does. The error starts inside the function, at the line that raised it. The function stops there. The error travels up to the caller, and looks for a matching except. If it finds one, that block runs. If not, it keeps travelling, and finally stops the program with a traceback. You decide who handles the error.", anim="A red arrow leaves a function box upward and lands in an except box; a second arrow shows the error passing through if no match"),
    B=dict(file="custom.py", label="A custom exception", on="BillError extends Exception",
           src='''
class BillError(Exception):
    pass
def pay(amount):
    if amount <= 0:
        raise BillError("amount must be positive")
    return amount
try:
    pay(0)
except BillError as e:
    print("Bill problem:", e)
''',
           narr="[HL 1] A new exception type. The name in brackets says it builds on Exception. We will study classes properly soon. [HL 2] Pass means, nothing more is needed. [HL 3] A payment function. [HL 4] If the amount is zero or less, [HL 5] raise our own error, with a message. [HL 6] Return the amount otherwise. [HL 7] Try. [HL 8] A bad payment. [HL 9] Except bill error as e catches only our type. [HL 10] Bill problem, amount must be positive."),
    term="Bill problem, amount must be positive.",
    recap=["raise Type(message) stops the code with an error.", "except Type as e gives you the error to print.", "A custom exception is a class that extends Exception.", "Put the most specific except first."],
    bug=dict(title="the except blocks are in the wrong order", kind="output", file="raiseit.py", wrong='''
try:
    int("x")
except Exception:
    print("general")
except ValueError:
    print("value")
''', fixed='''
try:
    int("x")
except ValueError:
    print("value")
except Exception:
    print("general")
''', wrong_note="the general block comes first", fixed_note="the specific block comes first",
             why="Python uses the first except that matches, and Exception matches everything, so a later more specific block never runs.",
             narr="Bug of the Day. We have a value error block, but the output says general. Python tries the except blocks in order, and uses the first match. Exception matches every error, so it wins, and the value error block never runs. Put the most specific block first, and the general one last."),
    pun="Why was the referee so good at coding? It knew when to raise a flag.",
    task="raise an error for a bad score", challenge="Write check_score(score) that raises ValueError if score is above 100, and test it with 120.",
    answer="Use def check_score(score): if score > 100: raise ValueError(\"score too high\"), then wrap check_score(120) in try and except ValueError.",
    shorts=[
        ("Raise", "You can raise an error yourself. Raise, an exception type, and a message. Raise value error, age cannot be negative. The function stops at that line, and the error travels up to the nearest except. Think of a referee blowing a whistle when a rule is broken. Use raise when your function receives a value it cannot accept.", "RAISE VALUEERROR(\"...\")", "Blow the whistle."),
        ("Except as e", "To read the error message, add as e to the except line. Except value error as e. Now e holds the error object. Printing e shows the message you passed to raise. It is a good way to tell the user what went wrong, in your own words. It also helps when you log errors, to find bugs later.", "EXCEPT VALUEERROR AS E:", "Read the message."),
        ("Your own exception", "You can make your own kind of exception. Write class, a name, then Exception in brackets, and a colon, and the word pass. That is the whole thing. Now you can raise it, and catch it by name. It makes your code read clearly, because bill error says exactly what went wrong, better than a plain value error.", "CLASS BILLERROR(EXCEPTION):", "A custom error type."),
        ("Order of except blocks", "Here is a quiet bug. You write an except for exception first, and an except for value error after it. Python uses the first match. Exception matches everything, so it wins, and the second block never runs. No error, only the wrong message. Put the most specific block first, and the general one last.", "SPECIFIC FIRST", "Order matters."),
        ("Pun and challenge", "Why was the referee so good at coding? It knew when to raise a flag. Your challenge. Write a function called check score, that raises a value error if the score is above one hundred. Then call it with one twenty inside a try block, and print the error message in the except block. Share your code in the comments below.", "RAISE FOR A BAD SCORE", "Try raise."),
    ],
))

EPISODES.append(dict(
    n=56, title="Modules and import", spoken="modules and import",
    yt="Python Modules and import Explained", thumb="IMPORT A TOOL",
    vis="Xecxec opening a toolbox labelled math and pulling out a calculator",
    goals=["import a module and use its names", "import a single name with from", "import your own file as a module"],
    tags=["python import", "python modules", "python from import", "modulenotfounderror"],
    hash=["#modules", "#import"],
    analogy="a toolbox in a garage: you fetch the box you need, and use the tools inside",
    c_title="Borrowing code",
    c_pts=["import module makes its names available as module.name", "from module import name brings one name in directly", "Every .py file is a module"],
    intro="Nobody writes everything from scratch. Today we learn to borrow code, from Python and from our own files.",
    concept="A module is a file of ready-made code. Import brings it in. After import math, you write math, a dot, and the name you want. From math import floor brings floor in directly, with no prefix. Python ships with hundreds of modules, called the standard library. Think of a toolbox in a garage. You fetch the box you need, and use the tools inside. Any dot py file you write is also a module, if it sits in the same folder.",
    A=dict(file="usemod.py", label="Import in action", on="import your own module, and two standard ones",
           files={"shacktools.py": 'def label(name):\n    return "[" + name + "]"\n'},
           src='''
import shacktools
print(shacktools.label("Baga"))
import math
print(math.sqrt(16))
from shacktools import label
print(label("Colva"))
print(math.pi)
''',
           narr="[HL 1] Import our own file, shacktools dot py, from the same folder. [HL 2] Use its function with the module name and a dot. [HL 3] Import the math module from the standard library. [HL 4] Square root of sixteen is four point zero. [HL 5] From, the module, import, a name. Now label works without the prefix. [HL 6] Colva in brackets. [HL 7] And pi, with every digit a float can hold."),
    c2=dict(label="Where import looks", on="A search path: the current folder first, then the standard library, then installed packages", narr="Here is where Python looks. First, the folder of your script. Then the standard library. Then the packages you installed. The first match wins. So never name your own file the same as a standard module, like random or math. Your file would hide the real one, and strange errors would follow.", anim="A path of three boxes lights up in order; a matching box stops the search"),
    B=dict(file="alias.py", label="Aliases and from", on="import with as, and from with several names",
           src='''
import math as m
from math import floor, ceil
print(m.floor(2.7))
print(floor(2.7), ceil(2.1))
''',
           narr="[HL 1] Import math, and give it the short name m. [HL 2] From math, import floor and ceil, two names at once. [HL 3] Use the alias. Floor of two point seven is two. [HL 4] Use the names directly. Floor gives two, ceil of two point one gives three. Aliases save typing, and from imports save more. Use whichever keeps your code clear."),
    term="Two, then two three.",
    recap=["import module gives you module.name.", "from module import name gives you name directly.", "as gives a module a shorter name.", "Your own dot py file is a module too."],
    bug=dict(title="a module that does not exist", file="usemod.py", wrong='''
import maths
print(maths.sqrt(16))
''', fixed='''
import math
print(math.sqrt(16))
''', wrong_note="maths is a typo for math", fixed_note="the right module name",
             why="Python can only import a module it can find; a misspelled name is not found, so Python raises ModuleNotFoundError.",
             narr="Bug of the Day. We import maths, with an s. There is no such module. Python says, module not found error, no module named maths. Check the spelling of the module name. The error shows exactly what it looked for. Fix the name, and the import works."),
    pun="Why did the programmer love imports? Someone else had already done the hard work.",
    task="use math for a circle area", challenge="Import math and print the area of a circle of radius 3, rounded to 2 decimals.",
    answer="Use import math and print(round(math.pi * 3 ** 2, 2)), which prints 28.27.",
    shorts=[
        ("What is a module?", "A module is a file of ready-made code. Import brings it in. After import math, you write math dot sqrt, and Python finds the square root tool inside. Python ships with hundreds of modules, called the standard library. Think of a toolbox in a garage. You fetch the box you need, and use the tools inside, without building them yourself.", "IMPORT MATH", "Borrow ready-made code."),
        ("From import", "Sometimes you want just one tool from a module. From math import floor. Now you can write floor directly, with no math prefix. You can import several names at once, separated by commas. It makes code shorter, but the prefix form tells readers where a name came from. Use from imports for a few well-known names, and the prefix form otherwise.", "FROM MATH IMPORT FLOOR", "Bring one name in."),
        ("Your own modules", "Every dot py file you write is a module. Put a function in shacktools dot py. In another file, in the same folder, write import shacktools. Then call shacktools dot label. That is how big programs are split into small files. Never name your file the same as a standard module, like random or math, or you will hide the real one.", "IMPORT SHACKTOOLS", "Your files are modules."),
        ("Module not found", "The import bug. You write import maths, with an s. Python says, module not found error, no module named maths. The error shows exactly the name it looked for. Check the spelling. Check that the file is in the same folder, if it is your own. And if it is a package, check that you installed it, which we cover in a few episodes.", "MODULENOTFOUNDERROR", "Check the name."),
        ("Pun and challenge", "Why did the programmer love imports? Someone else had already done the hard work. Your challenge. Import the math module. Print the area of a circle with radius three. The formula is pi times radius squared. Round the answer to two decimals. You should see twenty eight point two seven. Share your line of code in the comments below.", "A CIRCLE'S AREA", "Try math."),
    ],
))

EPISODES.append(dict(
    n=57, title="Writing your own module", spoken="writing your own module",
    yt="Python: if __name__ == \"__main__\" Explained", thumb="__NAME__ == MAIN",
    vis="Xecxec holding a sign that says MAIN in one claw and a sign that says IMPORTED in the other",
    goals=["put reusable functions in a module", "explain what __name__ holds", "keep test code from running on import"],
    tags=["python __name__ main", "python write module", "python import side effects", "if name equals main"],
    hash=["#modules", "#main"],
    analogy="a shop with a front counter and a storeroom: the demo runs only when the shop is opened directly, not when someone borrows a tool",
    c_title="Run or imported?",
    c_pts=["Python sets __name__ for every file", "A file run directly has __name__ equal to \"__main__\"", "An imported file has its own file name instead"],
    intro="A module often has test code at the bottom. Today we learn how to stop it running every time someone imports the file.",
    concept="When Python runs a file, it sets a special name called dunder name. If you run the file directly, dunder name is the text, dunder main. If another file imports it, dunder name is the module's own name. So you can put an if at the bottom, if dunder name equals dunder main. Code under that if runs only when the file is run directly, not when it is imported.",
    A=dict(file="usearea.py", label="A module with a guard", on="importing shape.py does not run its demo",
           files={"shape.py": 'def area(w, h):\n    return w * h\n\nif __name__ == "__main__":\n    print("Testing:", area(2, 3))\n'},
           src='''
import shape
print(shape.area(4, 5))
print(shape.__name__)
''',
           narr="[HL 1] Import our module. Python runs shape dot py from top to bottom. It defines area, and then reaches the guard. Dunder name is shape here, not main, so the test line is skipped. [HL 2] Use the module's function. Twenty. [HL 3] The module's name is simply shape. If you run shape dot py directly, you would see its test print instead."),
    c2=dict(label="Two ways to start a file", on="Two panels: running shape.py directly gives __name__ = '__main__' and the demo runs; importing it gives __name__ = 'shape' and the demo is skipped", narr="Here are the two cases side by side. On the left, you run the file directly. The name is main, the guard is True, and the test code runs. On the right, another file imports it. The name is the module's own name, the guard is False, and the test is skipped. One file, two behaviours, chosen by one if.", anim="Two panels with the value of __name__ flipping; the guarded line lights up on the left and stays grey on the right"),
    B=dict(file="shape_run.py", label="Seeing __name__", on="print __name__ and use the guard in a script",
           src='''
def area(w, h):
    return w * h
print(__name__)
if __name__ == "__main__":
    print(area(2, 3))
''',
           narr="[HL 1] A small function. [HL 2] Return the product. [HL 3] Print the special name. When we run this file directly, it says dunder main. [HL 4] The guard. [HL 5] True, so the test line runs. Six. If this file were imported, the guard would be False, and only the function would be defined."),
    term="Dunder main, then six.",
    recap=["Python sets __name__ for every file.", "A file run directly has __name__ equal to \"__main__\".", "An imported file has its own name instead.", "Put test or demo code under the main guard."],
    bug=dict(title="test code runs on import", kind="output", file="usearea.py",
             files={"shape.py": 'def area(w, h):\n    return w * h\n\nprint("Testing:", area(2, 3))\n'},
             fixed_files={"shape.py": 'def area(w, h):\n    return w * h\n\nif __name__ == "__main__":\n    print("Testing:", area(2, 3))\n'},
             wrong='''
import shape
print(shape.area(4, 5))
''', fixed='''
import shape
print(shape.area(4, 5))
''', wrong_note="shape.py prints its test at the top level", fixed_note="shape.py hides its test behind the guard",
             why="Every line at the top level of a module runs when it is imported, so a stray print appears in every program that imports it; guard it with if __name__ == \"__main__\".",
             narr="Bug of the Day. Our module prints a test line at the top level. We import it, and the test line appears in our own program's output. Every top level line of a module runs when it is imported. Wrap the test in the main guard, and now it runs only when you run the module directly."),
    pun="Why was the module so well behaved? It knew when it was main, and when it was only a guest.",
    task="guard a demo", challenge="Write a module file with one function, and a demo print guarded by the main guard.",
    answer="Put the function first, then if __name__ == \"__main__\": print(demo_call).",
    shorts=[
        ("What is __name__?", "Every Python file has a special name called dunder name. If you run the file directly, dunder name is the text, dunder main. If another file imports it, dunder name is the file's own name instead. It is Python's way of telling the file how it is being used. One small value, and a very useful trick.", "__NAME__", "How was I started?"),
        ("The main guard", "Put this at the bottom of a module. If dunder name equals dunder main, colon. Everything below it runs only when you run the file directly. When another file imports it, the guard is False, and the code is skipped. It is the standard way to keep test code and demos in a module without bothering the files that import it.", "IF __NAME__ == \"__MAIN__\":", "Run only when main."),
        ("Reusable code", "Modules let you split a big program into small files. Put your functions in one file, and import them everywhere. Every file only needs to know the names it uses. If you fix a function once, every file that imports it gets the fix. That is why professional code is split into modules, and not written as one huge file.", "ONE FIX, EVERYWHERE", "Split into files."),
        ("Surprise output", "A bug that confuses beginners. You import a module, and extra lines appear in your output. The module has print statements at the top level, and every top level line runs on import. Wrap test code in the main guard, and it only runs when you run the module itself. Your imports become quiet, and predictable.", "TEST LINE ON IMPORT", "Hide the demo."),
        ("Pun and challenge", "Why was the module so well behaved? It knew when it was main, and when it was only a guest. Your challenge. Write a module with one function, and a demo call to it, guarded by if dunder name equals dunder main. Then import it from another file, and check that the demo does not run. Share your module below.", "GUARD YOUR DEMO", "Try the main guard."),
    ],
))

EPISODES.append(dict(
    n=58, title="pip and virtual environments", spoken="pip and virtual environments",
    yt="Python pip and venv for Beginners", thumb="PIP + VENV",
    vis="Xecxec carrying a package box labelled pip install into a clean glass room labelled venv",
    goals=["install a package with pip", "make an isolated environment with venv", "know when a package is in the wrong environment"],
    tags=["python pip", "python venv", "virtual environment python", "pip install python"],
    hash=["#pip", "#venv"],
    analogy="a kitchen per recipe: each dish gets its own set of ingredients, so one recipe cannot spoil another",
    c_title="Packages and environments",
    c_pts=["pip installs packages from the Python Package Index", "A virtual environment is a private folder of packages", "Activate the environment before you install"],
    intro="Python has a huge library of packages written by other people. Today we learn how to install them safely.",
    concept="Pip is the tool that installs packages. Pip install, and the package name. But if you install everything into one place, projects start to clash. A virtual environment is a private folder of packages, one per project. Think of a separate kitchen for each recipe. One recipe cannot spoil another. You make one with python dash m venv. You activate it, and then pip installs into it.",
    A=dict(file="pipcheck.py", label="Is a package installed?", on="try to import a package that is not installed yet",
           src='''
try:
    import pyfiglet
    print("pyfiglet is installed")
except ModuleNotFoundError:
    print("pyfiglet is missing")
''',
           narr="[HL 1] A try block. [HL 2] We try to import a package called pyfiglet. [HL 3] If it works, we say so. [HL 4] If Python cannot find it, [HL 5] we say it is missing. On a fresh computer, the answer is missing. After pip install pyfiglet, the same program says installed. The terminal commands are shown on screen."),
    ref=[("Terminal commands", "python -m venv .venv\n.venv\\Scripts\\activate        (Windows)\nsource .venv/bin/activate      (Mac and Linux)\npython -m pip install pyfiglet\npython -m pip list\ndeactivate")],
    c2=dict(label="One kitchen per recipe", on="Two project boxes, each with its own packages folder; a global Python sits outside both", narr="Here is the picture. Python sits in the middle. Project one has its own private folder of packages. Project two has another. They can even use different versions of the same package, without clashing. A virtual environment is just that private folder, plus a small script that points Python at it. Activate it, and every pip install goes inside.", anim="Two project boxes with separate package shelves; a global Python box stays unchanged"),
    B=dict(file="inenv.py", label="Am I inside a venv?", on="compare prefix and base prefix",
           src='''
import sys
print(sys.prefix != sys.base_prefix)
''',
           narr="[HL 1] The sys module knows how Python was started. [HL 2] Prefix is where this Python lives. Base prefix is the main installation. Inside a virtual environment, they differ, and this prints True. Outside one, they are the same, and it prints False. Run it before and after you activate your environment, and watch the answer change."),
    term="False, outside a virtual environment. After you activate one, it prints True.",
    recap=["pip installs packages into the Python that runs it.", "A virtual environment is a private set of packages for one project.", "Activate the environment before you run pip install.", "Use python -m pip, so pip matches your python."],
    bug=dict(title="the package went to the wrong environment", file="pipcheck.py", wrong='''
import pyfiglet
print(pyfiglet.figlet_format("Hi"))
''', fixed='''
try:
    import pyfiglet
except ModuleNotFoundError:
    print("Install it with: python -m pip install pyfiglet")
''', wrong_note="the package is not in this Python", fixed_note="the program tells you how to install it",
             why="pip may have installed the package into a different Python, or a different environment, than the one running your script; python -m pip installs into the Python you run.",
             narr="Bug of the Day. We installed the package, but our script says, module not found error, no module named pyfiglet. The package went to a different Python, or a different environment, than the one running our script. Activate your virtual environment, and install with python dash m pip, so pip belongs to the same Python."),
    pun="Why did the package love virtual environments? It finally had its own room.",
    task="make and use a venv", challenge="Create a virtual environment called .venv, activate it, and run python -m pip list.",
    answer="Run python -m venv .venv, then activate it, then python -m pip list. The list is nearly empty.",
    shorts=[
        ("What is pip?", "Pip is Python's package installer. Pip install, and the name of a package, downloads it from the Python Package Index, and makes it available to import. There are hundreds of thousands of packages, for web apps, data, games, and more. Use python dash m pip, so that pip belongs to the same Python that runs your code.", "PIP INSTALL NAME", "Install a package."),
        ("Why venv?", "If you install every package into one place, projects start to clash, because they need different versions. A virtual environment solves this. It is a private folder of packages, one for each project. Think of a separate kitchen for each recipe. One recipe cannot spoil another. Make one for every project, and you will avoid many headaches.", "ONE ENVIRONMENT PER PROJECT", "A kitchen per recipe."),
        ("Make and activate", "Making an environment takes one command. Python dash m venv dot venv. That creates a folder called dot venv. Activate it with the activate script, which is different on Windows and on Mac or Linux. Your terminal prompt changes, to show the environment name. Now every pip install goes into that folder, and nowhere else.", "PYTHON -M VENV .VENV", "Two commands."),
        ("Wrong environment", "A common bug. You install a package, but your script says, module not found error. The package went into a different Python than the one running the script. Check which environment is active. Activate the right one, and install with python dash m pip. Then the package and the script share the same Python.", "INSTALLED… BUT NOT FOUND", "Same Python, same pip."),
        ("Pun and challenge", "Why did the package love virtual environments? It finally had its own room. Your challenge. Create a virtual environment called dot venv. Activate it. Then run python dash m pip list, and see how short the list is. A fresh environment is nearly empty. Share what you see in the comments, and tell us which system you use.", "MAKE A VENV", "Try venv."),
    ],
))

EPISODES.append(dict(
    n=59, title="CSV and JSON basics", spoken="CSV and JSON basics",
    yt="Python CSV and JSON for Beginners", thumb="CSV + JSON",
    vis="Xecxec holding a spreadsheet in one claw and a curly-bracket scroll in the other",
    goals=["read a CSV file by column names", "turn data into JSON text and back", "know that JSON keys become strings"],
    tags=["python csv", "python json", "json dumps loads", "csv dictreader"],
    hash=["#csv", "#json"],
    analogy="a spreadsheet and a packing list: CSV is rows and columns, JSON is labelled boxes inside boxes",
    c_title="Two common formats",
    c_pts=["CSV is rows of values separated by commas", "csv.DictReader reads each row as a dictionary", "json.dumps makes text and json.loads reads it back"],
    intro="Real data lives in files like spreadsheets and web responses. Today we read two common formats.",
    concept="CSV means comma separated values. Each line is a row, and the first line names the columns. The csv module reads each row as a dictionary. JSON is the format of the web. It looks like Python dictionaries and lists. Json dumps turns Python data into JSON text. Json loads turns JSON text back into Python data. One catch. JSON keys are always strings, so a number key comes back as text.",
    A=dict(file="readcsv.py", label="Reading a CSV file", on="DictReader gives one dictionary per row",
           files={"marks.csv": "name,marks\nAsha,88\nRavi,92\n"},
           src='''
import csv
with open("marks.csv") as f:
    for row in csv.DictReader(f):
        print(row["name"], row["marks"])
''',
           narr="[HL 1] Import the csv module. [HL 2] Open the file with with. [HL 3] DictReader reads the first line as column names, and gives one dictionary for each following row. [HL 4] Pick the fields by column name. Asha, eighty eight. Ravi, ninety two. Notice that every value is a string. Convert with int if you need numbers."),
    c2=dict(label="Row to dictionary", on="A CSV table with a header row; each data row becomes a dictionary with the header names as keys", narr="Look at how DictReader works. The first line is the header, name and marks. For each later line, it builds a dictionary. The header names become the keys, and the cells become the values. So a row becomes a dictionary with name and marks. Every value is a string, because a file has no way to know what is a number.", anim="Table rows slide out one by one and turn into dictionaries with keys from the header"),
    B=dict(file="jsondemo.py", label="JSON round trip", on="dumps, loads, and what changes on the way",
           src='''
import json
data = {"name": "Asha", "marks": [88, 92], "pass": True}
text = json.dumps(data)
print(text)
back = json.loads(text)
print(back["marks"][1])
print({1: "a"} == json.loads(json.dumps({1: "a"})))
''',
           narr="[HL 1] Import the json module. [HL 2] A dictionary with a string, a list, and a boolean. [HL 3] Dumps turns it into JSON text. [HL 4] The text uses double quotes, and a lowercase true. [HL 5] Loads turns the text back into Python data. [HL 6] The second mark is ninety two. [HL 7] And now the catch. A dictionary with the number one as a key, after a round trip, is not equal to the original. False. The key came back as the text one."),
    term="The JSON text, then ninety two, then False.",
    recap=["CSV rows can be read as dictionaries with csv.DictReader.", "All CSV values come in as strings.", "json.dumps makes JSON text and json.loads reads it.", "JSON keys are always strings."],
    bug=dict(title="JSON keys become strings", kind="output", file="jsondemo.py", wrong='''
import json
data = {1: "one"}
print(json.loads(json.dumps(data)))
''', fixed='''
import json
data = {1: "one"}
back = json.loads(json.dumps(data))
print({int(k): v for k, v in back.items()})
''', wrong_note="the number key 1 changes", fixed_note="keys are converted back with int()",
             why="JSON only allows string keys, so a number key is written as text; convert the keys back yourself after loading.",
             narr="Bug of the Day. We save a dictionary with the number one as a key, and load it back. The key is now the text one, in quotes. JSON only allows string keys. A lookup with the number one would now fail. After loading, convert the keys back with int, in a dictionary comprehension."),
    pun="Why did JSON go to school? It wanted to learn the keys, but only as strings.",
    task="read a column from a CSV", challenge="Read marks.csv and print the total of the marks.",
    answer="Use total = 0, loop over csv.DictReader(f), add int(row[\"marks\"]). It prints 180.",
    shorts=[
        ("CSV files", "A CSV file stores a table as plain text. Each line is a row, and the cells are separated by commas. The first line names the columns. The csv module can read each row as a dictionary, keyed by those names. Use DictReader, and pick fields like row, bracket, name. Every value arrives as a string, so convert numbers with int.", "NAME,MARKS", "Spreadsheets as text."),
        ("DictReader", "Csv dot DictReader reads a file, and gives you one dictionary for each data row. The first line becomes the keys. So you write row name, and row marks, and the code reads like the table. It is far safer than splitting lines by commas yourself, because it handles quotes, and commas inside cells. Open the file with with, and loop.", "CSV.DICTREADER(F)", "A dictionary per row."),
        ("JSON text", "JSON is the format of the web. It looks like Python dictionaries and lists. Json dumps turns Python data into JSON text, ready to save or send. Json loads turns JSON text back into Python data. Together they let your program talk to files, and to other programs, in a format that almost every language understands.", "DUMPS · LOADS", "Python data to text and back."),
        ("Keys become strings", "A small JSON surprise. You save a dictionary with the number one as a key. You load it back, and the key is now the text one. JSON only allows string keys. A lookup with the number one will fail. After loading, convert the keys back with int, in a dictionary comprehension, and your data is whole again.", "1 → \"1\"", "JSON keys are text."),
        ("Pun and challenge", "Why did JSON go to school? It wanted to learn the keys, but only as strings. Your challenge. Make a CSV file with names and marks, two columns, three rows. Read it with csv dot DictReader. Add up all the marks, converting each with int, and print the total. Check it with a calculator. Share your code in the comments below.", "TOTAL FROM A CSV", "Try CSV."),
    ],
))

EPISODES.append(dict(
    n=60, title="Mini project: Contact book", spoken="the contact book mini project",
    yt="Python Mini Project: Contact Book With JSON", thumb="CONTACT BOOK",
    vis="Xecxec holding a little address book with a phone icon",
    goals=["save a dictionary to a JSON file", "load it back when the program starts", "survive a missing or empty file"],
    tags=["python contact book", "python json file", "python mini project", "jsondecodeerror"],
    hash=["#project", "#json"],
    analogy="a paper address book: you open it, add an entry, and put it back on the shelf",
    c_title="Planning the contact book",
    c_pts=["Keep contacts in a dictionary of name to phone", "Load it from contacts.json at the start", "Save it back after every change"],
    intro="Time for a project that remembers things. Today we build a contact book that saves to a file.",
    concept="Here is the plan. Contacts live in a dictionary, name to phone number. At the start, we load the dictionary from a JSON file. If the file does not exist yet, we start with an empty dictionary. After every change, we save the dictionary back, with json dump. Now the contacts survive after the program ends. It uses files, JSON, exceptions, and dictionaries, everything from this module.",
    A=dict(file="contacts.py", label="Load, add, save", on="a missing file is fine; add a contact and save",
           src='''
import json
try:
    with open("contacts.json") as f:
        contacts = json.load(f)
except FileNotFoundError:
    contacts = {}
contacts["Asha"] = "98220 11111"
with open("contacts.json", "w") as f:
    json.dump(contacts, f)
print(contacts)
print(len(contacts))
''',
           narr="[HL 1] Import json. [HL 2] Try to load. [HL 3] Open the contacts file. [HL 4] Load the dictionary from it. [HL 5] If the file does not exist yet, [HL 6] start with an empty dictionary. [HL 7] Add a contact. [HL 8] Open the file for writing. [HL 9] Dump the dictionary into it. [HL 10] Print the contacts. [HL 11] And how many there are. On the first run, there is one."),
    c2=dict(label="Load, change, save", on="A cycle: load from file, change the dictionary, save to file, repeat on the next run", narr="Here is the cycle. Load the data from the file. Change it in memory. Save it back to the file. The next time the program runs, it loads what was saved. That is how every simple app remembers things. If the file is missing on the first run, start with an empty dictionary, and the cycle still works.", anim="Three boxes in a loop with an arrow; a file icon sits in the middle"),
    B=dict(file="showcontacts.py", label="Reading saved contacts", on="load an existing file and list the contacts",
           files={"contacts.json": '{"Ravi": "98220 22222"}'},
           src='''
import json
with open("contacts.json") as f:
    contacts = json.load(f)
for name, phone in sorted(contacts.items()):
    print(name, phone)
print("Asha" in contacts)
''',
           narr="[HL 1] Import json. [HL 2] Open the saved file. [HL 3] Load it into a dictionary. [HL 4] Loop over the pairs, in alphabetical order. [HL 5] Print each name and phone number. Ravi, nine eight two two zero, two two two two two. [HL 6] And check for a name that is not saved yet. Asha is not there, so False."),
    term="Ravi and his number, then False.",
    recap=["Keep the data in a dictionary and save it with json.dump.", "Load it at the start with json.load.", "Handle a missing file with except FileNotFoundError.", "An empty or damaged file raises a JSONDecodeError."],
    bug=dict(title="loading an empty JSON file", file="contacts.py", trim=1, files={"contacts.json": "\n"}, wrong='''
import json
with open("contacts.json") as f:
    contacts = json.load(f)
''', fixed='''
import json
try:
    with open("contacts.json") as f:
        contacts = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    contacts = {}
print(contacts)
''', wrong_note="contacts.json exists but is empty", fixed_note="both problems are handled",
             why="An empty file is not valid JSON, so json.load raises a JSONDecodeError; catch it and start with an empty dictionary.",
             narr="Bug of the Day. The file exists, but it is empty. Json load says, JSON decode error, expecting value, line two column one. An empty file is not valid JSON. Catch the error, along with file not found, and start with an empty dictionary. Your program now survives a missing file, and an empty one."),
    pun="Why did the contact book never lose touch? It always saved everyone.",
    task="add a delete feature", challenge="Add code to delete the contact Ravi from the dictionary if he is there, and save the file again.",
    answer="Use if \"Ravi\" in contacts: del contacts[\"Ravi\"], then save with json.dump(contacts, f).",
    shorts=[
        ("The contact book plan", "Let us build a contact book that remembers. Keep contacts in a dictionary, name to phone number. At the start, load the dictionary from a JSON file. After every change, save it back. Now the contacts survive after the program ends. It uses files, JSON, exceptions, and dictionaries, so it is the perfect project for this module.", "A CONTACT BOOK", "A program with memory."),
        ("Save with json dump", "To save a dictionary, open the file in write mode, inside a with block. Then call json dot dump, with the dictionary and the file. The data is written as JSON text. Because we use with, the file is closed and saved when the block ends. One short block, and your data is safe on disk.", "JSON.DUMP(DATA, F)", "Save the dictionary."),
        ("Load with json load", "To load, open the file, and call json dot load. You get the dictionary back, exactly as you saved it, apart from keys being strings. Wrap it in try and except, because on the first run, the file does not exist yet. In the except block, start with an empty dictionary. Your program now works on its first run, too.", "JSON.LOAD(F)", "Load it back."),
        ("Empty file", "A bug that appears after a crash. The file exists, but it is empty. Json load says, JSON decode error, expecting value, line one, column one. An empty file is not valid JSON. Catch the error, along with file not found, and start with an empty dictionary. Real programs must expect damaged files, not only missing ones.", "JSONDECODEERROR", "Expect empty files."),
        ("Pun and challenge", "Why did the contact book never lose touch? It always saved everyone. Your challenge. Add a delete feature to the contact book. If the name Ravi is in the dictionary, delete it, and save the file again. Then load the file in another run, and check that Ravi is gone. Share your code in the comments below.", "DELETE A CONTACT", "Extend the contact book."),
    ],
))
