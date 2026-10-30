# Module 13 — Projects & finale

Episodes 84–86 · Peach + Lilac

## EP 84 — Project: Student Record System

**Module 13 · Projects & finale · 8:00 · Peach + Lilac · Prerequisite: EP 83**

**Learning goals:** combine a `typedef struct`, an array of structs, functions and binary files into one working program; build a menu loop that survives bad input; save records with `fwrite` and load them back with `fread` so data survives a restart; add a new feature (search) to an existing program.

### YouTube

- **Title:** Build a Student Record System in C | C Programming EP 84
- **Description:** Your college office keeps student records. Today you build that system in C: add students, list them in a neat table, and keep them saved to a file even after you close the program. Full code included, explained line by line. Chapters: 0:00 Your college office, in C · 0:20 The plan · 0:55 The Student struct · 1:35 Saving and loading · 2:55 Adding a student · 4:00 Showing all · 4:35 The menu loop · 5:25 Demo · 6:10 Bug of the Day · 7:20 Challenge
- **Tags:** c project, student record system in c, c mini project, struct and file handling c, fwrite fread c, menu driven program c, c programming project for students, learn c, koding konkani, class 12 computer project, c project with source code, gcc
- **Thumbnail:** big text "BUILD THIS IN C"; a terminal table with Roll / Name / Marks rows and a floppy-disk save icon; Xecxec wearing a college office clerk's spectacles with a pen behind his ear; peach background, lilac accents

### Scene list

| # | Start | Length | Template | On screen | Animation & SFX |
| --- | --- | --- | --- | --- | --- |
| 1 | 0:00 | 0:15 | Terminal | Finished program running: menu, add a student, table prints; program closed and reopened, data still there | Typing SFX; table rows slide in; "still there!" sparkle |
| 2 | 0:15 | 0:05 | Title card | EP 84 · PROJECT: STUDENT RECORD SYSTEM | Tiles slam in; claw-click |
| 3 | 0:20 | 0:35 | Concept slide | Plan diagram: Student struct → array `list[50]` → functions (load, save, add, show) → file `students.dat`; small badges linking each part to its earlier episode (EP 34, 61, 62, 71) | Boxes pop in, arrows draw; tick SFX |
| 4 | 0:55 | 0:40 | Code explain | `students.c` lines 1–14 | Butter highlights; struct drawn as an ID card |
| 5 | 1:35 | 1:20 | Code explain | Lines 16–38: loadRecords, saveRecords, clearInput | Butter highlights; file icon opens/closes; records fly to and from disk |
| 6 | 2:55 | 1:05 | Code explain | Lines 40–59: addStudent | Butter highlights; tracker for s.roll, s.name, s.marks, count |
| 7 | 4:00 | 0:35 | Code explain | Lines 61–70: showAll | Columns line up as `%-6d` / `%-20s` widths are drawn |
| 8 | 4:35 | 0:50 | Code explain | Lines 72–91: main and the menu loop | Butter highlights; loop arrow cycles around the switch |
| 9 | 5:25 | 0:40 | Terminal | Full demo session (run 1 and run 2) | Typing SFX; mint tick when data reappears |
| 10 | 6:05 | 0:05 | Pun card | Pun | Drum hit; Xecxec stamping a report card |
| 11 | 6:10 | 1:10 | Bug of the Day | `menubug.c`: typing `x` makes the menu loop forever | Text floods the terminal, scroll speeds up; Xecxec gets buried; fix freezes it, mint tick |
| 12 | 7:20 | 0:25 | Challenge | Challenge card: add "3. Search by roll number" | Timer ticks |
| 13 | 7:45 | 0:15 | Outro | Next: EP 85 · Bank / ATM simulator | ATM screen glowing; sign-off jingle |

### Narration script

**\[1 · Cold open\]** This is your college office, in C. Add a student. Show everyone in a neat table. Close the program. Open it again, and the records are still there. By the end of this video, you will have built all of it yourself.

**\[2 · Title\]** Episode 84. Project: student record system.

**\[3 · The plan\]** Here's the plan. Each student is a struct with a roll number, a name and marks, like the ID card from EP 61. We keep up to 50 of them in an array of structs, the class register from EP 62. Four small functions do the work: load, save, add and show. And a binary file, students dot dat, keeps the data safe between runs, just like EP 71. Nothing new today. Every piece is something you already know. A project is just the pieces, put together.

**\[4 · The struct\]** \[HL 1-2\] Lines one and two: stdio for input and output, string dot h for strcspn, which we'll use to clean the name. \[HL 4\] Line four: hash define MAX 50, the most students we can store. \[HL 5\] Line five: the file name, in one place, so we never mistype it. \[HL 7-11\] Lines seven to eleven: typedef struct, with int roll, char name of 40, and float marks. Thanks to typedef from EP 63, we can just write Student. \[HL 13\] Line thirteen: Student list of MAX, our register. \[HL 14\] Line fourteen: int count equals 0, how many students are actually stored. These two are global, because every function needs them. In a bigger program you'd pass them as parameters, but for one file, this keeps the code simple.

**\[5 · Saving and loading\]** \[HL 16\] loadRecords. \[HL 17\] Line seventeen opens the file in r b mode: read, binary. \[HL 18-20\] If fp is NULL, the file doesn't exist yet. That's normal on the very first run, so we just return with zero students. \[HL 21\] Line twenty-one is the clever bit. fread reads up to MAX records of size Student into list, and it returns how many it actually read. We store that straight into count. \[HL 22\] Close the file. \[HL 25\] Now saveRecords. \[HL 26\] w b mode: write, binary. This replaces the old file with a fresh copy. \[HL 27-30\] If it fails, we tell the user. Always check fopen, that was EP 69's bug. \[HL 31\] fwrite writes count records from list in one go. \[HL 32\] Close. \[HL 35-38\] And clearInput: it reads and throws away characters until the end of the line. After scanf reads a number, the Enter key is still waiting in the input. clearInput cleans it up. Remember this little function; it saves us in the Bug of the Day.

**\[6 · Adding a student\]** \[HL 40\] addStudent. \[HL 41-44\] First, if count equals MAX, the register is full, so we stop. \[HL 45\] A temporary Student, s. \[HL 46-48\] Ask for the roll number, read it with scanf, \[TRACK s.roll=101\] and clear the leftover Enter. \[HL 49-50\] For the name, we use fgets, not scanf, because names have spaces, like Riya Naik. fgets reads the whole line, up to the size of the array, so it can't overflow. \[HL 51\] fgets keeps the newline at the end, so strcspn finds it and we replace it with the end-of-string character. \[TRACK s.name="Riya Naik"\] \[HL 52-54\] Read the marks \[TRACK s.marks=88.5\] and clear the line again. \[HL 55\] list of count equals s copies the whole struct into the next free slot. \[HL 56\] count plus plus. \[TRACK count=1\] \[HL 57\] Save straight away, so nothing is lost if the power goes during a Goa monsoon storm. \[HL 58\] Confirm with "Saved Riya Naik".

**\[7 · Showing all\]** \[HL 61-65\] showAll. If there are no students, say so and return. \[HL 66\] Print the heading. Percent minus 6 s means: a string, 6 characters wide, left-aligned. \[HL 67-69\] Then a for loop prints every record with the same widths, so the columns line up like a real table. Marks get percent point 1 f, one decimal place.

**\[8 · The menu loop\]** \[HL 72-74\] main. choice starts at zero, and the first thing we do is load the saved records. \[HL 75\] A do-while loop, from EP 28, because the menu must show at least once. \[HL 76\] Print the menu. \[HL 77\] Here's the safety net. scanf returns how many values it read. If it isn't 1, the user typed something that isn't a number. \[HL 78-80\] So we clear the line, complain politely, and continue, which jumps back to the top of the loop. \[HL 82\] Otherwise clear the Enter key. \[HL 83-88\] The switch from EP 23 calls the right function. \[HL 89\] And we keep looping while choice isn't 3.

**\[9 · Demo\]** Compile it: gcc students dot c, dash o, students. Run it. Choice 1: roll 101, Riya Naik, 88.5. Saved. Choice 1 again: roll 102, Sanjay Gaonkar, 76. Choice 2: a neat table. Now let's be a naughty user and type a b c. "Please type a number." No crash. Choice 3, bye. Now run it again and pick 2. Both students are still there, loaded from students dot dat. That's a real, working program.

**\[10 · Pun\]** Why did the student record system pass every exam? Because it always kept its marks in order.

**\[11 · Bug of the Day\]** Today's bug: the messy menu loop. Here's a simpler menu without our safety net. It just calls scanf and goes into the switch. Type 1 and it works. But type the letter x, and the screen fills with "Pick 1, 2 or 3", forever. Why? scanf with percent d sees the x, can't turn it into a number, and leaves the x in the input. choice stays 0. The loop comes back, scanf sees the same x again, fails again. Forever. The program never waits for you. No compiler can warn you about this; it only happens at run time. The fix is the three lines you saw in main: check that scanf returned 1, and if not, clear the bad input with clearInput and continue. Rule: never trust user input. Always check what scanf returns.

**\[12 · Challenge\]** Your challenge: add a search feature. Change the menu to four options, with 3 being "Search", and write a function searchByRoll that asks for a roll number, loops through the list, and prints the student's name and marks, or "No student with roll" and the number. Remember to change Exit to option 4 in the loop condition too.

**\[13 · Outro\]** Next episode: our second project. A bank ATM simulator, with deposits, withdrawals, and a lot of checking. Keep coding, says Xecxec!

### Code shown

Full program, `students.c` (91 lines):

```c
#include <stdio.h>
#include <string.h>

#define MAX 50
#define FILENAME "students.dat"

typedef struct {
    int roll;
    char name[40];
    float marks;
} Student;

Student list[MAX];
int count = 0;

void loadRecords(void) {
    FILE *fp = fopen(FILENAME, "rb");
    if (fp == NULL) {
        return;                     // first run: no file yet
    }
    count = fread(list, sizeof(Student), MAX, fp);
    fclose(fp);
}

void saveRecords(void) {
    FILE *fp = fopen(FILENAME, "wb");
    if (fp == NULL) {
        printf("Could not save!\n");
        return;
    }
    fwrite(list, sizeof(Student), count, fp);
    fclose(fp);
}

void clearInput(void) {
    int c;
    while ((c = getchar()) != '\n' && c != EOF) { }
}

void addStudent(void) {
    if (count == MAX) {
        printf("Register is full.\n");
        return;
    }
    Student s;
    printf("Roll number: ");
    scanf("%d", &s.roll);
    clearInput();
    printf("Name: ");
    fgets(s.name, sizeof(s.name), stdin);
    s.name[strcspn(s.name, "\n")] = '\0';
    printf("Marks: ");
    scanf("%f", &s.marks);
    clearInput();
    list[count] = s;
    count++;
    saveRecords();
    printf("Saved %s.\n", s.name);
}

void showAll(void) {
    if (count == 0) {
        printf("No records yet.\n");
        return;
    }
    printf("%-6s %-20s %s\n", "Roll", "Name", "Marks");
    for (int i = 0; i < count; i++) {
        printf("%-6d %-20s %.1f\n", list[i].roll, list[i].name, list[i].marks);
    }
}

int main(void) {
    int choice = 0;
    loadRecords();
    do {
        printf("\n1. Add  2. Show all  3. Exit\nChoice: ");
        if (scanf("%d", &choice) != 1) {
            clearInput();
            printf("Please type a number.\n");
            continue;
        }
        clearInput();
        switch (choice) {
            case 1: addStudent(); break;
            case 2: showAll();    break;
            case 3: printf("Bye!\n"); break;
            default: printf("Pick 1, 2 or 3.\n");
        }
    } while (choice != 3);
    return 0;
}
```

Build: `gcc students.c -o students` (compiles clean with `-Wall -Wextra`).

**Expected output, run 1** (user input shown after each prompt; starting with no `students.dat`):

```text
1. Add  2. Show all  3. Exit
Choice: 1
Roll number: 101
Name: Riya Naik
Marks: 88.5
Saved Riya Naik.

1. Add  2. Show all  3. Exit
Choice: 1
Roll number: 102
Name: Sanjay Gaonkar
Marks: 76
Saved Sanjay Gaonkar.

1. Add  2. Show all  3. Exit
Choice: 2
Roll   Name                 Marks
101    Riya Naik            88.5
102    Sanjay Gaonkar       76.0

1. Add  2. Show all  3. Exit
Choice: abc
Please type a number.

1. Add  2. Show all  3. Exit
Choice: 3
Bye!
```

**Run 2** (data loaded from `students.dat`):

```text
1. Add  2. Show all  3. Exit
Choice: 2
Roll   Name                 Marks
101    Riya Naik            88.5
102    Sanjay Gaonkar       76.0

1. Add  2. Show all  3. Exit
Choice: 3
Bye!
```

Note: `students.dat` is binary; opening it in Notepad shows unreadable characters, and its size depends on the machine's struct layout (on screen: "don't edit this file by hand").

### Bug of the Day

Wrong code (`menubug.c`):

```c
#include <stdio.h>

int main(void) {
    int choice = 0;
    do {
        printf("1. Add  2. Show all  3. Exit\nChoice: ");
        scanf("%d", &choice);
        switch (choice) {
            case 1: printf("Adding...\n"); break;
            case 2: printf("Showing...\n"); break;
            case 3: printf("Bye!\n"); break;
            default: printf("Pick 1, 2 or 3.\n");
        }
    } while (choice != 3);
    return 0;
}
```

Compiles with no warning. Typing `x` gives endless output (stop it with Ctrl+C):

```text
1. Add  2. Show all  3. Exit
Choice: x
Pick 1, 2 or 3.
1. Add  2. Show all  3. Exit
Choice: Pick 1, 2 or 3.
1. Add  2. Show all  3. Exit
Choice: Pick 1, 2 or 3.
...
```

Fixed code:

```c
#include <stdio.h>

void clearInput(void) {
    int c;
    while ((c = getchar()) != '\n' && c != EOF) { }
}

int main(void) {
    int choice = 0;
    do {
        printf("1. Add  2. Show all  3. Exit\nChoice: ");
        if (scanf("%d", &choice) != 1) {
            clearInput();
            printf("Please type a number.\n");
            continue;
        }
        clearInput();
        switch (choice) {
            case 1: printf("Adding...\n"); break;
            case 2: printf("Showing...\n"); break;
            case 3: printf("Bye!\n"); break;
            default: printf("Pick 1, 2 or 3.\n");
        }
    } while (choice != 3);
    return 0;
}
```

```text
1. Add  2. Show all  3. Exit
Choice: x
Please type a number.
1. Add  2. Show all  3. Exit
Choice: 3
Bye!
```

Why: when `scanf("%d")` fails it leaves the bad character in the input, so every later `scanf` fails on the same character; checking the return value and clearing the line breaks the cycle.

### Pun & challenge

- **Pun:** Why did the student record system pass every exam? It always kept its marks in order.
- **Challenge:** Add menu option 3, "Search", with a function `searchByRoll` that prints the matching student or "No student with roll N."; move Exit to option 4.
- **Challenge answer:** add this function above `main`:

```c
void searchByRoll(void) {
    int roll;
    printf("Roll to find: ");
    scanf("%d", &roll);
    clearInput();
    for (int i = 0; i < count; i++) {
        if (list[i].roll == roll) {
            printf("Found: %s, %.1f marks\n", list[i].name, list[i].marks);
            return;
        }
    }
    printf("No student with roll %d.\n", roll);
}
```

Then in `main`: menu text `"\n1. Add  2. Show all  3. Search  4. Exit\nChoice: "`, add `case 3: searchByRoll(); break;`, change Exit to `case 4`, the default message to `"Pick 1 to 4.\n"`, and the loop to `while (choice != 4)`.

```text
1. Add  2. Show all  3. Search  4. Exit
Choice: 3
Roll to find: 102
Found: Sanjay Gaonkar, 76.0 marks

1. Add  2. Show all  3. Search  4. Exit
Choice: 3
Roll to find: 999
No student with roll 999.
```

### Shorts for EP 84

**S1 · Your College Office, in C** — 0:30 · built from scenes 1 and 9

- **Hook (first 1.5s):** a student table appearing in the terminal, then the program closing
- **Script:** Add a student. Show a neat table. Close the program. Open it again. The records are still there. This is a full student record system in C, about 90 lines, built from structs, functions and a binary file. Full code and line-by-line explanation in episode 84.
- **On-screen text:** CLOSE IT. REOPEN. STILL THERE.
- **Caption + hashtags:** Your first real C project, start to finish. #cprogramming #cproject #kodingkonkani #learntocode #studentproject

**S2 · Saving Structs in 30 Seconds** — 0:35 · built from scene 5

- **Hook (first 1.5s):** records flying from the screen into a file icon
- **Script:** Saving an array of structs takes one line: fwrite, the array, the size of one struct, how many, and the file. Loading takes one line too: fread returns how many records it read, so you store that straight into count. Open with w b to save and r b to load. Always check fopen for NULL.
- **On-screen text:** fwrite TO SAVE · fread TO LOAD
- **Caption + hashtags:** Make your C data survive a restart. #cprogramming #filehandling #kodingkonkani #learntocode #ctutorial

**S3 · The Menu That Never Stops** — 0:40 · built from scene 11

- **Hook (first 1.5s):** terminal flooding with "Pick 1, 2 or 3."
- **Script:** Type a letter into this menu, and it goes crazy. Why? scanf can't read x as a number, so it leaves the x in the input. Next loop, same x, same failure. Forever. The fix: check that scanf returned 1. If it didn't, throw away the rest of the line and continue. Never trust user input.
- **On-screen text:** ONE LETTER. INFINITE LOOP.
- **Caption + hashtags:** The bug that breaks every beginner menu. #cprogramming #debugging #kodingkonkani #scanf #learntocode

**S4 · Marks in Order** — 0:12 · built from scene 10

- **Hook (first 1.5s):** Xecxec stamping "PASS" on a report card
- **Script:** Why did the student record system pass every exam? Because it always kept its marks in order.
- **On-screen text:** KEPT ITS MARKS IN ORDER
- **Caption + hashtags:** Top of the class. #codingmemes #programmerhumor #kodingkonkani #cprogramming #learntocode

**S5 · Quiz: Why fgets for Names?** — 0:25 · built from scene 6

- **Hook (first 1.5s):** "Riya Naik" typed in, only "Riya" saved
- **Script:** Why does the program read names with fgets instead of scanf percent s? A: fgets is faster. B: scanf percent s stops at the first space. C: scanf can't read strings. The answer is B. With scanf, Riya Naik becomes just Riya. fgets reads the whole line.
- **On-screen text:** A · B · C — WHY fgets?
- **Caption + hashtags:** Comment your answer before the reveal. #cprogramming #codingquiz #kodingkonkani #learntocode #strings

## EP 85 — Project: Bank / ATM Simulator

**Module 13 · Projects & finale · 8:00 · Peach + Lilac · Prerequisite: EP 84**

**Learning goals:** design a program as small functions that take a value and return the updated value (no globals); validate every input (not a number, negative, zero, too large) before using it; persist a single value in a text file with `fprintf` / `fscanf`; add a PIN check with a limited number of tries.

### YouTube

- **Title:** Build an ATM in C (Without Breaking the Bank) | EP 85
- **Description:** Withdraw minus 5000 rupees and get richer? Not in our ATM. We build a full bank ATM simulator in C with balance, deposit and withdraw, save the balance to a file, and validate every single input. Full code, explained line by line. Chapters: 0:00 Withdraw without breaking the bank · 0:20 The plan · 0:50 Saving the balance · 2:00 Reading a safe amount · 3:05 Deposit and withdraw · 4:15 The menu · 4:50 Demo · 5:40 Bug of the Day · 7:00 Challenge
- **Tags:** c project, atm program in c, bank management system c, c mini project, input validation c, file handling c, menu driven program c, c project with source code, learn c, koding konkani, class 12 computer project, gcc
- **Thumbnail:** big text "BUILD AN ATM"; an ATM screen showing "Rs -40000.00" in tomato with a big cross; Xecxec in a security-guard cap blocking the slot; peach background, lilac accents

### Scene list

| # | Start | Length | Template | On screen | Animation & SFX |
| --- | --- | --- | --- | --- | --- |
| 1 | 0:00 | 0:20 | Terminal | A broken ATM: withdraw -5000, balance goes UP to 15000; withdraw 50000, balance -40000 | Cash-register "cha-ching" then alarm siren; Xecxec faints |
| 2 | 0:20 | 0:05 | Title card | EP 85 · PROJECT: BANK / ATM SIMULATOR | Tiles slam in; claw-click |
| 3 | 0:25 | 0:25 | Concept slide | Plan: `balance` lives in main → passed into deposit/withdraw → new balance returned → saved to `balance.txt`. Rule card: "Never trust input" | Arrows loop from main to function and back; stamp SFX on the rule |
| 4 | 0:50 | 1:10 | Code explain | `atm.c` lines 1–26: constants, loadBalance, saveBalance | Butter highlights; text file icon shows `12500.00` inside |
| 5 | 2:00 | 1:05 | Code explain | Lines 28–44: clearInput, readAmount | Butter highlights; bad inputs (abc, -50, 0) bounce off a shield |
| 6 | 3:05 | 1:10 | Code explain | Lines 46–62: deposit, withdraw | Butter highlights; tracker for balance and amount; MIN\_BALANCE line drawn on a bar |
| 7 | 4:15 | 0:35 | Code explain | Lines 64–85: main | Butter highlights; loop arrow around the switch |
| 8 | 4:50 | 0:45 | Terminal | Full demo session | Typing SFX; note notes slide out of an ATM slot on withdraw |
| 9 | 5:35 | 0:05 | Pun card | Pun | Drum hit; Xecxec counting cash |
| 10 | 5:40 | 1:20 | Bug of the Day | `atmbug.c`: no validation; negative and huge withdrawals; fixed version | Balance counter spins the wrong way; fix shows checks as gates, mint tick |
| 11 | 7:00 | 0:45 | Challenge | Challenge card: 4-digit PIN, 3 tries, then "Card blocked" | Keypad beeps; timer ticks |
| 12 | 7:45 | 0:15 | Outro | Next: EP 86 · Finale | Graduation cap drops onto Xecxec; sign-off jingle |

### Narration script

**\[1 · Cold open\]** Welcome to the worst ATM in Goa. Balance: 10,000 rupees. Let's withdraw minus 5,000. "Please collect minus 5,000". And the balance goes up to 15,000! Now withdraw 50,000. Balance: minus 40,000. The bank manager has fainted. Today we build an ATM that checks everything.

**\[2 · Title\]** Episode 85. Project: bank ATM simulator.

**\[3 · The plan\]** Here's the plan. The balance lives in main, as a local variable. When you deposit or withdraw, main passes the balance into a function, and the function returns the new balance. That's call by value from EP 38, used on purpose. No globals this time. After every change, we save the balance to a small text file, so it survives a restart. And one rule above all: never trust input. Every amount gets checked before it touches the balance.

**\[4 · Saving the balance\]** \[HL 3\] Line three: the file name. \[HL 4\] Line four: MIN\_BALANCE, 500 rupees, the minimum the bank wants you to keep. A named constant, from EP 10, instead of a magic number. \[HL 6-7\] loadBalance starts with a default opening balance of 10,000 for the very first run. \[HL 8\] Open balance dot txt for reading. \[HL 9\] If the file exists, \[HL 10-12\] fscanf reads one double with percent l f. If that fails, say someone typed rubbish into the file, we fall back to 10,000. \[HL 13\] Close it. \[HL 15\] Return the balance. \[HL 18\] saveBalance takes the balance as a parameter. \[HL 19-23\] Open for writing, and check for NULL. \[HL 24\] fprintf writes it with two decimal places. Because this is a text file, you can open it in Notepad and read it. That's handy for one number. For many records, like last episode, a binary file is better.

**\[5 · Reading a safe amount\]** \[HL 28-31\] clearInput, the same helper from EP 84. \[HL 33\] readAmount: the security guard of our ATM. Its only job is to return a valid amount. \[HL 35\] while 1 means "keep asking until we get a good answer". \[HL 36\] Ask for the amount. \[HL 37\] Two checks in one line. scanf must return 1, meaning it really read a number, and amount must be greater than zero. Because of the double ampersand, if scanf fails, C doesn't even look at amount. \[HL 38-39\] If both pass, clear the Enter key and return the amount. \[HL 41-42\] If not, clear the bad line and say "Enter a positive number". Then the loop asks again. abc, rejected. Minus 50, rejected. Zero, rejected. Every function that needs an amount calls readAmount, so the checking is written in one place.

**\[6 · Deposit and withdraw\]** \[HL 46\] deposit takes the current balance. \[HL 47\] Gets a safe amount from readAmount. \[TRACK amount=2500\] \[HL 48\] Adds it. \[TRACK balance=12500\] \[HL 49-50\] Prints a receipt and returns the new balance. \[HL 53\] withdraw also takes the balance. \[HL 54\] Safe amount again. \[HL 55\] The second check: would the balance drop below 500? \[TRACK amount=20000\] If balance minus amount is less than MIN\_BALANCE, \[HL 56-57\] decline, and return the balance unchanged. \[HL 59-61\] Otherwise subtract, say "Please collect", and return the new balance. \[TRACK amount=4000\] \[TRACK balance=8500\] One honest note: we use double for money to keep this simple. Real banking software stores paise as whole numbers, because decimals can't always be stored exactly. You saw that kind of rounding in EP 08.

**\[7 · The menu\]** \[HL 65\] main loads the balance once. \[HL 67\] Welcome message. \[HL 68-75\] The same safe menu loop from EP 84: check that scanf read a number, otherwise clear and continue. \[HL 77\] Option 1 prints the balance. \[HL 78\] Option 2: balance equals deposit of balance, then save. See how the returned value is stored back into balance? Without that assignment, the deposit would vanish, exactly like EP 38's bug. \[HL 79\] Option 3, the same for withdraw. \[HL 80\] Option 4 says goodbye. \[HL 83\] Loop until 4.

**\[8 · Demo\]** Compile with gcc atm dot c, dash o, atm, and run. Check balance: 10,000. Deposit 2,500. Now withdraw, and try to break it. Minus 50: rejected. a b c: rejected. 20,000: declined, you must keep 500. 4,000: please collect. Balance: 8,500. Exit, and open balance dot txt: 8500 point 00, saved. Run it again, and the ATM remembers.

**\[9 · Pun\]** Why did the ATM need a break? It had too many withdrawals and no deposit of energy left.

**\[10 · Bug of the Day\]** Today's bug: no input validation. Here's the ATM from the cold open, cut down. It reads the amount with scanf and subtracts it. No checks at all. The compiler is perfectly happy, even with dash Wall. It is valid C. It's just a terrible ATM. Minus 5,000 makes the balance go up to 15,000. 50,000 makes it minus 40,000. And type letters, and scanf fails, amount stays unset, and you get garbage. The fix adds two gates. Gate one: if scanf didn't return 1, or the amount is zero or less, print "Invalid amount" and stop. Gate two: if the amount is more than the balance minus 500, print "Declined". Only after both gates do we touch the balance. In real software, most security problems start right here: with input nobody checked.

**\[11 · Challenge\]** Your challenge: add a PIN check. Write a function checkPin that allows three tries to enter the PIN 4321. It returns 1 if the PIN is right, and 0 after three wrong tries. In main, call it before the menu. If it returns 0, print "Card blocked. Visit your branch." and end the program. Hint: a for loop from 1 to 3, and remember to clear the input after each try.

**\[12 · Outro\]** Two projects done! Next episode is the grand finale: exam prep, the questions examiners love, and a sneak peek at what comes after C. Keep coding, says Xecxec!

### Code shown

Full program, `atm.c` (85 lines):

```c
#include <stdio.h>

#define BALANCE_FILE "balance.txt"
#define MIN_BALANCE 500.0

double loadBalance(void) {
    double balance = 10000.0;          // opening balance on first run
    FILE *fp = fopen(BALANCE_FILE, "r");
    if (fp != NULL) {
        if (fscanf(fp, "%lf", &balance) != 1) {
            balance = 10000.0;
        }
        fclose(fp);
    }
    return balance;
}

void saveBalance(double balance) {
    FILE *fp = fopen(BALANCE_FILE, "w");
    if (fp == NULL) {
        printf("Warning: could not save balance.\n");
        return;
    }
    fprintf(fp, "%.2f\n", balance);
    fclose(fp);
}

void clearInput(void) {
    int c;
    while ((c = getchar()) != '\n' && c != EOF) { }
}

double readAmount(void) {
    double amount;
    while (1) {
        printf("Amount (Rs): ");
        if (scanf("%lf", &amount) == 1 && amount > 0) {
            clearInput();
            return amount;
        }
        clearInput();
        printf("Enter a positive number.\n");
    }
}

double deposit(double balance) {
    double amount = readAmount();
    balance += amount;
    printf("Deposited Rs %.2f\n", amount);
    return balance;
}

double withdraw(double balance) {
    double amount = readAmount();
    if (balance - amount < MIN_BALANCE) {
        printf("Declined: keep at least Rs %.2f in the account.\n", MIN_BALANCE);
        return balance;
    }
    balance -= amount;
    printf("Please collect Rs %.2f\n", amount);
    return balance;
}

int main(void) {
    double balance = loadBalance();
    int choice = 0;
    printf("Welcome to Xecxec Bank ATM\n");
    do {
        printf("\n1. Balance  2. Deposit  3. Withdraw  4. Exit\nChoice: ");
        if (scanf("%d", &choice) != 1) {
            clearInput();
            printf("Please type a number.\n");
            continue;
        }
        clearInput();
        switch (choice) {
            case 1: printf("Balance: Rs %.2f\n", balance); break;
            case 2: balance = deposit(balance);  saveBalance(balance); break;
            case 3: balance = withdraw(balance); saveBalance(balance); break;
            case 4: printf("Thank you. Visit again!\n"); break;
            default: printf("Pick 1 to 4.\n");
        }
    } while (choice != 4);
    return 0;
}
```

Build: `gcc atm.c -o atm` (compiles clean with `-Wall -Wextra`).

**Expected output** (no `balance.txt` at start; user input shown after each prompt):

```text
Welcome to Xecxec Bank ATM

1. Balance  2. Deposit  3. Withdraw  4. Exit
Choice: 1
Balance: Rs 10000.00

1. Balance  2. Deposit  3. Withdraw  4. Exit
Choice: 2
Amount (Rs): 2500
Deposited Rs 2500.00

1. Balance  2. Deposit  3. Withdraw  4. Exit
Choice: 3
Amount (Rs): -50
Enter a positive number.
Amount (Rs): abc
Enter a positive number.
Amount (Rs): 20000
Declined: keep at least Rs 500.00 in the account.

1. Balance  2. Deposit  3. Withdraw  4. Exit
Choice: 3
Amount (Rs): 4000
Please collect Rs 4000.00

1. Balance  2. Deposit  3. Withdraw  4. Exit
Choice: 1
Balance: Rs 8500.00

1. Balance  2. Deposit  3. Withdraw  4. Exit
Choice: 4
Thank you. Visit again!
```

Contents of `balance.txt` afterwards:

```text
8500.00
```

### Bug of the Day

Wrong code (`atmbug.c`):

```c
#include <stdio.h>

int main(void) {
    double balance = 10000.0;
    double amount;
    printf("Amount to withdraw (Rs): ");
    scanf("%lf", &amount);
    balance -= amount;
    printf("Please collect Rs %.2f\n", amount);
    printf("Balance: Rs %.2f\n", balance);
    return 0;
}
```

No compiler warning, even with `-Wall`. Wrong output for input `-5000`:

```text
Amount to withdraw (Rs): -5000
Please collect Rs -5000.00
Balance: Rs 15000.00
```

For input `50000`:

```text
Amount to withdraw (Rs): 50000
Please collect Rs 50000.00
Balance: Rs -40000.00
```

(For input `abc`, scanf fails and `amount` is never set, so the output is garbage that changes from machine to machine.)

Fixed code:

```c
#include <stdio.h>

int main(void) {
    double balance = 10000.0;
    double amount;
    printf("Amount to withdraw (Rs): ");
    if (scanf("%lf", &amount) != 1 || amount <= 0) {
        printf("Invalid amount.\n");
        return 1;
    }
    if (amount > balance - 500.0) {
        printf("Declined: not enough balance.\n");
        return 1;
    }
    balance -= amount;
    printf("Please collect Rs %.2f\n", amount);
    printf("Balance: Rs %.2f\n", balance);
    return 0;
}
```

```text
Amount to withdraw (Rs): -5000
Invalid amount.
```

```text
Amount to withdraw (Rs): 50000
Declined: not enough balance.
```

```text
Amount to withdraw (Rs): 2000
Please collect Rs 2000.00
Balance: Rs 8000.00
```

Why: the compiler only checks that code is valid C, not that input makes sense, so the program itself must reject non-numbers, non-positive amounts and amounts larger than the allowed balance.

### Pun & challenge

- **Pun:** Why did the ATM need a break? Too many withdrawals, and no deposit of energy left.
- **Challenge:** Add `int checkPin(void)`: three tries to enter PIN 4321, returns 1 on success, 0 after three wrong tries. Call it before the menu; on 0 print "Card blocked. Visit your branch." and end.
- **Challenge answer:** add this function after `clearInput`:

```c
int checkPin(void) {
    const int correctPin = 4321;
    int pin;
    for (int tries = 1; tries <= 3; tries++) {
        printf("Enter PIN: ");
        if (scanf("%d", &pin) == 1 && pin == correctPin) {
            clearInput();
            return 1;
        }
        clearInput();
        printf("Wrong PIN. %d tries left.\n", 3 - tries);
    }
    return 0;
}
```

and right after the welcome `printf` in `main`:

```c
    if (!checkPin()) {
        printf("Card blocked. Visit your branch.\n");
        return 1;
    }
```

```text
Welcome to Xecxec Bank ATM
Enter PIN: 1111
Wrong PIN. 2 tries left.
Enter PIN: 2222
Wrong PIN. 1 tries left.
Enter PIN: 3333
Wrong PIN. 0 tries left.
Card blocked. Visit your branch.
```

(A real ATM never stores the PIN in the program like this; it's fine for practice.)

### Shorts for EP 85

**S1 · The Worst ATM in Goa** — 0:25 · built from scene 1

- **Hook (first 1.5s):** "Withdraw: -5000" and the balance jumping UP
- **Script:** Withdraw minus 5,000 rupees, and your balance goes up to 15,000. Withdraw 50,000, and you're at minus 40,000. This ATM compiles with zero warnings. It's valid C. It just never checks the input. In episode 85, we build one that does.
- **On-screen text:** WITHDRAW -5000 = GET RICH?
- **Caption + hashtags:** Valid code, broken bank. #cprogramming #cproject #kodingkonkani #learntocode #inputvalidation

**S2 · Input Validation in 30 Seconds** — 0:35 · built from scene 5

- **Hook (first 1.5s):** "abc", "-50" and "0" bouncing off a shield
- **Script:** Two checks make input safe. One: did scanf return 1? If not, the user typed something that isn't a number. Two: is the value in range, like greater than zero? If either fails, clear the line and ask again. Put this in one function, readAmount, and call it everywhere. Write the checking once, use it everywhere.
- **On-screen text:** IS IT A NUMBER? IS IT IN RANGE?
- **Caption + hashtags:** Two checks every C program needs. #cprogramming #learntocode #kodingkonkani #scanf #ctutorial

**S3 · The Bug That Robs the Bank** — 0:40 · built from scene 10

- **Hook (first 1.5s):** balance counter spinning to "Rs -40000.00"
- **Script:** This withdraw code reads the amount and subtracts it. No checks. Minus 5,000 adds money. 50,000 sends you negative. Letters give garbage. The fix: gate one, reject anything that isn't a positive number. Gate two, decline if it would drop below the minimum balance. Only then touch the balance.
- **On-screen text:** NO CHECKS = NO BANK
- **Caption + hashtags:** Most security bugs start with unchecked input. #cprogramming #debugging #kodingkonkani #security #learntocode

**S4 · The Tired ATM** — 0:12 · built from scene 9

- **Hook (first 1.5s):** an ATM yawning, Xecxec fanning it
- **Script:** Why did the ATM need a break? It had too many withdrawals and no deposit of energy left.
- **On-screen text:** NO DEPOSIT OF ENERGY
- **Caption + hashtags:** Even machines need a holiday. #codingmemes #programmerhumor #kodingkonkani #cprogramming #learntocode

**S5 · Quiz: Will It Withdraw?** — 0:25 · built from scene 6

- **Hook (first 1.5s):** "Balance 1000. Minimum 500. Withdraw 600?"
- **Script:** Balance is 1,000 rupees. The minimum balance is 500. You try to withdraw 600. What happens? A: Please collect 600. B: Declined. C: Enter a positive number. The answer is B. 1,000 minus 600 is 400, which is below 500.
- **On-screen text:** COLLECT · DECLINED · INVALID?
- **Caption + hashtags:** Comment your answer before the reveal. #cprogramming #codingquiz #kodingkonkani #learntocode #cproject

## EP 86 — Finale: Exam Prep & What's Next

**Module 13 · Projects & finale · 8:00 · Peach + Lilac · Prerequisite: EP 85**

**Learning goals:** revise the 20 questions that come up most in C theory and viva exams, each mapped to its episode; predict the output of classic "trick" snippets (post-increment, integer division, sizeof a string); use a calm 4-step method for output and debugging questions in an exam; see what C++ looks like and know what to learn next.

### YouTube

- **Title:** Xecxec's Final Exam: Top 20 C Questions | C Programming EP 86
- **Description:** The grand finale of Koding Konkani. We revise the 20 C questions examiners love, solve three classic output puzzles, learn a calm method for the exam hall, and take a first look at C++. Take Xecxec's final exam and comment your score! Chapters: 0:00 Xecxec's final exam · 0:20 Look how far you've come · 1:00 Top 20 exam questions · 3:05 Predict the output · 4:30 Bug of the Day: exam panic · 5:45 What's next: C++ · 6:50 Final challenge · 7:30 Thank you
- **Tags:** c programming exam questions, c viva questions, c important questions, c output questions, c programming revision, c to c++, learn c, c for beginners, koding konkani, class 12 computer science exam, first year engineering c, gcc
- **Thumbnail:** big text "FINAL EXAM"; an exam paper with "C" and a big lilac tick; Xecxec in a graduation cap holding a diploma; peach background, lilac accents

### Scene list

| # | Start | Length | Template | On screen | Animation & SFX |
| --- | --- | --- | --- | --- | --- |
| 1 | 0:00 | 0:15 | Concept slide | Exam hall: rows of desks, a clock ticking, Xecxec as invigilator handing out a paper titled "Xecxec's Final Exam" | Clock tick; paper rustle; school bell |
| 2 | 0:15 | 0:05 | Title card | EP 86 · FINALE: EXAM PREP & WHAT'S NEXT | Tiles slam in; claw-click |
| 3 | 0:20 | 0:40 | Concept slide | Course map from EP 01: all 14 module tiles light up one by one in their colour pairs, ending with a "86 / 86" counter | Each tile pings; counter rolls up; confetti burst |
| 4 | 1:00 | 2:05 | Concept slide | Top 20 exam questions, shown 5 at a time on 4 cards; each question has an episode badge (e.g. "EP 38") | Cards flip in; tick SFX per question; Xecxec points at each badge |
| 5 | 3:05 | 1:20 | Code explain | `predict.c` (14 lines), three puzzles revealed one by one | Answer boxes stay blank, 3-second countdown, then fill in mint; tracker for a, b, x, y |
| 6 | 4:25 | 0:05 | Pun card | Pun | Drum hit; Xecxec tosses graduation cap |
| 7 | 4:30 | 1:15 | Bug of the Day | Panic bug: `exam.c` with `if (marks = 40)` printing "Pass" for 35 marks; then the 4-step calm method card | Heartbeat SFX speeds up then slows; GCC warning in butter; fix with `==`, mint tick; 4 steps stamp down |
| 8 | 5:45 | 1:05 | Code explain | Side by side: `hello.c` and `hello.cpp`; then a roadmap: C++, data structures, Python, projects | Lines from C morph into C++; roadmap path drawn along a Goan coastline |
| 9 | 6:50 | 0:40 | Challenge | Final challenge: 3 output questions, "comment your score out of 3" | Timer ticks; scoreboard |
| 10 | 7:30 | 0:30 | Outro | Thank-you card: "86 episodes. You did it." Xecxec waves goodbye on the beach at sunset | Waves; sign-off jingle, extended |

### Narration script

**\[1 · Cold open\]** Pens down. Phones away. Xecxec is your invigilator today, and he takes it very seriously. This is the last episode of Koding Konkani, and it ends the way every good course should: with an exam. Don't worry. You're ready.

**\[2 · Title\]** Episode 86. Finale: exam prep, and what's next.

**\[3 · Look how far you've come\]** Look at this map from EP 01. Back then, every tile was locked. Now look. Basics. Operators. Decisions. Loops. Functions. Arrays. Strings. Nine episodes of pointers. Structures, dynamic memory, files, six sorting algorithms, and two real projects. You went from printing "Hello, World" to building an ATM that refuses to be robbed. Eighty-six episodes. Give yourself a moment. That's real work.

**\[4 · Top 20 exam questions\]** Here are the twenty questions that appear again and again in C theory papers and viva exams. If you can answer all twenty out loud, you're in great shape. Each one has its episode number, so you know exactly where to revise. Card one, the basics. One: what are the steps from source code to a running program? Preprocess, compile, link, run. EP 05. Two: what is the difference between a variable declaration and a definition? EP 36. Three: what is the difference between int, float, char and double, and how big is each? EP 08 and 09. Four: what is the difference between equals and double equals? EP 16. Five: what is the difference between i plus plus and plus plus i? EP 17. Card two, control and functions. Six: when do you use a for loop, a while loop, and a do-while loop? Module 4. Seven: what do break and continue do? Module 4. Eight: what is the difference between call by value and call by reference? EP 38 and EP 55. Nine: what is recursion, and why does it need a base case? EP 39. Ten: what is the difference between local, global and static variables? EP 37. Card three, arrays, strings and pointers. Eleven: how is an array stored in memory, and what happens if you go out of bounds? EP 41. Twelve: why does a string end with backslash zero? Module 7. Thirteen: what is a pointer, and what do the star and ampersand operators do? EP 53 and 54. Fourteen: how are arrays and pointers related? EP 57. Fifteen: what is a NULL pointer, and why must you check for it? EP 59. Card four, the advanced ones. Sixteen: what is the difference between a structure and a union? EP 64. Seventeen: what is the difference between malloc and calloc, and why do you need free? Module 10. Eighteen: what are the file opening modes, like r, w, a, r b and w b? EP 69 and 71. Nineteen: compare bubble, selection and insertion sort, and their Big-O. Module 12. Twenty: what is the difference between linear and binary search, and when can you use binary search? EP 73. Screenshot these cards. That's your revision list.

**\[5 · Predict the output\]** Output questions are where marks are won or lost. Let's do three. Pause before each answer. \[HL 4\] Puzzle one. int a equals 5. \[HL 5\] int b equals a plus plus, plus 2. Post-increment uses the old value first, then adds one. So b is 5 plus 2, \[TRACK b=7\] which is 7, and then \[TRACK a=6\] a becomes 6. \[HL 6\] Output: a equals 6, b equals 7. \[HL 8\] Puzzle two. int x equals 7 divided by 2. Both are integers, so the decimal is thrown away. \[TRACK x=3\] x is 3. \[HL 9\] float y equals 7 divided by 2.0f. Now one side is a float, so \[TRACK y=3.5\] y is 3.5. \[HL 10\] Output: x equals 3, y equals 3.5. \[HL 12\] Puzzle three. char s, empty brackets, equals "Goa". \[HL 13\] What is sizeof s? Three letters, so 3? No! The string also stores the hidden backslash zero at the end. So the answer is 4. A char is always one byte, so this is 4 on every machine. Three puzzles, three classic traps.

**\[6 · Pun\]** Why did Xecxec pass the C exam with full marks? Because he never forgot to return.

**\[7 · Bug of the Day\]** Today's bug isn't in your code. It's in your head: panicking in the exam. You see a question, your heart races, and you write this: if marks equals 40, with a single equals sign. marks is 35, and the program prints "Pass"! Why? A single equals is assignment. It sets marks to 40, and 40 is not zero, so the condition is true. That's EP 16's bug, and panic makes everyone repeat old bugs. GCC with dash Wall even warns: suggest parentheses around assignment used as truth value. In the exam hall there's no compiler, so you need a method instead. Four calm steps. One: breathe, and read the whole question twice. Two: for output questions, draw boxes for every variable, just like our memory boxes, and update them line by line. Three: for every line, ask, "Which bug of the day lives here?" Equals versus double equals, integer division, a missing break, an off-by-one loop. Four: write your answer, then check it once against your boxes. Slow is smooth, and smooth is fast. The fix in the code is just a double equals. The fix in the exam is staying calm.

**\[8 · What's next: C++\]** So what comes after C? Here's a small taste. On the left, C. On the right, C++. Hash include iostream instead of stdio dot h. cout with two less-than signs instead of printf. And look: a type called string, so no more char arrays and backslash zero. Compile it with g plus plus instead of gcc. The output: "Hello from C++, Xecxec!" The good news: almost everything you learned carries straight over. Variables, loops, functions, arrays, pointers, structs: C++ has all of them. On top, it adds classes and objects, and a big library of ready-made tools. Here's a road map. Next, C++ and object-oriented programming. Then data structures, like linked lists, trees and graphs, using the pointers you already understand. Then try another language, like Python, and notice how much easier it feels after C. And keep building projects. Projects teach more than any video.

**\[9 · Final challenge\]** Your final challenge: Xecxec's exam. Three questions, no compiler, only your brain. int i equals 3. Question one: what does printf percent d, i plus plus times 2 print? Question two: on the next line, what does plus plus i times 2 print? Question three: what is 17 mod 5? Write your answers, then check them with the pinned comment. And comment your score out of 3. Xecxec reads every single one.

**\[10 · Thank you\]** That's it. Eighty-six episodes. You came in not knowing what a compiler was, and you leave able to write real programs in one of the most important languages ever made. Thank you for learning with us, from all of us at Koding Konkani. Go build something. And one last time: keep coding, says Xecxec!

### Code shown

File 1: `predict.c`

```c
#include <stdio.h>

int main(void) {
    int a = 5;
    int b = a++ + 2;
    printf("a = %d, b = %d\n", a, b);

    int x = 7 / 2;
    float y = 7 / 2.0f;
    printf("x = %d, y = %.1f\n", x, y);

    char s[] = "Goa";
    printf("sizeof = %zu\n", sizeof(s));
    return 0;
}
```

```text
a = 6, b = 7
x = 3, y = 3.5
sizeof = 4
```

File 2: `hello.cpp` (shown beside the EP 04 `hello.c`)

```cpp
#include <iostream>
using namespace std;

int main() {
    string name = "Xecxec";
    cout << "Hello from C++, " << name << "!" << endl;
    return 0;
}
```

Build and run (g++ is installed alongside gcc in MSYS2 UCRT64 if `mingw-w64-ucrt-x86_64-gcc` was installed in EP 03):

```bash
g++ hello.cpp -o hello
./hello
```

```text
Hello from C++, Xecxec!
```

### Bug of the Day

Wrong code (`exam.c`):

```c
#include <stdio.h>

int main(void) {
    int marks = 35;
    if (marks = 40) {
        printf("Pass\n");
    }
    return 0;
}
```

`gcc -Wall exam.c -o exam` warns but still builds:

```text
exam.c: In function 'main':
exam.c:5:9: warning: suggest parentheses around assignment used as truth value [-Wparentheses]
    5 |     if (marks = 40) {
      |         ^~~~~
```

Wrong output:

```text
Pass
```

Fixed code:

```c
#include <stdio.h>

int main(void) {
    int marks = 35;
    if (marks >= 40) {
        printf("Pass\n");
    } else {
        printf("Try again\n");
    }
    return 0;
}
```

```text
Try again
```

Why: a single `=` assigns 40 to `marks` and the condition becomes 40, which is true; a comparison needs `==` (or `>=` for a pass mark), and under exam pressure the 4-step calm method catches it.

The 4-step calm method (scene 7 card):

1. Breathe and read the question twice.
2. Draw a box for every variable and update it line by line.
3. For every line, ask which Bug of the Day could live there.
4. Write the answer, then check it once against your boxes.

### Pun & challenge

- **Pun:** Why did Xecxec pass the C exam with full marks? He never forgot to return.
- **Challenge:** Without running it, predict all three lines, then comment your score out of 3:

```c
#include <stdio.h>

int main(void) {
    int i = 3;
    printf("%d\n", i++ * 2);
    printf("%d\n", ++i * 2);
    printf("%d\n", 17 % 5);
    return 0;
}
```

- **Challenge answer:** line 1 uses the old value 3, so 3 × 2 = 6 (then i becomes 4); line 2 increments first to 5, so 5 × 2 = 10; line 3: 17 = 3 × 5 + 2, so the remainder is 2.

```text
6
10
2
```

### Shorts for EP 86

**S1 · Xecxec's Final Exam** — 0:25 · built from scenes 1 and 3

- **Hook (first 1.5s):** a school bell and an exam paper landing on a desk
- **Script:** Pens down. This is Xecxec's final exam. Eighty-six episodes. Basics, loops, functions, nine episodes of pointers, files, six sorting algorithms and two real projects. You went from Hello World to an ATM that can't be robbed. Now prove it. The final episode of Koding Konkani is out.
- **On-screen text:** 86 EPISODES. ONE FINAL EXAM.
- **Caption + hashtags:** The finale is here. Are you ready? #cprogramming #learntocode #kodingkonkani #exams #codingjourney

**S2 · 3 Output Traps in 30 Seconds** — 0:40 · built from scene 5

- **Hook (first 1.5s):** `sizeof("Goa")` = 3?
- **Script:** Three traps examiners love. One: b equals a plus plus plus 2, with a equal to 5. b is 7, a is 6, because post-increment uses the old value first. Two: 7 divided by 2 in integers is 3, not 3.5. Three: the size of the char array "Goa" is 4, not 3, because of the hidden backslash zero.
- **On-screen text:** 7 · 3 · 4
- **Caption + hashtags:** Save this before your C exam. #cprogramming #learntocode #kodingkonkani #exams #computerscience

**S3 · The Exam Panic Bug** — 0:40 · built from scene 7

- **Hook (first 1.5s):** heartbeat sound and "marks = 35 ... Pass?!"
- **Script:** Under pressure, you write if marks equals 40 with one equals sign. marks is 35, and it prints Pass. One equals assigns, two equals compares. Panic makes you repeat old bugs. So use four calm steps: read twice, draw boxes for every variable, check each line for a known bug, then verify once. Slow is smooth, smooth is fast.
- **On-screen text:** = ASSIGNS · == COMPARES
- **Caption + hashtags:** The bug is in your head, not your code. #cprogramming #debugging #kodingkonkani #examtips #learntocode

**S4 · Never Forgot to Return** — 0:12 · built from scene 6

- **Hook (first 1.5s):** Xecxec in a graduation cap holding a report card with full marks
- **Script:** Why did Xecxec pass the C exam with full marks? Because he never forgot to return.
- **On-screen text:** NEVER FORGOT TO RETURN
- **Caption + hashtags:** Return 0, return champion. #codingmemes #programmerhumor #kodingkonkani #cprogramming #learntocode

**S5 · Quiz: Score Out of 3** — 0:35 · built from scene 9

- **Hook (first 1.5s):** "Can you get 3 out of 3?"
- **Script:** int i equals 3. What does i plus plus times 2 print? Then plus plus i times 2? And 17 mod 5? Answers: 6, because post-increment uses 3 first. Then 10, because i was 4 and becomes 5 before multiplying. And 2, the remainder. Comment your score out of 3.
- **On-screen text:** i++ \* 2 · ++i \* 2 · 17 % 5
- **Caption + hashtags:** Comment your score before checking. #cprogramming #codingquiz #kodingkonkani #learntocode #exams
