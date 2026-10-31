# Module 1 — First program & basics

Episodes 5–14 · Pastel blue + Tomato

## EP 05 — How a C Program Is Built

**Module 1 · First program & basics · 5:45 · Pastel blue + Tomato · Prerequisite: EP 04**

**Learning goals:** name the four stages GCC runs (preprocess, compile, assemble, link); produce each stage's file with `-E`, `-S` and `-c`; tell a compile error from a link error; always recompile after editing.

### YouTube

- **Title:** What Happens When You Hit Enter? | C Programming EP 05
- **Description:** You typed gcc hello.c and a program appeared. In this episode we open the box and watch the four stages GCC runs: preprocess, compile, assemble and link. You will also learn why your edits sometimes "don't work" (spoiler: you forgot to recompile). 0:00 What happens when you hit Enter? 0:20 The four stages 0:55 Stage 1: the preprocessor (gcc -E) 1:50 Stage 2: compiling to assembly (gcc -S) 2:35 Stages 3 and 4: object file and linker 3:19 Running it and the exit code 3:59 Bug of the Day: edited but not recompiled 4:54 Challenge 5:29 Next episode
- **Tags:** c programming, gcc, how compiler works, preprocessor, linker, object file, compile c program, c tutorial for beginners, koding konkani, learn c in english, msys2 gcc
- **Thumbnail:** big text "WHAT GCC DOES"; a four-step conveyor belt (.c to .i to .s to .o to .exe) in tomato boxes on pastel blue; Xecxec riding the belt with claws up, surprised face.

### Scene list

| # | Start | Length | Template | On screen | Animation & SFX |
| --- | --- | --- | --- | --- | --- |
| 1 | 0:00 | 0:15 | Terminal | `gcc ep05.c -o ep05` typed, Enter pressed, freeze frame with "?" | Keystroke ticks; screen freezes on Enter; Xecxec peeks in, claw-click |
| 2 | 0:15 | 0:05 | Title card | EP 05 · HOW A C PROGRAM IS BUILT | Title slams in, whoosh |
| 3 | 0:20 | 0:35 | Concept slide | Last challenge answer, then a four-box pipeline: Preprocess, Compile, Assemble, Link | Boxes drop in one by one with pop; file icons slide between them |
| 4 | 0:55 | 0:55 | Terminal | `gcc -E ep05.c -o ep05.i`; scroll the .i file to the bottom where `main` appears; comment gone | Fast scroll whoosh; comment line fades out in red |
| 5 | 1:50 | 0:45 | Code explain | `gcc -S ep05.c -o ep05.s`; first lines of assembly with the string `Namaskar, Goa!` highlighted | Butter highlight on the string line; Xecxec squints |
| 6 | 2:35 | 0:40 | Concept slide | `gcc -c` makes ep05.o; linker joins ep05.o + C library (printf lives there) into ep05.exe; the `print` typo shows a link error | Puzzle pieces snap together; error box shakes in tomato |
| 7 | 3:15 | 0:04 | Pun card | Pun | Drum ba-dum, Xecxec claw-click |
| 8 | 3:19 | 0:40 | Terminal | `./ep05` prints `Namaskar, Goa!`; `echo $?` prints `0` | Ding on output; "0 = all good" tag |
| 9 | 3:59 | 0:55 | Bug of the Day | Edit the text in VS Code, save, run old exe, old text prints; recompile, new text prints | Butter warning stripe; buzzer, then success chime |
| 10 | 4:54 | 0:35 | Challenge | Break the file two ways; name the stage that complains | Timer ticks; Xecxec holds up a sign |
| 11 | 5:29 | 0:16 | Outro | Next: EP 06 · Comments & clean code; sign-off | Xecxec waves; outro sting |

### Narration script

**\[1 · Hook\]** You type gcc, ep05 dot c, dash o, ep05. You press Enter. Half a second later, a program exists that did not exist before. But what actually happened in that half second? Today, we open the box.

**\[2 · Title\]** Episode five. How a C program is built.

**\[3 · Four stages\]** First, last episode's challenge: print your name and your village on two lines. Two printf calls, each ending with backslash n, and you're done. Now, the big idea. When you run gcc, it is not one step. It is four. Stage one, the preprocessor, cleans and prepares your file. Stage two, the compiler, turns C into assembly language. Stage three, the assembler, turns assembly into machine code, called an object file. Stage four, the linker, joins your code with library code to make the final program. Think of a Kadamba bus route: Panjim, Porvorim, Mapusa, then Calangute. Same bus, four stops. And we can get off at any stop.

**\[4 · Preprocessor\]** Here is our small program. Look at line three: a comment. Line one: hash include, stdio dot h. Now type gcc, dash capital E, ep05 dot c, dash o, ep05 dot i. Dash E means: stop after the preprocessor. Open ep05 dot i. Whoa. Hundreds of lines. That's because hash include copied the whole stdio dot h file into ours. Scroll to the very bottom. There is our main. And notice: the comment is gone. The preprocessor deletes comments and pastes in included files. Your line count will be different from mine, and that's fine.

**\[5 · Compile to assembly\]** Next stop. Type gcc, dash capital S, ep05 dot c, dash o, ep05 dot s. Dash S means: stop after compiling. Open the dot s file. This is assembly language, very close to what the processor understands. \[HL the .string / .ascii line\] See this line? That's our text, Namaskar, Goa, stored as a string. You don't need to read assembly in this course. Just know that this is what your C turns into. Your file may look a bit different on Windows, and that's normal.

**\[6 · Assemble and link\]** Stage three. Type gcc, dash c, small c, ep05 dot c, dash o, ep05 dot o. This makes an object file: real machine code, but not a complete program yet. Why not? Because printf is not in our file. It lives in the C library. Stage four, the linker, finds printf in the library and joins it to our object file. Watch what happens if we misspell printf as print. The compiler only gives a warning. But the linker gives a real error: undefined reference to print. That means "I looked everywhere, and print does not exist." Now you know: "undefined reference" always comes from the linker.

**\[7 · Pun\]** Why did the linker break up with the compiler? It said, "I need someone who can complete me."

**\[8 · Run\]** Now we run it. Dot slash ep05. Namaskar, Goa! Then type echo, dollar, question mark. It prints zero. Remember return zero from episode four? This is where that zero goes. Zero means the program ended without problems.

**\[9 · Bug of the Day\]** Today's bug catches everyone. You change the text to Namaskar, Mapusa. You save. You run dot slash ep05. And it still says Namaskar, Goa! Did VS Code lose your change? No. The program you ran is the old exe file. Your edit is in the dot c file, but the exe was built before the edit. The fix: after every edit, run gcc again, then run the program. Save, compile, run. Every single time.

**\[10 · Challenge\]** Your challenge. Take ep05 dot c and break it two ways. First, delete the semicolon after printf. Second, spell printf as print. Compile each one and read the message. For each, tell me which stage complained: the compiler or the linker. Put your answers in the comments.

**\[11 · Outro\]** Next episode: comments and clean code, so that future you does not hate present you. Keep coding, says Xecxec!

### Code shown

```c
#include <stdio.h>

// The preprocessor deletes this comment
int main(void)
{
    printf("Namaskar, Goa!\n");
    return 0;
}
```

```bash
gcc -E ep05.c -o ep05.i     # stop after preprocessing
gcc -S ep05.c -o ep05.s     # stop after compiling (assembly)
gcc -c ep05.c -o ep05.o     # stop after assembling (object file)
gcc ep05.o -o ep05          # link into a program
./ep05
echo $?
```

**Expected output:**

```text
Namaskar, Goa!
0
```

On screen note for scene 4: "Line count of ep05.i depends on your machine." For scene 5: "Assembly differs between Windows and Linux."

Link error demo (scene 6), with `print("Namaskar, Goa!\n");` on line 6:

```text
ep05.c: In function 'main':
ep05.c:6:5: warning: implicit declaration of function 'print'; did you mean 'printf'? [-Wimplicit-function-declaration]
    6 |     print("Namaskar, Goa!\n");
      |     ^~~~~
      |     printf
...: undefined reference to `print'
collect2.exe: error: ld returned 1 exit status
```

The linker line starts with a temp-file path that differs per machine; show it as `...`.

### Bug of the Day

Wrong workflow: edit, save, run the old program.

```c
#include <stdio.h>

int main(void)
{
    printf("Namaskar, Mapusa!\n");   /* edited and saved */
    return 0;
}
```

```bash
./ep05
```

**Wrong output** (no error at all, which is why it is confusing):

```text
Namaskar, Goa!
```

**Fix:**

```bash
gcc ep05.c -o ep05
./ep05
```

```text
Namaskar, Mapusa!
```

The .exe is a separate file built from the old source, so it only changes when you compile again.

### Pun & challenge

- **Pun:** "Why did the linker break up with the compiler? It needed someone who could complete it."
- **Challenge:** Break ep05.c two ways (delete the semicolon; spell printf as print). Compile each and say which stage complains.
- **Challenge answer:** Missing semicolon: the compiler, `error: expected ';' before 'return'`. `print`: the compiler only warns (implicit declaration), then the linker fails with `undefined reference to 'print'`.

### Shorts for EP 05

**S1 · What happens when you press Enter?** — 0:30 · built from scenes 1, 3

- **Hook (first 1.5s):** "You press Enter. Four things happen."
- **Script:** You press Enter. Four things happen. One: the preprocessor pastes in your include files and deletes comments. Two: the compiler turns C into assembly. Three: the assembler turns that into machine code. Four: the linker joins in library code like printf. Then you have a program. Full episode on the channel.
- **On-screen text:** 1 PREPROCESS · 2 COMPILE · 3 ASSEMBLE · 4 LINK
- **Caption + hashtags:** What GCC really does in half a second. #cprogramming #learntocode #kodingkonkani #gcc #compiler

**S2 · Four stages in 30 seconds** — 0:35 · built from scenes 4–6

- **Hook (first 1.5s):** "Dash E. Dash S. Dash c. Remember these."
- **Script:** Want to see each stage yourself? gcc dash capital E stops after the preprocessor: you get a dot i file with hundreds of lines. gcc dash capital S stops after compiling: you get assembly in a dot s file. gcc dash small c stops after assembling: you get an object file. Plain gcc goes all the way and links. Four stops, one bus.
- **On-screen text:** -E .i · -S .s · -c .o · gcc .exe
- **Caption + hashtags:** Get off the GCC bus at any stop. #cprogramming #learntocode #kodingkonkani #gcc #ctutorial

**S3 · My edit didn't work?!** — 0:25 · built from scene 9

- **Hook (first 1.5s):** "I changed the code. Why is the output the same?"
- **Script:** You change the text. You save. You run the program. Same old output. Your code didn't change? It did. But you ran the old exe. The exe only updates when you compile again. Save, compile, run. Every time.
- **On-screen text:** SAVE · COMPILE · RUN
- **Caption + hashtags:** The most common beginner mistake in C. #cprogramming #learntocode #kodingkonkani #codingbugs #gcc

**S4 · The linker's breakup** — 0:10 · built from scene 7

- **Hook (first 1.5s):** "Why did the linker break up with the compiler?"
- **Script:** Why did the linker break up with the compiler? It needed someone who could complete it.
- **On-screen text:** "YOU COMPLETE ME"
- **Caption + hashtags:** Linker humour, sorry. #cprogramming #programmingjokes #kodingkonkani #learntocode

**S5 · Compiler or linker?** — 0:20 · built from scenes 6, 10

- **Hook (first 1.5s):** "Who throws this error: compiler or linker?"
- **Script:** Who throws this error? Undefined reference to print. Compiler or linker? Think. ... It's the linker. "Undefined reference" means the linker searched the libraries and found nothing called print. Comment if you got it.
- **On-screen text:** undefined reference to \`print' · COMPILER or LINKER?
- **Caption + hashtags:** Quick quiz: who complains? #cprogramming #learntocode #kodingkonkani #cquiz #gcc

## EP 06 — Comments & Clean Code

**Module 1 · First program & basics · 5:50 · Pastel blue + Tomato · Prerequisite: EP 05**

**Learning goals:** write single-line `//` and multi-line `/* */` comments; add a header comment to a file; indent code inside braces with 4 spaces; spot an unclosed `/*` from its GCC error.

### YouTube

- **Title:** Future You Will Hate This Code | C Programming EP 06
- **Description:** Code is read far more often than it is written. Learn how to write comments in C, how to indent, and how to name things so your code makes sense next week. Plus the classic unclosed comment bug. 0:00 Future you will hate present you 0:20 Messy code vs clean code 0:55 Single-line comments 1:45 Multi-line and header comments 2:35 Indentation and naming 3:23 Comments vanish before compiling 3:53 Bug of the Day: unclosed comment 4:58 Challenge 5:33 Next episode
- **Tags:** c programming, comments in c, clean code, code indentation, naming variables, c tutorial for beginners, koding konkani, unterminated comment, coding style, learn c
- **Thumbnail:** big text "CLEAN YOUR CODE"; split screen of a messy one-line program (red) and a neat indented one (mint); Xecxec holding a broom, proud pose.

### Scene list

| # | Start | Length | Template | On screen | Animation & SFX |
| --- | --- | --- | --- | --- | --- |
| 1 | 0:00 | 0:15 | Code explain | Messy fish-board program all jammed together; "Written by: you, 3 weeks ago" | Record scratch; Xecxec covers his eyes |
| 2 | 0:15 | 0:05 | Title card | EP 06 · COMMENTS & CLEAN CODE | Title slams in, whoosh |
| 3 | 0:20 | 0:35 | Concept slide | Last challenge answer; messy vs clean side by side; both print the same output | Split-screen wipe; two identical outputs appear with ding |
| 4 | 0:55 | 0:50 | Code explain | Clean fish\_board.c, lines 10 and 14 and 19 (the `//` comments) | Comment lines glow grey-green; tracker shows "ignored by GCC" |
| 5 | 1:45 | 0:50 | Code explain | Header block comment lines 1–5 | Block brackets `/*` and `*/` pulse in tomato |
| 6 | 2:35 | 0:44 | Concept slide | Indentation: 4 spaces inside `{ }`; naming: `p` vs `price`, `x2` vs `pomfretPrice` | Code blocks slide right by 4 spaces with a soft click; bad names crossed out |
| 7 | 3:19 | 0:04 | Pun card | Pun | Drum ba-dum, claw-click |
| 8 | 3:23 | 0:30 | Terminal | `gcc -E fish_board.c` bottom of output: comments gone (callback to EP 05) | Comments evaporate as steam particles |
| 9 | 3:53 | 1:05 | Bug of the Day | Unclosed `/*` swallows code; real GCC errors; fix | Butter stripe; buzzer; code greys out line by line as the comment "eats" it; success chime |
| 10 | 4:58 | 0:35 | Challenge | Add comments and indentation to your EP 04 or EP 05 program | Timer ticks; Xecxec holds a sign |
| 11 | 5:33 | 0:17 | Outro | Next: EP 07 · Variables; sign-off | Xecxec waves; outro sting |

### Narration script

**\[1 · Hook\]** Look at this code. Who wrote this mess? Oh. You did. Three weeks ago. Programmers have a saying: future you will hate present you. Today we make sure that doesn't happen.

**\[2 · Title\]** Episode six. Comments and clean code.

**\[3 · Messy vs clean\]** Last time, your challenge was to break the program two ways. The missing semicolon is caught by the compiler. The misspelled print gets past the compiler with a warning, then the linker stops it with "undefined reference". Well done if you got both. Now, look at these two programs. Left: everything jammed together. Right: neat, spaced, with notes. Compile both. Same output, exactly. The computer does not care how your code looks. But humans do: your teacher, your teammate, and you, next month. Clean code is for people.

**\[4 · Single-line comments\]** Here is our clean version: a price board for a fish stall. \[HL 10\] Line ten starts with two forward slashes. Everything after slash slash, until the end of that line, is a comment. GCC ignores it completely. It's a note for humans: "heading for the board". \[HL 14\] Line fourteen: another note, explaining that prices are per kilo. \[HL 19\] And line nineteen shows you can put a comment at the end of a line of code. return zero runs, and the note after it is ignored. Good comments explain why, not what. "Prices per kg" is useful. "This is printf" is not.

**\[5 · Multi-line comments\]** \[HL 1\] Now the top of the file. Line one: slash star. This opens a multi-line comment. Everything is ignored until star slash, \[HL 5\] here on line five. The stars at the start of lines two, three and four are just decoration, to make it look tidy. This is called a header comment. It says the file name, what the program does, and where it is from. Every program you write from now on should have one. It's like the name board on a shop. You know what's inside before you walk in.

**\[6 · Indent and name\]** Two more habits. First, indentation. Everything inside the curly braces of main moves right by four spaces. Then your eye can see where main starts and ends. In VS Code, the Tab key does this for you. Second, names. Later we'll create our own names for things. A name like p tells you nothing. A name like price tells you everything. Choose names that a friend could understand without asking you.

**\[7 · Pun\]** I wrote a joke in a comment. The compiler ignored it. Tough crowd.

**\[8 · Proof\]** Remember the preprocessor from episode five? Let's run gcc dash capital E on our file and scroll to the bottom. Look. Every comment is gone. The compiler never even sees them. So comments make your program easy to read, and they cost nothing when it runs.

**\[9 · Bug of the Day\]** Today's bug: the comment that never ends. Here I start a comment with slash star, "print the price of fish". But I forgot the star slash. Watch the colours in VS Code: everything below turns comment-coloured. printf is eaten. return zero is eaten. Even the closing brace is eaten. Compile, and GCC says: error, unterminated comment. And then: expected declaration or statement at end of input, because main never got its closing brace. The fix: close it on the same line with star slash, or use slash slash for one-line notes. Rule of thumb: slash slash for short notes, slash star only for blocks.

**\[10 · Challenge\]** Your challenge. Take your program from episode four or five. Add a header comment with the file name, your name and what it does. Add at least two slash slash comments that explain why. Fix the indentation to four spaces. Compile it to check it still works. Then compare: which version would you rather read next month?

**\[11 · Outro\]** Next episode: variables. We finally store things in memory, like fish in labelled baskets. Keep coding, says Xecxec!

### Code shown

Messy version (scene 1 and 3):

```c
#include <stdio.h>
int main(void){printf("Today's Fish Prices\n");
printf("-------------------\n");printf("Bangda   : Rs 200\n");
   printf("Pomfret  : Rs 900\n");
      printf("Prawns   : Rs 600\n");return 0;}
```

Clean version, fish\_board.c (scenes 3–5, 8):

```c
/*
 * fish_board.c
 * Prints today's price board for a fish stall.
 * Koding Konkani, EP 06
 */
#include <stdio.h>

int main(void)
{
    // Heading for the board
    printf("Today's Fish Prices\n");
    printf("-------------------\n");

    // One line per fish (price per kg)
    printf("Bangda   : Rs 200\n");
    printf("Pomfret  : Rs 900\n");
    printf("Prawns   : Rs 600\n");

    return 0;  // 0 means the program ended fine
}
```

**Expected output** (both versions):

```text
Today's Fish Prices
-------------------
Bangda   : Rs 200
Pomfret  : Rs 900
Prawns   : Rs 600
```

### Bug of the Day

```c
#include <stdio.h>

int main(void)
{
    /* Print the price of fish
    printf("Bangda: Rs 200 per kg\n");
    return 0;
}
```

**GCC output:**

```text
bug06.c: In function 'main':
bug06.c:5:5: error: unterminated comment
    5 |     /* Print the price of fish
      |     ^
bug06.c:4:1: error: expected declaration or statement at end of input
    4 | {
      | ^
```

**Fixed:**

```c
#include <stdio.h>

int main(void)
{
    // Print the price of fish
    printf("Bangda: Rs 200 per kg\n");
    return 0;
}
```

```text
Bangda: Rs 200 per kg
```

A `/*` comment runs until the next `*/`, so without one it swallows the rest of the file, including main's closing brace.

### Pun & challenge

- **Pun:** "I wrote a joke in a comment. The compiler ignored it. Tough crowd."
- **Challenge:** Take your EP 04 or EP 05 program, add a header comment, at least two `//` comments that explain why, and 4-space indentation. Recompile to check it still works.
- **Challenge answer:** Any version that compiles with the same output, has a `/* ... */` header (file name, author, purpose), `//` notes explaining intent, and every line inside `main` indented 4 spaces.

### Shorts for EP 06

**S1 · Who wrote this mess?** — 0:20 · built from scenes 1, 3

- **Hook (first 1.5s):** "Who wrote this mess? Oh. You did."
- **Script:** Who wrote this mess? Oh. You did. Three weeks ago. Here's the same program, cleaned up: a header comment, short notes, four-space indents. Same output. But one you can actually read. Clean code is for humans.
- **On-screen text:** SAME OUTPUT · ONE IS READABLE
- **Caption + hashtags:** Future you will thank you. #cprogramming #learntocode #kodingkonkani #cleancode #codingtips

**S2 · Comments in 30 seconds** — 0:30 · built from scenes 4–5

- **Hook (first 1.5s):** "Two ways to write a comment in C."
- **Script:** Two ways to write a comment in C. Slash slash: everything after it on that line is ignored. Great for short notes. Slash star, then star slash: everything between them is ignored, even many lines. Great for a header at the top of your file. Comments explain why, not what.
- **On-screen text:** // ONE LINE · /\* MANY LINES \*/
- **Caption + hashtags:** Comments in C, fast. #cprogramming #learntocode #kodingkonkani #ctutorial #coding

**S3 · The comment that ate my code** — 0:30 · built from scene 9

- **Hook (first 1.5s):** "This comment just ate my whole program."
- **Script:** This comment just ate my whole program. I opened it with slash star and forgot star slash. So printf, return, even the closing brace became part of the comment. GCC says: unterminated comment. Fix: close it, or use slash slash for one-line notes.
- **On-screen text:** error: unterminated comment
- **Caption + hashtags:** Always close your comments. #cprogramming #learntocode #kodingkonkani #codingbugs #gcc

**S4 · Tough crowd** — 0:10 · built from scene 7

- **Hook (first 1.5s):** "I told the compiler a joke."
- **Script:** I wrote a joke in a comment. The compiler ignored it. Tough crowd.
- **On-screen text:** // haha?
- **Caption + hashtags:** The compiler has no sense of humour. #programmingjokes #cprogramming #kodingkonkani #learntocode

**S5 · Does this compile?** — 0:20 · built from scenes 8–9

- **Hook (first 1.5s):** "Does this compile? Yes or no?"
- **Script:** Does this compile? Slash star, print price, then printf, return zero, closing brace. No star slash anywhere. Yes or no? ... No! The comment never closes, so it swallows everything. GCC: unterminated comment.
- **On-screen text:** YES or NO?
- **Caption + hashtags:** Spot the problem. #cprogramming #cquiz #kodingkonkani #learntocode #gcc

## EP 07 — Variables

**Module 1 · First program & basics · 6:20 · Pastel blue + Tomato · Prerequisite: EP 06**

**Learning goals:** declare an `int` variable and assign a value to it; declare and initialise in one line; print a variable with `%d`; update a variable using its old value; always initialise before use and compile with `-Wall`.

### YouTube

- **Title:** Variables Are Labelled Fish Baskets | C Programming EP 07
- **Description:** A variable is a named box in memory that holds a value. Learn how to declare, assign, print and update variables in C, with animated memory boxes. Plus the bug that prints random numbers: using a variable before giving it a value. 0:00 Variables are labelled fish baskets 0:20 What is a variable? 1:00 Declare and assign 2:00 Print with %d 2:45 Change a variable 3:35 Naming rules 4:14 Bug of the Day: uninitialised variable 5:24 Challenge 6:04 Next episode
- **Tags:** c programming, variables in c, int variable, declare variable c, printf %d, uninitialized variable, memory boxes, c tutorial for beginners, koding konkani, learn c
- **Thumbnail:** big text "VARIABLES"; three woven fish baskets labelled age, rollNo, marks with numbers 19, 42, 78 inside; Xecxec sitting in one basket, cheeky grin.

### Scene list

| # | Start | Length | Template | On screen | Animation & SFX |
| --- | --- | --- | --- | --- | --- |
| 1 | 0:00 | 0:15 | Concept slide | A Mapusa fish market stall with labelled baskets: Bangda, Pomfret, Prawns | Market ambience; baskets drop in; Xecxec peeks out of a basket |
| 2 | 0:15 | 0:05 | Title card | EP 07 · VARIABLES | Title slams in, whoosh |
| 3 | 0:20 | 0:40 | Memory boxes | Last challenge answer; a row of memory boxes; one gets a label "age" and a value 19 | Label tag swings on with a clack; number drops in with a plop |
| 4 | 1:00 | 1:00 | Code explain | ep07.c lines 5–9 | Line highlights; memory box appears per declaration; variable tracker panel on the right |
| 5 | 2:00 | 0:45 | Code explain | Lines 11–12, `%d` placeholder replaced by the value | `%d` flips like a card to show 19; terminal strip shows output |
| 6 | 2:45 | 0:50 | Code explain | Lines 14–15, `marks = marks + 5` | Box value 78 lifts out, +5 joins, 83 drops back in; tracker updates |
| 7 | 3:35 | 0:35 | Concept slide | Naming rules: letters, digits, underscore; no digit first; no spaces; case matters; no keywords | Bad names stamped with a red X; good names get a mint tick |
| 8 | 4:10 | 0:04 | Pun card | Pun | Drum ba-dum, claw-click |
| 9 | 4:14 | 1:10 | Bug of the Day | `int total;` used before assigning; garbage output; `-Wall` warning; fix | Box shows "???" with dust; buzzer; then `= 0` drops in, success chime |
| 10 | 5:24 | 0:40 | Challenge | Store age, height (in cm), roll number; print each on its own line | Timer ticks; three empty boxes wait |
| 11 | 6:04 | 0:16 | Outro | Next: EP 08 · Data types; sign-off | Xecxec waves; outro sting |

### Narration script

**\[1 · Hook\]** Walk into Mapusa market on a Friday. Every basket has a label: bangda, pomfret, prawns. You never have to guess what's inside. That is exactly what a variable is in C. A labelled basket that holds a value.

**\[2 · Title\]** Episode seven. Variables.

**\[3 · What is a variable\]** Last episode's challenge was to clean up an old program with a header comment, a few slash slash notes and four-space indents. If it still compiles and gives the same output, you nailed it. Now: your computer's memory is a long row of tiny boxes. A variable is one of those boxes, with a name stuck on it. We say, "Give me a box called age." C finds a free box, labels it age, and from then on, whenever we say age, C knows which box we mean. We can put a number in it, read it, or change it.

**\[4 · Declare and assign\]** Let's write it. \[HL 5\] Line five: int age, semicolon. This is a declaration. int means the box holds a whole number, an integer. age is the label. Right now the box exists, but we haven't put anything in it. \[HL 6\] Line six: age equals nineteen. This is an assignment. \[TRACK age=19\] The equals sign in C does not mean "is equal to". It means "put the value on the right into the box on the left". \[HL 8\] Line eight does both at once: int rollNo equals forty-two. \[TRACK rollNo=42\] This is called initialising: declare and give a starting value in one line. \[HL 9\] Line nine, same thing: int marks equals seventy-eight. \[TRACK marks=78\] Three baskets, three labels, three values.

**\[5 · Print with %d\]** Now let's read a box. \[HL 11\] Line eleven: printf, "Age: percent d", comma, age. The percent d is a placeholder. It means "put a whole number here". After the closing quote, comma, age tells printf which number. So printf takes the value from the age box, nineteen, and puts it where percent d was. Output: Age: 19. \[HL 12\] Line twelve does the same with rollNo. Roll no: 42.

**\[6 · Change a variable\]** The best part of a variable: it can vary. \[HL 14\] Line fourteen: marks equals marks plus five. In maths class, this line makes no sense. In C, read it right to left. First, take the value in marks, seventy-eight. Add five, eighty-three. Then put eighty-three back into marks. \[TRACK marks=83\] The old seventy-eight is gone. A box holds only one value at a time. \[HL 15\] Line fifteen prints it: Marks after bonus: 83.

**\[7 · Naming rules\]** A few rules for names. Use letters, digits and underscore. A name cannot start with a digit, so 2ndMarks is not allowed. No spaces, so roll no is not allowed; write rollNo or roll\_no. Capital letters matter: Age and age are two different boxes. And you cannot use C's own words, like int or return. Pick names that say what's inside, like we learned in episode six.

**\[8 · Pun\]** Why did the variable go to therapy? It had too many changes in its life.

**\[9 · Bug of the Day\]** Today's bug prints a random number. Look: int total, semicolon. Then total equals total plus fifty. Then print total. You expect fifty. Run it. I got thirty-two thousand something. You might get zero, or a huge number, or something else. Why? When you declare a box without a value, C does not clean it. It holds whatever junk was left in that memory before. Junk plus fifty is still junk. GCC can warn you, but only if you ask. Compile with dash capital W, all. Now GCC says: warning, total is used uninitialized. From today, always compile with dash Wall. The fix: give total a starting value. int total equals zero. Now the output is Total: 50. Every time.

**\[10 · Challenge\]** Your challenge. Create three variables: your age, your height in centimetres, and your roll number. Use whole numbers for all three. Print each one on its own line with a label. Compile with dash Wall, and make sure there are no warnings.

**\[11 · Outro\]** Next episode: data types. Why did two and a half kilos of fish become two kilos? Keep coding, says Xecxec!

### Code shown

```c
#include <stdio.h>

int main(void)
{
    int age;            // declare: make a box called age
    age = 19;           // assign: put 19 in the box

    int rollNo = 42;    // declare and assign together
    int marks = 78;

    printf("Age: %d\n", age);
    printf("Roll no: %d\n", rollNo);

    marks = marks + 5;  // bonus marks
    printf("Marks after bonus: %d\n", marks);

    return 0;
}
```

```bash
gcc -Wall ep07.c -o ep07
./ep07
```

**Expected output:**

```text
Age: 19
Roll no: 42
Marks after bonus: 83
```

### Bug of the Day

```c
#include <stdio.h>

int main(void)
{
    int total;
    total = total + 50;
    printf("Total: %d\n", total);
    return 0;
}
```

**Without `-Wall`:** no message at all. **Wrong output** (a garbage value; on screen: "your number will differ"):

```text
Total: 32815
```

**With `gcc -Wall`:**

```text
bug07.c: In function 'main':
bug07.c:6:11: warning: 'total' is used uninitialized [-Wuninitialized]
    6 |     total = total + 50;
      |     ~~~~~~^~~~~~~~~~~~
bug07.c:5:9: note: 'total' was declared here
    5 |     int total;
      |         ^~~~~
```

**Fixed:**

```c
#include <stdio.h>

int main(void)
{
    int total = 0;
    total = total + 50;
    printf("Total: %d\n", total);
    return 0;
}
```

```text
Total: 50
```

A local variable without a starting value holds leftover junk from memory, so always initialise it.

### Pun & challenge

- **Pun:** "Why did the variable go to therapy? It had too many changes in its life."
- **Challenge:** Store your age, height in cm and roll number in three `int` variables and print each on its own line with a label. Zero warnings with `-Wall`.
- **Challenge answer:**

```c
#include <stdio.h>

int main(void)
{
    int age = 17;
    int heightCm = 168;
    int rollNo = 23;

    printf("Age: %d\n", age);
    printf("Height: %d cm\n", heightCm);
    printf("Roll no: %d\n", rollNo);
    return 0;
}
```

### Shorts for EP 07

**S1 · Variables are fish baskets** — 0:20 · built from scenes 1, 3

- **Hook (first 1.5s):** "Every basket in the fish market has a label."
- **Script:** Every basket in the fish market has a label. You never guess what's inside. A variable in C is the same: a box in memory with a name on it. You can put a value in, read it, and change it. That's it. That's a variable.
- **On-screen text:** VARIABLE = LABELLED BOX
- **Caption + hashtags:** The easiest way to understand variables. #cprogramming #learntocode #kodingkonkani #variables #ctutorial

**S2 · marks = marks + 5?!** — 0:30 · built from scene 6

- **Hook (first 1.5s):** "This line breaks maths. But not C."
- **Script:** marks equals marks plus five. In maths, impossible. In C, read it right to left. Take the value in marks, seventy-eight. Add five. Put eighty-three back in the box. The equals sign in C means "store", not "is equal to".
- **On-screen text:** = MEANS "STORE"
- **Caption + hashtags:** The equals sign is not what you think. #cprogramming #learntocode #kodingkonkani #codingbasics #c

**S3 · Why is my number random?** — 0:35 · built from scene 9

- **Hook (first 1.5s):** "I added 50 to zero and got 32 thousand."
- **Script:** I added fifty and got thirty-two thousand. Why? I declared int total without a value. In C, that box holds leftover junk. Junk plus fifty is junk. Compile with dash Wall and GCC warns you: total is used uninitialized. Fix: int total equals zero.
- **On-screen text:** ALWAYS INITIALISE · gcc -Wall
- **Caption + hashtags:** The bug that prints random numbers. #cprogramming #codingbugs #kodingkonkani #learntocode #gcc

**S4 · Variable therapy** — 0:10 · built from scene 8

- **Hook (first 1.5s):** "Why did the variable go to therapy?"
- **Script:** Why did the variable go to therapy? It had too many changes in its life.
- **On-screen text:** TOO MANY CHANGES
- **Caption + hashtags:** It varies. #programmingjokes #cprogramming #kodingkonkani #learntocode

**S5 · What does this print?** — 0:20 · built from scenes 6, 10

- **Hook (first 1.5s):** "x is 10. What does this print?"
- **Script:** int x equals ten. x equals x plus x. x equals x plus one. Print x. What's the answer? ... Twenty-one. Ten plus ten is twenty, then plus one. Comment your answer before you check.
- **On-screen text:** int x = 10; x = x + x; x = x + 1; · ?
- **Caption + hashtags:** Quick C quiz. #cquiz #cprogramming #kodingkonkani #learntocode #variables

## EP 08 — Data Types: int, float, char

**Module 1 · First program & basics · 6:15 · Pastel blue + Tomato · Prerequisite: EP 07**

**Learning goals:** choose between `int`, `float` and `char` for a value; print each with `%d`, `%f`/`%.1f` and `%c`; use `sizeof` with `%zu` to see how many bytes a type uses; explain why storing 2.5 in an `int` gives 2.

### YouTube

- **Title:** Why 2.5 kg Became 2 kg | C Data Types EP 08
- **Description:** Not every basket can hold every kind of fish. Learn C's three basic data types (int, float and char), how to print each one, and how much memory each uses with sizeof. Plus the bug that silently chops off your decimals. 0:00 Why 2.5 kg became 2 kg 0:20 What is a data type? 1:00 int, float, char in code 2:10 Printing each type 2:55 sizeof: how big is each box? 3:39 A char is secretly a number 4:14 Bug of the Day: decimals in an int 5:24 Challenge 5:59 Next episode
- **Tags:** c programming, data types in c, int float char, sizeof operator, format specifiers, %f, %c, c tutorial for beginners, koding konkani, learn c, float vs int
- **Thumbnail:** big text "2.5 = 2 ?!"; a weighing scale showing 2.5 kg with a fish, and a code box printing 2; Xecxec shocked, claws on cheeks.

### Scene list

| # | Start | Length | Template | On screen | Animation & SFX |
| --- | --- | --- | --- | --- | --- |
| 1 | 0:00 | 0:15 | Terminal | Scale shows 2.5 kg; program prints `Weight: 2 kg` | Scale ding; then a sad trombone; Xecxec drops his claws |
| 2 | 0:15 | 0:05 | Title card | EP 08 · DATA TYPES | Title slams in, whoosh |
| 3 | 0:20 | 0:40 | Memory boxes | Last challenge answer; three boxes of different shapes: int (whole), float (decimal), char (one letter) | Each box shape pops in with its own colour; example values drop in |
| 4 | 1:00 | 1:10 | Code explain | ep08.c lines 5–7 | Highlights; variable tracker shows fishCount=12, weight=2.5, grade='A' |
| 5 | 2:10 | 0:45 | Code explain | Lines 9–12 with output strip | `%d`, `%f`, `%.1f`, `%c` each flip to the value; output types out |
| 6 | 2:55 | 0:40 | Code explain | Lines 14–16 sizeof; byte blocks 4, 4, 1 drawn as squares | Byte squares stack with a tick per byte; note "sizes can differ on other machines" |
| 7 | 3:35 | 0:04 | Pun card | Pun | Drum ba-dum, claw-click |
| 8 | 3:39 | 0:35 | Concept slide | `'A'` is stored as 65; `printf("%c %d", grade, grade)` prints `A 65` | Letter A morphs into 65 and back; ASCII strip slides past |
| 9 | 4:14 | 1:10 | Bug of the Day | `int weight = 2.5;` prints 2; `-Wall` is silent; `-Wconversion` warns; fix with float | Butter stripe; the .5 falls off the number and drops into the sea with a splash; success chime |
| 10 | 5:24 | 0:35 | Challenge | Print the sizeof char, int, float, double | Timer ticks; Xecxec holds a measuring tape |
| 11 | 5:59 | 0:16 | Outro | Next: EP 09 · More types; sign-off | Xecxec waves; outro sting |

### Narration script

**\[1 · Hook\]** The fish seller puts your bangda on the scale. Two and a half kilos. You type it into your program. And your program says: two kilos. Where did half a kilo of fish go? Today we find out.

**\[2 · Title\]** Episode eight. Data types: int, float and char.

**\[3 · What is a type\]** First, last time's challenge: three int variables for age, height in centimetres and roll number, each printed with percent d. Good. Now, in episode seven, every box was an int. But not every value is a whole number. A data type tells C what kind of value a box holds, and how big the box must be. Today we meet three. int holds whole numbers, like twelve or minus five. float holds numbers with a decimal point, like two point five. And char holds a single character, like the letter A.

**\[4 · In code\]** \[HL 5\] Line five: int fishCount equals twelve. \[TRACK fishCount=12\] A whole number of fish. Nothing new. \[HL 6\] Line six: float weight equals two point five f. \[TRACK weight=2.5\] float means this box can hold a decimal. The small f at the end tells C this number is a float. Without it, C treats 2.5 as a bigger type called double, which we meet next episode. \[HL 7\] Line seven: char grade equals A, in single quotes. \[TRACK grade='A'\] A char holds exactly one character, and it always goes in single quotes. Double quotes are for text, like in printf. Single quotes are for one character. Mix them up and you'll get errors.

**\[5 · Printing\]** Each type has its own placeholder. \[HL 9\] Line nine: percent d for the int. Fish: 12. \[HL 10\] Line ten: percent f for the float. Weight: 2.500000 kg. Six digits after the point. That's the default, and it looks ugly. \[HL 11\] So line eleven uses percent point one f: show only one digit after the point. Weight: 2.5 kg. Much better. We'll learn more of these tricks in episode eleven. \[HL 12\] Line twelve: percent c for a char. Grade: A.

**\[6 · sizeof\]** How big is each box? C has a tool for that: sizeof. \[HL 14\] Line fourteen: sizeof, int. It gives the size in bytes. To print it, we use percent z u, a placeholder made for sizes. On my machine: int uses 4 bytes. \[HL 15\] float: 4 bytes. \[HL 16\] char: 1 byte. A byte is 8 bits, 8 tiny on-off switches. These sizes are normal for Windows and Linux PCs today, but C does not promise them on every machine. That's exactly why sizeof exists: you ask, instead of guessing.

**\[7 · Pun\]** Why did the float leave the party early? It couldn't handle the point.

**\[8 · char is a number\]** A secret: a char is really a small number. The computer stores the letter A as the number sixty-five. This mapping is called ASCII. If we print grade with percent c, we see A. If we print the same grade with percent d, we see sixty-five. Same box, two ways of looking at it. We'll use this trick a lot when we reach strings.

**\[9 · Bug of the Day\]** Now the mystery from the start. Here's the code: int weight equals two point five. Print it with percent d. Output: Weight: 2 kg. An int box only holds whole numbers. When you put two point five into it, C simply chops off the decimal part. It does not round. Two point nine would also become two. The scary part: even with dash Wall, GCC says nothing. You need an extra flag, dash W conversion, and then GCC warns: conversion from double to int changes value from 2.5 to 2. The fix: use the right basket. float weight equals two point five f, and print it with percent point one f. Now it prints 2.5 kg, and your half kilo of fish is back.

**\[10 · Challenge\]** Your challenge. Print the sizeof char, int, float and double, one per line. Use percent z u. Then comment what your machine says. Is your double bigger than your float?

**\[11 · Outro\]** Next episode: more types. long, double, unsigned, and the odometer that rolled back to zero. Keep coding, says Xecxec!

### Code shown

```c
#include <stdio.h>

int main(void)
{
    int fishCount = 12;
    float weight = 2.5f;
    char grade = 'A';

    printf("Fish: %d\n", fishCount);
    printf("Weight: %f kg\n", weight);
    printf("Weight: %.1f kg\n", weight);
    printf("Grade: %c\n", grade);

    printf("int uses %zu bytes\n", sizeof(int));
    printf("float uses %zu bytes\n", sizeof(float));
    printf("char uses %zu byte\n", sizeof(char));

    return 0;
}
```

**Expected output** (on screen: "sizes can differ on other machines"):

```text
Fish: 12
Weight: 2.500000 kg
Weight: 2.5 kg
Grade: A
int uses 4 bytes
float uses 4 bytes
char uses 1 byte
```

Scene 8 snippet:

```c
#include <stdio.h>

int main(void)
{
    char grade = 'A';
    printf("%c %d\n", grade, grade);
    return 0;
}
```

```text
A 65
```

### Bug of the Day

```c
#include <stdio.h>

int main(void)
{
    int weight = 2.5;
    printf("Weight: %d kg\n", weight);
    return 0;
}
```

**Wrong output** (`gcc -Wall` gives no warning):

```text
Weight: 2 kg
```

**With `gcc -Wall -Wconversion`:**

```text
bug08.c: In function 'main':
bug08.c:5:18: warning: conversion from 'double' to 'int' changes value from '2.5e+0' to '2' [-Wfloat-conversion]
    5 |     int weight = 2.5;
      |                  ^~~
```

**Fixed:**

```c
#include <stdio.h>

int main(void)
{
    float weight = 2.5f;
    printf("Weight: %.1f kg\n", weight);
    return 0;
}
```

```text
Weight: 2.5 kg
```

An `int` can only hold whole numbers, so C throws away (truncates) the decimal part without rounding.

### Pun & challenge

- **Pun:** "Why did the float leave the party early? It couldn't handle the point."
- **Challenge:** Print `sizeof` for char, int, float and double, one per line, using `%zu`.
- **Challenge answer:**

```c
#include <stdio.h>

int main(void)
{
    printf("char   : %zu\n", sizeof(char));
    printf("int    : %zu\n", sizeof(int));
    printf("float  : %zu\n", sizeof(float));
    printf("double : %zu\n", sizeof(double));
    return 0;
}
```

```text
char   : 1
int    : 4
float  : 4
double : 8
```

(Typical on Windows/Linux PCs; your machine may differ.)

### Shorts for EP 08

**S1 · Where did half a kilo go?** — 0:25 · built from scenes 1, 9

- **Hook (first 1.5s):** "2.5 kg of fish. My program says 2."
- **Script:** Two and a half kilos of fish. My program says two. Where did the half go? I stored it in an int. An int only holds whole numbers, so C chops off the decimal. No rounding, no warning. Use a float, and the fish is back.
- **On-screen text:** int weight = 2.5; → 2
- **Caption + hashtags:** C just ate half my fish. #cprogramming #learntocode #kodingkonkani #datatypes #ctutorial

**S2 · Three types in 30 seconds** — 0:30 · built from scenes 3–5

- **Hook (first 1.5s):** "int, float, char. Here's when to use each."
- **Script:** int, float, char. int for whole numbers, like twelve fish. Print with percent d. float for decimals, like two point five kilos. Print with percent f. char for one character, like grade A, in single quotes. Print with percent c. Pick the right basket for the right fish.
- **On-screen text:** int %d · float %f · char %c
- **Caption + hashtags:** C data types, fast. #cprogramming #learntocode #kodingkonkani #datatypes #coding

**S3 · The silent decimal chop** — 0:30 · built from scene 9

- **Hook (first 1.5s):** "Even -Wall won't catch this bug."
- **Script:** Even dash Wall won't catch this one. int weight equals two point five. It prints two. GCC is silent. Add dash W conversion and it finally warns: conversion from double to int changes value. Fix: float weight equals two point five f.
- **On-screen text:** gcc -Wall -Wconversion
- **Caption + hashtags:** The bug GCC doesn't warn you about. #cprogramming #codingbugs #kodingkonkani #learntocode #gcc

**S4 · The float left early** — 0:10 · built from scene 7

- **Hook (first 1.5s):** "Why did the float leave the party?"
- **Script:** Why did the float leave the party early? It couldn't handle the point.
- **On-screen text:** 2.5 → 2 ...
- **Caption + hashtags:** Floating-point humour. #programmingjokes #cprogramming #kodingkonkani #learntocode

**S5 · A or 65?** — 0:20 · built from scene 8

- **Hook (first 1.5s):** "Same variable. Two outputs. Which one?"
- **Script:** char grade equals A. printf percent c, grade, then percent d, grade. What prints? ... A, then sixty-five. A char is stored as a number. Sixty-five is the code for capital A.
- **On-screen text:** printf("%c %d", grade, grade); · ?
- **Caption + hashtags:** A char is secretly a number. #cquiz #cprogramming #kodingkonkani #learntocode #ascii

## EP 09 — More Types: long, double, unsigned

**Module 1 · First program & basics · 6:30 · Pastel blue + Tomato · Prerequisite: EP 08**

**Learning goals:** use `long long`, `double` and `unsigned int` with `%lld`, `%f` and `%u`; read the limits of a type from `<limits.h>` (`INT_MAX`, `INT_MIN`, `UINT_MAX`); explain wrap-around for unsigned types and why signed overflow is a bug; fix an overflow by using a bigger type.

### YouTube

- **Title:** The Odometer That Rolled Back to 0 | C Programming EP 09
- **Description:** Every box in C has a size limit, and when you go past it, strange things happen. Learn long long, double and unsigned, find the limits of each type with limits.h, and see integer overflow in action. 0:00 The odometer that rolled back 0:20 Bigger and smaller boxes 1:00 long long, double, unsigned in code 2:05 Limits with limits.h 2:55 Overflow: the odometer 3:49 Bug of the Day: 100000 x 100000 5:09 Challenge 5:44 Recap 6:14 Next episode
- **Tags:** c programming, integer overflow, long long in c, double vs float, unsigned int, limits.h, INT\_MAX, c data types, c tutorial for beginners, koding konkani
- **Thumbnail:** big text "999999 + 1 = 0?"; a scooter odometer rolling to 000000; Xecxec riding pillion, eyes spinning.

### Scene list

| # | Start | Length | Template | On screen | Animation & SFX |
| --- | --- | --- | --- | --- | --- |
| 1 | 0:00 | 0:15 | Concept slide | A scooter odometer at 99999 ticks to 00000 | Digit drums rolling; clunk; Xecxec falls off the seat |
| 2 | 0:15 | 0:05 | Title card | EP 09 · MORE TYPES | Title slams in, whoosh |
| 3 | 0:20 | 0:40 | Memory boxes | Last challenge answer (sizes 1, 4, 4, 8); boxes of 4 and 8 bytes; a sign bit on int vs none on unsigned | Boxes stretch from 4 to 8 bytes with a rubber-band sound; sign bit flashes |
| 4 | 1:00 | 1:05 | Code explain | ep09.c lines 6–12 | Highlights; tracker: distance, pi, likes |
| 5 | 2:05 | 0:50 | Code explain | Lines 14–15; a number line from INT\_MIN to INT\_MAX | Number line zooms out; ends glow tomato |
| 6 | 2:55 | 0:50 | Code explain | Lines 17–19: unsigned short 65535 + 1 = 0 | Odometer graphic from scene 1 returns; digits roll to 0 |
| 7 | 3:45 | 0:04 | Pun card | Pun | Drum ba-dum, claw-click |
| 8 | 3:49 | 1:20 | Bug of the Day | `int total = 100000 * 100000;` prints 1410065408; GCC warning; fix with long long | Butter stripe; number bursts out of its box; buzzer; bigger box arrives, success chime |
| 9 | 5:09 | 0:35 | Challenge | Print the largest int and the largest long long | Timer ticks |
| 10 | 5:44 | 0:30 | Concept slide | Recap table: type, placeholder, typical size | Rows slide in one by one with pop |
| 11 | 6:14 | 0:16 | Outro | Next: EP 10 · Constants & #define; sign-off | Xecxec waves; outro sting |

### Narration script

**\[1 · Hook\]** An old scooter has a five-digit odometer. It shows nine nine nine nine nine. You ride one more kilometre. And it shows zero zero zero zero zero. The scooter didn't become new. The counter just ran out of digits. C numbers do the exact same thing.

**\[2 · Title\]** Episode nine. More types: long, double and unsigned.

**\[3 · Bigger boxes\]** Last episode's challenge: on a typical PC you got char 1, int 4, float 4 and double 8 bytes. Good. Remember, an int box is 4 bytes. That gives it room for about four billion different values. Half of them are used for negative numbers, so an int goes up to about two point one billion. Sometimes that's not enough, and sometimes we never need negatives. So C gives us more types. long long is a bigger whole-number box, 8 bytes. double is a bigger decimal box, 8 bytes, with about twice the precision of float. And unsigned means "no negatives", so all the space goes to positive numbers.

**\[4 · In code\]** \[HL 6\] Line six: long long distance equals three eighty-four million, four hundred thousand. \[TRACK distance=384400000\] That's the distance to the Moon in metres. The LL at the end marks it as a long long number. \[HL 7\] Line seven: double pi equals three point one four one five nine two six five three five eight nine seven nine three. \[TRACK pi=3.141592653589793\] A float would lose most of those digits. A double keeps them. For decimals, most programmers use double by default. \[HL 8\] Line eight: unsigned int likes equals four billion, with a U at the end. \[TRACK likes=4000000000\] A normal int can't hold four billion. An unsigned int can, because it doesn't waste space on negatives. \[HL 10\] Now printing. long long uses percent l l d. \[HL 11\] double uses percent f, here with point fifteen for fifteen digits. \[HL 12\] unsigned uses percent u. Wrong placeholder, wrong output, so learn these pairs.

**\[5 · Limits\]** How do we know the exact limits? \[HL 2\] Line two includes limits dot h. It gives us named limits. \[HL 14\] Line fourteen prints INT underscore MIN and INT underscore MAX. On a typical PC: minus two billion one hundred forty-seven million four hundred eighty-three thousand six hundred forty-eight, up to plus two billion one hundred forty-seven million four hundred eighty-three thousand six hundred forty-seven. \[HL 15\] Line fifteen: the largest unsigned int is a little over four point two nine billion. Your machine will very likely show the same, but always check, don't guess.

**\[6 · Overflow\]** Now, let's build that odometer. \[HL 17\] Line seventeen: unsigned short odometer equals sixty-five thousand five hundred thirty-five. \[TRACK odometer=65535\] An unsigned short is a small 2-byte box, and that's its biggest value. \[HL 18\] Line eighteen: add one. \[TRACK odometer=0\] \[HL 19\] Print it. Zero! Just like the scooter. For unsigned types, C promises this wrap-around. For normal signed types like int, going past the limit is called overflow, and C makes no promise at all. The result can be anything. So treat signed overflow as a bug, always.

**\[7 · Pun\]** I told my int a really big number. It took it negatively.

**\[8 · Bug of the Day\]** Today's bug. You want one lakh times one lakh. That's ten billion. int total equals one hundred thousand times one hundred thousand. Compile, and GCC warns even without dash Wall: integer overflow in expression of type int results in one billion four hundred ten million sixty-five thousand four hundred eight. Run it. Total: 1410065408. Not ten billion. Ten billion is far bigger than INT\_MAX, so the int box overflowed. And here's the trap: making total a long long is not enough on its own. Both one lakhs are ints, so the multiplication still happens in int and overflows first. The fix: make one of the numbers a long long with LL. long long total equals one hundred thousand LL times one hundred thousand. Print with percent l l d. Now: Total: 10000000000. Ten billion. Correct.

**\[9 · Challenge\]** Your challenge. Include limits dot h and print the largest int and the largest long long. Use percent d and percent l l d. How many digits does the long long have? Write it in the comments.

**\[10 · Recap\]** Quick recap. int: percent d, usually 4 bytes. long long: percent l l d, 8 bytes. unsigned int: percent u, 4 bytes, no negatives. float: percent f, 4 bytes. double: percent f, 8 bytes, more precise. Screenshot this table.

**\[11 · Outro\]** Next episode: constants and hash define. Because pi doesn't change. Promise. Keep coding, says Xecxec!

### Code shown

```c
#include <stdio.h>
#include <limits.h>

int main(void)
{
    long long distance = 384400000LL;      // Earth to Moon in metres
    double pi = 3.141592653589793;
    unsigned int likes = 4000000000U;      // no negatives allowed

    printf("Distance: %lld m\n", distance);
    printf("Pi: %.15f\n", pi);
    printf("Likes: %u\n", likes);

    printf("int range: %d to %d\n", INT_MIN, INT_MAX);
    printf("unsigned int max: %u\n", UINT_MAX);

    unsigned short odometer = 65535;       // biggest unsigned short
    odometer = odometer + 1;               // one more km...
    printf("Odometer: %hu\n", odometer);

    return 0;
}
```

**Expected output** (on screen: "limits shown are typical for Windows/Linux PCs"):

```text
Distance: 384400000 m
Pi: 3.141592653589793
Likes: 4000000000
int range: -2147483648 to 2147483647
unsigned int max: 4294967295
Odometer: 0
```

Recap table (scene 10):

| Type | Placeholder | Typical size |
| --- | --- | --- |
| int | %d | 4 bytes |
| unsigned int | %u | 4 bytes |
| long long | %lld | 8 bytes |
| float | %f | 4 bytes |
| double | %f | 8 bytes |

### Bug of the Day

```c
#include <stdio.h>

int main(void)
{
    int total = 100000 * 100000;
    printf("Total: %d\n", total);
    return 0;
}
```

**GCC output** (shown even without `-Wall`):

```text
bug09.c: In function 'main':
bug09.c:5:24: warning: integer overflow in expression of type 'int' results in '1410065408' [-Woverflow]
    5 |     int total = 100000 * 100000;
      |                        ^
```

**Wrong output:**

```text
Total: 1410065408
```

**Fixed:**

```c
#include <stdio.h>

int main(void)
{
    long long total = 100000LL * 100000;
    printf("Total: %lld\n", total);
    return 0;
}
```

```text
Total: 10000000000
```

The multiplication is done in the type of its operands, so at least one number must already be `long long` (the `LL`) before multiplying.

### Pun & challenge

- **Pun:** "I told my int a really big number. It took it negatively."
- **Challenge:** Include `<limits.h>` and print the largest `int` and the largest `long long`.
- **Challenge answer:**

```c
#include <stdio.h>
#include <limits.h>

int main(void)
{
    printf("Largest int: %d\n", INT_MAX);
    printf("Largest long long: %lld\n", LLONG_MAX);
    return 0;
}
```

```text
Largest int: 2147483647
Largest long long: 9223372036854775807
```

(19 digits for long long.)

### Shorts for EP 09

**S1 · The odometer rolled back** — 0:25 · built from scenes 1, 6

- **Hook (first 1.5s):** "99999 plus 1 equals... zero?"
- **Script:** Ninety-nine thousand nine hundred ninety-nine, plus one, equals zero? On an odometer, yes. It ran out of digits. C numbers do the same. An unsigned short holds up to sixty-five thousand five hundred thirty-five. Add one, and it wraps to zero.
- **On-screen text:** 65535 + 1 = 0
- **Caption + hashtags:** Numbers in C have limits. #cprogramming #learntocode #kodingkonkani #overflow #ctutorial

**S2 · Which type when?** — 0:30 · built from scenes 3, 10

- **Hook (first 1.5s):** "int not big enough? Here's what to use."
- **Script:** int not big enough? Use long long, 8 bytes, printed with percent l l d. Never need negatives? Use unsigned, printed with percent u. Need precise decimals? Use double instead of float. Pick the box that fits your number.
- **On-screen text:** long long %lld · unsigned %u · double %f
- **Caption + hashtags:** C types cheat sheet. #cprogramming #learntocode #kodingkonkani #datatypes #coding

**S3 · 1 lakh x 1 lakh = wrong** — 0:35 · built from scene 8

- **Hook (first 1.5s):** "One lakh times one lakh. C says 1.4 billion."
- **Script:** One lakh times one lakh should be ten billion. C says one point four billion. Why? Both numbers are int, so the answer must fit in an int. It doesn't, so it overflows. Fix: one hundred thousand LL times one hundred thousand, stored in a long long.
- **On-screen text:** 100000LL \* 100000
- **Caption + hashtags:** Integer overflow, explained. #cprogramming #codingbugs #kodingkonkani #learntocode #overflow

**S4 · It took it negatively** — 0:10 · built from scene 7

- **Hook (first 1.5s):** "I told my int a really big number."
- **Script:** I told my int a really big number. It took it negatively.
- **On-screen text:** INT\_MAX + 1 = ?
- **Caption + hashtags:** Overflow humour. #programmingjokes #cprogramming #kodingkonkani #learntocode

**S5 · Biggest int?** — 0:20 · built from scenes 5, 9

- **Hook (first 1.5s):** "What's the biggest number an int can hold?"
- **Script:** What's the biggest number an int can hold on a normal PC? A: one million. B: about two point one billion. C: infinity. ... B. Two billion one hundred forty-seven million four hundred eighty-three thousand six hundred forty-seven. It's called INT\_MAX.
- **On-screen text:** A) 1 million B) 2.1 billion C) infinity
- **Caption + hashtags:** Know your limits. #cquiz #cprogramming #kodingkonkani #learntocode #limits

## EP 10 — Constants & #define

**Module 1 · First program & basics · 6:00 · Pastel blue + Tomato · Prerequisite: EP 09**

**Learning goals:** spot a magic number and replace it with a name; declare a `const` variable and know it cannot be changed; write a `#define` macro and know the preprocessor swaps it as text; avoid putting a semicolon at the end of a `#define`.

### YouTube

- **Title:** Pi Doesn't Change. Promise. | C Constants & #define EP 10
- **Description:** Some values should never change: pi, a bus fare, the number of days in a week. Learn how to lock them with const and #define, why magic numbers make code hard to fix, and the semicolon that breaks every macro. 0:00 Pi doesn't change. Promise. 0:20 Magic numbers 1:00 const: a locked box 2:05 #define: find and replace 2:55 const or #define? 3:35 Bug of the Day: changing a const 4:30 Bonus bug: semicolon in #define 5:09 Challenge 5:44 Next episode
- **Tags:** c programming, const in c, #define, macros in c, magic numbers, constants in c, preprocessor, read-only variable, c tutorial for beginners, koding konkani
- **Thumbnail:** big text "LOCK IT"; a box with a padlock labelled PI = 3.14159; Xecxec trying to prise it open with a claw, failing.

### Scene list

| # | Start | Length | Template | On screen | Animation & SFX |
| --- | --- | --- | --- | --- | --- |
| 1 | 0:00 | 0:15 | Code explain | A program with `15` used in six places; "Bus fare is now Rs 20. Find them all." | Search beam sweeps; five found, one missed blinks red; Xecxec facepalms |
| 2 | 0:15 | 0:05 | Title card | EP 10 · CONSTANTS & #DEFINE | Title slams in, whoosh |
| 3 | 0:20 | 0:40 | Concept slide | Last challenge answer; "magic number" definition; `3.14159` vs `PI` | Number spins in a puff of smoke; replaced by a name tag |
| 4 | 1:00 | 1:05 | Code explain | ep10.c lines 7–11 | Padlock icon snaps onto PI box with a click; tracker shows PI, radius, area |
| 5 | 2:05 | 0:50 | Code explain | Line 3 `#define`; lines 13–14; then the preprocessed view shows `trips * 15` | BUS\_FARE text slides out, 15 slides in (find-and-replace animation) |
| 6 | 2:55 | 0:36 | Concept slide | Comparison table: const vs #define | Two columns fill row by row with pop |
| 7 | 3:31 | 0:04 | Pun card | Pun | Drum ba-dum, claw-click |
| 8 | 3:35 | 0:55 | Bug of the Day | `PI = 3.0f;` and the real GCC error; fix | Butter stripe; claw bounces off padlock with a clang; buzzer |
| 9 | 4:30 | 0:39 | Bug of the Day | `#define BUS_FARE 15;` breaks printf; error points at the macro | Semicolon highlighted in tomato; the swapped text shows `15;` inside printf |
| 10 | 5:09 | 0:35 | Challenge | Circle area and circumference with `const` PI, radius 5 | Timer ticks; a pizza circle draws itself |
| 11 | 5:44 | 0:16 | Outro | Next: EP 11 · printf deep dive; sign-off | Xecxec waves; outro sting |

### Narration script

**\[1 · Hook\]** Here's a program for bus fares. The fare, fifteen rupees, appears in six places. Tomorrow, the fare goes up to twenty. You change five of them. You miss one. Now your program is wrong, and nobody knows why. There's a better way.

**\[2 · Title\]** Episode ten. Constants and hash define.

**\[3 · Magic numbers\]** First, the challenge from episode nine. INT\_MAX is two billion one hundred forty-seven million four hundred eighty-three thousand six hundred forty-seven. LLONG\_MAX has nineteen digits. Now, a number that suddenly appears in code, with no name, is called a magic number. Like fifteen. Fifteen what? Rupees? Minutes? Students? Nobody knows. Or three point one four one five nine. You probably guessed pi, but why make people guess? The fix is to give the number a name, and lock it so it can't change by accident.

**\[4 · const\]** \[HL 7\] Line seven: const float PI equals three point one four one five nine f. \[TRACK PI=3.14159\] This is a normal float variable, with one extra word in front: const. const means "read only". Once PI gets its value, nobody can change it. By habit, we write constant names in capital letters, so they stand out. \[HL 8\] Line eight: float radius equals seven. \[TRACK radius=7.0\] \[HL 10\] Line ten: float area equals PI times radius times radius. The star means multiply. \[TRACK area=153.94\] \[HL 11\] Line eleven prints the area with two decimals. Area: 153.94. Now the code reads like the maths formula. Pi r squared.

**\[5 · #define\]** \[HL 3\] Now line three: hash define, BUS underscore FARE, fifteen. No equals sign. No semicolon. No type. This is not a variable at all. Remember the preprocessor from episode five? Before compiling, it does a find-and-replace. Every BUS\_FARE in the file becomes the text fifteen. \[HL 14\] So line fourteen, trips times BUS\_FARE, becomes trips times fifteen before the compiler even sees it. With four trips: Bus cost: Rs 60. And when the fare changes? You edit one line, line three. Every use updates. No missed spots.

**\[6 · Which one?\]** So which should you use? const is a real variable with a type, so the compiler checks how you use it. A hash define is plain text replacement: no type, no checks, but it works anywhere in the file, even before main. Both are common in real code. A simple rule for this course: use const for values inside a function, and hash define for fixed settings at the top of the file.

**\[7 · Pun\]** I asked PI to change, just once. It said, "Sorry, I'm a constant. I don't do that."

**\[8 · Bug of the Day\]** Today's bug. Someone thinks three is "close enough" for pi. They write PI equals three point zero f, after the const line. Compile. GCC says: error, assignment of read-only variable PI. That's the padlock doing its job. The error isn't a problem; it's protection. The fix is to delete that line. If you really need a different value, change the const line itself, in one place.

**\[9 · Bonus bug\]** A bonus bug, because everyone does this one. You write hash define BUS\_FARE fifteen, semicolon. Habit, right? Every line ends with a semicolon. Not this one. The preprocessor copies the semicolon too. So printf with trips times BUS\_FARE becomes trips times fifteen semicolon, inside printf's brackets. GCC says: error, expected closing bracket before semicolon token. And it adds a note: in expansion of macro BUS\_FARE. That note is your clue. The fix: no semicolon at the end of a hash define.

**\[10 · Challenge\]** Your challenge. Use const float PI. Take a radius of five. Print the area of the circle, and also the circumference, which is two times PI times radius. Two decimals each.

**\[11 · Outro\]** Next episode: a deep dive into printf. We'll make your output look rich. Keep coding, says Xecxec!

### Code shown

```c
#include <stdio.h>

#define BUS_FARE 15          // macro: text swap before compiling

int main(void)
{
    const float PI = 3.14159f;  // const: a variable that cannot change
    float radius = 7.0f;

    float area = PI * radius * radius;
    printf("Area: %.2f\n", area);

    int trips = 4;
    printf("Bus cost: Rs %d\n", trips * BUS_FARE);

    return 0;
}
```

**Expected output:**

```text
Area: 153.94
Bus cost: Rs 60
```

Comparison table (scene 6):

|  | const | #define |
| --- | --- | --- |
| What it is | A read-only variable | Text replacement by the preprocessor |
| Has a type | Yes | No |
| Checked by compiler | Yes | Only after the swap |
| Semicolon at end | Yes | No |
| Good for | Values inside a function | Fixed settings at the top of a file |

### Bug of the Day

```c
#include <stdio.h>

int main(void)
{
    const float PI = 3.14159f;
    PI = 3.0f;
    printf("PI: %.2f\n", PI);
    return 0;
}
```

**GCC output:**

```text
bug10.c: In function 'main':
bug10.c:6:8: error: assignment of read-only variable 'PI'
    6 |     PI = 3.0f;
      |        ^
```

**Fixed:**

```c
#include <stdio.h>

int main(void)
{
    const float PI = 3.14159f;
    printf("PI: %.2f\n", PI);
    return 0;
}
```

```text
PI: 3.14
```

A `const` variable is read-only after it is initialised, so any later assignment is a compile error.

**Bonus bug (scene 9):**

```c
#include <stdio.h>
#define BUS_FARE 15;
int main(void)
{
    int trips = 4;
    printf("Bus cost: Rs %d\n", trips * BUS_FARE);
    return 0;
}
```

```text
bonus10.c: In function 'main':
bonus10.c:2:20: error: expected ')' before ';' token
    2 | #define BUS_FARE 15;
      |                    ^
bonus10.c:6:41: note: in expansion of macro 'BUS_FARE'
    6 |     printf("Bus cost: Rs %d\n", trips * BUS_FARE);
      |                                         ^~~~~~~~
bonus10.c:6:11: note: to match this '('
    6 |     printf("Bus cost: Rs %d\n", trips * BUS_FARE);
      |           ^
```

Fix: `#define BUS_FARE 15` with no semicolon. The preprocessor copies everything after the name, semicolon included.

### Pun & challenge

- **Pun:** "I asked PI to change, just once. It said: sorry, I'm a constant."
- **Challenge:** With `const float PI`, print the area and circumference of a circle of radius 5, two decimals each.
- **Challenge answer:**

```c
#include <stdio.h>

int main(void)
{
    const float PI = 3.14159f;
    float radius = 5.0f;

    printf("Area: %.2f\n", PI * radius * radius);
    printf("Circumference: %.2f\n", 2 * PI * radius);
    return 0;
}
```

```text
Area: 78.54
Circumference: 31.42
```

### Shorts for EP 10

**S1 · The fare went up** — 0:25 · built from scenes 1, 5

- **Hook (first 1.5s):** "The bus fare changed. Now fix six lines."
- **Script:** The bus fare went from fifteen to twenty. It's in six places in your code. You fix five. One is still wrong. Instead, write hash define BUS\_FARE fifteen at the top. Use the name everywhere. Next time, change one line. Done.
- **On-screen text:** ONE NAME · ONE PLACE TO CHANGE
- **Caption + hashtags:** Stop using magic numbers. #cprogramming #learntocode #kodingkonkani #cleancode #ctutorial

**S2 · const vs #define** — 0:30 · built from scenes 4–6

- **Hook (first 1.5s):** "Two ways to make a constant in C."
- **Script:** Two ways to make a constant in C. const float PI equals three point one four: a real variable, with a type, that nobody can change. Hash define BUS\_FARE fifteen: the preprocessor swaps the name for the text before compiling. No type, no semicolon.
- **On-screen text:** const = LOCKED BOX · #define = FIND & REPLACE
- **Caption + hashtags:** Constants in C, fast. #cprogramming #learntocode #kodingkonkani #coding #c

**S3 · The semicolon that breaks macros** — 0:30 · built from scene 9

- **Hook (first 1.5s):** "One semicolon. Three errors."
- **Script:** One semicolon, three lines of errors. Hash define BUS\_FARE fifteen semicolon. The preprocessor copies the semicolon into printf, and GCC says expected closing bracket before semicolon. Look for "in expansion of macro". Fix: no semicolon after a hash define.
- **On-screen text:** WRONG: #define X 15; · RIGHT: #define X 15
- **Caption + hashtags:** The macro mistake everyone makes once. #cprogramming #codingbugs #kodingkonkani #learntocode #gcc

**S4 · PI won't change** — 0:10 · built from scene 7

- **Hook (first 1.5s):** "I asked PI to change."
- **Script:** I asked PI to change, just once. It said, sorry, I'm a constant. I don't do that.
- **On-screen text:** error: read-only variable 'PI'
- **Caption + hashtags:** Some things never change. #programmingjokes #cprogramming #kodingkonkani #learntocode

**S5 · Error or not?** — 0:20 · built from scene 8

- **Hook (first 1.5s):** "Does this line compile?"
- **Script:** const int DAYS equals seven. Next line: DAYS equals eight. Does it compile? ... No. GCC says: assignment of read-only variable DAYS. const means locked.
- **On-screen text:** const int DAYS = 7; DAYS = 8; · ?
- **Caption + hashtags:** Quick C quiz. #cquiz #cprogramming #kodingkonkani #learntocode #const

## EP 11 — printf Deep Dive

**Module 1 · First program & basics · 6:40 · Pastel blue + Tomato · Prerequisite: EP 10**

**Learning goals:** use width (`%5d`), left-align (`%-5d`) and zero-pad (`%05d`); control decimals with precision (`%.2f`, `%8.2f`); print strings with `%s` and a real percent sign with `%%`; line up columns to print a neat bill; match every placeholder to the right type.

### YouTube

- **Title:** Make Your C Output Look Rich | printf Deep Dive EP 11
- **Description:** printf can do much more than print a line. Learn width, alignment, zero padding, precision, %s and %%, then build a neat restaurant bill with perfectly lined-up columns. Plus what happens when you print a float with %d. 0:00 Make your output look rich 0:20 Anatomy of a placeholder 0:55 Width, left-align, zero-pad 2:00 Precision for decimals 2:45 %s, %c and %% 3:24 Build a neat bill 4:34 Bug of the Day: %d for a float 5:49 Challenge 6:24 Next episode
- **Tags:** c programming, printf in c, format specifiers, printf width precision, %d %f %s, printf alignment, c tutorial for beginners, koding konkani, formatted output c, learn c
- **Thumbnail:** big text "RICH OUTPUT"; left: a messy bill with jagged numbers, right: a perfectly aligned bill on a cream receipt; Xecxec wearing sunglasses holding the receipt.

### Scene list

| # | Start | Length | Template | On screen | Animation & SFX |
| --- | --- | --- | --- | --- | --- |
| 1 | 0:00 | 0:15 | Terminal | Jagged bill vs aligned bill, side by side | Receipt printer whirr; Xecxec puts on sunglasses |
| 2 | 0:15 | 0:05 | Title card | EP 11 · PRINTF DEEP DIVE | Title slams in, whoosh |
| 3 | 0:20 | 0:35 | Concept slide | Last challenge answer; anatomy diagram of `%-8.2f`: percent, flag, width, precision, type | Each part lifts off with a label and a pop |
| 4 | 0:55 | 1:05 | Code explain | ep11.c lines 9–12 with square-bracket output | Width shown as dotted boxes; digits slide right, left, then zeros fill in |
| 5 | 2:00 | 0:45 | Code explain | Lines 13–14 precision | Extra decimals fall away; rounding arrow shows 45.5 to 45.50 |
| 6 | 2:45 | 0:35 | Code explain | Lines 15–17: `%c`, `%s`, `%%` | "Feni" bottle label pops into the brackets; % sign doubles then merges |
| 7 | 3:20 | 0:04 | Pun card | Pun | Drum ba-dum, claw-click |
| 8 | 3:24 | 1:10 | Code explain | bill.c lines 5–9, column guides | Vertical guide lines show 12, 4, 9 column widths; rows print one by one with receipt whirr |
| 9 | 4:34 | 1:15 | Bug of the Day | `printf("%d", price)` with float price; GCC warning; garbage output; fix | Butter stripe; garbage numbers flicker; buzzer; success chime |
| 10 | 5:49 | 0:35 | Challenge | Print a neat bill for 3 items of your own | Timer ticks; blank receipt |
| 11 | 6:24 | 0:16 | Outro | Next: EP 12 · scanf; sign-off | Xecxec waves; outro sting |

### Narration script

**\[1 · Hook\]** Two bills. Same items, same prices. One looks like a mess. The other looks like it came from a proper restaurant. The only difference? A few numbers inside printf. Let's make your output look rich.

**\[2 · Title\]** Episode eleven. printf deep dive.

**\[3 · Anatomy\]** Last challenge: with radius five, area is 78.54 and circumference is 31.42. Nice. Now, you know percent d and percent f. But a placeholder can have more parts. Look at percent minus eight point two f. Percent starts it. Minus is a flag: left-align. Eight is the width: use at least eight spaces. Point two is the precision: two digits after the decimal. And f is the type. Every part is optional, except the percent and the type.

**\[4 · Width\]** In this program, I've put square brackets around each output, so you can see the spaces. \[HL 9\] Line nine: plain percent d with qty, which is three. Output: bracket, three, bracket. \[HL 10\] Line ten: percent five d. Width five. The number takes one space, so printf adds four spaces in front. Numbers are right-aligned by default. \[HL 11\] Line eleven: percent minus five d. The minus flips it: number first, then four spaces. Left-aligned. \[HL 12\] Line twelve: percent zero five d. Instead of spaces, fill with zeros: zero zero zero zero three. Useful for roll numbers and bill numbers.

**\[5 · Precision\]** \[HL 13\] Line thirteen: percent point two f, with price forty-five point five. Two digits after the point: forty-five point five zero. Perfect for rupees and paise. printf rounds when it cuts digits, so two point three four six with point two f becomes two point three five. \[HL 14\] Line fourteen combines both: percent eight point two f. The whole thing takes eight spaces, with two decimals. That's three spaces, then forty-five point five zero.

**\[6 · %s %c %%\]** \[HL 15\] Line fifteen: percent c, the size char, L. \[HL 16\] Line sixteen: percent s prints a string, a piece of text in double quotes. Here: Feni. We'll do much more with strings in module seven. \[HL 17\] And line seventeen: how do you print a real percent sign? Percent starts a placeholder, so one percent confuses printf. Write two: percent percent. Output: 100% fresh.

**\[7 · Pun\]** My printf output was so neat, the receipt asked for my autograph. Well, at least it was well formatted.

**\[8 · Neat bill\]** Now let's build the rich bill. The trick is to use the same widths on every line. \[HL 5\] Line five is the header. Percent minus twelve s: the item name, left-aligned in twelve spaces. Percent four s: Qty, right-aligned in four. Percent nine s: Amount, right-aligned in nine. \[HL 6\] Line six uses the same widths, but with real types: percent minus twelve s for Fish thali, percent four d for the quantity two, and percent nine point two f for three hundred sixty point zero zero. \[HL 7\] Lines seven \[HL 8\] and eight, same pattern: Sol kadhi, then Bebinca. \[HL 9\] Line nine is the total. For the Qty column, we print an empty string, so it stays blank. Look at the result. Every column lines up, because every line uses the same widths.

**\[9 · Bug of the Day\]** Today's bug. float price equals forty-five point five. printf, "Price: percent d", price. You expect forty-five, maybe. Run it. I got two billion and something. Run again: a completely different number. Your numbers will be different too. Why? printf trusts you. percent d tells it "an int is coming", but you sent a float, which is stored completely differently. printf reads the wrong bits from the wrong place. GCC warns you, if you compile with dash Wall: format percent d expects argument of type int, but argument 2 has type double. Wait, double? Yes: when you pass a float to printf, C automatically turns it into a double. That's also why percent f works for both float and double. The fix: use percent point two f. Price: 45.50. Rule: placeholder and type must always match.

**\[10 · Challenge\]** Your challenge. Print a neat bill for three items you'd buy in your town: name, quantity and amount. Use the same widths on every line, and add a total line. Post a screenshot of your output.

**\[11 · Outro\]** So far, our programs only talk. Next episode, with scanf, the user can finally talk back. Keep coding, says Xecxec!

### Code shown

```c
#include <stdio.h>

int main(void)
{
    int qty = 3;
    float price = 45.5f;
    char size = 'L';

    printf("[%d]\n", qty);
    printf("[%5d]\n", qty);          // width 5, right-aligned
    printf("[%-5d]\n", qty);         // width 5, left-aligned
    printf("[%05d]\n", qty);         // pad with zeros
    printf("[%.2f]\n", price);       // 2 digits after the point
    printf("[%8.2f]\n", price);      // width 8, 2 decimals
    printf("[%c]\n", size);
    printf("[%s]\n", "Feni");        // a string
    printf("100%% fresh\n");         // a real percent sign

    return 0;
}
```

**Expected output:**

```text
[3]
[    3]
[3    ]
[00003]
[45.50]
[   45.50]
[L]
[Feni]
100% fresh
```

bill.c (scene 8):

```c
#include <stdio.h>

int main(void)
{
    printf("%-12s %4s %9s\n", "Item", "Qty", "Amount");
    printf("%-12s %4d %9.2f\n", "Fish thali", 2, 360.00);
    printf("%-12s %4d %9.2f\n", "Sol kadhi", 3, 90.00);
    printf("%-12s %4d %9.2f\n", "Bebinca", 1, 120.50);
    printf("%-12s %4s %9.2f\n", "TOTAL", "", 570.50);
    return 0;
}
```

**Expected output:**

```text
Item          Qty    Amount
Fish thali      2    360.00
Sol kadhi       3     90.00
Bebinca         1    120.50
TOTAL                570.50
```

### Bug of the Day

```c
#include <stdio.h>

int main(void)
{
    float price = 45.5f;
    printf("Price: %d\n", price);
    return 0;
}
```

**GCC output with `-Wall`:**

```text
bug11.c: In function 'main':
bug11.c:6:21: warning: format '%d' expects argument of type 'int', but argument 2 has type 'double' [-Wformat=]
    6 |     printf("Price: %d\n", price);
      |                    ~^     ~~~~~
      |                     |     |
      |                     int   double
      |                    %f
```

**Wrong output** (garbage that changes each run; on screen: "your number will differ"):

```text
Price: 2084392984
```

**Fixed:**

```c
#include <stdio.h>

int main(void)
{
    float price = 45.5f;
    printf("Price: %.2f\n", price);
    return 0;
}
```

```text
Price: 45.50
```

printf cannot check types at run time; it reads whatever bits the placeholder asks for, so a mismatch prints garbage.

### Pun & challenge

- **Pun:** "My output was so neat, the receipt asked for my autograph. At least it was well formatted."
- **Challenge:** Print a neat bill for three items from your town (name, qty, amount) with fixed widths and a total line.
- **Challenge answer:** Reuse the bill.c pattern: `"%-12s %4d %9.2f\n"` for each item, `"%-12s %4s %9s\n"` for the header, and `"%-12s %4s %9.2f\n"` with `""` for the total line. Columns line up because every line uses widths 12, 4 and 9.

### Shorts for EP 11

**S1 · Messy bill vs rich bill** — 0:25 · built from scenes 1, 8

- **Hook (first 1.5s):** "Same bill. One looks broke. One looks rich."
- **Script:** Same bill. One looks broke, one looks rich. The secret: widths inside printf. Percent minus twelve s for the name, percent four d for the quantity, percent nine point two f for the amount. Same widths on every line, and the columns line up.
- **On-screen text:** %-12s %4d %9.2f
- **Caption + hashtags:** Make your C output look professional. #cprogramming #learntocode #kodingkonkani #printf #ctutorial

**S2 · printf in 30 seconds** — 0:35 · built from scenes 3–5

- **Hook (first 1.5s):** "Every part of %-8.2f, explained."
- **Script:** Percent minus eight point two f. Percent: start. Minus: left-align. Eight: width, at least eight spaces. Point two: two digits after the decimal. f: it's a float. Want zeros instead of spaces? Percent zero five d. Want a real percent sign? Percent percent.
- **On-screen text:** % FLAG WIDTH .PRECISION TYPE
- **Caption + hashtags:** printf format specifiers, decoded. #cprogramming #learntocode #kodingkonkani #printf #coding

**S3 · Why does printf print garbage?** — 0:30 · built from scene 9

- **Hook (first 1.5s):** "Price is 45.5. printf says 2 billion."
- **Script:** The price is forty-five point five. printf says two billion. Why? I used percent d for a float. printf trusts the placeholder and reads the wrong bits. Compile with dash Wall and GCC tells you: percent d expects int, but argument has type double. Fix: percent point two f.
- **On-screen text:** %d + float = GARBAGE
- **Caption + hashtags:** Match your placeholders. #cprogramming #codingbugs #kodingkonkani #learntocode #printf

**S4 · Well formatted** — 0:10 · built from scene 7

- **Hook (first 1.5s):** "My output was so neat..."
- **Script:** My printf output was so neat, the receipt asked for my autograph. At least it was well formatted.
- **On-screen text:** %9.2f OF FAME
- **Caption + hashtags:** Formatting humour. #programmingjokes #cprogramming #kodingkonkani #learntocode

**S5 · What does this print?** — 0:20 · built from scene 4

- **Hook (first 1.5s):** "What does %05d print for 42?"
- **Script:** printf, percent zero five d, forty-two. What prints? A: 42. B: three spaces then 42. C: 00042. ... C. Width five, padded with zeros. Comment if you got it right.
- **On-screen text:** printf("%05d", 42); · A) 42 B) "   42" C) 00042
- **Caption + hashtags:** printf quiz. #cquiz #cprogramming #kodingkonkani #learntocode #printf

## EP 12 — scanf: Taking Input

**Module 1 · First program & basics · 6:45 · Pastel blue + Tomato · Prerequisite: EP 11**

**Learning goals:** read an `int`, a `float` and a `char` from the keyboard with `scanf`; explain what `&` does ("the address of the box"); use `" %c"` to skip a leftover Enter; read two numbers in one `scanf` call.

### YouTube

- **Title:** Let the User Talk Back | scanf in C EP 12
- **Description:** Until now our programs only talked. With scanf, the user can type numbers and letters into your program. Learn how scanf works, why it needs the & sign, and the sneaky Enter key that ruins %c. Plus the crash you get when you forget &. 0:00 Let the user talk back 0:20 How scanf works 0:55 Reading an int 1:55 What does & mean? 2:40 Reading a float and a char 3:35 Two numbers at once 4:19 Bug of the Day: forgetting & 5:54 Challenge 6:29 Next episode
- **Tags:** c programming, scanf in c, user input c, scanf ampersand, address of operator, scanf %c newline, read integer c, c tutorial for beginners, koding konkani, learn c
- **Thumbnail:** big text "TYPE BACK!"; a keyboard with a speech bubble coming out of the screen; Xecxec typing with both claws, tongue out in concentration.

### Scene list

| # | Start | Length | Template | On screen | Animation & SFX |
| --- | --- | --- | --- | --- | --- |
| 1 | 0:00 | 0:15 | Terminal | `Enter your age:` prompt, cursor blinks, user types 17 | Keyboard clacks; Xecxec leans in, claw-click |
| 2 | 0:15 | 0:05 | Title card | EP 12 · SCANF: TAKING INPUT | Title slams in, whoosh |
| 3 | 0:20 | 0:35 | Concept slide | Last challenge answer; printf sends text out, scanf brings values in | Two arrows: printf from program to screen, scanf from keyboard to program |
| 4 | 0:55 | 1:00 | Code explain | ep12.c lines 5, 9–10 | Prompt types out; value 17 flies from keyboard into the age box; tracker age=17 |
| 5 | 1:55 | 0:45 | Memory boxes | Box `age` with an address tag on its side (e.g. 0x...); `&age` points to the tag | Address tag flips out like a house number plate; on screen: "your address will differ" |
| 6 | 2:40 | 0:55 | Code explain | Lines 12–16: `%f` with &height, `" %c"` with &section | Leftover Enter shown as a small "\\n" block sitting in the input queue, swept away by the space |
| 7 | 3:35 | 0:40 | Code explain | ep12\_sum.c reading two numbers in one call | Two values fly into two boxes; sum appears with ding |
| 8 | 4:15 | 0:04 | Pun card | Pun | Drum ba-dum, claw-click |
| 9 | 4:19 | 1:35 | Bug of the Day | `scanf("%d", age);` without &; GCC warnings; program crashes | Butter stripe; value flies to a random address and explodes; buzzer; fix with & and success chime |
| 10 | 5:54 | 0:35 | Challenge | Read two numbers, print their sum (and product as a bonus) | Timer ticks; keyboard waits |
| 11 | 6:29 | 0:16 | Outro | Next: EP 13 · Type casting; sign-off | Xecxec waves; outro sting |

### Narration script

**\[1 · Hook\]** Every program so far has been a one-way conversation. It talks, you listen. Today, that changes. Your program will ask a question, and wait for you to answer.

**\[2 · Title\]** Episode twelve. scanf: taking input.

**\[3 · How it works\]** First, the challenge: a neat bill for three items of your choice. If your columns lined up, you're a printf pro now. Today's tool is printf's twin, scanf. printf takes values from your program and sends them out to the screen. scanf goes the other way. It takes what the user types on the keyboard and puts it into a variable. Same placeholders: percent d, percent f, percent c. Just in the other direction.

**\[4 · Reading an int\]** \[HL 5\] Line five: int age. An empty box, waiting. \[HL 9\] Line nine: printf, "Enter your age: ". Notice there's no backslash n, so the cursor stays on the same line, right after the question. That looks nicer. \[HL 10\] Line ten: scanf, "percent d", comma, ampersand age. When the program reaches this line, it stops and waits. The user types seventeen and presses Enter. scanf reads it as a whole number, because of percent d, and stores it in age. \[TRACK age=17\] The program continues.

**\[5 · What is &\]** So what is that ampersand? Remember: every variable is a box in memory. Every box has an address, like a house number. The ampersand means "the address of". So and-age means "the address of the age box". Why does scanf need it? printf only needs the value, so you hand it the value. But scanf must put a value into your box. So you tell it where the box lives. Without the address, scanf has nowhere to deliver. Like ordering from a delivery app without giving your address. The addresses on screen are just examples. Yours will differ. We'll go much deeper into addresses in the pointers module.

**\[6 · float and char\]** \[HL 12\] Line twelve asks for height. \[HL 13\] Line thirteen: scanf with percent f and ampersand height. The user types one point six eight. \[TRACK height=1.68\] \[HL 15\] Line fifteen asks for the section. \[HL 16\] Now look closely at line sixteen. The quote has a space, then percent c. Why the space? When the user typed one point six eight, they also pressed Enter. scanf took the number, but the Enter key is still sitting there, waiting. percent c reads any single character, including Enter. Without the space, section would get the Enter, not the letter. The space tells scanf: skip any spaces and Enters first, then read the character. \[TRACK section='B'\] \[HL 18\] Line eighteen prints everything: Age 17, height 1.68 m, section B.

**\[7 · Two at once\]** One scanf can read more than one value. \[HL 6\] Line six: printf, "Enter two numbers: ". \[HL 7\] Line seven: scanf, "percent d space percent d", ampersand a, ampersand b. The user can type twelve, space, thirty, or twelve, Enter, thirty. Both work, because percent d skips spaces and Enters on its own. \[TRACK a=12\] \[TRACK b=30\] \[HL 8\] Line eight prints a plus b. Sum: 42.

**\[8 · Pun\]** scanf asked for my address. I said, "Aren't we moving a bit fast?"

**\[9 · Bug of the Day\]** Today's bug is the most famous scanf mistake in the world. scanf, "percent d", age. No ampersand. With dash Wall, GCC warns twice. First: format percent d expects argument of type int star, but argument 2 has type int. int star means "an address of an int". GCC wanted an address and got a plain number. Second: age is used uninitialized. Because without the ampersand, we're passing the junk value inside age. Run it anyway. Type seventeen. And the program crashes. On Linux you see "Segmentation fault". On Windows, the program usually just stops, and Age is never printed. What happened? scanf treated the junk value as an address, and tried to write seventeen into some random place in memory that doesn't belong to us. The operating system stopped it. The fix is one character: ampersand age. Now it prints Age: 17. Rule: printf takes values. scanf takes addresses.

**\[10 · Challenge\]** Your challenge. Ask the user for two whole numbers. Read both with one scanf. Print their sum. Bonus: also print their product. Don't forget your ampersands.

**\[11 · Outro\]** Next episode: type casting. Why does five divided by two give two? Keep coding, says Xecxec!

### Code shown

```c
#include <stdio.h>

int main(void)
{
    int age;
    float height;
    char section;

    printf("Enter your age: ");
    scanf("%d", &age);

    printf("Enter your height in metres: ");
    scanf("%f", &height);

    printf("Enter your section: ");
    scanf(" %c", &section);     // space skips the leftover Enter

    printf("Age %d, height %.2f m, section %c\n", age, height, section);
    return 0;
}
```

**Expected run** (user types 17, 1.68, B):

```text
Enter your age: 17
Enter your height in metres: 1.68
Enter your section: B
Age 17, height 1.68 m, section B
```

ep12\_sum.c (scene 7):

```c
#include <stdio.h>

int main(void)
{
    int a, b;
    printf("Enter two numbers: ");
    scanf("%d %d", &a, &b);
    printf("Sum: %d\n", a + b);
    return 0;
}
```

**Expected run** (user types 12 30):

```text
Enter two numbers: 12 30
Sum: 42
```

### Bug of the Day

```c
#include <stdio.h>

int main(void)
{
    int age;
    printf("Enter your age: ");
    scanf("%d", age);
    printf("Age: %d\n", age);
    return 0;
}
```

**GCC output with `-Wall`:**

```text
bug12.c: In function 'main':
bug12.c:7:13: warning: format '%d' expects argument of type 'int *', but argument 2 has type 'int' [-Wformat=]
    7 |     scanf("%d", age);
      |            ~^   ~~~
      |             |   |
      |             |   int
      |             int *
bug12.c:7:5: warning: 'age' is used uninitialized [-Wuninitialized]
    7 |     scanf("%d", age);
      |     ^~~~~~~~~~~~~~~~
bug12.c:5:9: note: 'age' was declared here
    5 |     int age;
      |         ^~~
```

**Wrong result** (user types 17): the program crashes. On Linux the terminal shows `Segmentation fault`; on Windows the program usually stops silently and `Age:` is never printed. On screen: "exact crash message depends on your system".

```text
Enter your age: 17
```

**Fixed:**

```c
#include <stdio.h>

int main(void)
{
    int age;
    printf("Enter your age: ");
    scanf("%d", &age);
    printf("Age: %d\n", age);
    return 0;
}
```

```text
Enter your age: 17
Age: 17
```

scanf needs the address of the box (`&age`) so it can write into it; without `&` it uses the junk value as an address and writes to memory the program does not own.

### Pun & challenge

- **Pun:** "scanf asked for my address. I said: aren't we moving a bit fast?"
- **Challenge:** Read two whole numbers with one `scanf` and print their sum. Bonus: print the product too.
- **Challenge answer:**

```c
#include <stdio.h>

int main(void)
{
    int a, b;
    printf("Enter two numbers: ");
    scanf("%d %d", &a, &b);
    printf("Sum: %d\n", a + b);
    printf("Product: %d\n", a * b);
    return 0;
}
```

```text
Enter two numbers: 12 30
Sum: 42
Product: 360
```

### Shorts for EP 12

**S1 · Your program can listen** — 0:20 · built from scenes 1, 4

- **Hook (first 1.5s):** "Your program can finally listen."
- **Script:** Your program can finally listen. printf asks, "Enter your age". scanf, percent d, ampersand age, waits for you to type. You type seventeen, press Enter, and it's stored in age. Two lines. Your first interactive program.
- **On-screen text:** scanf("%d", &age);
- **Caption + hashtags:** User input in C, made simple. #cprogramming #learntocode #kodingkonkani #scanf #ctutorial

**S2 · What does & mean?** — 0:30 · built from scene 5

- **Hook (first 1.5s):** "Why does scanf need this & sign?"
- **Script:** Why does scanf need the ampersand? Every variable lives at an address in memory, like a house number. Ampersand age means "the address of age". printf only needs the value. But scanf has to deliver a value into your box, so it needs the address. No address, no delivery.
- **On-screen text:** & = "ADDRESS OF"
- **Caption + hashtags:** The & in scanf, explained. #cprogramming #learntocode #kodingkonkani #scanf #pointers

**S3 · One missing & = crash** — 0:30 · built from scene 9

- **Hook (first 1.5s):** "One missing character crashed my program."
- **Script:** One missing character crashed my program. scanf, percent d, age. No ampersand. scanf used the junk inside age as an address and wrote into random memory. Crash. GCC with dash Wall warned me: expects int star, but argument has type int. Fix: ampersand age.
- **On-screen text:** scanf("%d", age); → CRASH
- **Caption + hashtags:** The most famous scanf bug. #cprogramming #codingbugs #kodingkonkani #learntocode #scanf

**S4 · scanf moves fast** — 0:10 · built from scene 8

- **Hook (first 1.5s):** "scanf asked for my address."
- **Script:** scanf asked for my address. I said, aren't we moving a bit fast?
- **On-screen text:** &you
- **Caption + hashtags:** Address-of humour. #programmingjokes #cprogramming #kodingkonkani #learntocode

**S5 · Why was my char skipped?** — 0:25 · built from scene 6

- **Hook (first 1.5s):** "Spot the difference: "%c" vs " %c""
- **Script:** Spot the difference. scanf, percent c, versus scanf, space percent c. After you type a number and press Enter, that Enter is still waiting. Plain percent c grabs it, and your letter is skipped. Space percent c skips the Enter first. Which one should you use? Space percent c.
- **On-screen text:** "%c" vs " %c" · WHICH ONE?
- **Caption + hashtags:** The invisible Enter key bug. #cquiz #cprogramming #kodingkonkani #learntocode #scanf

## EP 13 — Type Casting

**Module 1 · First program & basics · 6:25 · Pastel blue + Tomato · Prerequisite: EP 12**

**Learning goals:** predict the result of integer division and `%`; explain implicit conversion (int mixed with double becomes double); write an explicit cast like `(float)a / b`; know that casting to `int` truncates instead of rounding; place the cast before the division, not after.

### YouTube

- **Title:** Why 5 / 2 Is 2 in C | Type Casting EP 13
- **Description:** In C, 5 divided by 2 is 2. Not 2.5. Learn why integer division throws away the remainder, how C converts types on its own, and how to take control with a cast. Plus the bill-splitting bug that cheats your friend out of 50 paise. 0:00 Why 5 / 2 is 2 0:20 Integer division and % 1:15 Implicit conversion 2:00 Explicit cast 2:45 Casting to int truncates 3:30 char to int 4:04 Bug of the Day: splitting the bill 5:34 Challenge 6:09 Next episode
- **Tags:** c programming, type casting in c, integer division, implicit conversion, explicit cast, modulus operator, float division c, c tutorial for beginners, koding konkani, learn c
- **Thumbnail:** big text "5 / 2 = 2 ?!"; a calculator showing 2.5 with a big red cross, and C code showing 2; Xecxec holding half a coconut, confused.

### Scene list

| # | Start | Length | Template | On screen | Animation & SFX |
| --- | --- | --- | --- | --- | --- |
| 1 | 0:00 | 0:15 | Terminal | Program prints `5 / 2 = 2`; calculator beside it shows 2.5 | Calculator beep; record scratch; Xecxec drops a coconut |
| 2 | 0:15 | 0:05 | Title card | EP 13 · TYPE CASTING | Title slams in, whoosh |
| 3 | 0:20 | 0:55 | Code explain | Last challenge answer; ep13.c lines 5–8 | Five coconuts shared between two crabs: 2 each, 1 left over (the remainder) |
| 4 | 1:15 | 0:45 | Code explain | Line 9: `5.0 / 2`; a "type ladder" int, float, double | The int 2 climbs the ladder to become 2.0; result 2.5 |
| 5 | 2:00 | 0:45 | Code explain | Line 10: `(float)a / b` | A tomato "(float)" stamp lands on `a`; tracker shows 5 becoming 5.0 |
| 6 | 2:45 | 0:45 | Code explain | Lines 12–14: `(int)price` gives 99 | A knife slices off .99; it falls into the sea with a splash; label "cut, not rounded" |
| 7 | 3:30 | 0:30 | Code explain | Lines 16–17: `(int)letter` gives 65 | Callback to EP 08: A morphs into 65 |
| 8 | 4:00 | 0:04 | Pun card | Pun | Drum ba-dum, claw-click |
| 9 | 4:04 | 1:30 | Bug of the Day | Splitting Rs 7 between 2 friends gives 3.00; fix with a cast; also the "cast too late" version | Butter stripe; 50 paise coin rolls away; buzzer; fix and success chime |
| 10 | 5:34 | 0:35 | Challenge | Read 3 marks, print the average with 2 decimals | Timer ticks; three report cards |
| 11 | 6:09 | 0:16 | Outro | Next: EP 14 · Mini project: unit converter; sign-off | Xecxec waves; outro sting |

### Narration script

**\[1 · Hook\]** Ask your calculator: five divided by two. Two point five. Ask C. Two. Is C bad at maths? No. C is just very, very literal. Today you'll learn exactly what it's thinking.

**\[2 · Title\]** Episode thirteen. Type casting.

**\[3 · Integer division\]** First, the challenge: read two numbers with one scanf, print the sum and product. With twelve and thirty, sum forty-two, product three sixty. Now. \[HL 5\] Line five: int a equals five, b equals two. \[TRACK a=5\] \[TRACK b=2\] \[HL 7\] Line seven prints a divided by b. Both are ints. When C divides an int by an int, the answer is also an int. Any fraction is thrown away. Think of five coconuts shared between two crabs. Each crab gets two whole coconuts. You can't hand out half a coconut in integer land. So five by two is two. \[HL 8\] And the leftover coconut? That's what percent, the modulus operator, gives you. Five modulus two is one, the remainder. In printf, we write percent percent to show the percent sign, like we learned in episode eleven.

**\[4 · Implicit\]** \[HL 9\] Line nine: five point zero divided by two. Now one side is a double. When C mixes types in one calculation, it quietly converts the smaller type to the bigger one. This is called implicit conversion. Picture a ladder: int at the bottom, then float, then double. The int two climbs up and becomes two point zero. Now it's double divided by double, and the answer is two point five.

**\[5 · Explicit\]** But what if both values are int variables? You can't add point zero to a variable. Instead, you cast. \[HL 10\] Line ten: open bracket, float, close bracket, a, divided by b. The type in brackets is a cast. It says: "treat a as a float, just for this calculation." \[TRACK a=5.0\] a becomes five point zero for a moment. Now it's float divided by int, so b climbs the ladder too, and we get two point five. The variable a itself is still an int with value five. The cast doesn't change the box, only the value we use.

**\[6 · Truncation\]** Casting works in the other direction too. \[HL 12\] Line twelve: float price equals ninety-nine point nine nine. \[HL 13\] Line thirteen: int rupees equals bracket int bracket price. \[TRACK rupees=99\] You get ninety-nine, not a hundred. Casting to int does not round. It just cuts off everything after the decimal point. This is called truncation, and it's the same thing we saw in episode eight with two point five kilos of fish.

**\[7 · char\]** \[HL 16\] Line sixteen: char letter equals A. \[HL 17\] Line seventeen casts it with bracket int. Code of A is 65. In episode eight we saw this with percent d. The cast makes it clear in the code that we really want the number.

**\[8 · Pun\]** I tried to cast my int as the hero of the movie. It said, "Sorry, I only do whole roles."

**\[9 · Bug of the Day\]** Today's bug. You and your friend split a seven-rupee bus ticket. int total equals seven, int people equals two. float share equals total divided by people. Print with point two f. Each pays: three point zero zero. Somebody just lost fifty paise. But share is a float, so why? Because C does the right side first. total divided by people is int divided by int, so the answer is three. Only then is three stored in the float, as three point zero. No warning, even with dash Wall. The fix: cast before dividing. bracket float total, divided by people. Now: three point five zero. And watch out for this trap. If you write bracket float, then brackets around total divided by people, the division still happens first in int, and you cast a three. Cast the number, not the answer.

**\[10 · Challenge\]** Your challenge. Read three marks as ints, with one scanf. Print their average with two decimals. Test with seventy-eight, eighty-five and ninety. If you get eighty-four point zero zero, you've hit today's bug. The right answer is eighty-four point three three.

**\[11 · Outro\]** Next episode is our first mini project: a unit converter. Kilometres to miles, rupees to dollars, and more. Everything from module one, in one program. Keep coding, says Xecxec!

### Code shown

```c
#include <stdio.h>

int main(void)
{
    int a = 5, b = 2;

    printf("5 / 2 = %d\n", a / b);              // int / int
    printf("5 %% 2 = %d\n", a % b);             // the remainder
    printf("5.0 / 2 = %f\n", 5.0 / 2);          // implicit: 2 becomes 2.0
    printf("(float)a / b = %.1f\n", (float)a / b);   // explicit cast

    float price = 99.99f;
    int rupees = (int)price;                    // cuts off, no rounding
    printf("Rupees: %d\n", rupees);

    char letter = 'A';
    printf("Code of %c is %d\n", letter, (int)letter);

    return 0;
}
```

**Expected output:**

```text
5 / 2 = 2
5 % 2 = 1
5.0 / 2 = 2.500000
(float)a / b = 2.5
Rupees: 99
Code of A is 65
```

### Bug of the Day

```c
#include <stdio.h>

int main(void)
{
    int total = 7;
    int people = 2;
    float share = total / people;
    printf("Each pays: %.2f\n", share);
    return 0;
}
```

**GCC output:** none, even with `-Wall`. **Wrong output:**

```text
Each pays: 3.00
```

**Fixed:**

```c
#include <stdio.h>

int main(void)
{
    int total = 7;
    int people = 2;
    float share = (float)total / people;
    printf("Each pays: %.2f\n", share);
    return 0;
}
```

```text
Each pays: 3.50
```

The division is done as int / int before the result is stored in the float, so the cast must go on an operand before dividing. Note: `(float)(total / people)` is still wrong (3.00), because the int division happens inside the brackets first.

### Pun & challenge

- **Pun:** "I tried to cast my int as the hero. It said: sorry, I only do whole roles."
- **Challenge:** Read three integer marks with one `scanf` and print the average with 2 decimals. Test with 78, 85, 90.
- **Challenge answer:**

```c
#include <stdio.h>

int main(void)
{
    int m1, m2, m3;
    printf("Enter 3 marks: ");
    scanf("%d %d %d", &m1, &m2, &m3);

    float avg = (m1 + m2 + m3) / 3.0f;
    printf("Average: %.2f\n", avg);
    return 0;
}
```

```text
Enter 3 marks: 78 85 90
Average: 84.33
```

(Dividing by `3` instead of `3.0f` gives `84.00`.)

### Shorts for EP 13

**S1 · C says 5 / 2 = 2** — 0:25 · built from scenes 1, 3

- **Hook (first 1.5s):** "Calculator: 2.5. C: 2."
- **Script:** Calculator says five divided by two is two point five. C says two. Why? Both numbers are ints, so C gives an int answer and throws away the fraction. Five coconuts, two crabs: two each, one left over. And that leftover? Five percent two equals one.
- **On-screen text:** int / int = int
- **Caption + hashtags:** C is not bad at maths. #cprogramming #learntocode #kodingkonkani #integerdivision #ctutorial

**S2 · Casting in 30 seconds** — 0:30 · built from scenes 4–6

- **Hook (first 1.5s):** "How to get 2.5 out of two ints."
- **Script:** How do you get two point five out of two ints? Cast one of them. Bracket float a, divided by b. The cast treats a as a float, so the division becomes a float division. Casting the other way, bracket int ninety-nine point nine nine, gives ninety-nine. It cuts, it does not round.
- **On-screen text:** (float)a / b · (int)99.99 = 99
- **Caption + hashtags:** Type casting in C, fast. #cprogramming #learntocode #kodingkonkani #typecasting #coding

**S3 · Who stole 50 paise?** — 0:30 · built from scene 9

- **Hook (first 1.5s):** "Split Rs 7 between two. C says Rs 3 each."
- **Script:** Split seven rupees between two friends. C says three each. Who stole fifty paise? total divided by people is int divided by int, so you get three, even if you store it in a float. Fix: bracket float total, divided by people. Three point five zero. Cast before you divide.
- **On-screen text:** CAST BEFORE YOU DIVIDE
- **Caption + hashtags:** The integer division trap. #cprogramming #codingbugs #kodingkonkani #learntocode #c

**S4 · Whole roles only** — 0:10 · built from scene 8

- **Hook (first 1.5s):** "I tried to cast my int in a movie."
- **Script:** I tried to cast my int as the hero of the movie. It said, sorry, I only do whole roles.
- **On-screen text:** (int) HERO
- **Caption + hashtags:** Casting call. #programmingjokes #cprogramming #kodingkonkani #learntocode

**S5 · 2.5 or 2.0?** — 0:20 · built from scene 9

- **Hook (first 1.5s):** "Which line gives 2.5?"
- **Script:** int a is five, int b is two. Line one: bracket float, a divided by b. Line two: bracket float, then brackets a divided by b. Which gives two point five? ... Line one. In line two, the int division happens first and gives two.
- **On-screen text:** (float)a / b · vs · (float)(a / b)
- **Caption + hashtags:** Brackets matter. #cquiz #cprogramming #kodingkonkani #learntocode #typecasting

## EP 14 — Mini Project: Unit Converter

**Module 1 · First program & basics · 7:20 · Pastel blue + Tomato · Prerequisite: EP 13**

**Learning goals:** plan a small program as input, calculation, output; combine `#define`, `const`, `scanf`, `double` maths and formatted `printf` in one file; read a `double` with `%lf`; avoid integer division inside a formula by writing `9.0` instead of `9`.

### YouTube

- **Title:** Build a Unit Converter in C | Mini Project EP 14
- **Description:** Our first real project. Using everything from Module 1 (variables, types, constants, scanf, printf and casting), we build a unit converter for kilometres to miles, rupees to dollars and Celsius to Fahrenheit, step by step. Plus the mixed-types bug that makes 37 degrees come out wrong. 0:00 km to miles, rupees to dollars 0:20 Plan: input, process, output 1:00 Header, #define and const 1:55 Reading input with %lf 3:00 The formulas 4:00 Neat output 4:59 Bug of the Day: 9/5 in a formula 6:24 Challenge 6:59 Module 1 complete
- **Tags:** c programming, c mini project, unit converter in c, c project for beginners, scanf %lf, celsius to fahrenheit c, km to miles c, c tutorial for beginners, koding konkani, learn c
- **Thumbnail:** big text "MY FIRST PROJECT"; a retro converter machine with three dials (km, Rs, degrees C); Xecxec in a hard hat turning a dial.

### Scene list

| # | Start | Length | Template | On screen | Animation & SFX |
| --- | --- | --- | --- | --- | --- |
| 1 | 0:00 | 0:15 | Terminal | Finished converter run: inputs typed, results table appears | Keyboard clacks; results drop in with ding; Xecxec in a hard hat claps claws |
| 2 | 0:15 | 0:05 | Title card | EP 14 · MINI PROJECT: UNIT CONVERTER | Title slams in, whoosh |
| 3 | 0:20 | 0:40 | Concept slide | Last challenge answer; plan: Input, Process, Output boxes with what goes in each | Three boxes connected by arrows; items fly into each box |
| 4 | 1:00 | 0:55 | Code explain | converter.c lines 1–13 | Header comment fades in; KM\_PER\_MILE and RUPEES\_PER\_DOLLAR get padlock and tag icons |
| 5 | 1:55 | 1:05 | Code explain | Lines 15–27 | Values fly from keyboard into km, rupees, celsius boxes; tracker updates |
| 6 | 3:00 | 1:00 | Code explain | Lines 29–31 formulas | Each formula animates its numbers: 60 / 1.609344, 500 / 88.0, 37 \* 9.0 / 5 + 32 |
| 7 | 4:00 | 0:55 | Code explain | Lines 33–36 output, with column guides | Guide lines at width 8; results line up with receipt whirr |
| 8 | 4:55 | 0:04 | Pun card | Pun | Drum ba-dum, claw-click |
| 9 | 4:59 | 1:25 | Bug of the Day | `celsius * 9 / 5 + 32` gives 98.0; fix with 9.0 gives 98.6 | Butter stripe; thermometer stuck at 98.0; buzzer; fix and thermometer rises to 98.6, success chime |
| 10 | 6:24 | 0:35 | Challenge | Add one new conversion (e.g. cm to inches) | Timer ticks; a fourth empty dial appears on the machine |
| 11 | 6:59 | 0:21 | Outro | Module 1 complete badge; Next: EP 15 · Module 2 Operators; sign-off | Badge stamps with a thud; confetti; Xecxec dances; outro sting |

### Narration script

**\[1 · Hook\]** Kilometres to miles. Rupees to dollars. Celsius to Fahrenheit. Type three numbers, get three answers, neatly lined up. By the end of this video, you'll have built this yourself, using only what we learned in module one.

**\[2 · Title\]** Episode fourteen. Mini project: unit converter.

**\[3 · Plan\]** First, last time's challenge. With seventy-eight, eighty-five and ninety, the average is eighty-four point three three. If you got eighty-four point zero zero, divide by three point zero instead of three. Now, before any code, a plan. Almost every program has three parts. Input: what does the user give us? Here, a distance in kilometres, an amount in rupees, and a temperature in Celsius. Process: what maths do we do? Three conversion formulas. Output: what do we show? A neat table of results. Planning first saves you from staring at a blank screen.

**\[4 · Setup\]** \[HL 1\] Lines one to six: a header comment, just like episode six taught us. File name, what it does, and where it's from. \[HL 7\] Line seven: include stdio dot h, for printf and scanf. \[HL 9\] Line nine: hash define KM\_PER\_MILE, one point six zero nine three four four. One mile is exactly that many kilometres, and it never changes, so it's a perfect hash define. \[HL 13\] Line thirteen: const double RUPEES\_PER\_DOLLAR equals eighty-eight. This is only an example rate. Real exchange rates change every day, so check today's rate and put it here. Notice it's one line to change, not ten. That's the magic-number lesson from episode ten.

**\[5 · Input\]** \[HL 15\] Line fifteen: double km, rupees. Two decimal boxes in one line. We use double, because it's more precise than float, like we saw in episode nine. \[HL 16\] Line sixteen: int celsius. Whole degrees only, to keep it simple. \[HL 18\] Line eighteen prints a title for our converter. \[HL 20\] Line twenty asks for the distance. \[HL 21\] Line twenty-one: scanf, percent l f, ampersand km. Here's something new. For printf, percent f works for both float and double. But for scanf, a double needs percent l f. l f for "long float". If you use percent f with a double in scanf, you get garbage. \[TRACK km=60\] \[HL 23\] Lines twenty-three \[HL 24\] and twenty-four do the same for rupees. \[TRACK rupees=500\] \[HL 26\] Lines twenty-six \[HL 27\] and twenty-seven read celsius with percent d and ampersand. \[TRACK celsius=37\] Every scanf has its ampersand. Episode twelve would be proud.

**\[6 · Process\]** Now the maths. \[HL 29\] Line twenty-nine: miles equals km divided by KM\_PER\_MILE. Sixty divided by one point six zero nine three four four. \[TRACK miles=37.28\] \[HL 30\] Line thirty: dollars equals rupees divided by RUPEES\_PER\_DOLLAR. Five hundred divided by eighty-eight. \[TRACK dollars=5.68\] \[HL 31\] Line thirty-one: Fahrenheit equals celsius times nine point zero, divided by five, plus thirty-two. Why nine point zero and not nine? Hold that thought. It's today's bug. \[TRACK fahrenheit=98.6\]

**\[7 · Output\]** \[HL 33\] Line thirty-three prints a blank line and a results heading. The backslash n at the start gives some breathing space. \[HL 34\] Line thirty-four: percent eight point two f for km, then percent eight point two f for miles. Width eight, two decimals, from episode eleven. \[HL 35\] Line thirty-five: same widths for rupees and dollars. \[HL 36\] Line thirty-six: percent eight d for celsius, because it's an int, and percent eight point one f for Fahrenheit. Run it. Type sixty, five hundred and thirty-seven. Sixty kilometres is thirty-seven point two eight miles. Five hundred rupees is five point six eight dollars at our example rate. Thirty-seven Celsius is ninety-eight point six Fahrenheit. All numbers in one neat column.

**\[8 · Pun\]** I tried to convert my friend to Fahrenheit. Now he's just a few degrees cooler.

**\[9 · Bug of the Day\]** Now, why nine point zero? Here's the version most people write first: celsius times nine, divided by five, plus thirty-two. Run it with thirty-seven. Ninety-eight point zero. But a normal body temperature is ninety-eight point six! C works left to right. celsius times nine: int times int, three hundred thirty-three. Then divided by five: int divided by int, sixty-six, not sixty-six point six. The point six is lost, like we saw in episode thirteen. Add thirty-two, ninety-eight, and only then is it stored in a double. No warning from GCC. The fix: write nine point zero. Now celsius times nine point zero is a double, three hundred thirty-three point zero, and everything after stays double. Ninety-eight point six. One dot and one zero fixed the whole formula.

**\[10 · Challenge\]** Your challenge. Add one new conversion of your choice. Centimetres to inches, kilograms to pounds, or litres to cups. Use a hash define for the conversion factor, read the value with percent l f, and print it in the same neat style. Share your output in the comments.

**\[11 · Outro\]** And that's module one, complete! You can now store values, choose types, take input and print neat output. Next episode starts module two: operators, where C learns to do real maths and make comparisons. Keep coding, says Xecxec!

### Code shown

```c
/*
 * converter.c
 * Converts km to miles, rupees to dollars,
 * and Celsius to Fahrenheit.
 * Koding Konkani, EP 14
 */
#include <stdio.h>

#define KM_PER_MILE 1.609344

int main(void)
{
    const double RUPEES_PER_DOLLAR = 88.0;   // example rate only

    double km, rupees;
    int celsius;

    printf("=== Xecxec's Unit Converter ===\n");

    printf("Distance in km: ");
    scanf("%lf", &km);

    printf("Amount in rupees: ");
    scanf("%lf", &rupees);

    printf("Temperature in Celsius: ");
    scanf("%d", &celsius);

    double miles = km / KM_PER_MILE;
    double dollars = rupees / RUPEES_PER_DOLLAR;
    double fahrenheit = celsius * 9.0 / 5 + 32;

    printf("\n--- Results ---\n");
    printf("%8.2f km      = %8.2f miles\n", km, miles);
    printf("%8.2f rupees  = %8.2f dollars\n", rupees, dollars);
    printf("%8d Celsius = %8.1f Fahrenheit\n", celsius, fahrenheit);

    return 0;
}
```

**Expected run** (user types 60, 500, 37; on screen: "88.0 is an example rate, use today's rate"):

```text
=== Xecxec's Unit Converter ===
Distance in km: 60
Amount in rupees: 500
Temperature in Celsius: 37

--- Results ---
   60.00 km      =    37.28 miles
  500.00 rupees  =     5.68 dollars
      37 Celsius =     98.6 Fahrenheit
```

### Bug of the Day

```c
#include <stdio.h>

int main(void)
{
    int celsius = 37;
    double fahrenheit = celsius * 9 / 5 + 32;
    printf("%.1f F\n", fahrenheit);
    return 0;
}
```

**GCC output:** none, even with `-Wall`. **Wrong output:**

```text
98.0 F
```

**Fixed:**

```c
#include <stdio.h>

int main(void)
{
    int celsius = 37;
    double fahrenheit = celsius * 9.0 / 5 + 32;
    printf("%.1f F\n", fahrenheit);
    return 0;
}
```

```text
98.6 F
```

`celsius * 9 / 5` is all int maths (333 / 5 = 66), so the .6 is lost before the result reaches the double; `9.0` makes the whole chain double.

### Pun & challenge

- **Pun:** "I tried to convert my friend to Fahrenheit. Now he's a few degrees cooler."
- **Challenge:** Add one new conversion (cm to inches, kg to pounds, or litres to cups) with a `#define` factor, `%lf` input and the same neat output.
- **Challenge answer** (cm to inches as a standalone example):

```c
#include <stdio.h>

#define CM_PER_INCH 2.54

int main(void)
{
    double cm;
    printf("Length in cm: ");
    scanf("%lf", &cm);
    printf("%.2f cm = %.2f inches\n", cm, cm / CM_PER_INCH);
    return 0;
}
```

```text
Length in cm: 30
30.00 cm = 11.81 inches
```

### Shorts for EP 14

**S1 · I built a unit converter** — 0:25 · built from scenes 1, 7

- **Hook (first 1.5s):** "My first C project. 39 lines."
- **Script:** My first C project. Thirty-nine lines. Type kilometres, rupees and Celsius. Get miles, dollars and Fahrenheit, in one neat table. Variables, constants, scanf, printf. Everything from module one, in one program. Full build on the channel.
- **On-screen text:** km → miles · Rs → $ · C → F
- **Caption + hashtags:** Build this in your first week of C. #cprogramming #learntocode #kodingkonkani #cproject #beginnerproject

**S2 · Plan any program in 30 seconds** — 0:30 · built from scene 3

- **Hook (first 1.5s):** "Stuck on a blank screen? Do this first."
- **Script:** Stuck on a blank screen? Plan in three boxes. Input: what does the user give you? Process: what maths do you do? Output: what do you show? For our converter: three numbers in, three formulas, one neat table out. Then the code almost writes itself.
- **On-screen text:** INPUT → PROCESS → OUTPUT
- **Caption + hashtags:** How to start any program. #cprogramming #learntocode #kodingkonkani #programmingtips #coding

**S3 · 37 C = 98.0 F?** — 0:35 · built from scene 9

- **Hook (first 1.5s):** "My converter says body temperature is 98.0."
- **Script:** My converter says thirty-seven Celsius is ninety-eight point zero Fahrenheit. It should be ninety-eight point six. The formula: celsius times nine, divided by five. All ints. So three thirty-three divided by five is sixty-six, not sixty-six point six. Fix: nine point zero. Now it's ninety-eight point six.
- **On-screen text:** \* 9 → 98.0 · \* 9.0 → 98.6
- **Caption + hashtags:** One dot fixed my formula. #cprogramming #codingbugs #kodingkonkani #learntocode #c

**S4 · A few degrees cooler** — 0:10 · built from scene 8

- **Hook (first 1.5s):** "I tried to convert my friend."
- **Script:** I tried to convert my friend to Fahrenheit. Now he's just a few degrees cooler.
- **On-screen text:** FRIEND → FAHRENHEIT
- **Caption + hashtags:** Conversion humour. #programmingjokes #cprogramming #kodingkonkani #learntocode

**S5 · %f or %lf?** — 0:20 · built from scene 5

- **Hook (first 1.5s):** "Reading a double with scanf. %f or %lf?"
- **Script:** You want to read a double with scanf. Percent f or percent l f? ... Percent l f. In printf, percent f works for float and double. In scanf, a double needs percent l f. Remember it.
- **On-screen text:** scanf("%?", &km); · %f or %lf?
- **Caption + hashtags:** The scanf rule for doubles. #cquiz #cprogramming #kodingkonkani #learntocode #scanf
