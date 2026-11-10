# Module 1 — Variables, types and input

Episodes 5–12 · Pastel Blue + Tomato · Python 3.13

## EP 05 — Variables and names

**Module 1 · Variables, types and input · 5:17 · Pastel Blue + Tomato · Prerequisite: EP 04**

**Learning goals:** create a variable with = and give it a good name; explain that a name is a tag tied to a value; see that changing fish later does not change total.

### YouTube

- **Title:** Variables and Names in Python | Python Programming EP 05
- **Description:** Learn what a variable really is in Python, and why changing one name does not change another, with Xecxec the crab. 0:00 Intro · 0:20 What is a variable? · 1:00 Make three names · 1:40 Tags on values · 2:20 Follow the values · 3:00 Run it · 3:20 Recap · 3:55 Bug of the Day · 4:42 Challenge · 5:02 Next episode
- **Tags:** python variables, python for beginners, python tutorial, assignment in python, python names, nameerror, koding konkani, learn programming, class 11 computer science, coding in goa
- **Thumbnail:** big text "VARIABLES" in tomato on pastel blue; Xecxec holding two name tags tied to the numbers 3 and 120; thin black border and drop shadow.

### Scene list

| # | Start | Length | Template | On screen | Animation & SFX |
| --- | --- | --- | --- | --- | --- |
| 1 | 0:00 | 0:20 | Title card | EP 05 · VARIABLES | Tomato title card: EP sticker thuds in, title stamps with a whoosh, Xecxec scuttles in and waves; thud, whoosh, claw-click, sting |
| 2 | 0:20 | 0:40 | Concept slide | "What is a variable?": three numbered lines and a name-tag analogy card | Lines spring in one by one with a pop; the name-tag card slides in from the right |
| 3 | 1:00 | 0:40 | Code explain | `variables.py`: five assignments, then two prints; line 4 is the star | Code types in with key-tick; butter [HL n] highlight sweeps line by line with marker-swipe; explanation card on the right |
| 4 | 1:40 | 0:40 | Memory boxes | Three name tags, fish, price and total, tied by arrows to the values 3, 120 and 360 | Three tags pop in with arrows to the values; the fish arrow later swings from 3 to 5 while the total arrow stays on 360 |
| 5 | 2:20 | 0:40 | Code explain | `variables.py` again with the output panel on the right | Same code; the output panel fills line by line with a ding per output line; [TRACK] cards update |
| 6 | 3:00 | 0:20 | Terminal | Terminal: `python variables.py` | Dark-blue terminal: the command types with key-tick, output prints in mint with a ding |
| 7 | 3:20 | 0:35 | Concept slide | Recap: four ideas on one card | Four recap lines tick in one by one with a pop; Xecxec nods after each tick |
| 8 | 3:55 | 0:40 | Bug of the Day | BUG OF THE DAY: using a name before it exists | Butter banner drops in with a buzzer; wrong code shakes; the Python error lines appear in tomato; the fix slides in and the terminal turns mint with a ding |
| 9 | 4:35 | 0:07 | Pun card | My variable and I broke up. I assigned it a new value. | Full tomato screen, card flips in with a rimshot, Xecxec snaps his claw |
| 10 | 4:42 | 0:20 | Challenge | Task card: swap two variables without losing a value | Task card pops in; checklist ticks with a pop; Xecxec holds a tiny pen |
| 11 | 5:02 | 0:15 | Outro | Next: EP 06 · Numbers: int and float | Next-episode card slides up with a whoosh; right side stays empty for end-screen elements; sign-off text types in |

### Narration script

**[1 · Title]** Welcome back to Koding Konkani! Module one starts today. Every program needs to remember things, like a score or a price. Today we learn how Python remembers, using variables.

**[2 · What is a variable]** A variable is a name for a value. You write the name, an equals sign, and the value. Python stores the value, and ties the name to it, like a tag on a fish crate. Equals here does not mean the same as in maths. It means, tie this name to that value. Pick names that say what they hold, like fish and price, not x and y.

**[3 · Make three names]** [HL 2] [TRACK fish=3] The name fish is tied to three. [HL 3] [TRACK price=120] The name price is tied to one hundred twenty. [HL 4] [TRACK total=360] Now Python works out fish times price, which is three hundred sixty, and ties total to it. The right side is worked out first, and then the name is tied. Python works out the number once, right there. It does not remember the formula.

**[4 · Tags on values]** Look at the picture. Fish points at three. Price points at one hundred twenty. Total points at three hundred sixty. When you write fish equals five, Python moves only the fish arrow. It now points at five. The total arrow stays on three hundred sixty, because that number was worked out earlier. A name is a tag, and tags can be moved to other values.

**[5 · Follow the values]** [HL 5] [TRACK fish=5] Line five ties fish to a new value, five. [HL 4] Line four does not run again. So total is still three hundred sixty. [HL 6] The first print shows, Total, three hundred sixty. [HL 7] The second print shows, Fish now, five. Predict before you run. If total changed with fish, it would be six hundred. It does not. Python runs lines once, in order.

**[6 · Run it]** Run it. Total, three hundred sixty. Fish now, five. Total did not follow fish. Change the price and run it again, and see which numbers move.

**[7 · Recap]** Recap time. One: a variable is a name tied to a value, and equals does the tying. Two: Python works out the right side first, once, and does not remember the formula. Three: changing fish moves only the fish tag. Four: create a name before you use it. Say these four ideas out loud, then try changing price and predicting the new total.

**[8 · Bug of the Day]** Bug of the Day. We print total on line one, before we tie it to a value on line two. Python says, name error, name total is not defined. Python reads from the top, and at line one, total does not exist yet. Swap the two lines, and it works. Always create a name before you use it.

**[9 · Pun]** My variable and I broke up. I assigned it a new value.

**[10 · Challenge]** Your challenge: make two variables, a equals one and b equals two, and swap them. After the swap, a is two and b is one. Comment your answer below.

**[11 · Outro]** Next time: numbers, whole and decimal. Keep coding, says Xecxec!

### Code shown

File 1: `variables.py` (scene 3, 5)

```python
# Xecxec keeps score
fish = 3
price = 120
total = fish * price
fish = 5
print("Total:", total)
print("Fish now:", fish)
```

**Expected output:**

```text
Total: 360
Fish now: 5
```

### Bug of the Day

Wrong code (total is printed on line 1, before it is created on line 2):

```python
print("Total:", total)
total = 360
```

Python output:

```text
Traceback (most recent call last):
  File "vb.py", line 1, in <module>
    print("Total:", total)
                    ^^^^^
NameError: name 'total' is not defined
```

Fixed code (the lines are swapped):

```python
total = 360
print("Total:", total)
```

**Why:** Python runs top to bottom, so a name must be tied to a value before any line uses it.

### Pun & challenge

- **Pun:** "My variable and I broke up. I assigned it a new value."
- **Challenge:** Make a = 1 and b = 2, then swap them so that a is 2 and b is 1.
- **Challenge answer:** Use a third name: temp = a, then a = b, then b = temp; or in one line, a, b = b, a. Both give a = 2 and b = 1.

### Shorts for EP 05

**S1 · What is a variable?** — 0:20 · built from scene 2

- **Hook (first 1.5s):** "A name tied to a value."
- **Script:** A name tied to a value. Write the name, an equals sign, and the value. Python stores the value and ties the name to it, like a tag on a fish crate.
- **On-screen text:** VARIABLE = NAME + VALUE
- **Caption + hashtags:** Variables in 30 seconds. #python #variables #beginners #kodingkonkani #goa

**S2 · Equals is not maths** — 0:20 · built from scene 3

- **Hook (first 1.5s):** "Equals does not mean equal."
- **Script:** Equals does not mean equal. It means, tie this name to that value. Python works out the right side first, then ties the name on the left.
- **On-screen text:** = MEANS TIE THE NAME
- **Caption + hashtags:** What equals really means. #python #assignment #learntocode #kodingkonkani #coding

**S3 · Names are movable tags** — 0:20 · built from scene 4

- **Hook (first 1.5s):** "Move the tag, not the number."
- **Script:** Move the tag, not the number. Fish points at three. Say fish equals five, and the tag swings to five. The total tag stays where it was.
- **On-screen text:** FISH MOVES, TOTAL STAYS
- **Caption + hashtags:** Names are tags. #python #memory #variables #kodingkonkani #coding

**S4 · Name is not defined** — 0:20 · built from scene 8

- **Hook (first 1.5s):** "Use a name before it exists."
- **Script:** Use a name before it exists, and Python says, name error, name total is not defined. Python reads from the top, so create the name first.
- **On-screen text:** NAMEERROR: NAME NOT DEFINED
- **Caption + hashtags:** Create it before you use it. #python #bugfix #nameerror #kodingkonkani #coding

**S5 · Pun and challenge** — 0:20 · built from scenes 9, 10

- **Hook (first 1.5s):** "My variable and I broke up."
- **Script:** My variable and I broke up. I assigned it a new value. Your challenge: swap two variables, a and b, without losing a value. Full video: EP 5.
- **On-screen text:** SWAP A AND B
- **Caption + hashtags:** Try the swap challenge. #python #codingchallenge #kodingkonkani #programmingjokes #goa

## EP 06 — Numbers: int and float

**Module 1 · Variables, types and input · 5:17 · Pastel Blue + Tomato · Prerequisite: EP 05**

**Learning goals:** tell an int from a float and check with type(); know that / always gives a float; use round() when decimal noise matters.

### YouTube

- **Title:** Numbers in Python: int and float | Python Programming EP 06
- **Description:** Whole numbers, decimals, and why 0.1 plus 0.2 is not quite 0.3, with Xecxec the crab. 0:00 Intro · 0:20 Two kinds of numbers · 1:00 Cups of tea · 1:40 Why 0.1 + 0.2 is odd · 2:15 Follow the types · 2:55 Run it · 3:15 Recap · 3:50 Bug of the Day · 4:42 Challenge · 5:02 Next episode
- **Tags:** python int float, python numbers, python for beginners, python tutorial, floating point, python round, koding konkani, learn programming, class 11 computer science, coding in goa
- **Thumbnail:** big text "INT OR FLOAT?" in tomato on pastel blue; Xecxec between a whole-number crate marked 3 and a decimal crate marked 12.5; thin black border and drop shadow.

### Scene list

| # | Start | Length | Template | On screen | Animation & SFX |
| --- | --- | --- | --- | --- | --- |
| 1 | 0:00 | 0:20 | Title card | EP 06 · INT OR FLOAT? | Tomato title card: EP sticker thuds in, title stamps with a whoosh, Xecxec scuttles in and waves; thud, whoosh, claw-click, sting |
| 2 | 0:20 | 0:40 | Concept slide | "Two kinds of numbers": three numbered lines and a crates analogy card | Lines spring in with a pop; the card shows a whole-fish crate and a weighing scale |
| 3 | 1:00 | 0:40 | Code explain | `numbers.py`: cups, tea, bill, and three prints | Code types in with key-tick; butter [HL n] highlight sweeps line by line with marker-swipe; explanation card on the right |
| 4 | 1:40 | 0:35 | Concept slide | Two boxes: whole numbers are exact; decimals are close; a warning card shows 0.30000000000000004 | Two cards pop in side by side; the decimal card wobbles and shows 0.30000000000000004 in tomato |
| 5 | 2:15 | 0:40 | Code explain | `numbers.py` again with the output panel on the right | Same code; the output panel fills line by line with a ding per output line; [TRACK] cards update |
| 6 | 2:55 | 0:20 | Terminal | Terminal: `python numbers.py` | Dark-blue terminal: the command types with key-tick, output prints in mint with a ding |
| 7 | 3:15 | 0:35 | Concept slide | Recap: four ideas on one card | Four recap lines tick in one by one with a pop; Xecxec nods after each tick |
| 8 | 3:50 | 0:40 | Bug of the Day | BUG OF THE DAY: an assert that fails on decimals | Butter banner drops in with a buzzer; wrong code shakes; the Python error lines appear in tomato; the fix slides in and the terminal turns mint with a ding |
| 9 | 4:30 | 0:12 | Pun card | Zero point one plus zero point two walked into a bar and ordered zero point three. The bartender said: close enough. | Full tomato screen, card flips in with a rimshot, Xecxec snaps his claw |
| 10 | 4:42 | 0:20 | Challenge | Task card: a bill with a float price; print its type | Task card pops in; checklist ticks with a pop; Xecxec holds a tiny pen |
| 11 | 5:02 | 0:15 | Outro | Next: EP 07 · Strings | Next-episode card slides up with a whoosh; right side stays empty for end-screen elements; sign-off text types in |

### Narration script

**[1 · Title]** Welcome back! Last time we tied names to values. Today the values are numbers. Python has two kinds, and knowing which is which saves you from strange answers.

**[2 · Two kinds of numbers]** Python has two main kinds of numbers. An int is a whole number, like three or one hundred. A float has a decimal point, like twelve point five. Think of counting fish, and weighing fish. Counting gives whole numbers. Weighing gives decimals. Python decides the kind from how you write the number, so three is an int, and three point zero is a float.

**[3 · Cups of tea]** [HL 1] [TRACK cups=3] Cups is the whole number three. [HL 2] [TRACK tea=12.5] Tea is twelve point five, so it is a float. [HL 3] [TRACK bill=37.5] Bill is cups times tea. An int times a float always gives a float, so we get thirty seven point five. [HL 4] Print the label and the bill. [HL 5] The type function tells us the kind of each value. [HL 6] And what about eight divided by two?

**[4 · Why 0.1 + 0.2 is odd]** Whole numbers are exact. Decimals are not always. A computer stores floats in binary, and some decimals, like point one, cannot be written exactly in binary. So point one plus point two gives point three, followed by a tiny tail of zeros and a four. This is not a Python bug. Every language does it. When it matters, use the round function.

**[5 · Follow the types]** [HL 4] Three times twelve point five is thirty seven point five. [HL 5] The type of cups is int. The type of tea is float. [HL 6] Here is the surprise. Eight divided by two prints four point zero, not four. The slash always gives a float, even when the answer looks whole. Predict first, then check. Slash means a float. Always.

**[6 · Run it]** Run it. Bill, thirty seven point five. Class int, class float. And four point zero. Try changing cups to a float, and see what happens to the types.

**[7 · Recap]** Recap. One: an int is a whole number, and a float has a decimal point. Two: the type function tells you which one you have. Three: slash always gives a float, even for eight divided by two. Four: decimals carry a tiny error, so round before you compare. Say these four ideas out loud, and you are ready for text.

**[8 · Bug of the Day]** Bug of the Day. We check that point one plus point two equals point three, using assert. Python says, assertion error, total should be point three. The sum has a tiny tail, so the check fails. Fix it by rounding to two places first. Never compare decimals with a plain equals check.

**[9 · Pun]** Zero point one plus zero point two walked into a bar and ordered zero point three. The bartender said: close enough.

**[10 · Challenge]** Your challenge: set price to nineteen point five and quantity to four. Print the total and its type.

**[11 · Outro]** Next time: strings, which is how Python handles text. Keep coding, says Xecxec!

### Code shown

File 1: `numbers.py` (scene 3, 5)

```python
cups = 3
tea = 12.5
bill = cups * tea
print("Bill:", bill)
print(type(cups), type(tea))
print(8 / 2)
```

**Expected output:**

```text
Bill: 37.5
<class 'int'> <class 'float'>
4.0
```

### Bug of the Day

Wrong code (an exact comparison of 0.1 + 0.2 with 0.3):

```python
total = 0.1 + 0.2
assert total == 0.3, "total should be 0.3"
```

Python output:

```text
Traceback (most recent call last):
  File "numbug.py", line 2, in <module>
    assert total == 0.3, "total should be 0.3"
           ^^^^^^^^^^^^
AssertionError: total should be 0.3
```

Fixed code (rounded to two places before comparing):

```python
total = 0.1 + 0.2
assert round(total, 2) == 0.3, "total should be 0.3"
print(total)
print(round(total, 2))
```

**Why:** Floats are stored in binary and carry tiny errors, so compare rounded values instead of exact ones.

### Pun & challenge

- **Pun:** "0.1 plus 0.2 walked into a bar and ordered 0.3. The bartender said: close enough."
- **Challenge:** Set price = 19.5 and quantity = 4, then print the total and its type.
- **Challenge answer:** total = price * quantity gives 78.0, and type(total) is float.

### Shorts for EP 06

**S1 · Int versus float** — 0:20 · built from scene 2

- **Hook (first 1.5s):** "Counting or weighing?"
- **Script:** Counting or weighing? Whole numbers are ints, like three. Decimals are floats, like twelve point five. Python decides from how you write it.
- **On-screen text:** INT OR FLOAT?
- **Caption + hashtags:** Two kinds of numbers. #python #int #float #kodingkonkani #beginners

**S2 · Ask for the type** — 0:20 · built from scene 5

- **Hook (first 1.5s):** "Not sure what it is? Ask."
- **Script:** Not sure what it is? Ask. The type function tells you. Cups gives class int. Tea gives class float. Check before you guess.
- **On-screen text:** TYPE(CUPS)
- **Caption + hashtags:** Check with type. #python #type #learntocode #kodingkonkani #coding

**S3 · Slash gives a float** — 0:20 · built from scene 5

- **Hook (first 1.5s):** "Eight divided by two is four point zero."
- **Script:** Eight divided by two is four point zero. The slash always gives a float, even when the answer looks whole.
- **On-screen text:** 8 / 2 = 4.0
- **Caption + hashtags:** Slash is always a float. #python #division #float #kodingkonkani #coding

**S4 · The assert that failed** — 0:20 · built from scene 8

- **Hook (first 1.5s):** "Point one plus point two fails."
- **Script:** Point one plus point two is not exactly point three. Python says, assertion error. Round to two places before you compare decimals.
- **On-screen text:** ASSERTIONERROR
- **Caption + hashtags:** Round before you compare. #python #bugfix #assertionerror #kodingkonkani #coding

**S5 · Pun and challenge** — 0:20 · built from scenes 9, 10

- **Hook (first 1.5s):** "Close enough, said the bartender."
- **Script:** Close enough, said the bartender. Point one plus point two ordered point three. Your challenge: price nineteen point five, quantity four, print the total and its type. Full video: EP 6.
- **On-screen text:** PRINT THE TOTAL + ITS TYPE
- **Caption + hashtags:** Try the challenge. #python #codingchallenge #kodingkonkani #programmingjokes #goa

## EP 07 — Strings

**Module 1 · Variables, types and input · 5:10 · Pastel Blue + Tomato · Prerequisite: EP 06**

**Learning goals:** write text with single or double quotes; join strings with + and repeat them with *; pick one character with an index, including -1.

### YouTube

- **Title:** Strings in Python: Join, Repeat and Index | Python Programming EP 07
- **Description:** Work with text in Python: length, joining, repeating and picking letters, with Xecxec the crab. 0:00 Intro · 0:20 Text is a string · 0:55 Four string tricks · 1:35 Numbered letters · 2:10 Follow the letters · 2:50 Run it · 3:10 Recap · 3:45 Bug of the Day · 4:35 Challenge · 4:55 Next episode
- **Tags:** python strings, python string indexing, python for beginners, python tutorial, string concatenation, typeerror, koding konkani, learn programming, class 11 computer science, coding in goa
- **Thumbnail:** big text "STRINGS" in tomato on pastel blue; Xecxec threading beads that spell XECXEC on a string; thin black border and drop shadow.

### Scene list

| # | Start | Length | Template | On screen | Animation & SFX |
| --- | --- | --- | --- | --- | --- |
| 1 | 0:00 | 0:20 | Title card | EP 07 · STRINGS | Tomato title card: EP sticker thuds in, title stamps with a whoosh, Xecxec scuttles in and waves; thud, whoosh, claw-click, sting |
| 2 | 0:20 | 0:35 | Concept slide | "Text is a string": three numbered lines and a bead-necklace analogy card | Lines spring in with a pop; the card shows letters threaded on a string like beads |
| 3 | 0:55 | 0:40 | Code explain | `strings.py`: name, beach, and four prints | Code types in with key-tick; butter [HL n] highlight sweeps line by line with marker-swipe; explanation card on the right |
| 4 | 1:35 | 0:35 | Concept slide | The word XECXEC as six boxes numbered 0 to 5 on top and -6 to -1 below | Six letter boxes pop in; numbers 0 to 5 count along the top, and -1 to -6 count backwards along the bottom |
| 5 | 2:10 | 0:40 | Code explain | `strings.py` again with the output panel on the right | Same code; the output panel fills line by line with a ding per output line; [TRACK] cards update |
| 6 | 2:50 | 0:20 | Terminal | Terminal: `python strings.py` | Dark-blue terminal: the command types with key-tick, output prints in mint with a ding |
| 7 | 3:10 | 0:35 | Concept slide | Recap: four ideas on one card | Four recap lines tick in one by one with a pop; Xecxec nods after each tick |
| 8 | 3:45 | 0:40 | Bug of the Day | BUG OF THE DAY: joining a string and an int | Butter banner drops in with a buzzer; wrong code shakes; the Python error lines appear in tomato; the fix slides in and the terminal turns mint with a ding |
| 9 | 4:25 | 0:10 | Pun card | A string walked into a bar and asked for a slice. The bartender said: only with an index. | Full tomato screen, card flips in with a rimshot, Xecxec snaps his claw |
| 10 | 4:35 | 0:20 | Challenge | Task card: print the first and last letters of your name | Task card pops in; checklist ticks with a pop; Xecxec holds a tiny pen |
| 11 | 4:55 | 0:15 | Outro | Next: EP 08 · Input from the user | Next-episode card slides up with a whoosh; right side stays empty for end-screen elements; sign-off text types in |

### Narration script

**[1 · Title]** Welcome back! So far we used numbers. Today we work with text. In Python, a piece of text is called a string, and it comes with some handy tricks.

**[2 · Text is a string]** A string is text inside quotes. You can use double quotes or single quotes, as long as the pair matches. A string is like a necklace of beads, where each bead is one character. Spaces and symbols count as beads too. Python can count the beads, join two necklaces, repeat one, or pick a single bead.

**[3 · Four string tricks]** [HL 1] [TRACK name=Xecxec] A name tied to the string Xecxec. [HL 2] Single quotes work too, so beach is Palolem. [HL 3] The length function counts the beads. Xecxec has six. [HL 4] Plus joins strings together. Notice the spaces inside the quotes, they are part of the text. [HL 5] Star repeats a string, so ha times three is hahaha. [HL 6] Square brackets pick a letter by its position.

**[4 · Numbered letters]** Each letter has a position number, called an index. Counting starts at zero, not one. So X is zero, E is one, and C is five, the last one. Python also counts from the end. Minus one is the last letter, minus two is the one before it. Using a number outside the word gives an error, so stay inside the bead count.

**[5 · Follow the letters]** [HL 3] The length is six. [HL 4] Xecxec loves Palolem, joined into one string. [HL 5] Hahaha. [HL 6] Index zero is the first letter, X. Index minus one is the last letter, C. They print with a space between them. Predict first. What would name at index two print? The answer is C. Zero, one, two.

**[6 · Run it]** Run it. Six. Xecxec loves Palolem. Hahaha. And X, then C. Now change the beach to your favourite beach, and run it again.

**[7 · Recap]** Recap. One: a string is text inside matching quotes. Two: plus joins strings, and star repeats them. Three: the first letter has index zero, and minus one is the last. Four: plus cannot join text and a number. Say these four ideas out loud, then print the first and last letters of your own name.

**[8 · Bug of the Day]** Bug of the Day. We try to join text and a number with plus. Python says, type error, can only concatenate str, not int, to str. Plus joins strings only. Fix it by giving print each piece separated by commas. Print adds the spaces for you.

**[9 · Pun]** A string walked into a bar and asked for a slice. The bartender said: only with an index.

**[10 · Challenge]** Your challenge: store your name in a variable. Print its length, its first letter, and its last letter.

**[11 · Outro]** Next time: asking the user a question with input. Keep coding, says Xecxec!

### Code shown

File 1: `strings.py` (scene 3, 5)

```python
name = "Xecxec"
beach = 'Palolem'
print(len(name))
print(name + " loves " + beach)
print("ha" * 3)
print(name[0], name[-1])
```

**Expected output:**

```text
6
Xecxec loves Palolem
hahaha
X c
```

### Bug of the Day

Wrong code (a string is joined to an int with +):

```python
age = 5
print("Xecxec is " + age + " years old")
```

Python output:

```text
Traceback (most recent call last):
  File "sb.py", line 2, in <module>
    print("Xecxec is " + age + " years old")
          ~~~~~~~~~~~~~^~~~~
TypeError: can only concatenate str (not "int") to str
```

Fixed code (print gets the pieces separated by commas):

```python
age = 5
print("Xecxec is", age, "years old")
```

**Why:** Plus joins two strings, so a number must be given to print separately or turned into text first.

### Pun & challenge

- **Pun:** "A string walked into a bar and asked for a slice. The bartender said: only with an index."
- **Challenge:** Store your name in a variable, then print its length, its first letter and its last letter.
- **Challenge answer:** With name = "Atreya", print(len(name)), print(name[0]) and print(name[-1]) give 6, A and a.

### Shorts for EP 07

**S1 · A string is a necklace** — 0:20 · built from scene 2

- **Hook (first 1.5s):** "Text is a necklace of beads."
- **Script:** Text is a necklace of beads. A string is text in quotes, and each character is one bead. Python can count, join, repeat or pick them.
- **On-screen text:** STRING = TEXT IN QUOTES
- **Caption + hashtags:** Strings explained. #python #strings #beginners #kodingkonkani #goa

**S2 · Join and repeat** — 0:20 · built from scenes 3, 5

- **Hook (first 1.5s):** "Plus joins. Star repeats."
- **Script:** Plus joins. Star repeats. Name plus loves plus beach makes one sentence. And ha times three makes hahaha.
- **On-screen text:** + JOINS, * REPEATS
- **Caption + hashtags:** Two string tricks. #python #strings #concatenation #kodingkonkani #coding

**S3 · Count from zero** — 0:20 · built from scene 4

- **Hook (first 1.5s):** "The first letter is number zero."
- **Script:** The first letter is number zero. X is zero, E is one, C is five. And minus one counts from the end.
- **On-screen text:** INDEX STARTS AT 0
- **Caption + hashtags:** Zero is the first. #python #indexing #learntocode #kodingkonkani #coding

**S4 · Cannot concatenate** — 0:20 · built from scene 8

- **Hook (first 1.5s):** "You cannot add text and a number."
- **Script:** You cannot add text and a number. Python says, type error, can only concatenate str to str. Give print the pieces with commas.
- **On-screen text:** TYPEERROR: CONCATENATE
- **Caption + hashtags:** Plus joins strings only. #python #bugfix #typeerror #kodingkonkani #coding

**S5 · Pun and challenge** — 0:20 · built from scenes 9, 10

- **Hook (first 1.5s):** "A string asked for a slice."
- **Script:** A string asked for a slice. The bartender said, only with an index. Your challenge: print your name's length, first letter and last letter. Full video: EP 7.
- **On-screen text:** LENGTH, FIRST, LAST
- **Caption + hashtags:** Try it. #python #codingchallenge #kodingkonkani #programmingjokes #goa

## EP 08 — Input from the user

**Module 1 · Variables, types and input · 5:03 · Pastel Blue + Tomato · Prerequisite: EP 07**

**Learning goals:** ask the user a question with input(); know that input() always gives back a string; turn the answer into a number with int().

### YouTube

- **Title:** Input in Python: Ask the User a Question | Python Programming EP 08
- **Description:** Use input() to talk to your user, and learn why the answer is always text, with Xecxec the crab. 0:00 Intro · 0:15 Programs that listen · 0:50 Ask and answer · 1:30 Always a string · 2:05 Follow the answer · 2:45 Run it · 3:05 Recap · 3:40 Bug of the Day · 4:28 Challenge · 4:48 Next episode
- **Tags:** python input, python user input, python for beginners, python tutorial, input function, typeerror, koding konkani, learn programming, class 11 computer science, coding in goa
- **Thumbnail:** big text "ASK THE USER" in tomato on pastel blue; Xecxec holding a speech bubble with a question mark toward a terminal prompt; thin black border and drop shadow.

### Scene list

| # | Start | Length | Template | On screen | Animation & SFX |
| --- | --- | --- | --- | --- | --- |
| 1 | 0:00 | 0:15 | Title card | EP 08 · ASK THE USER | Tomato title card: EP sticker thuds in, title stamps with a whoosh, Xecxec scuttles in and waves; thud, whoosh, claw-click, sting |
| 2 | 0:15 | 0:35 | Concept slide | "Programs that listen": three numbered lines and a shop-counter analogy card | Lines spring in with a pop; the card shows a shopkeeper asking a customer a question |
| 3 | 0:50 | 0:40 | Code explain | `ask.py`: one input line and three prints | Code types in with key-tick; butter [HL n] highlight sweeps line by line with marker-swipe; explanation card on the right |
| 4 | 1:30 | 0:35 | Concept slide | A speech bubble reading 3 turns into a text card marked str; an int() machine turns it into a number card | A speech bubble drops in with the answer; it lands as a text card; the int machine turns it into a number card with a ding |
| 5 | 2:05 | 0:40 | Code explain | `ask.py` again with the output panel on the right | Same code; the output panel fills line by line with a ding per output line; [TRACK] cards update |
| 6 | 2:45 | 0:20 | Terminal | Terminal: `python ask.py`, then the user types 3 | Dark-blue terminal: the command types with key-tick, output prints in mint with a ding |
| 7 | 3:05 | 0:35 | Concept slide | Recap: four ideas on one card | Four recap lines tick in one by one with a pop; Xecxec nods after each tick |
| 8 | 3:40 | 0:40 | Bug of the Day | BUG OF THE DAY: multiplying the text from input | Butter banner drops in with a buzzer; wrong code shakes; the Python error lines appear in tomato; the fix slides in and the terminal turns mint with a ding |
| 9 | 4:20 | 0:08 | Pun card | I asked Python for input. It waited. So did I. We are still waiting. | Full tomato screen, card flips in with a rimshot, Xecxec snaps his claw |
| 10 | 4:28 | 0:20 | Challenge | Task card: ask for a price, convert it, print it with tax | Task card pops in; checklist ticks with a pop; Xecxec holds a tiny pen |
| 11 | 4:48 | 0:15 | Outro | Next: EP 09 · Operators | Next-episode card slides up with a whoosh; right side stays empty for end-screen elements; sign-off text types in |

### Narration script

**[1 · Title]** Welcome back! Until now our programs knew everything in advance. Today they ask. With input, your program can wait for the user to type an answer.

**[2 · Programs that listen]** The input function pauses the program and waits. Whatever you write inside the brackets is shown as the question, called the prompt. The user types an answer and presses enter. Think of a shopkeeper asking, how many fish? The customer answers, and the shopkeeper writes it down. You can call input as many times as you like, once for each question.

**[3 · Ask and answer]** [HL 1] [TRACK beaches=3] Input shows the question, then waits. The answer is tied to the name beaches. Here the user typed three. [HL 2] Print shows it. [HL 3] Now plus joins beaches to itself. [HL 4] And int turns the text into a real number before adding one.

**[4 · Always a string]** Here is the big surprise. Input always gives back a string, even when the user types digits. The character three is not the number three. That is why plus joined the text, and gave thirty three. To do maths, wrap the input in int, which turns text into a whole number. Or use float, if decimals are allowed.

**[5 · Follow the answer]** [HL 1] The user types three. Python gets the text three. [HL 2] Print shows beaches, three. [HL 3] Plus joins the text, so we get thirty three. It is text plus text. [HL 4] Int converts the text to the number three. Add one, and we get four. Predict first. Without int, would beaches plus one work? No. Text plus a number is an error.

**[6 · Run it]** Run it. The question appears and waits. We type three and press enter. Beaches, three. Thirty three. Four. Python waited for us, and then carried on.

**[7 · Recap]** Recap. One: input shows a prompt, waits, and returns what the user typed. Two: the answer is always a string, even if it looks like a number. Three: wrap it in int or float before doing maths. Four: text times a decimal is a type error. Say these four ideas out loud, then ask your own question.

**[8 · Bug of the Day]** Bug of the Day. The user types four. Beaches is the text four. We multiply it by two point five. Python says, type error, can't multiply sequence by non-int of type float. Text can be repeated by a whole number, but not a decimal. Wrap input in int, and the maths works.

**[9 · Pun]** I asked Python for input. It waited. So did I. We are still waiting.

**[10 · Challenge]** Your challenge: ask the user for a price. Convert it with float, then print the price plus ten percent.

**[11 · Outro]** Next time: operators, the maths symbols of Python. Keep coding, says Xecxec!

### Code shown

File 1: `ask.py` (scene 3, 5)

Input: 3

```python
beaches = input("How many beaches? ")
print("Beaches:", beaches)
print(beaches + beaches)
print(int(beaches) + 1)
```

**Expected output:**

```text
How many beaches? Beaches: 3
33
4
```

### Bug of the Day

Wrong code (beaches is the text from input, run with input: 4):

```python
beaches = input("How many beaches? ")
print("Total:", beaches * 2.5)
```

Python output:

```text
Traceback (most recent call last):
  File "ib.py", line 2, in <module>
    print("Total:", beaches * 2.5)
                    ~~~~~~~~^~~~~
TypeError: can't multiply sequence by non-int of type 'float'
```

Fixed code (int() added around input):

```python
beaches = int(input("How many beaches? "))
print("Total:", beaches * 2.5)
```

Output of the fixed code:

```text
How many beaches? Total: 10.0
```

**Why:** input() always returns a string, and a string can only be repeated by a whole number, so convert the answer with int() first.

### Pun & challenge

- **Pun:** "I asked Python for input. It waited. So did I. We are still waiting."
- **Challenge:** Ask the user for a price, convert it with float, then print the price plus ten percent.
- **Challenge answer:** price = float(input("Price? ")) then print(price * 1.1); an input of 100 gives 110.00000000000001 or about 110.

### Shorts for EP 08

**S1 · Programs that listen** — 0:20 · built from scene 2

- **Hook (first 1.5s):** "Your program can ask questions."
- **Script:** Your program can ask questions. Input shows a prompt, waits, and returns what the user typed. Press enter, and it carries on.
- **On-screen text:** INPUT() = ASK + WAIT
- **Caption + hashtags:** Ask the user. #python #input #beginners #kodingkonkani #goa

**S2 · Input is always text** — 0:20 · built from scene 4

- **Hook (first 1.5s):** "The number three is not three."
- **Script:** The number three is not three. Input always gives back a string, even when the user types digits. Plus will join them, not add them.
- **On-screen text:** INPUT GIVES A STRING
- **Caption + hashtags:** Always text. #python #input #strings #kodingkonkani #coding

**S3 · Wrap it in int** — 0:20 · built from scenes 3, 5

- **Hook (first 1.5s):** "One word fixes the maths."
- **Script:** One word fixes the maths. Wrap input in int, and the text becomes a real number you can add or multiply.
- **On-screen text:** INT(INPUT())
- **Caption + hashtags:** Convert the answer. #python #int #learntocode #kodingkonkani #coding

**S4 · Cannot multiply sequence** — 0:20 · built from scene 8

- **Hook (first 1.5s):** "Text times two point five."
- **Script:** Text times two point five fails. Python says, can't multiply sequence by non-int of type float. Convert the input first.
- **On-screen text:** TYPEERROR: SEQUENCE
- **Caption + hashtags:** Convert before maths. #python #bugfix #typeerror #kodingkonkani #coding

**S5 · Pun and challenge** — 0:20 · built from scenes 9, 10

- **Hook (first 1.5s):** "Python waited. So did I."
- **Script:** Python waited. So did I. Your challenge: ask for a price, convert it with float, and print the price plus ten percent. Full video: EP 8.
- **On-screen text:** PRICE PLUS 10%
- **Caption + hashtags:** Try it. #python #codingchallenge #kodingkonkani #programmingjokes #goa

## EP 09 — Operators

**Module 1 · Variables, types and input · 5:04 · Pastel Blue + Tomato · Prerequisite: EP 08**

**Learning goals:** use + - * / // % and ** correctly; explain floor division and remainder with tables and shacks; know that ^ is not the power operator.

### YouTube

- **Title:** Operators in Python: // % and ** | Python Programming EP 09
- **Description:** The maths symbols of Python, including floor division, remainder and power, with Xecxec the crab. 0:00 Intro · 0:15 The seven operators · 0:50 Tables and shacks · 1:30 Floor division · 2:05 Follow the maths · 2:45 Run it · 3:05 Recap · 3:40 Bug of the Day · 4:29 Challenge · 4:49 Next episode
- **Tags:** python operators, floor division python, modulo python, python power, python for beginners, python tutorial, koding konkani, learn programming, class 11 computer science, coding in goa
- **Thumbnail:** big text "// % **" in tomato on pastel blue; Xecxec juggling the symbols // % and ** like beach balls; thin black border and drop shadow.

### Scene list

| # | Start | Length | Template | On screen | Animation & SFX |
| --- | --- | --- | --- | --- | --- |
| 1 | 0:00 | 0:15 | Title card | EP 09 · // % ** | Tomato title card: EP sticker thuds in, title stamps with a whoosh, Xecxec scuttles in and waves; thud, whoosh, claw-click, sting |
| 2 | 0:15 | 0:35 | Concept slide | "The seven operators": three numbered lines and a calculator analogy card | Lines spring in with a pop; the card shows a calculator with seven keys lighting up |
| 3 | 0:50 | 0:40 | Code explain | `ops.py`: shacks, tables and five prints | Code types in with key-tick; butter [HL n] highlight sweeps line by line with marker-swipe; explanation card on the right |
| 4 | 1:30 | 0:35 | Concept slide | A number line from -5 to 5 with 17 / 5 and -17 / 5 marked; a floor arrow steps down to the next whole number | A number line slides in; a dot lands on 3.4 and a floor arrow steps left to 3; another dot lands on -3.4 and the floor arrow steps left to -4 |
| 5 | 2:05 | 0:40 | Code explain | `ops.py` again with the output panel on the right | Same code; the output panel fills line by line with a ding per output line; [TRACK] cards update |
| 6 | 2:45 | 0:20 | Terminal | Terminal: `python ops.py` | Dark-blue terminal: the command types with key-tick, output prints in mint with a ding |
| 7 | 3:05 | 0:35 | Concept slide | Recap: five operators on one card | Four recap lines tick in one by one with a pop; Xecxec nods after each tick |
| 8 | 3:40 | 0:40 | Bug of the Day | BUG OF THE DAY: caret is not power | Butter banner drops in with a buzzer; wrong code shakes; the Python error lines appear in tomato; the fix slides in and the terminal turns mint with a ding |
| 9 | 4:20 | 0:09 | Pun card | Why did floor division break up with the slash? It was tired of the remainders. | Full tomato screen, card flips in with a rimshot, Xecxec snaps his claw |
| 10 | 4:29 | 0:20 | Challenge | Task card: 100 minutes into hours and minutes | Task card pops in; checklist ticks with a pop; Xecxec holds a tiny pen |
| 11 | 4:49 | 0:15 | Outro | Next: EP 10 · f-strings and formatting | Next-episode card slides up with a whoosh; right side stays empty for end-screen elements; sign-off text types in |

### Narration script

**[1 · Title]** Welcome back! You know plus, minus and times. Today we meet the other operators, including two that surprise most beginners: floor division and remainder.

**[2 · The seven operators]** Python has seven maths operators. Plus, minus and times work as you expect. Slash divides and gives a float. Double slash is floor division, which keeps only the whole part. Percent gives the remainder. And double star raises to a power. Think of a calculator with a few extra keys. Today we learn the extra ones.

**[3 · Tables and shacks]** [HL 1] [TRACK shacks=17] Seventeen guests. [HL 2] [TRACK tables=5] Five tables. [HL 3] Floor division gives three. Each table seats three full groups. [HL 4] Percent gives the remainder, two. Two guests are left standing. [HL 5] Double star is power. Two to the power ten is one thousand twenty four. [HL 6] Plain slash gives three point four, a float.

**[4 · Floor division]** Floor division rounds the answer down, towards the smaller number. Seventeen divided by five is three point four, and the floor is three. Now the surprise. Minus seventeen divided by five is minus three point four, and down from there is minus four, not minus three. Down means more negative, not closer to zero. Remember that, and negative numbers stop being scary.

**[5 · Follow the maths]** [HL 3] Seventeen floor divided by five is three. [HL 4] Seventeen percent five is two, because five times three is fifteen and two is left. [HL 5] One thousand twenty four. [HL 6] Three point four. [HL 7] Minus four, because floor goes down. Predict before you run. The last line is the tricky one. Did you say minus three? Check the number line.

**[6 · Run it]** Run it. Three. Two. One thousand twenty four. Three point four. Minus four. Change shacks to twenty, and predict all five answers first.

**[7 · Recap]** Recap. One: slash divides and always gives a float. Two: double slash keeps the whole part, and rounds down. Three: percent gives the remainder. Four: double star is power, and caret is something else. And remember, minus seventeen floor five is minus four. Say these out loud, and try a few of your own numbers.

**[8 · Bug of the Day]** Bug of the Day. We try to square root two, using caret. Python says, type error, unsupported operand types for caret, int and float. In Python, caret is a different operator, used on bits. Power is double star. Two to the power point five is the square root of two.

**[9 · Pun]** Why did floor division break up with the slash? It was tired of the remainders.

**[10 · Challenge]** Your challenge: turn one hundred thirty five minutes into hours and minutes, using floor division and remainder.

**[11 · Outro]** Next time: f-strings, the neat way to print values. Keep coding, says Xecxec!

### Code shown

File 1: `ops.py` (scene 3, 5)

```python
shacks = 17
tables = 5
print(shacks // tables)
print(shacks % tables)
print(2 ** 10)
print(shacks / tables)
print(-17 // 5)
```

**Expected output:**

```text
3
2
1024
3.4
-4
```

### Bug of the Day

Wrong code (caret used for power):

```python
print(2 ^ 0.5)
```

Python output:

```text
Traceback (most recent call last):
  File "ob.py", line 1, in <module>
    print(2 ^ 0.5)
          ~~^~~~~
TypeError: unsupported operand type(s) for ^: 'int' and 'float'
```

Fixed code (double star used for power):

```python
print(2 ** 0.5)
```

Output of the fixed code:

```text
1.4142135623730951
```

**Why:** The caret is the bitwise XOR operator in Python; use ** for powers.

### Pun & challenge

- **Pun:** "Why did floor division break up with the slash? It was tired of the remainders."
- **Challenge:** Turn 135 minutes into hours and minutes using // and %.
- **Challenge answer:** 135 // 60 gives 2 hours and 135 % 60 gives 15 minutes, so print 2 and 15.

### Shorts for EP 09

**S1 · Floor division** — 0:20 · built from scene 4

- **Hook (first 1.5s):** "Seventeen shared among five tables."
- **Script:** Seventeen guests, five tables. Double slash gives three, the whole groups. Percent gives two, the guests left over.
- **On-screen text:** // AND % 
- **Caption + hashtags:** Quotient and remainder. #python #operators #beginners #kodingkonkani #goa

**S2 · The remainder** — 0:20 · built from scenes 3, 5

- **Hook (first 1.5s):** "What is left over?"
- **Script:** What is left over? Percent gives the remainder. Seventeen percent five is two, because five times three is fifteen.
- **On-screen text:** 17 % 5 = 2
- **Caption + hashtags:** Remainder explained. #python #modulo #learntocode #kodingkonkani #coding

**S3 · Floor goes down** — 0:20 · built from scenes 4, 5

- **Hook (first 1.5s):** "Minus seventeen floor five is minus four."
- **Script:** Minus seventeen floor divided by five is minus four, not minus three. Floor goes down, towards the smaller number.
- **On-screen text:** -17 // 5 = -4
- **Caption + hashtags:** Floor means down. #python #floordivision #negativenumbers #kodingkonkani #coding

**S4 · Caret is not power** — 0:20 · built from scene 8

- **Hook (first 1.5s):** "Caret does not mean power."
- **Script:** Caret does not mean power in Python. Two caret point five gives a type error. Use double star for powers.
- **On-screen text:** 2 ** 0.5, NOT 2 ^ 0.5
- **Caption + hashtags:** Use double star. #python #bugfix #typeerror #kodingkonkani #coding

**S5 · Pun and challenge** — 0:20 · built from scenes 9, 10

- **Hook (first 1.5s):** "Tired of the remainders."
- **Script:** Floor division broke up with the slash. It was tired of the remainders. Your challenge: turn one hundred thirty five minutes into hours and minutes. Full video: EP 9.
- **On-screen text:** 135 MINUTES = ? H ? M
- **Caption + hashtags:** Try it. #python #codingchallenge #kodingkonkani #programmingjokes #goa

## EP 10 — f-strings and formatting

**Module 1 · Variables, types and input · 5:17 · Pastel Blue + Tomato · Prerequisite: EP 09**

**Learning goals:** put values inside text with an f-string and {}; format decimals with :.2f; run a small expression inside the braces.

### YouTube

- **Title:** f-strings in Python: Print Values Neatly | Python Programming EP 10
- **Description:** The cleanest way to put values into text, including two-decimal prices, with Xecxec the crab. 0:00 Intro · 0:15 Fill in the blanks · 0:55 Fish bill · 1:35 Format codes · 2:15 Follow the template · 2:55 Run it · 3:15 Recap · 3:55 Bug of the Day · 4:42 Challenge · 5:02 Next episode
- **Tags:** python f-strings, python string formatting, python for beginners, python tutorial, format decimals python, valueerror, koding konkani, learn programming, class 11 computer science, coding in goa
- **Thumbnail:** big text "F-STRINGS" in tomato on pastel blue; Xecxec pouring values into curly braces on a text card marked f; thin black border and drop shadow.

### Scene list

| # | Start | Length | Template | On screen | Animation & SFX |
| --- | --- | --- | --- | --- | --- |
| 1 | 0:00 | 0:15 | Title card | EP 10 · F-STRINGS | Tomato title card: EP sticker thuds in, title stamps with a whoosh, Xecxec scuttles in and waves; thud, whoosh, claw-click, sting |
| 2 | 0:15 | 0:40 | Concept slide | "Fill in the blanks": three numbered lines and a bill-template analogy card | Lines spring in with a pop; the card shows a bill with blank spaces being filled in |
| 3 | 0:55 | 0:40 | Code explain | `fstring.py`: three names and three f-string prints | Code types in with key-tick; butter [HL n] highlight sweeps line by line with marker-swipe; explanation card on the right |
| 4 | 1:35 | 0:40 | Concept slide | A braces card: {total:.2f} split into the value, the colon and the format code | The card {total:.2f} pops in; three pieces light up one by one: the name, the colon, and .2f; a result card shows 358.50 |
| 5 | 2:15 | 0:40 | Code explain | `fstring.py` again with the output panel on the right | Same code; the output panel fills line by line with a ding per output line; [TRACK] cards update |
| 6 | 2:55 | 0:20 | Terminal | Terminal: `python fstring.py` | Dark-blue terminal: the command types with key-tick, output prints in mint with a ding |
| 7 | 3:15 | 0:40 | Concept slide | Recap: four ideas on one card | Four recap lines tick in one by one with a pop; Xecxec nods after each tick |
| 8 | 3:55 | 0:40 | Bug of the Day | BUG OF THE DAY: the d format code on a float | Butter banner drops in with a buzzer; wrong code shakes; the Python error lines appear in tomato; the fix slides in and the terminal turns mint with a ding |
| 9 | 4:35 | 0:07 | Pun card | Why did the f-string cry? Someone forgot it at the start. | Full tomato screen, card flips in with a rimshot, Xecxec snaps his claw |
| 10 | 4:42 | 0:20 | Challenge | Task card: a receipt line with two decimals | Task card pops in; checklist ticks with a pop; Xecxec holds a tiny pen |
| 11 | 5:02 | 0:15 | Outro | Next: EP 11 · Booleans and comparisons | Next-episode card slides up with a whoosh; right side stays empty for end-screen elements; sign-off text types in |

### Narration script

**[1 · Title]** Welcome back! Printing with commas works, but it gets messy. Today we learn f-strings, the neat way to put values inside a sentence.

**[2 · Fill in the blanks]** An f-string is a template with blanks. Put the letter f right before the opening quote. Then write curly braces wherever a value should go. Python fills each blank with the value inside. It is like a printed bill with blank spaces for the name and the total. And if you forget the f, Python prints the braces as plain text, with no error.

**[3 · Fish bill]** [HL 1] [TRACK name=Xecxec] A name. [HL 2] [TRACK fish=3] A count. [HL 3] [TRACK price=119.5] A price with a decimal. [HL 4] [TRACK total=358.5] The total, three hundred fifty eight point five. [HL 5] The f before the quote turns on the blanks. Name and fish are filled in from their values. [HL 6] After a colon inside the braces, we add a format code. Point two f means, two digits after the decimal point.

**[4 · Format codes]** Look inside the braces. The name comes first, then a colon, then the format code. Point two f means, show a float with two decimals. So three fifty eight point five prints as three fifty eight point five zero. That is perfect for money. Use d for whole numbers, but never for a float, or Python complains. You can also put a small expression inside the braces, like fish times two.

**[5 · Follow the template]** [HL 5] Python fills the blanks. Xecxec bought three fish. [HL 6] The total prints as three fifty eight point five zero, with two decimals. [HL 7] The braces can hold a calculation. Fish times two is six, so we get, six fish in two trips. Predict first. What would the format code point one f print for the total? Three fifty eight point five.

**[6 · Run it]** Run it. Xecxec bought three fish. Total, three fifty eight point five zero. Six fish in two trips. Change the price, and watch the total follow.

**[7 · Recap]** Recap. One: an f-string starts with f before the quote, and uses braces for values. Two: after a colon in the braces, you can add a format code. Three: point two f gives two decimals, and d is for whole numbers only. Four: you can put a small calculation inside the braces. Say these four ideas out loud, then rewrite an old print with an f-string.

**[8 · Bug of the Day]** Bug of the Day. We used the format code point two d on a float. Python says, value error, unknown format code d for object of type float. The d code is for whole numbers only. For a float, use point two f, and the bill prints correctly.

**[9 · Pun]** Why did the f-string cry? Someone forgot it at the start.

**[10 · Challenge]** Your challenge: print a receipt line in one f-string, showing a name, a quantity and a total with two decimals.

**[11 · Outro]** Next time: booleans, the yes and no of Python. Keep coding, says Xecxec!

### Code shown

File 1: `fstring.py` (scene 3, 5)

```python
name = "Xecxec"
fish = 3
price = 119.5
total = fish * price
print(f"{name} bought {fish} fish")
print(f"Total: {total:.2f}")
print(f"{fish * 2} fish in two trips")
```

**Expected output:**

```text
Xecxec bought 3 fish
Total: 358.50
6 fish in two trips
```

### Bug of the Day

Wrong code (the integer code d is used on a float):

```python
price = 119.5
fish = 3
total = fish * price
print(f"Total: {total:.2d}")
```

Python output:

```text
Traceback (most recent call last):
  File "fb.py", line 4, in <module>
    print(f"Total: {total:.2d}")
                   ^^^^^^^^^^^
ValueError: Unknown format code 'd' for object of type 'float'
```

Fixed code (d replaced by f):

```python
price = 119.5
fish = 3
total = fish * price
print(f"Total: {total:.2f}")
```

Output of the fixed code:

```text
Total: 358.50
```

**Why:** The d code formats whole numbers; floats need f, as in :.2f.

### Pun & challenge

- **Pun:** "Why did the f-string cry? Someone forgot it at the start."
- **Challenge:** Print a receipt line with a name, a quantity and a total with two decimals, all in one f-string.
- **Challenge answer:** For example print(f"{item}: {qty} x {price:.2f} = {total:.2f}") with item = "Fish", qty = 3, price = 119.5.

### Shorts for EP 10

**S1 · Fill in the blanks** — 0:20 · built from scene 2

- **Hook (first 1.5s):** "A sentence with blanks."
- **Script:** A sentence with blanks. Put f before the quote, and write curly braces where values go. Python fills them in.
- **On-screen text:** F"HELLO {NAME}"
- **Caption + hashtags:** f-strings in 30 seconds. #python #fstrings #beginners #kodingkonkani #goa

**S2 · Two decimals for money** — 0:20 · built from scene 4

- **Hook (first 1.5s):** "Make money look like money."
- **Script:** Make money look like money. Inside the braces, add colon, point two f. Three fifty eight point five prints with two decimals.
- **On-screen text:** {TOTAL:.2F}
- **Caption + hashtags:** Two decimals. #python #formatting #learntocode #kodingkonkani #coding

**S3 · Maths inside braces** — 0:20 · built from scene 5

- **Hook (first 1.5s):** "Braces can do maths."
- **Script:** Braces can do maths. Put fish times two inside them, and Python prints six. No extra variable needed.
- **On-screen text:** {FISH * 2}
- **Caption + hashtags:** Expressions inside. #python #fstrings #coding #kodingkonkani #tips

**S4 · Unknown format code** — 0:20 · built from scene 8

- **Hook (first 1.5s):** "Use d on a float, and it fails."
- **Script:** Use the d code on a float, and Python says, value error, unknown format code d. Floats need f.
- **On-screen text:** VALUEERROR: CODE D
- **Caption + hashtags:** d is for whole numbers. #python #bugfix #valueerror #kodingkonkani #coding

**S5 · Pun and challenge** — 0:20 · built from scenes 9, 10

- **Hook (first 1.5s):** "The f-string cried."
- **Script:** The f-string cried because someone forgot it at the start. Your challenge: print a receipt line with name, quantity and total in one f-string. Full video: EP 10.
- **On-screen text:** ONE-LINE RECEIPT
- **Caption + hashtags:** Try it. #python #codingchallenge #kodingkonkani #programmingjokes #goa

## EP 11 — Booleans and comparisons

**Module 1 · Variables, types and input · 5:09 · Pastel Blue + Tomato · Prerequisite: EP 10**

**Learning goals:** compare values with == != < > <= >=; combine answers with and, or and not; tell = (assign) from == (compare).

### YouTube

- **Title:** Booleans and Comparisons in Python | Python Programming EP 11
- **Description:** True, False and the symbols that produce them, with Xecxec the crab. 0:00 Intro · 0:20 Yes or no · 0:55 Six comparisons · 1:35 Combining answers · 2:10 Follow the answers · 2:50 Run it · 3:10 Recap · 3:45 Bug of the Day · 4:34 Challenge · 4:54 Next episode
- **Tags:** python booleans, python comparison operators, python and or not, python for beginners, python tutorial, typeerror, koding konkani, learn programming, class 11 computer science, coding in goa
- **Thumbnail:** big text "TRUE OR FALSE" in tomato on pastel blue; Xecxec holding a green TRUE sign and a red FALSE sign; thin black border and drop shadow.

### Scene list

| # | Start | Length | Template | On screen | Animation & SFX |
| --- | --- | --- | --- | --- | --- |
| 1 | 0:00 | 0:20 | Title card | EP 11 · TRUE OR FALSE | Tomato title card: EP sticker thuds in, title stamps with a whoosh, Xecxec scuttles in and waves; thud, whoosh, claw-click, sting |
| 2 | 0:20 | 0:35 | Concept slide | "Yes or no": three numbered lines and a traffic-light analogy card | Lines spring in with a pop; the card shows a green light for True and a red light for False |
| 3 | 0:55 | 0:40 | Code explain | `checks.py`: age, hours, and six prints; the comparison operators glow | Code types in with key-tick; butter [HL n] highlight sweeps line by line with marker-swipe; explanation card on the right |
| 4 | 1:35 | 0:35 | Concept slide | Three logic cards: and needs both True, or needs one True, not flips the answer | Three cards pop in; for each, two lamps light green or red and the result lamp follows the rule with a ding |
| 5 | 2:10 | 0:40 | Code explain | `checks.py` again with the output panel on the right | Same code; the output panel fills line by line with a ding per output line; [TRACK] cards update |
| 6 | 2:50 | 0:20 | Terminal | Terminal: `python checks.py` | Dark-blue terminal: the command types with key-tick, output prints in mint with a ding |
| 7 | 3:10 | 0:35 | Concept slide | Recap: four ideas on one card | Four recap lines tick in one by one with a pop; Xecxec nods after each tick |
| 8 | 3:45 | 0:40 | Bug of the Day | BUG OF THE DAY: one equals sign inside print | Butter banner drops in with a buzzer; wrong code shakes; the Python error lines appear in tomato; the fix slides in and the terminal turns mint with a ding |
| 9 | 4:25 | 0:09 | Pun card | Why did the boolean go to the party? It wanted to be True to itself. | Full tomato screen, card flips in with a rimshot, Xecxec snaps his claw |
| 10 | 4:34 | 0:20 | Challenge | Task card: is a number even and positive? | Task card pops in; checklist ticks with a pop; Xecxec holds a tiny pen |
| 11 | 4:54 | 0:15 | Outro | Next: EP 12 · Type conversion | Next-episode card slides up with a whoosh; right side stays empty for end-screen elements; sign-off text types in |

### Narration script

**[1 · Title]** Welcome back! A program often needs to answer a question with yes or no. In Python, those two answers are called booleans, and today we learn how to produce them.

**[2 · Yes or no]** A boolean has only two possible values, True and False, both with a capital first letter. Comparisons produce them. Is age at least eighteen? The answer is True or False. Think of a traffic light with only green and red. Booleans are what make programs decide, which is exactly what we use in the next module.

**[3 · Six comparisons]** [HL 1] [TRACK age=17] Age is seventeen. [HL 2] [TRACK hours=6] Hours is six. [HL 3] Greater than or equal to eighteen. Seventeen is not, so False. [HL 4] Double equals asks, are they equal? Yes, so True. Notice, two equals signs. One equals ties a name. Two equals compares. [HL 5] Not equal gives False.

**[4 · Combining answers]** You can combine answers. And needs both sides to be True. Or needs at least one side True. Not flips an answer, True becomes False and False becomes True. So, age at least sixteen and hours more than four, is True and True, which is True. Not of False is True. Use brackets to keep your meaning clear.

**[5 · Follow the answers]** [HL 3] False. [HL 4] True. [HL 5] False. [HL 6] Seventeen is at least sixteen, and six is more than four, so both are True, and the answer is True. [HL 7] Age greater than twenty is False, and not flips it to True. [HL 8] The type of True is class bool. Predict each answer before you run.

**[6 · Run it]** Run it. False, True, False, True, True. And class bool. Change age to twenty one, and predict the new answers first.

**[7 · Recap]** Recap. One: a boolean is True or False. Two: double equals compares, and single equals assigns. Three: and needs both sides True, or needs one, and not flips the answer. Four: comparisons like greater than or equal give a boolean. Say these four ideas out loud, then predict each answer on the screen before you run it.

**[8 · Bug of the Day]** Bug of the Day. We wrote age equals seventeen inside print. Python reads that as a keyword argument. It says, type error, print got an unexpected keyword argument age. One equals sign assigns. Two equals signs compare. Use double equals, and Python prints True.

**[9 · Pun]** Why did the boolean go to the party? It wanted to be True to itself.

**[10 · Challenge]** Your challenge: set n to ten. Print whether n is even and also greater than zero.

**[11 · Outro]** Next time: type conversion, turning one kind of value into another. Keep coding, says Xecxec!

### Code shown

File 1: `checks.py` (scene 3, 5)

```python
age = 17
hours = 6
print(age >= 18)
print(age == 17)
print(age != 17)
print(age >= 16 and hours > 4)
print(not (age > 20))
print(type(True))
```

**Expected output:**

```text
False
True
False
True
True
<class 'bool'>
```

### Bug of the Day

Wrong code (a single = inside print):

```python
age = 17
print(age = 17)
```

Python output:

```text
Traceback (most recent call last):
  File "cb.py", line 2, in <module>
    print(age = 17)
    ~~~~~^^^^^^^^^^
TypeError: print() got an unexpected keyword argument 'age'
```

Fixed code (== used to compare):

```python
age = 17
print(age == 17)
```

Output of the fixed code:

```text
True
```

**Why:** A single = assigns and a double == compares; inside brackets a single = is read as a keyword argument.

### Pun & challenge

- **Pun:** "Why did the boolean go to the party? It wanted to be True to itself."
- **Challenge:** Set n = 10, then print whether n is even and also greater than zero.
- **Challenge answer:** print(n % 2 == 0 and n > 0) prints True for n = 10.

### Shorts for EP 11

**S1 · True or False** — 0:20 · built from scene 2

- **Hook (first 1.5s):** "Only two possible answers."
- **Script:** Only two possible answers. A boolean is True or False. Comparisons produce them, and decisions depend on them.
- **On-screen text:** TRUE OR FALSE
- **Caption + hashtags:** Booleans in 30 seconds. #python #boolean #beginners #kodingkonkani #goa

**S2 · Equals versus double equals** — 0:20 · built from scene 3

- **Hook (first 1.5s):** "One equals ties. Two equals asks."
- **Script:** One equals ties a name to a value. Two equals asks, are they equal? Mixing them up is a classic beginner bug.
- **On-screen text:** = TIES, == ASKS
- **Caption + hashtags:** Assign or compare? #python #comparison #learntocode #kodingkonkani #coding

**S3 · And, or, not** — 0:20 · built from scenes 4, 5

- **Hook (first 1.5s):** "Three words that combine answers."
- **Script:** Three words that combine answers. And needs both True. Or needs one True. Not flips the answer.
- **On-screen text:** AND / OR / NOT
- **Caption + hashtags:** Logic in a minute. #python #logic #coding #kodingkonkani #tips

**S4 · Unexpected keyword** — 0:20 · built from scene 8

- **Hook (first 1.5s):** "One equals sign inside print."
- **Script:** One equals sign inside print. Python says, type error, unexpected keyword argument age. Use double equals to compare.
- **On-screen text:** TYPEERROR: KEYWORD ARGUMENT
- **Caption + hashtags:** Use ==. #python #bugfix #typeerror #kodingkonkani #coding

**S5 · Pun and challenge** — 0:20 · built from scenes 9, 10

- **Hook (first 1.5s):** "True to itself."
- **Script:** The boolean went to the party because it wanted to be True to itself. Your challenge: print whether ten is even and greater than zero. Full video: EP 11.
- **On-screen text:** EVEN AND POSITIVE?
- **Caption + hashtags:** Try it. #python #codingchallenge #kodingkonkani #programmingjokes #goa

## EP 12 — Type conversion

**Module 1 · Variables, types and input · 5:13 · Pastel Blue + Tomato · Prerequisite: EP 11**

**Learning goals:** convert with int(), float(), str() and bool(); know that int() cuts the decimal part instead of rounding; read a ValueError from a bad conversion.

### YouTube

- **Title:** Type Conversion in Python: int, float, str, bool | Python Programming EP 12
- **Description:** Turn one kind of value into another, safely, and finish Module 1 with Xecxec the crab. 0:00 Intro · 0:15 Four converters · 0:50 Converting in code · 1:30 What gets cut · 2:10 Follow the values · 2:50 Run it · 3:10 Recap · 3:50 Bug of the Day · 4:38 Challenge · 4:58 Next episode
- **Tags:** python type conversion, python int float str, python casting, python for beginners, python tutorial, valueerror, koding konkani, learn programming, class 11 computer science, coding in goa
- **Thumbnail:** big text "CONVERT IT" in tomato on pastel blue; Xecxec turning a text card marked 42 into a number card through a machine; thin black border and drop shadow.

### Scene list

| # | Start | Length | Template | On screen | Animation & SFX |
| --- | --- | --- | --- | --- | --- |
| 1 | 0:00 | 0:15 | Title card | EP 12 · CONVERT IT | Tomato title card: EP sticker thuds in, title stamps with a whoosh, Xecxec scuttles in and waves; thud, whoosh, claw-click, sting |
| 2 | 0:15 | 0:35 | Concept slide | "Four converters": three numbered lines and a currency-exchange analogy card | Lines spring in with a pop; the card shows a currency exchange counter with four windows |
| 3 | 0:50 | 0:40 | Code explain | `convert.py`: text, number, price and five prints | Code types in with key-tick; butter [HL n] highlight sweeps line by line with marker-swipe; explanation card on the right |
| 4 | 1:30 | 0:40 | Concept slide | A number line with 7.9; int() drops straight down to 7; bool() cards show 0 as False and Goa as True | A dot lands on 7.9 and drops straight down to 7 with a thud; then two bool cards flip: zero turns False, Goa turns True |
| 5 | 2:10 | 0:40 | Code explain | `convert.py` again with the output panel on the right | Same code; the output panel fills line by line with a ding per output line; [TRACK] cards update |
| 6 | 2:50 | 0:20 | Terminal | Terminal: `python convert.py` | Dark-blue terminal: the command types with key-tick, output prints in mint with a ding |
| 7 | 3:10 | 0:40 | Concept slide | Recap: four converters on one card | Four recap lines tick in one by one with a pop; Xecxec nods after each tick |
| 8 | 3:50 | 0:40 | Bug of the Day | BUG OF THE DAY: converting text that is not a number | Butter banner drops in with a buzzer; wrong code shakes; the Python error lines appear in tomato; the fix slides in and the terminal turns mint with a ding |
| 9 | 4:30 | 0:08 | Pun card | I tried to convert my cat to an int. Python said: invalid literal. | Full tomato screen, card flips in with a rimshot, Xecxec snaps his claw |
| 10 | 4:38 | 0:20 | Challenge | Task card: ask for a number as text and double it | Task card pops in; checklist ticks with a pop; Xecxec holds a tiny pen |
| 11 | 4:58 | 0:15 | Outro | Next: Module 2 · EP 13 · if and else | Next-episode card slides up with a whoosh; right side stays empty for end-screen elements; sign-off text types in |

### Narration script

**[1 · Title]** Welcome back! This is the last episode of Module one. We have met ints, floats, strings and booleans. Today we learn to turn one into another.

**[2 · Four converters]** Python gives you four converters, named after the types they make. Int makes a whole number. Float makes a decimal. Str makes text. And bool makes True or False. Like a currency exchange, you hand over one kind of value and get another kind back. The original stays as it was. Conversion makes a new value.

**[3 · Converting in code]** [HL 1] [TRACK text=42] The text forty two, in quotes. [HL 2] [TRACK number=42] Int turns it into the number forty two. [HL 3] [TRACK price=19.5] Float turns the text nineteen point five into a decimal. [HL 4] Now we can add. Forty two plus eight is fifty. [HL 5] Nineteen point five times two is thirty nine point zero. [HL 6] Str turns the number back into text, so we can join it with fish.

**[4 · What gets cut]** Two details catch people out. First, int does not round. It simply cuts off the decimal part, so seven point nine becomes seven. If you want rounding, use the round function. Second, bool follows a simple rule. Zero and empty text are False. Everything else is True, so the word Goa is True. And if the text is not a real number, the conversion fails.

**[5 · Follow the values]** [HL 4] The text became a number, so we get fifty. [HL 5] Thirty nine point zero. [HL 6] Forty two fish. [HL 7] Seven, not eight. The decimal part is cut. [HL 8] Bool of zero is False. Bool of the word Goa is True. Predict first. What would int of minus seven point nine give? Minus seven. Int cuts towards zero.

**[6 · Run it]** Run it. Fifty. Thirty nine point zero. Forty two fish. Seven. False, True. Change the text to a word, and see what happens in the next scene.

**[7 · Recap]** Recap. One: int, float, str and bool convert one kind of value to another. Two: int cuts the decimal part and does not round. Three: bool of zero or empty text is False, and everything else is True. Four: converting text that is not a number gives a value error. That is the end of Module one. Say these ideas out loud, and give yourself a clap.

**[8 · Bug of the Day]** Bug of the Day. We ask int to convert the text abc. Python says, value error, invalid literal for int with base ten, abc. The conversion needs text that looks like a whole number. Fix the text, and it works. Check the input before you convert it.

**[9 · Pun]** I tried to convert my cat to an int. Python said: invalid literal.

**[10 · Challenge]** Your challenge: set text to the string twelve point five. Convert it to a float, double it, and print the answer.

**[11 · Outro]** Module one is done! Next: if and else, where programs start to decide. Keep coding, says Xecxec!

### Code shown

File 1: `convert.py` (scene 3, 5)

```python
text = "42"
number = int(text)
price = float("19.5")
print(number + 8)
print(price * 2)
print(str(number) + " fish")
print(int(7.9))
print(bool(0), bool("Goa"))
```

**Expected output:**

```text
50
39.0
42 fish
7
False True
```

### Bug of the Day

Wrong code (int() is given the text abc):

```python
text = "abc"
number = int(text)
print(number)
```

Python output:

```text
Traceback (most recent call last):
  File "tb.py", line 2, in <module>
    number = int(text)
ValueError: invalid literal for int() with base 10: 'abc'
```

Fixed code (the text is a valid whole number):

```python
text = "42"
number = int(text)
print(number)
```

Output of the fixed code:

```text
42
```

**Why:** int() only accepts text that looks like a whole number, so check or clean the text before converting it.

### Pun & challenge

- **Pun:** "I tried to convert my cat to an int. Python said: invalid literal."
- **Challenge:** Set text = "12.5", convert it to a float, double it and print the answer.
- **Challenge answer:** float(text) * 2 gives 25.0.

### Shorts for EP 12

**S1 · Four converters** — 0:20 · built from scene 2

- **Hook (first 1.5s):** "Four functions, four types."
- **Script:** Four functions, four types. Int, float, str and bool. Hand over one kind of value, get another kind back.
- **On-screen text:** INT FLOAT STR BOOL
- **Caption + hashtags:** Convert in 30 seconds. #python #typeconversion #beginners #kodingkonkani #goa

**S2 · Int cuts, never rounds** — 0:20 · built from scene 5

- **Hook (first 1.5s):** "Seven point nine becomes seven."
- **Script:** Seven point nine becomes seven. Int cuts off the decimal part, it does not round. Want rounding? Use round.
- **On-screen text:** INT(7.9) = 7
- **Caption + hashtags:** Cut, not round. #python #int #learntocode #kodingkonkani #coding

**S3 · Truthy and falsy** — 0:20 · built from scenes 4, 5

- **Hook (first 1.5s):** "Zero is False. Goa is True."
- **Script:** Zero is False. Empty text is False. Everything else is True, so the word Goa is True.
- **On-screen text:** BOOL(0) = FALSE
- **Caption + hashtags:** What is True? #python #bool #coding #kodingkonkani #tips

**S4 · Invalid literal** — 0:20 · built from scene 8

- **Hook (first 1.5s):** "Convert the word abc."
- **Script:** Convert the word abc with int, and Python says, value error, invalid literal. Only text that looks like a whole number works.
- **On-screen text:** VALUEERROR: INVALID LITERAL
- **Caption + hashtags:** Check before converting. #python #bugfix #valueerror #kodingkonkani #coding

**S5 · Pun and challenge** — 0:20 · built from scenes 9, 10

- **Hook (first 1.5s):** "My cat is not an int."
- **Script:** I tried to convert my cat to an int. Python said, invalid literal. Your challenge: convert twelve point five from text to a float and double it. Full video: EP 12.
- **On-screen text:** TEXT TO FLOAT, THEN DOUBLE
- **Caption + hashtags:** Try it. #python #codingchallenge #kodingkonkani #programmingjokes #goa
