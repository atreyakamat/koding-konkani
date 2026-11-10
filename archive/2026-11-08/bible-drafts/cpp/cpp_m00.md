# Module 0 — Welcome & setup

Episodes 1–4 · Peach + Tomato · g++ 13.3, -std=c++17 -Wall -Wextra

## EP 01 — Hello, C++!

**Module 0 · Welcome & setup · 5:17 · Peach + Tomato · Prerequisite: none (the C course helps, but is not required)**

**Learning goals:** write and run a first C++ program; name its three parts: include, main and cout; know that every statement ends with a semicolon.

### YouTube

- **Title:** Hello, C++! Your First Program | C++ Programming EP 01
- **Description:** Write, compile and run your very first C++ program with Xecxec the crab. No experience needed, just bring curiosity. 0:00 Intro · 0:20 What is C++? · 1:00 The program line by line · 1:40 From code to program · 2:15 Run it in your head · 3:00 Compile and run · 3:20 Recap · 3:55 Bug of the Day · 4:42 Challenge · 5:02 Next episode
- **Tags:** c++, c++ for beginners, c++ tutorial, hello world c++, cout, koding konkani, learn programming, class 11 computer science, first year engineering, coding in goa
- **Thumbnail:** big text "HELLO, C++!" in tomato on peach; Xecxec waving a claw at a dark-blue terminal card showing Hello, Goa!; thin black border and drop shadow.

### Scene list

| # | Start | Length | Template | On screen | Animation & SFX |
| --- | --- | --- | --- | --- | --- |
| 1 | 0:00 | 0:20 | Title card | EP 01 · HELLO, C++! | Tomato title card: EP sticker thuds in, title stamps with a whoosh, Xecxec scuttles in and waves; thud, whoosh, claw-click, sting |
| 2 | 0:20 | 0:40 | Concept slide | "What is C++?": three numbered lines and a fish-curry recipe card on the right | Lines spring in one by one with a pop; the recipe card slides in from the right |
| 3 | 1:00 | 0:40 | Code explain | `hello.cpp`: the 7-line first program, line 4 is the star | Code types in with key-tick; butter [HL n] highlight sweeps line by line with marker-swipe; explanation card on the right |
| 4 | 1:40 | 0:35 | Concept slide | Three boxes: your code, the compiler, the program; arrows between them | Three boxes appear left to right; arrows draw on between them with a whoosh; a tomato cross pops on the compiler box for the error case |
| 5 | 2:15 | 0:45 | Code explain | `hello.cpp` again, with the output panel on the right | Same code; the output panel fills line by line with a ding per output line; [TRACK] cards update |
| 6 | 3:00 | 0:20 | Terminal | Terminal: `g++ hello.cpp -o hello`, then `./hello` | Dark-blue terminal: the command types with key-tick, output prints in mint with a ding |
| 7 | 3:20 | 0:35 | Concept slide | Recap: four ideas on one card | Four recap lines tick in one by one with a pop; Xecxec nods after each tick |
| 8 | 3:55 | 0:40 | Bug of the Day | BUG OF THE DAY: a statement with no semicolon | Butter banner drops in with a buzzer; wrong code shakes; the g++ error lines appear in tomato; the fix slides in and the terminal turns mint with a ding |
| 9 | 4:35 | 0:07 | Pun card | I told my compiler a joke. It said: expected ';' before 'laugh'. | Full tomato screen, card flips in with a rimshot, Xecxec snaps his claw |
| 10 | 4:42 | 0:20 | Challenge | Task card: print your name, then your favourite beach | Task card pops in; checklist ticks with a pop; Xecxec holds a tiny pen |
| 11 | 5:02 | 0:15 | Outro | Next: EP 02 · Setting up and compiling | Next-episode card slides up with a whoosh; right side stays empty for end-screen elements; sign-off text types in |

### Narration script

**[1 · Title]** Welcome to Koding Konkani! I am your narrator, and this little crab is Xecxec. In this series you will learn C plus plus, one small idea at a time. Today, we write our very first program.

**[2 · What is C++]** C plus plus is a programming language. You write instructions in plain text. Then a tool called the compiler turns those instructions into a real program. Think of a recipe card for fish curry. The card is your code, and the kitchen is the computer. The card does nothing until someone cooks it. Computers only understand ones and zeros. The compiler translates your words into those numbers, so you never have to.

**[3 · The program]** [HL 1] The first line says, include iostream. It brings in the tools for printing to the screen. [HL 3] Every C plus plus program starts running at main. [HL 4] Here is the star. std colon colon cout sends text to the screen. The two arrows push the text towards it. [HL 5] A second line prints the sign-off. [HL 6] Return zero tells the computer, all went well.

**[4 · From code to program]** Here is the journey. Your code goes into the compiler. The compiler checks every word. If it is happy, it builds a program. Only then can the computer run it. If the compiler is not happy, it tells you the line number. That is why you will see two kinds of messages: compiler errors before the program runs, and results after.

**[5 · Run it in your head]** [HL 4] When this line runs, Hello, Goa appears. [HL 5] Next, the second line prints below it. The word endl means end of line, so the next text starts fresh underneath. Change the words inside the quotes and the output changes too. Try your own name. Before you run it, predict the output. Two lines. The second one says, Keep coding, says Xecxec. Were you right? Predicting before running is the habit that makes you fast.

**[6 · Compile and run]** In the terminal, type g plus plus, the file name, dash o, hello. No message means success. Now run it with dot slash hello. There it is. Our first program.

**[7 · Recap]** Let us recap. One: every C plus plus program starts at main. Two: include iostream gives you cout, and cout prints text with arrows. Three: every statement ends with a semicolon. And remember the journey: code, compiler, program. If you can say those four things out loud, you have understood today's episode. Pause the video, and say them once, slowly.

**[8 · Bug of the Day]** Bug of the Day. Our code has no semicolon after endl. The compiler says, expected semicolon before return. Notice it points at the end of the line, and shows the next line underneath. Add the semicolon, and it compiles. If you ever see this message, look at the line above the one it names.

**[9 · Pun]** I told my compiler a joke. It said: expected semicolon before laugh.

**[10 · Challenge]** Your challenge: print your name on one line, and your favourite beach on the next. Comment your answer below.

**[11 · Outro]** Next time: setting up your computer and compiling properly. Keep coding, says Xecxec!

### Code shown

File 1: `hello.cpp` (scene 3, 5)

```cpp
#include <iostream>

int main() {
    std::cout << "Hello, Goa!" << std::endl;
    std::cout << "Keep coding, says Xecxec!" << std::endl;
    return 0;
}
```

**Expected output:**

```text
Hello, Goa!
Keep coding, says Xecxec!
```

### Bug of the Day

Wrong code (line 4 has no semicolon):

```cpp
#include <iostream>

int main() {
    std::cout << "Hello, Goa!" << std::endl
    return 0;
}
```

GCC output:

```text
hello.cpp: In function ‘int main()’:
hello.cpp:4:44: error: expected ‘;’ before ‘return’
    4 |     std::cout << "Hello, Goa!" << std::endl
      |                                            ^
      |                                            ;
    5 |     return 0;
      |     ~~~~~~
```

Fixed code (semicolon added):

```cpp
#include <iostream>

int main() {
    std::cout << "Hello, Goa!" << std::endl;
    return 0;
}
```

**Why:** g++ only notices a missing semicolon when it reaches the next statement, so the real mistake is usually on the line above the one it names.

### Pun & challenge

- **Pun:** "I told my compiler a joke. It said: expected ';' before 'laugh'."
- **Challenge:** Print your name on one line and your favourite beach on the next.
- **Challenge answer:** Use two cout lines, for example Atreya, then Palolem, each ending with std::endl.

### Shorts for EP 01

**S1 · The smallest C++ program** — 0:20 · built from scene 3

- **Hook (first 1.5s):** "Seven lines make a real program."
- **Script:** Seven lines make a real program. Three of them matter most: include, main and cout. Everything else in C plus plus is built on these three.
- **On-screen text:** THE SMALLEST C++ PROGRAM
- **Caption + hashtags:** Your first C++ program in 30 seconds. #cpp #learntocode #kodingkonkani #codingforbeginners #goa

**S2 · From code to program** — 0:22 · built from scene 4

- **Hook (first 1.5s):** "What does a compiler actually do?"
- **Script:** What does a compiler actually do? Your code goes in. The compiler checks every word. If all is fine, out comes a program you can run. If not, you get a line number. The compiler is your first teacher.
- **On-screen text:** CODE, COMPILER, PROGRAM
- **Caption + hashtags:** The compiler is your first teacher. #cpp #compiler #programming #kodingkonkani #learntocode

**S3 · What does cout do?** — 0:20 · built from scenes 3, 5

- **Hook (first 1.5s):** "Two little arrows, one big job."
- **Script:** Two little arrows, one big job. cout is the screen. The arrows push text towards it. Put words in quotes and they appear exactly as written. And endl moves to the next line.
- **On-screen text:** COUT: ARROWS TO THE SCREEN
- **Caption + hashtags:** cout explained slowly. #cpp #cout #helloworld #kodingkonkani #coding

**S4 · The missing semicolon** — 0:20 · built from scene 8

- **Hook (first 1.5s):** "One missing character, one angry compiler."
- **Script:** One missing character, one angry compiler. Remove a single semicolon and g plus plus says, expected semicolon before return. The error points at the next line, so always check the line above.
- **On-screen text:** EXPECTED ';' BEFORE 'RETURN'
- **Caption + hashtags:** Always check the line above. #cpp #bugfix #compilererror #kodingkonkani #coding

**S5 · Pun and challenge** — 0:20 · built from scenes 9, 10

- **Hook (first 1.5s):** "Can your compiler take a joke?"
- **Script:** Can your compiler take a joke? I told mine one and it said, expected semicolon before laugh. Your challenge: print your name, then your favourite beach. Full video: EP 1.
- **On-screen text:** PRINT YOUR NAME + YOUR BEACH
- **Caption + hashtags:** Try the challenge in the comments. #cpp #codingchallenge #kodingkonkani #programmingjokes #goa

## EP 02 — Setting up and compiling

**Module 0 · Welcome & setup · 5:34 · Peach + Tomato · Prerequisite: EP 01**

**Learning goals:** install a C++ compiler and check it with g++ --version; compile and run a program from the terminal; read the parts of a compile command: file name, -o and ./name.

### YouTube

- **Title:** Install C++ and Compile Your First File | C++ Programming EP 02
- **Description:** Set up g++ and VS Code on Windows, Mac or Linux, then compile and run a program with Xecxec. 0:00 Intro · 0:20 What you need · 1:05 Install g++ · 1:45 How g++ builds a file · 2:20 A program with numbers · 3:05 Compile and run · 3:30 Recap · 4:10 Bug of the Day · 4:59 Challenge · 5:19 Next episode
- **Tags:** install c++, g++, vs code c++, compile c++, c++ for beginners, koding konkani, mingw, c++ tutorial, class 11 computer science, coding in goa
- **Thumbnail:** big text "SET UP C++" in tomato on peach; Xecxec raising both claws beside a terminal showing g++ --version; thin black border and drop shadow.

### Scene list

| # | Start | Length | Template | On screen | Animation & SFX |
| --- | --- | --- | --- | --- | --- |
| 1 | 0:00 | 0:20 | Title card | EP 02 · SET UP AND COMPILE | Tomato title card: EP sticker thuds in, title stamps with a whoosh, Xecxec scuttles in and waves; thud, whoosh, claw-click, sting |
| 2 | 0:20 | 0:45 | Concept slide | "What you need": three numbered lines and a kitchen analogy card | Lines spring in one by one with a pop; the kitchen card slides in with a chopping board, a stove and a chef |
| 3 | 1:05 | 0:40 | Concept slide | Install steps for Windows, Mac and Linux, shown as three tabs | Three tabs (Windows, Mac, Linux) switch with a pop; the active steps tick in one by one |
| 4 | 1:45 | 0:35 | Concept slide | Three boxes: fish.cpp, g++, fish; the command written under the arrows | Three boxes appear; arrows draw on between them; the dash o part of the command glows tomato |
| 5 | 2:20 | 0:45 | Code explain | `fish.cpp`: two numbers, a label and a total | Same code; the output panel fills line by line with a ding per output line; [TRACK] cards update |
| 6 | 3:05 | 0:25 | Terminal | Terminal: `g++ fish.cpp -o fish`, then `./fish` | Dark-blue terminal: the command types with key-tick, output prints in mint with a ding |
| 7 | 3:30 | 0:40 | Concept slide | Recap: four steps on one card | Four recap lines tick in one by one with a pop; Xecxec nods after each tick |
| 8 | 4:10 | 0:40 | Bug of the Day | BUG OF THE DAY: no include line | Butter banner drops in with a buzzer; wrong code shakes; the g++ error lines appear in tomato; the fix slides in and the terminal turns mint with a ding |
| 9 | 4:50 | 0:09 | Pun card | Why did the programmer bring a ladder to the compiler? To reach the high-level language. | Full tomato screen, card flips in with a rimshot, Xecxec snaps his claw |
| 10 | 4:59 | 0:20 | Challenge | Task card: install, check, compile, change the price | Task card pops in; checklist ticks with a pop; Xecxec holds a tiny pen |
| 11 | 5:19 | 0:15 | Outro | Next: EP 03 · C vs C++: what changed | Next-episode card slides up with a whoosh; right side stays empty for end-screen elements; sign-off text types in |

### Narration script

**[1 · Title]** Welcome back! Last time we wrote a program. Today we set up your computer so you can run it yourself. It takes about ten minutes, and you only do it once.

**[2 · What you need]** You need three things. A compiler, which is g plus plus. An editor, where you type your code, like VS Code. And a terminal, where you give commands. Think of a kitchen. The compiler is the stove, the editor is the chopping board, and the terminal is you, giving the orders. Do not worry if the names sound strange. By the end of today, you will have typed every one of these commands yourself.

**[3 · Install g++]** First, install the compiler. On Windows, install MinGW-w64 through MSYS2, then add its bin folder to your path. On a Mac, open the terminal and type xcode-select dash dash install. On Linux, install g plus plus with your package manager, for example sudo apt install g plus plus. Then check it. Type g plus plus, space, dash dash version. If you see a version number, you are ready.

**[4 · How g++ builds a file]** Here is what g plus plus does. It reads fish dot cpp, checks it, and writes a new file, the program. The dash o part names that new file. Without it, you get a default name, and that is easy to forget. Run this same command again after every change you make to the file.

**[5 · A program with numbers]** [HL 4] [TRACK fish=3] Here we make a whole number called fish, and put three in it. [HL 5] [TRACK price=120] Another number called price, one hundred twenty. [HL 6] Print the label, then the value of fish. [HL 7] And here, C plus plus does the maths for us: fish times price. Three times one hundred twenty is three hundred sixty. Predict first: if we change the price to one hundred fifty, what should the total be? Four hundred fifty. Keep that in mind, it is today's challenge.

**[6 · Compile and run]** Save the file as fish dot cpp. Compile with g plus plus, fish dot cpp, dash o, fish. Then run it. On Mac and Linux, type dot slash fish. On Windows, type fish. Fish, three. Total, three hundred sixty.

**[7 · Recap]** Recap time. One: you need a compiler, an editor and a terminal. Two: check the compiler with g plus plus, dash dash version. Three: compile with g plus plus, the file name, dash o, and a name for the program. Four: run it with dot slash and that name. If any step fails, do not panic. Read the message, check the spelling, and try again. Every programmer does this, every single day.

**[8 · Bug of the Day]** Bug of the Day. We forgot the include line at the top. The compiler says, cout is not a member of std. Read the small note below it. It even tells you, did you forget to include iostream? Add the line back and it works.

**[9 · Pun]** Why did the programmer bring a ladder to the compiler? To reach the high-level language.

**[10 · Challenge]** Your challenge: install g plus plus, run g plus plus dash dash version, and compile fish dot cpp. Then change the price and run it again.

**[11 · Outro]** Next: how C plus plus is different from C. Keep coding, says Xecxec!

### Code shown

File 1: `fish.cpp` (scene 5)

```cpp
#include <iostream>

int main() {
    int fish = 3;
    int price = 120;
    std::cout << "Fish: " << fish << std::endl;
    std::cout << "Total: " << fish * price << std::endl;
    return 0;
}
```

**Expected output:**

```text
Fish: 3
Total: 360
```

### Bug of the Day

Wrong code (no #include line):

```cpp
int main() {
    int fish = 3;
    std::cout << "Fish: " << fish << std::endl;
    return 0;
}
```

GCC output:

```text
fish.cpp: In function ‘int main()’:
fish.cpp:3:10: error: ‘cout’ is not a member of ‘std’
    3 |     std::cout << "Fish: " << fish << std::endl;
      |          ^~~~
fish.cpp:1:1: note: ‘std::cout’ is defined in header ‘<iostream>’; did you forget to ‘#include <iostream>’?
  +++ |+#include <iostream>
    1 | int main() {
fish.cpp:3:43: error: ‘endl’ is not a member of ‘std’
```

Fixed code (include line added):

```cpp
#include <iostream>

int main() {
    int fish = 3;
    std::cout << "Fish: " << fish << std::endl;
    return 0;
}
```

**Why:** The compiler only knows the names you bring in. The note under the error says which header to include.

### Pun & challenge

- **Pun:** "Why did the programmer bring a ladder to the compiler? To reach the high-level language."
- **Challenge:** Install g++, check the version, compile fish.cpp, then change the price and run it again.
- **Challenge answer:** Change int price = 120; to int price = 150; and recompile: the total becomes 450.

### Shorts for EP 02

**S1 · What you need for C++** — 0:20 · built from scene 2

- **Hook (first 1.5s):** "Three tools, ten minutes."
- **Script:** Three tools, ten minutes. A compiler, an editor and a terminal. g plus plus is the stove, VS Code is the chopping board, and the terminal is you, giving the orders.
- **On-screen text:** 3 TOOLS FOR C++
- **Caption + hashtags:** Set up C++ in three steps. #cpp #setup #beginners #kodingkonkani #goa

**S2 · Check your compiler** — 0:20 · built from scene 3

- **Hook (first 1.5s):** "Is g++ really installed?"
- **Script:** Is g plus plus really installed? Open the terminal and type g plus plus, dash dash version. A version number means you are ready. An error means the install needs a second look.
- **On-screen text:** G++ --VERSION
- **Caption + hashtags:** One command to check your setup. #cpp #gpp #terminal #kodingkonkani #learntocode

**S3 · Decode the compile command** — 0:20 · built from scenes 4, 6

- **Hook (first 1.5s):** "g++ fish.cpp -o fish: what does it mean?"
- **Script:** g plus plus fish dot cpp dash o fish. What does it mean? g plus plus is the compiler. Fish dot cpp is your source. Dash o names the result. Then run it with dot slash fish.
- **On-screen text:** G++ FISH.CPP -O FISH
- **Caption + hashtags:** Decode the command. #cpp #compile #learncoding #kodingkonkani #terminal

**S4 · cout is not a member of std** — 0:20 · built from scene 8

- **Hook (first 1.5s):** "The line you always forget."
- **Script:** The line you always forget. Remove the include line and g plus plus says, cout is not a member of std. Then the note below tells you the fix. Always read the note.
- **On-screen text:** 'COUT' IS NOT A MEMBER OF 'STD'
- **Caption + hashtags:** Read the note under the error. #cpp #bugfix #iostream #kodingkonkani #compilererror

**S5 · Pun and challenge** — 0:20 · built from scenes 9, 10

- **Hook (first 1.5s):** "A ladder for the compiler?"
- **Script:** A ladder for the compiler? Why did the programmer bring one? To reach the high-level language. Your challenge: compile fish dot cpp, change the price, and run it again. Full video: EP 2.
- **On-screen text:** COMPILE FISH.CPP + CHANGE THE PRICE
- **Caption + hashtags:** Do the challenge. #cpp #codingchallenge #kodingkonkani #programmingjokes #goa

## EP 03 — C vs C++: what changed

**Module 0 · Welcome & setup · 5:11 · Peach + Tomato · Prerequisite: EP 02**

**Learning goals:** see how cout replaces printf and cin replaces scanf; understand using namespace std and what std:: means; know why C++ was built on top of C.

### YouTube

- **Title:** C vs C++: What Changed? | C++ Programming EP 03
- **Description:** Compare C and C++ side by side: printf versus cout, headers and namespaces, with Xecxec. 0:00 Intro · 0:15 Why C++ exists · 0:55 printf versus cout · 1:35 What is std? · 2:05 A full example · 2:45 Run it · 3:05 Recap · 3:45 Bug of the Day · 4:36 Challenge · 4:56 Next episode
- **Tags:** c vs c++, cout vs printf, namespace std, using namespace std, c++ for beginners, koding konkani, c++ tutorial, class 11 computer science, coding in goa, learn c++
- **Thumbnail:** big text "C vs C++" in tomato on peach; Xecxec shaking his shell between two code cards, C on the left and C++ on the right; thin black border and drop shadow.

### Scene list

| # | Start | Length | Template | On screen | Animation & SFX |
| --- | --- | --- | --- | --- | --- |
| 1 | 0:00 | 0:15 | Title card | EP 03 · C vs C++: WHAT CHANGED | Tomato title card: EP sticker thuds in, title stamps with a whoosh, Xecxec scuttles in and waves; thud, whoosh, claw-click, sting |
| 2 | 0:15 | 0:40 | Concept slide | "Why C++?": three numbered lines and a phone-and-newer-phone analogy card | Lines spring in with a pop; the analogy card slides in with two phones side by side |
| 3 | 0:55 | 0:40 | Concept slide | Two code panels side by side: C with printf on the left, C++ with cout on the right | Lines spring in one by one with a pop; the explanation card slides in from the right |
| 4 | 1:35 | 0:30 | Concept slide | A box labelled std holding cout, cin, endl and string; a second box labelled your code | The std box pops in with its four items; an arrow runs from your code to the box with a whoosh; the words using namespace std stamp across the arrow |
| 5 | 2:05 | 0:40 | Code explain | `age.cpp`: a number, a label and a calculation inside the line | Same code; the output panel fills line by line with a ding per output line; [TRACK] cards update |
| 6 | 2:45 | 0:20 | Terminal | Terminal: `g++ age.cpp -o age`, then `./age` | Dark-blue terminal: the command types with key-tick, output prints in mint with a ding |
| 7 | 3:05 | 0:40 | Concept slide | Recap: four ideas on one card | Four recap lines tick in one by one with a pop; Xecxec nods after each tick |
| 8 | 3:45 | 0:40 | Bug of the Day | BUG OF THE DAY: cout without using namespace std | Butter banner drops in with a buzzer; wrong code shakes; the g++ error lines appear in tomato; the fix slides in and the terminal turns mint with a ding |
| 9 | 4:25 | 0:11 | Pun card | C++ is just C with a bigger toolbox, and a lot more places to drop a screw. | Full tomato screen, card flips in with a rimshot, Xecxec snaps his claw |
| 10 | 4:36 | 0:20 | Challenge | Task card: print your age now and in ten years | Task card pops in; checklist ticks with a pop; Xecxec holds a tiny pen |
| 11 | 4:56 | 0:15 | Outro | Next: EP 04 · Anatomy of a C++ program | Next-episode card slides up with a whoosh; right side stays empty for end-screen elements; sign-off text types in |

### Narration script

**[1 · Title]** If you watched our C course, welcome back. If not, welcome anyway. Today we see what C plus plus changed, and why.

**[2 · Why C++ exists]** C plus plus began as C with extras. Almost everything you know from C still works. But C plus plus adds friendlier tools, like safer text, and ways to organise big programs. Think of a phone and its newer model. Same calls, same texts, but more things you can do. C plus plus was created in the early nineteen eighties, and it is still used today for games, browsers and banking systems.

**[3 · printf versus cout]** On the left, C prints with printf and a format code. On the right, C plus plus uses cout. You do not need a format code. The value just goes in, and the arrows push it to the screen. And for input, C used scanf, and C plus plus uses cin, with the arrows pointing the other way.

**[4 · What is std?]** Where do cout and endl live? In a box called std, short for standard. To use them you write std colon colon cout. Or you say once, at the top, using namespace std, and the box is opened for the whole file. Just remember: std is a box, and the using line opens it.

**[5 · A full example]** [HL 2] This line opens the std box. [HL 5] [TRACK age=17] Make a number called age, with seventeen. [HL 6] Print the label and the age. See how easy it is to mix text and numbers. [HL 7] And we can calculate inside the line. Age plus one is eighteen. Predict first: with age seventeen, what does the second line print? Eighteen. The calculation happens first, and then the result is printed.

**[6 · Run it]** Compile and run. Age, seventeen. Next year, eighteen. No format codes, and no mistakes with percent d.

**[7 · Recap]** Recap. One: C plus plus keeps almost everything from C, and adds friendlier tools. Two: cout replaces printf, and cin replaces scanf, with arrows pointing the way. Three: cout and cin live in the std box, so write std colon colon, or say using namespace std once at the top. Four: you can mix text and numbers in one line. That is a lot already. Well done.

**[8 · Bug of the Day]** Bug of the Day. We use cout, but we forgot using namespace std. The compiler says, cout was not declared in this scope. Did you mean std colon colon cout? Yes! Add the using line, or write std colon colon in front.

**[9 · Pun]** C plus plus is just C with a bigger toolbox, and a lot more places to drop a screw.

**[10 · Challenge]** Your challenge: a program with a number called age. Print your age now, and your age in ten years.

**[11 · Outro]** Next: the anatomy of a C plus plus program. Keep coding, says Xecxec!

### Code shown

File 1: `age.cpp` (scene 5)

```cpp
#include <iostream>
using namespace std;

int main() {
    int age = 17;
    cout << "Age: " << age << endl;
    cout << "Next year: " << age + 1 << endl;
    return 0;
}
```

**Expected output:**

```text
Age: 17
Next year: 18
```

### Bug of the Day

Wrong code (cout used without std):

```cpp
#include <iostream>

int main() {
    int age = 17;
    cout << "Age: " << age << endl;
    return 0;
}
```

GCC output:

```text
age.cpp: In function ‘int main()’:
age.cpp:5:5: error: ‘cout’ was not declared in this scope; did you mean ‘std::cout’?
    5 |     cout << "Age: " << age << endl;
      |     ^~~~
      |     std::cout
In file included from age.cpp:1:
/usr/include/c++/13/iostream:63:18: note: ‘std::cout’ declared here
   63 |   extern ostream cout;          ///< Linked to standard output
```

Fixed code (using namespace std added):

```cpp
#include <iostream>
using namespace std;

int main() {
    int age = 17;
    cout << "Age: " << age << endl;
    return 0;
}
```

**Why:** Names from the standard library live in the std box, so you either write std:: in front or open the box once with using namespace std.

### Pun & challenge

- **Pun:** "C++ is just C with a bigger toolbox, and a lot more places to drop a screw."
- **Challenge:** Print your age now and your age in ten years.
- **Challenge answer:** Make int age = 17; then print age and age + 10 with cout.

### Shorts for EP 03

**S1 · printf versus cout** — 0:20 · built from scene 3

- **Hook (first 1.5s):** "No more percent d."
- **Script:** No more percent d. In C you write printf with a format code. In C plus plus you push the value into cout with arrows. Fewer codes, fewer mistakes.
- **On-screen text:** PRINTF VS COUT
- **Caption + hashtags:** printf versus cout in 30 seconds. #cpp #cprogramming #beginners #kodingkonkani #learntocode

**S2 · What is std?** — 0:20 · built from scene 4

- **Hook (first 1.5s):** "A box that holds cout."
- **Script:** A box that holds cout. std is the standard box. cout, cin and endl live inside it. Write std colon colon cout, or open the box once with using namespace std.
- **On-screen text:** WHAT IS STD?
- **Caption + hashtags:** std explained. #cpp #namespace #std #kodingkonkani #coding

**S3 · Mix text and numbers** — 0:20 · built from scene 5

- **Hook (first 1.5s):** "One line, text and a number."
- **Script:** One line, text and a number. cout, arrows, a label, an arrow, the age. Arrows can be chained, and each arrow pushes one thing to the screen.
- **On-screen text:** COUT << "AGE: " << AGE
- **Caption + hashtags:** Chain your arrows. #cpp #cout #coding #kodingkonkani #beginners

**S4 · cout was not declared** — 0:20 · built from scene 8

- **Hook (first 1.5s):** "The did-you-mean that saves you."
- **Script:** The did-you-mean that saves you. Forget using namespace std and g plus plus says, cout was not declared. Then it suggests std colon colon cout. Read the suggestion.
- **On-screen text:** 'COUT' WAS NOT DECLARED
- **Caption + hashtags:** Read the suggestion! #cpp #bugfix #compiler #kodingkonkani #coding

**S5 · Pun and challenge** — 0:21 · built from scenes 9, 10

- **Hook (first 1.5s):** "A screw in the toolbox?"
- **Script:** A screw in the toolbox? C plus plus is just C with a bigger toolbox, and a lot more places to drop a screw. Your challenge: print your age now and in ten years. Full video: EP 3.
- **On-screen text:** AGE NOW + AGE IN 10 YEARS
- **Caption + hashtags:** Comment your answer. #cpp #challenge #kodingkonkani #programmingjokes #goa

## EP 04 — Anatomy of a C++ program

**Module 0 · Welcome & setup · 5:09 · Peach + Tomato · Prerequisite: EP 03**

**Learning goals:** name the parts: include, main, statements, braces, comments and return 0; write a single-line comment with //; recognise a missing closing brace error.

### YouTube

- **Title:** Anatomy of a C++ Program | C++ Programming EP 04
- **Description:** Take a C++ program apart piece by piece: main, braces, statements and comments, with Xecxec. 0:00 Intro · 0:15 The parts · 0:55 Walk through the code · 1:35 Numbers in memory · 2:05 Comments · 2:45 Run it · 3:05 Recap · 3:45 Bug of the Day · 4:34 Challenge · 4:54 Next module
- **Tags:** c++ program structure, main function, comments in c++, braces, c++ for beginners, koding konkani, c++ tutorial, class 11 computer science, coding in goa, learn c++
- **Thumbnail:** big text "ANATOMY OF A PROGRAM" in tomato on peach; Xecxec holding a magnifying glass over a code card with coloured labels; thin black border and drop shadow.

### Scene list

| # | Start | Length | Template | On screen | Animation & SFX |
| --- | --- | --- | --- | --- | --- |
| 1 | 0:00 | 0:15 | Title card | EP 04 · ANATOMY OF A PROGRAM | Tomato title card: EP sticker thuds in, title stamps with a whoosh, Xecxec scuttles in and waves; thud, whoosh, claw-click, sting |
| 2 | 0:15 | 0:40 | Concept slide | "The parts": three numbered lines and a bus-route analogy card | Lines spring in with a pop; the bus-route card slides in with three stops |
| 3 | 0:55 | 0:40 | Code explain | `shacks.cpp`: a 12-line program with coloured labels on each part | Code types in with key-tick; butter [HL n] highlight sweeps line by line with marker-swipe; explanation card on the right |
| 4 | 1:35 | 0:30 | Memory boxes | Two memory boxes: shacks = 12 and open_now = 9, and a printed result Closed: 3 | Two labelled boxes pop in with their values and addresses; a subtraction arrow draws on and the result 3 is printed, not stored; pop per box |
| 5 | 2:05 | 0:40 | Code explain | `shacks.cpp` again; the comment line glows and the output panel fills | Same code; the output panel fills line by line with a ding per output line; [TRACK] cards update |
| 6 | 2:45 | 0:20 | Terminal | Terminal: `g++ shacks.cpp -o shacks`, then `./shacks` | Dark-blue terminal: the command types with key-tick, output prints in mint with a ding |
| 7 | 3:05 | 0:40 | Concept slide | Recap: four rules on one card | Four recap lines tick in one by one with a pop; Xecxec nods after each tick |
| 8 | 3:45 | 0:40 | Bug of the Day | BUG OF THE DAY: a missing closing brace | Butter banner drops in with a buzzer; wrong code shakes; the g++ error lines appear in tomato; the fix slides in and the terminal turns mint with a ding |
| 9 | 4:25 | 0:09 | Pun card | Why did the brace feel lonely? Its partner never showed up at end of input. | Full tomato screen, card flips in with a rimshot, Xecxec snaps his claw |
| 10 | 4:34 | 0:20 | Challenge | Task card: boys plus girls, print the total | Task card pops in; checklist ticks with a pop; Xecxec holds a tiny pen |
| 11 | 4:54 | 0:15 | Outro | Next: Module 1 · Variables and types | Next-episode card slides up with a whoosh; right side stays empty for end-screen elements; sign-off text types in |

### Narration script

**[1 · Title]** Today we open up a C plus plus program and name every part, like a biology class, but nobody gets hurt.

**[2 · The parts]** A program is like a bus route. It has a starting stop, which is main. Then it visits stops in order, which are statements. Each statement ends with a semicolon, like a ticket stamp. And the route ends with return zero. Every program you will ever write, from a tiny calculator to a banking app, follows this same route.

**[3 · Walk through the code]** [HL 1] Include brings in a toolbox. [HL 2] Using namespace std opens the std box. [HL 5] Main is where the bus starts. The curly brace after it opens the body. [HL 6] The body holds our statements. Each one ends with a semicolon. [HL 11] Return zero means, finished, no problems. [HL 12] And the last curly brace closes main.

**[4 · Numbers in memory]** Our program keeps two numbers in memory. Shacks holds twelve. Open now holds nine. When we calculate shacks minus open now, the answer, three, is not stored anywhere. It is printed straight away. Each box has a name, a value and an address, like a house number on a street in Panaji.

**[5 · Comments]** [HL 4] This line starts with two slashes. That is a comment. The compiler ignores it, but humans love it. [HL 6] [TRACK shacks=12] Twelve shacks on the beach. [HL 7] [TRACK open_now=9] Nine are open. [HL 10] Closed is twelve minus nine, which is three. Use comments to explain why, not what. Predict before you run: the closed line prints twelve minus nine. Three. Always predict first.

**[6 · Run it]** Compile it and run. Shacks, twelve. Open, nine. Closed, three. The comment is nowhere in the output, because the compiler threw it away.

**[7 · Recap]** Recap. One: a program starts at main and ends at return zero. Two: every statement ends with a semicolon. Three: curly braces come in pairs, one to open and one to close. Four: a comment starts with two slashes, and the compiler ignores it. Say these four rules out loud, and you can read any beginner program. Try it on the shacks program, line by line.

**[8 · Bug of the Day]** Bug of the Day. We forgot the closing curly brace at the end. The compiler says, expected closing brace at end of input. And a note says, to match this opening brace. Always count your braces. Open, close, open, close.

**[9 · Pun]** Why did the brace feel lonely? Its partner never showed up at end of input.

**[10 · Challenge]** Your challenge: write a program with a comment, two numbers called boys and girls in your class, and print the total.

**[11 · Outro]** Module zero is done! Next: variables and types. Keep coding, says Xecxec!

### Code shown

File 1: `shacks.cpp` (scene 3, 5)

```cpp
#include <iostream>
using namespace std;

// Xecxec counts the beach shacks
int main() {
    int shacks = 12;
    int open_now = 9;
    cout << "Shacks: " << shacks << endl;
    cout << "Open: " << open_now << endl;
    cout << "Closed: " << shacks - open_now << endl;
    return 0;
}
```

**Expected output:**

```text
Shacks: 12
Open: 9
Closed: 3
```

### Bug of the Day

Wrong code (the closing brace of main is missing):

```cpp
#include <iostream>
using namespace std;

int main() {
    int shacks = 12;
    cout << "Shacks: " << shacks << endl;
    return 0;
```

GCC output:

```text
shacks.cpp: In function ‘int main()’:
shacks.cpp:7:14: error: expected ‘}’ at end of input
    7 |     return 0;
      |              ^
shacks.cpp:4:12: note: to match this ‘{’
    4 | int main() {
      |            ^
```

Fixed code (closing brace added):

```cpp
#include <iostream>
using namespace std;

int main() {
    int shacks = 12;
    cout << "Shacks: " << shacks << endl;
    return 0;
}
```

**Why:** Every opening brace needs a matching closing brace. The note under the error shows which opening brace is still waiting.

### Pun & challenge

- **Pun:** "Why did the brace feel lonely? Its partner never showed up at end of input."
- **Challenge:** Write a program with a comment, two numbers (boys and girls) and print the total.
- **Challenge answer:** Use int boys = 20; and int girls = 18; then print boys + girls, which gives 38.

### Shorts for EP 04

**S1 · A program is a bus route** — 0:20 · built from scene 2

- **Hook (first 1.5s):** "Start at main, stop at return."
- **Script:** Start at main, stop at return. Every program begins at main, visits each statement in order, and ends at return zero. Like a bus route through Panaji.
- **On-screen text:** A PROGRAM IS A BUS ROUTE
- **Caption + hashtags:** Think of a bus route. #cpp #programming #beginners #kodingkonkani #goa

**S2 · Name every part** — 0:20 · built from scene 3

- **Hook (first 1.5s):** "Twelve lines, five parts."
- **Script:** Twelve lines, five parts. Include, using, main, statements and return. Coloured labels point at each part, so you never have to guess again.
- **On-screen text:** 12 LINES, 5 PARTS
- **Caption + hashtags:** Label the code. #cpp #structure #learntocode #kodingkonkani #coding

**S3 · Comments** — 0:20 · built from scene 5

- **Hook (first 1.5s):** "The line the compiler ignores."
- **Script:** The line the compiler ignores. Two slashes make a comment. The compiler skips it, but humans read it. Explain why you did something, not what the code does.
- **On-screen text:** // COMMENTS
- **Caption + hashtags:** Comment your code. #cpp #comments #coding #kodingkonkani #beginners

**S4 · Expected } at end of input** — 0:20 · built from scene 8

- **Hook (first 1.5s):** "Count your braces."
- **Script:** Count your braces. A missing closing brace gives, expected closing brace at end of input. And a note shows which opening brace is still waiting.
- **On-screen text:** EXPECTED '}' AT END OF INPUT
- **Caption + hashtags:** Open, close, open, close. #cpp #bugfix #braces #kodingkonkani #compilererror

**S5 · Pun and challenge** — 0:20 · built from scenes 9, 10

- **Hook (first 1.5s):** "A lonely brace."
- **Script:** A lonely brace. Why did the brace feel lonely? Its partner never showed up at end of input. Your challenge: boys plus girls, print the total. Full video: EP 4.
- **On-screen text:** BOYS + GIRLS = ?
- **Caption + hashtags:** Try it! #cpp #challenge #kodingkonkani #programmingjokes #goa
