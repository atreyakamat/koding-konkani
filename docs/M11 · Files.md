# Module 11 — Files

Episodes 69–71 · Apricot + Dark blue

## EP 69 — Writing Files

**Module 11 · Files · 6:30 · Apricot + Dark blue · Prerequisite: EP 68**

**Learning goals:** explain why data in variables disappears when a program ends; open a file with `fopen` and pick the right mode (`"w"`, `"a"`, `"r"`); write text with `fprintf` and `fputs`, then close it with `fclose`; always check `fopen`'s result for `NULL` before using the file.

### YouTube

- **Title:** Make Your Data Survive a Restart: Writing Files | C EP 69
- **Description:** Everything in your variables vanishes when the program ends. Files fix that. We open a file, write to it with fprintf, add to it with append mode, and learn why skipping the NULL check crashes your program. 0:00 Where did my data go? 0:25 What is a file? 1:00 fopen and FILE \* 1:35 File modes: w, a, r 2:10 Writing a diary, line by line 3:40 Append mode 4:40 Bug of the Day: not checking NULL 5:55 Challenge
- **Tags:** c programming, file handling in c, fopen in c, fprintf, write to file in c, append mode, fclose, file modes in c, learn c, koding konkani
- **Thumbnail:** big text "DATA THAT SURVIVES"; a laptop power button with a notebook file safely glowing beside it; Xecxec hugging the file; Apricot background, Dark blue blocks.

### Scene list

| # | Start | Length | Template | On screen | Animation & SFX |
| --- | --- | --- | --- | --- | --- |
| 1 | 0:00 | 0:20 | Terminal | A game score `score = 950` printed, program ends, run again: `score = 0` | Power-off SFX, numbers fade to dust; Xecxec gasps |
| 2 | 0:20 | 0:05 | Title card | EP 69 · WRITING FILES | Apricot card, Dark blue text, claw-click |
| 3 | 0:25 | 0:35 | Concept slide | RAM (temporary, Lilac boxes) vs disk (permanent, a file icon); arrow "program → file" | RAM boxes empty on power-off; file icon stays; click SFX |
| 4 | 1:00 | 0:35 | Memory boxes | `FILE *fp` as a pointer box pointing to a "file handle" card linked to `diary.txt` | Arrow draws from `fp` to the handle; link chain SFX |
| 5 | 1:35 | 0:35 | Concept slide | Mode table: `"w"` write (creates or wipes), `"a"` append (adds at end), `"r"` read (must exist) | Three cards flip; `"w"` card shows an eraser wiping old text |
| 6 | 2:10 | 1:15 | Code explain | `write.c` with a live `diary.txt` panel | Each `fprintf` line types into the file panel; `fclose` shows a lid closing |
| 7 | 3:25 | 0:15 | Terminal | Compile, run, then `cat diary.txt` | Output and file contents appear |
| 8 | 3:40 | 0:05 | Pun card | Pun | Xecxec writing in a diary with a feather, rimshot |
| 9 | 3:45 | 0:55 | Code explain | `append.c` | File panel keeps the old 3 lines; new line slides in at the bottom in Mint |
| 10 | 4:40 | 1:15 | Bug of the Day | `nullbug.c` writes to `notes/today.txt` (folder missing): crash | Apricot frame with Butter highlight; `fp` box shows NULL; arrow points at nothing, crash SFX; fix adds the `if` guard |
| 11 | 5:55 | 0:20 | Challenge | "Save your name and age to me.txt" | Timer ring |
| 12 | 6:15 | 0:15 | Outro | Next: EP 70, reading files | Xecxec waves, end card |

### Narration script

**\[1 · Hook\]** You play a game. You score 950. You close it, open it again, and your score is 0. Where did it go? Every variable we've used so far lives in memory, and memory is cleared when the program ends. Today we learn how to make data survive a restart.

**\[2 · Title\]** Episode sixty-nine. Writing files.

**\[3 · What is a file\]** Your variables live in RAM, the computer's short-term memory. Fast, but temporary. Files live on the disk, the long-term memory. Slower, but they stay even after you switch off the computer. Your C code, your photos, your notes, all files. Today our program will create its own file and write to it. Like a fisherman writing today's catch in a notebook, so tomorrow he still knows.

**\[4 · FILE pointer\]** To work with a file, C gives us a type called FILE, in capital letters, from stdio dot h. We never use a FILE directly. We use a pointer to one: FILE star fp. You learned pointers in Module 8. fp doesn't hold the file's text. It points to a handle that C uses to keep track of the open file: which file, and where we are in it. The function fopen opens the file and gives us that pointer.

**\[5 · Modes\]** fopen needs two things: the file name, and a mode. The mode is a short string. "w" means write. It creates the file if it doesn't exist. Careful: if the file does exist, "w" wipes it clean first. "a" means append. It adds new text to the end and keeps what's there. "r" means read, and the file must already exist. We'll use "r" next episode.

**\[6 · Code explain\]** Let's write a diary. \[HL 4\] FILE star fp equals fopen, "diary dot txt", "w". Open diary dot txt for writing. \[HL 6\] if fp equals NULL. If fopen fails, it gives back NULL instead of a real pointer. Maybe the disk is full, or the folder doesn't exist. \[HL 7\] \[HL 8\] Then we print a message and return 1, which means something went wrong. \[HL 11\] fprintf, fp, "Day 1: Learned files in C", backslash n. fprintf is printf with one extra first argument: where to print. Instead of the screen, it prints into fp. \[HL 12\] fprintf again with percent d and 7, so the file gets "Fish caught: 7". Everything you know about printf formats works here. \[HL 13\] fputs, "Mood: happy" backslash n, fp. fputs writes a plain string with no formatting. Notice the order: the string first, then the file. \[HL 15\] fclose fp. This closes the file. C often holds your text in a waiting area, a buffer, and fclose makes sure everything is really written to the disk. Forget fclose, and you might lose your last lines. \[HL 16\] Finally, we tell the user "Saved to diary dot txt".

**\[7 · Terminal\]** Compile and run. It says "Saved to diary dot txt". Now type cat diary dot txt. In the MSYS2 terminal, cat shows a file's contents. Three lines, exactly what we wrote. The file is in the same folder you ran the program from. Run the program a second time, and you still see three lines, not six. Remember, "w" wipes the file first.

**\[8 · Pun\]** Why did the file feel so calm? Because it finally got closure.

**\[9 · Append\]** To add a new day without wiping the old ones, we use "a". \[HL 4\] fopen, "diary dot txt", "a". \[HL 6\] Same NULL check. \[HL 11\] fprintf, "Day 2: Monsoon, stayed home and coded". \[HL 13\] fclose. Run it, then cat the file. The first three lines are still there, and Day 2 is added at the bottom. Run it again, and another Day 2 line is added. Use "w" when you want a fresh file. Use "a" for logs and diaries that grow.

**\[10 · Bug of the Day\]** Today's bug: not checking fopen for NULL. This program opens notes slash today dot txt, but there is no notes folder. "w" can create a file, but it can't create a folder. So fopen fails and returns NULL. The program doesn't check. It calls fprintf with a NULL pointer. Compile: no error, no warning. Run: the program crashes. On Linux you see "Segmentation fault". On Windows it just stops, and "Saved!" is never printed. The fix: always check. If fp equals NULL, print a message and return 1. Even better, use perror, which prints the file name and the real reason, like "No such file or directory".

**\[11 · Challenge\]** Your challenge: ask the user for their name and age, then save both into a file called me dot txt, one per line. Check for NULL, and close the file. Open it with cat to prove it worked.

**\[12 · Outro\]** Next episode: reading files, and getting our diary back. Keep coding, says Xecxec!

### Code shown

```c
#include <stdio.h>

int main(void) {
    FILE *fp = fopen("diary.txt", "w");

    if (fp == NULL) {
        printf("Could not open diary.txt\n");
        return 1;
    }

    fprintf(fp, "Day 1: Learned files in C\n");
    fprintf(fp, "Fish caught: %d\n", 7);
    fputs("Mood: happy\n", fp);

    fclose(fp);
    printf("Saved to diary.txt\n");
    return 0;
}
```

```text
Saved to diary.txt
```

Contents of `diary.txt` (`cat diary.txt`):

```text
Day 1: Learned files in C
Fish caught: 7
Mood: happy
```

```c
#include <stdio.h>

int main(void) {
    FILE *fp = fopen("diary.txt", "a");

    if (fp == NULL) {
        printf("Could not open diary.txt\n");
        return 1;
    }

    fprintf(fp, "Day 2: Monsoon, stayed home and coded\n");

    fclose(fp);
    printf("Added a new line\n");
    return 0;
}
```

```text
Added a new line
```

Contents of `diary.txt` after one run:

```text
Day 1: Learned files in C
Fish caught: 7
Mood: happy
Day 2: Monsoon, stayed home and coded
```

### Bug of the Day

```c
#include <stdio.h>

int main(void) {
    FILE *fp = fopen("notes/today.txt", "w");

    fprintf(fp, "Hello file\n");
    fclose(fp);

    printf("Saved!\n");
    return 0;
}
```

No compiler error or warning. When the `notes` folder does not exist, the program crashes before printing anything (Linux shows `Segmentation fault`; on Windows the program stops silently with a non-zero exit code). On screen: "your crash message may differ".

Fixed:

```c
#include <stdio.h>

int main(void) {
    FILE *fp = fopen("notes/today.txt", "w");

    if (fp == NULL) {
        perror("notes/today.txt");
        return 1;
    }

    fprintf(fp, "Hello file\n");
    fclose(fp);

    printf("Saved!\n");
    return 0;
}
```

```text
notes/today.txt: No such file or directory
```

`fopen` returns `NULL` when it cannot open the file, and passing `NULL` to `fprintf` crashes the program.

### Pun & challenge

- **Pun:** Why did the file feel so calm? Because it finally got closure.
- **Challenge:** Read the user's name and age, and save them to `me.txt` as `Name: ...` and `Age: ...` on two lines.
- **Challenge answer:**

```c
char name[50];
int age;
printf("Name: ");
scanf("%49s", name);
printf("Age: ");
scanf("%d", &age);

FILE *fp = fopen("me.txt", "w");
if (fp == NULL) {
    printf("Could not open me.txt\n");
    return 1;
}
fprintf(fp, "Name: %s\nAge: %d\n", name, age);
fclose(fp);
printf("Saved to me.txt\n");
```

### Shorts for EP 69

**S1 · Why Did My Score Reset to 0?** — 0:20 · built from scenes 1 and 3

- **Hook (first 1.5s):** "score = 950" turning into "score = 0"
- **Script:** You score 950, close the program, open it again: 0. Variables live in RAM, and RAM is wiped when the program ends. To keep data, write it to a file on the disk. That's file handling in C. Full episode on Koding Konkani.
- **On-screen text:** 950 to 0?! / RAM FORGETS / FILES REMEMBER
- **Caption + hashtags:** Make your data survive a restart. #cprogramming #learntocode #kodingkonkani #filehandling #codingforbeginners

**S2 · Writing a File in 30 Seconds** — 0:30 · built from scenes 5–6

- **Hook (first 1.5s):** A file icon with text typing into it
- **Script:** Three steps. Open: FILE star fp equals fopen, file name, "w". Check: if fp is NULL, stop. Write: fprintf, fp, then your text, just like printf. Then close with fclose. "w" wipes the file first, "a" adds to the end.
- **On-screen text:** OPEN / CHECK / WRITE / CLOSE
- **Caption + hashtags:** Four steps to save anything. #cprogramming #learntocode #kodingkonkani #fopen #ctutorial

**S3 · My Program Crashed Writing a File** — 0:30 · built from scene 10

- **Hook (first 1.5s):** Crash SFX and a NULL box
- **Script:** This program crashes before it prints anything. Why? The folder "notes" doesn't exist, so fopen returns NULL. Then fprintf writes to NULL. Crash. Always check: if fp equals NULL, use perror to print the reason, and return 1.
- **On-screen text:** CRASH! / fopen = NULL / ALWAYS CHECK
- **Caption + hashtags:** The one check every file program needs. #cprogramming #learntocode #kodingkonkani #debugging #filehandling

**S4 · Pun: Closure** — 0:10 · built from scene 8

- **Hook (first 1.5s):** Xecxec closing a diary with a sigh
- **Script:** Why did the file feel so calm? Because it finally got closure.
- **On-screen text:** fclose(fp); CLOSURE
- **Caption + hashtags:** Always close your files. Emotionally too. #cprogramming #codingmemes #kodingkonkani #programmerhumor

**S5 · "w" or "a"?** — 0:20 · built from scenes 5 and 9

- **Hook (first 1.5s):** Two cards: "w" and "a"
- **Script:** Quiz. You want to keep a daily log, adding one line each day without losing old ones. Which mode: "w" or "a"? Answer: "a", append. "w" would wipe yesterday's log every time.
- **On-screen text:** "w" OR "a"? / ANSWER: "a"
- **Caption + hashtags:** Don't wipe your diary by mistake. #cprogramming #learntocode #kodingkonkani #cquiz #fopen

## EP 70 — Reading Files

**Module 11 · Files · 6:45 · Apricot + Dark blue · Prerequisite: EP 69**

**Learning goals:** open a file in `"r"` mode and report a missing file with `perror`; read a file line by line with `fgets` until it returns `NULL`; read structured data with `fscanf` and use its return value to stop the loop; explain what `EOF` is and why loops must test the read function's result.

### YouTube

- **Title:** Read Your Diary Back: Reading Files in C | C EP 70
- **Description:** Last episode we wrote a diary to a file. Today we read it back, line by line with fgets, and word by word with fscanf. Then we meet EOF and fix the loop that never stops reading. 0:00 Challenge answer and hook 0:25 Opening for reading 1:00 fgets: line by line 2:30 fscanf: a marks file 4:10 What is EOF? 4:45 Bug of the Day: infinite EOF loop 6:05 Challenge
- **Tags:** c programming, read file in c, fgets in c, fscanf in c, EOF in c, file handling in c, perror, read file line by line, learn c, koding konkani
- **Thumbnail:** big text "READ IT BACK"; an open diary with lines flying out into a terminal; Xecxec reading with tiny glasses; Apricot background, Dark blue blocks.

### Scene list

| # | Start | Length | Template | On screen | Animation & SFX |
| --- | --- | --- | --- | --- | --- |
| 1 | 0:00 | 0:20 | Terminal | EP 69 challenge: run, then `cat me.txt` | Typing SFX; then a closed diary appears, lock clicks open |
| 2 | 0:20 | 0:05 | Title card | EP 70 · READING FILES | Apricot card, claw-click |
| 3 | 0:25 | 0:35 | Terminal | `"r"` on a missing file: `perror` prints `nothere.txt: No such file or directory` | Empty folder icon, Tomato message slides in |
| 4 | 1:00 | 1:30 | Code explain | `readlines.c` with `diary.txt` panel and a reading cursor | Cursor highlights one line of the file per loop; `line` buffer box fills; `count` tracker 1 → 4; final `fgets` returns NULL (grey) |
| 5 | 2:30 | 0:05 | Pun card | Pun | Xecxec with a book, rimshot |
| 6 | 2:35 | 1:35 | Code explain | `marks.c` with `marks.txt` panel | Name and number tokens jump from the file into `name` and `mark` boxes; `total` and `students` trackers |
| 7 | 4:10 | 0:35 | Concept slide | "EOF = end of file", value `-1` on GCC; table: `fgets` → NULL, `fscanf` → EOF or fewer items, `fgetc` → EOF | Cards flip; "EOF" sign at the end of a road |
| 8 | 4:45 | 1:20 | Bug of the Day | `!= 0` test: "Xecxec 95" repeats forever | Apricot frame with Butter highlight; return value box shows -1, and -1 != 0 is true (Tomato); output floods; Ctrl+C keycap |
| 9 | 6:05 | 0:25 | Challenge | "Ask for a file name and count its lines" | Timer ring |
| 10 | 6:30 | 0:15 | Outro | Next: EP 71, binary files | Xecxec waves, end card |

### Narration script

**\[1 · Recap and hook\]** Last challenge: read a name and age, then save them to me dot txt with fprintf, checking for NULL and closing the file. Run it, cat the file, and there it is. But a program that only writes is like a diary you can never open. Today we read files back into our program.

**\[2 · Title\]** Episode seventy. Reading files.

**\[3 · Opening for reading\]** To read, we open with mode "r". Unlike "w", "r" never creates a file. If the file isn't there, fopen returns NULL. So the NULL check matters even more. Here we use perror, which prints your message, then a colon, then the real reason from the system. Try opening nothere dot txt: "nothere dot txt: No such file or directory". Clear and honest.

**\[4 · fgets\]** Let's read our diary from last episode, which now has four lines. \[HL 4\] fopen, "diary dot txt", "r". \[HL 5\] \[HL 6\] \[HL 7\] If fp is NULL, perror and return 1. \[HL 10\] char line, 100. A buffer, a box of 100 characters to hold one line at a time. \[HL 11\] count equals 0. \[TRACK count=0\] \[HL 13\] while, fgets, line, sizeof line, fp, not equal to NULL. fgets reads one line from fp into line. It stops at the newline, or when the buffer is full, so it never overflows. sizeof line tells it the size, 100. It keeps the newline character, and adds the null terminator at the end. When there is nothing left to read, fgets returns NULL, and the loop ends. \[HL 14\] count plus plus. \[TRACK count=1\] \[HL 15\] printf percent d, colon, percent s. No backslash n here, because line already ends with the newline from the file. First line: "1: Day 1: Learned files in C". \[TRACK count=2\] Then "2: Fish caught: 7". \[TRACK count=3\] "3: Mood: happy". \[TRACK count=4\] "4: Day 2: Monsoon". Then fgets returns NULL. \[HL 18\] fclose. \[HL 19\] "Read 4 lines". The pattern is: read inside the loop condition, and stop when the read fails.

**\[5 · Pun\]** Why did the C program love reading files? It could never put them down until it reached the end.

**\[6 · fscanf\]** fgets reads whole lines. But what if each line has a name and a number, like a marks list? Here is marks dot txt: Ravi 72, Anjali 88, Xecxec 95. We use fscanf, which is scanf for files. \[HL 10\] char name 30. \[HL 11\] int mark. \[HL 12\] total and students both start at 0. \[HL 14\] while fscanf, fp, "percent 29 s, percent d", name, address of mark, equals 2. fscanf returns how many items it filled. We asked for two, a word and a number. The 29 stops it from overflowing our 30-character name box. If it returns 2, we got a full line. First line: name is Ravi, mark is 72. \[TRACK name=Ravi mark=72\] \[HL 15\] printf percent minus 8 s and percent 3 d: the name left-aligned in 8 spaces, the number in 3, so the columns line up. \[HL 16\] total plus equals mark. \[TRACK total=72\] \[HL 17\] students plus plus. \[TRACK students=1\] Then Anjali, 88. \[TRACK total=160 students=2\] Then Xecxec, 95. \[TRACK total=255 students=3\] Next time, there's nothing left, fscanf does not return 2, and the loop stops. \[HL 21\] \[HL 22\] If students is more than 0, we print the average: total, cast to double, divided by students. 255 by 3 is 85 point 00. The cast is from Episode 13: without it, int division would drop the decimals.

**\[7 · EOF\]** So what is EOF? It stands for End Of File. It's a special value, defined in stdio dot h, which is minus 1 on GCC. It's not a character inside the file. It's a signal that reading functions return when there's nothing left. fgetc, which reads one character, returns EOF at the end. fscanf returns EOF if it hits the end before reading anything. And fgets returns NULL instead. The rule is simple: always loop on the result of the read function itself.

**\[8 · Bug of the Day\]** Today's bug: the infinite EOF loop. A student writes: while fscanf, and so on, not equal to 0. The idea: "keep going until fscanf reads nothing". Compile: no error. Run it. Ravi 72, Anjali 88, Xecxec 95, then Xecxec 95, Xecxec 95, forever. Press Control C. What happened? At the end of the file, fscanf does not return 0. It returns EOF, which is minus 1. And minus 1 is not equal to 0, so the condition stays true. fscanf keeps failing, name and mark keep their old values, and we print them again and again. The fix: test for exactly what you want. equals 2. If fscanf gives back anything other than 2, stop.

**\[9 · Challenge\]** Your challenge: ask the user for a file name, open it, and count how many lines it has using fgets. If the file can't be opened, use perror. Test it on diary dot txt; you should get 4.

**\[10 · Outro\]** Next episode: binary files, where we save whole structs and build a tiny database. Keep coding, says Xecxec!

### Code shown

```c
#include <stdio.h>

int main(void) {
    FILE *fp = fopen("diary.txt", "r");
    if (fp == NULL) {
        perror("diary.txt");
        return 1;
    }

    char line[100];
    int count = 0;

    while (fgets(line, sizeof line, fp) != NULL) {
        count++;
        printf("%d: %s", count, line);
    }

    fclose(fp);
    printf("Read %d lines\n", count);
    return 0;
}
```

```text
1: Day 1: Learned files in C
2: Fish caught: 7
3: Mood: happy
4: Day 2: Monsoon, stayed home and coded
Read 4 lines
```

`marks.txt`:

```text
Ravi 72
Anjali 88
Xecxec 95
```

```c
#include <stdio.h>

int main(void) {
    FILE *fp = fopen("marks.txt", "r");
    if (fp == NULL) {
        perror("marks.txt");
        return 1;
    }

    char name[30];
    int mark;
    int total = 0, students = 0;

    while (fscanf(fp, "%29s %d", name, &mark) == 2) {
        printf("%-8s %3d\n", name, mark);
        total += mark;
        students++;
    }

    fclose(fp);
    if (students > 0) {
        printf("Average: %.2f\n", (double)total / students);
    }
    return 0;
}
```

```text
Ravi      72
Anjali    88
Xecxec    95
Average: 85.00
```

Missing-file demo (scene 3), same `perror` pattern with `fopen("nothere.txt", "r")`:

```text
nothere.txt: No such file or directory
```

### Bug of the Day

```c
#include <stdio.h>

int main(void) {
    FILE *fp = fopen("marks.txt", "r");
    if (fp == NULL) {
        return 1;
    }

    char name[30];
    int mark;

    while (fscanf(fp, "%29s %d", name, &mark) != 0) {
        printf("%s %d\n", name, mark);
    }

    fclose(fp);
    return 0;
}
```

No compiler error or warning. Output never stops (Ctrl+C to quit):

```text
Ravi 72
Anjali 88
Xecxec 95
Xecxec 95
Xecxec 95
...
```

Fixed:

```c
    while (fscanf(fp, "%29s %d", name, &mark) == 2) {
```

At end of file `fscanf` returns `EOF` (-1), not 0, so `!= 0` stays true forever; testing `== 2` stops on any failed read.

### Pun & challenge

- **Pun:** Why did the C program love reading files? It could never put them down until it reached the end.
- **Challenge:** Ask for a file name, then count its lines with `fgets` (use `perror` if it can't be opened).
- **Challenge answer:**

```c
char fname[100];
printf("File name: ");
scanf("%99s", fname);

FILE *fp = fopen(fname, "r");
if (fp == NULL) {
    perror(fname);
    return 1;
}

char line[256];
int count = 0;
while (fgets(line, sizeof line, fp) != NULL) {
    count++;
}
fclose(fp);
printf("%s has %d lines\n", fname, count);
```

```text
File name: diary.txt
diary.txt has 4 lines
```

Note: a line longer than 255 characters would be counted more than once; fine for this challenge.

### Shorts for EP 70

**S1 · Open Your Diary in C** — 0:20 · built from scenes 1 and 4

- **Hook (first 1.5s):** A locked diary clicking open
- **Script:** We saved a diary to a file. Now let's read it back. Open with "r", then loop: while fgets reads a line, print it. When fgets returns NULL, the file is done. Four lines, back on screen. Full episode on Koding Konkani.
- **On-screen text:** OPEN WITH "r" / fgets LINE BY LINE
- **Caption + hashtags:** Reading files, the easy way. #cprogramming #learntocode #kodingkonkani #filehandling #codingforbeginners

**S2 · fgets vs fscanf in 30 Seconds** — 0:30 · built from scenes 4 and 6

- **Hook (first 1.5s):** A whole line vs separate words flying out of a file
- **Script:** Two ways to read a file. fgets reads a whole line into a char array, and returns NULL at the end. fscanf reads values, like a name and a number, and returns how many it filled. Loop while fgets is not NULL, or while fscanf equals the count you asked for.
- **On-screen text:** fgets = LINES / fscanf = VALUES
- **Caption + hashtags:** Pick the right reader. #cprogramming #learntocode #kodingkonkani #fgets #fscanf

**S3 · My File Loop Never Ends** — 0:30 · built from scene 8

- **Hook (first 1.5s):** "Xecxec 95" repeating down the screen
- **Script:** Three lines in the file, but the last one prints forever. The loop says while fscanf is not 0. But at the end of the file, fscanf returns EOF, which is minus 1. Minus 1 is not 0, so the loop never stops. Test for exactly what you want: equals 2.
- **On-screen text:** NEVER ENDS? / EOF = -1 / USE == 2
- **Caption + hashtags:** EOF is not zero. #cprogramming #learntocode #kodingkonkani #debugging #EOF

**S4 · Pun: Can't Put It Down** — 0:10 · built from scene 5

- **Hook (first 1.5s):** Xecxec glued to a book
- **Script:** Why did the C program love reading files? It could never put them down until it reached the end.
- **On-screen text:** READ UNTIL EOF
- **Caption + hashtags:** A real page-turner. #cprogramming #codingmemes #kodingkonkani #programmerhumor

**S5 · What Does EOF Equal?** — 0:15 · built from scene 7

- **Hook (first 1.5s):** "EOF = ?"
- **Script:** Quick quiz. In GCC, what is the value of EOF? 0? 1? Minus 1? It's minus 1. And it's a signal from reading functions, not a character stored in the file.
- **On-screen text:** EOF = ? / 0, 1, or -1? / -1
- **Caption + hashtags:** Viva question alert. #cprogramming #learntocode #kodingkonkani #cquiz #EOF

## EP 71 — Binary Files and Records

**Module 11 · Files · 7:30 · Apricot + Dark blue · Prerequisite: EP 70**

**Learning goals:** explain the difference between text files and binary files; save and load an array of structs with `fwrite` and `fread`, checking how many records were transferred; jump straight to record N with `fseek` and measure a file with `ftell`; update one record in place with `"r+b"` mode, and always use `b` modes for binary data.

### YouTube

- **Title:** Build a Tiny Database in C: fwrite, fread, fseek | C EP 71
- **Description:** Text files are great for people. Binary files are great for programs. We save three student structs in one fwrite call, read them back, jump straight to record 2 with fseek, edit one record in place, and fix the Windows text-mode bug that eats your data. 0:00 Challenge answer and hook 0:30 Text vs binary 1:15 Saving structs with fwrite 2:45 Reading records with fread 3:50 Jumping with fseek and ftell 4:40 Updating one record 5:30 Bug of the Day: text mode for binary data 6:55 Challenge
- **Tags:** c programming, binary file in c, fwrite in c, fread in c, fseek in c, ftell, file handling in c, structure in file, student record program c, koding konkani
- **Thumbnail:** big text "TINY DATABASE"; three record cards stacked in a filing drawer with byte numbers 0, 28, 56 on the tabs; Xecxec as a librarian pulling out card 2; Apricot background, Dark blue blocks.

### Scene list

| # | Start | Length | Template | On screen | Animation & SFX |
| --- | --- | --- | --- | --- | --- |
| 1 | 0:00 | 0:30 | Terminal | EP 70 challenge: line counter on `diary.txt`; then a school office clerk flipping through a huge register | Typing SFX; register pages flip, Xecxec yawns |
| 2 | 0:30 | 0:05 | Title card | EP 71 · BINARY FILES & RECORDS | Apricot card, claw-click |
| 3 | 0:35 | 0:40 | Memory boxes | Number 1000 stored as text (4 characters '1','0','0','0') vs as an int (4 raw bytes in Lilac) | Characters type in; raw bytes slide in as hex boxes; "people read" vs "programs read" labels |
| 4 | 1:15 | 1:30 | Code explain | `binwrite.c` with an array of 3 struct cards | Three cards fly into a file drawer in one move; size badge "28 bytes each" with "your size may differ" note |
| 5 | 2:45 | 1:00 | Code explain | `binread.c` lines 1–22 (fread loop) | Cards pull out one at a time into the `st` box; return value badge shows 1, 1, 1, then 0 |
| 6 | 3:45 | 0:05 | Pun card | Pun | Xecxec in a librarian bun, rimshot |
| 7 | 3:50 | 0:50 | Code explain | `binread.c` lines 24–32 (fseek, ftell) | File position cursor jumps from byte 0 to 28; then to the end, ruler shows 84 bytes |
| 8 | 4:40 | 0:50 | Code explain | `update.c` | Cursor jumps to byte 56, card lifted, marks 95.5 → 99.0 in Mint, put back in the same slot |
| 9 | 5:30 | 1:25 | Bug of the Day | `rolls.c` uses `"w"`/`"r"` for binary ints on Windows | Apricot frame with Butter highlight; byte strip: 0A becomes 0D 0A on write; 1A acts as a stop sign on read; "Windows only" badge; fix to `"wb"`/`"rb"` (Mint) |
| 10 | 6:55 | 0:20 | Challenge | "Save 3 shop items as structs, then read and print them" | Bebinca, kokad and feni cards appear, timer ring |
| 11 | 7:15 | 0:15 | Outro | Module 11 complete badge; Next: EP 72 | Badge stamp, Xecxec waves, end card |

### Narration script

**\[1 · Recap and hook\]** Last challenge: ask for a file name, open it with "r", and count lines with fgets until it returns NULL. On diary dot txt, you get 4. Now think about the school office register. Hundreds of students, one row each. To find roll number 250, the clerk flips page after page. Today we build a tiny database in C, where we can jump straight to any record.

**\[2 · Title\]** Episode seventy-one. Binary files and records.

**\[3 · Text vs binary\]** So far our files were text: characters people can read. If we save the number 1000 as text, we store four characters: 1, 0, 0, 0. To get the number back, the program has to read the characters and convert them. A binary file stores the bytes exactly as they sit in memory. The int 1000 is just its 4 raw bytes, usually. Open it in Notepad and you'll see junk, but your program can load it back instantly. And every record is the same size, which is the secret to jumping straight to one.

**\[4 · fwrite\]** \[HL 3\] Here's our record: struct Student, with roll, an int, name, 20 characters, and marks, a float. You built structs like this in Module 9. \[HL 10\] An array of 3 students, filled in right here. \[HL 16\] fopen, "students dot dat", "wb". The b means binary. \[HL 17\] NULL check with perror, as always. \[HL 22\] size\_t written equals fwrite, s, sizeof struct Student, 3, fp. fwrite takes four things: where the data starts, the size of one item, how many items, and the file. So: from the array s, write 3 items, each the size of one Student. It returns how many items it actually wrote. size\_t is the unsigned type C uses for sizes and counts. \[HL 23\] fclose. \[HL 25\] Print "Wrote", percent z u, written. Percent z u is the format for size\_t. We get 3. \[HL 26\] And the size of one record: 28 bytes on our machine. 4 for the int, 20 for the name, 4 for the float. Your size may differ on other machines, and padding can add extra bytes, as you saw in Episode 64. One call, three whole records saved.

**\[5 · fread\]** Now let's read them back. \[HL 10\] fopen with "rb", read binary. \[HL 16\] struct Student st, one empty record box. \[HL 18\] while fread, address of st, sizeof st, 1, fp, equals 1. fread is fwrite's twin: where to put the data, the size of one item, how many, and the file. We read one record at a time. It returns how many records it read. 1 means success. At the end of the file it returns 0, and the loop stops. Same rule as last episode: loop on the read function's result. \[TRACK st.roll=1\] \[HL 19\] Print roll, name and marks. 1, Ravi, 72.5. \[TRACK st.roll=2\] 2, Anjali, 88.0. \[TRACK st.roll=3\] 3, Xecxec, 95.5. Exactly what we saved.

**\[6 · Pun\]** Why did the binary file make a great librarian? It always kept its records straight.

**\[7 · fseek and ftell\]** Now the magic. Every record is 28 bytes. So record 1 starts at byte 0, record 2 at byte 28, record 3 at byte 56. To read record 2, we don't need to read record 1 first. \[HL 25\] fseek, fp, 1 times sizeof st, SEEK\_SET. fseek moves the file's reading position. SEEK\_SET means "count from the start of the file". So we jump to byte 28. We cast sizeof to long because fseek expects a long offset. \[HL 26\] fread one record. \[HL 27\] "Record 2 is Anjali". Straight there, no flipping pages. \[HL 29\] fseek, fp, 0, SEEK\_END: jump to the very end. \[HL 30\] ftell tells us the current position in bytes. At the end, that's the file size: 84. \[HL 31\] 84 divided by 28 is 3 records. That's how a program can count records without reading them.

**\[8 · Update\]** Last trick: changing one record without rewriting the whole file. Xecxec got a re-evaluation. \[HL 11\] fopen with "r plus b": read and write, binary, and the file must exist. \[HL 18\] pos equals 2 times sizeof st. Record 3 starts at byte 56. \[HL 20\] fseek to pos. \[HL 21\] fread the record into st. \[TRACK st.marks=95.5\] \[HL 22\] Change marks to 99. \[TRACK st.marks=99.0\] \[HL 24\] fseek back to pos. Why again? Reading moved the position forward by 28 bytes. We must go back to overwrite the same slot. Also, C requires a fseek between reading and writing on the same file. \[HL 25\] fwrite the record. \[HL 26\] fclose. Run the reader again: Xecxec now has 99.0, and the file is still 84 bytes. One record changed, nothing else touched. That's a tiny database.

**\[9 · Bug of the Day\]** Today's bug only shows up on Windows, which is exactly where you're coding. This program saves three ints, 10, 26 and 30, but opens the file with "w" and "r" instead of "wb" and "rb". Compile: no error, no warning. On Linux it works fine. On Windows it prints "Read 1 of 3 numbers". Where did the other two go? In text mode, Windows does two conversions. When writing, every byte with value 10, the newline, becomes two bytes, 13 and 10. When reading, a byte with value 26, which is Control Z, is treated as end of file. Our int 10 contains a byte 10, and our int 26 contains a byte 26. So the file is corrupted on the way in, and reading stops early on the way out. The fix: always use "wb", "rb" and "r plus b" for binary data. In binary mode, bytes go to the disk exactly as they are.

**\[10 · Challenge\]** Your challenge: make a struct Item with an id, a name and a quantity. Fill an array with three items from a Goan sweet shop: bebinca, kokad and feni. Save them to items dot dat with one fwrite, then open the file again and print every record with fread.

**\[11 · Outro\]** That's Module 11 complete! Your programs can now remember things after they close. Next episode, we start Module 12: algorithms, where we teach C to search and sort. Keep coding, says Xecxec!

### Code shown

```c
#include <stdio.h>

struct Student {
    int roll;
    char name[20];
    float marks;
};

int main(void) {
    struct Student s[3] = {
        {1, "Ravi", 72.5f},
        {2, "Anjali", 88.0f},
        {3, "Xecxec", 95.5f}
    };

    FILE *fp = fopen("students.dat", "wb");
    if (fp == NULL) {
        perror("students.dat");
        return 1;
    }

    size_t written = fwrite(s, sizeof(struct Student), 3, fp);
    fclose(fp);

    printf("Wrote %zu records\n", written);
    printf("Each record is %zu bytes\n", sizeof(struct Student));
    return 0;
}
```

```text
Wrote 3 records
Each record is 28 bytes
```

On screen: "28 bytes on our machine; your size may differ".

```c
#include <stdio.h>

struct Student {
    int roll;
    char name[20];
    float marks;
};

int main(void) {
    FILE *fp = fopen("students.dat", "rb");
    if (fp == NULL) {
        perror("students.dat");
        return 1;
    }

    struct Student st;

    while (fread(&st, sizeof st, 1, fp) == 1) {
        printf("%d  %-8s %.1f\n", st.roll, st.name, st.marks);
    }

    /* Jump straight to record 2 (index 1) */
    fseek(fp, 1 * (long)sizeof st, SEEK_SET);
    fread(&st, sizeof st, 1, fp);
    printf("Record 2 is %s\n", st.name);

    fseek(fp, 0, SEEK_END);
    long size = ftell(fp);
    printf("File size: %ld bytes, %ld records\n", size, size / (long)sizeof st);

    fclose(fp);
    return 0;
}
```

```text
1  Ravi     72.5
2  Anjali   88.0
3  Xecxec   95.5
Record 2 is Anjali
File size: 84 bytes, 3 records
```

Note: after the `while` loop hits end of file, `fseek` clears the end-of-file state, so the next `fread` works.

```c
#include <stdio.h>

struct Student {
    int roll;
    char name[20];
    float marks;
};

int main(void) {
    FILE *fp = fopen("students.dat", "r+b");
    if (fp == NULL) {
        perror("students.dat");
        return 1;
    }

    struct Student st;
    long pos = 2 * (long)sizeof st;

    fseek(fp, pos, SEEK_SET);
    fread(&st, sizeof st, 1, fp);
    st.marks = 99.0f;

    fseek(fp, pos, SEEK_SET);
    fwrite(&st, sizeof st, 1, fp);
    fclose(fp);

    printf("Updated %s to %.1f\n", st.name, st.marks);
    return 0;
}
```

```text
Updated Xecxec to 99.0
```

Running the reader again after the update:

```text
1  Ravi     72.5
2  Anjali   88.0
3  Xecxec   99.0
Record 2 is Anjali
File size: 84 bytes, 3 records
```

### Bug of the Day

```c
#include <stdio.h>

int main(void) {
    int rolls[3] = {10, 26, 30};

    FILE *fp = fopen("rolls.dat", "w");
    if (fp == NULL) {
        perror("rolls.dat");
        return 1;
    }
    fwrite(rolls, sizeof(int), 3, fp);
    fclose(fp);

    int back[3] = {0, 0, 0};
    fp = fopen("rolls.dat", "r");
    if (fp == NULL) {
        perror("rolls.dat");
        return 1;
    }
    size_t got = fread(back, sizeof(int), 3, fp);
    fclose(fp);

    printf("Read %zu of 3 numbers\n", got);
    return 0;
}
```

No compiler error or warning. On Windows (MSYS2 UCRT64) the expected wrong output is below, and `rolls.dat` is 13 bytes instead of 12. On Linux and macOS text and binary modes are the same, so it prints `Read 3 of 3 numbers`. On screen: "Windows only".

```text
Read 1 of 3 numbers
```

Fixed:

```c
    FILE *fp = fopen("rolls.dat", "wb");
    ...
    fp = fopen("rolls.dat", "rb");
```

```text
Read 3 of 3 numbers
```

In Windows text mode, byte 10 is written as 13 10 and byte 26 (Ctrl+Z) is read as end of file, so binary data must use `"wb"`/`"rb"`.

### Pun & challenge

- **Pun:** Why did the binary file make a great librarian? It always kept its records straight.
- **Challenge:** Make `struct Item { int id; char name[20]; int qty; }`, save 3 items (Bebinca 12, Kokad 30, Feni 5) to `items.dat` with one `fwrite`, then read and print them with `fread`.
- **Challenge answer:**

```c
struct Item {
    int id;
    char name[20];
    int qty;
};

int main(void) {
    struct Item items[3] = {{1, "Bebinca", 12}, {2, "Kokad", 30}, {3, "Feni", 5}};

    FILE *fp = fopen("items.dat", "wb");
    if (fp == NULL) { perror("items.dat"); return 1; }
    fwrite(items, sizeof(struct Item), 3, fp);
    fclose(fp);

    struct Item it;
    fp = fopen("items.dat", "rb");
    if (fp == NULL) { perror("items.dat"); return 1; }
    while (fread(&it, sizeof it, 1, fp) == 1) {
        printf("%d %-8s %d\n", it.id, it.name, it.qty);
    }
    fclose(fp);
    return 0;
}
```

```text
1 Bebinca  12
2 Kokad    30
3 Feni     5
```

### Shorts for EP 71

**S1 · Find Roll Number 250 Instantly** — 0:20 · built from scenes 1 and 7

- **Hook (first 1.5s):** A clerk flipping a giant register, sweating
- **Script:** The office clerk flips 250 pages to find one student. In a binary file, every record is the same size. So record N starts at N times the record size. fseek jumps straight there. No flipping. Full episode on Koding Konkani.
- **On-screen text:** FLIP 250 PAGES? / fseek / JUMP STRAIGHT THERE
- **Caption + hashtags:** A tiny database in C. #cprogramming #learntocode #kodingkonkani #filehandling #fseek

**S2 · fwrite and fread in 30 Seconds** — 0:30 · built from scenes 4–5

- **Hook (first 1.5s):** Three record cards flying into a drawer
- **Script:** fwrite saves raw bytes: where the data is, size of one item, how many, and the file. One call can save a whole array of structs. fread is its twin and loads them back. Both return how many items they handled, so loop while fread returns 1. Open with "wb" and "rb".
- **On-screen text:** fwrite(data, size, count, fp) / fread = TWIN
- **Caption + hashtags:** Save whole structs in one line. #cprogramming #learntocode #kodingkonkani #fwrite #fread

**S3 · Windows Ate My Data** — 0:30 · built from scene 9

- **Hook (first 1.5s):** "Read 1 of 3 numbers" in Tomato
- **Script:** Saved three numbers, read back one. Why? I opened a binary file with "w" and "r". On Windows, text mode turns byte 10 into two bytes, and treats byte 26 as end of file. My numbers 10 and 26 broke it. Always use "wb" and "rb" for binary data.
- **On-screen text:** 3 SAVED, 1 READ?! / TEXT MODE / USE "wb" "rb"
- **Caption + hashtags:** One missing letter b. #cprogramming #learntocode #kodingkonkani #debugging #windows

**S4 · Pun: Records Straight** — 0:10 · built from scene 6

- **Hook (first 1.5s):** Xecxec in a librarian bun
- **Script:** Why did the binary file make a great librarian? It always kept its records straight.
- **On-screen text:** RECORDS STRAIGHT
- **Caption + hashtags:** Organised to the byte. #cprogramming #codingmemes #kodingkonkani #programmerhumor

**S5 · Where Does Record 4 Start?** — 0:15 · built from scene 7

- **Hook (first 1.5s):** File ruler with byte marks
- **Script:** Each record is 28 bytes. Record 1 starts at byte 0. Where does record 4 start? 3 times 28: byte 84. Comment if you got it.
- **On-screen text:** 28 BYTES EACH / RECORD 4 = ? / BYTE 84
- **Caption + hashtags:** fseek maths in 10 seconds. #cprogramming #learntocode #kodingkonkani #cquiz #fseek
