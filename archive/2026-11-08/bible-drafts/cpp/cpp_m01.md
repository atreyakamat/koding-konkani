# Module 1 — Variables and types

Episodes 5–12 · Pastel Blue + Tomato · g++ 13.3, -std=c++17 -Wall -Wextra

## EP 05 — Variables and types

**Module 1 · Variables and types · 5:37 · Pastel Blue + Tomato · Prerequisite: EP 04**

**Learning goals:** create variables of type int, double, char and bool; pick the right type for a value; always give a variable a starting value.

### YouTube

- **Title:** Variables and Types in C++: int, double, char, bool | C++ Programming EP 05
- **Description:** Learn how C++ stores whole numbers, decimals, letters and true or false values in variables, with Xecxec the crab. 0:00 Intro · 0:25 Boxes with types · 1:10 Declaring variables · 1:50 Variables in memory · 2:25 Run it in your head · 3:05 Compile and run · 3:25 Recap · 4:05 Bug of the Day · 5:02 Challenge · 5:22 Next episode
- **Tags:** c++ variables, c++ data types, int double char bool, c++ for beginners, koding konkani, c++ tutorial, uninitialized variable, class 11 computer science, first year engineering, coding in goa
- **Thumbnail:** big text "VARIABLES + TYPES" in tomato on pastel blue; Xecxec holding four labelled boxes marked int, double, char and bool; thin black border and drop shadow.

### Scene list

| # | Start | Length | Template | On screen | Animation & SFX |
| --- | --- | --- | --- | --- | --- |
| 1 | 0:00 | 0:25 | Title card | EP 05 · VARIABLES AND TYPES | Tomato title card: EP sticker thuds in, title stamps with a whoosh, Xecxec scuttles in and waves; thud, whoosh, claw-click, sting |
| 2 | 0:25 | 0:45 | Concept slide | "Boxes with types": four numbered lines (int, double, char, bool) and a fridge-shelves analogy card | Four lines spring in one by one with a pop; the fridge card slides in with a bottle shelf, an ice tray and a lemon drawer |
| 3 | 1:10 | 0:40 | Code explain | `vars.cpp`: four variables, each line shows type, name and value | Code types in with key-tick; butter [HL n] highlight sweeps line by line with marker-swipe; explanation card on the right |
| 4 | 1:50 | 0:35 | Memory boxes | Four memory boxes: fish = 3, price = 120.5, grade = 'A', open_now = true, each with a size and an address | Four labelled boxes pop in one by one, each with its value, its size in bytes and an address tag; boxes differ in width to show their sizes; pop per box |
| 5 | 2:25 | 0:40 | Code explain | `vars.cpp` again, with the output panel on the right | Same code; the output panel fills line by line with a ding per output line; [TRACK] cards update |
| 6 | 3:05 | 0:20 | Terminal | Terminal: `g++ vars.cpp -o vars`, then `./vars` | Dark-blue terminal: the command types with key-tick, output prints in mint with a ding |
| 7 | 3:25 | 0:40 | Concept slide | Recap: four ideas on one card | Four recap lines tick in one by one with a pop; Xecxec nods after each tick |
| 8 | 4:05 | 0:45 | Bug of the Day | BUG OF THE DAY: a variable with no starting value | Butter banner drops in with a buzzer; the g++ warning appears in tomato, then the program runs and prints the wrong result; the fix slides in and the output turns mint with a ding |
| 9 | 4:50 | 0:12 | Pun card | An uninitialised variable walks into a bar. The bartender asks, what will you have? It says: whatever was there before. | Full tomato screen, card flips in with a rimshot, Xecxec snaps his claw |
| 10 | 5:02 | 0:20 | Challenge | Task card: four variables, four types | Task card pops in; checklist ticks with a pop; Xecxec holds a tiny pen |
| 11 | 5:22 | 0:15 | Outro | Next: EP 06 · Reading input with cin | Next-episode card slides up with a whoosh; right side stays empty for end-screen elements; sign-off text types in |

### Narration script

**[1 · Title]** Welcome back! So far our programs only printed words. Today they learn to remember things. A variable is a little labelled box, and C plus plus has a different kind of box for every kind of data.

**[2 · Boxes with types]** A variable is a named box in memory. Every box has a type, and the type says what can go inside. Int holds whole numbers, like three fish. Double holds numbers with a decimal point, like one hundred twenty point five. Char holds one single character, written in single quotes. And bool holds only true or false. Think of a beach shack fridge. One shelf for bottles, one tray for ice. Each place is shaped for one job.

**[3 · Declaring variables]** [HL 5] Int fish equals three. First the type, then the name, then the value. [HL 6] Double price equals one hundred twenty point five. [HL 7] Char grade equals A. Notice the single quotes around the letter. [HL 8] And bool open now equals true. [HL 9] Now we print each one. The names have no quotes, so cout prints the value stored inside, not the word itself.

**[4 · Variables in memory]** Here is what memory looks like. Each variable is a box with a name, a value and an address. On most computers, an int takes four bytes, so fish needs four. A double is bigger, eight bytes. A char takes one byte, and so does a bool. Different types, different sizes. The address tells the computer where on the street each box lives.

**[5 · Run it in your head]** [HL 5] [TRACK fish=3] Fish holds three. [HL 6] [TRACK price=120.5] Price holds one hundred twenty point five. [HL 7] [TRACK grade=A] Grade holds A. [HL 8] [TRACK open_now=true] Open now holds true. [HL 12] Look at the last output line. A bool prints as one for true, and zero for false. So the screen says, Open, one.

**[6 · Compile and run]** Compile with g plus plus, vars dot cpp, dash o, vars. Then run it. Fish, three. Price, one hundred twenty point five. Grade, A. Open, one. Each value comes out in the shape of its type.

**[7 · Recap]** Recap. One: a variable is a named box in memory. Two: every box has a type. Int for whole numbers, double for decimals, char for one letter, bool for true or false. Three: a bool prints as one or zero. Four: always give a variable a starting value when you make it. Say these four out loud, then change the grade to B and run the program again.

**[8 · Bug of the Day]** Bug of the Day. Here we make an int called packets, but we never give it a value. The compiler warns us: packets is used uninitialized. It is only a warning, so the program still runs, and prints a strange number. Run it again and the number may change. That is garbage left behind in memory. Give every variable a value when you make it. With equals zero, the output is a clean zero.

**[9 · Pun]** An uninitialised variable walks into a bar. The bartender asks, what will you have? It says, whatever was there before.

**[10 · Challenge]** Your challenge: make four variables. Your age, your height in metres, your first initial, and whether you like fish. Print all four. Comment your answer below.

**[11 · Outro]** Next time: reading input with cin, so your program can ask a question and listen. Keep coding, says Xecxec!

### Code shown

File 1: `vars.cpp` (scene 3, 5)

```cpp
#include <iostream>
using namespace std;

int main() {
    int fish = 3;
    double price = 120.5;
    char grade = 'A';
    bool open_now = true;
    cout << "Fish: " << fish << endl;
    cout << "Price: " << price << endl;
    cout << "Grade: " << grade << endl;
    cout << "Open: " << open_now << endl;
    return 0;
}
```

**Expected output:**

```text
Fish: 3
Price: 120.5
Grade: A
Open: 1
```

### Bug of the Day

Wrong code (packets is never given a value):

```cpp
#include <iostream>
using namespace std;

int main() {
    int packets;
    cout << "Packets: " << packets << endl;
    return 0;
}
```

GCC and program output:

```text
packets.cpp: In function ‘int main()’:
packets.cpp:6:28: warning: ‘packets’ is used uninitialized [-Wuninitialized]
    6 |     cout << "Packets: " << packets << endl;
      |                            ^~~~~~~
packets.cpp:5:9: note: ‘packets’ was declared here
    5 |     int packets;
      |         ^~~~~~~
Output when run:
Packets: 32764
```

Fixed code (starting value added):

```cpp
#include <iostream>
using namespace std;

int main() {
    int packets = 0;
    cout << "Packets: " << packets << endl;
    return 0;
}
```

Output of the fixed code:

```text
Packets: 0
```

**Why:** A variable you do not set holds whatever was left in that memory before, so always write int packets = 0; or another starting value.

### Pun & challenge

- **Pun:** "An uninitialised variable walks into a bar. The bartender asks, what will you have? It says: whatever was there before."
- **Challenge:** Make four variables: your age, your height in metres, your first initial and whether you like fish. Print all four.
- **Challenge answer:** Use int, double, char and bool, for example 17, 1.65, 'A' and true; the bool prints as 1.

### Shorts for EP 05

**S1 · Four boxes, four types** — 0:20 · built from scene 2

- **Hook (first 1.5s):** "Four boxes for four kinds of data."
- **Script:** Four boxes for four kinds of data. Int for whole numbers. Double for decimals. Char for one letter in single quotes. Bool for true or false. Pick the box that fits the value.
- **On-screen text:** INT, DOUBLE, CHAR, BOOL
- **Caption + hashtags:** Four types in 30 seconds. #cpp #datatypes #beginners #kodingkonkani #learntocode

**S2 · Declaring a variable** — 0:20 · built from scene 3

- **Hook (first 1.5s):** "Type, name, value: three words."
- **Script:** Type, name, value: three words make a variable. Int fish equals three. Double price equals one hundred twenty point five. Char grade equals A, with single quotes around the letter.
- **On-screen text:** TYPE + NAME = VALUE
- **Caption + hashtags:** Declare a variable. #cpp #variables #coding #kodingkonkani #beginners

**S3 · Boxes in memory** — 0:20 · built from scene 4

- **Hook (first 1.5s):** "Every variable has an address."
- **Script:** Every variable has an address. Each box has a name, a value, a size and an address. On most computers an int takes four bytes, a double takes eight, and a char takes one.
- **On-screen text:** NAME, VALUE, SIZE, ADDRESS
- **Caption + hashtags:** Memory is a street of boxes. #cpp #memory #programming #kodingkonkani #learntocode

**S4 · Used uninitialized** — 0:20 · built from scene 8

- **Hook (first 1.5s):** "The variable you forgot to set."
- **Script:** The variable you forgot to set. Make an int and never give it a value, and g plus plus warns, used uninitialized. The program still runs and prints garbage. Always set a starting value.
- **On-screen text:** 'PACKETS' IS USED UNINITIALIZED
- **Caption + hashtags:** Always give a starting value. #cpp #bugfix #uninitialized #kodingkonkani #compilerwarning

**S5 · Pun and challenge** — 0:20 · built from scenes 9, 10

- **Hook (first 1.5s):** "A variable walks into a bar."
- **Script:** A variable walks into a bar. The bartender asks what it will have. Whatever was there before. Your challenge: make four variables and print them all. Full video: EP 5.
- **On-screen text:** 4 VARIABLES, 4 TYPES
- **Caption + hashtags:** Try the challenge in the comments. #cpp #codingchallenge #kodingkonkani #programmingjokes #goa

## EP 06 — Reading input with cin

**Module 1 · Variables and types · 5:12 · Pastel Blue + Tomato · Prerequisite: EP 05**

**Learning goals:** read numbers and words with cin >>; read a whole line with getline; know that cin >> stops at the first space.

### YouTube

- **Title:** Reading Input with cin and getline in C++ | C++ Programming EP 06
- **Description:** Make your C++ program ask questions and listen: cin, getline and why cin stops at a space, with Xecxec. 0:00 Intro · 0:15 How input works · 0:55 cin and getline · 1:35 Where the input goes · 2:10 Run it in your head · 2:50 Compile and run · 3:10 Recap · 3:50 Bug of the Day · 4:37 Challenge · 4:57 Next episode
- **Tags:** c++ cin, c++ getline, c++ input, cin vs getline, c++ for beginners, koding konkani, c++ tutorial, class 11 computer science, first year engineering, coding in goa
- **Thumbnail:** big text "READ INPUT: CIN" in tomato on pastel blue; Xecxec with a claw cupped to an ear beside a speech bubble reading cin >> name; thin black border and drop shadow.

### Scene list

| # | Start | Length | Template | On screen | Animation & SFX |
| --- | --- | --- | --- | --- | --- |
| 1 | 0:00 | 0:15 | Title card | EP 06 · READING INPUT WITH CIN | Tomato title card: EP sticker thuds in, title stamps with a whoosh, Xecxec scuttles in and waves; thud, whoosh, claw-click, sting |
| 2 | 0:15 | 0:40 | Concept slide | "How input works": three numbered lines and a waiter-taking-an-order analogy card | Lines spring in with a pop; the waiter card slides in with a notepad and a pencil |
| 3 | 0:55 | 0:40 | Code explain | `greet.cpp`: two variables, a prompt, then cin and getline | Code types in with key-tick; butter [HL n] highlight sweeps line by line with marker-swipe; explanation card on the right |
| 4 | 1:35 | 0:35 | Memory boxes | Three memory boxes: name = Priya, age = 17, city = Old Goa, with the typed line shown above them | The typed line Priya 17 Old Goa appears; a bracket slides over each piece in turn and drops it into its box; the boxes fill with a pop, the last one taking two words |
| 5 | 2:10 | 0:40 | Code explain | `greet.cpp` again, with the typed input and the output panel on the right | Same code; the output panel fills line by line with a ding per output line; [TRACK] cards update |
| 6 | 2:50 | 0:20 | Terminal | Terminal: `g++ greet.cpp -o greet`, then `./greet`, then the typed line | Dark-blue terminal: the command types with key-tick, output prints in mint with a ding |
| 7 | 3:10 | 0:40 | Concept slide | Recap: four rules on one card | Four recap lines tick in one by one with a pop; Xecxec nods after each tick |
| 8 | 3:50 | 0:40 | Bug of the Day | BUG OF THE DAY: cin stops at the first space | Butter banner drops in with a buzzer; the program compiles and runs; the wrong output appears in tomato; the fix slides in and the output turns mint with a ding |
| 9 | 4:30 | 0:07 | Pun card | Why is cin so polite? It stops listening at the first space. | Full tomato screen, card flips in with a rimshot, Xecxec snaps his claw |
| 10 | 4:37 | 0:20 | Challenge | Task card: name, then favourite beach | Task card pops in; checklist ticks with a pop; Xecxec holds a tiny pen |
| 11 | 4:57 | 0:15 | Outro | Next: EP 07 · Operators and expressions | Next-episode card slides up with a whoosh; right side stays empty for end-screen elements; sign-off text types in |

### Narration script

**[1 · Title]** Until now our programs only talked. Today they listen. We will ask the user a question and read the answer, using cin and getline.

**[2 · How input works]** Reading input is the opposite of printing. With cout, the arrows point at the screen. With cin, the arrows point at a variable, because the typed value flows into it. Cin reads one word at a time, and it stops at any space. When you want a whole line, with spaces, use getline. Think of a waiter. Cin writes down one item at a time. Getline writes down the whole order.

**[3 · cin and getline]** [HL 6] We make two strings, name and city. [HL 7] And a whole number, age. [HL 8] The prompt asks for all three. [HL 9] Cin pushes the first word into name, and the next word into age. [HL 10] Cin ws skips the leftover spaces. [HL 11] Then getline reads everything left on the line, spaces and all, into city. [HL 12] Finally, we greet the user.

**[4 · Where the input goes]** Watch where each piece goes. The user types one line: Priya, seventeen, Old Goa. Cin takes the first word, Priya, and drops it in the name box. It takes the next, seventeen, and drops it in the age box. Then getline grabs the rest of the line, Old Goa, with the space inside, and drops it in the city box.

**[5 · Run it in your head]** [HL 9] [TRACK name=Priya] Name becomes Priya. [TRACK age=17] Age becomes seventeen. [HL 11] [TRACK city=Old Goa] City becomes Old Goa. [HL 12] The first message prints Hello, Priya, from Old Goa. [HL 13] The second adds one to age, so it says eighteen.

**[6 · Compile and run]** Compile it and run it. The prompt appears. Type Priya, seventeen, Old Goa, and press enter. Hello, Priya, from Old Goa. Next year you will be eighteen. Your program just listened.

**[7 · Recap]** Recap. One: with cin, the arrows point at the variable that receives the value. Two: cin reads one word or number at a time, and stops at any space. Three: getline reads the whole line, spaces included. Four: after cin, use cin ws to skip leftover spaces before getline. Try typing your own name and city into the greeting program, and watch each piece land in its box.

**[8 · Bug of the Day]** Bug of the Day. We ask for a full name, and the user types Priya Naik. But the program says, Hello, Priya. Where did Naik go? There is no error, because cin did exactly what it should. It stopped at the first space. The second word waits in the input, and nobody reads it. Use getline instead, and the whole name arrives.

**[9 · Pun]** Why is cin so polite? It stops listening at the first space.

**[10 · Challenge]** Your challenge: read a first name with cin, then a favourite beach with getline, and greet the user using both. Comment your answer below.

**[11 · Outro]** Next time: operators, and how C plus plus does arithmetic. Keep coding, says Xecxec!

### Code shown

File 1: `greet.cpp` (scene 3, 5)

```cpp
#include <iostream>
#include <string>
using namespace std;

int main() {
    string name, city;
    int age;
    cout << "Name, age, city? ";
    cin >> name >> age;
    cin >> ws;
    getline(cin, city);
    cout << "Hello, " << name << " from " << city << "!" << endl;
    cout << "Next year you will be " << age + 1 << "." << endl;
    return 0;
}
```

Run with input: Priya 17 Old Goa

**Expected output:**

```text
Name, age, city? Hello, Priya from Old Goa!
Next year you will be 18.
```

### Bug of the Day

Wrong code (cin >> reads only up to the first space):

```cpp
#include <iostream>
#include <string>
using namespace std;

int main() {
    string full_name;
    cout << "Full name? ";
    cin >> full_name;
    cout << "Hello, " << full_name << "!" << endl;
    return 0;
}
```

GCC and program output:

```text
Input: Priya Naik
Output when run:
Full name? Hello, Priya!
```

Fixed code (getline reads the whole line):

```cpp
#include <iostream>
#include <string>
using namespace std;

int main() {
    string full_name;
    cout << "Full name? ";
    getline(cin, full_name);
    cout << "Hello, " << full_name << "!" << endl;
    return 0;
}
```

Output of the fixed code:

```text
Full name? Hello, Priya Naik!
```

**Why:** The >> operator stops at whitespace, so use getline(cin, variable) when the input can contain spaces.

### Pun & challenge

- **Pun:** "Why is cin so polite? It stops listening at the first space."
- **Challenge:** Read a first name with cin, then a favourite beach with getline, and greet the user with both.
- **Challenge answer:** Use cin >> name >> ws; then getline(cin, beach); and print both in one greeting.

### Shorts for EP 06

**S1 · cout versus cin** — 0:20 · built from scene 2

- **Hook (first 1.5s):** "Arrows that point at a variable."
- **Script:** Arrows that point at a variable. With cout, the arrows point at the screen. With cin, they point the other way, into your variable. Type a value, and it flows in.
- **On-screen text:** COUT >> SCREEN, CIN >> VARIABLE
- **Caption + hashtags:** Which way do the arrows point? #cpp #cin #beginners #kodingkonkani #learntocode

**S2 · cin then getline** — 0:20 · built from scene 3

- **Hook (first 1.5s):** "One line, three kinds of reading."
- **Script:** One line, three kinds of reading. Cin takes a word. Cin takes a number. Then getline takes the rest of the line, spaces and all. Skip leftover spaces first with cin ws.
- **On-screen text:** CIN, CIN, GETLINE
- **Caption + hashtags:** Read words, numbers and lines. #cpp #getline #input #kodingkonkani #coding

**S3 · Where does the input go?** — 0:20 · built from scene 4

- **Hook (first 1.5s):** "Follow the typed line."
- **Script:** Follow the typed line. Priya, seventeen, Old Goa. Cin drops Priya into name, seventeen into age, and getline drops Old Goa into city. Each piece finds its box.
- **On-screen text:** PRIYA 17 OLD GOA
- **Caption + hashtags:** Follow the input. #cpp #memory #cin #kodingkonkani #beginners

**S4 · Where did the surname go?** — 0:20 · built from scene 8

- **Hook (first 1.5s):** "The surname that disappeared."
- **Script:** The surname that disappeared. Type Priya Naik, and cin only reads Priya, because it stops at the first space. No error, no warning. Use getline for full names.
- **On-screen text:** CIN STOPS AT THE FIRST SPACE
- **Caption + hashtags:** Use getline for full names. #cpp #bugfix #getline #kodingkonkani #coding

**S5 · Pun and challenge** — 0:20 · built from scenes 9, 10

- **Hook (first 1.5s):** "Why is cin so polite?"
- **Script:** Why is cin so polite? It stops listening at the first space. Your challenge: read a name with cin, a beach with getline, and greet the user. Full video: EP 6.
- **On-screen text:** CIN + GETLINE GREETING
- **Caption + hashtags:** Try the challenge. #cpp #codingchallenge #kodingkonkani #programmingjokes #goa

## EP 07 — Operators and expressions

**Module 1 · Variables and types · 5:04 · Pastel Blue + Tomato · Prerequisite: EP 06**

**Learning goals:** use + - * / and % on numbers; predict the result of an expression using precedence; know that dividing two ints throws away the decimal part.

### YouTube

- **Title:** C++ Operators: + - * / % and Precedence | C++ Programming EP 07
- **Description:** Do arithmetic in C++: the five operators, the remainder, operator precedence and the integer division trap, with Xecxec. 0:00 Intro · 0:20 The five operators · 0:55 Maths in code · 1:35 Who goes first? · 2:05 Run it in your head · 2:45 Compile and run · 3:05 Recap · 3:40 Bug of the Day · 4:29 Challenge · 4:49 Next episode
- **Tags:** c++ operators, c++ arithmetic, modulus operator, integer division, operator precedence, koding konkani, c++ for beginners, c++ tutorial, class 11 computer science, coding in goa
- **Thumbnail:** big text "C++ MATHS" in tomato on pastel blue; Xecxec juggling plus, minus, times, divide and percent signs; thin black border and drop shadow.

### Scene list

| # | Start | Length | Template | On screen | Animation & SFX |
| --- | --- | --- | --- | --- | --- |
| 1 | 0:00 | 0:20 | Title card | EP 07 · OPERATORS AND EXPRESSIONS | Tomato title card: EP sticker thuds in, title stamps with a whoosh, Xecxec scuttles in and waves; thud, whoosh, claw-click, sting |
| 2 | 0:20 | 0:35 | Concept slide | "The five operators": five numbered lines and a sharing-samosas analogy card | Five lines spring in one by one with a pop; the samosa card slides in showing seventeen samosas on five plates |
| 3 | 0:55 | 0:40 | Code explain | `ops.cpp`: two ints and five printed expressions | Code types in with key-tick; butter [HL n] highlight sweeps line by line with marker-swipe; explanation card on the right |
| 4 | 1:35 | 0:30 | Concept slide | The expression 2 + 3 * 4 with the multiplication glowing first, then the addition, then the answer 14 | The expression appears; a bracket wraps 3 * 4 and turns it into 12; then 2 + 12 becomes 14; a tomato cross pops on the wrong answer 20; pop per step |
| 5 | 2:05 | 0:40 | Code explain | `ops.cpp` again, with the output panel on the right | Same code; the output panel fills line by line with a ding per output line; [TRACK] cards update |
| 6 | 2:45 | 0:20 | Terminal | Terminal: `g++ ops.cpp -o ops`, then `./ops` | Dark-blue terminal: the command types with key-tick, output prints in mint with a ding |
| 7 | 3:05 | 0:35 | Concept slide | Recap: four ideas on one card | Four recap lines tick in one by one with a pop; Xecxec nods after each tick |
| 8 | 3:40 | 0:40 | Bug of the Day | BUG OF THE DAY: five divided by two gives two | Butter banner drops in with a buzzer; the program compiles and runs; the wrong output appears in tomato; the fix slides in and the output turns mint with a ding |
| 9 | 4:20 | 0:09 | Pun card | I divided five by two and got two. The point got lost along the way. | Full tomato screen, card flips in with a rimshot, Xecxec snaps his claw |
| 10 | 4:29 | 0:20 | Challenge | Task card: 250 minutes in hours and minutes | Task card pops in; checklist ticks with a pop; Xecxec holds a tiny pen |
| 11 | 4:49 | 0:15 | Outro | Next: EP 08 · Comparison and logical operators | Next-episode card slides up with a whoosh; right side stays empty for end-screen elements; sign-off text types in |

### Narration script

**[1 · Title]** Computers are brilliant at maths, but only if we ask in their language. Today we learn the symbols for adding, multiplying, dividing, and a surprising one for leftovers.

**[2 · The five operators]** C plus plus has five arithmetic operators. Plus adds. Minus subtracts. Star multiplies. Slash divides. And percent gives the remainder, what is left over after dividing. Imagine sharing seventeen samosas between five plates. Each plate gets three. That is the slash. Two samosas are left over. That is the percent. Try it on paper first: eleven divided by four, and eleven percent four.

**[3 · Maths in code]** [HL 5] Seventeen students. [HL 6] Five groups. [HL 7] Students plus groups is twenty-two. [HL 8] Students times groups is eighty-five. [HL 9] Now watch this. Students divided by groups is three, not three point four. Both numbers are ints, so C plus plus keeps only the whole part. [HL 10] Percent gives the remainder, which is two.

**[4 · Who goes first?]** What does two plus three times four give? Not twenty. Multiplication, division and remainder go first. Addition and subtraction come after. So three times four is twelve, then two plus twelve is fourteen. If you want addition first, use round brackets. Two plus three, in brackets, times four, is twenty.

**[5 · Run it in your head]** [HL 5] [TRACK students=17] Students is seventeen. [HL 6] [TRACK groups=5] Groups is five. [HL 7] Twenty-two. [HL 8] Eighty-five. [HL 9] Three. [HL 10] Two. [HL 11] And fourteen, because the star goes first.

**[6 · Compile and run]** Compile and run. Sum, twenty-two. Product, eighty-five. Quotient, three. Remainder, two. Mixed, fourteen. All five answers match our predictions.

**[7 · Recap]** Recap. One: plus, minus, star, slash and percent do the arithmetic. Two: percent gives the remainder. Three: multiplication and division go before addition and subtraction, and brackets override both. Four: an int divided by an int is an int, so make one side a decimal when you need decimals. Test yourself: what is twenty-three percent five? The answer is three.

**[8 · Bug of the Day]** Bug of the Day. We want half of five, so we write double half equals five divided by two. It compiles with no warning, and prints two. Not two point five. Both five and two are ints, so the division happens on whole numbers first, and only then is the answer stored as a double. Make one side a decimal, write five point zero, and the answer is two point five.

**[9 · Pun]** I divided five by two and got two. The point got lost along the way.

**[10 · Challenge]** Your challenge: turn two hundred fifty minutes into hours and minutes, using slash and percent. Comment your answer below.

**[11 · Outro]** Next time: comparing values and making decisions with true and false. Keep coding, says Xecxec!

### Code shown

File 1: `ops.cpp` (scene 3, 5)

```cpp
#include <iostream>
using namespace std;

int main() {
    int students = 17;
    int groups = 5;
    cout << "Sum: " << students + groups << endl;
    cout << "Product: " << students * groups << endl;
    cout << "Quotient: " << students / groups << endl;
    cout << "Remainder: " << students % groups << endl;
    cout << "Mixed: " << 2 + 3 * 4 << endl;
    return 0;
}
```

**Expected output:**

```text
Sum: 22
Product: 85
Quotient: 3
Remainder: 2
Mixed: 14
```

### Bug of the Day

Wrong code (5 / 2 divides two ints):

```cpp
#include <iostream>
using namespace std;

int main() {
    double half = 5 / 2;
    cout << "Half of 5: " << half << endl;
    return 0;
}
```

GCC and program output:

```text
Output when run:
Half of 5: 2
```

Fixed code (5.0 makes it a decimal division):

```cpp
#include <iostream>
using namespace std;

int main() {
    double half = 5.0 / 2;
    cout << "Half of 5: " << half << endl;
    return 0;
}
```

Output of the fixed code:

```text
Half of 5: 2.5
```

**Why:** If both sides of a slash are ints, C++ divides as whole numbers and drops the decimal part; make at least one side a double.

### Pun & challenge

- **Pun:** "I divided five by two and got two. The point got lost along the way."
- **Challenge:** Turn 250 minutes into hours and minutes using / and %.
- **Challenge answer:** Hours is 250 / 60, which is 4, and minutes is 250 % 60, which is 10.

### Shorts for EP 07

**S1 · The five operators** — 0:20 · built from scene 2

- **Hook (first 1.5s):** "Five symbols do all the maths."
- **Script:** Five symbols do all the maths. Plus, minus, star, slash, and percent. Seventeen samosas on five plates: slash says three each, percent says two left over.
- **On-screen text:** +  -  *  /  %
- **Caption + hashtags:** Five operators, one minute. #cpp #operators #beginners #kodingkonkani #learntocode

**S2 · Integer division** — 0:20 · built from scene 3

- **Hook (first 1.5s):** "Seventeen divided by five is three."
- **Script:** Seventeen divided by five is three. Not three point four. Two ints give an int, so the decimal part is thrown away. The remainder, with percent, is two.
- **On-screen text:** 17 / 5 = 3 AND 17 % 5 = 2
- **Caption + hashtags:** Ints divide into ints. #cpp #integerdivision #maths #kodingkonkani #coding

**S3 · Who goes first?** — 0:20 · built from scene 4

- **Hook (first 1.5s):** "Two plus three times four."
- **Script:** Two plus three times four. Is it twenty? No, it is fourteen. Multiplication goes before addition. Use round brackets if you want the addition to go first.
- **On-screen text:** 2 + 3 * 4 = 14
- **Caption + hashtags:** Precedence in 30 seconds. #cpp #precedence #maths #kodingkonkani #beginners

**S4 · 5 / 2 is 2** — 0:20 · built from scene 8

- **Hook (first 1.5s):** "Half of five is two?"
- **Script:** Half of five is two? Write five divided by two, and C plus plus prints two. Both numbers are ints. Write five point zero, and you get two point five.
- **On-screen text:** 5 / 2 = 2  BUT  5.0 / 2 = 2.5
- **Caption + hashtags:** Make one side a decimal. #cpp #bugfix #integerdivision #kodingkonkani #coding

**S5 · Pun and challenge** — 0:20 · built from scenes 9, 10

- **Hook (first 1.5s):** "Where did the point go?"
- **Script:** Where did the point go? I divided five by two and got two. The point got lost along the way. Your challenge: turn two hundred fifty minutes into hours and minutes. Full video: EP 7.
- **On-screen text:** 250 MINUTES = ? HOURS ? MINUTES
- **Caption + hashtags:** Try the challenge. #cpp #codingchallenge #kodingkonkani #programmingjokes #goa

## EP 08 — Comparison and logical operators

**Module 1 · Variables and types · 5:04 · Pastel Blue + Tomato · Prerequisite: EP 07**

**Learning goals:** compare values with == != < > <= >=; combine conditions with && || !; never confuse = (store) with == (compare).

### YouTube

- **Title:** C++ Comparison and Logical Operators: == && || ! | C++ Programming EP 08
- **Description:** Make true-or-false decisions in C++ with comparison and logical operators, and avoid the famous = versus == mistake, with Xecxec. 0:00 Intro · 0:15 Questions with yes or no · 0:50 Comparing in code · 1:30 AND, OR, NOT · 2:05 Run it in your head · 2:45 Compile and run · 3:05 Recap · 3:40 Bug of the Day · 4:29 Challenge · 4:49 Next episode
- **Tags:** c++ comparison operators, c++ logical operators, and or not, == vs =, c++ boolean, koding konkani, c++ for beginners, c++ tutorial, class 11 computer science, coding in goa
- **Thumbnail:** big text "TRUE OR FALSE?" in tomato on pastel blue; Xecxec holding a green TRUE card in one claw and a red FALSE card in the other; thin black border and drop shadow.

### Scene list

| # | Start | Length | Template | On screen | Animation & SFX |
| --- | --- | --- | --- | --- | --- |
| 1 | 0:00 | 0:15 | Title card | EP 08 · COMPARE AND DECIDE | Tomato title card: EP sticker thuds in, title stamps with a whoosh, Xecxec scuttles in and waves; thud, whoosh, claw-click, sting |
| 2 | 0:15 | 0:35 | Concept slide | "Questions with two answers": three numbered lines and a bouncer-at-the-door analogy card | Lines spring in with a pop; the bouncer card slides in with a checklist of entry rules |
| 3 | 0:50 | 0:40 | Code explain | `marks.cpp`: three bool variables built from comparisons | Code types in with key-tick; butter [HL n] highlight sweeps line by line with marker-swipe; explanation card on the right |
| 4 | 1:30 | 0:35 | Concept slide | A table with three rows: A && B, A || B, !A, and the four true/false combinations of A and B | The table rows fill in one by one with mint ticks for true and tomato crosses for false; the row being explained glows butter; pop per row |
| 5 | 2:05 | 0:40 | Code explain | `marks.cpp` again, with the output panel on the right | Same code; the output panel fills line by line with a ding per output line; [TRACK] cards update |
| 6 | 2:45 | 0:20 | Terminal | Terminal: `g++ marks.cpp -o marks`, then `./marks` | Dark-blue terminal: the command types with key-tick, output prints in mint with a ding |
| 7 | 3:05 | 0:35 | Concept slide | Recap: four ideas on one card | Four recap lines tick in one by one with a pop; Xecxec nods after each tick |
| 8 | 3:40 | 0:40 | Bug of the Day | BUG OF THE DAY: one equals sign instead of two | Butter banner drops in with a buzzer; the g++ warning appears in tomato, then the program runs and prints the wrong result; the fix slides in and the output turns mint with a ding |
| 9 | 4:20 | 0:09 | Pun card | Why did the single equals sign get arrested? It assigned when it should have compared. | Full tomato screen, card flips in with a rimshot, Xecxec snaps his claw |
| 10 | 4:29 | 0:20 | Challenge | Task card: even and positive | Task card pops in; checklist ticks with a pop; Xecxec holds a tiny pen |
| 11 | 4:49 | 0:15 | Outro | Next: EP 09 · Type conversion and casting | Next-episode card slides up with a whoosh; right side stays empty for end-screen elements; sign-off text types in |

### Narration script

**[1 · Title]** Programs make decisions, and every decision starts with a question that has only two answers: true, or false. Today we learn how to ask those questions.

**[2 · Questions with two answers]** A comparison asks a question about two values, and the answer is a bool. Double equals asks, are they equal? Exclamation equals asks, are they different? Then less than, greater than, and the versions with equals, for at least and at most. Think of a bouncer at a beach party. Are you eighteen or older? True, come in. False, sorry.

**[3 · Comparing in code]** [HL 5] Marks is seventy-two. [HL 6] Passed asks, is marks at least forty? True. [HL 7] Distinction asks, is marks at least seventy-five? False. [HL 8] Merit uses two questions joined by double ampersand, which means and. Marks at least sixty, and marks below seventy-five. Both must be true. [HL 9] Boolalpha makes cout print true and false as words, instead of one and zero.

**[4 · AND, OR, NOT]** Three tools combine questions. And, written as double ampersand, is true only when both sides are true. Or, written as double bar, is true when at least one side is true. Not, an exclamation mark, flips true into false, and false into true. Say it as a sentence: passed and not distinction. Read your conditions aloud, and mistakes become easy to hear.

**[5 · Run it in your head]** [HL 5] [TRACK marks=72] Marks is seventy-two. [HL 10] Passed is true. [HL 11] Distinction is false. [HL 12] Merit is true, because seventy-two is between sixty and seventy-five. [HL 13] Not passed flips true into false. [HL 14] And fail or topper is false, because seventy-two is neither below forty nor above ninety.

**[6 · Compile and run]** Compile and run. Passed, true. Distinction, false. Merit, true. Not passed, false. Fail or topper, false. Five questions, five clear answers.

**[7 · Recap]** Recap. One: a comparison asks a question and answers true or false. Two: double equals compares, a single equals stores. Three: and needs both sides true, or needs one, and not flips the answer. Four: boolalpha prints true and false as words. Pause the video, and write one condition that is true for seventy-two and false for eighty.

**[8 · Bug of the Day]** Bug of the Day. We write if level equals five, with a single equals sign. The compiler warns: suggest parentheses around assignment used as truth value. It is only a warning, so the program runs. And it prints Level five, then Level is five. But level was three! A single equals sign stores five into level, and five counts as true. Use double equals to compare, and the message correctly stays hidden.

**[9 · Pun]** Why did the single equals sign get arrested? It assigned when it should have compared.

**[10 · Challenge]** Your challenge: write a bool that is true only when a number is even and also greater than zero. Test it with minus four, then four. Comment your answer below.

**[11 · Outro]** Next time: converting between int and double, safely. Keep coding, says Xecxec!

### Code shown

File 1: `marks.cpp` (scene 3, 5)

```cpp
#include <iostream>
using namespace std;

int main() {
    int marks = 72;
    bool passed = marks >= 40;
    bool distinction = marks >= 75;
    bool merit = marks >= 60 && marks < 75;
    cout << boolalpha;
    cout << "Passed: " << passed << endl;
    cout << "Distinction: " << distinction << endl;
    cout << "Merit: " << merit << endl;
    cout << "Not passed: " << !passed << endl;
    cout << "Fail or topper: " << (marks < 40 || marks > 90) << endl;
    return 0;
}
```

**Expected output:**

```text
Passed: true
Distinction: false
Merit: true
Not passed: false
Fail or topper: false
```

### Bug of the Day

Wrong code (if (level = 5) stores instead of comparing):

```cpp
#include <iostream>
using namespace std;

int main() {
    int level = 3;
    if (level = 5) {
        cout << "Level five!" << endl;
    }
    cout << "Level is " << level << endl;
    return 0;
}
```

GCC and program output:

```text
level.cpp: In function ‘int main()’:
level.cpp:6:15: warning: suggest parentheses around assignment used as truth value [-Wparentheses]
    6 |     if (level = 5) {
      |         ~~~~~~^~~
Output when run:
Level five!
Level is 5
```

Fixed code (double equals compares):

```cpp
#include <iostream>
using namespace std;

int main() {
    int level = 3;
    if (level == 5) {
        cout << "Level five!" << endl;
    }
    cout << "Level is " << level << endl;
    return 0;
}
```

Output of the fixed code:

```text
Level is 3
```

**Why:** A single = stores a value and the stored value counts as true, so use == whenever you want to compare.

### Pun & challenge

- **Pun:** "Why did the single equals sign get arrested? It assigned when it should have compared."
- **Challenge:** Write a bool that is true only when a number is even and greater than zero, and test it with -4 and 4.
- **Challenge answer:** Use n % 2 == 0 && n > 0: it is false for -4 and true for 4.

### Shorts for EP 08

**S1 · Comparison operators** — 0:20 · built from scene 2

- **Hook (first 1.5s):** "Every question has two answers."
- **Script:** Every question has two answers. Double equals asks, are they equal? Exclamation equals asks, are they different? Less than and greater than ask which is bigger. The answer is always true or false.
- **On-screen text:** ==  !=  <  >  <=  >=
- **Caption + hashtags:** Ask true-or-false questions. #cpp #operators #beginners #kodingkonkani #learntocode

**S2 · Marks and merit** — 0:20 · built from scene 3

- **Hook (first 1.5s):** "Between sixty and seventy-five."
- **Script:** Between sixty and seventy-five. Marks at least sixty, and marks below seventy-five. Two questions joined by double ampersand, and both must be true. Seventy-two passes the test.
- **On-screen text:** MARKS >= 60 && MARKS < 75
- **Caption + hashtags:** Join two questions. #cpp #logicaloperators #coding #kodingkonkani #beginners

**S3 · AND, OR, NOT** — 0:20 · built from scene 4

- **Hook (first 1.5s):** "And, or, not in thirty seconds."
- **Script:** And, or, not in thirty seconds. And needs both sides true. Or needs just one. Not flips the answer. Read your condition aloud as a sentence, and the mistakes jump out.
- **On-screen text:** &&   ||   !
- **Caption + hashtags:** Three tools, one truth table. #cpp #truthtable #logic #kodingkonkani #learntocode

**S4 · = versus ==** — 0:20 · built from scene 8

- **Hook (first 1.5s):** "One missing equals sign."
- **Script:** One missing equals sign. Write if level equals five with a single equals, and the program stores five instead of asking. g plus plus only warns, so the bug hides. Use double equals to compare.
- **On-screen text:** IF (LEVEL = 5) IS A BUG
- **Caption + hashtags:** Store with =, compare with ==. #cpp #bugfix #comparison #kodingkonkani #coding

**S5 · Pun and challenge** — 0:20 · built from scenes 9, 10

- **Hook (first 1.5s):** "The equals sign got arrested."
- **Script:** The equals sign got arrested. It assigned when it should have compared. Your challenge: a bool that is true only for even numbers above zero. Test minus four and four. Full video: EP 8.
- **On-screen text:** EVEN AND POSITIVE?
- **Caption + hashtags:** Try the challenge. #cpp #codingchallenge #kodingkonkani #programmingjokes #goa

## EP 09 — Type conversion and casting

**Module 1 · Variables and types · 5:19 · Pastel Blue + Tomato · Prerequisite: EP 08**

**Learning goals:** explain implicit conversion between int and double; convert on purpose with static_cast; recognise a narrowing conversion error in braces.

### YouTube

- **Title:** Type Conversion and static_cast in C++ | C++ Programming EP 09
- **Description:** See how C++ converts between int and double, how to convert on purpose with static_cast, and why braces refuse to lose data, with Xecxec. 0:00 Intro · 0:20 Changing types · 1:05 static_cast in code · 1:45 Widening and narrowing · 2:20 Run it in your head · 3:00 Compile and run · 3:20 Recap · 3:55 Bug of the Day · 4:44 Challenge · 5:04 Next episode
- **Tags:** c++ type conversion, static_cast, implicit conversion, narrowing conversion, int to double, koding konkani, c++ for beginners, c++ tutorial, class 11 computer science, coding in goa
- **Thumbnail:** big text "CASTING TYPES" in tomato on pastel blue; Xecxec pouring a double-shaped jug into an int-shaped glass with drops spilling; thin black border and drop shadow.

### Scene list

| # | Start | Length | Template | On screen | Animation & SFX |
| --- | --- | --- | --- | --- | --- |
| 1 | 0:00 | 0:20 | Title card | EP 09 · TYPE CONVERSION AND CASTING | Tomato title card: EP sticker thuds in, title stamps with a whoosh, Xecxec scuttles in and waves; thud, whoosh, claw-click, sting |
| 2 | 0:20 | 0:45 | Concept slide | "Changing types": three numbered lines and a measuring-jug analogy card | Lines spring in with a pop; the jug card slides in with a big jug, a small glass and drops spilling |
| 3 | 1:05 | 0:40 | Code explain | `convert.cpp`: total and people, then two static_cast lines | Code types in with key-tick; butter [HL n] highlight sweeps line by line with marker-swipe; explanation card on the right |
| 4 | 1:45 | 0:35 | Concept slide | Two jugs: int to double with a tick and no loss; double to int with a cross and the .4 dropped | A small int glass pours into a big double jug and everything fits, mint tick; then the double jug pours into the int glass and the decimal drops are lost, tomato cross; pop per step |
| 5 | 2:20 | 0:40 | Code explain | `convert.cpp` again, with the output panel on the right | Same code; the output panel fills line by line with a ding per output line; [TRACK] cards update |
| 6 | 3:00 | 0:20 | Terminal | Terminal: `g++ convert.cpp -o convert`, then `./convert` | Dark-blue terminal: the command types with key-tick, output prints in mint with a ding |
| 7 | 3:20 | 0:35 | Concept slide | Recap: four ideas on one card | Four recap lines tick in one by one with a pop; Xecxec nods after each tick |
| 8 | 3:55 | 0:40 | Bug of the Day | BUG OF THE DAY: a double squeezed into an int with braces | Butter banner drops in with a buzzer; wrong code shakes; the g++ narrowing error appears in tomato; the fix slides in and the output turns mint with a ding |
| 9 | 4:35 | 0:09 | Pun card | A double tried to fit into an int. The compiler said: sorry, no extra decimals allowed. | Full tomato screen, card flips in with a rimshot, Xecxec snaps his claw |
| 10 | 4:44 | 0:20 | Challenge | Task card: average of three marks | Task card pops in; checklist ticks with a pop; Xecxec holds a tiny pen |
| 11 | 5:04 | 0:15 | Outro | Next: EP 10 · auto, const and constexpr | Next-episode card slides up with a whoosh; right side stays empty for end-screen elements; sign-off text types in |

### Narration script

**[1 · Title]** Sometimes a value is the wrong type for the job. An int needs to become a double, or a double needs to become an int. Today we learn to convert between types, on purpose and safely.

**[2 · Changing types]** C plus plus converts types in two ways. Implicit conversion happens by itself. Add an int and a double, and the int quietly becomes a double. That is safe, like pouring a small glass into a big jug. The other way is risky. Putting a double into an int throws away the decimal part, like pouring a big jug into a small glass. So when you really want that, say it out loud, with static cast.

**[3 · static_cast in code]** [HL 5] Total is seventeen. [HL 6] People is five. [HL 7] Here is the fix for integer division. Static cast to double turns total into seventeen point zero before dividing. Now a double divided by an int is a decimal division, so the average is three point four. [HL 8] And going back, static cast to int cuts off the decimal part. Three point four becomes three. It does not round, it truncates.

**[4 · Widening and narrowing]** Widening means going to a bigger type, like int to double. Nothing is lost. Narrowing means going to a smaller type, like double to int. Something is lost, here the decimal part. Narrowing is where bugs hide, so C plus plus gives you a safety net. When you use curly braces to create a variable, the compiler refuses any narrowing it can see.

**[5 · Run it in your head]** [HL 5] [TRACK total=17] Total is seventeen. [HL 6] [TRACK people=5] People is five. [HL 7] [TRACK average=3.4] Average is seventeen divided by five, which is three point four. [HL 8] [TRACK rounded=3] Rounded is three. [HL 9] The first line prints three point four. [HL 10] The second prints three.

**[6 · Compile and run]** Compile and run. Average, three point four. Rounded down, three. Without the cast, the average would have been three. The cast made all the difference.

**[7 · Recap]** Recap. One: widening, like int to double, is safe and happens by itself. Two: narrowing, like double to int, loses the decimal part. Three: static cast says you meant it, and truncates instead of rounding. Four: curly braces refuse any narrowing they can see. If you remember one thing, remember this: cast first, then divide.

**[8 · Bug of the Day]** Bug of the Day. We write int whole in curly braces with three point seven inside. The compiler says, narrowing conversion of three point seven from double to int. This time it is a real error, so nothing is built. Braces refuse to lose data silently. If you truly want three, say so with static cast to int. Then the program prints Whole, three.

**[9 · Pun]** A double tried to fit into an int. The compiler said, sorry, no extra decimals allowed.

**[10 · Challenge]** Your challenge: the marks are seventy-two, sixty-five and ninety. Find their average as a double, then print it rounded down as an int. Comment your answer below.

**[11 · Outro]** Next time: auto, const and constexpr, the keywords that protect your values. Keep coding, says Xecxec!

### Code shown

File 1: `convert.cpp` (scene 3, 5)

```cpp
#include <iostream>
using namespace std;

int main() {
    int total = 17;
    int people = 5;
    double average = static_cast<double>(total) / people;
    int rounded = static_cast<int>(average);
    cout << "Average: " << average << endl;
    cout << "Rounded down: " << rounded << endl;
    return 0;
}
```

**Expected output:**

```text
Average: 3.4
Rounded down: 3
```

### Bug of the Day

Wrong code (int whole{3.7} narrows a double):

```cpp
#include <iostream>
using namespace std;

int main() {
    int whole{3.7};
    cout << "Whole: " << whole << endl;
    return 0;
}
```

GCC output:

```text
whole.cpp: In function ‘int main()’:
whole.cpp:5:15: error: narrowing conversion of ‘3.7000000000000002e+0’ from ‘double’ to ‘int’ [-Wnarrowing]
    5 |     int whole{3.7};
      |               ^~~
```

Fixed code (static_cast says it on purpose):

```cpp
#include <iostream>
using namespace std;

int main() {
    int whole = static_cast<int>(3.7);
    cout << "Whole: " << whole << endl;
    return 0;
}
```

Output of the fixed code:

```text
Whole: 3
```

**Why:** Curly braces refuse to lose data by accident; if you really want to drop the decimal part, say so with static_cast<int>.

### Pun & challenge

- **Pun:** "A double tried to fit into an int. The compiler said: sorry, no extra decimals allowed."
- **Challenge:** Find the average of the marks 72, 65 and 90 as a double, then print it rounded down as an int.
- **Challenge answer:** Cast the sum to double before dividing by 3; the average is about 75.6667 and the int is 75.

### Shorts for EP 09

**S1 · Big jug, small glass** — 0:20 · built from scene 2

- **Hook (first 1.5s):** "Pouring a jug into a glass."
- **Script:** Pouring a jug into a glass. An int into a double fits easily. A double into an int spills the decimals. When you want that, say it out loud with static cast.
- **On-screen text:** INT TO DOUBLE IS SAFE
- **Caption + hashtags:** Widening is safe, narrowing spills. #cpp #typeconversion #beginners #kodingkonkani #learntocode

**S2 · Fix integer division** — 0:20 · built from scene 3

- **Hook (first 1.5s):** "Make seventeen divided by five exact."
- **Script:** Make seventeen divided by five exact. Cast the total to double first, then divide. Three point four, not three. One small cast saves your decimals.
- **On-screen text:** STATIC_CAST<DOUBLE>(TOTAL) / PEOPLE
- **Caption + hashtags:** Cast before you divide. #cpp #staticcast #coding #kodingkonkani #maths

**S3 · Truncate, not round** — 0:20 · built from scene 4

- **Hook (first 1.5s):** "Three point nine becomes three."
- **Script:** Three point nine becomes three. Casting a double to an int cuts the decimals off. It does not round. If you want rounding, that is a different tool.
- **On-screen text:** STATIC_CAST<INT>(3.9) = 3
- **Caption + hashtags:** Casting truncates. #cpp #casting #programming #kodingkonkani #beginners

**S4 · Narrowing conversion** — 0:20 · built from scene 8

- **Hook (first 1.5s):** "Braces refuse to lose data."
- **Script:** Braces refuse to lose data. Write int whole in braces with three point seven, and g plus plus says, narrowing conversion from double to int. It is a real error. Use static cast instead.
- **On-screen text:** NARROWING CONVERSION OF 3.7
- **Caption + hashtags:** Braces are a safety net. #cpp #bugfix #narrowing #kodingkonkani #compilererror

**S5 · Pun and challenge** — 0:20 · built from scenes 9, 10

- **Hook (first 1.5s):** "No extra decimals allowed."
- **Script:** No extra decimals allowed. A double tried to fit into an int, and the compiler said sorry. Your challenge: the average of seventy-two, sixty-five and ninety. Full video: EP 9.
- **On-screen text:** AVERAGE OF 72, 65, 90
- **Caption + hashtags:** Try the challenge. #cpp #codingchallenge #kodingkonkani #programmingjokes #goa

## EP 10 — auto, const and constexpr

**Module 1 · Variables and types · 5:32 · Pastel Blue + Tomato · Prerequisite: EP 09**

**Learning goals:** let the compiler pick a type with auto; protect a value with const; name a fixed number with constexpr.

### YouTube

- **Title:** auto, const and constexpr in C++ | C++ Programming EP 10
- **Description:** Let the compiler guess types with auto, lock values with const and name fixed numbers with constexpr, with Xecxec. 0:00 Intro · 0:20 Three keywords · 1:05 Reading the code · 1:50 A locked box · 2:30 Run it in your head · 3:10 Compile and run · 3:30 Recap · 4:10 Bug of the Day · 4:57 Challenge · 5:17 Next episode
- **Tags:** c++ auto, c++ const, c++ constexpr, const vs constexpr, read-only variable, koding konkani, c++ for beginners, c++ tutorial, class 11 computer science, coding in goa
- **Thumbnail:** big text "AUTO + CONST" in tomato on pastel blue; Xecxec locking a box with a padlock labelled const; thin black border and drop shadow.

### Scene list

| # | Start | Length | Template | On screen | Animation & SFX |
| --- | --- | --- | --- | --- | --- |
| 1 | 0:00 | 0:20 | Title card | EP 10 · AUTO, CONST, CONSTEXPR | Tomato title card: EP sticker thuds in, title stamps with a whoosh, Xecxec scuttles in and waves; thud, whoosh, claw-click, sting |
| 2 | 0:20 | 0:45 | Concept slide | "Three keywords": three numbered lines and a padlock-on-a-locker analogy card | Lines spring in with a pop; the locker card slides in with a padlock clicking shut |
| 3 | 1:05 | 0:45 | Code explain | `shop.cpp`: a constexpr at the top, then const and three auto variables | Code types in with key-tick; butter [HL n] highlight sweeps line by line with marker-swipe; explanation card on the right |
| 4 | 1:50 | 0:40 | Memory boxes | Two memory boxes: tables = 8 with a padlock icon and a read-only tag, price = 250.0 open and editable | The two boxes pop in; a padlock snaps onto the tables box with a click; an arrow tries to write 9 into it and bounces off with a buzzer; an arrow writes into price and succeeds |
| 5 | 2:30 | 0:40 | Code explain | `shop.cpp` again, with the output panel on the right | Same code; the output panel fills line by line with a ding per output line; [TRACK] cards update |
| 6 | 3:10 | 0:20 | Terminal | Terminal: `g++ shop.cpp -o shop`, then `./shop` | Dark-blue terminal: the command types with key-tick, output prints in mint with a ding |
| 7 | 3:30 | 0:40 | Concept slide | Recap: four ideas on one card | Four recap lines tick in one by one with a pop; Xecxec nods after each tick |
| 8 | 4:10 | 0:40 | Bug of the Day | BUG OF THE DAY: assigning to a const | Butter banner drops in with a buzzer; wrong code shakes; the g++ read-only error appears in tomato; the fix slides in and the output turns mint with a ding |
| 9 | 4:50 | 0:07 | Pun card | Why can't a const go to parties? It refuses to change. | Full tomato screen, card flips in with a rimshot, Xecxec snaps his claw |
| 10 | 4:57 | 0:20 | Challenge | Task card: circle area with pi | Task card pops in; checklist ticks with a pop; Xecxec holds a tiny pen |
| 11 | 5:17 | 0:15 | Outro | Next: EP 11 · Strings with std::string | Next-episode card slides up with a whoosh; right side stays empty for end-screen elements; sign-off text types in |

### Narration script

**[1 · Title]** Three little keywords make your code shorter and safer. Auto lets the compiler pick the type. Const locks a value. And constexpr names a number that never changes. Let us meet them.

**[2 · Three keywords]** Auto says, you work out the type from the value. Write auto x equals four, and x is an int. Const says, once this has a value, nobody may change it. Constexpr goes one step further. It says, this value is known before the program even runs, so it is perfect for fixed numbers like a tax rate. Think of a locker at the shack. Once you lock your bag, nobody changes what is inside.

**[3 · Reading the code]** [HL 4] A constexpr double, the tax rate, eighteen percent, named with a k in front. It lives outside main, so every function can see it. [HL 7] Const int tables is eight. This one is locked. [HL 8] Auto price equals two hundred fifty point zero. The compiler sees a decimal, so price is a double. [HL 9] Auto seats equals four. A whole number, so seats is an int. [HL 10] And auto total takes its type from the maths, a double.

**[4 · A locked box]** Here is const in memory. The tables box has a padlock. You can read it as much as you like, but any attempt to write into it is blocked, and the compiler stops you before the program runs. The price box has no lock, so we can still change it later. Use const for everything that should not change. It tells readers, and the compiler, what you meant.

**[5 · Run it in your head]** [HL 7] [TRACK tables=8] Tables is eight, locked. [HL 8] [TRACK price=250.0] Price is two hundred fifty. [HL 9] [TRACK seats=4] Seats is four. [HL 10] [TRACK total=295] Total is price times one point one eight, which is two hundred ninety-five. [HL 11] The first line prints eight. [HL 13] The last prints two hundred ninety-five.

**[6 · Compile and run]** Compile and run. Tables, eight. Seats, four. Total, two hundred ninety-five. Notice we never wrote the word double or int on the three auto lines, yet the numbers came out right.

**[7 · Recap]** Recap. One: auto lets the compiler pick the type from the value. Two: const locks a value after it is set, and the compiler blocks any change. Three: constexpr names a value known before the program runs. Four: use const by default, and remove it only when a value truly must change. Try adding the word const to a variable of your own, then try to change it.

**[8 · Bug of the Day]** Bug of the Day. We lock tables with const, then try to set it to nine. The compiler says, assignment of read-only variable tables. That is the padlock doing its job. This is a real error, so no program is built. If the value truly must change, remove const. If it must not, fix the line that tries to change it. Here, we simply start with nine.

**[9 · Pun]** Why can't a const go to parties? It refuses to change.

**[10 · Challenge]** Your challenge: make a constexpr for pi, three point one four one five nine. Make a const radius of five. Print the area, pi times radius times radius. Comment your answer below.

**[11 · Outro]** Next time: strings, which are text you can join, measure and change. Keep coding, says Xecxec!

### Code shown

File 1: `shop.cpp` (scene 3, 5)

```cpp
#include <iostream>
using namespace std;

constexpr double kGst = 0.18;

int main() {
    const int tables = 8;
    auto price = 250.0;
    auto seats = 4;
    auto total = price * (1 + kGst);
    cout << "Tables: " << tables << endl;
    cout << "Seats: " << seats << endl;
    cout << "Total: " << total << endl;
    return 0;
}
```

**Expected output:**

```text
Tables: 8
Seats: 4
Total: 295
```

### Bug of the Day

Wrong code (tables is const but gets a new value):

```cpp
#include <iostream>
using namespace std;

int main() {
    const int tables = 8;
    tables = 9;
    cout << "Tables: " << tables << endl;
    return 0;
}
```

GCC output:

```text
locked.cpp: In function ‘int main()’:
locked.cpp:6:12: error: assignment of read-only variable ‘tables’
    6 |     tables = 9;
      |     ~~~~~~~^~~
```

Fixed code (start with the value we want):

```cpp
#include <iostream>
using namespace std;

int main() {
    const int tables = 9;
    cout << "Tables: " << tables << endl;
    return 0;
}
```

Output of the fixed code:

```text
Tables: 9
```

**Why:** A const variable can be set only once, when it is created, so the compiler rejects any later assignment.

### Pun & challenge

- **Pun:** "Why can't a const go to parties? It refuses to change."
- **Challenge:** Make a constexpr for pi (3.14159) and a const radius of 5, then print the area of the circle.
- **Challenge answer:** Print kPi * radius * radius; the area is about 78.5397.

### Shorts for EP 10

**S1 · Three keywords** — 0:20 · built from scene 2

- **Hook (first 1.5s):** "Three keywords, three jobs."
- **Script:** Three keywords, three jobs. Auto lets the compiler pick the type. Const locks a value after it is set. Constexpr names a number that is known before the program even runs.
- **On-screen text:** AUTO  CONST  CONSTEXPR
- **Caption + hashtags:** Three keywords in 30 seconds. #cpp #constexpr #beginners #kodingkonkani #learntocode

**S2 · auto picks the type** — 0:20 · built from scene 3

- **Hook (first 1.5s):** "You do not always have to say int."
- **Script:** You do not always have to say int. Write auto price equals two hundred fifty point zero, and the compiler sees a decimal, so price is a double. Auto seats equals four becomes an int.
- **On-screen text:** AUTO PRICE = 250.0
- **Caption + hashtags:** Let the compiler decide. #cpp #auto #coding #kodingkonkani #beginners

**S3 · A padlock for a variable** — 0:20 · built from scene 4

- **Hook (first 1.5s):** "Lock a value with one word."
- **Script:** Lock a value with one word. Const puts a padlock on the box. You can read what is inside as often as you like, but nobody can change it. The compiler enforces it.
- **On-screen text:** CONST = A PADLOCK
- **Caption + hashtags:** Const protects your values. #cpp #const #programming #kodingkonkani #learntocode

**S4 · Assignment of read-only variable** — 0:20 · built from scene 8

- **Hook (first 1.5s):** "You cannot change a const."
- **Script:** You cannot change a const. Try, and g plus plus says, assignment of read-only variable tables. It is a real error, so nothing is built. Remove the extra line, or start with the value you want.
- **On-screen text:** ASSIGNMENT OF READ-ONLY VARIABLE
- **Caption + hashtags:** Const means set once. #cpp #bugfix #const #kodingkonkani #compilererror

**S5 · Pun and challenge** — 0:20 · built from scenes 9, 10

- **Hook (first 1.5s):** "A const at a party."
- **Script:** A const at a party. Why can't a const go? It refuses to change. Your challenge: a constexpr pi, a const radius, and the area of a circle. Full video: EP 10.
- **On-screen text:** AREA = PI * R * R
- **Caption + hashtags:** Try the challenge. #cpp #codingchallenge #kodingkonkani #programmingjokes #goa

## EP 11 — Strings with std::string

**Module 1 · Variables and types · 5:24 · Pastel Blue + Tomato · Prerequisite: EP 10**

**Learning goals:** create and join strings with +; measure a string with .length() and read a letter with [ ]; know why two string literals cannot be added.

### YouTube

- **Title:** C++ Strings: std::string, +, length() | C++ Programming EP 11
- **Description:** Store, join and measure text in C++ with std::string, and find out why adding two quoted pieces of text fails, with Xecxec. 0:00 Intro · 0:25 Text as a string · 1:05 Joining and measuring · 1:45 Letters in memory · 2:25 Run it in your head · 3:05 Compile and run · 3:25 Recap · 4:00 Bug of the Day · 4:49 Challenge · 5:09 Next episode
- **Tags:** c++ string, std::string, string length, string concatenation, c++ for beginners, koding konkani, c++ tutorial, invalid operands, class 11 computer science, coding in goa
- **Thumbnail:** big text "C++ STRINGS" in tomato on pastel blue; Xecxec threading letter beads G, O, A onto a string; thin black border and drop shadow.

### Scene list

| # | Start | Length | Template | On screen | Animation & SFX |
| --- | --- | --- | --- | --- | --- |
| 1 | 0:00 | 0:25 | Title card | EP 11 · STRINGS WITH STD::STRING | Tomato title card: EP sticker thuds in, title stamps with a whoosh, Xecxec scuttles in and waves; thud, whoosh, claw-click, sting |
| 2 | 0:25 | 0:40 | Concept slide | "Text as a string": three numbered lines and a bead-necklace analogy card | Lines spring in with a pop; the necklace card slides in with letter beads numbered from zero |
| 3 | 1:05 | 0:40 | Code explain | `strings.cpp`: two strings, a joined one, then length, first letter and an append | Code types in with key-tick; butter [HL n] highlight sweeps line by line with marker-swipe; explanation card on the right |
| 4 | 1:45 | 0:40 | Memory boxes | Nine character boxes holding G, o, a, space, B, e, a, c, h, numbered 0 to 8, under the label full | The nine boxes pop in left to right with index numbers underneath; a pointer arrow marks box 0 and the letter G lifts out; the length bracket 9 spans all boxes; pop per box |
| 5 | 2:25 | 0:40 | Code explain | `strings.cpp` again, with the output panel on the right | Same code; the output panel fills line by line with a ding per output line; [TRACK] cards update |
| 6 | 3:05 | 0:20 | Terminal | Terminal: `g++ strings.cpp -o strings`, then `./strings` | Dark-blue terminal: the command types with key-tick, output prints in mint with a ding |
| 7 | 3:25 | 0:35 | Concept slide | Recap: four ideas on one card | Four recap lines tick in one by one with a pop; Xecxec nods after each tick |
| 8 | 4:00 | 0:40 | Bug of the Day | BUG OF THE DAY: adding two string literals | Butter banner drops in with a buzzer; wrong code shakes; the g++ invalid operands error appears in tomato; the fix slides in and the output turns mint with a ding |
| 9 | 4:40 | 0:09 | Pun card | I tried to add two string literals. The compiler said we are not compatible: invalid operands. | Full tomato screen, card flips in with a rimshot, Xecxec snaps his claw |
| 10 | 4:49 | 0:20 | Challenge | Task card: your full name and its length | Task card pops in; checklist ticks with a pop; Xecxec holds a tiny pen |
| 11 | 5:09 | 0:15 | Outro | Next: EP 12 · Formatting output | Next-episode card slides up with a whoosh; right side stays empty for end-screen elements; sign-off text types in |

### Narration script

**[1 · Title]** Numbers are only half of programming. The other half is text: names, messages and words. In C plus plus, text lives in a type called string, and today we learn to join it, measure it and pick it apart.

**[2 · Text as a string]** A string is a row of characters. To use it, include the string header, then write string, a name, and a value in double quotes. Plus joins two strings together. Dot length tells you how many characters it holds. And square brackets pick out one character, counting from zero, not from one. Think of a necklace of letter beads. The first bead is bead zero.

**[3 · Joining and measuring]** [HL 6] First is Goa. [HL 7] Second is Beach. [HL 8] Full joins first, a space in quotes, and second. Without the space, the words would stick together. [HL 9] Printing full gives Goa Beach. [HL 10] Dot length counts every character, including the space. [HL 11] Full in square brackets with zero picks the first letter. [HL 12] And plus equals adds the letters e and s to the end.

**[4 · Letters in memory]** Here is the string full in memory. Nine boxes, one per character, numbered from zero to eight. The space is a character too, in box three. That is why the length is nine, not eight. And index zero is the letter G. If you ask for an index past the end, you reach outside the string, so always stay between zero and length minus one.

**[5 · Run it in your head]** [HL 6] [TRACK first=Goa] First is Goa. [HL 7] [TRACK second=Beach] Second is Beach. [HL 8] [TRACK full=Goa Beach] Full is Goa Beach. [HL 9] The first print says, Goa Beach. [HL 10] The length is nine. [HL 11] The first letter is G. [HL 12] [TRACK full=Goa Beaches] After plus equals, full becomes Goa Beaches. [HL 13] And that is the last line.

**[6 · Compile and run]** Compile and run. Goa Beach. Length, nine. First letter, G. And Goa Beaches. Four lines, four string tools, one tidy program.

**[7 · Recap]** Recap. One: a string is a row of characters, and you need the string header. Two: plus joins strings, and at least one side must be a real string. Three: dot length counts every character, including spaces. Four: indexes start at zero, so the last letter is at length minus one. Say them out loud, and you can handle any beginner text task.

**[8 · Bug of the Day]** Bug of the Day. We try to build a message by adding hello comma, in quotes, and Goa, in quotes. The compiler says, invalid operands of types const char array and const char array to binary operator plus. Quoted text is not a string yet. It is a plain array of characters, and plus does not work on two of those. Wrap one side in string, and plus works.

**[9 · Pun]** I tried to add two string literals. The compiler said we are not compatible: invalid operands.

**[10 · Challenge]** Your challenge: join your first and last name with a space between them. Print the full name and how many characters it has. Comment your answer below.

**[11 · Outro]** Next time: formatting output, so numbers line up like a proper price list. Keep coding, says Xecxec!

### Code shown

File 1: `strings.cpp` (scene 3, 5)

```cpp
#include <iostream>
#include <string>
using namespace std;

int main() {
    string first = "Goa";
    string second = "Beach";
    string full = first + " " + second;
    cout << full << endl;
    cout << "Length: " << full.length() << endl;
    cout << "First letter: " << full[0] << endl;
    full += "es";
    cout << full << endl;
    return 0;
}
```

**Expected output:**

```text
Goa Beach
Length: 9
First letter: G
Goa Beaches
```

### Bug of the Day

Wrong code (two quoted pieces of text are added):

```cpp
#include <iostream>
#include <string>
using namespace std;

int main() {
    string msg = "Hello, " + "Goa";
    cout << msg << endl;
    return 0;
}
```

GCC output:

```text
hello_goa.cpp: In function ‘int main()’:
hello_goa.cpp:6:28: error: invalid operands of types ‘const char [8]’ and ‘const char [4]’ to binary ‘operator+’
    6 |     string msg = "Hello, " + "Goa";
      |                  ~~~~~~~~~ ^ ~~~~~
      |                  |           |
      |                  |           const char [4]
      |                  const char [8]
```

Fixed code (one side is wrapped in string):

```cpp
#include <iostream>
#include <string>
using namespace std;

int main() {
    string msg = string("Hello, ") + "Goa";
    cout << msg << endl;
    return 0;
}
```

Output of the fixed code:

```text
Hello, Goa
```

**Why:** Text in double quotes is a plain character array, not a string, so at least one side of + must be a std::string.

### Pun & challenge

- **Pun:** "I tried to add two string literals. The compiler said we are not compatible: invalid operands."
- **Challenge:** Join your first and last name with a space between them, then print the full name and its length.
- **Challenge answer:** Use first + " " + last, then print full and full.length().

### Shorts for EP 11

**S1 · Text is a string** — 0:20 · built from scene 2

- **Hook (first 1.5s):** "Text in C++ is a row of beads."
- **Script:** Text in C plus plus is a row of beads. Include string, then write string, a name and a value in quotes. Plus joins strings. Dot length counts the characters.
- **On-screen text:** STRING = A ROW OF CHARACTERS
- **Caption + hashtags:** Meet std::string. #cpp #strings #beginners #kodingkonkani #learntocode

**S2 · Join and measure** — 0:20 · built from scene 3

- **Hook (first 1.5s):** "Goa plus Beach equals Goa Beach."
- **Script:** Goa plus Beach equals Goa Beach, if you add the space yourself. Then dot length says nine, because the space counts. Square brackets with zero give the first letter, G.
- **On-screen text:** "GOA" + " " + "BEACH"
- **Caption + hashtags:** Join strings with plus. #cpp #stringconcatenation #coding #kodingkonkani #beginners

**S3 · Count from zero** — 0:20 · built from scene 4

- **Hook (first 1.5s):** "The first letter is number zero."
- **Script:** The first letter is number zero. A string of nine characters has places zero to eight. The space counts as a character too. Always stay between zero and length minus one.
- **On-screen text:** INDEX 0 TO 8
- **Caption + hashtags:** Strings count from zero. #cpp #index #programming #kodingkonkani #learntocode

**S4 · Invalid operands** — 0:20 · built from scene 8

- **Hook (first 1.5s):** "Two quoted texts cannot be added."
- **Script:** Two quoted texts cannot be added. Write hello in quotes plus Goa in quotes, and g plus plus says, invalid operands. Quoted text is not a string yet. Wrap one side in string.
- **On-screen text:** INVALID OPERANDS TO BINARY +
- **Caption + hashtags:** Wrap one side in string(). #cpp #bugfix #strings #kodingkonkani #compilererror

**S5 · Pun and challenge** — 0:20 · built from scenes 9, 10

- **Hook (first 1.5s):** "Two literals, not compatible."
- **Script:** Two literals, not compatible. I tried to add two string literals, and the compiler said, invalid operands. Your challenge: join your first and last name and print the length. Full video: EP 11.
- **On-screen text:** FULL NAME + LENGTH
- **Caption + hashtags:** Try the challenge. #cpp #codingchallenge #kodingkonkani #programmingjokes #goa

## EP 12 — Formatting output

**Module 1 · Variables and types · 5:24 · Pastel Blue + Tomato · Prerequisite: EP 11**

**Learning goals:** set column widths with setw and alignment with left and right; control decimals with fixed and setprecision; know that setprecision alone counts all digits.

### YouTube

- **Title:** Formatting Output in C++: setw, setprecision, fixed | C++ Programming EP 12
- **Description:** Make C++ output look tidy: line up columns with setw and control decimal places with fixed and setprecision, with Xecxec. 0:00 Intro · 0:20 Why format? · 1:00 A price list · 1:40 Width and precision · 2:20 Run it in your head · 3:00 Compile and run · 3:25 Recap · 4:00 Bug of the Day · 4:49 Challenge · 5:09 Next module
- **Tags:** c++ setw, c++ setprecision, c++ fixed, iomanip, format output c++, koding konkani, c++ for beginners, c++ tutorial, class 11 computer science, coding in goa
- **Thumbnail:** big text "TIDY OUTPUT" in tomato on pastel blue; Xecxec holding a neat price-list card with aligned columns; thin black border and drop shadow.

### Scene list

| # | Start | Length | Template | On screen | Animation & SFX |
| --- | --- | --- | --- | --- | --- |
| 1 | 0:00 | 0:20 | Title card | EP 12 · FORMATTING OUTPUT | Tomato title card: EP sticker thuds in, title stamps with a whoosh, Xecxec scuttles in and waves; thud, whoosh, claw-click, sting |
| 2 | 0:20 | 0:40 | Concept slide | "Why format?": three numbered lines and a messy-versus-neat price-board analogy card | Lines spring in with a pop; the card slides in showing a crooked chalkboard menu next to a tidy printed one |
| 3 | 1:00 | 0:40 | Code explain | `menu.cpp`: setup line, a header row and two item rows | Code types in with key-tick; butter [HL n] highlight sweeps line by line with marker-swipe; explanation card on the right |
| 4 | 1:40 | 0:40 | Concept slide | Two rows of boxes: a ten-box strip with Fish at the left and an eight-box strip with 249.50 at the right | Empty column strips appear; the text Fish drops into the left of the ten-wide strip and the number 249.50 into the right of the eight-wide strip; spare boxes fill with dots; pop per placement |
| 5 | 2:20 | 0:40 | Code explain | `menu.cpp` again, with the output panel on the right | Same code; the output panel fills line by line with a ding per output line; [TRACK] cards update |
| 6 | 3:00 | 0:25 | Terminal | Terminal: `g++ menu.cpp -o menu`, then `./menu` | Dark-blue terminal: the command types with key-tick, output prints in mint with a ding |
| 7 | 3:25 | 0:35 | Concept slide | Recap: four ideas on one card | Four recap lines tick in one by one with a pop; Xecxec nods after each tick |
| 8 | 4:00 | 0:40 | Bug of the Day | BUG OF THE DAY: setprecision without fixed | Butter banner drops in with a buzzer; the program compiles and runs; the wrong output appears in tomato; the fix slides in and the output turns mint with a ding |
| 9 | 4:40 | 0:09 | Pun card | setprecision without fixed is like a Goa thali with no rice: something important is missing. | Full tomato screen, card flips in with a rimshot, Xecxec snaps his claw |
| 10 | 4:49 | 0:20 | Challenge | Task card: a three-row price table | Task card pops in; checklist ticks with a pop; Xecxec holds a tiny pen |
| 11 | 5:09 | 0:15 | Outro | Next: Module 2 · Making decisions | Next-episode card slides up with a whoosh; right side stays empty for end-screen elements; sign-off text types in |

### Narration script

**[1 · Title]** Your numbers are correct, but do they look good? Today we make output tidy, with neat columns and exactly the number of decimals we want, using a header called iomanip.

**[2 · Why format?]** Raw output is honest but untidy. Prices of different lengths wobble out of line, and decimals run on. Include iomanip, and you get tools. Setw sets the width of the next item. Left and right choose which side the text sticks to. Fixed tells cout to count decimals after the point. And setprecision says how many. Think of a menu board at a shack. A tidy board sells more fish.

**[3 · A price list]** [HL 7] Fixed and setprecision two, set once, stay for the rest of the program. Every double now shows two decimals. [HL 8] The header row. Left and setw ten, so Item sits in a ten-wide column, pushed to the left. Then right and setw eight, so Price sits in an eight-wide column, pushed to the right. [HL 9] Same pattern for Fish and its price. [HL 10] And again for Prawns.

**[4 · Width and precision]** Setw reserves boxes. Ten boxes for the name, and the word Fish fills four of them. Left alignment pushes it to the start, and the spare six stay empty. Eight boxes for the price. The number two hundred forty-nine point five zero fills six, and right alignment pushes it to the end. Setw only affects the very next item, which is why we repeat it on every column.

**[5 · Run it in your head]** [HL 6] [TRACK price=249.5] Price is two hundred forty-nine point five. [HL 7] From here on, doubles show two decimals. [HL 8] The header is Item, then Price on the right edge. [HL 9] Fish and two hundred forty-nine point five zero. Notice the extra zero, added by fixed. [HL 10] And Prawns with three hundred ninety-nine point zero zero.

**[6 · Compile and run]** Compile and run. A tidy table appears. Names line up on the left. Prices line up on the right, each with two decimals. That is the same data as before, but now it is easy to read.

**[7 · Recap]** Recap. One: include iomanip to format output. Two: setw reserves a width, and works only on the very next item. Three: left and right choose the side the text sticks to. Four: fixed with setprecision gives an exact number of decimals. Without fixed, setprecision counts all digits. Print a price list of your own, and make the columns line up.

**[8 · Bug of the Day]** Bug of the Day. We want pi with two decimals, so we write setprecision two. It prints three point one. Only two digits in total! Without fixed, setprecision counts all digits, before and after the point. Add fixed, and setprecision counts only the digits after the point. Now the output is three point one four. No error, so you have to notice the output.

**[9 · Pun]** Setprecision without fixed is like a Goa thali with no rice. Something important is missing.

**[10 · Challenge]** Your challenge: print a table with three items. Names on the left, prices on the right, every price with two decimals. Comment your answer below.

**[11 · Outro]** Module one is done! Next time: making decisions with if and else. Keep coding, says Xecxec!

### Code shown

File 1: `menu.cpp` (scene 3, 5)

```cpp
#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    double price = 249.5;
    cout << fixed << setprecision(2);
    cout << left << setw(10) << "Item" << right << setw(8) << "Price" << endl;
    cout << left << setw(10) << "Fish" << right << setw(8) << price << endl;
    cout << left << setw(10) << "Prawns" << right << setw(8) << 399.0 << endl;
    return 0;
}
```

**Expected output:**

```text
Item         Price
Fish        249.50
Prawns      399.00
```

### Bug of the Day

Wrong code (setprecision(2) without fixed):

```cpp
#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    double pi = 3.14159;
    cout << setprecision(2) << pi << endl;
    return 0;
}
```

GCC and program output:

```text
Output when run:
3.1
```

Fixed code (fixed added before setprecision):

```cpp
#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    double pi = 3.14159;
    cout << fixed << setprecision(2) << pi << endl;
    return 0;
}
```

Output of the fixed code:

```text
3.14
```

**Why:** Without fixed, setprecision(2) means two digits in total; with fixed it means two digits after the decimal point.

### Pun & challenge

- **Pun:** "setprecision without fixed is like a Goa thali with no rice: something important is missing."
- **Challenge:** Print a table with three items, names on the left and prices on the right, every price with two decimals.
- **Challenge answer:** Use fixed << setprecision(2), then left << setw(10) for names and right << setw(8) for prices.

### Shorts for EP 12

**S1 · Why format output?** — 0:20 · built from scene 2

- **Hook (first 1.5s):** "Correct numbers can still look messy."
- **Script:** Correct numbers can still look messy. Include iomanip and use setw for width, left and right for sides, fixed and setprecision for decimals. A tidy menu board sells more fish.
- **On-screen text:** SETW  FIXED  SETPRECISION
- **Caption + hashtags:** Make output tidy. #cpp #iomanip #beginners #kodingkonkani #learntocode

**S2 · A price list in code** — 0:20 · built from scene 3

- **Hook (first 1.5s):** "Names left, prices right."
- **Script:** Names left, prices right. Left and setw ten for the name. Right and setw eight for the price. Fixed and setprecision two set the decimals once for the whole program.
- **On-screen text:** LEFT + SETW(10), RIGHT + SETW(8)
- **Caption + hashtags:** Build a price list. #cpp #setw #coding #kodingkonkani #beginners

**S3 · How setw works** — 0:20 · built from scene 4

- **Hook (first 1.5s):** "Setw reserves boxes."
- **Script:** Setw reserves boxes. Ten boxes for a name. The word fills four. Left alignment keeps it at the start. Remember, setw affects only the very next item.
- **On-screen text:** SETW = RESERVED WIDTH
- **Caption + hashtags:** Width applies to one item. #cpp #setw #programming #kodingkonkani #learntocode

**S4 · setprecision needs fixed** — 0:20 · built from scene 8

- **Hook (first 1.5s):** "Two decimals gave me three point one."
- **Script:** Two decimals gave me three point one. Set precision two without fixed counts all digits, so pi becomes three point one. Add fixed, and you get three point one four.
- **On-screen text:** SETPRECISION(2) -> 3.1
- **Caption + hashtags:** Always pair it with fixed. #cpp #bugfix #setprecision #kodingkonkani #coding

**S5 · Pun and challenge** — 0:20 · built from scenes 9, 10

- **Hook (first 1.5s):** "A thali with no rice."
- **Script:** A thali with no rice. Setprecision without fixed is missing something important. Your challenge: print a three-row price table with two decimals. Full video: EP 12.
- **On-screen text:** 3-ROW PRICE TABLE
- **Caption + hashtags:** Try the challenge. #cpp #codingchallenge #kodingkonkani #programmingjokes #goa
