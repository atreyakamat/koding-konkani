# Module 5 — Functions

Episodes 34–40 · Lilac + Tomato

## EP 34 — What Are Functions?

**Module 5 · Functions · 6:20 · Lilac + Tomato · Prerequisite: EP 33**

**Learning goals:** define a function with no inputs and no output (`void name(void)`); call it from `main` as many times as needed; explain how control jumps into a function and comes back; fix the "implicit declaration" error by defining a function before it is called.

### YouTube

- **Title:** Stop Copy-Pasting Code: Functions | C Programming EP 34
- **Description:** Typing the same lines again and again? Functions let you write code once and use it everywhere. We build our first two functions, watch exactly how a call jumps in and back, and fix the classic "implicit declaration" error. Chapters: 0:00 The copy-paste problem · 0:25 What is a function · 1:15 Anatomy of a function · 2:00 Code walkthrough · 3:20 Running it · 3:55 How a call jumps · 4:35 Bug of the Day · 5:30 Challenge
- **Tags:** c programming, functions in c, c functions tutorial, void function c, function call c, learn c, c for beginners, implicit declaration error, koding konkani, c programming in english, class 11 computer science, gcc
- **Thumbnail:** big text "STOP COPY-PASTING"; a stack of identical code blocks with a tomato "X" over it, one clean `greet();` card beside it; Xecxec holding up one claw like a stop sign; lilac background, tomato text

### Scene list

| # | Start | Length | Template | On screen | Animation & SFX |
| --- | --- | --- | --- | --- | --- |
| 1 | 0:00 | 0:20 | Concept slide | The same 3 printf lines pasted 10 times; the code panel scrolls and scrolls | Paste sound on each copy, scroll speeds up; Xecxec's eyes spin |
| 2 | 0:20 | 0:05 | Title card | EP 34 · WHAT ARE FUNCTIONS? | Tiles slam in; claw-click |
| 3 | 0:25 | 0:50 | Concept slide | "Fish curry recipe" card: write the recipe once, cook it any day; then "define once, call many times" | Recipe card flips; 3 plates pop in one by one with a pop SFX |
| 4 | 1:15 | 0:45 | Concept slide | Labelled anatomy: `void greet(void) { ... }` with tags: return type, name, parameters, body | Each tag slides in with an arrow to its part; tick SFX |
| 5 | 2:00 | 1:20 | Code explain | `functions.c` (18 lines) | Butter line highlights on cues; call arrows drawn from main to each function |
| 6 | 3:20 | 0:35 | Terminal | `gcc functions.c -o functions` then `./functions`; output appears line by line | Typing SFX; each output line drops in |
| 7 | 3:55 | 0:05 | Pun card | Pun | Drum hit; Xecxec claw-claps |
| 8 | 4:00 | 0:35 | Concept slide | Flow of control: a glowing dot runs down main, jumps into greet, runs its body, jumps back to the next line | Whoosh on each jump, soft "boing" on return |
| 9 | 4:35 | 0:55 | Bug of the Day | `bug.c`: greet called above its definition; tomato error in terminal | Error buzzer; Xecxec facepalms; fix slides greet above main, mint tick |
| 10 | 5:30 | 0:35 | Challenge | Challenge card + expected output box | Timer ticks; Xecxec taps the card |
| 11 | 6:05 | 0:15 | Outro | Next: EP 35 · Parameters & return values | Juice-machine teaser silhouette; sign-off jingle |

### Narration script

**\[1 · Cold open\]** Look at this program. Print a line of dashes. Print a greeting. Print dashes again. Greeting again. Dashes again. Copy, paste, copy, paste. Now your teacher says, "Change the greeting." In ten places. Xecxec has already given up. There is a better way, and every real program uses it.

**\[2 · Title\]** Episode 34. What are functions?

**\[3 · What is a function\]** Think of a fish curry recipe. Your aaji writes it down once. After that, nobody rewrites the recipe every time they cook. They just say, "Make the fish curry," and follow the same steps. A function is exactly that: a named block of code that you write once and then use whenever you want. Writing it is called defining the function. Using it is called calling the function. Define once, call many times. And if the recipe needs a change, you fix it in one place, and every plate gets the new taste.

**\[4 · Anatomy\]** Every function has four parts. First, the return type: what the function gives back when it finishes. Here it is void, which means "nothing". Second, the name: greet. Names follow the same rules as variable names from EP 07. Third, the brackets with the parameters, which are the inputs. We write void inside them to say "this function takes no inputs". Fourth, the body, inside curly braces: the statements that run when the function is called. You already know one function very well: main. It is also a function. It just happens to be the one C runs first.

**\[5 · Code walkthrough\]** Here is our program with two functions. \[HL 1\] Line one, our usual include for printf. \[HL 3\] Line three: void printLine, void in brackets, open brace. We are defining a function called printLine that takes nothing and returns nothing. \[HL 4\] Its body has one job: print twenty dashes and a new line. \[HL 5\] Line five closes it. Important: defining a function does not run it. It only teaches C the recipe. \[HL 7-9\] Lines seven to nine define a second function, greet, which prints "Namaskar from Goa!". \[HL 11\] Line eleven: main, where the program actually starts. \[HL 12\] Line twelve: printLine, open bracket, close bracket, semicolon. This is a call. The empty brackets are required; they tell C "run this function now". \[HL 13\] Line thirteen calls greet. \[HL 14-16\] Lines fourteen to sixteen call them again: line, greet, line. \[HL 17\] And return zero ends main. Notice the order: both functions are written above main. C reads your file from top to bottom, so it should meet a function before you call it. Keep that in mind; it is today's bug. Now, if you want to change the greeting, you change line eight. One place. Done.

**\[6 · Running it\]** Compile it the usual way: gcc functions dot c, dash o, functions. Then run it with dot slash functions. Dashes. Namaskar from Goa. Dashes. Namaskar from Goa. Dashes. Five lines of output from five short calls.

**\[7 · Pun\]** Why did the function break up with main? Because main kept calling, but never let it return the favour.

**\[8 · How a call jumps\]** Let's follow the computer with this glowing dot. It starts at the top of main. It reaches the call to printLine, and jumps into printLine's body. It prints the dashes, hits the closing brace, and jumps back to main, to the very next line. Then it meets greet, jumps in, prints, and jumps back again. That's all a function call is: go there, do the job, come back to where you left. Like a Kadamba bus going to Panjim and coming back to the same stop.

**\[9 · Bug of the Day\]** Today's bug: calling before declaring. Here, main calls greet on line four, but greet is only written on line eight, below main. When the compiler reaches line four, it has never heard of greet. On the GCC that MSYS2 installs today, which is version 14 or newer, you get this error: implicit declaration of function greet. In plain English: "You used greet, but nobody introduced greet to me." On older GCC 13 it is only a warning, but it is still a bug, so treat it as one. The simple fix: move the whole greet function above main. Now the compiler meets greet first, and the call works. In EP 36 you'll learn a second fix, called a prototype.

**\[10 · Challenge\]** Your challenge: write a function called welcome that prints a three-line banner: a row of stars, the words "Welcome, coder!", and another row of stars. Then call it three times from main. Pause, type it, run it. The answer is pinned in the comments and shown at the start of the next episode.

**\[11 · Outro\]** Today our functions took nothing in and gave nothing back. Next episode, we feed them inputs and get answers out: parameters and return values. Keep coding, says Xecxec!

### Code shown

```c
#include <stdio.h>

void printLine(void) {
    printf("--------------------\n");
}

void greet(void) {
    printf("Namaskar from Goa!\n");
}

int main(void) {
    printLine();
    greet();
    printLine();
    greet();
    printLine();
    return 0;
}
```

**Expected output** (`gcc functions.c -o functions` then `./functions`):

```text
--------------------
Namaskar from Goa!
--------------------
Namaskar from Goa!
--------------------
```

### Bug of the Day

Wrong code (`bug.c`):

```c
#include <stdio.h>

int main(void) {
    greet();
    return 0;
}

void greet(void) {
    printf("Namaskar from Goa!\n");
}
```

GCC 14 and newer (current MSYS2 UCRT64) stop with an error; GCC 13 prints the same line as a warning and still builds:

```text
bug.c: In function 'main':
bug.c:4:5: error: implicit declaration of function 'greet' [-Wimplicit-function-declaration]
    4 |     greet();
      |     ^~~~~
```

A "conflicting types for 'greet'" message follows on line 8. Fixed code:

```c
#include <stdio.h>

void greet(void) {
    printf("Namaskar from Goa!\n");
}

int main(void) {
    greet();
    return 0;
}
```

```text
Namaskar from Goa!
```

Why: C reads the file top to bottom, so a function must be defined (or declared, EP 36) before the line that calls it.

### Pun & challenge

- **Pun:** Why did the function break up with main? Main kept calling, but never let it return the favour.
- **Challenge:** Write `void welcome(void)` that prints a row of stars, "  Welcome, coder!", and another row of stars. Call it three times from main.
- **Challenge answer:**

```c
#include <stdio.h>

void welcome(void) {
    printf("********************\n");
    printf("  Welcome, coder!\n");
    printf("********************\n");
}

int main(void) {
    welcome();
    welcome();
    welcome();
    return 0;
}
```

### Shorts for EP 34

**S1 · Stop Copy-Pasting Your Code** — 0:30 · built from scenes 1–3

- **Hook (first 1.5s):** the code panel scrolling endlessly with paste sounds
- **Script:** Print dashes. Print a greeting. Dashes again. Greeting again. Copy, paste, copy, paste. Now change the greeting in ten places. Or don't. Write it once as a function, give it a name, and call that name whenever you need it. Change it in one place, and every call updates. That's functions in C, and it starts in episode 34.
- **On-screen text:** STOP COPY-PASTING · WRITE IT ONCE
- **Caption + hashtags:** Your code does not need ten copies of the same lines. #cprogramming #learntocode #kodingkonkani #functions #codinglife

**S2 · Functions in 30 Seconds** — 0:30 · built from scenes 4–5

- **Hook (first 1.5s):** `void greet(void)` with four tags popping on
- **Script:** A function in C has four parts. Return type: what it gives back. void means nothing. Name: greet. Brackets: the inputs. void means none. Body: the code in curly braces. Defining it teaches C the recipe. Calling it, greet with empty brackets and a semicolon, actually runs it. Define once, call many times.
- **On-screen text:** RETURN TYPE · NAME · INPUTS · BODY
- **Caption + hashtags:** Every C function, explained in four parts. #cprogramming #learntocode #kodingkonkani #ctutorial #programmingbasics

**S3 · Bug: Implicit Declaration** — 0:35 · built from scene 9

- **Hook (first 1.5s):** red error text "implicit declaration of function 'greet'"
- **Script:** You call greet in main, and GCC says: implicit declaration of function greet. Why? Because greet is written below main. C reads top to bottom, so at that line it has never met greet. Move the function above main, and it compiles. Next time GCC says "implicit declaration", it means: introduce your function first.
- **On-screen text:** "WHO IS greet?" — GCC
- **Caption + hashtags:** The most common first-function error in C, fixed. #cprogramming #debugging #kodingkonkani #gcc #learntocode

**S4 · The Function Breakup** — 0:12 · built from scene 7

- **Hook (first 1.5s):** Xecxec holding a broken heart labelled `return`
- **Script:** Why did the function break up with main? Main kept calling, but never let it return the favour.
- **On-screen text:** MAIN KEPT CALLING
- **Caption + hashtags:** Programmer relationships are complicated. #codingmemes #cprogramming #kodingkonkani #programmerhumor #learntocode

**S5 · Quiz: Where Does It Return?** — 0:25 · built from scene 8

- **Hook (first 1.5s):** "After greet() finishes, where does C go?"
- **Script:** main calls printLine, then greet, then printLine. After greet finishes, where does the program continue? A: the start of main. B: the line right after the greet call. C: the end of the program. Think for three seconds. The answer is B. A function always returns to the line right after the call.
- **On-screen text:** A · B · C — WHERE DOES IT GO BACK?
- **Caption + hashtags:** Comment your answer before the reveal. #cprogramming #codingquiz #kodingkonkani #learntocode #functions

## EP 35 — Parameters & Return Values

**Module 5 · Functions · 6:35 · Lilac + Tomato · Prerequisite: EP 34**

**Learning goals:** write functions that take one or more parameters; return a value with `return` and store or print it in the caller; tell parameters (in the definition) from arguments (in the call); spot and fix a missing return in a non-void function.

### YouTube

- **Title:** A Function Is a Juice Machine | C Programming EP 35
- **Description:** Put fruit in, get juice out. That is exactly how parameters and return values work in C. We write square and average functions, nest one call inside another, and fix the sneaky "missing return" bug that gives you wrong answers without any error. Chapters: 0:00 The juice machine · 0:25 Parameters and arguments · 1:15 return · 1:55 Code walkthrough · 3:45 Running it · 4:15 Bug of the Day · 5:45 Challenge
- **Tags:** c programming, function parameters c, return value c, arguments vs parameters, c functions, learn c, c for beginners, control reaches end of non-void function, koding konkani, class 12 computer science, gcc, c tutorial
- **Thumbnail:** big text "INPUT IN, ANSWER OUT"; a juice machine with `7` going in the top and `49` coming out of the tap; Xecxec sipping from a glass with a straw; lilac background, tomato text

### Scene list

| # | Start | Length | Template | On screen | Animation & SFX |
| --- | --- | --- | --- | --- | --- |
| 1 | 0:00 | 0:20 | Concept slide | Juice machine: a mango goes in, mango juice comes out; then a `7` goes in, `49` comes out | Blender whirr; glass clinks down |
| 2 | 0:20 | 0:05 | Title card | EP 35 · PARAMETERS & RETURN VALUES | Tiles slam in; claw-click |
| 3 | 0:25 | 0:50 | Concept slide | `int square(int n)` with `n` tagged "parameter"; `square(7)` with `7` tagged "argument"; arrow copies 7 into n | Value 7 flies from the call into the box labelled n; pop SFX |
| 4 | 1:15 | 0:40 | Concept slide | `return result;` sends a value back; return type `int` must match | Value 49 rides an arrow back to the call site, replacing `square(7)` |
| 5 | 1:55 | 1:50 | Code explain | `params.c` (18 lines) | Butter highlights; variable tracker for n, result, s |
| 6 | 3:45 | 0:25 | Terminal | Compile and run; 3 output lines | Typing SFX; lines drop in |
| 7 | 4:10 | 0:05 | Pun card | Pun | Drum hit; Xecxec spits out juice |
| 8 | 4:15 | 1:30 | Bug of the Day | `bug.c`: `bigger` with no return on one path; GCC warning; wrong output differs by build | Warning in butter; output "Bigger: 3" with a tomato cross; fix adds `return b;` |
| 9 | 5:45 | 0:35 | Challenge | Challenge card: add two numbers read from the user | Timer ticks |
| 10 | 6:20 | 0:15 | Outro | Next: EP 36 · Prototypes & header files | Two files shaking hands; sign-off jingle |

### Narration script

**\[1 · Cold open\]** At the juice stall near Calangute beach, you hand over a mango, and the machine hands back mango juice. You don't care what happens inside. Fruit goes in, juice comes out. In C, functions can work exactly like this. A number goes in, and an answer comes out.

**\[2 · Title\]** Episode 35. Parameters and return values.

**\[3 · Parameters and arguments\]** Last episode, our functions had void in the brackets: no inputs. Now look at this: int square, open bracket, int n. That n is a parameter. It is a variable that belongs to the function, waiting to receive a value. When we call square, open bracket, 7, the 7 is called an argument. On the call, C copies the argument into the parameter, so n becomes 7. Easy way to remember: the parameter is the empty glass, the argument is the juice you pour in. A function can have many parameters, separated by commas, and each one needs its own type.

**\[4 · return\]** Now the output. The word before the function name, int, is the return type. It promises: "I will give back a whole number." The return statement keeps that promise. return result sends the value back to whoever called the function, and the function stops right there. Back in main, the whole expression square of 7 is replaced by that answer. So you can store it, print it, or even pass it to another function.

**\[5 · Code walkthrough\]** Let's read the code. \[HL 3\] Line three: int square, int n. One parameter, returns an int. \[HL 4\] Line four: int result equals n times n. \[HL 5\] Line five: return result. \[HL 8\] Line eight: float average, int a, comma, int b. Two parameters, and it returns a float. \[HL 9\] Line nine: return, a plus b, divided by 2.0f. Why 2.0f and not 2? Remember EP 13: int divided by int throws away the decimal. Dividing by 2.0f makes it a float division, so we keep the point five. \[HL 12\] Now main. \[HL 13\] Line thirteen: int s equals square of 7. \[TRACK n=7\] The 7 is copied into n. \[TRACK result=49\] result becomes 49. The function returns 49, \[TRACK s=49\] and s becomes 49. \[HL 14\] Line fourteen prints "7 squared is 49". \[HL 15\] Line fifteen calls average of 4 and 7 right inside printf. We don't need a variable. The answer, 5.5, goes straight into the percent point one f. \[HL 16\] Line sixteen is fun: square of square of 3. C solves the inside first. \[TRACK n=3\] Square of 3 gives 9. \[TRACK n=9\] Then square of 9 gives 81. A function call can be an argument to another function call. \[HL 17\] And return zero ends main.

**\[6 · Running it\]** Compile and run. 7 squared is 49. Average of 4 and 7 is 5.5. Square of square of 3 is 81. Three answers from two little machines.

**\[7 · Pun\]** Why did the function go to therapy? It had too many issues it couldn't return to.

**\[8 · Bug of the Day\]** Today's bug: the missing return. Look at bigger. If a is greater than b, it returns a. But what if it isn't? The function reaches the closing brace without returning anything. Compile with dash Wall, and GCC warns: control reaches end of non-void function. That means "you promised an int, but on one path you gave nothing back." Here is the scary part. It is only a warning, so the program still runs. When we call bigger of 3 and 9, the answer should be 9, but on our test machine it printed 3. With optimisation turned on, it printed 0. The value is garbage, whatever was lying around. This is called undefined behaviour, and your result may be different. The fix is one line: after the if, return b. Now every path returns a value. Rule: if a function is not void, every path must end in a return. And always compile with dash Wall so GCC can warn you.

**\[9 · Challenge\]** Your challenge: write a function add that takes two ints and returns their sum. In main, read two numbers from the user with scanf, call add, and print the result. If the user types 12 and 30, your program should print "Sum = 42". Pause and try it.

**\[10 · Outro\]** So far, every function had to sit above main. Next episode, we learn how to introduce a function early with a prototype, and how to split code across files with a header. Keep coding, says Xecxec!

### Code shown

```c
#include <stdio.h>

int square(int n) {
    int result = n * n;
    return result;
}

float average(int a, int b) {
    return (a + b) / 2.0f;
}

int main(void) {
    int s = square(7);
    printf("7 squared is %d\n", s);
    printf("Average of 4 and 7 is %.1f\n", average(4, 7));
    printf("Square of square(3) is %d\n", square(square(3)));
    return 0;
}
```

**Expected output:**

```text
7 squared is 49
Average of 4 and 7 is 5.5
Square of square(3) is 81
```

### Bug of the Day

Wrong code (`bug.c`):

```c
#include <stdio.h>

int bigger(int a, int b) {
    if (a > b) {
        return a;
    }
}

int main(void) {
    printf("Bigger: %d\n", bigger(3, 9));
    return 0;
}
```

`gcc -Wall bug.c -o bug` prints:

```text
bug.c: In function 'bigger':
bug.c:7:1: warning: control reaches end of non-void function [-Wreturn-type]
    7 | }
      | ^
```

It still builds. Output on our test machine (on screen: "undefined behaviour, your output may differ"):

```text
Bigger: 3
```

With `-O2` the same code printed `Bigger: 0`. Fixed code:

```c
#include <stdio.h>

int bigger(int a, int b) {
    if (a > b) {
        return a;
    }
    return b;
}

int main(void) {
    printf("Bigger: %d\n", bigger(3, 9));
    return 0;
}
```

```text
Bigger: 9
```

Why: a non-void function must return a value on every path; falling off the end gives the caller garbage.

### Pun & challenge

- **Pun:** Why did the function go to therapy? It had too many issues it couldn't return to.
- **Challenge:** Write `int add(int a, int b)`. Read two numbers with scanf, call add, print `Sum = ...`. Input `12 30` should print `Sum = 42`.
- **Challenge answer:**

```c
#include <stdio.h>

int add(int a, int b) {
    return a + b;
}

int main(void) {
    int x, y;
    printf("Enter two numbers: ");
    scanf("%d %d", &x, &y);
    printf("Sum = %d\n", add(x, y));
    return 0;
}
```

```text
Enter two numbers: 12 30
Sum = 42
```

### Shorts for EP 35

**S1 · A Function Is a Juice Machine** — 0:25 · built from scenes 1 and 3

- **Hook (first 1.5s):** a `7` dropping into a juice machine
- **Script:** Mango in, juice out. 7 in, 49 out. That's a C function with a parameter and a return value. The parameter is the empty glass waiting inside the function. The argument is what you pour in when you call it. And return hands the answer back.
- **On-screen text:** 7 IN · 49 OUT
- **Caption + hashtags:** The juice-stall way to understand C functions. #cprogramming #learntocode #kodingkonkani #functions #ctutorial

**S2 · Parameter vs Argument in 30s** — 0:30 · built from scenes 3–4

- **Hook (first 1.5s):** "Parameter or argument? Most students mix these up."
- **Script:** In int square, int n, the n is a parameter: a variable inside the function. In square of 7, the 7 is an argument: the actual value you send. On the call, the argument is copied into the parameter. Then return sends the answer back, and square of 7 becomes 49 right there in your code.
- **On-screen text:** PARAMETER = GLASS · ARGUMENT = JUICE
- **Caption + hashtags:** Never mix these up in a viva again. #cprogramming #learntocode #kodingkonkani #computerscience #exams

**S3 · The Missing Return Bug** — 0:40 · built from scene 8

- **Hook (first 1.5s):** output "Bigger: 3" with a big tomato question mark
- **Script:** Bigger of 3 and 9 should be 9. This program printed 3. Why? The function returns a only when a is bigger. Otherwise it falls off the end and returns garbage. GCC even warned: control reaches end of non-void function. Add return b at the end, and you get 9. Every path in a non-void function needs a return.
- **On-screen text:** BIGGER OF 3 AND 9 = 3??
- **Caption + hashtags:** No error, wrong answer. The worst kind of bug. #cprogramming #debugging #kodingkonkani #gcc #learntocode

**S4 · Therapy for Functions** — 0:12 · built from scene 7

- **Hook (first 1.5s):** Xecxec lying on a therapist's couch shaped like curly braces
- **Script:** Why did the function go to therapy? It had too many issues it couldn't return to.
- **On-screen text:** ISSUES IT COULDN'T RETURN TO
- **Caption + hashtags:** Even functions need someone to talk to. #codingmemes #programmerhumor #kodingkonkani #cprogramming #learntocode

**S5 · Quiz: square(square(3))** — 0:25 · built from scene 5

- **Hook (first 1.5s):** `square(square(3))` = ?
- **Script:** square returns n times n. What does square of square of 3 print? A: 9. B: 18. C: 81. The inner call runs first: square of 3 is 9. Then square of 9 is 81. The answer is C.
- **On-screen text:** square(square(3)) = ?
- **Caption + hashtags:** Comment A, B or C before the reveal. #cprogramming #codingquiz #kodingkonkani #learntocode #functions

## EP 36 — Prototypes & Header Files

**Module 5 · Functions · 7:00 · Lilac + Tomato · Prerequisite: EP 35**

**Learning goals:** write a function prototype so a function can be defined below main; explain the difference between a declaration and a definition; split a program into `main.c`, `shapes.c` and `shapes.h` and compile them together with one gcc command; read a "conflicting types" error caused by a prototype that does not match.

Scope note: this episode is the introduction. Include guards, multi-file libraries and reuse across projects come in EP 82 (Build your own header library).

### YouTube

- **Title:** Introduce Your Function First: Prototypes | C Programming EP 36
- **Description:** Why does C complain when main calls a function written below it? Prototypes fix that, and they are also the secret behind every #include. We write our first prototypes, make our first header file, and compile a two-file program. Chapters: 0:00 Introduce yourself first · 0:25 Prototype vs definition · 1:15 Code walkthrough · 2:35 What is a .h file · 3:20 Splitting into files · 4:50 Compiling two files · 5:25 Bug of the Day · 6:25 Challenge
- **Tags:** c programming, function prototype c, header files in c, declaration vs definition, multiple files c, gcc compile multiple files, include header c, learn c, c for beginners, conflicting types error, koding konkani, gcc
- **Thumbnail:** big text "INTRODUCE YOURSELF"; a name-tag sticker reading `int cube(int n);`; Xecxec wearing the name tag and waving; lilac background, tomato text

### Scene list

| # | Start | Length | Template | On screen | Animation & SFX |
| --- | --- | --- | --- | --- | --- |
| 1 | 0:00 | 0:20 | Concept slide | First day of college: a stranger walks up and asks for your notes. Then the same stranger with a name tag | Crowd murmur; name tag sticks on with a slap |
| 2 | 0:20 | 0:05 | Title card | EP 36 · PROTOTYPES & HEADER FILES | Tiles slam in; claw-click |
| 3 | 0:25 | 0:50 | Concept slide | Two cards: "Declaration (prototype)" = `int cube(int n);` and "Definition" = full function with body | Semicolon on the prototype glows tomato; tick SFX |
| 4 | 1:15 | 1:20 | Code explain | `prototype.c` (18 lines): prototypes on top, main, definitions below | Butter highlights; arrows from prototypes to definitions |
| 5 | 2:35 | 0:45 | Concept slide | `#include <stdio.h>` opens to reveal a file full of prototypes, including printf's | File icon unfolds like a menu card; paper rustle |
| 6 | 3:20 | 1:30 | Code explain | Three panels side by side: `shapes.h`, `shapes.c`, `main.c` | Each panel slides in; `#include "shapes.h"` line pastes the header's text in with a copy animation |
| 7 | 4:50 | 0:30 | Terminal | `gcc main.c shapes.c -o shapes` then `./shapes`; then the linker error when shapes.c is left out | Typing SFX; tomato text for the error |
| 8 | 5:20 | 0:05 | Pun card | Pun | Drum hit; Xecxec adjusts his name tag |
| 9 | 5:25 | 1:00 | Bug of the Day | `bug.c`: prototype says int, definition says float | Error buzzer; prototype and definition shake side by side; fix makes them match, mint tick |
| 10 | 6:25 | 0:20 | Challenge | Challenge card: split EP 35's square and average into mymaths.h / mymaths.c | Timer ticks |
| 11 | 6:45 | 0:15 | Outro | Next: EP 37 · Scope & lifetime | Variable in a locked room; sign-off jingle |

### Narration script

**\[1 · Cold open\]** First day of college. A stranger walks up and says, "Give me your notes." You'd say, "Who are you?" Now the same person walks up wearing a name tag: "Hi, I'm Rohan, from your class." Much better. The C compiler feels the same way. In EP 34, calling a function before C had met it gave us an error. Today we learn how a function can introduce itself first.

**\[2 · Title\]** Episode 36. Prototypes and header files.

**\[3 · Prototype vs definition\]** A function prototype is a one-line introduction. Look: int cube, open bracket, int n, close bracket, semicolon. It tells the compiler three things: the name, what goes in, and what comes out. No body, no curly braces, just a semicolon. This is called a declaration. The full function, with its body, is the definition. You can declare a function at the top of the file and define it anywhere below, even after main. The compiler reads the prototype, says "OK, I know cube now", and happily accepts calls to it.

**\[4 · Code walkthrough\]** \[HL 3\] Line three: the prototype for cube. Takes an int, returns an int, ends with a semicolon. \[HL 4\] Line four: the prototype for showResult. Takes two ints, returns nothing. \[HL 6\] Line six: main. This time main sits near the top, so anyone opening the file sees the main story first. \[HL 7\] Line seven: int c equals cube of 4. The compiler has not seen cube's body yet, but it has seen the prototype, so it knows this call is correct. \[TRACK c=64\] \[HL 8\] Line eight calls showResult with 4 and c. \[HL 12-14\] Lines twelve to fourteen: the real definition of cube. Return n times n times n. \[HL 16-18\] Lines sixteen to eighteen: the definition of showResult, which prints "Cube of 4 is 64". One rule: the prototype and the definition must match exactly. Same return type, same name, same parameter types. Remember that rule; it is today's bug.

**\[5 · What is a .h file\]** Here's a secret. Since EP 04 you have typed hash include, stdio dot h. What is inside that file? Mostly prototypes! Somewhere inside it is the prototype for printf. The real body of printf lives in a library that gets linked in when you build. A file that ends in dot h is a header file. Its job is to introduce functions. When you write hash include, the preprocessor copies that file's text into yours, right at that line. So all those introductions arrive before your code uses them.

**\[6 · Splitting into files\]** Now let's make our own. Panel one, shapes dot h. It holds just two prototypes: rectArea and rectPerimeter, each taking a length and a width. No bodies. Panel two, shapes dot c. \[HL shapes.c 1\] It starts with hash include, "shapes dot h", in double quotes. Double quotes mean "look in my own folder first". Angle brackets, like stdio dot h, mean "look in the system's folders". \[HL shapes.c 3-5\] Then the definition of rectArea, returning length times width. \[HL shapes.c 7-9\] And rectPerimeter, returning 2 times, length plus width. Panel three, main dot c. \[HL main.c 1-2\] It includes stdio dot h for printf and shapes dot h for our functions. \[HL main.c 5\] l is 8, w is 5. \[HL main.c 6-7\] It prints the area and the perimeter. main dot c never sees the function bodies. It only needs the introductions. Think of it like a restaurant: the header is the menu, the dot c file is the kitchen, and main is the customer who orders from the menu.

**\[7 · Compiling two files\]** To build it, list both dot c files: gcc main dot c, shapes dot c, dash o, shapes. Never list the dot h file; it is already pasted in by include. Run it: Area 40, Perimeter 26. What if you forget shapes dot c? Then the compiler is happy, because the prototypes are there, but the linker cannot find the kitchen. You get "undefined reference to rectArea". On Windows the path in the message looks longer, but the key words are the same. If you see "undefined reference", check that every dot c file is in your gcc command.

**\[8 · Pun\]** Why did the header file get invited to every party? Because it always made a great first declaration.

**\[9 · Bug of the Day\]** Today's bug: the mismatched prototype. The prototype at the top says int half, int n. But the definition below says float half, float n. The compiler compares them and stops: conflicting types for half; have float of float. Then a note: previous declaration of half with type int of int. The introduction and the real person don't match, so the compiler refuses. The fix: make the prototype an exact copy of the definition's first line, plus a semicolon. Now half of 9 gives 4.5. Pro tip: copy and paste the first line of the definition to make your prototype. No typing mistakes.

**\[10 · Challenge\]** Your challenge: take square and average from EP 35. Put their prototypes in mymaths dot h, their definitions in mymaths dot c, and call them from main dot c. Compile both dot c files together and get the same output as last episode.

**\[11 · Outro\]** Next episode: where do variables live, and when do they disappear? Scope and lifetime. Keep coding, says Xecxec!

### Code shown

File 1: `prototype.c`

```c
#include <stdio.h>

int cube(int n);
void showResult(int n, int value);

int main(void) {
    int c = cube(4);
    showResult(4, c);
    return 0;
}

int cube(int n) {
    return n * n * n;
}

void showResult(int n, int value) {
    printf("Cube of %d is %d\n", n, value);
}
```

```text
Cube of 4 is 64
```

File 2: `shapes.h`

```c
// shapes.h - prototypes only
int rectArea(int length, int width);
int rectPerimeter(int length, int width);
```

File 3: `shapes.c`

```c
#include "shapes.h"

int rectArea(int length, int width) {
    return length * width;
}

int rectPerimeter(int length, int width) {
    return 2 * (length + width);
}
```

File 4: `main.c`

```c
#include <stdio.h>
#include "shapes.h"

int main(void) {
    int l = 8, w = 5;
    printf("Area: %d\n", rectArea(l, w));
    printf("Perimeter: %d\n", rectPerimeter(l, w));
    return 0;
}
```

Build and run:

```bash
gcc main.c shapes.c -o shapes
./shapes
```

```text
Area: 40
Perimeter: 26
```

Forgetting `shapes.c` (`gcc main.c -o shapes`) gives a linker error; the path before it differs on Windows:

```text
main.c:(.text+0x25): undefined reference to `rectArea'
main.c:(.text+0x4a): undefined reference to `rectPerimeter'
collect2: error: ld returned 1 exit status
```

### Bug of the Day

Wrong code (`bug.c`):

```c
#include <stdio.h>

int half(int n);

int main(void) {
    printf("%d\n", half(9));
    return 0;
}

float half(float n) {
    return n / 2;
}
```

GCC error:

```text
bug.c:10:7: error: conflicting types for 'half'; have 'float(float)'
   10 | float half(float n) {
      |       ^~~~
bug.c:3:5: note: previous declaration of 'half' with type 'int(int)'
    3 | int half(int n);
      |     ^~~~
```

Fixed code:

```c
#include <stdio.h>

float half(float n);

int main(void) {
    printf("%.1f\n", half(9));
    return 0;
}

float half(float n) {
    return n / 2;
}
```

```text
4.5
```

Why: a prototype is a promise about the function's types, so it must match the definition exactly (and the printf format must match the new float return).

### Pun & challenge

- **Pun:** Why did the header file get invited to every party? It always made a great first declaration.
- **Challenge:** Move `square` and `average` from EP 35 into `mymaths.h` (prototypes) and `mymaths.c` (definitions); call them from `main.c`; build with `gcc main.c mymaths.c -o maths`.
- **Challenge answer:**

```c
// mymaths.h
int square(int n);
float average(int a, int b);
```

```c
// mymaths.c
#include "mymaths.h"

int square(int n) {
    return n * n;
}

float average(int a, int b) {
    return (a + b) / 2.0f;
}
```

```c
// main.c
#include <stdio.h>
#include "mymaths.h"

int main(void) {
    printf("7 squared is %d\n", square(7));
    printf("Average of 4 and 7 is %.1f\n", average(4, 7));
    return 0;
}
```

```text
7 squared is 49
Average of 4 and 7 is 5.5
```

### Shorts for EP 36

**S1 · Introduce Yourself First** — 0:25 · built from scenes 1 and 3

- **Hook (first 1.5s):** a stranger asking "Give me your notes"
- **Script:** A stranger asks for your notes. Who are you? Same with C. Call a function the compiler hasn't met, and it complains. The fix is a prototype: one line at the top, like int cube, int n, semicolon. Name, inputs, output. Now the compiler knows who cube is, and you can write the body anywhere below.
- **On-screen text:** NAME TAG FOR YOUR FUNCTION
- **Caption + hashtags:** A prototype is your function's name tag. #cprogramming #learntocode #kodingkonkani #functions #ctutorial

**S2 · What's Inside stdio.h?** — 0:30 · built from scene 5

- **Hook (first 1.5s):** `#include <stdio.h>` cracking open like a box
- **Script:** You've typed include stdio dot h a hundred times. What's inside? Mostly prototypes. One of them introduces printf. The include line copies that file's text into your program, so the compiler meets printf before you use it. A dot h file is a list of introductions. A dot c file has the real code.
- **On-screen text:** .h = MENU · .c = KITCHEN
- **Caption + hashtags:** The secret behind every #include. #cprogramming #learntocode #kodingkonkani #computerscience #headerfiles

**S3 · Conflicting Types Bug** — 0:35 · built from scene 9

- **Hook (first 1.5s):** tomato error "conflicting types for 'half'"
- **Script:** The prototype says int half, int n. The definition says float half, float n. GCC stops: conflicting types for half. The introduction doesn't match the real function. Fix: copy the definition's first line, add a semicolon, and that's your prototype. Now they match and it compiles.
- **On-screen text:** PROTOTYPE ≠ DEFINITION
- **Caption + hashtags:** Copy the first line, add a semicolon. Done. #cprogramming #debugging #kodingkonkani #gcc #learntocode

**S4 · The Party Guest** — 0:12 · built from scene 8

- **Hook (first 1.5s):** a `.h` file icon in a party hat
- **Script:** Why did the header file get invited to every party? Because it always made a great first declaration.
- **On-screen text:** A GREAT FIRST DECLARATION
- **Caption + hashtags:** Header files: the life of the party. #codingmemes #programmerhumor #kodingkonkani #cprogramming #learntocode

**S5 · Quiz: Which Files Go in gcc?** — 0:25 · built from scene 7

- **Hook (first 1.5s):** three file icons: main.c, shapes.c, shapes.h
- **Script:** Your program has main dot c, shapes dot c and shapes dot h. Which gcc command is right? A: gcc main dot c. B: gcc main dot c shapes dot c. C: gcc main dot c shapes dot h. The answer is B. List every dot c file. The header is already pulled in by include.
- **On-screen text:** A · B · C — WHICH COMPILES?
- **Caption + hashtags:** Comment your answer, then check. #cprogramming #codingquiz #kodingkonkani #gcc #learntocode

## EP 37 — Scope & Lifetime

**Module 5 · Functions · 6:40 · Lilac + Tomato · Prerequisite: EP 36**

**Learning goals:** say where a local, global or static local variable can be used (scope) and how long it lives (lifetime); predict the output of a function that uses a `static` counter; recognise a shadowed variable and turn on `-Wshadow` to catch it.

### YouTube

- **Title:** What Happens in a Function Stays There | C Programming EP 37
- **Description:** Why can't main see a variable you made inside a function? Why does a static variable remember its value? We cover local, global and static variables with a simple fish-market example, and catch a sneaky shadowed variable. Chapters: 0:00 What happens in a function · 0:25 Scope and lifetime · 1:25 Local vs global vs static · 2:15 Code walkthrough · 4:05 Running it · 4:40 Bug of the Day · 5:50 Challenge
- **Tags:** c programming, variable scope c, local and global variables, static variable c, lifetime of variables, shadowing c, Wshadow, learn c, c for beginners, koding konkani, class 12 computer science, gcc
- **Thumbnail:** big text "STAYS IN THE FUNCTION"; a variable box locked inside a room shaped like curly braces; Xecxec peeking through the keyhole; lilac background, tomato text

### Scene list

| # | Start | Length | Template | On screen | Animation & SFX |
| --- | --- | --- | --- | --- | --- |
| 1 | 0:00 | 0:20 | Concept slide | A variable `basket` made inside a function; main tries to print it; tomato error `'basket' undeclared` | Door slams shut on the box; error buzzer |
| 2 | 0:20 | 0:05 | Title card | EP 37 · SCOPE & LIFETIME | Tiles slam in; claw-click |
| 3 | 0:25 | 1:00 | Concept slide | Two words: SCOPE = where you can use it; LIFETIME = how long it exists. Fish-market picture: each stall's basket (local), the market clock tower (global), the stall owner's notebook (static) | Each picture pops in with its label; market chatter bed |
| 4 | 1:25 | 0:50 | Memory boxes | Three boxes: local appears and vanishes with each call; global sits above everything; static stays after the call | Local box fades in/out with a puff; static box glows lilac |
| 5 | 2:15 | 1:50 | Code explain | `scope.c` (26 lines) | Butter highlights; trackers for total, basket, visits, fresh |
| 6 | 4:05 | 0:30 | Terminal | Compile and run; 5 output lines | Typing SFX |
| 7 | 4:35 | 0:05 | Pun card | Pun | Drum hit; Xecxec puts on sunglasses |
| 8 | 4:40 | 1:10 | Bug of the Day | `bug.c`: inner `int score` hides the outer one; output 10 instead of 25 | Two score boxes, inner one covers outer like a shadow; -Wshadow warning in butter; fix removes `int`, mint tick |
| 9 | 5:50 | 0:35 | Challenge | Challenge card: ticket counter with static | Timer ticks |
| 10 | 6:25 | 0:15 | Outro | Next: EP 38 · Call by value | Two cups swapping and failing; sign-off jingle |

### Narration script

**\[1 · Cold open\]** Here's a function that makes a variable called basket. Back in main, we try to print basket. And GCC says: basket undeclared. But we made it! Yes, inside the function. And what happens in a function stays in the function.

**\[2 · Title\]** Episode 37. Scope and lifetime.

**\[3 · Scope and lifetime\]** Two words today. Scope means: where in the code can I use this variable? Lifetime means: how long does it exist while the program runs? Picture the Mapusa fish market. Each stall has its own basket. You can't reach into another stall's basket; that's a local variable. The big clock in the middle of the market, everyone can see; that's a global variable. And the stall owner's notebook, which stays at the stall and remembers yesterday's sales; that's a static local variable. Let's see each one in C.

**\[4 · Memory boxes\]** A local variable is made inside a function. Its scope is only that function's curly braces. It is created when the function is called and destroyed when the function returns. Call again, and you get a brand-new one. A global variable is made outside all functions, at the top of the file. Every function can use it, and it lives for the whole program. A static local variable is made inside a function with the word static. Its scope is still only that function, but its lifetime is the whole program. It is set up once, and it keeps its value between calls.

**\[5 · Code walkthrough\]** \[HL 3\] Line three: int total equals zero, outside every function. This is global. \[HL 5\] Line five: addFish, taking count. Parameters are locals too. \[HL 6\] Line six: int basket equals count. A local, only alive inside addFish. \[HL 7\] Line seven adds basket to the global total. addFish can see total because it is global. \[HL 8\] Line eight prints both. \[HL 11\] Line eleven: function visit. \[HL 12\] Line twelve: static int visits equals zero. This zero is set only once, before the program starts using it, not on every call. \[HL 13\] Line thirteen: int fresh equals zero. A normal local, set to zero on every call. \[HL 14-15\] Lines fourteen and fifteen add one to each. \[HL 16\] Line sixteen prints them. Now main. \[HL 20\] addFish of 5: \[TRACK basket=5\] basket is 5, \[TRACK total=5\] total becomes 5. When addFish returns, basket is destroyed. \[HL 21\] addFish of 3: a brand-new basket, \[TRACK basket=3\] 3, and \[TRACK total=8\] total becomes 8, because the global remembers. \[HL 22\] First visit: \[TRACK visits=1\] visits is 1, \[TRACK fresh=1\] fresh is 1. \[HL 23\] Second visit: \[TRACK visits=2\] visits is 2, but fresh starts again at zero and becomes 1. \[HL 24\] Third visit: \[TRACK visits=3\] visits 3, fresh still 1. That's the difference: the static remembers, the local forgets. One warning about globals: they're handy, but any function can change them, which makes bugs hard to find. Use locals and parameters first; use a global only when you really must.

**\[6 · Running it\]** Compile and run. Basket 5, total 5. Basket 3, total 8. Then visits 1, 2, 3, while fresh stays 1 every time.

**\[7 · Pun\]** Why don't local variables go to parties? Because they never get out of their function.

**\[8 · Bug of the Day\]** Today's bug: the shadowed variable. score starts at 10. The loop runs three times and adds 5 each time, so we expect 25. But the program prints 10. Look at line six: int score equals zero, inside the loop. That int creates a new, second score that only lives inside the loop's braces. It hides, or shadows, the outer one. All the adding happens to the inner score, which dies at the end of each loop round. The outer score never changes. GCC doesn't complain, not even with dash Wall. You need an extra flag, dash Wshadow. Then GCC says: declaration of score shadows a previous local. The fix: delete the word int, and the loop uses the outer score. Now it prints 25. Add dash Wshadow to your compile command, and GCC will catch this for you.

**\[9 · Challenge\]** Your challenge: the bus-stand ticket counter. Write a function nextTicket that returns 101 the first time, 102 the second time, 103 the third, using a static variable. Call it three times in a loop and print "Your ticket: " and the number.

**\[10 · Outro\]** Next episode: why passing a variable to a function gives the function a copy, and why our swap function won't swap. Keep coding, says Xecxec!

### Code shown

```c
#include <stdio.h>

int total = 0;              // global: visible everywhere

void addFish(int count) {
    int basket = count;     // local: lives only inside addFish
    total = total + basket;
    printf("Basket: %d, Total: %d\n", basket, total);
}

void visit(void) {
    static int visits = 0;  // static local: remembers between calls
    int fresh = 0;          // normal local: reset every call
    visits++;
    fresh++;
    printf("visits = %d, fresh = %d\n", visits, fresh);
}

int main(void) {
    addFish(5);
    addFish(3);
    visit();
    visit();
    visit();
    return 0;
}
```

**Expected output:**

```text
Basket: 5, Total: 5
Basket: 3, Total: 8
visits = 1, fresh = 1
visits = 2, fresh = 1
visits = 3, fresh = 1
```

Cold-open snippet (scene 1), where main tries to use `basket`, gives:

```text
error: 'basket' undeclared (first use in this function)
```

### Bug of the Day

Wrong code (`bug.c`):

```c
#include <stdio.h>

int main(void) {
    int score = 10;
    for (int i = 0; i < 3; i++) {
        int score = 0;
        score = score + 5;
    }
    printf("Final score: %d\n", score);
    return 0;
}
```

`gcc bug.c` and `gcc -Wall bug.c` give no message at all. Wrong output:

```text
Final score: 10
```

With `gcc -Wall -Wshadow bug.c -o bug`:

```text
bug.c: In function 'main':
bug.c:6:13: warning: declaration of 'score' shadows a previous local [-Wshadow]
    6 |         int score = 0;
      |             ^~~~~
bug.c:4:9: note: shadowed declaration is here
    4 |     int score = 10;
      |         ^~~~~
```

Fixed code:

```c
#include <stdio.h>

int main(void) {
    int score = 10;
    for (int i = 0; i < 3; i++) {
        score = score + 5;
    }
    printf("Final score: %d\n", score);
    return 0;
}
```

```text
Final score: 25
```

Why: writing `int` again inside the loop makes a new local that hides the outer variable, so the outer one is never updated.

### Pun & challenge

- **Pun:** Why don't local variables go to parties? They never get out of their function.
- **Challenge:** Write `int nextTicket(void)` using a `static` counter so it returns 101, 102, 103 on successive calls. Print three tickets from a loop.
- **Challenge answer:**

```c
#include <stdio.h>

int nextTicket(void) {
    static int ticket = 100;
    ticket++;
    return ticket;
}

int main(void) {
    for (int i = 0; i < 3; i++) {
        printf("Your ticket: %d\n", nextTicket());
    }
    return 0;
}
```

```text
Your ticket: 101
Your ticket: 102
Your ticket: 103
```

### Shorts for EP 37

**S1 · What Happens in a Function Stays There** — 0:25 · built from scene 1 and 4

- **Hook (first 1.5s):** tomato error "'basket' undeclared"
- **Script:** We made basket inside a function. main tries to print it. Error: basket undeclared. Why? A local variable only exists inside its own function. It is born when the function is called and destroyed when it returns. What happens in a function stays in the function.
- **On-screen text:** LOCAL = STAYS INSIDE
- **Caption + hashtags:** Why main can't see your function's variables. #cprogramming #learntocode #kodingkonkani #scope #ctutorial

**S2 · static in 30 Seconds** — 0:30 · built from scenes 5–6

- **Hook (first 1.5s):** "visits = 1, 2, 3 but fresh = 1, 1, 1"
- **Script:** Two variables inside the same function. fresh is a normal local: it is reset to zero on every call. visits is static: it is set up once and keeps its value between calls. Call the function three times. visits counts 1, 2, 3. fresh is stuck at 1. Static means: same scope, longer memory.
- **On-screen text:** static = REMEMBERS
- **Caption + hashtags:** The keyword that gives a function a memory. #cprogramming #learntocode #kodingkonkani #computerscience #static

**S3 · The Shadow Bug** — 0:35 · built from scene 8

- **Hook (first 1.5s):** "Expected 25. Got 10."
- **Script:** score starts at 10, the loop adds 5 three times, but it prints 10. The culprit: int score inside the loop. That creates a second score that hides the first. No warning, even with dash Wall. Add dash Wshadow, and GCC points right at it. Delete that int, and you get 25.
- **On-screen text:** EXPECTED 25 · GOT 10
- **Caption + hashtags:** One extra word, one silent bug. #cprogramming #debugging #kodingkonkani #gcc #learntocode

**S4 · Local Variables at Parties** — 0:12 · built from scene 7

- **Hook (first 1.5s):** Xecxec at a party, a variable box stuck behind curly-brace bars
- **Script:** Why don't local variables go to parties? Because they never get out of their function.
- **On-screen text:** NEVER GETS OUT
- **Caption + hashtags:** Introvert variables, explained. #codingmemes #programmerhumor #kodingkonkani #cprogramming #learntocode

**S5 · Quiz: Global, Local or Static?** — 0:25 · built from scenes 3–4

- **Hook (first 1.5s):** "Which variable remembers between calls but can't be seen outside?"
- **Script:** Which kind of variable keeps its value between calls but can only be used inside its function? A: global. B: local. C: static local. The answer is C. A global is visible everywhere. A local forgets. A static local remembers, but stays private.
- **On-screen text:** GLOBAL · LOCAL · STATIC?
- **Caption + hashtags:** Comment your answer before the reveal. #cprogramming #codingquiz #kodingkonkani #learntocode #exams

## EP 38 — Call by Value

**Module 5 · Functions · 6:10 · Lilac + Tomato · Prerequisite: EP 37**

**Learning goals:** explain that C passes a copy of each argument to a function; trace why a swap function changes only its own copies; get a changed value back to the caller using `return`; know that pointers (EP 55) are the real fix for swap.

### YouTube

- **Title:** Why My Swap Didn't Swap: Call by Value | C Programming EP 38
- **Description:** You wrote a perfect swap function. Inside, it swaps. Back in main, nothing changed. Why? Because C gives every function a photocopy of your variables. We trace it in memory, fix a related bug with return, and set up the real fix that comes with pointers. Chapters: 0:00 The swap that didn't · 0:20 Photocopies · 1:05 Code walkthrough · 2:40 Memory view · 3:30 Running it · 3:55 Bug of the Day · 5:05 Challenge
- **Tags:** c programming, call by value c, swap function c, why swap not working c, function arguments copy, pass by value, learn c, c for beginners, koding konkani, class 12 computer science, c interview question, gcc
- **Thumbnail:** big text "SWAP FAILED?"; two cups labelled x=5 and y=9 with a broken swap arrow between them; Xecxec confused, holding a photocopy; lilac background, tomato text

### Scene list

| # | Start | Length | Template | On screen | Animation & SFX |
| --- | --- | --- | --- | --- | --- |
| 1 | 0:00 | 0:15 | Terminal | Output: "Inside swap: a = 9, b = 5" then "Back in main: x = 5, y = 9" | Mint tick on line 1, tomato cross on line 2; record-scratch SFX |
| 2 | 0:15 | 0:05 | Title card | EP 38 · CALL BY VALUE | Tiles slam in; claw-click |
| 3 | 0:20 | 0:45 | Concept slide | Photocopy machine: your class notes go in, a copy comes out; a friend scribbles on the copy; your original is clean | Photocopier whirr; pen scribble SFX |
| 4 | 1:05 | 1:35 | Code explain | `swap.c` (15 lines) | Butter highlights; trackers for x, y, a, b, temp |
| 5 | 2:40 | 0:50 | Memory boxes | Two frames: main's boxes x=5, y=9; swap's boxes a, b, temp; values copied across, swapped inside, then swap's frame vanishes | Copy arrows; swap's frame crumbles with a paper-tear SFX |
| 6 | 3:30 | 0:20 | Terminal | Compile and run; 2 output lines | Typing SFX |
| 7 | 3:50 | 0:05 | Pun card | Pun | Drum hit; Xecxec holds up a photocopy of himself |
| 8 | 3:55 | 1:10 | Bug of the Day | `bug.c`: addBonus changes its copy; marks stays 70; fix returns the new value | Two marks boxes; one turns 80 then vanishes; fix arrow carries 80 back, mint tick |
| 9 | 5:05 | 0:50 | Challenge | Challenge card: explain the swap bug in 2 sentences + teaser of `&x` | Timer ticks; lilac pointer arrow teaser |
| 10 | 5:55 | 0:15 | Outro | Next: EP 39 · Recursion | Mirror inside a mirror; sign-off jingle |

### Narration script

**\[1 · Cold open\]** Inside the swap function: a is 9, b is 5. Swapped! Back in main: x is 5, y is 9. Not swapped. The function did its job, and still nothing changed. Today we find out who is lying.

**\[2 · Title\]** Episode 38. Call by value.

**\[3 · Photocopies\]** Your friend wants your physics notes. You don't hand over your only copy. You go to the xerox shop near college and give a photocopy. Your friend can write all over that photocopy. Your original stays clean. C does exactly this with function arguments. When you call a function, C copies the value of each argument into the function's parameter. This is called call by value. The function works on the copy. The caller's variable is never touched.

**\[4 · Code walkthrough\]** \[HL 3\] Line three: void swap, int a, int b. Two parameters, nothing returned. \[HL 4\] Line four: int temp equals a. We save a in temp. \[HL 5\] Line five: a equals b. \[HL 6\] Line six: b equals temp. This is the classic three-step swap. Like swapping two glasses of drink using an empty third glass. \[HL 7\] Line seven prints a and b inside swap. \[HL 11\] Now main. Line eleven: \[TRACK x=5\] x is 5, \[TRACK y=9\] y is 9. \[HL 12\] Line twelve: swap of x and y. C copies the values: \[TRACK a=5\] a gets 5, \[TRACK b=9\] b gets 9. Inside swap, \[TRACK temp=5\] temp becomes 5, \[TRACK a=9\] a becomes 9, \[TRACK b=5\] b becomes 5. Printed: a equals 9, b equals 5. Then swap returns, and a, b and temp are destroyed, just like the locals in EP 37. \[HL 13\] Line thirteen prints x and y. \[TRACK x=5\] \[TRACK y=9\] Still 5 and 9. The swap really happened, but only to the photocopies.

**\[5 · Memory view\]** Here's the same thing in memory. main has two boxes, x and y, at their own addresses. When swap is called, C builds a new set of boxes for swap: a, b and temp. The values 5 and 9 are copied across. Notice the arrows go one way only: from main into swap. Inside, a and b swap. When swap ends, its boxes are thrown away. Nothing ever travelled back to x and y. To change x and y themselves, swap would need their addresses, not their values. That's exactly what pointers give us, in EP 55.

**\[6 · Running it\]** Compile and run. Inside swap: a equals 9, b equals 5. Back in main: x equals 5, y equals 9. Now you know why.

**\[7 · Pun\]** Why did the variable refuse to change? It was told it was only being passed by value.

**\[8 · Bug of the Day\]** Today's bug: expecting changes outside. Here, addBonus takes marks and adds 10. In main, marks is 70, we call addBonus, then print. Output: 70. No error, no warning. The function added 10 to its own copy, and the copy vanished. For a single value, the fix is easy: make the function return the new value, and assign it back. int addBonus returns marks plus 10, and in main we write marks equals addBonus of marks. Now it prints 80. The rule: a function can't change the caller's variables through normal parameters. If you want a result back, return it.

**\[9 · Challenge\]** Your challenge is a thinking one. In two sentences, explain to a friend why our swap didn't swap. Write it in the comments. Bonus: return can only send back one value, but swap needs to change two. So how could we fix it? Here's a hint: the ampersand you've been typing in scanf since EP 12. scanf can change your variable because you give it the address. Hold on to that idea for the pointers module.

**\[10 · Outro\]** Next episode: a function that calls itself. Recursion. Keep coding, says Xecxec!

### Code shown

```c
#include <stdio.h>

void swap(int a, int b) {
    int temp = a;
    a = b;
    b = temp;
    printf("Inside swap: a = %d, b = %d\n", a, b);
}

int main(void) {
    int x = 5, y = 9;
    swap(x, y);
    printf("Back in main: x = %d, y = %d\n", x, y);
    return 0;
}
```

**Expected output:**

```text
Inside swap: a = 9, b = 5
Back in main: x = 5, y = 9
```

### Bug of the Day

Wrong code (`bug.c`):

```c
#include <stdio.h>

void addBonus(int marks) {
    marks = marks + 10;
}

int main(void) {
    int marks = 70;
    addBonus(marks);
    printf("Marks: %d\n", marks);
    return 0;
}
```

No error or warning, even with `-Wall -Wextra`. Wrong output:

```text
Marks: 70
```

Fixed code:

```c
#include <stdio.h>

int addBonus(int marks) {
    return marks + 10;
}

int main(void) {
    int marks = 70;
    marks = addBonus(marks);
    printf("Marks: %d\n", marks);
    return 0;
}
```

```text
Marks: 80
```

Why: the parameter is a copy of main's `marks`, so the change must come back through `return` and be assigned.

### Pun & challenge

- **Pun:** Why did the variable refuse to change? It was told it was only being passed by value.
- **Challenge:** In two sentences, explain why `swap(x, y)` did not swap x and y. Bonus: how could a function change two of main's variables?
- **Challenge answer:** C passes copies of x and y into a and b, so swap only swaps its own copies, which are destroyed when it returns. To change main's variables, pass their addresses (`swap(&x, &y)` with `int *a, int *b`), covered in EP 55.

### Shorts for EP 38

**S1 · Why My Swap Didn't Swap** — 0:30 · built from scenes 1 and 4

- **Hook (first 1.5s):** "Inside: swapped. Outside: not swapped."
- **Script:** Inside swap, a is 9 and b is 5. Swapped. Back in main, x is still 5 and y is still 9. The function swapped perfectly, just not your variables. C handed it copies. It swapped the copies, then threw them away. That's call by value.
- **On-screen text:** SWAPPED... THE COPIES
- **Caption + hashtags:** The most famous beginner bug in C. #cprogramming #learntocode #kodingkonkani #functions #codinginterview

**S2 · Call by Value in 30 Seconds** — 0:30 · built from scenes 3 and 5

- **Hook (first 1.5s):** a photocopier spitting out a sheet with `5` on it
- **Script:** When you call a function in C, it gets a photocopy of each argument. It can scribble on the copy all it wants. Your original variable stays the same. When the function ends, the copies are thrown away. Want a result back? Use return. Want to change the original? You'll need its address. That's pointers.
- **On-screen text:** FUNCTIONS GET PHOTOCOPIES
- **Caption + hashtags:** Call by value, explained with a xerox shop. #cprogramming #learntocode #kodingkonkani #computerscience #exams

**S3 · The Bonus That Vanished** — 0:30 · built from scene 8

- **Hook (first 1.5s):** "Marks: 70" with a tomato cross
- **Script:** addBonus adds 10 to marks. Marks was 70. After the call: still 70. The function added 10 to its copy, then the copy disappeared. Fix: return marks plus 10, and write marks equals addBonus of marks. Now it's 80.
- **On-screen text:** WHERE DID MY 10 MARKS GO?
- **Caption + hashtags:** No error, no bonus. #cprogramming #debugging #kodingkonkani #gcc #learntocode

**S4 · Passed by Value** — 0:12 · built from scene 7

- **Hook (first 1.5s):** a variable box shrugging
- **Script:** Why did the variable refuse to change? It was told it was only being passed by value.
- **On-screen text:** ONLY PASSED BY VALUE
- **Caption + hashtags:** Variables have feelings too. #codingmemes #programmerhumor #kodingkonkani #cprogramming #learntocode

**S5 · Quiz: What Does It Print?** — 0:25 · built from scene 8

- **Hook (first 1.5s):** `addBonus(marks);` with marks = 70
- **Script:** marks is 70. We call addBonus of marks, which adds 10 to its parameter. Then we print marks. A: 70. B: 80. C: error. The answer is A, 70. The function changed a copy, not the original.
- **On-screen text:** 70 · 80 · ERROR?
- **Caption + hashtags:** Comment your answer before the reveal. #cprogramming #codingquiz #kodingkonkani #learntocode #functions

## EP 39 — Recursion

**Module 5 · Functions · 6:50 · Lilac + Tomato · Prerequisite: EP 38**

**Learning goals:** explain recursion as a function that calls itself on a smaller problem; write a base case and a recursive case; trace `factorial(4)` on the call stack, going down and coming back up; recognise the crash caused by a missing base case.

### YouTube

- **Title:** A Function That Calls Itself: Recursion | C Programming EP 39
- **Description:** Recursion sounds scary, but it's just a function that solves a small piece and asks itself to do the rest. We build a countdown and a factorial, watch every call pile up on the call stack, and crash a program on purpose by forgetting the base case. Chapters: 0:00 A function that calls itself · 0:20 The two rules · 1:10 Countdown · 2:05 Factorial · 3:15 The call stack · 4:20 Running it · 4:45 Bug of the Day · 5:55 Challenge
- **Tags:** c programming, recursion in c, recursive function c, factorial recursion, base case, call stack, stack overflow, learn c, c for beginners, koding konkani, class 12 computer science, gcc
- **Thumbnail:** big text "IT CALLS ITSELF"; a function card holding a phone, calling a smaller copy of itself, which calls a smaller copy; Xecxec on the smallest phone; lilac background, tomato text

### Scene list

| # | Start | Length | Template | On screen | Animation & SFX |
| --- | --- | --- | --- | --- | --- |
| 1 | 0:00 | 0:15 | Concept slide | Queue at a bus stand: "How many people are in front of me?" Each person asks the one ahead | Whisper SFX passes down the line; answers come back up with counting pops |
| 2 | 0:15 | 0:05 | Title card | EP 39 · RECURSION | Tiles slam in; claw-click |
| 3 | 0:20 | 0:50 | Concept slide | Two rules: 1. Base case (when to stop) 2. Recursive case (call yourself with a smaller problem) | Rule cards stamp down; stop-sign icon on rule 1 |
| 4 | 1:10 | 0:55 | Code explain | `recursion.c` lines 1–10: countdown | Butter highlights; each call draws a smaller card |
| 5 | 2:05 | 1:10 | Code explain | `recursion.c` lines 12–17: factorial | Butter highlights; tracker for n |
| 6 | 3:15 | 1:05 | Memory boxes | Call stack: frames for factorial(4), (3), (2), (1) stack up; then pop off with return values 1, 2, 6, 24 | Stack-up thunk per frame; pop SFX; return values ride arrows up |
| 7 | 4:20 | 0:20 | Terminal | Compile and run; 6 output lines | Typing SFX |
| 8 | 4:40 | 0:05 | Pun card | Pun | Drum hit; Xecxec dizzy |
| 9 | 4:45 | 1:10 | Bug of the Day | `bug.c`: factorial with no base case; GCC warning; stack frames pile past the top of the screen; crash | Frames pile up faster and faster, screen shakes, crash sound; fix adds base case, mint tick |
| 10 | 5:55 | 0:40 | Challenge | Challenge card: factorial of a number the user enters, up to 20 | Timer ticks |
| 11 | 6:35 | 0:15 | Outro | Next: EP 40 · Recursion practice | Mirror inside a mirror; sign-off jingle |

### Narration script

**\[1 · Cold open\]** You're in a long queue at the Panjim bus stand and you want to know your position. You can't see the front. So you ask the person ahead: "What's your position?" They don't know either, so they ask the person ahead of them. This goes on until the very first person says, "I'm number one." Then the answers come back: two, three, four, all the way to you. That is recursion.

**\[2 · Title\]** Episode 39. Recursion.

**\[3 · The two rules\]** A recursive function is a function that calls itself. Every recursive function needs two parts. First, a base case: a simple situation where the answer is known and the function stops calling itself. In the queue, it's the first person saying "I'm number one". Second, a recursive case: the function solves a smaller version of the same problem by calling itself, and then uses that answer. Every call must move closer to the base case. Without a base case, it never stops.

**\[4 · Countdown\]** Let's start simple. \[HL 3\] Line three: void countdown, int n. \[HL 4\] Line four: if n equals zero. That's our base case. \[HL 5-6\] Print "Blast off!" and return, which stops this call. \[HL 8\] Otherwise, line eight prints n. \[HL 9\] Line nine: countdown of n minus one. The function calls itself with a smaller number. So countdown of 3 prints 3, then calls countdown of 2, which prints 2, then countdown of 1, which prints 1, then countdown of 0, which hits the base case and prints "Blast off!". Each call is one step closer to zero. No loop anywhere, but it behaves like one.

**\[5 · Factorial\]** Now a classic exam favourite: factorial. 4 factorial, written 4 with an exclamation mark, means 4 times 3 times 2 times 1, which is 24. Notice something: 4 factorial is 4 times 3 factorial. And 3 factorial is 3 times 2 factorial. The problem contains a smaller copy of itself. \[HL 12\] Line twelve: int factorial, int n. \[HL 13-14\] Lines thirteen and fourteen: if n is less than or equal to 1, return 1. That's the base case, because 1 factorial and 0 factorial are both 1. \[HL 16\] Line sixteen: return n times factorial of n minus 1. That's the recursive case. \[TRACK n=4\] For 4, it needs factorial of 3 first, so it waits.

**\[6 · The call stack\]** How does C keep track of all these waiting calls? With the call stack. Think of a stack of plates. factorial of 4 is called: a new frame, a plate, goes on the stack, holding its own n equals 4. It calls factorial of 3: another plate on top, with its own n equals 3. Then 2. Then 1. Remember EP 37: each call gets its own local variables, so the four n's never mix. Now factorial of 1 hits the base case and returns 1. Its plate comes off. factorial of 2 can now finish: 2 times 1 is 2. Plate off. factorial of 3: 3 times 2 is 6. Plate off. factorial of 4: 4 times 6 is 24. Last plate off, and 24 goes back to main. Going down, we pile up. Coming back, we multiply.

**\[7 · Running it\]** Compile and run. 3, 2, 1, Blast off! 4 factorial equals 24. 5 factorial equals 120.

**\[8 · Pun\]** To understand recursion, you must first understand recursion.

**\[9 · Bug of the Day\]** Today's bug: no base case. This factorial only has return n times factorial of n minus one. No stopping rule. Compile with dash Wall, and modern GCC catches it: warning, infinite recursion detected. It's only a warning, so the program still builds. Run it, and the calls go 5, 4, 3, 2, 1, 0, minus 1, minus 2, forever. Each call adds a plate to the stack, and the stack has a fixed size. When it runs out, the program crashes. This is called a stack overflow. On Linux or in the MSYS2 terminal you may see "Segmentation fault". In a Windows terminal, the program often just stops with no output at all. Either way, nothing prints. The fix: add the base case back. If n is less than or equal to 1, return 1. Rule for life: write the base case first, then the recursive case.

**\[10 · Challenge\]** Your challenge: ask the user for n and print n factorial using recursion. Try 10. Then try 20. Hint: 20 factorial is too big for an int. Remember long long from EP 09, and print it with percent l l d.

**\[11 · Outro\]** Next episode, we practise: Fibonacci, power and sum of digits, plus why some recursion is painfully slow. Keep coding, says Xecxec!

### Code shown

```c
#include <stdio.h>

void countdown(int n) {
    if (n == 0) {
        printf("Blast off!\n");
        return;
    }
    printf("%d\n", n);
    countdown(n - 1);
}

int factorial(int n) {
    if (n <= 1) {
        return 1;               // base case
    }
    return n * factorial(n - 1); // recursive case
}

int main(void) {
    countdown(3);
    printf("4! = %d\n", factorial(4));
    printf("5! = %d\n", factorial(5));
    return 0;
}
```

**Expected output:**

```text
3
2
1
Blast off!
4! = 24
5! = 120
```

### Bug of the Day

Wrong code (`bug.c`):

```c
#include <stdio.h>

int factorial(int n) {
    return n * factorial(n - 1);
}

int main(void) {
    printf("%d\n", factorial(5));
    return 0;
}
```

`gcc -Wall bug.c -o bug` (GCC 12 and newer):

```text
bug.c: In function 'factorial':
bug.c:3:5: warning: infinite recursion detected [-Winfinite-recursion]
    3 | int factorial(int n) {
      |     ^~~~~~~~~
bug.c:4:16: note: recursive call
    4 |     return n * factorial(n - 1);
      |                ^~~~~~~~~~~~~~~~
```

Running it crashes with a stack overflow and prints nothing. In the MSYS2 or Linux terminal you may see `Segmentation fault`; in PowerShell the program usually ends silently (on screen: "the crash message depends on your terminal").

Fixed code:

```c
#include <stdio.h>

int factorial(int n) {
    if (n <= 1) {
        return 1;
    }
    return n * factorial(n - 1);
}

int main(void) {
    printf("%d\n", factorial(5));
    return 0;
}
```

```text
120
```

Why: without a base case the function never stops calling itself, and every call uses stack space until the stack runs out.

### Pun & challenge

- **Pun:** To understand recursion, you must first understand recursion.
- **Challenge:** Read n from the user and print n! using a recursive function. It must work for n = 20 (use `long long` and `%lld`).
- **Challenge answer:**

```c
#include <stdio.h>

long long factorial(int n) {
    if (n <= 1) {
        return 1;
    }
    return n * factorial(n - 1);
}

int main(void) {
    int n;
    printf("Enter n: ");
    scanf("%d", &n);
    printf("%d! = %lld\n", n, factorial(n));
    return 0;
}
```

```text
Enter n: 20
20! = 2432902008176640000
```

### Shorts for EP 39

**S1 · A Function That Calls Itself** — 0:30 · built from scenes 1 and 3

- **Hook (first 1.5s):** a long bus-stand queue whispering "What's your position?"
- **Script:** You're in a queue and want your position. Ask the person ahead. They ask the person ahead. Until the first person says "I'm number one". Then the answers come back: two, three, four. That's recursion: a function that calls itself on a smaller problem, with a base case where it stops.
- **On-screen text:** RECURSION = ASK THE NEXT PERSON
- **Caption + hashtags:** Recursion explained with a bus queue. #cprogramming #learntocode #kodingkonkani #recursion #ctutorial

**S2 · The Call Stack in 30 Seconds** — 0:35 · built from scene 6

- **Hook (first 1.5s):** four plates stacking up labelled factorial(4) to factorial(1)
- **Script:** factorial of 4 calls factorial of 3, which calls 2, which calls 1. Each call is a plate on the stack, with its own n. factorial of 1 returns 1. Then the plates come off: 2 times 1 is 2, 3 times 2 is 6, 4 times 6 is 24. Going down, we pile up. Coming back, we multiply.
- **On-screen text:** PILE UP · THEN MULTIPLY
- **Caption + hashtags:** Watch recursion happen, plate by plate. #cprogramming #learntocode #kodingkonkani #computerscience #recursion

**S3 · Stack Overflow Bug** — 0:35 · built from scene 9

- **Hook (first 1.5s):** frames piling up past the top of the screen, screen shaking
- **Script:** This factorial has no base case. It calls 5, 4, 3, 2, 1, 0, minus 1, and never stops. Every call takes stack space, until the stack runs out and the program crashes. A stack overflow. GCC even warns: infinite recursion detected. Fix: if n is less than or equal to 1, return 1. Base case first, always.
- **On-screen text:** NO BASE CASE = CRASH
- **Caption + hashtags:** The real meaning of stack overflow. #cprogramming #debugging #kodingkonkani #gcc #learntocode

**S4 · To Understand Recursion** — 0:10 · built from scene 8

- **Hook (first 1.5s):** Xecxec reading a book titled "Recursion" whose cover shows Xecxec reading the same book
- **Script:** To understand recursion, you must first understand recursion.
- **On-screen text:** FIRST UNDERSTAND RECURSION
- **Caption + hashtags:** Read this caption again. #codingmemes #programmerhumor #kodingkonkani #cprogramming #recursion

**S5 · Quiz: How Many Lines?** — 0:25 · built from scene 4

- **Hook (first 1.5s):** `countdown(3);` = how many lines?
- **Script:** countdown prints n and calls itself with n minus 1, and prints "Blast off!" when n is 0. How many lines does countdown of 3 print? A: 3. B: 4. C: it never stops. The answer is B: 3, 2, 1 and Blast off.
- **On-screen text:** 3 · 4 · FOREVER?
- **Caption + hashtags:** Comment A, B or C before the reveal. #cprogramming #codingquiz #kodingkonkani #learntocode #recursion

## EP 40 — Recursion Practice

**Module 5 · Functions · 7:00 · Lilac + Tomato · Prerequisite: EP 39**

**Learning goals:** write recursive Fibonacci, power and sum-of-digits functions using the base case + smaller problem recipe; trace a recursive call tree by hand; explain why naive recursive Fibonacci is slow (repeated calls) and switch to a loop when speed matters.

### YouTube

- **Title:** Recursion Practice: Fibonacci, Power, Digits | C Programming EP 40
- **Description:** Three classic recursion problems that show up in every C exam: Fibonacci, power and sum of digits. We solve each with the same three-step recipe, then discover why fib(40) makes over 33 crore function calls, and fix it with a simple loop. Chapters: 0:00 Mirror inside a mirror · 0:20 The recursion recipe · 0:50 Fibonacci · 2:00 Power · 2:45 Sum of digits · 3:45 Running it · 4:10 Bug of the Day: slow recursion · 5:50 Challenge
- **Tags:** c programming, recursion examples c, fibonacci recursion c, power function recursion, sum of digits recursion, recursion vs iteration, learn c, c for beginners, koding konkani, class 12 computer science, c exam questions, gcc
- **Thumbnail:** big text "331 MILLION CALLS?!"; an exploding Fibonacci call tree; Xecxec buried under tiny function cards; lilac background, tomato text

### Scene list

| # | Start | Length | Template | On screen | Animation & SFX |
| --- | --- | --- | --- | --- | --- |
| 1 | 0:00 | 0:15 | Concept slide | Two mirrors facing each other: endless reflections of Xecxec getting smaller | Shimmer SFX; reflections zoom in |
| 2 | 0:15 | 0:05 | Title card | EP 40 · RECURSION PRACTICE | Tiles slam in; claw-click |
| 3 | 0:20 | 0:30 | Concept slide | Recipe card: 1. Smallest case? 2. How is the problem a smaller copy? 3. Combine | Three steps tick in one by one |
| 4 | 0:50 | 1:10 | Code explain | `practice.c` lines 3–8: fib, plus call tree for fib(4) | Butter highlights; call tree grows branch by branch |
| 5 | 2:00 | 0:45 | Code explain | `practice.c` lines 10–15: power | Butter highlights; tracker for exp counting down |
| 6 | 2:45 | 1:00 | Code explain | `practice.c` lines 17–22: sumDigits | Digits of 4031 peel off one by one with % and / labels |
| 7 | 3:45 | 0:20 | Terminal | Compile and run; 3 output lines | Typing SFX |
| 8 | 4:05 | 0:05 | Pun card | Pun | Drum hit; Xecxec counting on his claws |
| 9 | 4:10 | 1:40 | Bug of the Day | `bug.c`: fib(40) with a call counter; 1.2 s pause; "Calls made: 331160281"; table of calls for n = 10, 20, 30, 40; loop fix | Spinner while waiting; counter rolls up like a petrol pump; fix runs instantly, mint tick |
| 10 | 5:50 | 0:55 | Challenge | Challenge card: print Fibonacci numbers 0 to 20 using recursive fib | Timer ticks |
| 11 | 6:45 | 0:15 | Outro | Module 5 complete badge · Next: EP 41 · Arrays | Badge stamp; sign-off jingle |

### Narration script

**\[1 · Cold open\]** Stand between two mirrors in a shop in Margao, and you see yourself, inside yourself, inside yourself, smaller and smaller. Recursion feels like that. Last episode we learned the idea. Today we practise on three problems that appear in almost every C exam.

**\[2 · Title\]** Episode 40. Recursion practice.

**\[3 · The recipe\]** For every recursion problem, ask three questions. One: what is the smallest case, where I already know the answer? That's the base case. Two: how is my problem a smaller copy of itself? Three: how do I combine the smaller answer into the full answer? Let's use this recipe three times.

**\[4 · Fibonacci\]** The Fibonacci series goes 0, 1, 1, 2, 3, 5, 8, 13. Each number is the sum of the two before it. Recipe. Smallest case: fib of 0 is 0, fib of 1 is 1. Smaller copy: fib of n is fib of n minus 1 plus fib of n minus 2. \[HL 3\] Line three: int fib, int n. \[HL 4-5\] Lines four and five: if n is less than or equal to 1, return n. That one line covers both base cases, because fib of 0 is 0 and fib of 1 is 1. \[HL 7\] Line seven: return fib of n minus 1, plus fib of n minus 2. This function calls itself twice. Look at the call tree for fib of 4. It calls fib of 3 and fib of 2. fib of 3 calls fib of 2 and fib of 1. And see, fib of 2 appears twice. fib of 1 appears three times. Remember that; it matters soon.

**\[5 · Power\]** Next: power. 2 to the power 10. Recipe. Smallest case: anything to the power zero is 1. Smaller copy: base to the power exp is base times base to the power exp minus 1. \[HL 10\] Line ten: int power, int base, int exp. \[HL 11-12\] Lines eleven and twelve: if exp equals zero, return 1. \[HL 14\] Line fourteen: return base times power of base, exp minus 1. \[TRACK exp=10\] exp goes 10, 9, 8, all the way \[TRACK exp=0\] to 0, then the answers multiply back up to 1024.

**\[6 · Sum of digits\]** Third: sum of the digits of 4031. That's 4 plus 0 plus 3 plus 1, which is 8. Two tricks from EP 15: n mod 10 gives the last digit, and n divided by 10 removes the last digit. Recipe. Smallest case: if n is 0, there are no digits left, so the sum is 0. Smaller copy: the last digit plus the sum of the digits of the rest. \[HL 17\] Line seventeen: int sumDigits, int n. \[HL 18-19\] If n equals zero, return zero. \[HL 21\] Return n mod 10, plus sumDigits of n divided by 10. \[TRACK n=4031\] 4031 gives 1, plus sumDigits of 403. \[TRACK n=403\] That gives 3, plus sumDigits of 40. \[TRACK n=40\] That gives 0, plus sumDigits of 4. \[TRACK n=4\] That gives 4, plus sumDigits of 0, \[TRACK n=0\] which is 0. Total: 1 plus 3 plus 0 plus 4. 8.

**\[7 · Running it\]** Compile and run. fib of 7 is 13. 2 to the power 10 is 1024. Sum of digits of 4031 is 8. All three, correct.

**\[8 · Pun\]** Fibonacci's favourite food? Anything that adds up from the last two meals.

**\[9 · Bug of the Day\]** Today's bug: slow recursion. Our fib is correct, but watch what happens with fib of 40. We add a global counter, calls, that goes up by one every time fib runs. Run it, and wait. On our test machine it took about a second; your time will differ, and older laptops take longer. The answer: 102,334,155. And the counter: 331,160,281 calls. That's over 33 crore function calls for one number! Why? Remember the call tree: fib calls itself twice, and the same values get calculated again and again. Look at this table. fib of 10: 177 calls. fib of 20: 21,891. fib of 30: about 27 lakh. fib of 40: over 33 crore. Each step of 10 multiplies the work by more than 100. There's no error, no warning, just a program that seems frozen. The fix: when recursion repeats work, use a loop. Keep two variables, a and b, start them at 0 and 1, and step forward n times. fib of 40 now takes just 40 steps and finishes instantly. Recursion is beautiful, but it is not always fast. Later, in the algorithms module, you'll see a trick that keeps the recursion and remembers old answers.

**\[10 · Challenge\]** Your challenge: print the first 21 Fibonacci numbers, from fib of 0 up to fib of 20, on one line, using the recursive fib from today. It's still fast for numbers this small. The last number should be 6765.

**\[11 · Outro\]** That's Module 5 complete! You can now write functions, pass values, split files, and think recursively. Next module: storing many values in one name. Arrays. Keep coding, says Xecxec!

### Code shown

```c
#include <stdio.h>

int fib(int n) {
    if (n <= 1) {
        return n;
    }
    return fib(n - 1) + fib(n - 2);
}

int power(int base, int exp) {
    if (exp == 0) {
        return 1;
    }
    return base * power(base, exp - 1);
}

int sumDigits(int n) {
    if (n == 0) {
        return 0;
    }
    return (n % 10) + sumDigits(n / 10);
}

int main(void) {
    printf("fib(7) = %d\n", fib(7));
    printf("2^10 = %d\n", power(2, 10));
    printf("Sum of digits of 4031 = %d\n", sumDigits(4031));
    return 0;
}
```

**Expected output:**

```text
fib(7) = 13
2^10 = 1024
Sum of digits of 4031 = 8
```

### Bug of the Day

Slow code (`bug.c`):

```c
#include <stdio.h>

long long calls = 0;

long long fib(int n) {
    calls++;
    if (n <= 1) {
        return n;
    }
    return fib(n - 1) + fib(n - 2);
}

int main(void) {
    printf("fib(40) = %lld\n", fib(40));
    printf("Calls made: %lld\n", calls);
    return 0;
}
```

No error or warning. Output after a noticeable pause (about 1.2 s on our test machine; on screen: "your time will differ"):

```text
fib(40) = 102334155
Calls made: 331160281
```

Calls made by recursive fib (shown as a table in scene 9):

| n | Calls |
| --- | --- |
| 10 | 177 |
| 20 | 21,891 |
| 30 | 2,692,537 |
| 40 | 331,160,281 |

Fixed code (loop, runs instantly):

```c
#include <stdio.h>

long long fib(int n) {
    long long a = 0, b = 1;
    for (int i = 0; i < n; i++) {
        long long next = a + b;
        a = b;
        b = next;
    }
    return a;
}

int main(void) {
    printf("fib(40) = %lld\n", fib(40));
    return 0;
}
```

```text
fib(40) = 102334155
```

Why: recursive fib recomputes the same smaller values again and again, so the number of calls grows explosively; a loop computes each value once.

### Pun & challenge

- **Pun:** Fibonacci's favourite food? Anything that adds up from the last two meals.
- **Challenge:** Using today's recursive `fib`, print fib(0) to fib(20) on one line.
- **Challenge answer:**

```c
#include <stdio.h>

int fib(int n) {
    if (n <= 1) {
        return n;
    }
    return fib(n - 1) + fib(n - 2);
}

int main(void) {
    for (int i = 0; i <= 20; i++) {
        printf("%d ", fib(i));
    }
    printf("\n");
    return 0;
}
```

```text
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765
```

### Shorts for EP 40

**S1 · 331 Million Function Calls** — 0:30 · built from scene 9

- **Hook (first 1.5s):** the call counter rolling up past 300,000,000
- **Script:** This tiny Fibonacci function looks innocent. Ask it for fib of 40, and it makes 331 million calls. Why? It calls itself twice, and the same values get worked out again and again. fib of 10: 177 calls. fib of 40: 331 million. The same answer with a loop takes 40 steps.
- **On-screen text:** 331,160,281 CALLS
- **Caption + hashtags:** Correct code can still be terrible code. #cprogramming #learntocode #kodingkonkani #recursion #algorithms

**S2 · The Recursion Recipe** — 0:35 · built from scenes 3 and 6

- **Hook (first 1.5s):** recipe card "3 questions for every recursion"
- **Script:** Three questions solve any recursion problem. What's the smallest case? How is my problem a smaller copy? How do I combine? Sum of digits: if n is 0, return 0. Otherwise, the last digit, n mod 10, plus the sum of digits of n divided by 10. 4031 becomes 1 plus 3 plus 0 plus 4. 8.
- **On-screen text:** SMALLEST · SMALLER COPY · COMBINE
- **Caption + hashtags:** Save this for your next C exam. #cprogramming #learntocode #kodingkonkani #computerscience #exams

**S3 · Slow Recursion Bug** — 0:40 · built from scene 9

- **Hook (first 1.5s):** a frozen terminal with a spinner
- **Script:** No error. No warning. Your program just seems frozen. Recursive fib of 40 is making 331 million calls because it recalculates the same values over and over. Fix: a loop with two variables, a and b, starting at 0 and 1. Step forward n times. Same answer, 40 steps, instant.
- **On-screen text:** FROZEN? COUNT YOUR CALLS
- **Caption + hashtags:** When recursion is the wrong tool. #cprogramming #debugging #kodingkonkani #performance #learntocode

**S4 · Fibonacci's Favourite Food** — 0:12 · built from scene 8

- **Hook (first 1.5s):** Xecxec with two plates and a third plate that is the two combined
- **Script:** Fibonacci's favourite food? Anything that adds up from the last two meals.
- **On-screen text:** ADDS UP FROM THE LAST TWO
- **Caption + hashtags:** Maths jokes, but make them recursive. #codingmemes #programmerhumor #kodingkonkani #cprogramming #fibonacci

**S5 · Quiz: power(3, 4)** — 0:25 · built from scene 5

- **Hook (first 1.5s):** `power(3, 4)` = ?
- **Script:** power returns 1 when exp is 0, otherwise base times power of base, exp minus 1. What is power of 3 and 4? A: 12. B: 64. C: 81. The answer is C: 3 times 3 times 3 times 3 is 81.
- **On-screen text:** 12 · 64 · 81?
- **Caption + hashtags:** Comment your answer before the reveal. #cprogramming #codingquiz #kodingkonkani #learntocode #recursion
