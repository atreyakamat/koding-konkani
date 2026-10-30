# Koding Konkani — C Course Plan

Oct 30, 2026 · @Atreya

## Overview

Koding Konkani teaches C from zero to sorting algorithms and projects in 86 videos of 5–8 minutes each. Everything is in English and fully animated in Remotion: no on-camera host, an AI narrator explains every line of code, and Crab Xecxec (said "Sheck Sheck") is the animated mascot.

| Decision | Locked choice |
| --- | --- |
| Channel | Koding Konkani |
| Audience | School (Class 11–12) and college first years |
| Language | English only: narration, on-screen text and code |
| Host | None on camera; 100% Remotion animation with code explained line by line |
| Voice | AI male English narrator |
| Length | 86 videos, 5–8 min each, about 9 hours total |
| Release | 3 long videos a week (4 when we have a buffer) plus a Short every day |
| Tone | Friendly, fun, a pun or joke every 1–2 minutes |
| Tool | Remotion, one shared template for every episode |
| Look | Neo-brutalism, pastel tomato and peach with black and white (colours not final) |
| Next series | C++, about 40 videos, planned after C ships |

The goal: a student who finishes all 74 can write, debug and explain a 300-line C project, and pass a first-year C exam.

## Crab Xecxec (Sheck Sheck)

Xecxec is a confident Goan beach crab who thinks he is the best programmer on Baga beach, and is usually right, except when he forgets a semicolon.

- **Look:** chunky tomato-red crab, thick black outline, two big white eyes, a tiny black laptop. Flat neo-brutal style, no gradients.
- **Personality:** cheeky, proud, a little dramatic, never mean to the viewer. Celebrates small wins loudly.
- **Role in each video:** opens with the hook, reacts to bugs, delivers the pun card, and gives the challenge at the end.
- **Moves (animated):** a sideways scuttle on entry, claws up for wins, shell-shake for errors, a claw-snap on every pun.
- **Sound:** a short claw-click "xec-xec" sound as his signature, used on entry and on correct answers.

**Catchphrases (English, on screen):**

- "Semicolon first, questions later!"
- "Compile first, panic later."
- "Shell yeah!" when code runs.
- "That's not a bug, that's a crab-ture."
- "Pinch the pointer, don't lose it."
- Sign-off: "Keep coding, says Xecxec!"

Xecxec doesn't talk; he reacts with animation and his claw-click sound while the narrator explains. His lines appear as speech bubbles.

## Episode template

Every episode follows the same 8 beats, so viewers know the rhythm and we can build each one from one Remotion template.

| # | Beat | Time | What happens |
| --- | --- | --- | --- |
| 1 | Cold open | 0:00–0:15 | Xecxec hits a funny problem or question the episode solves |
| 2 | Title card | 0:15–0:20 | Episode number, title, Koding Konkani logo sting |
| 3 | Why it matters | 0:20–1:00 | A real-life Goan analogy (fish market, bus route, feni bottle labels) |
| 4 | Concept | 1:00–3:00 | Animated explanation: memory boxes, flow arrows, diagrams |
| 5 | Live code | 3:00–5:00 | Code types itself, then the narrator explains every line with highlights, arrows and a live variable tracker; terminal output |
| 6 | Bug of the Day | 5:00–6:00 | The most common student mistake, the error message, the fix |
| 7 | Pun card | anywhere, 1–2 per video | A full-screen card with one pun and a claw-snap sound |
| 8 | Challenge + outro | last 45s | One small task, "answer in comments", next-episode teaser, subscribe |

Shorter topics drop beat 3 to 20 seconds; heavier topics (pointers, memory) stretch beat 4 toward 8 minutes total. Every episode also ships a 30–45 second vertical Short cut from beats 1, 6 and 7.

## Visual design system

Neo-brutalism: flat pastel blocks, thick black borders, hard offset shadows, chunky type. Colours below are a starting set, not final.

| Token | Hex | Use |
| --- | --- | --- |
| Tomato | #FF6F59 | Xecxec, primary buttons, highlights, title cards |
| Peach | #FFD8BE | Main background |
| Cream | #FFF4EC | Cards, code panels on light scenes |
| Ink | #111111 | Borders (4px), text, hard shadows (8px offset) |
| White | #FFFFFF | Text on tomato, code panel light lines |
| Mint (accent) | #B8F2D0 | "Correct" states, output that worked |
| Butter (accent) | #FFE58A | Warnings, "Bug of the Day" badge |

**Type:** Space Grotesk or Archivo Black for titles, JetBrains Mono for code. Titles all-caps, tight letter spacing.

**Shapes:** rectangles with 4px black borders, 0–8px corners, hard 8px black drop shadows, no gradients, no blur.

**Scene types in the Remotion template:**

1. **Title card** — tomato block, episode number in a black sticker, title slams in.
2. **Talking slide** — peach background, 1–3 bold lines, Xecxec in the corner.
3. **Code panel** — cream window with black border, typed code, line highlight in butter.
4. **Memory boxes** — variables as labelled boxes with addresses; pointers as thick black arrows.
5. **Terminal** — black window, white monospace output, mint for success, tomato for errors.
6. **Bug of the Day** — butter badge, error message shake, then the fix.
7. **Pun card** — full-screen tomato, one white line, claw-snap.
8. **Challenge card** — cream card with a checkbox list and "Comment your answer".
9. **Outro / end screen** — next video tile, subscribe block, Xecxec waving.

**Motion:** snappy spring pops and slams (no slow fades), 8–12 frame moves, a slight 2-frame shake on impacts. Matching sound effect on every move.

Design mock-ups of these scenes come next, once you approve this direction.

## Audio

A single AI male English narrator voices every episode; English text-to-speech is mature, so this is low risk.

**Voice plan**

1. I write each script in English: narration, on-screen text, code and the exact line being explained at each moment.
2. We test 3–4 male voices (warm, friendly, clear, slightly upbeat) on a 30-second sample and you pick one. The same voice is used for all 86 videos.
3. The voice is generated with word timestamps, so highlights and animations fire exactly when a line is mentioned.
4. Free open models come first; any paid voice tool needs your OK before I sign up.

**Music:** one upbeat lo-fi bed under narration at -24 dB, ducked under speech; a short 3-second Koding Konkani sting on the title card. Royalty-free only, so YouTube doesn't flag it.

**Sound effect library (reused every episode)**

| Moment | Sound |
| --- | --- |
| Xecxec enters / correct answer | Claw click "xec-xec" |
| Code typing | Soft mechanical keys |
| Line highlight | Marker swipe |
| Card slam / title | Thud + whoosh |
| Compile success | Bright ding |
| Compile error | Low buzzer + glass tap |
| Pun card | Claw-snap + rimshot |
| Pointer arrow | Rubber-band twang |

## Course outline: 86 videos

14 modules, 86 videos. Pointers get 9 videos because that's where most students quit, and a dedicated algorithms module (12 videos) animates every sort step by step.

| Module | Videos | Episodes |
| --- | --- | --- |
| 0. Welcome & setup | 4 | 1–4 |
| 1. First program & basics | 10 | 5–14 |
| 2. Operators | 5 | 15–19 |
| 3. Decisions | 6 | 20–25 |
| 4. Loops | 8 | 26–33 |
| 5. Functions | 7 | 34–40 |
| 6. Arrays | 6 | 41–46 |
| 7. Strings | 5 | 47–51 |
| 8. Pointers | 9 | 52–60 |
| 9. Structures | 4 | 61–64 |
| 10. Dynamic memory | 4 | 65–68 |
| 11. Files | 3 | 69–71 |
| 12. Algorithms | 12 | 72–83 |
| 13. Projects & finale | 3 | 84–86 |

### Module 0 — Welcome & setup

| # | Title | Covers | Hook | Bug of the Day | Challenge |
| --- | --- | --- | --- | --- | --- |
| 1 | Welcome to Koding Konkani | Course map, meet Xecxec, how to learn | "A crab wants to teach you coding?" | Skipping practice | Comment why you're learning C |
| 2 | What is C, really? | History, compilers, why C still runs the world | "Your phone runs on 50-year-old code" | Thinking C is dead | Name 3 things built in C |
| 3 | Setting up: VS Code + GCC | Install on Windows, test the compiler | "Installing is the real boss fight" | gcc not found (PATH) | Run gcc --version |
| 4 | Hello, World! | main, printf, compile and run | "Your first words to a computer" | Missing semicolon | Print your name and village |

### Module 1 — First program & basics

| # | Title | Covers | Hook | Bug of the Day | Challenge |
| --- | --- | --- | --- | --- | --- |
| 5 | How a C program is built | Preprocess, compile, link, run | "What happens when you hit Enter?" | Editing but not recompiling | Break a file, read the error |
| 6 | Comments & clean code | //, /\* \*/, indentation, naming | "Future you will hate present you" | Unclosed /\* comment | Comment an old program |
| 7 | Variables | Declare, assign, memory boxes | "Variables are labelled fish baskets" | Using uninitialised variables | Store age, height, roll no |
| 8 | Data types: int, float, char | Sizes, ranges, sizeof | "Why 2.5 kg became 2 kg" | Storing decimals in int | Print sizeof every type |
| 9 | More types: long, double, unsigned | Range limits, overflow | "The odometer that rolled back" | Integer overflow | Find the largest int |
| 10 | Constants & #define | const, macros, magic numbers | "Pi doesn't change. Promise." | Changing a const | Circle area with const PI |
| 11 | printf deep dive | Format specifiers, width, precision | "Make your output look rich" | %d for a float | Print a neat bill |
| 12 | scanf: taking input | Reading numbers and chars, & | "Let the user talk back" | Forgetting & in scanf | Read two numbers, print sum |
| 13 | Type casting | Implicit vs explicit, int division | "Why 5/2 is 2" | Integer division surprise | Average of 3 marks |
| 14 | Mini project: Unit converter | Input, maths, formatted output | "km to miles, rupees to dollars" | Mixed types mistakes | Add one new conversion |

### Module 2 — Operators

| # | Title | Covers | Hook | Bug of the Day | Challenge |
| --- | --- | --- | --- | --- | --- |
| 15 | Arithmetic operators | + - \* / %, modulo uses | "Is today an even day?" | % with floats | Even or odd checker |
| 16 | Relational & logical operators | ==, !=, &&, \|\|, ! | "True or false, no maybe" | = instead of == | Check if age is 18–60 |
| 17 | Increment, decrement, assignment | ++, --, +=, pre vs post | "i++ vs ++i: the drama" | Pre/post confusion | Predict 5 outputs |
| 18 | Bitwise operators | &, \|, ^, <<, >> | "Computers only see 0s and 1s" | Mixing & and && | Check a bit is on |
| 19 | Precedence & the ternary | Order of operations, ?: | "Why 2+3\*4 isn't 20" | Missing brackets | Max of 2 with ?: |

### Module 3 — Decisions

| # | Title | Covers | Hook | Bug of the Day | Challenge |
| --- | --- | --- | --- | --- | --- |
| 20 | if and else | Branching basics | "Rain? Take the umbrella" | Semicolon after if() | Pass/fail checker |
| 21 | else-if ladders | Multiple conditions | "Grading: A, B, C… crab" | Wrong order of checks | Marks to grade |
| 22 | Nested if | Conditions inside conditions | "Ticket, ID, then entry" | Dangling else | Leap year checker |
| 23 | switch-case | Menus, break, default | "The restaurant menu machine" | Missing break (fall-through) | Day number to name |
| 24 | Logic puzzles in C | Combining conditions | "Can you beat Xecxec's riddle?" | Over-complicated conditions | Largest of 3 numbers |
| 25 | Mini project: Quiz app | if, switch, score | "Build a quiz for your friends" | Case-sensitive answers | Add 3 questions |

### Module 4 — Loops

| # | Title | Covers | Hook | Bug of the Day | Challenge |
| --- | --- | --- | --- | --- | --- |
| 26 | Why loops? while loop | Repeating safely | "Write 'sorry' 100 times" | Infinite loop | Count 1 to 50 |
| 27 | for loop | Init, condition, update | "The loop with a plan" | Off-by-one | Multiplication table |
| 28 | do-while | Run at least once | "Ask first, check later" | Missing ; after while | Menu that repeats |
| 29 | break & continue | Exiting and skipping | "Emergency exit from a loop" | break in wrong loop | Skip multiples of 3 |
| 30 | Nested loops | Loops inside loops | "Rows and columns of chairs" | Same variable in both loops | Print a grid |
| 31 | Pattern printing 1 | Stars, triangles | "The famous star pattern exam question" | Wrong spaces | Right triangle |
| 32 | Pattern printing 2 | Pyramids, numbers | "Build a pyramid, crab-style" | Space vs star count | Number pyramid |
| 33 | Mini project: Number games | Primes, factorial, reverse digits | "Is 97 prime? Ask C" | Wrong loop bound | Armstrong numbers |

### Module 5 — Functions

| # | Title | Covers | Hook | Bug of the Day | Challenge |
| --- | --- | --- | --- | --- | --- |
| 34 | What are functions? | Reuse, define, call | "Stop copy-pasting your code" | Calling before declaring | Function that greets |
| 35 | Parameters & return values | Inputs and outputs | "A function is a juice machine" | Missing return | Add two numbers |
| 36 | Prototypes & header files | Declarations, .h basics | "Introduce yourself first" | Mismatched prototype | Split into 2 files |
| 37 | Scope & lifetime | Local, global, static | "What happens in a function stays there" | Shadowed variables | Counter with static |
| 38 | Call by value | Copies, why swap fails | "Why my swap didn't swap" | Expecting changes outside | Explain the swap bug |
| 39 | Recursion | Base case, call stack | "A function that calls itself" | No base case (stack overflow) | Factorial recursively |
| 40 | Recursion practice | Fibonacci, power, sum of digits | "Mirror inside a mirror" | Slow recursion | Fibonacci up to 20 |

### Module 6 — Arrays

| # | Title | Covers | Hook | Bug of the Day | Challenge |
| --- | --- | --- | --- | --- | --- |
| 41 | Arrays intro | Declare, index, loop through | "A row of numbered lockers" | Index out of bounds | Store 5 marks |
| 42 | Array operations | Sum, max, min, average | "Who topped the class?" | Starting max at 0 | Find min and max |
| 43 | Searching | Linear and binary search | "Finding your name in the register" | Binary search on unsorted | Search a roll number |
| 44 | Sorting | Why order matters, swapping two values (full sorts in Module 12) | "Line up by height" | Wrong inner loop bound | Sort descending |
| 45 | 2D arrays | Rows, columns, matrices | "A cinema seat map" | Rows and columns swapped | Matrix addition |
| 46 | Arrays & functions | Passing arrays, size | "Hand over the whole locker row" | sizeof inside a function | Average function |

### Module 7 — Strings

| # | Title | Covers | Hook | Bug of the Day | Challenge |
| --- | --- | --- | --- | --- | --- |
| 47 | Strings are char arrays | The \\0 terminator | "The secret character at the end" | No room for \\0 | Print a name letter by letter |
| 48 | Reading strings | scanf, fgets, gets dangers | "Why your full name got cut" | scanf stops at spaces | Read a full address |
| 49 | string.h functions | strlen, strcpy, strcat, strcmp | "C's string toolbox" | Comparing strings with == | Compare two passwords |
| 50 | String manipulation | Reverse, palindrome, count vowels | "Is 'malayalam' a palindrome?" | Off-by-one on length | Count words |
| 51 | Mini project: Text tools | Case changer, word counter | "Build your own mini Word" | Buffer overflow | Add title-case |

### Module 8 — Pointers

| # | Title | Covers | Hook | Bug of the Day | Challenge |
| --- | --- | --- | --- | --- | --- |
| 52 | Memory & addresses | RAM as houses, & operator | "Every variable has a house number" | Printing address with %d | Print 3 addresses |
| 53 | What is a pointer? | Declare, \*, & | "A pointer is a GPS pin" | Uninitialised pointer | Change a value via pointer |
| 54 | Dereferencing | Reading and writing through \* | "Knock on the house door" | \* vs & confusion | Swap the right way |
| 55 | Call by reference | Pointers as parameters | "Fixing the swap bug from ep 38" | Passing value, not address | Function returning 2 results |
| 56 | Pointer arithmetic | p++, steps by type size | "Walking down the street" | Arithmetic on void\* | Walk an array with p++ |
| 57 | Pointers & arrays | Array name as pointer | "The locker row's first key" | Returning a local array | Sum array with pointers |
| 58 | Pointers & strings | char\*, string literals | "Strings were pointers all along" | Modifying a string literal | Own strlen with pointers |
| 59 | Pointer to pointer & NULL | \*\*, NULL checks | "A GPS pin to a GPS pin" | Dereferencing NULL | Safe NULL check |
| 60 | Function pointers | Passing functions around | "A remote control for functions" | Wrong signature | Calculator with function pointers |

### Module 9 — Structures

| # | Title | Covers | Hook | Bug of the Day | Challenge |
| --- | --- | --- | --- | --- | --- |
| 61 | struct basics | Grouping data, . operator | "A student ID card in code" | Forgetting struct keyword | Book struct |
| 62 | Structs, arrays & pointers | Array of structs, -> | "A whole class register" | . vs -> | 5 student records |
| 63 | typedef & enum | Clean names, named constants | "Give your types nicknames" | Enum values clash | Enum for days |
| 64 | union & memory layout | Shared memory, padding | "Why sizeof lied to you" | Reading the wrong union member | Compare struct vs union size |

### Module 10 — Dynamic memory

| # | Title | Covers | Hook | Bug of the Day | Challenge |
| --- | --- | --- | --- | --- | --- |
| 65 | Stack vs heap | Where memory lives | "Your room vs a rented godown" | Huge array on stack | Explain stack vs heap |
| 66 | malloc & free | Allocate, check NULL, release | "Borrow memory, return it" | Forgetting free (leak) | Allocate n marks |
| 67 | calloc & realloc | Zeroed memory, resizing | "Need a bigger basket" | Losing pointer on realloc fail | Growing list |
| 68 | Memory bugs | Leaks, dangling pointers, double free | "The ghost pointer" | Use after free | Find 3 bugs in code |

### Module 11 — Files

| # | Title | Covers | Hook | Bug of the Day | Challenge |
| --- | --- | --- | --- | --- | --- |
| 69 | Writing files | fopen, fprintf, modes | "Make data survive a restart" | Not checking fopen NULL | Save your name to a file |
| 70 | Reading files | fscanf, fgets, EOF | "Reading the diary back" | Infinite EOF loop | Count lines in a file |
| 71 | Binary files & records | fwrite, fread, fseek | "A tiny database" | Text mode for binary data | Save 3 structs |

### Module 12 — Algorithms

Every sort is shown on animated bars that swap and recolour as the narrator walks through each pass, then the C code is explained line by line.

| # | Title | Covers | Hook | Bug of the Day | Challenge |
| --- | --- | --- | --- | --- | --- |
| 72 | What is an algorithm? Big-O made easy | Steps, efficiency, O(1), O(n), O(n²), O(log n) | "Why some code takes 1 second and some takes 1 year" | Nested loops nobody noticed | Rank 4 snippets by speed |
| 73 | Linear vs binary search, visualised | Both searches animated and compared | "Guess my number in 7 tries" | Wrong mid calculation | Binary search on 1–100 |
| 74 | Bubble sort | Passes, swaps, early-exit flag | "The heaviest bubble floats to the top" | Inner loop running too far | Sort marks descending |
| 75 | Selection sort | Find min, swap into place | "Pick the shortest kid, every round" | Swapping inside the inner loop | Count the swaps |
| 76 | Insertion sort | Sorting like playing cards | "How you sort cards in your hand" | Overwriting before shifting | Insert into a sorted list |
| 77 | Recursion, visualised | Call stack animation, Tower of Hanoi | "Move 64 discs before the world ends" | Missing base case | Hanoi with 4 discs |
| 78 | Merge sort | Divide, conquer, merge | "Split the class, sort, then merge" | Wrong mid / leftover elements | Merge two sorted arrays |
| 79 | Quick sort | Pivot, partition, recursion | "Pick a captain, everyone lines up" | Bad pivot, infinite recursion | Sort 10 random numbers |
| 80 | Counting sort | Sorting without comparing | "Sorting 1,000 exam marks instantly" | Negative numbers break it | Sort grades 0–100 |
| 81 | Sorting showdown | Timing all 6 sorts on 10k numbers | "Which sort wins the race?" | Timing the wrong code | Predict the winner |
| 82 | Build your own header library | Write sort.h and sort.c, include guards, reuse | "Make your own #include" | Missing include guards | Add search.h |
| 83 | Stacks and queues with arrays | Push, pop, enqueue, dequeue | "Plates in a pile vs the bus queue" | Overflow and underflow | Bracket-matching checker |

### Module 13 — Projects & finale

| # | Title | Covers | Hook | Bug of the Day | Challenge |
| --- | --- | --- | --- | --- | --- |
| 84 | Project: Student record system | Structs, files, menus | "Your college office, in C" | Messy menu loops | Add a search feature |
| 85 | Project: Bank / ATM simulator | Functions, files, validation | "Withdraw without breaking the bank" | No input validation | Add a PIN check |
| 86 | Finale: exam prep & what's next | Top 20 exam questions, C++ teaser | "Xecxec's final exam" | Panicking in exams | Comment your final score |

## Pun and joke bank

A starter set of 20; each episode script picks 1–2 that match its topic.

| Topic | Pun / joke |
| --- | --- |
| Semicolons | "Without a semicolon, my code has no point; with it, it has a full stop." |
| Variables | "I tried to change, but I was declared const." |
| Data types | "Float like a butterfly, int like a bee." |
| Overflow | "My bank balance has integer overflow. In the wrong direction." |
| Comments | "Comments are like fish curry recipes: nobody writes them down, everyone regrets it." |
| if/else | "If you skip this video, else you'll regret it." |
| switch | "I wanted a break, but switch forgot it and fell through." |
| Loops | "Why did the loop go to therapy? It had trouble letting go." |
| Infinite loop | "Goa traffic on a Sunday: an infinite while loop." |
| Functions | "Functions are like susegad Goans: called only when needed." |
| Recursion | "To understand recursion, watch episode 39. To understand episode 39, understand recursion." |
| Arrays | "Arrays start at 0. Xecxec's patience starts at -1." |
| Strings | "A string walks into a bar and forgets its \\0. It never leaves." |
| Pointers | "I'd tell you a pointer joke, but you'd have to dereference it." |
| Pointers | "Pinch the pointer, don't lose it. Crab advice." |
| NULL | "My ex is like a NULL pointer: touch it and everything crashes." |
| struct | "A struct is just a variable that went to the gym." |
| malloc/free | "Free your memory. Unlike your Goan aunty, who remembers everything." |
| Files | "fopen without fclose is like opening the fridge and walking away." |
| Bugs | "It's not a bug, it's a crab-ture." |

Puns appear as full-screen pun cards and are read by the narrator, followed by Xecxec's claw-snap.

## Production pipeline

Each episode goes script → voice → animation → review → upload; once the template exists, 3 episodes a week is realistic.

1. **Script** — I write narration, on-screen text, code, the line-by-line explanation, puns and timings in one script file per episode.
2. **Your review** — you approve or change the script.
3. **Voice** — the AI narrator reads it; I level it to -16 LUFS and get word timestamps.
4. **Timing** — word timestamps drive when each highlight, arrow and animation fires.
5. **Render** — Remotion builds the long video (16:9, 1080p) plus Shorts (9:16).
6. **Your review** — watch, leave notes, I fix.
7. **Upload** — you upload; I prepare title, description, chapters and tags. I never publish for you.

**Release schedule:** 3 long videos a week (Mon, Wed, Fri), going to 4 when we have 2+ weeks of finished videos banked. A Short every day: 7 a week, cut from the long videos (hook, Bug of the Day, pun card, sort animations). At 3 a week the 86 videos take about 29 weeks; starting the week of 9 November 2026, the C series finishes around late May 2027, or mid-April at 4 a week. Daily Shorts need about 2 per long video plus a few standalone ones.

**Repo:** a new koding-konkani Remotion project on a branch with draft PRs, like your other video projects.

## Open decisions & next steps

- [ ] Approve the 86-video outline (add, cut or reorder episodes)
- [ ] Pick final colours from the scene template sheet
- [ ] Pick the narrator voice from the 30-second test
- [ ] Decide: GitHub repo name for the Remotion project
- [ ] Next from me: episode 1 script, then the voice test, then the Remotion template
