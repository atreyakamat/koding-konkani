# Module 2 — Operators

Episodes 15–19 · Cream + Apricot

## EP 15 — Arithmetic operators

**Module 2 · Operators · 6:00 · Cream + Apricot · Prerequisite: EP 13**

**Learning goals:** use + - \* / % on int values and predict the result; explain why 17 / 5 is 3 and 17 % 5 is 2; use % for even/odd, last digit and minutes-to-hours; print a literal % with %%.

### YouTube

- **Title:** The % Operator Is a Superpower | C Programming EP 15
- **Description:** Plus, minus, times and divide you already know. But C's fifth operator, %, the remainder, quietly solves dozens of problems: even or odd, last digit, minutes to hours. This episode explains all five arithmetic operators line by line, plus the error you get when you use % on a float. 0:00 Is today an even day? · 0:20 The five operators · 0:55 Code: all five in action · 2:25 Division vs remainder · 3:05 Three uses of % · 4:14 Bug of the Day: % with floats · 5:04 Challenge · 5:39 Next episode
- **Tags:** arithmetic operators in c, modulus operator in c, remainder in c, integer division c, even or odd in c, c operators, c programming for beginners, koding konkani, learn c, fmod in c
- **Thumbnail:** big text "% = SUPERPOWER" in apricot on cream; a huge apricot % sign with a cape; Xecxec saluting beside it.

### Scene list

| # | Start | Length | Template | On screen | Animation & SFX |
| --- | --- | --- | --- | --- | --- |
| 1 | 0:00 | 0:15 | Concept slide | Calendar page "30" with the question "Is today an even day?"; `30 % 2 = 0` | Calendar page tears off with a paper rip SFX; question types in; the expression slams down in apricot with a thud; Xecxec nods, claw-click |
| 2 | 0:15 | 0:05 | Title card | EP 15 · ARITHMETIC OPERATORS | Title stamps in on cream with whoosh + thud; apricot underline wipe |
| 3 | 0:20 | 0:35 | Concept slide | Five operator tiles: + add, - subtract, \* multiply, / divide, % remainder | Tiles flip in one by one with a marimba note each; the % tile wobbles and gets a small apricot cape |
| 4 | 0:55 | 1:30 | Code explain | arith.c (13 lines) with a variable tracker on the right and a mini terminal below | \[HL n\] butter highlight per line; \[TRACK\] boxes for a and b fill with a pop; each printf result drops into the terminal with a soft ding |
| 5 | 2:25 | 0:40 | Memory boxes | 17 fish shared into baskets of 5: 3 full baskets, 2 fish left over; labels "17 / 5 = 3" and "17 % 5 = 2" | Fish drop into baskets with a plop each; full baskets get a mint tick; leftover 2 fish flop with a splash SFX and glow apricot |
| 6 | 3:05 | 1:05 | Code explain | day.c (12 lines): even day, minutes to hours, last digit | \[HL n\] per line; \[TRACK\] boxes for day and minutes; a clock face splits 135 minutes into 2 h + 15 min with a tick-tock SFX; 2026 shrinks to its last digit 6 |
| 7 | 4:10 | 0:04 | Pun card | "I asked % to split the bill. It only told me what was left over." | Card flips, rimshot; Xecxec holds an empty wallet |
| 8 | 4:14 | 0:50 | Bug of the Day | kg.c using `kg % 2` on a float; the GCC error; fix with fmod | Butter banner + siren blip; error prints in tomato with a buzzer; `%` morphs into `fmod(kg, 2)`; terminal turns mint with a ding |
| 9 | 5:04 | 0:35 | Challenge | "Read a number. Print n % 2. 0 means even, 1 means odd." | Number cards 7 and 12 bounce in; pencil scribble SFX; question mark pulses |
| 10 | 5:39 | 0:21 | Outro | Next: EP 16 · Relational & logical operators + subscribe | Next card slides up; Xecxec waves, claw-click; sign-off types in |

### Narration script

**\[1 · Cold open\]** Is today an even day? Today is the thirtieth. Thirty, percent sign, two, equals zero. So yes. That little percent sign is one of the most useful tools in C, and most beginners skip right past it.

**\[2 · Title\]** Arithmetic operators.

**\[3 · The five\]** C has five arithmetic operators. Plus adds. Minus subtracts. Star multiplies; we use a star because there's no times sign on the keyboard. Slash divides. And percent gives the remainder after division. It's called the modulo operator, or just mod. Four of these you've known since school. The fifth one is the superpower.

**\[4 · arith.c\]** Let's see all five. \[HL 1\] As always, we include stdio dot h for printf. \[HL 3\] Then main. \[HL 4\] int a equals 17. \[TRACK a=17\] \[HL 5\] int b equals 5. \[TRACK b=5\] \[HL 7\] Now the first printf. Inside the quotes, "a plus b equals", then percent d, which you know from EP 11 is the slot for an int. After the comma, the value to put in that slot: a plus b. C works it out first, 22, then prints it. \[HL 8\] a minus b is 12. \[HL 9\] a star b is 85. \[HL 10\] Now a slash b. 17 divided by 5 is 3.4, but this prints 3. Remember EP 13: when both numbers are ints, C does integer division and throws away the decimal part. Not rounding, just chopping. \[HL 11\] And the last line. Look at the quotes: percent percent. Because a single percent inside printf's quotes starts a slot, like percent d, we write two percents to print one real percent sign. Then a percent b gives 2. \[HL 12\] Return zero, and we're done.

**\[5 · Fish baskets\]** So what is that 2? Picture 17 fish from the Mapusa market, packed into baskets of 5. You fill three full baskets. That's 17 slash 5: 3. Two fish are left over, flapping on the table. That's 17 percent 5: 2. Division tells you how many full groups. Mod tells you what's left over. Together they always rebuild the number: 3 times 5, plus 2, is 17.

**\[6 · day.c\]** Here are three real uses. \[HL 4\] int day equals 30. \[TRACK day=30\] \[HL 5\] int minutes equals 135. \[TRACK minutes=135\] \[HL 7\] day percent 2. Any number percent 2 is either 0 or 1. Zero means even, one means odd. Thirty gives zero: even day. \[HL 8\] Next, minutes to hours. \[HL 9\] minutes slash 60 gives full hours: 2. minutes percent 60 gives the minutes left over: 15. So 135 minutes is 2 hours and 15 minutes, perfect for a bus timetable. \[HL 10\] And the last one: any number percent 10 gives its last digit. 2026 percent 10 is 6. We'll use that trick a lot in the loops module.

**\[7 · Pun\]** I asked percent to split the restaurant bill. It only told me what was left over.

**\[8 · Bug of the Day\]** Today's bug. You have 7 point 5 kilos of prawns as a float, and you want the remainder after dividing by 2. So you write kg percent 2. GCC says: error: invalid operands to binary percent, have float and int. Binary here just means "an operator with two sides", not ones and zeroes. The real point: percent only works on whole-number types like int. For decimals, include math dot h and use the function fmod, f-mod: fmod of kg comma 2. That gives 1 point 5. One extra note: printf with percent f always shows six decimal places, so you'll see 1.500000.

**\[9 · Challenge\]** Your challenge: read a number with scanf, like in EP 12, and print n percent 2. If it prints 0, the number is even. If it prints 1, it's odd. Try 7, try 12, and then try minus 7. That last one has a surprise. Comment what you got.

**\[10 · Outro\]** Next episode: comparing things. Greater than, equal to, and the operators that make decisions possible. Keep coding, says Xecxec!

### Code shown

arith.c (scene 4):

```c
#include <stdio.h>

int main() {
    int a = 17;
    int b = 5;

    printf("a + b = %d\n", a + b);
    printf("a - b = %d\n", a - b);
    printf("a * b = %d\n", a * b);
    printf("a / b = %d\n", a / b);
    printf("a %% b = %d\n", a % b);
    return 0;
}
```

**Expected output:**

```text
a + b = 22
a - b = 12
a * b = 85
a / b = 3
a % b = 2
```

day.c (scene 6):

```c
#include <stdio.h>

int main() {
    int day = 30;
    int minutes = 135;

    printf("day %% 2 = %d\n", day % 2);
    printf("%d minutes = %d hours and %d minutes\n",
           minutes, minutes / 60, minutes % 60);
    printf("Last digit of 2026 = %d\n", 2026 % 10);
    return 0;
}
```

**Expected output:**

```text
day % 2 = 0
135 minutes = 2 hours and 15 minutes
Last digit of 2026 = 6
```

### Bug of the Day

Wrong code (kg.c):

```c
#include <stdio.h>

int main() {
    float kg = 7.5;
    printf("%f\n", kg % 2);
    return 0;
}
```

GCC output:

```text
kg.c: In function 'main':
kg.c:5:23: error: invalid operands to binary % (have 'float' and 'int')
    5 |     printf("%f\n", kg % 2);
      |                       ^
```

Fixed code:

```c
#include <stdio.h>
#include <math.h>

int main() {
    float kg = 7.5;
    printf("%f\n", fmod(kg, 2));
    return 0;
}
```

```text
1.500000
```

**Why:** % is defined only for integer types in C; fmod from math.h computes the remainder for floating-point values.

### Pun & challenge

- **Pun:** "I asked % to split the restaurant bill. It only told me what was left over."
- **Challenge:** Read a number with scanf and print n % 2. Try 7, 12 and -7.
- **Challenge answer:** shown at the start of EP 16. 7 gives 1 (odd), 12 gives 0 (even), and -7 gives -1, because in C the remainder takes the sign of the left number. So for an odd test, check "not equal to 0", which EP 16 teaches.

```c
#include <stdio.h>

int main() {
    int n;
    printf("Enter a number: ");
    scanf("%d", &n);
    printf("%d %% 2 = %d\n", n, n % 2);
    return 0;
}
```

```text
Enter a number: 7
7 % 2 = 1
```

### Shorts for EP 15

**S1 · Is today an even day?** — 0:20 · built from scenes 1–2

- **Hook (first 1.5s):** "Is today an even day? C knows in one symbol."
- **Script:** Is today an even day? C knows in one symbol. Today is the thirtieth. Thirty percent two equals zero, so it's even. That percent sign is the remainder operator, and it's one of the most useful tools in C. Full episode on the channel.
- **On-screen text:** 30 % 2 = 0
- **Caption + hashtags:** One symbol, tons of uses. Meet the % operator. #cprogramming #learntocode #kodingkonkani #codingtips #maths

**S2 · / vs % in 30 seconds** — 0:35 · built from scenes 5 and 6

- **Hook (first 1.5s):** "17 divided by 5 is 3 in C. Here's where the 2 went."
- **Script:** 17 divided by 5 is 3 in C. Here's where the 2 went. Put 17 fish into baskets of 5. Three full baskets: that's 17 slash 5. Two fish left over: that's 17 percent 5. Slash gives full groups, percent gives what's left. Use it for minutes to hours: 135 slash 60 is 2 hours, 135 percent 60 is 15 minutes.
- **On-screen text:** / = GROUPS · % = LEFTOVER
- **Caption + hashtags:** Division vs remainder, explained with fish. #cprogramming #learntocode #kodingkonkani #codingtips #goa

**S3 · % on a float?** — 0:25 · built from scene 8

- **Hook (first 1.5s):** "This one symbol breaks on decimals."
- **Script:** This one symbol breaks on decimals. kg percent 2, where kg is a float. GCC says: invalid operands to binary percent, have float and int. Percent only works on whole numbers. For decimals, include math dot h and use fmod: fmod of kg comma 2.
- **On-screen text:** % + float = ERROR
- **Caption + hashtags:** Use fmod, not %, for decimals in C. #cprogramming #debugging #kodingkonkani #learntocode #gcc

**S4 · Splitting the bill** — 0:12 · built from scene 7

- **Hook (first 1.5s):** "Never ask % to split the bill."
- **Script:** Never ask percent to split the bill. I tried. It only told me what was left over.
- **On-screen text:** % ONLY KNOWS LEFTOVERS
- **Caption + hashtags:** Xecxec is still paying. #programmerhumor #cprogramming #kodingkonkani #codingmemes #maths

**S5 · What does -7 % 2 print?** — 0:20 · built from scene 9

- **Hook (first 1.5s):** "7 % 2 is 1. What is -7 % 2?"
- **Script:** 7 percent 2 is 1. So what is minus 7 percent 2 in C? 1? Minus 1? Zero? Comment your answer before it shows. Answer: minus 1. In C, the remainder takes the sign of the left number.
- **On-screen text:** -7 % 2 = ?
- **Caption + hashtags:** Most people get this wrong. Comment first, then check. #cprogramming #codingquiz #kodingkonkani #learntocode #maths

## EP 16 — Relational & logical operators

**Module 2 · Operators · 6:30 · Cream + Apricot · Prerequisite: EP 15**

**Learning goals:** use ==, !=, <, >, <=, >= and know each gives 1 (true) or 0 (false); combine conditions with &&, || and !; explain short-circuit evaluation; spot = written where == was meant.

### YouTube

- **Title:** True or False, No Maybe: == && || ! | C Programming EP 16
- **Description:** In C, every comparison answers with a number: 1 for true, 0 for false. This episode covers all six relational operators and the three logical ones (AND, OR, NOT), shows short-circuiting, and catches the most famous bug in C: one equals sign instead of two. 0:00 True or false, no maybe · 0:20 1 means true, 0 means false · 1:00 The six comparisons · 2:20 AND, OR, NOT · 3:05 Code: can you board the bus? · 4:00 Short-circuiting · 4:34 Bug of the Day: = vs == · 5:24 Challenge · 6:09 Next episode
- **Tags:** relational operators in c, logical operators in c, == vs = in c, and or not in c, short circuit evaluation, true false in c, c operators, c programming for beginners, koding konkani, learn c
- **Thumbnail:** big text "= OR ==?" in apricot on cream; one equals sign in tomato with a cross, two equals signs in mint with a tick; Xecxec squinting between them.

### Scene list

| # | Start | Length | Template | On screen | Animation & SFX |
| --- | --- | --- | --- | --- | --- |
| 1 | 0:00 | 0:15 | Concept slide | Question cards "Is it raining?", "Is the bus here?", "Maybe?" | First two cards flip to 1 and 0 with a ding each; the "Maybe?" card gets stamped "NOT IN C" in tomato with a thud; Xecxec shakes his head, claw-click |
| 2 | 0:15 | 0:05 | Title card | EP 16 · RELATIONAL & LOGICAL OPERATORS | Title stamps in on cream with whoosh + thud; apricot underline wipe |
| 3 | 0:20 | 0:40 | Concept slide | A light switch: ON = 1 = true, OFF = 0 = false; six operator tiles: == != < > <= >= | Switch flips with a click sound and the bulb lights; tiles pop in with marimba notes; == tile gets a "TWO equals" label |
| 4 | 1:00 | 1:20 | Code explain | rel.c lines 1–10 with tracker and mini terminal | \[HL n\] per line; \[TRACK\] boxes for tide and age; each result 1 or 0 drops into the terminal, 1s in mint with a ding, 0s in tomato with a soft thud |
| 5 | 2:20 | 0:45 | Concept slide | Truth tables for && and \|\| as two 2x2 grids; ! as a flip switch | Grid cells fill in one by one with a tick; the && grid shows only one mint cell; the \|\| grid shows three mint cells; the ! switch flips 1 to 0 with a click |
| 6 | 3:05 | 0:55 | Code explain | rel.c lines 12–19: bus boarding with a small Kadamba-style bus illustration | \[HL n\] per line; \[TRACK\] boxes hasTicket and busFull; bus door opens with a hiss SFX when the result is 1 |
| 7 | 4:00 | 0:30 | Code explain | sc.c: `(x != 0) && (10 / x > 1)` | \[HL 5\] left side turns tomato 0; right side greys out with a "SKIPPED" stamp and a whoosh; a "divide by zero" bomb icon fizzles out harmlessly |
| 8 | 4:30 | 0:04 | Pun card | "Why did = fail the exam? It copied the answer instead of checking it." | Card flips, rimshot; Xecxec covers his eyes |
| 9 | 4:34 | 0:50 | Bug of the Day | marks.c using `marks = 100` instead of `marks == 100`; wrong output | Butter banner + siren blip; marks tracker box is overwritten from 20 to 100 with a splash SFX; output shown in tomato with a buzzer; second = slides in, output turns mint with a ding |
| 10 | 5:24 | 0:45 | Challenge | "Is age between 18 and 60?" with a number line, 18 and 60 marked | Number line draws in; a marker slides along with a whirr; bracket region glows apricot |
| 11 | 6:09 | 0:21 | Outro | Next: EP 17 · Increment, decrement, assignment + subscribe | Next card slides up; Xecxec waves, claw-click; sign-off types in |

### Narration script

**\[1 · Cold open\]** Is it raining? Yes or no. Is the bus here? Yes or no. Maybe? Not in C. In C, every question has exactly two answers. True or false. No maybe.

**\[2 · Title\]** Relational and logical operators.

**\[3 · 1 and 0\]** First, how C says true and false. When you compare two things, C answers with a number. 1 means true. 0 means false. Like a light switch: on or off. Now the six comparison operators, also called relational operators. Double equals: is equal to. Exclamation equals: is not equal to. Less than. Greater than. Less than or equal to. Greater than or equal to. Notice the first one: equal to is written with two equals signs, not one. Remember that. It comes back later in this episode.

**\[4 · rel.c part 1\]** Let's try them. \[HL 4\] int tide equals 3, the tide level in metres at Calangute. \[TRACK tide=3\] \[HL 5\] int age equals 19. \[TRACK age=19\] \[HL 7\] tide double-equals 3: is tide equal to 3? Yes, so this prints 1. \[HL 8\] tide not-equal 3: is tide different from 3? No, so 0. \[HL 9\] age greater-than-or-equal 18: 19 is at least 18, so 1. \[HL 10\] age less-than 13: 19 is not less than 13, so 0. Every comparison becomes a 1 or a 0, and percent d prints it like any other int.

**\[5 · AND, OR, NOT\]** Real questions often have more than one part. For that, C has three logical operators. Double ampersand means AND: true only when both sides are true. Double pipe, the two vertical lines, means OR: true when at least one side is true. And a single exclamation mark means NOT: it flips true to false and false to true. Look at the tables. For AND, only one box out of four is true: both yes. For OR, three boxes are true: only both no gives false.

**\[6 · rel.c part 2\]** Now a bus question. \[HL 12\] int hasTicket equals 1, so yes, you have a ticket. \[TRACK hasTicket=1\] \[HL 13\] int busFull equals 0, so the bus is not full. \[TRACK busFull=0\] \[HL 15\] Can you board? hasTicket AND not busFull. Not busFull flips 0 into 1. So it's 1 AND 1, which gives 1. Door opens. \[HL 16\] Weekend or holiday? 0 OR 1. Only one side needs to be true, so 1. \[HL 17\] Not hasTicket: not 1 is 0. \[HL 18\] Return zero.

**\[7 · Short-circuit\]** One clever detail. \[HL 4\] Here x is 0. \[HL 5\] We ask: x is not 0, AND 10 divided by x is more than 1. Dividing by zero would crash the program. But it never happens. The left side, x not equal to 0, is already false. With AND, if the left side is false, the answer must be false, so C skips the right side completely. This is called short-circuiting. OR does the same in reverse: if the left side is already true, C skips the right side. \[HL 6\] So r is 0, and nothing crashes.

**\[8 · Pun\]** Why did the single equals sign fail the exam? It copied the answer instead of checking it.

**\[9 · Bug of the Day\]** And here's the bug that pun was about. \[HL 4\] marks is 20. \[TRACK marks=20\] \[HL 6\] You want to ask: is marks equal to 100? But you type one equals sign. GCC gives no error and no warning here. The program prints: Is it 100? 100. And then: marks is now 100. \[TRACK marks=100\] One equals sign doesn't compare. It assigns. It puts 100 into marks, and the whole expression has the value 100. Your student just got full marks for free. Fix: two equals signs. Now it prints 0, false, and marks stays 20. Read it aloud as "is equal to" every time you write double equals.

**\[10 · Challenge\]** Your challenge: read an age with scanf, and print 1 if the age is between 18 and 60, including both, and 0 if not. You need two comparisons and one logical operator. Which one, AND or OR? Comment your line of code.

**\[11 · Outro\]** Next episode: plus plus, minus minus, and the drama between i plus plus and plus plus i. Keep coding, says Xecxec!

### Code shown

rel.c (scenes 4 and 6):

```c
#include <stdio.h>

int main() {
    int tide = 3;
    int age = 19;

    printf("tide == 3  -> %d\n", tide == 3);
    printf("tide != 3  -> %d\n", tide != 3);
    printf("age >= 18  -> %d\n", age >= 18);
    printf("age < 13   -> %d\n", age < 13);

    int hasTicket = 1;
    int busFull = 0;

    printf("can board  -> %d\n", hasTicket && !busFull);
    printf("weekend or holiday -> %d\n", 0 || 1);
    printf("!hasTicket -> %d\n", !hasTicket);
    return 0;
}
```

**Expected output:**

```text
tide == 3  -> 1
tide != 3  -> 0
age >= 18  -> 1
age < 13   -> 0
can board  -> 1
weekend or holiday -> 1
!hasTicket -> 0
```

sc.c (scene 7):

```c
#include <stdio.h>

int main() {
    int x = 0;
    int r = (x != 0) && (10 / x > 1);
    printf("r = %d\n", r);
    return 0;
}
```

**Expected output:**

```text
r = 0
```

### Bug of the Day

Wrong code (marks.c):

```c
#include <stdio.h>

int main() {
    int marks = 20;

    printf("Is it 100? %d\n", marks = 100);
    printf("marks is now %d\n", marks);
    return 0;
}
```

No compile error and no warning, even with -Wall. Wrong output:

```text
Is it 100? 100
marks is now 100
```

Fixed code:

```c
#include <stdio.h>

int main() {
    int marks = 20;

    printf("Is it 100? %d\n", marks == 100);
    printf("marks is now %d\n", marks);
    return 0;
}
```

```text
Is it 100? 0
marks is now 20
```

**Why:** = stores a value and evaluates to it, while == compares and evaluates to 1 or 0; inside an if condition (EP 20) GCC with -Wall at least warns "suggest parentheses around assignment used as truth value".

### Pun & challenge

- **Pun:** "Why did the single equals sign fail the exam? It copied the answer instead of checking it."
- **Challenge:** Read an age and print 1 if it is between 18 and 60 (both included), otherwise 0.
- **Challenge answer:** shown at the start of EP 17. Use AND, because both conditions must be true.

```c
#include <stdio.h>

int main() {
    int age;
    printf("Enter age: ");
    scanf("%d", &age);
    printf("Working age? %d\n", age >= 18 && age <= 60);
    return 0;
}
```

```text
Enter age: 19
Working age? 1
```

(Entering 65 prints `Working age? 0`.)

### Shorts for EP 16

**S1 · True or false, no maybe** — 0:20 · built from scenes 1–2

- **Hook (first 1.5s):** "In C, "maybe" doesn't exist."
- **Script:** In C, maybe doesn't exist. Is it raining? 1 or 0. Is the bus here? 1 or 0. Every question in C has exactly two answers: 1 for true, 0 for false. Learn the operators that ask those questions in the full episode.
- **On-screen text:** 1 = TRUE · 0 = FALSE
- **Caption + hashtags:** C has no maybe. Only 1 and 0. #cprogramming #learntocode #kodingkonkani #codingtips #computerscience

**S2 · AND, OR, NOT in 30 seconds** — 0:40 · built from scenes 5–6

- **Hook (first 1.5s):** "Can you board the bus? C decides with two symbols."
- **Script:** Can you board the bus? C decides with two symbols. Double ampersand is AND: both sides must be true. Double pipe is OR: at least one side must be true. Exclamation mark is NOT: it flips true and false. hasTicket AND not busFull: 1 AND not 0, which is 1 AND 1. True. Door opens.
- **On-screen text:** && AND · || OR · ! NOT
- **Caption + hashtags:** Logical operators explained with a Goa bus. #cprogramming #learntocode #kodingkonkani #codingtips #goa

**S3 · One = changed the marks** — 0:25 · built from scene 9

- **Hook (first 1.5s):** "This code gave a student full marks for free."
- **Script:** This code gave a student full marks for free. marks was 20. We wanted to ask: is marks equal to 100? But we typed one equals sign. One equals assigns. Now marks is 100. No error, no warning. Fix: two equals signs to compare.
- **On-screen text:** = ASSIGNS · == COMPARES
- **Caption + hashtags:** The most famous one-character bug in C. #cprogramming #debugging #kodingkonkani #learntocode #codingtips

**S4 · The copy-cat equals sign** — 0:12 · built from scene 8

- **Hook (first 1.5s):** "Why did = fail the exam?"
- **Script:** Why did the single equals sign fail the exam? It copied the answer instead of checking it.
- **On-screen text:** = COPIES · == CHECKS
- **Caption + hashtags:** Xecxec can't look. #programmerhumor #cprogramming #kodingkonkani #codingmemes #learntocode

**S5 · Does this crash?** — 0:20 · built from scene 7

- **Hook (first 1.5s):** "x is 0. We divide by x. Does it crash?"
- **Script:** x is 0. This line divides 10 by x. Does the program crash? Comment yes or no. Answer: no. The left side, x not equal to 0, is false, so AND skips the right side completely. That's called short-circuiting.
- **On-screen text:** (x != 0) && (10 / x > 1)
- **Caption + hashtags:** Crash or no crash? Comment before the answer. #cprogramming #codingquiz #kodingkonkani #learntocode #shortcircuit

## EP 17 — Increment, decrement, assignment

**Module 2 · Operators · 6:30 · Cream + Apricot · Prerequisite: EP 16**

**Learning goals:** use ++ and -- to add or subtract 1; predict the difference between x++ (use, then add) and ++x (add, then use); use the shortcut assignments +=, -=, \*=, /=, %=; avoid changing the same variable twice in one expression.

### YouTube

- **Title:** i++ vs ++i: The Drama Explained | C Programming EP 17
- **Description:** i++ and ++i both add 1, so why do they print different numbers? This episode explains increment and decrement line by line with a live variable tracker, then covers the shortcut assignment operators +=, -=, \*=, /= and %=. Plus the one line you should never write. 0:00 i++ vs ++i · 0:20 ++ and -- · 0:45 Code: fish counter · 1:50 Post vs pre, slowly · 2:50 Shortcut assignments · 3:55 Never do this · 4:29 Bug of the Day: the roll number · 5:19 Challenge: predict 5 outputs · 6:09 Next episode
- **Tags:** i++ vs ++i, increment operator in c, pre increment post increment, decrement operator c, compound assignment c, += in c, c operators, c programming for beginners, koding konkani, learn c
- **Thumbnail:** big text "i++ vs ++i" in apricot on cream, split down the middle with a lightning bolt; Xecxec holding popcorn, watching.

### Scene list

| # | Start | Length | Template | On screen | Animation & SFX |
| --- | --- | --- | --- | --- | --- |
| 1 | 0:00 | 0:15 | Concept slide | Two boxers in corners labelled "i++" and "++i"; both print a different number | Boxing bell SFX; labels bounce; scoreboards flip to 5 and 6 with a clack; Xecxec munches popcorn, crunch SFX |
| 2 | 0:15 | 0:05 | Title card | EP 17 · INCREMENT, DECREMENT, ASSIGNMENT | Title stamps in on cream with whoosh + thud; apricot underline wipe |
| 3 | 0:20 | 0:25 | Concept slide | `x++` means `x = x + 1`; `x--` means `x = x - 1` | Long form shrinks into short form with a zip SFX; +1 and -1 chips float up |
| 4 | 0:45 | 1:05 | Code explain | inc.c lines 1–9: fish counter with tracker | \[HL n\] per line; \[TRACK fish\] box ticks 5 → 6 → 5 with a click per change; one fish jumps into a basket and back out with plop SFX |
| 5 | 1:50 | 1:00 | Memory boxes | inc.c lines 11–17: boxes a, b, c, d; two-step timeline "use" and "add" swapping order | Post: copy arrow from a to b first (whoosh), then a ticks up (click); Pre: c ticks up first (click), then copy arrow (whoosh); step labels "1" and "2" pop in apricot |
| 6 | 2:50 | 1:05 | Code explain | wallet.c with a rupee wallet tracker | \[HL n\] per line; \[TRACK rupees\] updates each line with a coin clink; long form `rupees = rupees + 50` fades in beside each line then shrinks |
| 7 | 3:55 | 0:30 | Concept slide | `i = i++ + ++i;` with a big tomato "DON'T" stamp and the GCC warning | Line types in; warning text appears with a warning beep; stamp thuds; Xecxec backs away |
| 8 | 4:25 | 0:04 | Pun card | "Why did i++ arrive late? It always finishes what it's doing first, then moves on." | Card flips, rimshot; Xecxec taps a tiny watch |
| 9 | 4:29 | 0:50 | Bug of the Day | roll.c printing `roll++` shows 41 instead of 42 | Butter banner + siren blip; tracker shows roll 41 → 42 after printing; output 41 in tomato with buzzer; `++` slides to the front, output 42 in mint with a ding |
| 10 | 5:19 | 0:50 | Challenge | ch17.c with 5 blank output lines | Lines appear one by one with a tick; blanks pulse apricot; pencil scribble SFX |
| 11 | 6:09 | 0:21 | Outro | Next: EP 18 · Bitwise operators + subscribe | Next card slides up; Xecxec waves, claw-click; sign-off types in |

### Narration script

**\[1 · Cold open\]** i plus plus. Plus plus i. Both add one. So why does one print 5, and the other print 6? Tonight's main event. Let's settle this.

**\[2 · Title\]** Increment, decrement, assignment.

**\[3 · Shortcuts\]** Adding one to a variable is so common that C gives it a shortcut. x plus plus means x equals x plus 1. It's called increment. x minus minus means x equals x minus 1. That's decrement. Fun fact: the language C plus plus got its name from this operator. It's C, plus one.

**\[4 · Fish counter\]** \[HL 4\] int fish equals 5. \[TRACK fish=5\] \[HL 6\] fish plus plus on its own line. One more fish. \[TRACK fish=6\] \[HL 7\] printf shows 6. \[HL 8\] fish minus minus. One fish escapes back into the sea. \[TRACK fish=5\] \[HL 9\] printf shows 5. When plus plus sits alone on its own line like this, it doesn't matter which side you put it on. fish plus plus and plus plus fish do exactly the same job. The drama only starts when you use the value in the same line.

**\[5 · Post vs pre\]** Here's the drama. \[HL 11\] int a equals 5. \[TRACK a=5\] \[HL 12\] int b equals a plus plus. The plus plus is after a, so this is post-increment. Post means after. Step one: use the current value of a, which is 5, and copy it into b. \[TRACK b=5\] Step two: then add one to a. \[TRACK a=6\] \[HL 13\] So a is 6, but b is 5. \[HL 15\] Now int c equals 5. \[TRACK c=5\] \[HL 16\] int d equals plus plus c. The plus plus is before c, so this is pre-increment. Pre means before. Step one: add one to c first. \[TRACK c=6\] Step two: then use the new value, 6, and copy it into d. \[TRACK d=6\] \[HL 17\] So c is 6 and d is 6. The easy way to remember: read it left to right. a plus plus: you see a first, so you use a first. Plus plus c: you see plus plus first, so you add first.

**\[6 · Shortcut assignments\]** C has shortcuts for the other operators too. \[HL 4\] Your wallet has 100 rupees. \[TRACK rupees=100\] \[HL 6\] rupees plus-equals 50. That means rupees equals rupees plus 50. A friend paid you back. \[TRACK rupees=150\] \[HL 7\] Minus-equals 30, for a cutting chai and samosas. \[TRACK rupees=120\] \[HL 8\] Times-equals 2. \[TRACK rupees=240\] \[HL 9\] Divide-equals 4. \[TRACK rupees=60\] \[HL 10\] And mod-equals 7, which keeps only the remainder of 60 divided by 7. \[TRACK rupees=4\] \[HL 12\] So the wallet prints 4. These are called compound assignment operators. They save typing, and they make the meaning clear: change this variable, using its own value.

**\[7 · Never do this\]** One warning. Sometimes you'll see puzzle questions like this: i equals i plus plus plus plus plus i. Don't write this. This line changes i more than once in one expression, and the C standard says the result is undefined. That means different compilers may give different answers, and none of them is wrong. GCC even warns you with dash Wall: operation on i may be undefined. The rule: in one expression, change a variable at most once.

**\[8 · Pun\]** Why is i plus plus always late? It finishes using what it has first, and only then moves on.

**\[9 · Bug of the Day\]** Today's bug. The last roll number in the class is 41. \[TRACK roll=41\] You want to print the next one, 42, so you write printf with roll plus plus. It prints: Next roll number: 41. Why? Post-increment. printf gets the old value, 41, first. Only after that does roll become 42. \[TRACK roll=42\] No error, no warning, just the wrong number. Fix: plus plus roll. Pre-increment adds first, so printf gets 42. Or, even clearer, do the increment on its own line, then print.

**\[10 · Challenge\]** Your challenge: pause and predict the five output lines of this program before you run it. x starts at 3. Print x plus plus. Print x. Print plus plus x. Add 10. Then y equals x minus minus, and print x and y. Write your five answers in the comments, then compile and check.

**\[11 · Outro\]** Next episode: the operators that work on the ones and zeroes inside a number. Bitwise. Keep coding, says Xecxec!

### Code shown

inc.c (scenes 4–5):

```c
#include <stdio.h>

int main() {
    int fish = 5;

    fish++;
    printf("after fish++ : %d\n", fish);
    fish--;
    printf("after fish-- : %d\n", fish);

    int a = 5;
    int b = a++;
    printf("post: a = %d, b = %d\n", a, b);

    int c = 5;
    int d = ++c;
    printf("pre : c = %d, d = %d\n", c, d);
    return 0;
}
```

**Expected output:**

```text
after fish++ : 6
after fish-- : 5
post: a = 6, b = 5
pre : c = 6, d = 6
```

wallet.c (scene 6):

```c
#include <stdio.h>

int main() {
    int rupees = 100;

    rupees += 50;
    rupees -= 30;
    rupees *= 2;
    rupees /= 4;
    rupees %= 7;

    printf("rupees = %d\n", rupees);
    return 0;
}
```

**Expected output:**

```text
rupees = 4
```

Scene 7 line (shown, never run as a lesson):

```c
i = i++ + ++i;
```

```text
warning: operation on 'i' may be undefined [-Wsequence-point]
```

### Bug of the Day

Wrong code (roll.c):

```c
#include <stdio.h>

int main() {
    int roll = 41;
    printf("Next roll number: %d\n", roll++);
    return 0;
}
```

No error or warning. Wrong output:

```text
Next roll number: 41
```

Fixed code:

```c
#include <stdio.h>

int main() {
    int roll = 41;
    printf("Next roll number: %d\n", ++roll);
    return 0;
}
```

```text
Next roll number: 42
```

**Why:** post-increment hands over the old value and adds 1 afterwards; pre-increment adds 1 first and hands over the new value.

### Pun & challenge

- **Pun:** "Why is i++ always late? It finishes using what it has first, and only then moves on."
- **Challenge:** Predict the five output lines of ch17.c before running it.

```c
#include <stdio.h>

int main() {
    int x = 3;
    printf("%d\n", x++);
    printf("%d\n", x);
    printf("%d\n", ++x);
    x += 10;
    printf("%d\n", x);
    int y = x--;
    printf("%d %d\n", x, y);
    return 0;
}
```

- **Challenge answer:** shown at the start of EP 18. x++ prints 3 then x is 4; ++x makes 5 and prints 5; += 10 gives 15; y gets 15 and x drops to 14.

```text
3
4
5
15
14 15
```

### Shorts for EP 17

**S1 · i++ vs ++i** — 0:20 · built from scenes 1–2

- **Hook (first 1.5s):** "Both add one. So why do they print different numbers?"
- **Script:** i plus plus. Plus plus i. Both add one. So why does one print 5 and the other print 6? It's all about when the adding happens. The full fight is on the channel.
- **On-screen text:** i++ vs ++i
- **Caption + hashtags:** The oldest rivalry in C. #cprogramming #learntocode #kodingkonkani #codingtips #programming

**S2 · Post vs pre in 30 seconds** — 0:40 · built from scene 5

- **Hook (first 1.5s):** "b = a++ and d = ++c. Watch the boxes."
- **Script:** b equals a plus plus, and d equals plus plus c. Watch the boxes. a is 5. Post-increment: use first, so b gets 5, then a becomes 6. c is 5. Pre-increment: add first, so c becomes 6, then d gets 6. Read left to right: whatever you see first happens first.
- **On-screen text:** a++ USE THEN ADD · ++c ADD THEN USE
- **Caption + hashtags:** Post-increment vs pre-increment, with boxes. #cprogramming #learntocode #kodingkonkani #codingtips #computerscience

**S3 · The wrong roll number** — 0:25 · built from scene 9

- **Hook (first 1.5s):** "We asked for roll number 42. C printed 41."
- **Script:** We asked for roll number 42. C printed 41. The code: printf with roll plus plus. Post-increment gives printf the old value, 41, and adds one after. Fix: plus plus roll. Add first, then print. Now it's 42.
- **On-screen text:** roll++ → 41 · ++roll → 42
- **Caption + hashtags:** One position change, different answer. #cprogramming #debugging #kodingkonkani #learntocode #codingtips

**S4 · Why i++ is always late** — 0:12 · built from scene 8

- **Hook (first 1.5s):** "Why is i++ always late?"
- **Script:** Why is i plus plus always late? It finishes using what it has first, and only then moves on.
- **On-screen text:** i++: USE FIRST, MOVE LATER
- **Caption + hashtags:** Xecxec is still waiting. #programmerhumor #cprogramming #kodingkonkani #codingmemes #learntocode

**S5 · Predict the output** — 0:25 · built from scene 10

- **Hook (first 1.5s):** "x is 3. What do these three lines print?"
- **Script:** x is 3. Line one prints x plus plus. Line two prints x. Line three prints plus plus x. Comment your three numbers. Answer: 3, then 4, then 5. Post-increment prints the old value, pre-increment prints the new one.
- **On-screen text:** x++ · x · ++x → ?
- **Caption + hashtags:** Three lines, three numbers. Comment yours. #cprogramming #codingquiz #kodingkonkani #learntocode #programming

## EP 18 — Bitwise operators

**Module 2 · Operators · 7:00 · Cream + Apricot · Prerequisite: EP 17**

**Learning goals:** write a small number in binary (up to 4 bits); work out &, |, ^, \~, << and >> bit by bit; check, set and clear one bit with a mask; tell bitwise & apart from logical &&.

### YouTube

- **Title:** Computers Only See 0s and 1s: Bitwise | C Programming EP 18
- **Description:** Inside every int is a row of tiny switches. Bitwise operators flip them directly. This episode explains binary in one minute, then & | ^ \~ << >> bit by bit with animated switch boards, and uses them to check, switch on and switch off individual bits. Plus the bug that happens when & meets &&. 0:00 Only 0s and 1s · 0:20 Binary in one minute · 1:20 AND, OR, XOR, NOT · 2:20 Code: bit.c · 3:35 Shifting left and right · 4:05 Bit masks: the light board · 5:04 Bug of the Day: & vs && · 5:54 Challenge · 6:39 Next episode
- **Tags:** bitwise operators in c, binary numbers, bitwise and or xor, left shift right shift c, bit masking in c, & vs && in c, check if bit is set, c operators, koding konkani, learn c
- **Thumbnail:** big text "0s AND 1s" in apricot on cream; a row of 4 light switches showing 1 1 0 0; Xecxec flicking one switch with a claw.

### Scene list

| # | Start | Length | Template | On screen | Animation & SFX |
| --- | --- | --- | --- | --- | --- |
| 1 | 0:00 | 0:15 | Concept slide | The number 12 dissolves into four switches 1 1 0 0 | Number shatters into switches with a glass-tinkle SFX; switches flick on/off with clicks; Xecxec's eyes widen, claw-click |
| 2 | 0:15 | 0:05 | Title card | EP 18 · BITWISE OPERATORS | Title stamps in on cream with whoosh + thud; apricot underline wipe |
| 3 | 0:20 | 1:00 | Memory boxes | Four boxes with place values 8 4 2 1; 12 = 1100 and 10 = 1010 built up | Place-value labels drop in; bits flip to 1 with a click and add up in a running total (8, +4 = 12) with a coin-clink per step |
| 4 | 1:20 | 1:00 | Concept slide | 1100 stacked over 1010; result rows for &, \|, ^, and \~ on 1100 | Columns light up one at a time left to right with a tick; result bits drop in (mint for 1, grey for 0); the \~ row flips every bit with a quick ripple click |
| 5 | 2:20 | 1:15 | Code explain | bit.c with tracker (a, b) and mini terminal | \[HL n\] per line; \[TRACK\] a=12, b=10; each result drops into terminal with a ding and its binary form shown small beside it |
| 6 | 3:35 | 0:30 | Memory boxes | 1100 slides left to 11000 (24) and right by 2 to 0011 (3) | Bits slide with a whoosh; new 0 enters from the right with a pop; bits falling off the right edge drop into the sea with a splash SFX |
| 7 | 4:05 | 0:55 | Code explain | flags.c with a board of 4 beach-shack lights numbered 3 2 1 0 | \[HL n\] per line; \[TRACK lights\] shows decimal and binary; matching bulb lights up or goes dark with a click; mask (1u << 1) appears as a stencil sliding over the board |
| 8 | 5:00 | 0:04 | Pun card | "There are 10 kinds of people: those who understand binary and those who don't." | Card flips, rimshot; Xecxec counts on two claws |
| 9 | 5:04 | 0:50 | Bug of the Day | board.c: `hasTicket & hasSeat` with 2 and 1 prints 0 | Butter banner + siren blip; 10 and 01 stack, no column matches, result 00 in tomato with a buzzer; second & slides in, result 1 in mint with a ding |
| 10 | 5:54 | 0:45 | Challenge | "Read a number n and a bit position k. Is bit k on?" | Switch row with one switch pulsing apricot; pencil scribble SFX |
| 11 | 6:39 | 0:21 | Outro | Next: EP 19 · Precedence & the ternary + subscribe | Next card slides up; Xecxec waves, claw-click; sign-off types in |

### Narration script

**\[1 · Cold open\]** You see the number 12. Your computer sees four tiny switches: on, on, off, off. Computers only see zeroes and ones. Today we learn the operators that flip those switches directly.

**\[2 · Title\]** Bitwise operators.

**\[3 · Binary in one minute\]** First, binary, in one minute. In normal numbers, each place is worth ten times the one on its right: ones, tens, hundreds. In binary, each place is worth two times the one on its right. So with four places, from right to left, they are worth 1, 2, 4 and 8. Each place holds one bit: 0 for off, 1 for on. To read a binary number, add up the places that are on. 1 1 0 0: the 8 is on, the 4 is on. 8 plus 4 is 12. 1 0 1 0: the 8 and the 2. That's 10. An int has more bits than this, usually 32, but the extra ones on the left are all zero here, so four is enough to see what's going on.

**\[4 · The operators\]** Now stack 12 on top of 10 and compare them column by column. Single ampersand is bitwise AND: the result bit is 1 only where both bits are 1. Only the 8 column matches, so 12 and 10 gives 1 0 0 0, which is 8. Single pipe is bitwise OR: 1 where at least one bit is 1. That gives 1 1 1 0, which is 14. The caret is XOR, exclusive or: 1 where the bits are different. That gives 0 1 1 0, which is 6. And the tilde is NOT: it flips every bit. Notice these look like the logical operators from EP 16, but they work on every bit separately instead of on the whole true-or-false value.

**\[5 · bit.c\]** Let's run it. \[HL 4\] unsigned int a equals 12, with a comment showing its bits. \[TRACK a=12\] We use unsigned, from EP 9, because bit tricks are simplest without negative numbers. \[HL 5\] unsigned int b equals 10. \[TRACK b=10\] \[HL 7\] a and b. We print it with percent u, the slot for an unsigned int. It prints 8. \[HL 8\] a or b: 14. \[HL 9\] a XOR b: 6. \[HL 10\] a shift-left 1: 24. We'll see why in a second. \[HL 11\] a shift-right 2: 3. \[HL 12\] And tilde a, AND 15. Tilde flips all 32 bits of a, which makes a huge number. Then AND 15, which is 1 1 1 1, keeps only the last four bits: 0 0 1 1. So it prints 3.

**\[6 · Shifts\]** Shifting slides every bit sideways. Shift-left by 1 moves all the bits one place to the left, and a new zero fills in on the right. 1 1 0 0 becomes 1 1 0 0 0, which is 24. Every shift left doubles the number. Shift-right by 2 moves the bits two places to the right; the two bits on the right edge fall off into the sea. 1 1 0 0 becomes 1 1, which is 3. Every shift right halves the number, throwing away any remainder, just like integer division in EP 15.

**\[7 · Light board\]** So why would anyone need this? Imagine a beach shack with four lights, numbered 3, 2, 1, 0 from left to right. One number can store all four as bits. \[HL 4\] lights equals 5. 5 is 0 1 0 1, so lights 0 and 2 are on. \[TRACK lights=5 (0101)\] \[HL 6\] Is light 2 on? Shift lights right by 2, so bit 2 lands at the end, then AND 1 to keep only that last bit. It prints 1. On. \[HL 7\] Light 1: shift by 1, AND 1. It prints 0. Off. \[HL 9\] Now switch light 1 on. 1u shift-left 1 makes a mask, 0 0 1 0, with only bit 1 on. The u just makes the 1 unsigned. OR with the mask turns that bit on and leaves the others alone. \[TRACK lights=7 (0111)\] \[HL 10\] It prints 7. \[HL 12\] Now switch light 0 off. The mask 1u shift-left 0 is 0 0 0 1. Tilde flips it so every bit is 1 except bit 0. AND with that clears bit 0 and keeps everything else. \[TRACK lights=6 (0110)\] \[HL 13\] It prints 6. Check, set, clear: that's how settings, permissions and hardware pins are stored in real programs.

**\[8 · Pun\]** There are 10 kinds of people in the world. Those who understand binary, and those who don't.

**\[9 · Bug of the Day\]** Today's bug mixes up single and double ampersand. \[HL 4\] hasTicket is 2, \[HL 5\] hasSeat is 1. In C, any non-zero number counts as true, so both are true. \[HL 7\] We want: can you board? But we wrote a single ampersand. It prints 0. No error, no warning. Why? Single ampersand works on bits. 2 is 1 0. 1 is 0 1. No column has a 1 in both, so the answer is 0 0: zero, false. Double ampersand is the logical AND from EP 16. It only asks: is each side non-zero? Both are, so it gives 1. For true-or-false questions, always use double ampersand. Save the single one for bits.

**\[10 · Challenge\]** Your challenge: read a number n and a bit position k with scanf, and print whether bit k of n is on, as 1 or 0. Hint: you just saw the trick with the light board. Test with n equals 5: bit 2 should be 1, bit 1 should be 0.

**\[11 · Outro\]** Next episode: why 2 plus 3 times 4 isn't 20, and C's only operator with three parts. Keep coding, says Xecxec!

### Code shown

bit.c (scene 5):

```c
#include <stdio.h>

int main() {
    unsigned int a = 12;   /* 1100 */
    unsigned int b = 10;   /* 1010 */

    printf("a & b  = %u\n", a & b);
    printf("a | b  = %u\n", a | b);
    printf("a ^ b  = %u\n", a ^ b);
    printf("a << 1 = %u\n", a << 1);
    printf("a >> 2 = %u\n", a >> 2);
    printf("~a & 15 = %u\n", ~a & 15);
    return 0;
}
```

**Expected output:**

```text
a & b  = 8
a | b  = 14
a ^ b  = 6
a << 1 = 24
a >> 2 = 3
~a & 15 = 3
```

flags.c (scene 7):

```c
#include <stdio.h>

int main() {
    unsigned int lights = 5;   /* 0101: lights 0 and 2 are on */

    printf("light 2 on? %u\n", (lights >> 2) & 1);
    printf("light 1 on? %u\n", (lights >> 1) & 1);

    lights = lights | (1u << 1);   /* switch light 1 on */
    printf("after on   = %u\n", lights);

    lights = lights & ~(1u << 0);  /* switch light 0 off */
    printf("after off  = %u\n", lights);
    return 0;
}
```

**Expected output:**

```text
light 2 on? 1
light 1 on? 0
after on   = 7
after off  = 6
```

### Bug of the Day

Wrong code (board.c):

```c
#include <stdio.h>

int main() {
    int hasTicket = 2;
    int hasSeat = 1;

    printf("Can board? %d\n", hasTicket & hasSeat);
    return 0;
}
```

No error or warning. Wrong output:

```text
Can board? 0
```

Fixed code:

```c
#include <stdio.h>

int main() {
    int hasTicket = 2;
    int hasSeat = 1;

    printf("Can board? %d\n", hasTicket && hasSeat);
    return 0;
}
```

```text
Can board? 1
```

**Why:** & compares bit by bit (10 & 01 = 00), while && only asks whether each side is non-zero, which is what a yes/no question needs.

### Pun & challenge

- **Pun:** "There are 10 kinds of people in the world: those who understand binary and those who don't."
- **Challenge:** Read a number n and a bit position k; print 1 if bit k of n is on, else 0.
- **Challenge answer:** shown at the start of EP 19. Shift the bit you want to the end, then AND 1.

```c
#include <stdio.h>

int main() {
    unsigned int n, k;
    printf("Number and bit: ");
    scanf("%u %u", &n, &k);
    printf("Bit %u of %u is %u\n", k, n, (n >> k) & 1);
    return 0;
}
```

```text
Number and bit: 5 2
Bit 2 of 5 is 1
```

(Input `5 1` prints `Bit 1 of 5 is 0`.)

### Shorts for EP 18

**S1 · Your computer sees switches** — 0:20 · built from scenes 1–2

- **Hook (first 1.5s):** "You see 12. Your computer sees this."
- **Script:** You see 12. Your computer sees four switches: on, on, off, off. 1 1 0 0. Every number is just switches. And C has operators that flip them one at a time. They're called bitwise operators. Full episode on the channel.
- **On-screen text:** 12 = 1100
- **Caption + hashtags:** Every number is secretly a row of switches. #cprogramming #binary #learntocode #kodingkonkani #computerscience

**S2 · & | ^ in 30 seconds** — 0:40 · built from scene 4

- **Hook (first 1.5s):** "12 AND 10 is 8. Here's why."
- **Script:** 12 AND 10 is 8. Here's why. 12 is 1 1 0 0. 10 is 1 0 1 0. Compare column by column. AND keeps a 1 only where both are 1: 1 0 0 0, which is 8. OR keeps a 1 where either is 1: 1 1 1 0, 14. XOR keeps a 1 where they differ: 0 1 1 0, 6.
- **On-screen text:** & BOTH · | EITHER · ^ DIFFERENT
- **Caption + hashtags:** Bitwise AND, OR and XOR, column by column. #cprogramming #binary #kodingkonkani #learntocode #codingtips

**S3 · & is not &&** — 0:25 · built from scene 9

- **Hook (first 1.5s):** "Both are true. C says false."
- **Script:** Both are true. C says false. hasTicket is 2 and hasSeat is 1, both non-zero, both true. But we wrote a single ampersand. That's bitwise AND: 1 0 and 0 1 share no bits, so the answer is 0. Use double ampersand for true-or-false questions.
- **On-screen text:** 2 & 1 = 0 · 2 && 1 = 1
- **Caption + hashtags:** One missing & and your logic breaks. #cprogramming #debugging #kodingkonkani #learntocode #codingtips

**S4 · 10 kinds of people** — 0:12 · built from scene 8

- **Hook (first 1.5s):** "There are 10 kinds of people."
- **Script:** There are 10 kinds of people in the world. Those who understand binary, and those who don't.
- **On-screen text:** 10 = TWO (IN BINARY)
- **Caption + hashtags:** If you laughed, you're one of the 10. #programmerhumor #binary #cprogramming #kodingkonkani #codingmemes

**S5 · What is 12 << 1?** — 0:20 · built from scene 6

- **Hook (first 1.5s):** "12 shifted left by one. What do you get?"
- **Script:** 12 shifted left by one. What do you get? 6? 13? 24? Comment your answer. Answer: 24. 1 1 0 0 slides left to 1 1 0 0 0. Every shift left doubles the number.
- **On-screen text:** 12 << 1 = ?
- **Caption + hashtags:** Halve it, double it, or add one? Comment first. #cprogramming #codingquiz #binary #kodingkonkani #learntocode

## EP 19 — Precedence & the ternary

**Module 2 · Operators · 6:30 · Cream + Apricot · Prerequisite: EP 18**

**Learning goals:** predict results using C's order of operations (\* / % before + -, left to right for equals); use brackets to force the order you mean; write a ternary expression condition ? a : b; spot the missing-brackets average bug and the & vs == trap.

### YouTube

- **Title:** Why 2 + 3 \* 4 Isn't 20 in C | C Programming EP 19
- **Description:** C doesn't read maths left to right; it follows an order of operations, called precedence. This episode shows the order step by step with animated brackets, then introduces C's only three-part operator, the ternary ?:. Plus the average that came out as 193. 0:00 Why 2 + 3 \* 4 isn't 20 · 0:20 The precedence ladder · 1:20 Code: prec.c · 2:30 The & trap · 3:00 The ternary ?: · 4:09 Bug of the Day: the 193 average · 4:59 Challenge · 5:39 Recap of Module 2 · 6:09 Next episode
- **Tags:** operator precedence in c, order of operations c, ternary operator in c, conditional operator c, associativity in c, c brackets, max of two numbers c, c operators, koding konkani, learn c
- **Thumbnail:** big text "2+3\*4 = 20?" in apricot on cream with 20 crossed out in tomato and 14 in mint; Xecxec holding a calculator, shocked.

### Scene list

| # | Start | Length | Template | On screen | Animation & SFX |
| --- | --- | --- | --- | --- | --- |
| 1 | 0:00 | 0:15 | Concept slide | `2 + 3 * 4` with two answers: 20 and 14 | Expression types in; "20" stamps in then gets crossed in tomato with a buzzer; "14" slides in mint with a ding; Xecxec drops his calculator, clatter SFX |
| 2 | 0:15 | 0:05 | Title card | EP 19 · PRECEDENCE & THE TERNARY | Title stamps in on cream with whoosh + thud; apricot underline wipe |
| 3 | 0:20 | 1:00 | Concept slide | Precedence ladder, top to bottom: ( ) · ! ++ -- · \* / % · + - · << >> · < > <= >= · == != · & · ^ · the pipe · && · the double pipe · ?: · = += | Rungs drop in from the top with a wooden knock each; Xecxec climbs down, pausing on \* / % and + -, which glow apricot |
| 4 | 1:20 | 1:10 | Code explain | prec.c with invisible brackets appearing | \[HL n\] per line; ghost brackets fade in around the part C does first, with a soft pop; sub-results replace sub-expressions with a click until one number remains |
| 5 | 2:30 | 0:30 | Code explain | trap.c: `x & 1 == 0` vs `(x & 1) == 0`, plus the GCC warning | Ghost brackets wrap `1 == 0` first in tomato; warning text slides in with a warning beep; real brackets snap in with a click, output turns mint |
| 6 | 3:00 | 1:05 | Code explain | tern.c with a fork-in-the-road graphic for ? and : | \[HL n\] per line; road splits in two; the condition sign flips to 1 or 0 and a tiny bus drives down the matching branch with an engine purr; chosen value drops into the tracker |
| 7 | 4:05 | 0:04 | Pun card | "The ternary operator walked up to a beach shack. Open? Fish curry rice if yes : coconut water if no." | Card flips, rimshot; Xecxec sips coconut water |
| 8 | 4:09 | 0:50 | Bug of the Day | avg.c: `a + b + c / 3` gives 193 | Butter banner + siren blip; ghost brackets wrap `c / 3` only; 193 appears in tomato with a buzzer; real brackets snap around a + b + c with a click; 80 appears in mint with a ding |
| 9 | 4:59 | 0:40 | Challenge | "Read two numbers. Print the bigger one using ?:" | Two number cards bounce in; fork-in-the-road icon pulses; pencil scribble SFX |
| 10 | 5:39 | 0:30 | Concept slide | Module 2 recap: five tiles for EP 15–19 | Tiles flip in one by one with a marimba note; a "MODULE 2 DONE" badge stamps in apricot; Xecxec does a victory scuttle |
| 11 | 6:09 | 0:21 | Outro | Next: EP 20 · if and else (Module 3: Decisions, mint + dark blue) + subscribe | Next card slides up in Module 3 colours; Xecxec waves, claw-click; sign-off types in |

### Narration script

**\[1 · Cold open\]** 2 plus 3 times 4. Quick, what's the answer? If you said 20, C disagrees. C says 14. And C is right.

**\[2 · Title\]** Precedence and the ternary.

**\[3 · The ladder\]** C doesn't simply read left to right. Some operators are stronger than others, and the stronger ones go first. This is called precedence. Think of it as a ladder. At the very top are brackets: whatever is inside brackets always goes first. Then the one-sided operators like not and plus plus. Then multiply, divide and mod. Then plus and minus. Then the shifts from EP 18. Then the comparisons, less than and greater than. Then equal and not equal. Then the bitwise ones: and, xor, or. Then the logical AND, then logical OR. Near the bottom, the ternary, which you'll meet in a minute. And right at the bottom, assignment, equals and plus-equals, which always happens last. You don't need to memorise the whole ladder today. Just remember: times and divide beat plus and minus, comparisons beat AND and OR, and brackets beat everything.

**\[4 · prec.c\]** Let's watch C work. \[HL 4\] 2 plus 3 times 4. Multiply is higher on the ladder, so C does 3 times 4 first: 12. Then 2 plus 12: 14. \[HL 5\] Want 20? Use brackets. Bracket 2 plus 3 first: 5. Then times 4: 20. \[HL 6\] 20 minus 6 minus 4. These are the same level. When operators are on the same rung, C goes left to right. 20 minus 6 is 14, minus 4 is 10. Not 20 minus 2. This left-to-right rule is called associativity. \[HL 7\] 17 slash 3 times 3. Also the same rung, so left to right. 17 slash 3 is 5, integer division from EP 13. Then 5 times 3 is 15. Not 17. \[HL 8\] 5 greater-than 3, AND, 2 greater-than 4. Comparisons are higher than AND, so they happen first: 1 AND 0, which is 0.

**\[5 · The & trap\]** Here's a trap from the bitwise episode. You want to check whether x is even by testing its last bit: x and 1, equals equals 0. \[HL 5\] Without brackets, it prints 0, even though 6 is even. Look at the ladder. Double equals is higher than single ampersand. So C first does 1 equals equals 0, which is 0, and then x and 0, which is 0. GCC with dash Wall even warns you: suggest parentheses around comparison in operand of ampersand. \[HL 6\] With brackets, x and 1 happens first, giving 0, and 0 equals equals 0 is 1. Correct. When you mix bitwise operators with comparisons, always use brackets.

**\[6 · The ternary\]** Now, the only operator in C with three parts. It's called the ternary operator, or the conditional operator. It looks like this: condition, question mark, value if true, colon, value if false. Think of a fork in the road. \[HL 4\] marks equals 72. \[TRACK marks=72\] \[HL 5\] age equals 16. \[TRACK age=16\] \[HL 7\] char result equals, marks greater-than-or-equal 40, question mark, capital P, colon, capital F. Is 72 at least 40? Yes, so the whole expression becomes P. \[TRACK result='P'\] \[HL 8\] printf with percent c, the slot for a character, prints Result: P. \[HL 10\] And the ternary can sit right inside printf. Bus fare: if age is less than 12, 10 rupees, otherwise 20. Age is 16, so the condition is false, and it picks 20. In the next module we learn if and else, which can do much bigger choices. The ternary is perfect for small ones: picking one of two values.

**\[7 · Pun\]** The ternary operator walked up to a beach shack. Is it open? Fish curry rice if yes, colon, coconut water if no. Xecxec got coconut water.

**\[8 · Bug of the Day\]** Today's bug. Three marks: 80, 90 and 70. The average should be 80. \[HL 5\] You write: int avg equals a plus b plus c slash 3. It prints: Average equals 193. What happened? Divide is higher on the ladder than plus. So C does only c slash 3 first: 70 slash 3 is 23. Then 80 plus 90 plus 23: 193. No error, no warning, just a very generous teacher. Fix: brackets. Bracket a plus b plus c, then divide by 3. 240 slash 3 is 80. If you ever feel unsure about the order, add brackets. They cost nothing.

**\[9 · Challenge\]** Your challenge: read two numbers with scanf and print the bigger one, using the ternary operator, not if. One line should do the choosing. Comment your line.

**\[10 · Recap\]** And that's Module 2 complete. EP 15: arithmetic and the mod superpower. EP 16: comparisons and logic, ones and zeroes, no maybe. EP 17: plus plus, minus minus and the shortcut assignments. EP 18: bitwise operators and switches. And today: precedence and the ternary. You now know almost every operator in C.

**\[11 · Outro\]** Next episode, a new module: decisions. Your programs start choosing their own path with if and else. Keep coding, says Xecxec!

### Code shown

prec.c (scene 4):

```c
#include <stdio.h>

int main() {
    printf("2 + 3 * 4   = %d\n", 2 + 3 * 4);
    printf("(2 + 3) * 4 = %d\n", (2 + 3) * 4);
    printf("20 - 6 - 4  = %d\n", 20 - 6 - 4);
    printf("17 / 3 * 3  = %d\n", 17 / 3 * 3);
    printf("5 > 3 && 2 > 4 = %d\n", 5 > 3 && 2 > 4);
    return 0;
}
```

**Expected output:**

```text
2 + 3 * 4   = 14
(2 + 3) * 4 = 20
20 - 6 - 4  = 10
17 / 3 * 3  = 15
5 > 3 && 2 > 4 = 0
```

trap.c (scene 5):

```c
#include <stdio.h>

int main() {
    int x = 6;
    printf("without brackets: %d\n", x & 1 == 0);
    printf("with brackets   : %d\n", (x & 1) == 0);
    return 0;
}
```

GCC with -Wall (compiles, but warns):

```text
trap.c: In function 'main':
trap.c:5:40: warning: suggest parentheses around comparison in operand of '&' [-Wparentheses]
    5 |     printf("without brackets: %d\n", x & 1 == 0);
      |                                        ^
```

**Expected output:**

```text
without brackets: 0
with brackets   : 1
```

tern.c (scene 6):

```c
#include <stdio.h>

int main() {
    int marks = 72;
    int age = 16;

    char result = (marks >= 40) ? 'P' : 'F';
    printf("Result: %c\n", result);

    printf("Bus fare: %d rupees\n", (age < 12) ? 10 : 20);
    return 0;
}
```

**Expected output:**

```text
Result: P
Bus fare: 20 rupees
```

### Bug of the Day

Wrong code (avg.c):

```c
#include <stdio.h>

int main() {
    int a = 80, b = 90, c = 70;
    int avg = a + b + c / 3;
    printf("Average = %d\n", avg);
    return 0;
}
```

No error or warning. Wrong output:

```text
Average = 193
```

Fixed code:

```c
#include <stdio.h>

int main() {
    int a = 80, b = 90, c = 70;
    int avg = (a + b + c) / 3;
    printf("Average = %d\n", avg);
    return 0;
}
```

```text
Average = 80
```

**Why:** / is higher in precedence than +, so without brackets only c is divided by 3 (70 / 3 = 23) and then added to 80 + 90.

### Pun & challenge

- **Pun:** "The ternary operator walked up to a beach shack. Open? Fish curry rice if yes : coconut water if no."
- **Challenge:** Read two numbers and print the bigger one using ?: (no if).
- **Challenge answer:** shown at the start of EP 20, which then rewrites the same program with if and else.

```c
#include <stdio.h>

int main() {
    int a, b;
    printf("Enter two numbers: ");
    scanf("%d %d", &a, &b);
    int max = (a > b) ? a : b;
    printf("Max = %d\n", max);
    return 0;
}
```

```text
Enter two numbers: 8 13
Max = 13
```

### Shorts for EP 19

**S1 · 2 + 3 \* 4 isn't 20** — 0:20 · built from scenes 1–2

- **Hook (first 1.5s):** "2 + 3 \* 4. If you said 20, C disagrees."
- **Script:** 2 plus 3 times 4. If you said 20, C disagrees. C says 14. Multiply goes before add, so it's 3 times 4 first, then plus 2. Want 20? Use brackets. Full episode on the channel.
- **On-screen text:** 2 + 3 \* 4 = 14
- **Caption + hashtags:** Your maths teacher was right all along. #cprogramming #learntocode #kodingkonkani #maths #codingtips

**S2 · The ternary in 30 seconds** — 0:35 · built from scene 6

- **Hook (first 1.5s):** "C's only operator with three parts."
- **Script:** C's only operator with three parts. Condition, question mark, value if true, colon, value if false. marks greater than or equal to 40, question mark, P, colon, F. 72 is at least 40, so you get P. Put it inside printf for a bus fare: age less than 12, 10 rupees, otherwise 20. One line, one choice.
- **On-screen text:** condition ? yes : no
- **Caption + hashtags:** The ternary operator explained with a fork in the road. #cprogramming #learntocode #kodingkonkani #codingtips #programming

**S3 · The 193 average** — 0:25 · built from scene 8

- **Hook (first 1.5s):** "80, 90 and 70. Average: 193?"
- **Script:** 80, 90 and 70. Average: 193? The code says a plus b plus c slash 3. Divide goes before plus, so only 70 gets divided: 23. Then 80 plus 90 plus 23 is 193. Fix: bracket a plus b plus c, then divide. Now it's 80.
- **On-screen text:** (a + b + c) / 3
- **Caption + hashtags:** Missing brackets, very generous teacher. #cprogramming #debugging #kodingkonkani #learntocode #codingtips

**S4 · Fish curry or coconut water?** — 0:12 · built from scene 7

- **Hook (first 1.5s):** "The ternary operator walks up to a beach shack."
- **Script:** The ternary operator walks up to a beach shack. Is it open? Fish curry rice if yes, coconut water if no. Xecxec got coconut water.
- **On-screen text:** open ? fish curry rice : coconut water
- **Caption + hashtags:** Shack was closed. #programmerhumor #cprogramming #kodingkonkani #codingmemes #goa

**S5 · What does 17 / 3 \* 3 print?** — 0:20 · built from scene 4

- **Hook (first 1.5s):** "17 / 3 \* 3. Is it 17?"
- **Script:** 17 divided by 3, times 3. Is it 17? Comment your answer. Answer: 15. Same level, so C goes left to right. 17 slash 3 is 5 with integers, and 5 times 3 is 15.
- **On-screen text:** 17 / 3 \* 3 = ?
- **Caption + hashtags:** Not 17. Comment your answer first. #cprogramming #codingquiz #kodingkonkani #learntocode #maths
