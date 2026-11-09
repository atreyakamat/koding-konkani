"""Module 2 — Control flow and loops (EP 13-22)."""

MODULE = {"id": 2, "name": "Control flow and loops", "range": "13–22", "colours": "Cream + Apricot"}
EPISODES = []
NEXT_AFTER = ("Next: EP 23 · String methods", "Module two is done! Next time: string methods, the tools that clean and change text.")

FLOW = "Flowchart boxes light up one at a time; the arrow follows the path Python takes, and the skipped branch stays grey"

EPISODES.append(dict(
    n=13, title="if and else", spoken="if and else",
    yt="Python if and else: Make Your Program Decide", thumb="IF OR ELSE?",
    vis="Xecxec standing at a fork in a beach path, one sign saying IF and the other saying ELSE",
    goals=["write a decision with if and else", "use the colon and the indent correctly", "run lines after the decision whatever the answer"],
    tags=["python if else", "python conditions", "python decisions", "syntaxerror expected colon"],
    hash=["#ifelse", "#conditions"],
    analogy="a beach lifeguard flag: red flag, you stay out; green flag, you can swim",
    c_title="Making decisions",
    c_pts=["if checks a condition", "else runs when the condition is False", "The colon and the indent mark each block"],
    intro="Programs become interesting when they can choose. Today we make our first real decisions with if and else.",
    concept="A decision has three parts. The word if, a condition that is True or False, and a colon. The lines indented below run only when the condition is True. Else gives the other path, for when it is False. Think of a lifeguard flag. Red flag, you stay out. Green flag, you can swim. The program checks, then walks down exactly one path.",
    A=dict(file="weather.py", label="A two-path decision", on="a hot-day check with a block of two lines",
           src='''
temperature = 34
if temperature > 30:
    print("Hot day")
    print("Drink water")
else:
    print("Pleasant day")
print("Enjoy the beach")
''',
           narr="[HL 1] The temperature is thirty four. [HL 2] The condition asks, is it greater than thirty? That is True. The colon opens the block. [HL 3] First line of the block, indented. [HL 4] Second line, same indent, so it is in the same block. [HL 5] Else covers the other path. Python skips it this time. [HL 6] This line would run if the answer were False. [HL 7] The last line is at the left edge, so it runs on both paths.",
           label2="Reading the output", narr2="Predict first. [TRACK temperature=34] Thirty four is greater than thirty. So both lines of the hot block run, and the else block is skipped. Then the last line prints. The output is Hot day, Drink water, Enjoy the beach. Change the temperature to twenty five, and the other path runs."),
    c2=dict(label="The path through the decision", on="A flowchart: condition diamond, a yes branch for the if block, a no branch for the else block, and a join before the last line",
            narr="Here is the decision as a map. Python arrives at the diamond and asks the question. If the answer is yes, it walks the if branch. If the answer is no, it walks the else branch. Then both branches join, and the program carries on with the next line. Exactly one branch is walked every time.", anim=FLOW),
    B=dict(file="marks.py", label="Pass or try again", on="a marks check with else",
           src='''
marks = 38
if marks >= 40:
    print("Pass")
else:
    print("Try again")
''',
           narr="[HL 1] [TRACK marks=38] Marks are thirty eight. [HL 2] Is marks greater than or equal to forty? No, thirty eight is smaller. [HL 3] So the Pass line is skipped. [HL 4] Python jumps to else. [HL 5] Try again prints. Change marks to forty, and Pass prints instead. Test the edge value, forty, every time you write a condition like this."),
    term="Try again. Thirty eight is below the pass mark of forty.",
    recap=["if runs a block only when its condition is True.", "else runs when the condition is False.", "The colon opens a block and the indent shows what belongs to it.", "A line at the left edge runs whichever path was taken."],
    bug=dict(title="a missing colon", file="marks.py", wrong='''
marks = 38
if marks >= 40
    print("Pass")
''', fixed='''
marks = 38
if marks >= 40:
    print("Pass")
''', wrong_note="no colon after the condition", fixed_note="colon added",
             why="The colon tells Python that a block follows; without it Python cannot tell where the condition ends.",
             narr="Bug of the Day. We forgot the colon after the condition. Python says, syntax error, expected a colon. The arrow points to the exact spot where the colon should be. Every if line must end with a colon. It tells Python, a block starts on the next line. Add it, and the program runs."),
    pun="Why did the program stand at the fork in the road? It had a lot of conditions to consider.",
    task="print Cheap or Expensive for a price", challenge="Make price = 450. Print Cheap if the price is below 500, otherwise print Expensive.",
    answer="Use if price < 500: print(\"Cheap\") and else: print(\"Expensive\"). With 450 it prints Cheap.",
    shorts=[
        ("What is if?", "The if statement lets a program choose. You write the word if, then a condition, then a colon. The lines indented below run only when the condition is True. Think of a lifeguard flag. Green flag, you swim. Red flag, you stay out. Your program checks the condition, and then walks exactly one path. That is a decision.", "IF + CONDITION + :", "Your first decision."),
        ("Else is the other path", "If has a partner called else. Else runs when the condition is False. So the program always takes exactly one of the two paths, never both, never neither. Line else up under its if, put a colon after it, and indent the lines below. After both paths, the program carries on with the next line at the left edge. That line always runs.", "IF... ELSE...", "Two paths, one runs."),
        ("Test the edge", "Marks are thirty eight, and the pass mark is forty. Is marks greater than or equal to forty? No, so Python prints Try again. Always test the edge value. At exactly forty, the condition is True, and Pass prints. The difference between greater than and greater than or equal matters. Edges are where beginner programs most often go wrong, so check them.", "38 >= 40 ?", "Test the edge value."),
        ("Expected a colon", "A very common bug. You write the if line, and forget the colon at the end. Python says, syntax error, expected a colon, and the arrow points to the exact spot. The colon tells Python a block starts on the next line. Every if, else, and loop line needs one. Add the colon, and the program runs again.", "SYNTAXERROR: EXPECTED ':'", "Never forget the colon."),
        ("Pun and challenge", "Why did the program stand at the fork in the road? It had a lot of conditions to consider. Your challenge. Make price equal four fifty. Print Cheap if the price is below five hundred. Otherwise, print Expensive. Then try five hundred, and see what happens at the edge. Share your answer in the comments below.", "CHEAP OR EXPENSIVE?", "Try the decision."),
    ],
))

EPISODES.append(dict(
    n=14, title="elif ladders", spoken="elif ladders",
    yt="Python elif: Choose Between Many Options", thumb="THE ELIF LADDER",
    vis="Xecxec climbing a ladder whose rungs are labelled A, B, C and D",
    goals=["chain several conditions with elif", "know that Python stops at the first True condition", "put conditions in the right order"],
    tags=["python elif", "python if elif else", "grade calculator python", "condition order"],
    hash=["#elif", "#conditions"],
    analogy="a ladder: you start at the top rung and step down until one rung holds your weight",
    c_title="More than two paths",
    c_pts=["elif adds more conditions", "Python checks from the top", "The first True condition wins and the rest are skipped"],
    intro="Two paths are not always enough. Today we build a ladder of conditions, and learn why the order matters.",
    concept="Sometimes there are many paths. Grade A, B, C and D. Python handles them with elif, short for else if. It checks the conditions from the top. The first one that is True wins, and Python skips the rest. Think of a ladder. You start at the top rung and step down until one rung holds. Because the first True wins, the order of the rungs matters a lot.",
    A=dict(file="grade.py", label="A grade ladder", on="marks turned into a grade with elif",
           src='''
marks = 72
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:
    print("Grade D")
''',
           narr="[HL 1] Marks are seventy two. [HL 2] First rung. Is it ninety or more? No. [HL 3] So Grade A is skipped. [HL 4] Second rung. Seventy five or more? No, seventy two is smaller. [HL 5] Skipped. [HL 6] Third rung. Sixty or more? Yes. [HL 7] So Grade C prints. [HL 8] Python never looks at else. [HL 9] That last line is a safety net for everything below sixty.",
           label2="Reading the output", narr2="Predict first. [TRACK marks=72] Seventy two fails the first two rungs and passes the third. Only Grade C prints. Even though seventy two is also at least fifty, that rung is not checked, because the third rung already won. One path runs, always."),
    mem=dict(label="Names and the chosen price", on="Two tags, age and price, tied to an int each", names=["age", "price"], **{"from": "B"},
             narr="Look at the end state. Age is tied to the int sixty five. Price is tied to the int seventy. Only one of the four branches ran, and only that branch tied the name price to a value. If no branch had run, the name price would not exist at all. That is why we added a final else."),
    B=dict(file="ticket.py", label="A ticket price ladder", on="a ticket price chosen by age",
           src='''
age = 65
if age < 5:
    price = 0
elif age < 18:
    price = 50
elif age < 60:
    price = 100
else:
    price = 70
print("Ticket price:", price)
''',
           narr="[HL 1] [TRACK age=65] Age is sixty five. [HL 2] Under five? No. [HL 4] Under eighteen? No. [HL 6] Under sixty? No. [HL 8] Everything else lands in else, so the price is seventy, a senior discount. [HL 10] Print the chosen price. Notice that every branch ties the same name, price. That way the last line always has a price to print."),
    term="Ticket price, seventy.",
    recap=["elif adds more conditions after if.", "Python checks from the top and runs only the first True branch.", "Order matters: put the strictest condition first.", "A final else catches everything that is left."],
    bug=dict(title="conditions in the wrong order", kind="output", file="grade.py", wrong='''
marks = 95
if marks >= 60:
    print("Grade C")
elif marks >= 90:
    print("Grade A")
''', fixed='''
marks = 95
if marks >= 90:
    print("Grade A")
elif marks >= 60:
    print("Grade C")
''', wrong_note="the loosest condition comes first", fixed_note="strictest condition first",
             why="Python stops at the first True condition, so a loose test placed first hides every stricter test below it.",
             narr="Bug of the Day. Marks are ninety five, a perfect grade A. But the program prints Grade C. Why? The first rung is, sixty or more. Ninety five passes it, and Python stops right there. The ninety test is never reached. Put the strictest condition first, and work down to the loosest."),
    pun="Why did the elif ladder get a promotion? It was always one step ahead.",
    task="turn a temperature into Cold, Warm or Hot", challenge="Make temp = 24. Print Cold if below 15, Warm if below 30, and Hot otherwise.",
    answer="Use if temp < 15: Cold, elif temp < 30: Warm, else: Hot. With 24 it prints Warm.",
    shorts=[
        ("What is elif?", "Elif is short for else if. It lets you add more conditions after the first if. Python checks them from the top, and runs the first branch whose condition is True. Then it skips everything else in the ladder. So exactly one branch runs. Think of climbing down a ladder until a rung holds your weight. Use elif whenever you have three or more choices.", "IF · ELIF · ELSE", "A ladder of conditions."),
        ("First True wins", "Here is the golden rule of the elif ladder. Python stops at the first True condition. Marks are seventy two. Is it ninety or more? No. Seventy five or more? No. Sixty or more? Yes, so Grade C prints, and Python never looks at the rest. Only one branch runs, no matter how many conditions could be true. Remember this rule.", "FIRST TRUE WINS", "Only one branch runs."),
        ("The last else", "End your ladder with an else. It catches everything that no condition matched. Without it, a value that fails every test would run nothing at all, and later lines might use a name that was never created. A final else is your safety net. Even a simple message like, invalid input, is better than silence. Add one every time.", "ELSE = SAFETY NET", "Catch everything left."),
        ("Wrong order, wrong grade", "Here is a sneaky bug. Marks are ninety five, but the program prints Grade C. The first rung says, sixty or more. Ninety five passes that, so Python stops, and never reaches the ninety test. There is no error, only a wrong answer. Put the strictest condition first, and then work down to the loosest one. Test with a perfect score.", "95 → GRADE C ?!", "Order the rungs."),
        ("Pun and challenge", "Why did the elif ladder get a promotion? It was always one step ahead. Your challenge. Make temp equal twenty four. Print Cold if it is below fifteen. Print Warm if it is below thirty. Otherwise print Hot. Remember to put the strictest condition first. Then test fourteen, thirty, and forty. Post your code in the comments.", "COLD, WARM OR HOT?", "Try an elif ladder."),
    ],
))

EPISODES.append(dict(
    n=15, title="and, or, not and truthiness", spoken="and, or and not",
    yt="Python and, or, not: Combine Conditions", thumb="AND · OR · NOT",
    vis="Xecxec holding three switches labelled AND, OR and NOT",
    goals=["combine conditions with and, or and not", "write each comparison in full", "know which values count as False"],
    tags=["python and or not", "python logical operators", "python truthiness", "python boolean logic"],
    hash=["#logic", "#booleans"],
    analogy="a beach club entry: you need a ticket AND to be eighteen; a child OR a senior walks in free",
    c_title="Combining conditions",
    c_pts=["and needs both sides True", "or needs at least one side True", "not flips True and False"],
    intro="One condition is often not enough. Today we combine them, and meet the strange idea that a value can be false without being the word False.",
    concept="Three small words combine conditions. And is True only when both sides are True. Or is True when at least one side is True. Not flips the answer. Think of a beach club. To enter, you need a ticket and you need to be eighteen. A child or a senior citizen walks in free. Python also treats some values as false by themselves. Zero, an empty string, and None all count as False.",
    A=dict(file="gate.py", label="Combining two conditions", on="and, or and not on an age and a ticket",
           src='''
age = 20
has_ticket = True
if age >= 18 and has_ticket:
    print("Enter")
if age < 5 or age > 60:
    print("Free")
print(not has_ticket)
''',
           narr="[HL 1] Age twenty. [HL 2] A ticket, which is True. [HL 3] Both sides must be True. Age is at least eighteen, and the ticket is True, so the line is True. [HL 4] Enter prints. [HL 5] Or needs only one side. Age below five? No. Age above sixty? No. Both are False, so the line is False. [HL 6] So Free is skipped. [HL 7] Not flips the ticket. True becomes False.",
           label2="Reading the output", narr2="Predict first. [TRACK age=20] The first condition is True, so Enter prints. The second is False, so nothing prints. The last line prints False. Together, the output is Enter, then False. Three small words, and your conditions can say almost anything."),
    c2=dict(label="Truth table", on="A small truth table for and, or and not with rows for True and False, and a list of values that count as False: 0, empty string, None",
            narr="Here is the truth table. And is True only in one row, when both are True. Or is False only in one row, when both are False. Not simply flips. Python also has a short list of values that count as False by themselves. Zero, an empty string, an empty list, and None. Almost everything else counts as True.",
            anim="Table rows light up one by one; the False-values list slides in with a pop and each item gets a red cross"),
    B=dict(file="truthy.py", label="Truthiness", on="an empty name is false; bool() shows what Python thinks",
           src='''
name = ""
if name:
    print("Hello", name)
else:
    print("Name is empty")
print(bool(0), bool(1), bool("Goa"), bool(""))
''',
           narr="[HL 1] An empty string. [HL 2] An if with no comparison, just the name. Python asks, is this value truthy? An empty string is not. [HL 3] So Hello is skipped. [HL 4] Else runs. [HL 5] Name is empty prints. [HL 6] The bool function shows what Python thinks. Zero is False. One is True. The word Goa is True. An empty string is False."),
    term="Name is empty. Then False True True False.",
    recap=["and needs both sides True, or needs at least one.", "not flips True and False.", "Write each comparison in full on both sides of and or or.", "Zero, an empty string, an empty list and None count as False."],
    bug=dict(title="x equals one or two", kind="output", file="menu.py", wrong='''
choice = 3
if choice == 1 or 2:
    print("Valid")
else:
    print("Invalid")
''', fixed='''
choice = 3
if choice == 1 or choice == 2:
    print("Valid")
else:
    print("Invalid")
''', wrong_note="the second side is only the number 2", fixed_note="both sides are full comparisons",
             why="Python reads the wrong line as (choice == 1) or 2, and the number 2 is always truthy, so the whole condition is always True.",
             narr="Bug of the Day. Choice is three. We want to know if it is one or two. The program says Valid. Wrong! Python reads this as, choice equals one, or two. And the plain number two is always true. So the whole condition is always true. Write the comparison in full on both sides, choice equals one, or choice equals two, and it works."),
    pun="Why was the boolean so calm? It knew when to say and, and when to say or.",
    task="free entry if age under 5 or over 60", challenge="Make age = 4. Print Free if age is below 5 or above 60, otherwise print Pay.",
    answer="Use if age < 5 or age > 60: print(\"Free\") and else: print(\"Pay\"). With 4 it prints Free.",
    shorts=[
        ("And, or, not", "Three small words combine conditions. And is True only when both sides are True. Or is True when at least one side is True. Not flips the answer, so True becomes False. Think of a beach club. You need a ticket and an adult age to enter. A child or a senior citizen enters free. Combine conditions, and you can describe almost any rule.", "AND · OR · NOT", "Combine conditions."),
        ("Truth table", "Here is the whole truth table in one go. And is True in just one case, when both sides are True. Or is False in just one case, when both sides are False. Not flips whatever it gets. That is all there is to it. If you ever feel lost with a long condition, draw this table on paper, and test each part.", "AND: BOTH · OR: ONE", "The whole table."),
        ("Truthy and falsy", "Some values count as False without being the word False. Zero is False. An empty string is False. An empty list is False. And so is None. Almost everything else counts as True. So if name, with no comparison, means, is the name not empty? It is a very short, very Pythonic way to check that something has a value.", "0 · \"\" · [] · NONE = FALSE", "Falsy values."),
        ("One or two", "Here is a famous trap. You write if choice equals one or two. Python reads that as, choice equals one, or the plain number two. And the number two is always truthy. So the condition is always True, even when choice is three. Write the comparison in full on both sides of the or, and the trap disappears.", "== 1 OR 2 ?!", "Write both comparisons."),
        ("Pun and challenge", "Why was the boolean so calm? It knew when to say and, and when to say or. Your challenge. Make age equal four. Print Free if age is below five, or above sixty. Otherwise print Pay. Then test the ages five, sixty, and sixty one. Do the edges give the answers you expect? Tell us in the comments.", "FREE OR PAY?", "Try and, or, not."),
    ],
))

EPISODES.append(dict(
    n=16, title="while loops", spoken="while loops",
    yt="Python while Loop: Repeat Until It Stops", thumb="REPEAT, REPEAT",
    vis="Xecxec riding a merry-go-round of waves labelled while count <= 3",
    goals=["repeat code with while", "use a counter that changes inside the loop", "stop a loop with a condition that becomes False"],
    tags=["python while loop", "python loops", "infinite loop python", "loop counter"],
    hash=["#whileloop", "#loops"],
    analogy="a sea wave: it keeps coming in while the tide is up, and it stops when the tide goes out",
    c_title="Repeating with while",
    c_pts=["while checks a condition before every round", "The loop body repeats while it is True", "Something inside must change the condition"],
    intro="Computers never get bored. Today we teach a program to repeat itself, as many times as we say.",
    concept="A while loop repeats a block while a condition is True. Python checks the condition before every round. If it is True, the body runs again. If it is False, the loop ends and the program carries on. Think of waves on a beach. They keep coming in while the tide is up. For the loop to end, something inside the body must change the condition. Usually that is a counter that goes up.",
    A=dict(file="waves.py", label="A counting loop", on="a counter that goes from one to three",
           src='''
count = 1
while count <= 3:
    print("Wave", count)
    count = count + 1
print("Done")
''',
           narr="[HL 1] A counter, starting at one. [HL 2] The loop line. While count is at most three, run the block below. [HL 3] Print the wave number. [HL 4] And now the most important line. We add one to count. Without it, the condition would never change. [HL 5] Back at the left edge, so the loop is over. Done prints once, after the loop finishes.",
           label2="Reading the output", narr2="Predict first. [TRACK count=1] Round one, count is one, so Wave one prints. [TRACK count=2] Round two prints Wave two. [TRACK count=3] Round three prints Wave three. Then count becomes four, the condition is False, and the loop ends. The output is Wave one, Wave two, Wave three, Done."),
    mem=dict(label="One name, rebound each round", on="The name count tied to a new int every round; after the loop it points at 4", names=["count"], **{"from": "A"},
             narr="Here is the picture after the loop ends. The name count is tied to the int four. It was tied to one, then two, then three, and each time the tag moved to a new number. The condition count at most three is now False, which is why the loop stopped. The old numbers are gone, and the tag is on four."),
    B=dict(file="saving.py", label="Saving until a target", on="saving money week by week until it reaches 200",
           src='''
saving = 100
weeks = 0
while saving < 200:
    saving = saving + 30
    weeks = weeks + 1
print("Weeks:", weeks)
print("Saved:", saving)
''',
           narr="[HL 1] [TRACK saving=100] We start with one hundred rupees. [HL 2] [TRACK weeks=0] And zero weeks gone. [HL 3] Keep going while the savings are below two hundred. [HL 4] Add thirty each round. [HL 5] And count the week. [TRACK saving=220] After four rounds, the savings are two hundred twenty. That is not below two hundred, so the loop stops. [HL 6] Four weeks. [HL 7] Two hundred twenty saved."),
    term="Weeks, four. Saved, two hundred twenty.",
    recap=["while repeats a block as long as its condition is True.", "Python checks the condition before every round.", "Something inside the loop must change the condition.", "A counter that goes up is the most common way to end a loop."],
    bug=dict(title="forgetting to update the counter", kind="hang", file="waves.py", wrong='''
count = 1
while count <= 3:
    print("Wave", count)
print("Done")
''', fixed='''
count = 1
while count <= 3:
    print("Wave", count)
    count = count + 1
print("Done")
''', wrong_note="count never changes", fixed_note="count goes up each round",
             why="Nothing inside the loop changes count, so the condition stays True forever and the loop never ends.",
             narr="Bug of the Day. We forgot the line that adds one to count. Count stays at one forever. The condition is always True, so the loop never ends, and Wave one prints again and again. No error appears, because there is nothing wrong with the rules. Press control C to stop the program. Then add the update line, and the loop ends."),
    pun="Why did the while loop never get any sleep? It kept going round and round.",
    task="count from 1 to 5 with while", challenge="Use a while loop to print the numbers 1 to 5, one per line.",
    answer="Use n = 1, then while n <= 5: print(n) and n = n + 1. It prints 1 2 3 4 5, one per line.",
    shorts=[
        ("What is a loop?", "A loop repeats a block of code. The while loop repeats as long as its condition is True. Python checks the condition before every round. If it is True, the body runs again. If it is False, the loop ends and the program carries on. Think of waves that keep coming while the tide is up. Loops let one short program do a very big job.", "WHILE CONDITION:", "Repeat with while."),
        ("The counter", "Most while loops have a counter. You start it before the loop, check it in the condition, and change it inside the body. Count equals one. While count is at most three. Print, then add one. Each round the counter moves closer to the end. When it passes three, the condition is False, and the loop stops. Three parts, one loop.", "START · CHECK · CHANGE", "Three parts of a loop."),
        ("Watch the name move", "Watch the name count. It starts tied to one. After round one it is tied to two. After round two, three. After round three, four. Each time, the tag moves to a brand new number. When count is four, the condition at most three is False. So the loop ends. The loop just keeps retying the same name, until it is time to stop.", "COUNT: 1 → 2 → 3 → 4", "Follow the counter."),
        ("The loop that never ends", "Here is the classic loop bug. You forget the line that changes the counter. Count stays one, the condition stays True, and Wave one prints forever. Python shows no error, because the rules are fine. Press control C to stop the program. Then add the missing update line. Always ask, what makes this loop stop, before you press run?", "FORGOT COUNT = COUNT + 1", "Control C saves you."),
        ("Pun and challenge", "Why did the while loop never get any sleep? It kept going round and round. Your challenge. Use a while loop to print the numbers one to five, one per line. Remember the three parts. Start the counter, check it in the condition, and change it inside the loop. Then try printing five down to one. Post your code in the comments.", "COUNT 1 TO 5", "Try a while loop."),
    ],
))

EPISODES.append(dict(
    n=17, title="for loops and range", spoken="for loops and range",
    yt="Python for Loop and range() Explained", thumb="FOR + RANGE",
    vis="Xecxec walking along stepping stones numbered 0 to 4",
    goals=["repeat a fixed number of times with for", "use range(stop) and range(start, stop)", "remember that the stop value is not included"],
    tags=["python for loop", "python range function", "range start stop", "off by one error"],
    hash=["#forloop", "#range"],
    analogy="stepping stones across a stream: range gives you the stones, and for walks over each one",
    c_title="Looping a fixed number of times",
    c_pts=["for walks through a series of values", "range(5) gives 0, 1, 2, 3, 4", "The stop value is never included"],
    intro="When you know how many times to repeat, there is a tidier loop. Today we meet for, and its partner range.",
    concept="A for loop walks through a series of values, one at a time. The range function makes the series. Range of five gives zero, one, two, three, four. Five numbers, but it starts at zero, and the stop value is never included. Think of stepping stones across a stream. Range lays out the stones, and for steps on each one. Range of one, six gives one to five.",
    A=dict(file="steps.py", label="A simple for loop", on="range(5) and the loop variable i",
           src='''
for i in range(5):
    print("Step", i)
print("Finished")
''',
           narr="[HL 1] The for line has three parts. A loop name, i. The word in. And range of five. Python ties i to zero, runs the block, then ties it to one, and so on. [HL 2] The block prints the step number. Notice we never wrote i equals i plus one. The for loop does that for us. [HL 3] This line is at the left edge, so it runs once, after the loop ends.",
           label2="Reading the output", narr2="Predict first. [TRACK i=0] I starts at zero. [TRACK i=4] And ends at four. The output is Step zero, Step one, Step two, Step three, Step four, then Finished. Five lines, numbered zero to four. A very common surprise is that the numbers start at zero, not one."),
    mem=dict(label="The loop name after the loop", on="The name i tied to the last value, 4, after the loop ends", names=["i"], **{"from": "A"},
             narr="Here is a small surprise. After the loop ends, the name i is still there. It stays tied to the last value it received, four. The for loop made the name, and tied it to each value in turn. It does not tidy the name away when the loop finishes. That is normal Python, and it is useful to know."),
    B=dict(file="table.py", label="A times table", on="range(1, 6) with a start and a stop",
           src='''
for n in range(1, 6):
    print("5 x", n, "=", 5 * n)
''',
           narr="[HL 1] [TRACK n=1] Range with two numbers gives a start and a stop. Start at one, stop before six. So n takes the values one to five. [HL 2] Each round prints a line of the five times table. The sum inside print is worked out each time. [TRACK n=5] The last line is, five times five equals twenty five. A start and a stop is how you ask for exactly the numbers you want."),
    term="A five times table, from one up to five.",
    recap=["for walks through a series of values.", "range(5) gives 0, 1, 2, 3, 4.", "range(1, 6) gives 1 to 5, because the stop is not included.", "The for loop updates its own loop name, so you never add one yourself."],
    bug=dict(title="an off-by-one range", kind="output", file="table.py", wrong='''
for n in range(1, 5):
    print(n)
''', fixed='''
for n in range(1, 6):
    print(n)
''', wrong_note="we want 1 to 5", fixed_note="stop is one past the last number",
             why="range stops before its stop value, so to include 5 the stop must be 6.",
             narr="Bug of the Day. We want the numbers one to five. We wrote range of one, five. The output stops at four. Python does not include the stop value. Five is the stop, so it is left out. To include five, the stop must be six. This is called an off by one bug, and every programmer meets it."),
    pun="Why did the for loop go to the stream? It loved stepping on every stone.",
    task="print the even numbers 2 to 10", challenge="Print the numbers 1 to 10, one per line, using for and range.",
    answer="Use for n in range(1, 11): print(n). The stop is 11 so that 10 is included.",
    shorts=[
        ("What is range?", "The range function makes a series of numbers. Range of five gives zero, one, two, three, four. Five numbers, but it starts at zero. The stop value is never included. Think of stepping stones across a stream. Range lays out the stones, and a for loop steps on each one in turn. Whenever you know how many times to repeat, for and range are your friends.", "RANGE(5) = 0 TO 4", "Numbers to loop over."),
        ("Start and stop", "Range can take a start and a stop. Range of one, six gives one, two, three, four, five. It starts at one, and stops before six. So the last number is always one less than the stop. If you want one to ten, write range of one, eleven. Read it as, from one, up to but not including eleven.", "RANGE(1, 6) = 1 TO 5", "Stop is not included."),
        ("The loop name", "In a for loop, Python makes the loop name for you. For i in range of five. I is tied to zero, then one, then two, and so on. You never write i equals i plus one. The loop does it. After the loop ends, i is still there, tied to the last value, which is four. Handy to know when you debug.", "FOR I IN RANGE(5):", "Python moves i for you."),
        ("Off by one", "Here is the most famous bug in loops. You want the numbers one to five, so you write range of one, five. The output stops at four. Range does not include the stop value. To get five, the stop must be six. Programmers call this an off by one bug. Whenever a loop runs one time too few, check the stop value first.", "RANGE(1, 5) MISSES 5", "Check the stop value."),
        ("Pun and challenge", "Why did the for loop go to the stream? It loved stepping on every stone. Your challenge. Print the numbers one to ten, one per line, using for and range. Think about which stop value you need to include ten. Then change your loop to print only the numbers one to five. Share your answer in the comments below.", "PRINT 1 TO 10", "Try for and range."),
    ],
))

EPISODES.append(dict(
    n=18, title="break, continue and loop else", spoken="break, continue and loop else",
    yt="Python break, continue and Loop else", thumb="BREAK OR CONTINUE",
    vis="Xecxec holding a stop sign labelled BREAK and a skip arrow labelled CONTINUE",
    goals=["leave a loop early with break", "skip one round with continue", "use else on a loop for the no-break case"],
    tags=["python break", "python continue", "python loop else", "infinite loop continue"],
    hash=["#break", "#continue"],
    analogy="a bus journey: break gets off the bus now, continue skips this stop, and else means you reached the end",
    c_title="Control inside a loop",
    c_pts=["break leaves the loop now", "continue skips to the next round", "else runs only if the loop was never broken"],
    intro="Sometimes a loop should stop early, or skip a round. Today we meet three tools that give you more control.",
    concept="Inside a loop, three tools give you more control. Break leaves the loop at once. Continue skips the rest of this round, and goes to the next. And else, after the loop, runs only when the loop finished without a break. Think of a bus journey. Break means get off the bus right now. Continue means skip this stop. Else means you reached the last stop.",
    A=dict(file="stop_at.py", label="Leaving early with break", on="a loop that stops when n is 4",
           src='''
for n in range(1, 10):
    if n == 4:
        print("Stop at 4")
        break
    print("n is", n)
''',
           narr="[HL 1] A loop over one to nine. [HL 2] An if inside the loop. When n is four, [HL 3] we print a message, [HL 4] and break. Break ends the whole loop at once. [HL 5] For other values, this line prints. It is at the same level as the if, so it runs when the if does not.",
           label2="Reading the output", narr2="Predict first. [TRACK n=4] N is one, two, three, and each prints. Then n is four. The condition is True, so Stop at four prints, and break ends the loop. Five to nine never happen. Nine rounds were planned, but only four ran."),
    mem=dict(label="Where the loop name stops", on="After the break, the name n stays tied to 4", names=["n"], **{"from": "A"},
             narr="Here is what is left after the break. The name n is tied to the int four, the value it had when the loop was left. The loop never reached five. Compare that with a loop that finishes normally, where the name ends on the last value in the series. This is a handy way to see where a loop stopped."),
    B=dict(file="odds.py", label="continue and else", on="skip even numbers; else runs because there was no break",
           src='''
for n in range(1, 6):
    if n % 2 == 0:
        continue
    print("Odd:", n)
else:
    print("Loop finished without break")
''',
           narr="[HL 1] A loop over one to five. [HL 2] If n is even, remainder zero when divided by two, [HL 3] we continue. That skips the rest of this round. [HL 4] Odd numbers reach this line and print. [HL 5] Now the loop else. [HL 6] It runs only when the loop was not broken. Here there was no break, so it prints."),
    term="Odd, one. Odd, three. Odd, five. Then, Loop finished without break.",
    recap=["break leaves the loop immediately.", "continue skips the rest of the current round.", "A loop else runs only when the loop ended without a break.", "In a while loop, update the counter before you continue."],
    bug=dict(title="continue skips the update", kind="hang", file="count.py", wrong='''
n = 0
while n < 5:
    if n == 2:
        continue
    print(n)
    n = n + 1
''', fixed='''
n = 0
while n < 5:
    if n == 2:
        n = n + 1
        continue
    print(n)
    n = n + 1
''', wrong_note="continue jumps over n = n + 1", fixed_note="update before continue",
             why="continue jumps straight back to the condition, so a counter update placed after it is skipped and the loop never ends.",
             narr="Bug of the Day. We want to skip the number two. But when n is two, continue jumps back to the top, and skips the line that adds one. So n stays two forever, and the program hangs after printing zero and one. With a while loop, add one before you continue. Then the loop moves on."),
    pun="Why did the loop get off the bus early? It heard someone say break.",
    task="print 1 to 10 but stop at 7", challenge="Loop from 1 to 10 and print each number, but stop the loop when you reach 7.",
    answer="Use for n in range(1, 11): if n == 7: break, then print(n). It prints 1 to 6.",
    shorts=[
        ("Break", "Break leaves a loop immediately. Say you are searching for a number. The moment you find it, you do not need to keep looking. So you write break, and Python jumps out of the loop and carries on with the next line. Think of a bus journey. Break means, I am getting off right now. It makes searches faster and your code simpler.", "BREAK = LEAVE NOW", "Stop a loop early."),
        ("Continue", "Continue skips the rest of the current round, and goes straight to the next one. Say you only want to print odd numbers. When a number is even, you write continue. Python skips the print for that round, and moves on. It is like skipping a stop on a bus route. The bus keeps going, and only this stop is missed.", "CONTINUE = SKIP THIS ONE", "Skip one round."),
        ("Loop else", "Here is a very Python feature. A loop can have an else. It runs only when the loop finished without hitting a break. So if you search for something, and the loop ends normally, the else tells you that nothing was found. It is like reaching the last stop of the bus route. It is rare in other languages, but very handy here.", "FOR... ELSE", "Else runs without a break."),
        ("Continue and the counter", "A tricky bug. In a while loop, you write continue before the line that adds one to the counter. When the condition is met, continue jumps back to the top, and the counter never changes. The loop hangs on that value forever. The fix is to update the counter before you continue. Always check where your update line sits.", "CONTINUE SKIPS THE UPDATE", "Update first."),
        ("Pun and challenge", "Why did the loop get off the bus early? It heard someone say break. Your challenge. Loop from one to ten, and print each number. But stop the loop as soon as you reach seven, using break. You should see only the numbers one to six. Then change break to continue, and see what changes. Tell us what you notice.", "STOP AT 7", "Try break and continue."),
    ],
))

EPISODES.append(dict(
    n=19, title="Nested loops and patterns", spoken="nested loops and patterns",
    yt="Python Nested Loops and Star Patterns", thumb="LOOPS IN LOOPS",
    vis="Xecxec drawing a triangle of stars with his claw",
    goals=["put one loop inside another", "follow how the inner loop restarts every round", "print patterns on one line with end="],
    tags=["python nested loops", "python star pattern", "python print end", "pattern programs python"],
    hash=["#nestedloops", "#patterns"],
    analogy="a clock: the minute hand does a full circle for every single step of the hour hand",
    c_title="A loop inside a loop",
    c_pts=["The outer loop runs once per round", "The inner loop runs fully each round", "print adds a newline unless you set end"],
    intro="One loop is good. A loop inside a loop is powerful. Today we draw patterns with nested loops.",
    concept="A nested loop is a loop inside a loop. The outer loop takes one step. Then the inner loop runs all the way through. Then the outer loop takes its next step, and the inner loop starts again from the beginning. Think of a clock. The minute hand does a full circle for each step of the hour hand. Nested loops are how programs draw grids and patterns.",
    A=dict(file="grid.py", label="Two loops, six lines", on="rows and columns printed as pairs",
           src='''
for row in range(1, 3):
    for col in range(1, 4):
        print("row", row, "col", col)
''',
           narr="[HL 1] The outer loop gives two rows. [HL 2] The inner loop gives three columns, and it is indented inside the outer loop. [HL 3] This line is inside both loops, so it runs two times three, six times. Watch the order. Row one runs with columns one, two, three. Only then does row two begin.",
           label2="Reading the output", narr2="Predict first. [TRACK row=1] Row one, column one. Row one, column two. Row one, column three. [TRACK row=2] Then row two, column one, two, three. Six lines in all. The inner loop starts again from column one, every time the outer loop moves."),
    c2=dict(label="Rows and columns", on="A 2 by 3 grid; a highlight sweeps column one to three along row one, then restarts along row two",
            narr="Picture a grid with two rows and three columns. The highlight walks across row one, one column at a time. When the row is finished, it jumps to row two, and walks the columns again, starting at column one. That restart is the key idea. The inner loop begins fresh every time the outer loop takes a step.",
            anim="A grid of cells; a butter highlight sweeps each row left to right with a tick per cell, then drops to the next row"),
    B=dict(file="triangle.py", label="A star triangle", on="print stars on one line with end",
           src='''
for row in range(1, 5):
    for col in range(row):
        print("*", end="")
    print()
''',
           narr="[HL 1] Four rows. [HL 2] The inner loop runs row times. Row one gives one star. Row two gives two. [HL 3] Print with end equal to empty quotes. Normally print finishes with a new line. Here we ask it to add nothing, so the stars stay on the same line. [HL 4] An empty print at the outer level adds one new line, after each row of stars is complete."),
    term="A triangle of stars: one, two, three, four stars in each row.",
    recap=["The inner loop runs fully for every step of the outer loop.", "Indent the inner loop inside the outer loop.", "print ends with a new line unless you set end.", "An empty print() starts the next line."],
    bug=dict(title="print adds a new line", kind="output", file="triangle.py", wrong='''
for row in range(1, 4):
    for col in range(row):
        print("*")
    print()
''', fixed='''
for row in range(1, 4):
    for col in range(row):
        print("*", end="")
    print()
''', wrong_note="the stars are on separate lines", fixed_note="end is empty so stars stay together",
             why="print ends every call with a new line by default, so stars printed one per call land on separate lines unless end is set to an empty string.",
             narr="Bug of the Day. We wanted a triangle. We got a long column of stars, with blank lines in between. Print adds a new line after every call, even inside the inner loop. Tell print to add nothing, with end equal to empty quotes. Then the stars of a row stay together, and the empty print starts the next row."),
    pun="Why did the nested loop get dizzy? It kept going round in circles inside circles.",
    task="print a square of 3 by 3 stars", challenge="Print a 3 by 3 square of stars, three stars in each of three rows.",
    answer="Use for row in range(3): for col in range(3): print(\"*\", end=\"\") then print(). It prints ***, three times.",
    shorts=[
        ("A loop in a loop", "A nested loop is a loop inside a loop. The outer loop takes one step. Then the inner loop runs all the way through. Then the outer loop takes the next step, and the inner loop begins again. It is like a clock. The minute hand makes a full circle for every step of the hour hand. Nested loops draw grids and patterns.", "LOOP IN A LOOP", "Nested loops explained."),
        ("Count the lines", "Here is a quick way to count. An outer loop of two, and an inner loop of three. The inner line runs two times three, which is six times. Row one runs columns one, two, three. Then row two runs the columns again, from one. So always multiply the two loop sizes, and you will know exactly how many lines to expect.", "2 × 3 = 6 LINES", "Multiply the loops."),
        ("Stay on one line", "Normally print adds a new line at the end. To keep printing on the same line, add end equal to empty quotes. The stars of one row now stay together. Then an empty print call, at the end of each row, adds the new line. That is the secret of every pattern program. Stars on a row, then a new line.", "PRINT(\"*\", END=\"\")", "Use end."),
        ("A column of stars", "Here is the bug every pattern beginner meets. You want a triangle, but you get a tall column of stars. Print adds a new line after every call, so each star lands on its own line. Fix it by adding end equal to empty quotes to the inner print. Then the rows of stars stay together, and the empty print starts each new row.", "A COLUMN, NOT A TRIANGLE", "Set end."),
        ("Pun and challenge", "Why did the nested loop get dizzy? It kept going round in circles inside circles. Your challenge. Print a square of stars, three stars across, and three rows down. You will need an outer loop for the rows, and an inner loop for the stars. Remember end equal to empty quotes, and an empty print to start a new row. Post your pattern below.", "A 3 BY 3 SQUARE", "Try a star square."),
    ],
))

EPISODES.append(dict(
    n=20, title="The match statement", spoken="the match statement",
    yt="Python match and case Explained", thumb="MATCH AND CASE",
    vis="Xecxec at a restaurant counter holding a menu with numbered dishes",
    goals=["choose between exact values with match and case", "combine values with the | symbol", "add case _ as the catch-all"],
    tags=["python match case", "python 3.10 match", "switch statement python", "case underscore"],
    hash=["#match", "#python313"],
    analogy="a restaurant menu: you say the dish number, and the kitchen picks the matching dish",
    c_title="Match and case",
    c_pts=["match looks at one value", "Each case is a pattern to compare with", "case _ catches everything else"],
    intro="When one value can be one of many exact options, an elif ladder gets long. Today we meet a tidier tool, match.",
    concept="The match statement looks at one value, and compares it with a list of cases. The first case that fits runs. Think of a restaurant menu. You say the dish number, and the kitchen picks the matching dish. You can join several values with a vertical bar, meaning, or. And case underscore is the catch-all. It matches anything that nothing else matched. It needs Python three ten or newer.",
    A=dict(file="menu.py", label="A menu with match", on="a dish number matched to a dish",
           src='''
choice = 2
match choice:
    case 1:
        print("Fish curry")
    case 2:
        print("Prawn rice")
    case _:
        print("Not on the menu")
''',
           narr="[HL 1] Choice is two. [HL 2] Match looks at the value of choice. [HL 3] Case one compares. Not a match. [HL 4] Skipped. [HL 5] Case two matches. [HL 6] So Prawn rice prints. [HL 7] Case underscore is the catch-all. It would match any other number. [HL 8] Not on the menu would print for it. Match stops at the first case that fits.",
           label2="Reading the output", narr2="Predict first. [TRACK choice=2] Choice is two, so case two matches. Only Prawn rice prints. Change choice to nine, and no numbered case fits, so the catch-all runs, and Not on the menu prints. Always end a match with the catch-all."),
    mem=dict(label="The value being matched", on="The name choice tied to the int 2", names=["choice"], **{"from": "A"},
             narr="Match does not change anything in memory. The name choice stays tied to the int two. Match only looks at the object, and compares it with each pattern in order. Nothing is created and nothing is tied by the cases here. It works just like an elif ladder with double equals, but it reads better."),
    B=dict(file="day.py", label="Combine cases with a bar", on="Sat or Sun is Weekend",
           src='''
day = "Sat"
match day:
    case "Sat" | "Sun":
        print("Weekend")
    case _:
        print("Weekday")
''',
           narr="[HL 1] [TRACK day=Sat] The day is the text Sat. [HL 2] Match the day. [HL 3] One case can hold several patterns joined with a vertical bar. Read it as, Sat or Sun. [HL 4] Weekend prints. [HL 5] The catch-all for every other day. [HL 6] Weekday. With one case instead of two, the program is shorter and clearer."),
    term="Weekend.",
    recap=["match compares one value with a list of cases.", "The first matching case runs and the rest are skipped.", "A vertical bar joins several patterns in one case.", "case _ catches everything that nothing else matched."],
    bug=dict(title="no case underscore", kind="output", file="command.py", wrong='''
command = "jump"
match command:
    case "start":
        print("Starting")
    case "stop":
        print("Stopping")
''', fixed='''
command = "jump"
match command:
    case "start":
        print("Starting")
    case "stop":
        print("Stopping")
    case _:
        print("Unknown command")
''', wrong_note="the command jump has no case", fixed_note="a catch-all case added",
             why="If no case fits and there is no case _, match does nothing and gives no error, so a wrong input fails silently.",
             narr="Bug of the Day. The command is jump. No case matches it. And there is no catch-all. So match does nothing at all. No error, no message, just silence. Silent failures are the hardest to find. Add case underscore at the end, with a friendly message, and unknown commands are handled."),
    pun="Why did the match statement win every game? It always found its pair.",
    task="print a day name for a number", challenge="Make day = 3. Use match to print Monday for 1, Tuesday for 2, Wednesday for 3, and Unknown for anything else.",
    answer="Use match day with case 1, case 2, case 3, and case _. With 3 it prints Wednesday.",
    shorts=[
        ("What is match?", "Match is a tidy way to choose between exact values. You write match, then a value. Below it, each case shows a pattern to compare with. The first case that fits runs, and the others are skipped. Think of a restaurant menu. You say the dish number, and the kitchen picks the dish. It needs Python three ten or newer, and it reads like a menu.", "MATCH · CASE", "A menu for your code."),
        ("The catch-all", "Case underscore is the catch-all. It matches any value that no earlier case matched. Put it last. Without it, a value that fits no case will do nothing at all, silently. With it, you can print a friendly message, such as, not on the menu. Every match statement should end with a catch-all, just as every elif ladder should end with an else.", "CASE _ = ANYTHING ELSE", "End with case underscore."),
        ("Or inside a case", "A case can match several values at once. Join them with a vertical bar, which reads as or. Case Sat bar Sun matches both weekend days. So one case does the work of two. Your program gets shorter and easier to read. Use the bar whenever several values should give the same result, and avoid repeating yourself.", "CASE \"SAT\" | \"SUN\"", "One case, many values."),
        ("Silent failure", "A tricky bug. You match a command, but the command is not in your list, and you forgot the catch-all. Python does nothing. No error, no message, just silence. Silent failures are the hardest bugs to find. The fix is easy. Add case underscore at the end, with a friendly message. Always plan for unexpected input, from real users.", "NO CASE _, NO MESSAGE", "Plan for the unexpected."),
        ("Pun and challenge", "Why did the match statement win every game? It always found its pair. Your challenge. Make day equal three. Use match to print Monday for one, Tuesday for two, and Wednesday for three. Anything else should print Unknown. Then change day to nine, and check that the catch-all works. Post your code in the comments, please.", "NUMBER TO DAY NAME", "Try match and case."),
    ],
))

EPISODES.append(dict(
    n=21, title="Loop patterns", spoken="loop patterns",
    yt="Python Loop Patterns: Accumulator, Counter, Flag", thumb="3 LOOP PATTERNS",
    vis="Xecxec with three jars labelled TOTAL, COUNT and FOUND",
    goals=["build a running total with an accumulator", "count matching items with a counter", "remember a result with a flag"],
    tags=["python accumulator", "python loop patterns", "python counter flag", "running total python"],
    hash=["#looppatterns", "#accumulator"],
    analogy="a shop till: the running total grows with every item, the counter counts items, and the flag lights up when a special item is scanned",
    c_title="Three loop patterns",
    c_pts=["Accumulator: add to a total each round", "Counter: add one when a test passes", "Flag: set True when something is found"],
    intro="Most loops do one of three jobs. Today we name them, so you can recognise them everywhere.",
    concept="Three patterns appear again and again. The accumulator builds a running total, adding to it each round. The counter counts how many items pass a test. The flag starts as False, and becomes True if something special is found. Think of a shop till. The running total grows with each item. The counter counts the items. And a flag lights up if one special item is scanned.",
    A=dict(file="total.py", label="The accumulator", on="a running total of 1 to 5",
           src='''
total = 0
for n in range(1, 6):
    total = total + n
print("Sum:", total)
''',
           narr="[HL 1] Start the total at zero, before the loop. [HL 2] A loop over one to five. [HL 3] Each round adds n to the total. Total becomes total plus n. [HL 4] After the loop, print the final total. The key rule is that the starting line sits outside the loop. If it was inside, the total would be reset every round.",
           label2="Reading the output", narr2="Predict first. [TRACK total=1] After round one, the total is one. [TRACK total=3] After round two, three. [TRACK total=15] And after round five, fifteen. One plus two plus three plus four plus five. The output is Sum, fifteen."),
    mem=dict(label="The total grows by rebinding", on="The name total tied to the int 15 after the loop", names=["total", "n"], **{"from": "A"},
             narr="Here is the end state. Total is tied to the int fifteen. N is tied to five, the last value in the loop. During the loop, total moved from zero to one, three, six, ten, and fifteen. Each addition made a brand new int, and the tag total moved to it. The accumulator pattern is simply, make a new total from the old one."),
    B=dict(file="count_flag.py", label="A counter and a flag", on="count multiples of 3 in 1 to 20; flag if 15 is seen",
           src='''
count = 0
found = False
for n in range(1, 21):
    if n % 3 == 0:
        count = count + 1
    if n == 15:
        found = True
print("Multiples of 3:", count)
print("Saw 15:", found)
''',
           narr="[HL 1] A counter, starting at zero. [HL 2] A flag, starting as False. [HL 3] A loop over one to twenty. [HL 4] If n divides by three with no remainder, [HL 5] the counter goes up by one. [HL 6] A second check. If n is fifteen, [HL 7] the flag turns to True. [TRACK found=True] Once True, it stays True. [HL 8] Six multiples of three. [HL 9] And the flag says, fifteen was seen."),
    term="Multiples of three, six. Saw fifteen, True.",
    recap=["An accumulator builds a total by adding in each round.", "A counter adds one whenever a test passes.", "A flag starts False and is set True when something is found.", "Start each of them before the loop, never inside it."],
    bug=dict(title="resetting the total inside the loop", kind="output", file="total.py", wrong='''
for n in range(1, 4):
    total = 0
    total = total + n
print(total)
''', fixed='''
total = 0
for n in range(1, 4):
    total = total + n
print(total)
''', wrong_note="total is reset every round", fixed_note="total starts before the loop",
             why="Setting total to zero inside the loop wipes the running total at the start of every round, so only the last number survives.",
             narr="Bug of the Day. We add one, two and three, and expect six. The program prints three. Why? The line total equals zero is inside the loop, so every round wipes the total clean. Only the last number is left. Move the starting line above the loop, and the total can grow. No error appears, so watch for this one."),
    pun="Why did the accumulator get rich? It never stopped adding up.",
    task="sum the even numbers 2 to 10", challenge="Use a loop to add up the numbers 1 to 10 and print the total.",
    answer="Use total = 0, then for n in range(1, 11): total = total + n, then print(total). It prints 55.",
    shorts=[
        ("The accumulator", "The accumulator is the most useful loop pattern. You start a total at zero, before the loop. Inside the loop, you add to it every round. When the loop ends, the total holds the answer. One plus two plus three plus four plus five gives fifteen. Remember the rule, the starting line goes outside the loop, never inside.", "TOTAL = TOTAL + N", "Add up in a loop."),
        ("The counter", "A counter counts how many items pass a test. Start the count at zero. Inside the loop, test each item. If it passes, add one to the count. At the end, the count tells you how many passed. For example, how many numbers up to twenty divide evenly by three? A counter says six. It is the pattern behind every, how many, question.", "COUNT = COUNT + 1", "Count the matches."),
        ("The flag", "A flag is a name that starts as False. Inside the loop, you set it to True if you find something special. Once True, it stays True. After the loop, you check the flag, and you know whether anything was found. Think of a till light that turns on when a special item is scanned. Flags answer, was there any, questions.", "FOUND = FALSE → TRUE", "Remember what you saw."),
        ("Reset trap", "Here is the bug behind many wrong totals. You put the line total equals zero inside the loop. Now every round wipes the total clean, and only the last number is left. Python shows no error. You just get the wrong answer. Move the starting line above the loop, and the total can grow properly. Check this first when a sum looks too small.", "TOTAL = 0 INSIDE THE LOOP?", "Start outside."),
        ("Pun and challenge", "Why did the accumulator get rich? It never stopped adding up. Your challenge. Use a loop to add up the numbers one to ten, and print the total. Start your total before the loop. When you finish, change your code so it adds only the even numbers. Which total do you get? Share your answers in the comments.", "SUM 1 TO 10", "Try the accumulator."),
    ],
))

EPISODES.append(dict(
    n=22, title="Mini project: Guess the number", spoken="the guess the number mini project",
    yt="Python Mini Project: Guess the Number Game", thumb="GUESS THE NUMBER",
    vis="Xecxec holding a question mark card between two arrows labelled HIGH and LOW",
    goals=["build a complete game with a loop and decisions", "use random.randint with a seed", "read a number from the user safely with int()"],
    tags=["python guess the number", "python mini project", "python random randint", "python beginner game"],
    hash=["#project", "#game"],
    analogy="a market game: the stall owner thinks of a number, and says higher or lower until you win",
    c_title="Planning the game",
    c_pts=["The computer picks a secret number", "The player guesses, and gets Too low or Too high", "The loop ends when the guess is right"],
    intro="Time for our first real project. Today we combine input, decisions and loops, to build a number guessing game.",
    concept="Here is the plan. The computer picks a secret number between one and ten. The player guesses. The program says Too low or Too high, until the guess is right. That uses everything from this module. A loop that repeats, decisions with if, elif and else, and a counter for the number of tries. To get the secret number, we borrow a ready-made tool called random.",
    A=dict(file="guess.py", label="The full game", on="the complete guessing game",
           src='''
import random
random.seed(4)
secret = random.randint(1, 10)
tries = 0
while True:
    guess = int(input("Guess 1-10: "))
    tries = tries + 1
    if guess < secret:
        print("Too low")
    elif guess > secret:
        print("Too high")
    else:
        print("Correct in", tries, "tries")
        break
''',
           stdin="7\n2\n4\n",
           narr="[HL 1] Import brings in the random tool. [HL 2] The seed makes the random choice repeatable, so our video matches your screen. Without it, the number would change every run. [HL 3] A secret number from one to ten. [HL 4] The tries counter. [HL 5] While True means, loop forever, until we break. [HL 6] Ask for a guess, and convert it with int. [HL 7] Count the try. [HL 8] If the guess is too small, [HL 9] say Too low. [HL 10] If it is too big, [HL 11] say Too high. [HL 12] Otherwise it must be right, [HL 13] so print the tries, [HL 14] and break out of the loop.",
           label2="Reading the output", narr2="Predict first. [TRACK secret=4] The secret is four. The player guesses seven. That is Too high. Then two, Too low. Then four. Correct in three tries. Each loop round asked one question, and moved the player closer to the answer."),
    c2=dict(label="The game flow", on="A flowchart of the game: pick secret, ask guess, compare three ways, loop back until Correct",
            narr="Here is the whole game as a flow. Pick a secret. Ask for a guess. Compare it three ways, too low, too high, or right. If it is not right, loop back and ask again. If it is right, print the result and break out. Draw a flow like this before you write any game, and the code almost writes itself.",
            anim=FLOW),
    B=dict(file="dice.py", label="Seeds make random repeatable", on="the same seed gives the same numbers",
           src='''
import random
random.seed(4)
print(random.randint(1, 10))
print(random.randint(1, 10))
''',
           narr="[HL 1] Bring in the random tool. [HL 2] Set the seed to four. [HL 3] The first random number from one to ten. [HL 4] And the second. With the same seed, you get the same numbers, every single time. Remove the seed line, and the numbers change on every run, just like a real game. We use the seed here only so our checks are repeatable."),
    term="Four, then five. The same two numbers every run, because of the seed.",
    recap=["random.randint picks a whole number between two limits, including both.", "A while True loop runs until a break.", "if, elif and else give Too low, Too high or Correct.", "int() turns the typed text into a number before comparing."],
    bug=dict(title="comparing text with a number", file="guess.py", wrong='''
secret = 7
guess = input("Guess: ")
if guess > secret:
    print("Too high")
''', stdin="5\n", fixed='''
secret = 7
guess = int(input("Guess: "))
if guess > secret:
    print("Too high")
''', wrong_note="guess is still text", fixed_note="guess converted with int",
             why="input gives a string and a string cannot be compared with a number using greater than; convert the answer with int() first.",
             narr="Bug of the Day. We compare the guess with the secret, but the guess is still text. Python says, type error. Greater than is not supported between a string and an int. Remember, input always gives text. Wrap the answer in int, and now both sides are numbers. Then the comparison works."),
    pun="Why did the guessing game never get lonely? It always had a number in mind.",
    task="add a Too many tries rule", challenge="Change the game so the player loses after 5 wrong guesses, and prints the secret number.",
    answer="Add if tries == 5 inside the wrong-guess branches, print the secret, and break. A while tries < 5 loop with an else also works.",
    shorts=[
        ("The game plan", "Let us build a game. The computer picks a secret number. The player guesses. The program says Too low or Too high, until the guess is right. You need a loop that repeats, decisions with if and else, and a counter for the tries. Everything from this module comes together. Plan the flow on paper first, and the code will follow easily.", "GUESS THE NUMBER", "Our first project."),
        ("Random numbers", "To pick a secret number, import the random tool. Then random dot randint, one comma ten, gives a whole number from one to ten, and both ends are included. Set a seed first, and the same number comes up every run, which is great for testing. Remove the seed line, and the number changes every time, just like a real game.", "RANDOM.RANDINT(1, 10)", "Pick a secret."),
        ("While true", "The game loop is while True. That means, loop forever, until we say stop. Inside, we ask for a guess, compare it, and print a hint. When the guess is right, we print the result and use break. Break is the only way out. This pattern, loop forever and break when done, is very common in games and menus.", "WHILE TRUE: ... BREAK", "Loop until you win."),
        ("Text versus number", "Here is the bug that breaks every first guessing game. You compare the guess with the secret, but the guess came from input, so it is text. Python says type error, greater than is not supported between a string and an int. Wrap the input in int, and both sides are numbers. Now the comparison works as you expect.", "TYPEERROR: STR > INT", "Convert with int."),
        ("Pun and challenge", "Why did the guessing game never get lonely? It always had a number in mind. Your challenge. Make the game fairer. Let the player lose after five wrong guesses. When that happens, print the secret number, and stop the loop. You can use the tries counter you already have. Share your improved game in the comments below.", "FIVE GUESSES ONLY", "Improve the game."),
    ],
))
