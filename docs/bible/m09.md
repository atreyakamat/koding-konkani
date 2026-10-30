# Module 9 — Structures

Episodes 61–64 · Cream + Tomato

## EP 61 — struct basics

**Module 9 · Structures · 6:20 · Cream + Tomato · Prerequisite: EP 60**

**Learning goals:** define a `struct` type with members of different types; declare struct variables and fill them by member assignment or by an initialiser list; read and write members with the dot operator; use `strcpy` for a char-array member; know that one struct can be copied into another with `=`.

### YouTube

- **Title:** struct in C: A Student ID Card in Code | C Programming EP 61
- **Description:** A name, a roll number and a percentage belong together, so why keep them in three separate variables? Today we build a struct, the student ID card of C, fill it two ways, and read it with the dot operator. Plus the error you get when you forget one small keyword. Chapters: 0:00 Three loose variables · 0:25 What a struct is · 1:10 Code line by line · 3:00 Memory picture · 3:40 Copying a struct · 4:20 Bug of the Day · 5:30 Challenge
- **Tags:** c programming, struct in c, structures in c, dot operator, struct initialization, user defined data type, learn c, c for beginners, koding konkani, c tutorial english
- **Thumbnail:** big text "STRUCT = ID CARD"; a student ID card whose fields (name, roll, %) are code boxes; Xecxec holding the card proudly with a lanyard; cream background, tomato blocks

### Scene list

| # | Start | Length | Template | On screen | Animation & SFX |
| --- | --- | --- | --- | --- | --- |
| 1 | 0:00 | 0:20 | Concept slide | Three loose variables name1, roll1, pct1 blowing away in the wind | Paper flutter, Xecxec chases them |
| 2 | 0:20 | 0:05 | Title card | EP 61 · STRUCT BASICS | Title slam, whoosh |
| 3 | 0:25 | 0:45 | Concept slide | Blank ID card template (the type) vs filled cards (variables) | Template stamps out two filled cards; stamp SFX |
| 4 | 1:10 | 1:50 | Code explain | ep61.c, 28 lines; tracker shows s1 and s2 as cards | Line highlights; each member field fills on the card; key-tap SFX |
| 5 | 3:00 | 0:35 | Memory boxes | s1 as one long box split into name\[30\], rollNo, percentage | Boxes slide together; size labels "your sizes may differ" |
| 6 | 3:35 | 0:05 | Pun card | Pun line | Drum hit, claw-click |
| 7 | 3:40 | 0:40 | Code explain | s3 = s1; then s3.rollNo = 99 | Photocopier animation; two cards side by side |
| 8 | 4:20 | 1:10 | Bug of the Day | Student s1; without struct keyword | Red underline on Student, error buzz; "struct" tile slides in |
| 9 | 5:30 | 0:30 | Challenge | Book struct | Book flips open, timer ring |
| 10 | 6:00 | 0:20 | Outro | Next: EP 62 structs, arrays and pointers; sign-off | Module tiles, claw-click, music out |

### Narration script

**\[1 · Three loose variables\]** Here is a student. To store her in C so far, we need a char array for the name, an int for the roll number, and a float for the percentage. Three separate variables. Now add a second student. Six variables. A whole class? Hundreds of loose variables, flying around like papers on a windy day at Miramar beach. We need a way to keep things that belong together, together.

**\[2 · Title\]** Episode 61. struct basics.

**\[3 · What a struct is\]** Think of your college ID card. Every card has the same fields: name, roll number, and maybe a percentage. The printed blank design is the same for everybody. That blank design is the struct type. Then each student gets their own filled card. Those are struct variables. A struct lets you make your own data type by grouping several values, even of different types, under one name. Arrays from Module 6 group many values of the same type. Structs group values of different types.

**\[4 · Code line by line\]** Let's make the card. \[HL 2\] Line 2 includes string.h, because we will use strcpy from Module 7. \[HL 4\] Line 4: the keyword struct, then the name Student, then an opening brace. This is the blank design. \[HL 5\] \[HL 6\] \[HL 7\] Lines 5 to 7 are the members, the fields on the card: a char array name of 30 characters, an int rollNo, a float percentage. \[HL 8\] Line 8: closing brace AND a semicolon. Do not forget that semicolon. This defines the type. It does not create any variable yet and uses no memory for a student. \[HL 11\] Line 11: struct Student s1. Now we have a real card, called s1. Notice we write both words: struct Student. In C, the type name is the whole phrase. \[HL 13\] Line 13 fills the name. We use the dot operator: s1 dot name means the name field of s1. Because name is a char array, we cannot write equals with a string. We use strcpy, just like in EP 49. \[TRACK s1.name="Anya Naik"\] \[HL 14\] Line 14: s1 dot rollNo equals 17. \[TRACK s1.rollNo=17\] \[HL 15\] Line 15: s1 dot percentage equals 88.5. The f at the end makes it a float literal. \[TRACK s1.percentage=88.5\] \[HL 17\] Line 17 shows the second way: fill a card at the moment you create it, with values in curly braces, in the same order as the members. Rohan Gaonkar, 23, 91.25. \[TRACK s2.name="Rohan Gaonkar"\] \[TRACK s2.rollNo=23\] \[TRACK s2.percentage=91.25\] \[HL 19\] Lines 19 to 25 print each member with the dot operator and the right format code: percent s for the name, percent d for the roll, percent point 2 f for the percentage.

**\[5 · Memory picture\]** What does s1 look like in memory? One block. Inside it, side by side: 30 bytes for the name, then the int, then the float. All of s1 lives together, in one piece. When you write s1 dot rollNo, C goes to the start of s1 and jumps to where rollNo sits inside it. On a typical machine this struct is 40 bytes, but your size may differ, and in EP 64 we will see why struct sizes sometimes surprise you.

**\[6 · Pun\]** Why did the variables join a struct? They wanted to be part of something bigger, with good member benefits.

**\[7 · Copying a struct\]** One more superpower. Arrays cannot be copied with equals, remember EP 41. But structs can. Write struct Student s3 equals s1, and every member is copied, even the name array inside. It is a photocopy. Then change s3 dot rollNo to 99. Print both roll numbers: 17 and 99. The original card is untouched. Two separate cards, two separate memories.

**\[8 · Bug of the Day\]** Today's bug: forgetting the struct keyword. Here, someone writes Student s1, without the word struct. Compile, and GCC says: error: unknown type name Student; use struct keyword to refer to the type. GCC 13 even shows the fix, writing struct right under the mistake. Then two more errors follow: request for member rollNo in something not a structure or union. That is a chain reaction from the first error, so always fix the first error first. Why does this happen? In C, the type is named struct Student, both words. Student alone means nothing. If you have used C plus plus, you may expect Student alone to work. In C, it does not. In EP 63, we learn typedef, which lets you give the type a short nickname. And a bonus bug: forget the semicolon after the closing brace of the struct, and GCC says expected semicolon, identifier or bracket before int, pointing at the next line. The struct definition swallowed the next line.

**\[9 · Challenge\]** Your challenge: make a struct Book with a title, an author, a number of pages, and a price. Create one book with an initialiser list, and print all four fields neatly. Use your favourite book. Answer in the comments.

**\[10 · Outro\]** One card is nice. But a class has many students. Next episode we make an array of structs, a whole class register, and meet a new arrow operator. EP 62. Keep coding, says Xecxec!

### Code shown

File 1, ep61.c:

```c
#include <stdio.h>
#include <string.h>

struct Student {
    char name[30];
    int rollNo;
    float percentage;
};

int main(void) {
    struct Student s1;

    strcpy(s1.name, "Anya Naik");
    s1.rollNo = 17;
    s1.percentage = 88.5f;

    struct Student s2 = {"Rohan Gaonkar", 23, 91.25f};

    printf("Name: %s\n", s1.name);
    printf("Roll: %d\n", s1.rollNo);
    printf("Percent: %.2f\n\n", s1.percentage);

    printf("Name: %s\n", s2.name);
    printf("Roll: %d\n", s2.rollNo);
    printf("Percent: %.2f\n", s2.percentage);

    return 0;
}
```

**Expected output:**

```text
Name: Anya Naik
Roll: 17
Percent: 88.50

Name: Rohan Gaonkar
Roll: 23
Percent: 91.25
```

File 2, ep61copy.c (scene 7):

```c
#include <stdio.h>

struct Student {
    char name[30];
    int rollNo;
    float percentage;
};

int main(void) {
    struct Student s1 = {"Anya Naik", 17, 88.5f};
    struct Student s3 = s1;

    s3.rollNo = 99;
    printf("s1 roll: %d, s3 roll: %d\n", s1.rollNo, s3.rollNo);

    return 0;
}
```

**Expected output:**

```text
s1 roll: 17, s3 roll: 99
```

### Bug of the Day

Wrong code:

```c
#include <stdio.h>

struct Student {
    char name[30];
    int rollNo;
};

int main(void) {
    Student s1;
    s1.rollNo = 17;
    printf("%d\n", s1.rollNo);
    return 0;
}
```

GCC 13 output (first error, then the chain reaction):

```text
ep61bug.c: In function 'main':
ep61bug.c:9:5: error: unknown type name 'Student'; use 'struct' keyword to refer to the type
    9 |     Student s1;
      |     ^~~~~~~
      |     struct 
ep61bug.c:10:7: error: request for member 'rollNo' in something not a structure or union
   10 |     s1.rollNo = 17;
      |       ^
```

Bonus (missing `;` after the struct's closing brace):

```text
ep61bug2.c:8:1: error: expected ';', identifier or '(' before 'int'
```

Fixed code:

```c
#include <stdio.h>

struct Student {
    char name[30];
    int rollNo;
};

int main(void) {
    struct Student s1;
    s1.rollNo = 17;
    printf("%d\n", s1.rollNo);
    return 0;
}
```

Output after the fix:

```text
17
```

Why: in C the type's full name is `struct Student`; the tag `Student` alone is not a type name unless you add a `typedef` (EP 63).

### Pun & challenge

- **Pun:** Why did the variables join a struct? They wanted to be part of something bigger, with good member benefits.
- **Challenge:** Define `struct Book` with title, author, pages and price. Create one book with an initialiser list and print all four fields.
- **Challenge answer:**

```c
struct Book {
    char title[50];
    char author[40];
    int pages;
    float price;
};

struct Book b = {"Wings of Fire", "A. P. J. Abdul Kalam", 180, 299.0f};
printf("Title : %s\n", b.title);
printf("Author: %s\n", b.author);
printf("Pages : %d\n", b.pages);
printf("Price : Rs %.2f\n", b.price);
```

### Shorts for EP 61

**S1 · Stop using loose variables** — 0:25 · built from scenes 1 and 3

- **Hook (first 1.5s):** Papers labelled name1, roll1, pct1 blow away. Xecxec chases them.
- **Script:** Name, roll number, percentage. Three loose variables per student. A whole class? Hundreds. A struct groups values that belong together into one new type. Like a blank ID card design. Then every student gets their own filled card. One name, all the details inside.
- **On-screen text:** ONE STUDENT = ONE STRUCT
- **Caption + hashtags:** Your first user-defined type in C. #cprogramming #learntocode #kodingkonkani #structs #codingforbeginners

**S2 · struct in 30 seconds** — 0:30 · built from scene 4

- **Hook (first 1.5s):** An ID card whose fields fill in one by one
- **Script:** struct in 30 seconds. Write struct, a name, and the members in braces. Semicolon at the end. That is the design. struct Student s1 creates a real card. Use the dot to reach a member: s1 dot rollNo equals 17. Or fill everything at once with values in braces, in member order. For a char array member, use strcpy.
- **On-screen text:** s1.rollNo = 17;
- **Caption + hashtags:** Define, create, fill, print. #cprogramming #learntocode #kodingkonkani #ctutorial #programming

**S3 · unknown type name** — 0:30 · built from scene 8

- **Hook (first 1.5s):** Red error text: "unknown type name 'Student'"
- **Script:** You defined struct Student. Then you wrote Student s1. GCC says: unknown type name Student, use struct keyword. In C, the type is called struct Student. Both words. Student alone means nothing. GCC 13 even shows you the fix. Want a short name? That is typedef, coming in EP 63.
- **On-screen text:** IT'S struct Student, NOT Student
- **Caption + hashtags:** The C plus plus habit that breaks your C code. #cprogramming #debugging #kodingkonkani #learntocode #codinglife

**S4 · Member benefits** — 0:12 · built from scene 6

- **Hook (first 1.5s):** Three variables in suits signing a membership form
- **Script:** Why did the variables join a struct? They wanted to be part of something bigger, with good member benefits.
- **On-screen text:** GOOD MEMBER BENEFITS
- **Caption + hashtags:** Join the struct. #programmerhumor #cprogramming #kodingkonkani #codingjokes

**S5 · Can you copy a struct?** — 0:25 · built from scenes 7 and 9

- **Hook (first 1.5s):** "s3 = s1;" with a big question mark
- **Script:** Quiz. Arrays cannot be copied with equals. Can structs? Three, two, one. Yes! s3 equals s1 copies every member, even arrays inside. Change s3, and s1 stays the same. Now your challenge: make a struct Book with title, author, pages and price, and print it. Answer in the comments.
- **On-screen text:** s3 = s1; ALLOWED?
- **Caption + hashtags:** Arrays can't, structs can. Did you know? #cprogramming #codingquiz #kodingkonkani #learntocode #structs

## EP 62 — Structs, arrays & pointers

**Module 9 · Structures · 6:40 · Cream + Tomato · Prerequisite: EP 61**

**Learning goals:** declare and initialise an array of structs; reach a member with `cls[i].marks`; point to a struct and use the arrow `->`; explain that `p->x` means `(*p).x`; pass a struct to a function by pointer so the function can change it.

### YouTube

- **Title:** Array of Structs and the Arrow -> | C Programming EP 62
- **Description:** One student card is easy. A whole class register needs an array of structs. Today we store three students, loop through them, change one through a pointer with the arrow operator, and settle the dot versus arrow confusion for good. Chapters: 0:00 The class register · 0:25 Array of structs · 1:05 Pointers to structs · 1:45 Code line by line · 3:40 Running it · 4:05 Dot or arrow? · 4:40 Bug of the Day · 5:50 Challenge
- **Tags:** c programming, array of structures in c, arrow operator in c, pointer to structure, struct and pointers, dot vs arrow, learn c, c for beginners, koding konkani, c tutorial english
- **Thumbnail:** big text ". OR -> ?"; a class register book with three ID cards in a row and a pointer arrow aimed at one; Xecxec holding a dot in one claw and an arrow in the other, confused; cream background, tomato blocks

### Scene list

| # | Start | Length | Template | On screen | Animation & SFX |
| --- | --- | --- | --- | --- | --- |
| 1 | 0:00 | 0:20 | Concept slide | A class register book opens to a page of names | Page flip, school bell |
| 2 | 0:20 | 0:05 | Title card | EP 62 · STRUCTS, ARRAYS & POINTERS | Title slam, whoosh |
| 3 | 0:25 | 0:40 | Memory boxes | cls\[0\], cls\[1\], cls\[2\] as three ID cards in a row, each with name, rollNo, marks | Cards slide in left to right, index labels pop |
| 4 | 1:05 | 0:40 | Memory boxes | Pointer p (GPS pin from EP 53) aimed at cls\[1\]; p->marks highlights the marks field | Pin drops, arrow draws, ping |
| 5 | 1:45 | 1:55 | Code explain | ep62.c, 35 lines; tracker shows the 3 cards and pointer p/top | Line highlights; marks field ticks 64.5 to 69.5; key-tap SFX |
| 6 | 3:40 | 0:20 | Terminal | Program output, 5 lines | Typing SFX, rows print like a register |
| 7 | 4:00 | 0:05 | Pun card | Pun line | Drum hit, claw-click |
| 8 | 4:05 | 0:35 | Concept slide | Rule card: have the struct? use . · have a pointer? use -> · p->x is (\*p).x | Two columns stamp in; equals sign glows |
| 9 | 4:40 | 1:10 | Bug of the Day | p.marks inside a function taking a pointer | Red underline, error buzz; GCC's "->" suggestion slides in |
| 10 | 5:50 | 0:30 | Challenge | Read 5 student records, print the topper | Five cards fill, crown on the topper; timer ring |
| 11 | 6:20 | 0:20 | Outro | Next: EP 63 typedef and enum; sign-off | Module tiles, claw-click, music out |

### Narration script

**\[1 · The class register\]** Every morning, the teacher opens the class register. One row per student: name, roll number, marks. In EP 61 we made one student card. But a class has forty students. We are not going to write s1, s2, s3, all the way to s40. You already know the answer from Module 6: an array. Only this time, an array of structs.

**\[2 · Title\]** Episode 62. Structs, arrays and pointers.

**\[3 · Array of structs\]** An array of structs is a row of lockers, where every locker holds a whole ID card. cls zero is the first card, cls one the second, cls two the third. To reach one field, you combine what you know. First the index in square brackets to pick the card, then the dot to pick the field. cls one dot marks means: the marks of the second student. Read it left to right: which card, then which field.

**\[4 · Pointers to structs\]** Now pointers. In EP 53, a pointer was a GPS pin holding an address. A pointer can hold the address of a whole struct too. Say p points to cls one. To get the marks, you could write star p in brackets, dot marks: first go to the address, then pick the field. The brackets are needed because the dot is stronger than the star. That is ugly, and programmers write it all the time. So C gives a shortcut: p arrow marks. A minus sign and a greater-than sign, and it means exactly the same thing. Go to the struct p points at, and take its marks.

**\[5 · Code line by line\]** Let's see it in a real program. \[HL 3\] Lines 3 to 7 define struct Student, with name, rollNo and marks. \[HL 9\] Line 9: a function printStudent that takes a pointer to a Student, called p. Why a pointer? A struct can be big. Passing a pointer sends just one address instead of copying the whole card. \[HL 10\] Line 10 prints the three fields with the arrow: p arrow name, p arrow rollNo, p arrow marks. The percent minus 8 s pads the name to 8 characters so the columns line up, from EP 11. \[HL 13\] Line 13: a function addGrace, also taking a pointer, plus a bonus. \[HL 14\] Line 14: p arrow marks equals p arrow marks plus bonus. Because we have the address, we change the real struct, not a copy. That is call by reference from EP 55. \[HL 18\] Now main. Line 18: struct Student cls, size 3, equals, and then lines 19 to 21: one set of braces per student, all inside an outer pair of braces. Anya, roll 1, 78. Rohan, roll 2, 64.5. Sneha, roll 3, 91. \[TRACK cls\[1\].marks=64.5\] \[HL 24\] Line 24: addGrace with ampersand cls one, and 5. The ampersand gives the address of the second card. Inside the function, p points to Rohan's card, and his marks go up by 5. \[TRACK cls\[1\].marks=69.5\] \[HL 26\] Lines 26 to 28 loop over all three students, with the for loop from EP 27, and pass the address of each card to printStudent. \[HL 30\] Line 30: a pointer called top, holding the address of cls two, Sneha's card. \[HL 31\] Line 31 prints top arrow name. \[HL 32\] And line 32 prints the long form, star top in brackets, dot name. Both print Sneha. Same thing, two spellings.

**\[6 · Running it\]** Compile and run. Anya, roll 1, 78. Rohan, roll 2, 69.5: the grace marks worked, because we changed the real card through a pointer. Sneha, roll 3, 91. Topper: Sneha. Same thing: Sneha.

**\[7 · Pun\]** Why did the pointer always get to the struct first? It knew exactly which way the arrow was pointing.

**\[8 · Dot or arrow?\]** Here is the one rule. Ask yourself: what do I have in my claw? If you have the struct itself, like s or cls one, use the dot. If you have a pointer to a struct, like p or top, use the arrow. And remember, p arrow x is only a shortcut for star p in brackets, dot x. Nothing magic.

**\[9 · Bug of the Day\]** Today's bug: dot versus arrow. Here is addGrace again, but someone wrote p dot marks. p is a pointer, not a struct. Compile it, and GCC 13 says: error: p is a pointer; did you mean to use arrow? And it even draws the arrow under the dot. GCC is very kind today. The opposite mistake happens too. If s is a real struct and you write s arrow marks, GCC says: invalid type argument of arrow, have struct Student. That means: you used an arrow, but you have a struct, not a pointer. The fix in both cases: check what you have. Pointer, arrow. Struct, dot.

**\[10 · Challenge\]** Your challenge: make an array of 5 Student structs. Read the name, roll number and marks of each student with scanf in a loop. Then print the topper's name, roll number and marks. Hint: keep the index of the best student so far, like finding the maximum in EP 42. Answer in the comments.

**\[11 · Outro\]** Writing struct Student again and again is getting long, and our programs are full of magic numbers. Next episode, typedef gives our types nicknames, and enum gives our numbers names. EP 63. Keep coding, says Xecxec!

### Code shown

```c
#include <stdio.h>

struct Student {
    char name[30];
    int rollNo;
    float marks;
};

void printStudent(struct Student *p) {
    printf("%-8s roll %2d  marks %.1f\n", p->name, p->rollNo, p->marks);
}

void addGrace(struct Student *p, float bonus) {
    p->marks = p->marks + bonus;
}

int main(void) {
    struct Student cls[3] = {
        {"Anya", 1, 78.0f},
        {"Rohan", 2, 64.5f},
        {"Sneha", 3, 91.0f}
    };

    addGrace(&cls[1], 5.0f);

    for (int i = 0; i < 3; i++) {
        printStudent(&cls[i]);
    }

    struct Student *top = &cls[2];
    printf("Topper: %s\n", top->name);
    printf("Same thing: %s\n", (*top).name);

    return 0;
}
```

**Expected output:**

```text
Anya     roll  1  marks 78.0
Rohan    roll  2  marks 69.5
Sneha    roll  3  marks 91.0
Topper: Sneha
Same thing: Sneha
```

### Bug of the Day

Wrong code:

```c
#include <stdio.h>

struct Student {
    char name[30];
    int rollNo;
    float marks;
};

void addGrace(struct Student *p, float bonus) {
    p.marks = p.marks + bonus;
}

int main(void) {
    struct Student s = {"Rohan", 2, 64.5f};
    addGrace(&s, 5.0f);
    printf("%.1f\n", s.marks);
    return 0;
}
```

GCC 13 output:

```text
ep62bug.c: In function 'addGrace':
ep62bug.c:10:6: error: 'p' is a pointer; did you mean to use '->'?
   10 |     p.marks = p.marks + bonus;
      |      ^
      |      ->
ep62bug.c:10:16: error: 'p' is a pointer; did you mean to use '->'?
   10 |     p.marks = p.marks + bonus;
      |                ^
      |                ->
```

The opposite mistake (`s->marks` where `s` is a struct, not a pointer):

```text
error: invalid type argument of '->' (have 'struct Student')
```

Fixed line (everything else unchanged):

```c
    p->marks = p->marks + bonus;
```

Output after the fix:

```text
69.5
```

Why: the dot needs a struct and the arrow needs a pointer to a struct; `p->marks` is shorthand for `(*p).marks`.

### Pun & challenge

- **Pun:** Why did the pointer always get to the struct first? It knew exactly which way the arrow was pointing.
- **Challenge:** Read 5 student records (name, roll, marks) into an array of structs, then print the topper's name, roll and marks.
- **Challenge answer:**

```c
struct Student cls[5];
int best = 0;

for (int i = 0; i < 5; i++) {
    printf("Name, roll, marks for student %d: ", i + 1);
    scanf("%29s %d %f", cls[i].name, &cls[i].rollNo, &cls[i].marks);
    if (cls[i].marks > cls[best].marks)
        best = i;
}

printf("\nTopper: %s (roll %d) with %.1f\n",
       cls[best].name, cls[best].rollNo, cls[best].marks);
/* note: no & before cls[i].name, because an array name is already an address (EP 57) */
```

### Shorts for EP 62

**S1 · A whole class in one variable** — 0:25 · built from scenes 1 and 3

- **Hook (first 1.5s):** Register book slams open: "40 students. 1 variable."
- **Script:** Forty students. You are not writing s1 to s40. Make an array of structs. Every slot holds a whole ID card. To reach a field, pick the card with the index, then the field with a dot. cls one dot marks: the second student's marks. Which card, then which field.
- **On-screen text:** cls\[1\].marks
- **Caption + hashtags:** An array where every slot is a whole struct. #cprogramming #learntocode #kodingkonkani #structs #codingforbeginners

**S2 · The arrow in 30 seconds** — 0:30 · built from scenes 4 and 8

- **Hook (first 1.5s):** A GPS pin drops on an ID card: "p->marks"
- **Script:** The arrow in 30 seconds. p is a pointer to a struct. To reach its marks, you could write star p in brackets, dot marks. Brackets needed, because dot is stronger than star. Too ugly. So C gives a shortcut: p arrow marks. Same meaning. The rule: have the struct, use dot. Have a pointer, use arrow.
- **On-screen text:** p->x == (\*p).x
- **Caption + hashtags:** Dot vs arrow, settled forever. #cprogramming #learntocode #kodingkonkani #pointers #ctutorial

**S3 · "did you mean to use ->?"** — 0:30 · built from scene 9

- **Hook (first 1.5s):** Error: "'p' is a pointer; did you mean to use '->'?"
- **Script:** p is a pointer to a struct, and you wrote p dot marks. GCC says: p is a pointer, did you mean to use arrow? It even draws it for you. The reverse also fails: a real struct with an arrow gives invalid type argument of arrow. Fix: pointer, arrow. Struct, dot.
- **On-screen text:** POINTER → ARROW · STRUCT → DOT
- **Caption + hashtags:** GCC literally tells you the fix. #cprogramming #debugging #kodingkonkani #learntocode #codinglife

**S4 · Which way the arrow points** — 0:12 · built from scene 7

- **Hook (first 1.5s):** A pointer racing a dot to a struct; the pointer wins
- **Script:** Why did the pointer always get to the struct first? It knew exactly which way the arrow was pointing.
- **On-screen text:** IT KNEW WHERE THE ARROW POINTED
- **Caption + hashtags:** Pointers have a great sense of direction. #programmerhumor #cprogramming #kodingkonkani #codingjokes

**S5 · Dot or arrow quiz** — 0:30 · built from scenes 8 and 10

- **Hook (first 1.5s):** "&cls\[2\] → top. top?name"
- **Script:** Quiz. top equals ampersand cls two. To print the name, is it top dot name or top arrow name? Three, two, one. Arrow! top holds an address, so it is a pointer. cls two dot name would also work, because cls two is the struct itself. Now your challenge: read 5 students and print the topper. Answer in the comments.
- **On-screen text:** top.name OR top->name?
- **Caption + hashtags:** Got it in 3 seconds? #cprogramming #codingquiz #kodingkonkani #learntocode #structs

## EP 63 — typedef & enum

**Module 9 · Structures · 6:30 · Cream + Tomato · Prerequisite: EP 62**

**Learning goals:** use `typedef` to give a struct or enum a short type name; define an `enum` and know its values are ints starting at 0; set custom enum values and predict the ones that follow; use an enum in a `switch`; avoid enumerator name clashes by prefixing names.

### YouTube

- **Title:** typedef and enum: Give Your Types Nicknames | C Programming EP 63
- **Description:** Tired of typing struct Student everywhere? Tired of remembering that 2 means green? Today typedef gives your types short names and enum gives your numbers real names. We build a Goa bus signal with both, and see why two enums cannot share a name. Chapters: 0:00 Magic numbers · 0:25 typedef · 1:00 enum · 1:45 Code line by line · 3:35 Running it · 3:55 Custom enum values · 4:40 Bug of the Day · 5:45 Challenge
- **Tags:** c programming, typedef in c, enum in c, enumeration, typedef struct, named constants, switch with enum, learn c, koding konkani, c tutorial english
- **Thumbnail:** big text "2 = GREEN??"; a traffic signal with 0, 1, 2 on the lights turning into RED, YELLOW, GREEN name tags; Xecxec wearing a name badge that says "Hi, I'm Bus"; cream background, tomato blocks

### Scene list

| # | Start | Length | Template | On screen | Animation & SFX |
| --- | --- | --- | --- | --- | --- |
| 1 | 0:00 | 0:20 | Concept slide | Code with `light = 2;` and `struct Student` repeated 6 times | Xecxec squints at the 2; typing fatigue groan |
| 2 | 0:20 | 0:05 | Title card | EP 63 · TYPEDEF & ENUM | Title slam, whoosh |
| 3 | 0:25 | 0:35 | Concept slide | Name badge: "struct Student" gets a nickname tag "Student" | Badge sticker slaps on; sticker SFX |
| 4 | 1:00 | 0:45 | Concept slide | Traffic light: 0, 1, 2 become RED, YELLOW, GREEN | Numbers flip to name tags one by one; click |
| 5 | 1:45 | 1:50 | Code explain | ep63.c, 36 lines; tracker shows b.route, b.seats, b.light | Line highlights; signal light changes colour with the tracker; key-tap SFX |
| 6 | 3:35 | 0:15 | Terminal | Program output, 3 lines | Typing SFX, bus horn on "Bus goes!" |
| 7 | 3:50 | 0:05 | Pun card | Pun line | Drum hit, claw-click |
| 8 | 3:55 | 0:45 | Code explain | ep63b.c, Month enum with JAN = 1 and JUN = 6 | Number counter ticks 1, 2, 3, jumps to 6, 7 |
| 9 | 4:40 | 1:05 | Bug of the Day | Two enums both using RED | Two RED tags collide, error buzz; prefixes SIGNAL\_ and FRUIT\_ slide in |
| 10 | 5:45 | 0:25 | Challenge | Enum for days, weekend check | Calendar flip, timer ring |
| 11 | 6:10 | 0:20 | Outro | Next: EP 64 union and memory layout; sign-off | Module tiles, claw-click, music out |

### Narration script

**\[1 · Magic numbers\]** Look at this line: light equals 2. What does 2 mean? Red? Green? Bus number 2? Nobody knows, not even you, three weeks later. And look here: struct Student, struct Student, struct Student, six times in one file. Our code is long and full of mystery numbers. Today we fix both problems with two small keywords.

**\[2 · Title\]** Episode 63. typedef and enum.

**\[3 · typedef\]** In Goa, everybody has a nickname. Your full name might be long, but at the fish market, everyone calls you by a short one. typedef gives a type a nickname. You write typedef, then the existing type, then the new short name. After that, both names work, and they mean exactly the same type. typedef does not create a new kind of data. It only creates a new name. And remember the bug from EP 61, writing Student without struct? With typedef, that is exactly what you are allowed to do.

**\[4 · enum\]** Now the mystery 2. An enum, short for enumeration, is a list of named whole-number constants. You write enum, and inside braces: RED, YELLOW, GREEN. C quietly numbers them: RED is 0, YELLOW is 1, GREEN is 2. Now instead of light equals 2, you write light equals GREEN. The computer still stores 2. But the human reading it understands it instantly. It is like #define from EP 10, but the names are grouped together and belong to one type.

**\[5 · Code line by line\]** Let's build a Goa bus signal. \[HL 3\] Lines 3 to 7: typedef enum, then in braces RED, YELLOW, GREEN, then after the closing brace, the name Signal. This does two things at once: it makes the enum, and gives it the short name Signal. Enumerator names are usually in capital letters, like constants. \[HL 9\] Lines 9 to 13: the same trick for a struct. typedef struct, the members, and the name Bus at the end. The members are a route string, a number of seats, and a light of type Signal. Yes, a struct member can be an enum. \[HL 15\] Line 15: a function signalName that takes a Signal and returns a string, a const char pointer, from EP 58. \[HL 16\] Inside, a switch from EP 23. switch works on enums, because enums are whole numbers. \[HL 17\] case RED returns the text RED. \[HL 18\] \[HL 19\] YELLOW, GREEN. \[HL 20\] Default returns UNKNOWN, just in case. We return directly, so no break is needed: return leaves the function immediately. \[HL 25\] Now main. Line 25: Bus b. Just Bus. No struct keyword, thanks to typedef. We fill it with the route Panaji-Mapusa, 40 seats, and the light RED. \[TRACK b.route="Panaji-Mapusa"\] \[TRACK b.seats=40\] \[TRACK b.light=RED\] \[HL 27\] Line 27 prints the route and seats. \[HL 28\] Line 28 prints the signal name and also its number with percent d. RED is 0. \[HL 30\] Line 30: b dot light equals GREEN. \[TRACK b.light=GREEN\] \[HL 31\] Line 31: if b dot light equals GREEN. Read it aloud. It sounds like English. That is the whole point. \[HL 32\] Bus goes!

**\[6 · Running it\]** Compile and run. Route: Panaji-Mapusa, seats: 40. Signal: RED, value 0. Signal: GREEN. Bus goes!

**\[7 · Pun\]** Why did the enum get the job at the traffic signal? It had all the right constants and never changed its mind.

**\[8 · Custom enum values\]** You can choose the numbers. In ep63b.c we have enum Month, with JAN equals 1. Then FEB and MAR with no value. The rule is simple: each enumerator without a value is one more than the one before. So FEB is 2, MAR is 3. Then JUN equals 6, and JUL is 7. The program prints 1, 2, 3, 6, 7. Use this when the numbers mean something real, like month numbers, or error codes.

**\[9 · Bug of the Day\]** Today's bug: enum values that clash. We have enum Signal with RED, YELLOW, GREEN. Then someone adds enum Fruit with APPLE, MANGO, and RED, because some apples are red. Compile. GCC says: error: redeclaration of enumerator RED. And a note: previous definition of RED with type enum Signal. Why? In C, enumerator names are not kept inside their enum. They all live in the same big room as your variables and functions. Two things in one room cannot have the same name. So if RED already means 0 for Signal, it cannot also mean something for Fruit. The fix: give each enum's names a prefix. SIGNAL\_RED, SIGNAL\_YELLOW, SIGNAL\_GREEN. FRUIT\_APPLE, FRUIT\_MANGO, FRUIT\_RED. Longer, but clear, and no clash. Real C libraries do this all the time.

**\[10 · Challenge\]** Your challenge: make a typedef enum Day with MON equal to 1, then TUE to SUN. Create a Day variable today, set it to SAT, and print "Weekend! Beach time." if it is SAT or SUN, otherwise "Weekday. Class time." Print the day number too. Answer in the comments.

**\[11 · Outro\]** Next episode: a strange cousin of the struct called union, where all members share one memory box. Plus the mystery of why sizeof sometimes lies to you. EP 64. Keep coding, says Xecxec!

### Code shown

File 1, ep63.c:

```c
#include <stdio.h>

typedef enum {
    RED,
    YELLOW,
    GREEN
} Signal;

typedef struct {
    char route[20];
    int seats;
    Signal light;
} Bus;

const char *signalName(Signal s) {
    switch (s) {
        case RED:    return "RED";
        case YELLOW: return "YELLOW";
        case GREEN:  return "GREEN";
        default:     return "UNKNOWN";
    }
}

int main(void) {
    Bus b = {"Panaji-Mapusa", 40, RED};

    printf("Route: %s, seats: %d\n", b.route, b.seats);
    printf("Signal: %s (value %d)\n", signalName(b.light), b.light);

    b.light = GREEN;
    if (b.light == GREEN) {
        printf("Signal: %s. Bus goes!\n", signalName(b.light));
    }

    return 0;
}
```

**Expected output:**

```text
Route: Panaji-Mapusa, seats: 40
Signal: RED (value 0)
Signal: GREEN. Bus goes!
```

File 2, ep63b.c:

```c
#include <stdio.h>

enum Month { JAN = 1, FEB, MAR, JUN = 6, JUL };

int main(void) {
    printf("%d %d %d %d %d\n", JAN, FEB, MAR, JUN, JUL);
    return 0;
}
```

**Expected output:**

```text
1 2 3 6 7
```

### Bug of the Day

Wrong code:

```c
#include <stdio.h>

enum Signal { RED, YELLOW, GREEN };
enum Fruit  { APPLE, MANGO, RED };

int main(void) {
    enum Signal s = RED;
    printf("%d\n", s);
    return 0;
}
```

GCC 13 output:

```text
ep63bug.c:4:29: error: redeclaration of enumerator 'RED'
    4 | enum Fruit  { APPLE, MANGO, RED };
      |                             ^~~
ep63bug.c:3:15: note: previous definition of 'RED' with type 'enum Signal'
    3 | enum Signal { RED, YELLOW, GREEN };
      |               ^~~
```

Fixed code:

```c
#include <stdio.h>

enum Signal { SIGNAL_RED, SIGNAL_YELLOW, SIGNAL_GREEN };
enum Fruit  { FRUIT_APPLE, FRUIT_MANGO, FRUIT_RED };

int main(void) {
    enum Signal s = SIGNAL_RED;
    printf("%d\n", s);
    return 0;
}
```

Output after the fix:

```text
0
```

Why: all enumerator names in C share one scope with other identifiers, so two enums cannot both define `RED`; prefixes keep them unique.

### Pun & challenge

- **Pun:** Why did the enum get the job at the traffic signal? It had all the right constants and never changed its mind.
- **Challenge:** `typedef enum` Day with MON = 1 up to SUN. Set `today = SAT`; print the day number and "Weekend! Beach time." for SAT/SUN, else "Weekday. Class time."
- **Challenge answer:**

```c
typedef enum { MON = 1, TUE, WED, THU, FRI, SAT, SUN } Day;

Day today = SAT;
if (today == SAT || today == SUN)
    printf("Day %d: Weekend! Beach time.\n", today);
else
    printf("Day %d: Weekday. Class time.\n", today);
/* prints: Day 6: Weekend! Beach time. */
```

### Shorts for EP 63

**S1 · What does 2 mean?** — 0:25 · built from scenes 1 and 4

- **Hook (first 1.5s):** `light = 2;` with a giant question mark. Xecxec squints.
- **Script:** light equals 2. Is that red? Green? Bus number 2? Mystery numbers make code impossible to read. An enum gives numbers names. RED is 0, YELLOW is 1, GREEN is 2. Now you write light equals GREEN. The computer still stores 2. But every human understands it.
- **On-screen text:** light = GREEN; NOT light = 2;
- **Caption + hashtags:** Stop writing mystery numbers. #cprogramming #learntocode #kodingkonkani #enum #codingforbeginners

**S2 · typedef in 30 seconds** — 0:30 · built from scenes 3 and 5

- **Hook (first 1.5s):** "struct Student" gets a sticker: "Hi, I'm Student"
- **Script:** typedef in 30 seconds. It gives a type a nickname. typedef struct, the members in braces, then the short name, like Bus. Now you write Bus b, without the word struct. It does not make a new type, only a new name for it. Works with enums too: typedef enum, the values, then Signal.
- **On-screen text:** typedef = NICKNAME
- **Caption + hashtags:** Shorter code, same meaning. #cprogramming #learntocode #kodingkonkani #typedef #ctutorial

**S3 · Two REDs, one error** — 0:30 · built from scene 9

- **Hook (first 1.5s):** Two RED tags crash into each other
- **Script:** enum Signal has RED. enum Fruit also has RED. GCC says: redeclaration of enumerator RED. In C, enum names do not live inside their enum. They all share one big room. Two things, one name, not allowed. Fix: prefixes. SIGNAL\_RED and FRUIT\_RED. Real C libraries do exactly this.
- **On-screen text:** redeclaration of enumerator 'RED'
- **Caption + hashtags:** Why C enums need prefixes. #cprogramming #debugging #kodingkonkani #learntocode #codinglife

**S4 · Never changed its mind** — 0:12 · built from scene 7

- **Hook (first 1.5s):** Traffic light in a job interview suit
- **Script:** Why did the enum get the job at the traffic signal? It had all the right constants and never changed its mind.
- **On-screen text:** ALL THE RIGHT CONSTANTS
- **Caption + hashtags:** Hired. #programmerhumor #cprogramming #kodingkonkani #codingjokes

**S5 · What is JUL?** — 0:25 · built from scenes 8 and 10

- **Hook (first 1.5s):** `enum { JAN = 1, FEB, MAR, JUN = 6, JUL };` "JUL = ?"
- **Script:** Quiz. JAN equals 1, then FEB, MAR, then JUN equals 6, then JUL. What is JUL? Three, two, one. 7! Each name without a value is one more than the one before. And MAR is 3. Your challenge: make a Day enum and check for the weekend. Answer in the comments.
- **On-screen text:** JUL = ?
- **Caption + hashtags:** Enum counting rules in 25 seconds. #cprogramming #codingquiz #kodingkonkani #learntocode #enum

## EP 64 — union & memory layout

**Module 9 · Structures · 6:45 · Cream + Tomato · Prerequisite: EP 63**

**Learning goals:** explain why `sizeof` a struct can be larger than the sum of its members (padding and alignment); reorder members to shrink a struct; define a `union` and explain that all members share one memory block; predict a union's size; keep track of which union member is valid with an enum tag.

### YouTube

- **Title:** Why sizeof Lied to You: Padding and union | C Programming EP 64
- **Description:** A char, an int and a char add up to 6 bytes. So why does sizeof say 12? Today we open the memory boxes, find the hidden padding, shrink the struct by reordering it, and meet union: the struct where every member lives in the same box. Chapters: 0:00 6 or 12? · 0:25 Padding and alignment · 1:25 Reorder to shrink · 1:55 What a union is · 2:35 Code line by line · 4:10 Running it · 4:35 Bug of the Day · 6:00 Challenge
- **Tags:** c programming, union in c, structure padding, memory alignment, sizeof struct, struct vs union, tagged union, learn c, koding konkani, c tutorial english
- **Thumbnail:** big text "6 + 0 = 12?"; a row of memory boxes with three grey "padding" boxes glowing; Xecxec holding a measuring tape, shocked; cream background, tomato blocks

### Scene list

| # | Start | Length | Template | On screen | Animation & SFX |
| --- | --- | --- | --- | --- | --- |
| 1 | 0:00 | 0:20 | Terminal | `char + int + char = 6 bytes` then `sizeof(struct Order) = 12` | Typing SFX; record scratch on 12 |
| 2 | 0:20 | 0:05 | Title card | EP 64 · UNION & MEMORY LAYOUT | Title slam, whoosh |
| 3 | 0:25 | 1:00 | Memory boxes | struct Order as 12 bytes: size, 3 padding, qty (4), type, 3 padding | Byte boxes fill; padding boxes appear in grey with a hiss; label "typical x86/x64 GCC, your sizes may differ" |
| 4 | 1:25 | 0:30 | Memory boxes | struct Packed: qty (4), size, type, 2 padding = 8 | Members slide into new order; boxes snap tighter; satisfying click |
| 5 | 1:55 | 0:40 | Concept slide | Struct = three separate lockers; union = one locker shared by three tenants | Three locker doors merge into one; tenants swap in and out |
| 6 | 2:35 | 1:35 | Code explain | ep64.c, 36 lines; tracker shows union v as one 4-byte box | Line highlights; the single box's label changes i / f / c; key-tap SFX |
| 7 | 4:10 | 0:20 | Terminal | Full program output, 8 lines | Typing SFX |
| 8 | 4:30 | 0:05 | Pun card | Pun line | Drum hit, claw-click |
| 9 | 4:35 | 1:25 | Bug of the Day | Write v.f = 2.5, read v.i, get 1075838976 | Bits pour into the box as a float, read out as an int; error buzz; enum tag badge snaps on |
| 10 | 6:00 | 0:25 | Challenge | Compare struct vs union with the same members | Two boxes side by side, scale tips; timer ring |
| 11 | 6:25 | 0:20 | Outro | Module 9 done; next: EP 65 Module 10 dynamic memory; sign-off | Module tiles, claw-click, music out |

### Narration script

**\[1 · 6 or 12?\]** Here is a struct called Order: a char for the size, an int for the quantity, and another char for the type. A char is 1 byte, an int is 4. One plus four plus one is 6. We ask sizeof. It says 12! Did sizeof just lie to us? No. It told the truth. We just did not know where to look.

**\[2 · Title\]** Episode 64. union and memory layout.

**\[3 · Padding and alignment\]** Think of a bus with seats in rows of four. A family of four wants to sit in one row together. If one person has already taken the first seat of a row, the family will not squeeze across two rows. They skip ahead to the next empty row. The processor is like that family with ints. It reads a 4-byte int fastest when the int starts at an address that is a multiple of 4. This is called alignment. So look at Order in memory. Byte 0: size, the char. Now qty, the int, needs to start at a multiple of 4. Bytes 1, 2 and 3 are left empty. These empty bytes are called padding. qty takes bytes 4 to 7. type, the char, takes byte 8. And then the whole struct is padded up to a multiple of 4 again, so that in an array of Orders, every int lines up. Bytes 9, 10 and 11: more padding. Total: 12. Six useful bytes, six empty ones. These are the numbers on a typical Windows or Linux machine with GCC. On other machines, the sizes may be different, so always use sizeof instead of guessing.

**\[4 · Reorder to shrink\]** Here is a trick. Same three members, different order. struct Packed puts the int first: qty in bytes 0 to 3. Then size at byte 4, type at byte 5. Two bytes of padding at the end to reach a multiple of 4. Total: 8. Same data, 4 bytes saved. A simple rule: put the biggest members first. For one struct, 4 bytes is nothing. For a million records, it is 4 megabytes.

**\[5 · What a union is\]** Now meet union. It is written just like a struct, but with one big difference. In a struct, every member gets its own locker. In a union, all members share one single locker. The locker is as big as the biggest member. So a union of an int, a float and a char is 4 bytes, the size of the int or float. Not 9. You can store an int in it, or a float, or a char, but only one at a time. Putting in a new one replaces the old one. Why would anyone want that? To save memory when a value can be one of several types, but never two at once. Like a parking spot that can hold a car or a scooter, but not both.

**\[6 · Code line by line\]** Let's measure everything. \[HL 3\] Lines 3 to 7: struct Order, char, int, char. \[HL 9\] Lines 9 to 13: struct Packed, the reordered version. \[HL 15\] Lines 15 to 19: union Value. It looks like a struct, but starts with the word union. Members i, f and c. \[HL 22\] Line 22 adds up the sizes of char, int and char. sizeof gives a value of type size\_t, so we print it with percent z u. \[HL 23\] Line 23 prints sizeof struct Order: 12. \[HL 24\] Line 24, struct Packed: 8. \[HL 25\] Line 25, the union: 4. Now let's use the union. \[HL 27\] Line 27: union Value v. One 4-byte box. \[HL 28\] Line 28: v dot i equals 65. The box now holds the int 65. \[TRACK v.i=65\] \[HL 29\] Line 29 prints it. 65. \[HL 30\] Line 30: v dot f equals 2.5. The same box now holds a float, and the 65 is gone. Overwritten. \[TRACK v.f=2.5\] \[HL 31\] Line 31 prints 2.5. \[HL 32\] Line 32: v dot c equals X. Now the box holds a char. \[TRACK v.c='X'\] \[HL 33\] Line 33 prints X. Each time we read the member we wrote last, so each print is correct. That is the golden rule of unions. Remember it, because today's bug breaks it.

**\[7 · Running it\]** Compile and run. char plus int plus char: 6 bytes. struct Order: 12. struct Packed: 8. union Value: 4. Then v dot i 65, v dot f 2.5, v dot c X. Remember, your sizes may differ on other systems, but on Windows with GCC you should see exactly these.

**\[8 · Pun\]** Why did the union members never fight over the room? Because only one of them could be home at a time.

**\[9 · Bug of the Day\]** Today's bug: reading the wrong union member. We write v dot f equals 2.5. Then we print v dot i. No error. No warning, even with -Wall and -Wextra. And the output is: 1075838976. Over one billion! Where did that come from? The box holds the bits of the float 2.5. A float stores numbers in a special pattern of sign, exponent and fraction. When we read those same 32 bits as an int, C does not convert anything. It just reads the pattern as if it were a whole number. And the pattern for 2.5 happens to look like 1075838976 on machines that use the standard float format, which is almost all of them. The union does not remember what you stored last. That is your job. The fix is a pattern called a tagged union. Put the union inside a struct, next to an enum from EP 63 that says what kind of value is inside. Set the tag every time you write. Check the tag every time you read. Now show checks the tag, sees IS\_FLOAT, and prints float 2.5. The tag is like a name board on the shared locker saying who lives there today.

**\[10 · Challenge\]** Your challenge: make a struct S and a union U with exactly the same three members: an int, a float, and a char array of 8. Print the sizeof of both. Before you run it, predict the numbers. Then explain the difference in one sentence. Answer in the comments.

**\[11 · Outro\]** That completes Module 9! You can now build your own data types. But every array and struct so far had a fixed size, decided before the program runs. What if you do not know how many students there will be? Module 10: dynamic memory, starting with EP 65. Keep coding, says Xecxec!

### Code shown

```c
#include <stdio.h>

struct Order {
    char size;
    int qty;
    char type;
};

struct Packed {
    int qty;
    char size;
    char type;
};

union Value {
    int i;
    float f;
    char c;
};

int main(void) {
    printf("char + int + char = %zu bytes\n", sizeof(char) + sizeof(int) + sizeof(char));
    printf("sizeof(struct Order)  = %zu\n", sizeof(struct Order));
    printf("sizeof(struct Packed) = %zu\n", sizeof(struct Packed));
    printf("sizeof(union Value)   = %zu\n\n", sizeof(union Value));

    union Value v;
    v.i = 65;
    printf("v.i = %d\n", v.i);
    v.f = 2.5f;
    printf("v.f = %.1f\n", v.f);
    v.c = 'X';
    printf("v.c = %c\n", v.c);

    return 0;
}
```

**Expected output** (typical x86/x64 with GCC; on screen: "your sizes may differ"):

```text
char + int + char = 6 bytes
sizeof(struct Order)  = 12
sizeof(struct Packed) = 8
sizeof(union Value)   = 4

v.i = 65
v.f = 2.5
v.c = X
```

### Bug of the Day

Wrong code:

```c
#include <stdio.h>

union Value {
    int i;
    float f;
};

int main(void) {
    union Value v;
    v.f = 2.5f;
    printf("v.i = %d\n", v.i);
    return 0;
}
```

No error and no warning, even with `gcc -Wall -Wextra`. Wrong output (on machines with 32-bit IEEE 754 floats and 32-bit int, which includes Windows x64):

```text
v.i = 1075838976
```

Fixed code (tagged union):

```c
#include <stdio.h>

typedef enum { IS_INT, IS_FLOAT } Kind;

typedef struct {
    Kind kind;
    union {
        int i;
        float f;
    } data;
} Value;

void show(Value v) {
    if (v.kind == IS_INT)
        printf("int: %d\n", v.data.i);
    else
        printf("float: %.1f\n", v.data.f);
}

int main(void) {
    Value v;
    v.kind = IS_FLOAT;
    v.data.f = 2.5f;
    show(v);
    return 0;
}
```

Output after the fix:

```text
float: 2.5
```

Why: a union's members share the same bytes, so reading `i` after writing `f` reinterprets the float's bit pattern as an integer instead of converting the value; a tag records which member is currently valid.

### Pun & challenge

- **Pun:** Why did the union members never fight over the room? Because only one of them could be home at a time.
- **Challenge:** Make `struct S` and `union U`, each with `int i; float f; char c[8];`. Predict, then print both sizes, and explain the difference in one sentence.
- **Challenge answer:**

```c
struct S { int i; float f; char c[8]; };
union  U { int i; float f; char c[8]; };

printf("struct S: %zu bytes\n", sizeof(struct S));  /* 16 = 4 + 4 + 8 */
printf("union  U: %zu bytes\n", sizeof(union U));   /* 8 = size of the biggest member */
/* A struct gives every member its own space; a union gives all members one shared space. */
```

### Shorts for EP 64

**S1 · 1 + 4 + 1 = 12?** — 0:25 · built from scenes 1 and 3

- **Hook (first 1.5s):** Terminal: "6 bytes" then "sizeof = 12". Record scratch.
- **Script:** A char, an int and a char. 1 plus 4 plus 1 is 6. sizeof says 12. Why? The processor likes ints to start at a multiple of 4. So C adds empty bytes, called padding: 3 after the first char, 3 at the end. Six bytes of data, six bytes of air. Your sizes may differ, so always use sizeof.
- **On-screen text:** 1 + 4 + 1 = 12?!
- **Caption + hashtags:** The hidden bytes inside your struct. #cprogramming #learntocode #kodingkonkani #memory #codingforbeginners

**S2 · union in 30 seconds** — 0:30 · built from scenes 5–6

- **Hook (first 1.5s):** Three locker doors merge into one
- **Script:** union in 30 seconds. A struct gives each member its own locker. A union gives all members one shared locker, as big as the biggest member. Store an int, then a float, and the int is gone. Only the last one you wrote is valid. Use it when a value can be one of several types, but never two at once.
- **On-screen text:** STRUCT: ALL · UNION: ONE AT A TIME
- **Caption + hashtags:** Struct vs union in one picture. #cprogramming #learntocode #kodingkonkani #union #ctutorial

**S3 · 2.5 became 1075838976** — 0:35 · built from scene 9

- **Hook (first 1.5s):** "v.f = 2.5" then "v.i = 1075838976". Xecxec's eyes pop.
- **Script:** We stored 2.5 as a float in a union. Then we read it as an int. Output: over one billion. No error, no warning. The union has no idea what is inside. C just reads the float's bit pattern as a whole number. Fix: a tagged union. Keep an enum next to it that says what is stored. Check it before you read.
- **On-screen text:** WRONG MEMBER = WRONG NUMBER
- **Caption + hashtags:** Same bits, totally different number. #cprogramming #debugging #kodingkonkani #learntocode #codinglife

**S4 · Only one home at a time** — 0:12 · built from scene 8

- **Hook (first 1.5s):** Three tenants peeking at one tiny locker
- **Script:** Why did the union members never fight over the room? Because only one of them could be home at a time.
- **On-screen text:** ONLY ONE HOME AT A TIME
- **Caption + hashtags:** Peaceful shared living, C style. #programmerhumor #cprogramming #kodingkonkani #codingjokes

**S5 · Shrink the struct** — 0:30 · built from scenes 4 and 10

- **Hook (first 1.5s):** "char, int, char = 12 bytes. Can you make it 8?"
- **Script:** Quiz. A struct with char, int, char is 12 bytes. Can you make it smaller without removing anything? Three, two, one. Put the int first! int, char, char is 8 bytes. Biggest members first, less padding. Now your challenge: compare a struct and a union with the same members. Predict the sizes. Answer in the comments.
- **On-screen text:** 12 → 8 BYTES?
- **Caption + hashtags:** Free memory, just by reordering. #cprogramming #codingquiz #kodingkonkani #learntocode #memory
