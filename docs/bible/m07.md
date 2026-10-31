# Module 7 — Strings

Episodes 47–51 · Pastel blue + Apricot

## EP 47 — Strings Are Char Arrays: The Secret Character

**Module 7 · Strings · 6:30 · Pastel blue + Apricot · Prerequisite: EP 46**

**Learning goals:** explain that a C string is a char array ending in '\\0'; declare a string with a string literal and know it needs length + 1 bytes; print a whole string with %s and single characters with %c; loop through a string until '\\0' instead of using a fixed size.

### YouTube

- **Title:** Strings in C: The Secret \\0 at the End | EP 47
- **Description:** C has no real string type. A string is just a char array with a hidden character at the end, and forgetting it causes some of the strangest bugs in C. Learn how strings are stored, why "Panjim" needs 7 bytes, and how to walk through a string letter by letter. 0:00 6 letters, 7 bytes? · 0:20 Title · 0:25 Chars in a row · 1:05 The null terminator · 1:55 Code walkthrough · 3:35 Running it · 3:55 Single vs double quotes · 4:25 Pun · 4:30 Bug of the Day · 5:35 Challenge · 6:05 Next episode
- **Tags:** c programming, strings in c, null terminator, char array in c, string literal, %s printf, learn c, c for beginners, koding konkani, c strings tutorial, class 12 computer science
- **Thumbnail:** big text "THE SECRET \\0"; seven apricot boxes spelling P-a-n-j-i-m with the seventh box glowing and labelled \\0; Xecxec peeking out of the last box; pastel blue background

### Scene list

| # | Start | Length | Template | On screen | Animation & SFX |
| --- | --- | --- | --- | --- | --- |
| 1 | 0:00 | 0:20 | Terminal | "Panjim has 7 bytes" printed; Xecxec counts six letters on his claws | Claw counting 1 to 6, then a confused shrug; question-mark pop |
| 2 | 0:20 | 0:05 | Title card | EP 47 · STRINGS | Title slams in; claw click |
| 3 | 0:25 | 0:40 | Memory boxes | char word\[6\] filled with 'G' 'O' 'A' 'N' 'S' '\\0' | Letters drop into lockers one by one like beach pebbles; plink per letter |
| 4 | 1:05 | 0:50 | Memory boxes | "Panjim" laid out in 7 boxes, last box \\0 = the stop sign | Bus drives along the boxes and brakes at the \\0 stop sign; bus brake SFX |
| 5 | 1:55 | 1:40 | Code explain | ep47\_strings.c types itself | Line highlights; tracker shows i and city\[i\] |
| 6 | 3:35 | 0:20 | Terminal | gcc ep47\_strings.c -o ep47 then ./ep47 | Output prints; "7 bytes" circled in apricot |
| 7 | 3:55 | 0:30 | Concept slide | 'A' (one char) vs "A" (two bytes: A and \\0) | Two boxes vs one box side by side; ding |
| 8 | 4:25 | 0:05 | Pun card | Pun | Xecxec rimshot |
| 9 | 4:30 | 1:05 | Bug of the Day | char first\[4\] = "Sara"; prints "SaraKamat" | Bus misses the stop and drives into the next array; tyre screech |
| 10 | 5:35 | 0:30 | Challenge | Print a name letter by letter | Letters fall vertically; ticking clock |
| 11 | 6:05 | 0:25 | Outro | Next: EP 48 Reading strings | Xecxec typing his full name and getting cut off; sign-off |

### Narration script

**\[1 · Hook\]** Panjim. P, a, n, j, i, m. Six letters. Xecxec counted them twice. But when we ask C how much memory this word takes, it says seven bytes. Where did the seventh one come from? There is a secret character hiding at the end of every string in C, and today we find it.

**\[2 · Title\]** Episode 47. Strings are char arrays.

**\[3 · Chars in a row\]** Many languages have a special string type. C does not. In C, a string is just an array of chars, the lockers from EP 41, with one letter in each. Here is char word six, filled with G, O, A, N, S, one character in single quotes per locker. And in the last locker, something odd: backslash zero.

**\[4 · The null terminator\]** Backslash zero is called the null character. Its value is zero. It is not the digit zero; it is a char whose number is zero. And it is the stop sign of every string. When printf prints a string, it does not know the size of the array. It just starts at the first letter and keeps printing until it hits backslash zero. Like a bus that keeps going until it reaches the last stop. That is why Panjim needs seven bytes: six letters, plus one stop sign. The rule: a string of length n needs n plus one bytes.

**\[5 · Code walkthrough\]** Let's read it. \[HL 4\] Line four builds a string the long way: six chars, ending with backslash zero, written by hand. \[HL 5\] Line five is the easy way. char city, empty brackets, equals Panjim in double quotes. Double quotes make a string literal, and C adds the backslash zero for you. The compiler counts the letters, adds one, and makes the array seven bytes. \[HL 7\] Line seven prints word with percent s. Percent s means print a string: start here, stop at backslash zero. \[HL 8\] Line eight prints city and its size. sizeof city is seven. We use percent z u for a sizeof value. \[HL 10\] Line ten is the important loop. Look at the condition. Not i less than six. It is city i not equal to backslash zero. \[TRACK i=0 city\[i\]='P'\] We keep going while the current char is not the stop sign. \[TRACK i=1 city\[i\]='a'\] \[HL 11\] Line eleven prints each char with percent c, which prints one character. \[TRACK i=5 city\[i\]='m'\] When i is six, city six is backslash zero, the condition is false, and the loop ends. \[TRACK i=6 city\[i\]='\\0'\] This loop works for any string of any length, because it does not care about the size. It only looks for the stop sign.

**\[6 · Running it\]** Compile and run. GOANS. Panjim has 7 bytes. Then each letter of Panjim on its own line, P, a, n, j, i, m. Six letters printed, seven bytes used.

**\[7 · Single vs double quotes\]** A quick warning. Single quotes and double quotes are different in C. A in single quotes is one char, one byte. A in double quotes is a string, two bytes: the A and the backslash zero. Use single quotes for one character, double quotes for a string. Mixing them up is a classic compile error.

**\[8 · Pun\]** Why did the string never get lost? It always knew where to stop.

**\[9 · Bug of the Day\]** Today's bug. Two strings: last is Kamat, first is char four equals Sara. Sara has four letters, the array has four boxes. Looks like a perfect fit. GCC does not even warn, because C allows this. But there is no room for the backslash zero. So when printf prints first, it prints S, a, r, a, and then finds no stop sign. It keeps going into whatever memory comes next. On my machine, the output is Hello, SaraKamat. Your output may be different, or have junk characters, because it depends on what sits next in memory. The fix: always leave room for the stop sign. char first five, or simply empty brackets and let C count.

**\[10 · Challenge\]** Your challenge. Make a string with your name, using empty brackets. Use a loop that stops at backslash zero to print one letter per line. Bonus: count the letters inside the same loop, and print the count at the end.

**\[11 · Outro\]** Next episode: reading strings from the keyboard, and why your full name gets cut in half. Keep coding, says Xecxec!

### Code shown

```c
#include <stdio.h>

int main() {
    char word[6] = {'G', 'O', 'A', 'N', 'S', '\0'};
    char city[] = "Panjim";

    printf("%s\n", word);
    printf("%s has %zu bytes\n", city, sizeof(city));

    for (int i = 0; city[i] != '\0'; i++) {
        printf("city[%d] = %c\n", i, city[i]);
    }
    return 0;
}
```

**Expected output**

```text
GOANS
Panjim has 7 bytes
city[0] = P
city[1] = a
city[2] = n
city[3] = j
city[4] = i
city[5] = m
```

### Bug of the Day

```c
#include <stdio.h>

int main() {
    char last[] = "Kamat";
    char first[4] = "Sara";

    printf("Hello, %s!\n", first);
    printf("%s\n", last);
    return 0;
}
```

No error and no warning (C allows the literal to fill the array exactly, dropping the \\0). Wrong output on my machine (on screen: "yours may differ or show junk characters"):

```text
Hello, SaraKamat!
Kamat
```

Fixed:

```c
    char first[] = "Sara";
```

Fixed output:

```text
Hello, Sara!
Kamat
```

Why: without room for '\\0', printf has no stop sign and keeps reading into the next variable in memory.

### Pun & challenge

- **Pun:** Why did the string never get lost? It always knew where to stop.
- **Challenge:** Store your name with char name\[\] = "..."; print it one letter per line with a loop that stops at '\\0'. Bonus: print the letter count.
- **Challenge answer:**

```c
#include <stdio.h>

int main() {
    char name[] = "Xecxec";

    for (int i = 0; name[i] != '\0'; i++) {
        printf("%c\n", name[i]);
    }
    return 0;
}
```

```text
X
e
c
x
e
c
```

Bonus: add int count = 0; before the loop, count++; inside it, and printf("%d letters\\n", count); after it (prints 6 letters).

### Shorts for EP 47

**S1 · 6 Letters, 7 Bytes?** — 0:22 · built from scenes 1, 4

- **Hook (first 1.5s):** Terminal: "Panjim has 7 bytes". Xecxec counting six on his claws.
- **Script:** Panjim has six letters. So why does C say seven bytes? Because every string in C ends with a hidden character, backslash zero. It is the stop sign that tells printf where the string ends.
- **On-screen text:** 6 LETTERS + \\0 = 7 BYTES
- **Caption + hashtags:** The secret character at the end of every C string. #cprogramming #learntocode #kodingkonkani #strings #codingforbeginners

**S2 · C Strings in 30 Seconds** — 0:30 · built from scenes 3–5

- **Hook (first 1.5s):** A bus stopping at a \\0 stop sign.
- **Script:** C has no string type. A string is a char array that ends with backslash zero. printf with percent s starts at the first letter and stops at backslash zero. To loop through a string, keep going while the char is not backslash zero. Length n needs n plus one bytes.
- **On-screen text:** STRING = CHARS + \\0
- **Caption + hashtags:** Everything about C strings starts here. #cprogramming #learntocode #kodingkonkani #strings #cprogrammingtutorial

**S3 · Hello, SaraKamat?** — 0:35 · built from scene 9

- **Hook (first 1.5s):** Terminal: "Hello, SaraKamat!". "I only printed first name."
- **Script:** I only printed the first name. Why did the surname come too? char first four equals Sara. Four letters, four boxes, no room for backslash zero. So printf never found the stop sign and kept reading into the next string. Leave room: use empty brackets.
- **On-screen text:** char first\[4\] = "Sara"; ✗
- **Caption + hashtags:** No warning, wrong output. Classic C. #cprogramming #learntocode #kodingkonkani #bugoftheday #debugging

**S4 · Knew Where to Stop** — 0:12 · built from scene 8

- **Hook (first 1.5s):** Xecxec holding a tiny stop sign with \\0 on it.
- **Script:** Why did the string never get lost? It always knew where to stop.
- **On-screen text:** IT ALWAYS KNEW WHERE TO STOP
- **Caption + hashtags:** Be like a C string. #cprogramming #codingmemes #kodingkonkani #programmerhumor #learntocode

**S5 · 'A' or "A"?** — 0:20 · built from scene 7

- **Hook (first 1.5s):** "'A' and "A": same size?"
- **Script:** A in single quotes, and A in double quotes. Same size? Pause and guess. No. Single quotes is one char, one byte. Double quotes is a string: the A plus backslash zero, two bytes.
- **On-screen text:** 'A' = 1 BYTE · "A" = 2 BYTES
- **Caption + hashtags:** Quotes matter in C. #cprogramming #codingquiz #kodingkonkani #learntocode #strings

## EP 48 — Reading Strings: Why Your Full Name Got Cut

**Module 7 · Strings · 7:00 · Pastel blue + Apricot · Prerequisite: EP 47**

**Learning goals:** read one word with scanf("%29s", ...) and know it stops at a space; read a whole line safely with fgets(buf, sizeof(buf), stdin); remove the newline fgets keeps using strcspn; explain why gets() must never be used.

### YouTube

- **Title:** scanf vs fgets: Read Full Names in C (Never gets!) | EP 48
- **Description:** You type "Atreya Kamat" and C only keeps "Atreya". Learn why scanf stops at spaces, how fgets reads a whole line safely, how to remove the extra newline, and why gets() was removed from the C language. 0:00 Half a name · 0:20 Title · 0:25 How scanf reads · 1:10 Meet fgets · 2:00 Code walkthrough · 4:00 Running it · 4:20 Never use gets · 5:05 Pun · 5:10 Bug of the Day · 6:10 Challenge · 6:40 Next episode
- **Tags:** c programming, fgets in c, scanf string, read string with spaces in c, gets dangerous, buffer overflow, strings in c, learn c, c for beginners, koding konkani, class 12 computer science
- **Thumbnail:** big text "NAME CUT IN HALF?"; a name tag "ATREYA | KAMAT" snipped by Xecxec's claw; a red "gets()" crossed out in the corner; pastel blue + apricot

### Scene list

| # | Start | Length | Template | On screen | Animation & SFX |
| --- | --- | --- | --- | --- | --- |
| 1 | 0:00 | 0:20 | Terminal | Type "Atreya Kamat", program prints "Hello, Atreya!" | "Kamat" falls off the screen; Xecxec catches it; snip SFX |
| 2 | 0:20 | 0:05 | Title card | EP 48 · READING STRINGS | Title slams in; claw click |
| 3 | 0:25 | 0:45 | Memory boxes | Keyboard buffer: A t r e y a \_ K a m a t \\n; scanf takes up to the space | scanf scoop lifts "Atreya", leaves " Kamat\\n" waiting; scoop SFX |
| 4 | 1:10 | 0:50 | Concept slide | fgets(where, how many, from where) with three labelled arrows | Each argument pops in with a label; pop SFX |
| 5 | 2:00 | 2:00 | Code explain | ep48\_input.c types itself | Line highlights; tracker shows name, address and the keyboard buffer |
| 6 | 4:00 | 0:20 | Terminal | Run with Atreya Kamat and a Panjim address | Input in apricot, output in white |
| 7 | 4:20 | 0:45 | Concept slide | gets(name) with a 10-box array and a 20-letter input spilling over | Letters overflow onto neighbouring boxes like a monsoon flood; warning siren |
| 8 | 5:05 | 0:05 | Pun card | Pun | Xecxec rimshot |
| 9 | 5:10 | 1:00 | Bug of the Day | scanf("%s") on a full name, then the fgets fix | Name tag cut, then stitched back; snip, then zip SFX |
| 10 | 6:10 | 0:30 | Challenge | Read a full address and print "Deliver to: ..." | Delivery scooter icon; ticking clock |
| 11 | 6:40 | 0:20 | Outro | Next: EP 49 string.h toolbox | Toolbox opens; sign-off |

### Narration script

**\[1 · Hook\]** Your program asks for your full name. You type Atreya Kamat and press Enter. It says: Hello, Atreya. Where did Kamat go? C did not lose it. It is still waiting, sitting in the keyboard buffer. Today you learn why, and how to read a whole line properly.

**\[2 · Title\]** Episode 48. Reading strings.

**\[3 · How scanf reads\]** When you type, your letters first go into a waiting area called the input buffer. Pressing Enter adds a newline at the end. scanf with percent s reads one word. It skips spaces at the start, takes letters, and stops at the first space or newline. So it takes Atreya, and leaves space Kamat newline in the buffer for whoever reads next. scanf percent s is fine for one word, like a city name. For anything with spaces, it is the wrong tool.

**\[4 · Meet fgets\]** The right tool is fgets. It takes three things. First, where to store the text: our char array. Second, how many bytes it may use: sizeof the array. Third, where to read from: stdin, which means the keyboard. fgets reads the whole line, spaces included, and it never writes more than the size you gave it. It always leaves room for backslash zero. That size limit is what makes it safe.

**\[5 · Code walkthrough\]** Let's read the code. \[HL 2\] Line two, a new header, string dot h. We need one function from it today. \[HL 5\] Line five, name with thirty chars. \[HL 6\] Line six, address with fifty. \[HL 9\] Line nine: scanf percent 29 s, name. The 29 is a limit: read at most 29 letters, leaving the thirtieth byte for backslash zero. Also notice: no ampersand before name. An array name already gives the location, as we saw in EP 46. \[TRACK name="Atreya" buffer=" Kamat\\n"\] \[HL 10\] Line ten prints what scanf got: only Atreya. \[HL 12\] Line twelve cleans up. while getchar is not newline, semicolon. getchar reads one char from the buffer. This loop throws away everything left over, up to and including the newline. \[TRACK buffer=""\] Without this line, the next fgets would read the leftover space Kamat and finish instantly. \[HL 15\] Line fifteen: fgets, address, sizeof address, stdin. It reads the whole address line. \[TRACK address="221B Fontainhas, Panjim\\n"\] But look at the tracker. fgets keeps the newline at the end. \[HL 16\] Line sixteen removes it. strcspn, from string dot h, finds the position of the first newline. We put backslash zero there, so the string ends one step earlier. \[TRACK address="221B Fontainhas, Panjim"\] \[HL 17\] Line seventeen prints the clean address.

**\[6 · Running it\]** Run it. Enter your name: Atreya Kamat. scanf got: Atreya. Enter your address: 221B Fontainhas, Panjim. fgets got the whole line, commas, spaces and all.

**\[7 · Never use gets\]** Some old books and some exam guides still teach a function called gets. Never use it. gets reads a line but has no size limit. If name holds ten chars and the user types twenty, gets writes the extra letters past the end of the array, over other variables, like monsoon water flooding the next house. This is called a buffer overflow, and attackers have used it to break into real programs. gets was so dangerous that it was removed from the C language in the C11 standard. Many compilers now warn you, and some refuse to build it. On Linux, the linker even prints: the gets function is dangerous and should not be used. Always use fgets.

**\[8 · Pun\]** Why did the programmer stop using gets? Because it never knew when to stop eating.

**\[9 · Bug of the Day\]** Today's bug is the hook from the start. char name thirty, scanf percent s name, then print Hello. No error, no warning. Type Atreya Kamat and you get Hello, Atreya. scanf stopped at the space. The fix: use fgets with sizeof name and stdin, and then the strcspn line to remove the newline. Now it prints Hello, Atreya Kamat.

**\[10 · Challenge\]** Your challenge. A delivery app needs your full address. Make a char array of a hundred. Read the whole address with fgets, remove the newline, and print Deliver to, followed by the address. Test it with an address that has spaces and commas.

**\[11 · Outro\]** Next episode, we open C's string toolbox, string dot h: length, copy, join, compare. And you will see why two equal passwords can fail an equals-equals check. Keep coding, says Xecxec!

### Code shown

```c
#include <stdio.h>
#include <string.h>

int main() {
    char name[30];
    char address[50];

    printf("Enter your name: ");
    scanf("%29s", name);
    printf("scanf got: %s\n", name);

    while (getchar() != '\n');

    printf("Enter your address: ");
    fgets(address, sizeof(address), stdin);
    address[strcspn(address, "\n")] = '\0';
    printf("fgets got: %s\n", address);
    return 0;
}
```

**Expected output** (user input shown after the prompts)

```text
Enter your name: Atreya Kamat
scanf got: Atreya
Enter your address: 221B Fontainhas, Panjim
fgets got: 221B Fontainhas, Panjim
```

Scene 7 (shown, never run as a lesson): on Linux GCC, `gets(name);` builds with an implicit-declaration warning plus a linker line `warning: the 'gets' function is dangerous and should not be used.` On Windows the message differs. On screen: "Removed from C in C11. Use fgets."

### Bug of the Day

```c
#include <stdio.h>

int main() {
    char name[30];
    printf("Enter your full name: ");
    scanf("%s", name);
    printf("Hello, %s!\n", name);
    return 0;
}
```

No error, no warning. Wrong output:

```text
Enter your full name: Atreya Kamat
Hello, Atreya!
```

Fixed:

```c
#include <stdio.h>
#include <string.h>

int main() {
    char name[30];
    printf("Enter your full name: ");
    fgets(name, sizeof(name), stdin);
    name[strcspn(name, "\n")] = '\0';
    printf("Hello, %s!\n", name);
    return 0;
}
```

Fixed output:

```text
Enter your full name: Atreya Kamat
Hello, Atreya Kamat!
```

Why: scanf's %s stops at the first space, while fgets reads the whole line up to the size limit.

### Pun & challenge

- **Pun:** Why did the programmer stop using gets? Because it never knew when to stop eating.
- **Challenge:** Read a full address into char address\[100\] with fgets, remove the newline, and print "Deliver to: \<address>".
- **Challenge answer:**

```c
#include <stdio.h>
#include <string.h>

int main() {
    char address[100];

    printf("Enter your full address: ");
    fgets(address, sizeof(address), stdin);
    address[strcspn(address, "\n")] = '\0';

    printf("Deliver to: %s\n", address);
    return 0;
}
```

```text
Enter your full address: H.No 12, Near Church, Margao, Goa
Deliver to: H.No 12, Near Church, Margao, Goa
```

### Shorts for EP 48

**S1 · Where Did My Surname Go?** — 0:22 · built from scenes 1, 3

- **Hook (first 1.5s):** Terminal: typed "Atreya Kamat", printed "Hello, Atreya!"
- **Script:** I typed Atreya Kamat. C said Hello, Atreya. Where did Kamat go? scanf percent s stops at the first space. The rest is still waiting in the keyboard buffer. The fix is one function: fgets.
- **On-screen text:** "ATREYA KAMAT" → "ATREYA"
- **Caption + hashtags:** scanf cut my name in half. #cprogramming #learntocode #kodingkonkani #strings #codingforbeginners

**S2 · fgets in 30 Seconds** — 0:30 · built from scenes 4–5

- **Hook (first 1.5s):** fgets( \_\_\_, \_\_\_, \_\_\_ ) with three blanks.
- **Script:** fgets takes three things: where to store the text, how many bytes it may use, and where to read from. fgets, name, sizeof name, stdin. It reads the whole line, spaces included, and never overflows. One catch: it keeps the newline. Remove it with strcspn.
- **On-screen text:** fgets(name, sizeof(name), stdin);
- **Caption + hashtags:** The safe way to read a line in C. #cprogramming #learntocode #kodingkonkani #fgets #cprogrammingtutorial

**S3 · Never Use gets()** — 0:35 · built from scene 7

- **Hook (first 1.5s):** "gets(name);" stamped with a red NO.
- **Script:** If your book teaches gets, skip that page. gets has no size limit. Type more letters than the array holds, and it writes past the end, over other memory. That is a buffer overflow. gets was removed from C in C11. Use fgets.
- **On-screen text:** gets() = REMOVED FROM C
- **Caption + hashtags:** The function so dangerous C deleted it. #cprogramming #learntocode #kodingkonkani #bufferoverflow #codingsafety

**S4 · Stop Eating** — 0:12 · built from scene 8

- **Hook (first 1.5s):** Xecxec stuffing his face with letters, cheeks bulging.
- **Script:** Why did the programmer stop using gets? Because it never knew when to stop eating.
- **On-screen text:** IT NEVER KNEW WHEN TO STOP
- **Caption + hashtags:** gets has no table manners. #cprogramming #codingmemes #kodingkonkani #programmerhumor #learntocode

**S5 · What Does fgets Store?** — 0:22 · built from scene 5

- **Hook (first 1.5s):** "You type Margao and press Enter. What is in the array?"
- **Script:** You type Margao and press Enter. fgets stores what? Pause and guess. M, a, r, g, a, o, then a newline, then backslash zero. The newline you typed is kept. That is why we remove it with strcspn.
- **On-screen text:** "Margao\\n\\0"
- **Caption + hashtags:** The hidden newline trips everyone once. #cprogramming #codingquiz #kodingkonkani #learntocode #fgets

## EP 49 — string.h: C's String Toolbox

**Module 7 · Strings · 7:00 · Pastel blue + Apricot · Prerequisite: EP 48**

**Learning goals:** get a string's length with strlen (not counting '\\0'); copy with strcpy and join with strcat into an array big enough to hold the result; compare strings with strcmp and read its 0 / negative / positive result; explain why == on two strings compares locations, not letters.

### YouTube

- **Title:** strlen, strcpy, strcat, strcmp in C | EP 49
- **Description:** C cannot copy a string with = or compare it with ==. Open the string.h toolbox: strlen for length, strcpy to copy, strcat to join, and strcmp to compare. Plus the password bug where two identical strings are "not equal". 0:00 The password that failed · 0:20 Title · 0:25 The toolbox · 0:55 strlen · 1:30 strcpy and strcat · 2:20 strcmp · 3:00 Code walkthrough · 4:45 Running it · 5:05 Pun · 5:10 Bug of the Day · 6:15 Challenge · 6:45 Next episode
- **Tags:** c programming, string.h in c, strlen, strcpy, strcat, strcmp, compare strings in c, strings in c, learn c, c for beginners, koding konkani
- **Thumbnail:** big text "== DOESN'T WORK?"; an apricot toolbox with four tools labelled strlen, strcpy, strcat, strcmp; Xecxec holding a lock with two identical keys looking confused

### Scene list

| # | Start | Length | Template | On screen | Animation & SFX |
| --- | --- | --- | --- | --- | --- |
| 1 | 0:00 | 0:20 | Terminal | Password "goa123" typed correctly, program says "Wrong password" | Lock rattles but stays shut; buzzer |
| 2 | 0:20 | 0:05 | Title card | EP 49 · STRING.H | Title slams in; claw click |
| 3 | 0:25 | 0:30 | Concept slide | Toolbox opens: strlen, strcpy, strcat, strcmp with one-line jobs | Tools slide out one by one; metal clink |
| 4 | 0:55 | 0:35 | Memory boxes | "Xecxec" in 7 boxes; strlen counts 6, skips \\0 | Counter ticks 1 to 6, \\0 box greys out |
| 5 | 1:30 | 0:50 | Memory boxes | strcpy copies letters into copy\[20\]; strcat moves \\0 and appends | Letters fly box to box; \\0 hops to the new end; whoosh |
| 6 | 2:20 | 0:40 | Concept slide | strcmp results: 0 equal, negative = first comes earlier, positive = later | Dictionary pages flip; three result chips stamp in |
| 7 | 3:00 | 1:45 | Code explain | ep49\_toolbox.c types itself | Line highlights; tracker shows first, copy and return values |
| 8 | 4:45 | 0:20 | Terminal | gcc ep49\_toolbox.c -o ep49 then ./ep49 | Five lines print |
| 9 | 5:05 | 0:05 | Pun card | Pun | Xecxec rimshot |
| 10 | 5:10 | 1:05 | Bug of the Day | typed == saved; "Wrong password"; -Wall warning; strcmp fix | Two arrays at different addresses with identical letters; address labels flash |
| 11 | 6:15 | 0:30 | Challenge | Password checker with fgets + strcmp | Padlock icon; ticking clock |
| 12 | 6:45 | 0:15 | Outro | Next: EP 50 String manipulation | "malayalam" mirrored; sign-off |

### Narration script

**\[1 · Hook\]** The saved password is goa123. You type goa123. Exactly the same. And the program says: wrong password. Your code is not broken in the way you think. You just used the wrong tool. Let's open C's string toolbox.

**\[2 · Title\]** Episode 49. string dot h.

**\[3 · The toolbox\]** Strings are arrays, and as we saw, you cannot do much with a whole array using plain operators. You cannot copy one with equals, and you cannot compare two with equals-equals. So C gives us a toolbox called string dot h. Four tools today. strlen measures. strcpy copies. strcat joins. strcmp compares.

**\[4 · strlen\]** strlen gives the length of a string. It starts at the first letter and counts until backslash zero. The backslash zero itself is not counted. So strlen of Xecxec is six, while sizeof the array is seven. strlen counts letters. sizeof counts bytes in the array.

**\[5 · strcpy and strcat\]** strcpy, destination, source, copies the source string into the destination, including backslash zero. It is how you do "equals" for strings. strcat, destination, source, adds the source to the end of the destination. It finds the backslash zero, writes the new letters over it, and puts a fresh backslash zero at the new end. One big rule for both: the destination array must be big enough. These functions do not check. If it does not fit, they write past the end, just like gets.

**\[6 · strcmp\]** strcmp, a, b compares two strings letter by letter, like a dictionary. If they are exactly equal, it returns zero. If a comes earlier in dictionary order, it returns a negative number. If a comes later, a positive number. Do not depend on the exact number, like minus one; only check equal to zero, less than zero, or greater than zero. And yes, zero means equal. It feels backwards at first: "zero difference" is the way to remember it.

**\[7 · Code walkthrough\]** Let's read it. \[HL 2\] Line two, string dot h. Without it, these functions are not declared. \[HL 5\] Line five: first, twenty bytes, holding Crab. We give it room to grow. \[HL 6\] Line six: second is Xecxec. \[HL 7\] Line seven: copy, twenty empty bytes. \[HL 9\] Line nine prints strlen of second: six. Percent z u, because strlen returns a size, just like sizeof. \[TRACK strlen=6\] \[HL 11\] Line eleven: strcpy, copy, second. \[TRACK copy="Xecxec"\] Destination first, source second, like an assignment: copy equals second. \[HL 14\] Line fourteen: strcat, first, space. \[TRACK first="Crab "\] \[HL 15\] Line fifteen: strcat, first, second. \[TRACK first="Crab Xecxec"\] Crab, space, Xecxec: eleven letters plus backslash zero, which fits in twenty. \[HL 18\] Line eighteen prints strcmp of apple and apple: zero, equal. \[HL 19\] Line nineteen: strcmp of apple and mango is less than zero, because a comes before m. So line twenty prints apple comes before mango.

**\[8 · Running it\]** Compile and run. Length of Xecxec: 6. Copy: Xecxec. Joined: Crab Xecxec. strcmp of apple and apple is 0. apple comes before mango.

**\[9 · Pun\]** Why did the two strings go to counselling? They were equal, but they kept saying zero to each other.

**\[10 · Bug of the Day\]** Back to our password. saved is goa123, typed is goa123, and the code says if typed equals-equals saved. With plain gcc, no warning at all. Output: wrong password. Compile with dash Wall and GCC tells you the truth: comparison between two arrays. Remember EP 46: an array name stands for the array's location in memory. These are two different arrays, in two different places, so their locations are never equal, even with the same letters inside. Equals-equals compared the addresses, not the letters. The fix: strcmp, typed, saved, equals-equals zero. Now: access granted. And a habit for life: always compile with dash Wall.

**\[11 · Challenge\]** Your challenge. Build a tiny password checker. Store the saved password, feni at 2026. Read the user's attempt with fgets, from EP 48, and remove the newline. Compare with strcmp. Print access granted or wrong password. Test it with a capital F, and notice that strcmp cares about capitals.

**\[12 · Outro\]** Next episode, we write our own string tools: reverse a word, count vowels, and check if malayalam is a palindrome. Keep coding, says Xecxec!

### Code shown

```c
#include <stdio.h>
#include <string.h>

int main() {
    char first[20] = "Crab";
    char second[] = "Xecxec";
    char copy[20];

    printf("Length of %s: %zu\n", second, strlen(second));

    strcpy(copy, second);
    printf("Copy: %s\n", copy);

    strcat(first, " ");
    strcat(first, second);
    printf("Joined: %s\n", first);

    printf("strcmp(\"apple\", \"apple\") = %d\n", strcmp("apple", "apple"));
    if (strcmp("apple", "mango") < 0) {
        printf("apple comes before mango\n");
    }
    return 0;
}
```

**Expected output**

```text
Length of Xecxec: 6
Copy: Xecxec
Joined: Crab Xecxec
strcmp("apple", "apple") = 0
apple comes before mango
```

### Bug of the Day

```c
#include <stdio.h>

int main() {
    char saved[] = "goa123";
    char typed[] = "goa123";

    if (typed == saved) {
        printf("Access granted\n");
    } else {
        printf("Wrong password\n");
    }
    return 0;
}
```

Plain `gcc pass_bug.c -o pass_bug` gives no warning. With `gcc -Wall pass_bug.c -o pass_bug`:

```text
pass_bug.c: In function 'main':
pass_bug.c:7:15: warning: comparison between two arrays [-Warray-compare]
    7 |     if (typed == saved) {
      |               ^~
pass_bug.c:7:15: note: use '&typed[0] == &saved[0]' to compare the addresses
```

Wrong output:

```text
Wrong password
```

Fixed:

```c
#include <stdio.h>
#include <string.h>

int main() {
    char saved[] = "goa123";
    char typed[] = "goa123";

    if (strcmp(typed, saved) == 0) {
        printf("Access granted\n");
    } else {
        printf("Wrong password\n");
    }
    return 0;
}
```

Fixed output:

```text
Access granted
```

Why: == on two arrays compares their memory locations, which are always different; strcmp compares the letters.

### Pun & challenge

- **Pun:** Why did the two strings go to counselling? They were equal, but they kept saying zero to each other.
- **Challenge:** Password checker: saved password "feni@2026", read the attempt with fgets, strip the newline, compare with strcmp. Try "Feni@2026" too.
- **Challenge answer:**

```c
#include <stdio.h>
#include <string.h>

int main() {
    char saved[] = "feni@2026";
    char typed[30];

    printf("Password: ");
    fgets(typed, sizeof(typed), stdin);
    typed[strcspn(typed, "\n")] = '\0';

    if (strcmp(typed, saved) == 0) {
        printf("Access granted\n");
    } else {
        printf("Wrong password\n");
    }
    return 0;
}
```

```text
Password: feni@2026
Access granted

Password: Feni@2026
Wrong password
```

### Shorts for EP 49

**S1 · Right Password, Wrong Answer** — 0:22 · built from scenes 1, 10

- **Hook (first 1.5s):** Terminal: typed goa123, "Wrong password".
- **Script:** Saved password: goa123. I typed goa123. The program says wrong password. Why? I compared strings with equals-equals. In C, that compares where the strings live, not what they say. Use strcmp.
- **On-screen text:** goa123 == goa123 → FALSE?!
- **Caption + hashtags:** The password bug every C beginner writes. #cprogramming #learntocode #kodingkonkani #strings #codingforbeginners

**S2 · string.h in 30 Seconds** — 0:30 · built from scenes 3–6

- **Hook (first 1.5s):** Toolbox snaps open with four tools.
- **Script:** Four tools from string dot h. strlen: the length, without backslash zero. strcpy: copy a string, destination first. strcat: join one string onto another. strcmp: compare; zero means equal. And make sure the destination has room.
- **On-screen text:** strlen · strcpy · strcat · strcmp
- **Caption + hashtags:** C's string toolbox in half a minute. #cprogramming #learntocode #kodingkonkani #stringh #cprogrammingtutorial

**S3 · == on Strings** — 0:35 · built from scene 10

- **Hook (first 1.5s):** Two identical arrays with different address labels.
- **Script:** Two arrays, same letters, goa123. typed equals-equals saved is false. Each array name stands for its location in memory, and two arrays never share a location. dash Wall even warns: comparison between two arrays. The fix: strcmp, typed, saved, equals-equals zero.
- **On-screen text:** strcmp(a, b) == 0 ✓
- **Caption + hashtags:** Compile with -Wall and C tells you. #cprogramming #learntocode #kodingkonkani #bugoftheday #debugging

**S4 · Saying Zero** — 0:12 · built from scene 9

- **Hook (first 1.5s):** Two strings on a sofa, a counsellor Xecxec with a clipboard.
- **Script:** Why did the two strings go to counselling? They were equal, but they kept saying zero to each other.
- **On-screen text:** EQUAL, BUT THEY KEPT SAYING ZERO
- **Caption + hashtags:** strcmp relationship advice. #cprogramming #codingmemes #kodingkonkani #programmerhumor #learntocode

**S5 · strlen or sizeof?** — 0:20 · built from scene 4

- **Hook (first 1.5s):** "char s\[\] = "Goa"; strlen(s) and sizeof(s)?"
- **Script:** char s equals Goa. What are strlen s and sizeof s? Pause and guess. strlen is 3: it counts letters. sizeof is 4: the array also holds backslash zero.
- **On-screen text:** strlen = 3 · sizeof = 4
- **Caption + hashtags:** One counts letters, one counts bytes. #cprogramming #codingquiz #kodingkonkani #learntocode #strings

## EP 50 — String Manipulation: Is "malayalam" a Palindrome?

**Module 7 · Strings · 7:00 · Pastel blue + Apricot · Prerequisite: EP 49**

**Learning goals:** reverse a string into a new array using the index len - 1 - i; end a hand-built string with '\\0'; check a palindrome by comparing a word with its reverse; count vowels by testing each char in a loop that stops at '\\0'.

### YouTube

- **Title:** Reverse a String & Check Palindrome in C | EP 50
- **Description:** malayalam reads the same both ways. Learn to reverse a string in C, check if it is a palindrome, and count vowels, all with simple loops. Plus the off-by-one bug that turns your reversed string into nothing at all. 0:00 Read it backwards · 0:20 Title · 0:25 The mirror index · 1:15 Reverse code · 2:35 Palindrome check · 3:15 Counting vowels · 4:30 Running it · 4:50 Pun · 4:55 Bug of the Day · 6:05 Challenge · 6:40 Next episode
- **Tags:** c programming, reverse string in c, palindrome in c, count vowels in c, string programs in c, strings in c, learn c, c for beginners, koding konkani, c interview questions, class 12 computer science
- **Thumbnail:** big text "SAME BOTH WAYS?"; "MALAYALAM" in apricot letters with its mirror reflection below like water at a beach; Xecxec reading it upside down

### Scene list

| # | Start | Length | Template | On screen | Animation & SFX |
| --- | --- | --- | --- | --- | --- |
| 1 | 0:00 | 0:20 | Concept slide | "malayalam", "level", "panjim" with mirror reflections | Words flip in a mirror; two glow mint, panjim glows tomato; shimmer SFX |
| 2 | 0:20 | 0:05 | Title card | EP 50 · STRING MANIPULATION | Title slams in; claw click |
| 3 | 0:25 | 0:50 | Memory boxes | "feni" boxes 0–3 over rev boxes; arrows pair i with len - 1 - i | Crossing arrows draw one by one; \\0 box stays put; swoosh per arrow |
| 4 | 1:15 | 1:20 | Code explain | Reverse part of ep50\_strings.c | Line highlights; tracker shows i, len - 1 - i, rev |
| 5 | 2:35 | 0:40 | Code explain | Palindrome part | strcmp result chip shows 0; mint tick |
| 6 | 3:15 | 1:15 | Code explain | Vowel-count part | Each vowel pops apricot as the loop passes it; tracker shows vowels |
| 7 | 4:30 | 0:20 | Terminal | gcc ep50\_strings.c -o ep50 then ./ep50 | Three lines print |
| 8 | 4:50 | 0:05 | Pun card | Pun | Xecxec rimshot |
| 9 | 4:55 | 1:10 | Bug of the Day | word\[len - i\] makes "Reversed: \[\]" | First arrow lands on the \\0 box; empty brackets flash; alarm buzz |
| 10 | 6:05 | 0:35 | Challenge | Count words in a sentence | Sentence with words lighting up; ticking clock |
| 11 | 6:40 | 0:20 | Outro | Next: EP 51 Mini project: Text tools | Xecxec at a tiny typewriter; sign-off |

### Narration script

**\[1 · Hook\]** Read malayalam backwards. m, a, l, a, y, a, l, a, m. Same word. Level, same. Panjim? mijnap. Not the same. Words that read the same both ways are called palindromes. Today we teach C to spot them, using nothing but loops and the tools from the last three episodes.

**\[2 · Title\]** Episode 50. String manipulation.

**\[3 · The mirror index\]** To reverse a string, we need a mirror formula. Take feni. Length four, indexes zero to three. The first box of the reverse gets the last letter, index three. The second gets index two. Then one, then zero. Look at the pattern: index i in the reverse takes letter number len minus one minus i from the original. When i is zero, len minus one minus zero is three. The minus one is there because the last letter sits at len minus one, not at len. At index len, there is only the backslash zero.

**\[4 · Reverse code\]** Let's read it. \[HL 5\] Line five, our word, malayalam. \[HL 6\] Line six, len equals strlen word: nine. \[TRACK len=9\] \[HL 9\] Line nine, rev, an array of twenty to hold the reverse. \[HL 10\] Line ten, i from zero while i is less than len. \[HL 11\] Line eleven, the mirror formula: rev i equals word len minus one minus i. \[TRACK i=0 src=8 rev="m"\] When i is zero, we copy word eight, the last m. \[TRACK i=1 src=7 rev="ma"\] When i is one, word seven. \[TRACK i=8 src=0 rev="malayalam"\] And so on until i is eight, which copies word zero. \[HL 13\] Now line thirteen, and this one is easy to forget. rev len equals backslash zero. We built rev letter by letter ourselves, so nobody added the stop sign for us. Without it, printf would run past the end, like the bug from EP 47. \[HL 14\] Line fourteen prints the reverse.

**\[5 · Palindrome check\]** Now the palindrome check is one line. \[HL 17\] Line seventeen: if strcmp, word, rev, equals-equals zero, the word and its reverse are the same, so it is a palindrome. \[HL 18\] Line eighteen prints that. \[HL 20\] Otherwise line twenty prints not a palindrome. This is exactly why we learned strcmp in EP 49, and not equals-equals.

**\[6 · Counting vowels\]** Last tool: counting vowels. \[HL 24\] Line twenty-four, vowels starts at zero. \[TRACK vowels=0\] \[HL 25\] Line twenty-five, the loop from EP 47, which stops at backslash zero. \[HL 26\] Line twenty-six copies the current letter into c, just to keep the next line short. \[HL 27\] Line twenty-seven checks if c is a, or e, or i, or o, or u, joined with the OR operator. \[TRACK i=1 c='a' vowels=1\] \[HL 28\] If yes, vowels plus plus. \[TRACK i=7 c='a' vowels=4\] malayalam has four a's, and no other vowels. \[HL 31\] Line thirty-one prints the count. Note: this only checks small letters. Capital A would not count. Handling capitals is part of next episode's project.

**\[7 · Running it\]** Compile and run. Reversed: malayalam. malayalam is a palindrome. Vowels: 4. Change the word to panjim and run again: Reversed mijnap, not a palindrome, 2 vowels.

**\[8 · Pun\]** Why do palindromes make terrible spies? You can read them from both sides.

**\[9 · Bug of the Day\]** Today's bug. Someone reverses feni with rev i equals word len minus i. No minus one. GCC is happy. Run it: Reversed, and then empty brackets. Nothing at all. Let's trace it. When i is zero, word len minus zero is word four. And word four is the backslash zero. So the very first char of rev is the stop sign, and printf stops before it prints anything. The other letters are in there, but they are hidden behind the stop sign. The fix: len minus one minus i. The last letter is at len minus one.

**\[10 · Challenge\]** Your challenge. Count the words in the sentence: Keep coding says Xecxec. The answer is four. Hint: do not just count spaces, because two spaces in a row, or a space at the start, would fool you. Instead, keep a flag called inWord. When you see a letter and inWord is zero, you just started a new word: count it and set inWord to one. When you see a space, set inWord back to zero.

**\[11 · Outro\]** Next episode, the Module 7 mini project: we build our own text tools, a case changer and a word counter, like a tiny Word. Keep coding, says Xecxec!

### Code shown

```c
#include <stdio.h>
#include <string.h>

int main() {
    char word[] = "malayalam";
    int len = strlen(word);

    /* Reverse into a new string */
    char rev[20];
    for (int i = 0; i < len; i++) {
        rev[i] = word[len - 1 - i];
    }
    rev[len] = '\0';
    printf("Reversed: %s\n", rev);

    /* Palindrome check */
    if (strcmp(word, rev) == 0) {
        printf("%s is a palindrome\n", word);
    } else {
        printf("%s is not a palindrome\n", word);
    }

    /* Count vowels */
    int vowels = 0;
    for (int i = 0; word[i] != '\0'; i++) {
        char c = word[i];
        if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') {
            vowels++;
        }
    }
    printf("Vowels: %d\n", vowels);
    return 0;
}
```

**Expected output**

```text
Reversed: malayalam
malayalam is a palindrome
Vowels: 4
```

With word = "panjim":

```text
Reversed: mijnap
panjim is not a palindrome
Vowels: 2
```

### Bug of the Day

```c
#include <stdio.h>
#include <string.h>

int main() {
    char word[] = "feni";
    int len = strlen(word);
    char rev[20];

    for (int i = 0; i < len; i++) {
        rev[i] = word[len - i];
    }
    rev[len] = '\0';
    printf("Reversed: [%s]\n", rev);
    return 0;
}
```

No error, no warning. Wrong output:

```text
Reversed: []
```

Fixed:

```c
        rev[i] = word[len - 1 - i];
```

Fixed output:

```text
Reversed: [inef]
```

Why: word\[len\] is the '\\0', so copying it into rev\[0\] ends the reversed string before its first letter.

### Pun & challenge

- **Pun:** Why do palindromes make terrible spies? You can read them from both sides.
- **Challenge:** Count the words in "Keep coding says Xecxec" using an inWord flag, so extra spaces do not fool you.
- **Challenge answer:**

```c
#include <stdio.h>

int main() {
    char line[] = "Keep coding says Xecxec";
    int words = 0;
    int inWord = 0;

    for (int i = 0; line[i] != '\0'; i++) {
        if (line[i] == ' ') {
            inWord = 0;
        } else if (inWord == 0) {
            inWord = 1;
            words++;
        }
    }
    printf("Words: %d\n", words);
    return 0;
}
```

```text
Words: 4
```

### Shorts for EP 50

**S1 · Can C Read Backwards?** — 0:22 · built from scenes 1, 3

- **Hook (first 1.5s):** "MALAYALAM" with its mirror image.
- **Script:** malayalam reads the same backwards. So does level. Panjim does not. To make C check this, reverse the word with one formula, len minus one minus i, then compare it with the original. Full episode on the channel.
- **On-screen text:** SAME BOTH WAYS = PALINDROME
- **Caption + hashtags:** Teaching C to read backwards. #cprogramming #learntocode #kodingkonkani #palindrome #codingforbeginners

**S2 · Reverse a String in 30 Seconds** — 0:30 · built from scenes 3–4

- **Hook (first 1.5s):** Crossing arrows between "feni" and "inef".
- **Script:** To reverse a string: rev i equals word len minus one minus i, for i from zero to len minus one. Then the step everyone forgets: rev len equals backslash zero. You built the string yourself, so you add the stop sign yourself.
- **On-screen text:** rev\[i\] = word\[len - 1 - i\];
- **Caption + hashtags:** One formula, any word, reversed. #cprogramming #learntocode #kodingkonkani #strings #cprogrammingtutorial

**S3 · My Reverse Printed Nothing** — 0:35 · built from scene 9

- **Hook (first 1.5s):** Terminal: "Reversed: \[\]". "Where did feni go?"
- **Script:** I reversed feni and got nothing. I wrote word len minus i. When i is zero, that is word four, the backslash zero. So the first char of my reverse was the stop sign, and printf stopped right away. Add minus one: len minus one minus i.
- **On-screen text:** len - i ✗  len - 1 - i ✓
- **Caption + hashtags:** One missing minus one, one empty string. #cprogramming #learntocode #kodingkonkani #bugoftheday #debugging

**S4 · Terrible Spies** — 0:12 · built from scene 8

- **Hook (first 1.5s):** Xecxec in a spy hat holding a note that reads the same both ways.
- **Script:** Why do palindromes make terrible spies? You can read them from both sides.
- **On-screen text:** YOU CAN READ THEM FROM BOTH SIDES
- **Caption + hashtags:** Secret agent: failed. #cprogramming #codingmemes #kodingkonkani #programmerhumor #learntocode

**S5 · How Many Vowels?** — 0:20 · built from scene 6

- **Hook (first 1.5s):** "Vowels in "malayalam"?"
- **Script:** How many vowels does malayalam have? Pause and count. Four. Four a's and nothing else. Our C loop checks each letter against a, e, i, o, u, and adds one every time it matches.
- **On-screen text:** m A l A y A l A m → 4
- **Caption + hashtags:** Count them before the loop does. #cprogramming #codingquiz #kodingkonkani #learntocode #strings

## EP 51 — Mini Project: Text Tools (Build Your Own Mini Word)

**Module 7 · Strings · 7:30 · Pastel blue + Apricot · Prerequisite: EP 50**

**Learning goals:** combine fgets, string functions and your own functions into one small program; change case with toupper and tolower from ctype.h; count words with isspace and an inWord flag; check that a destination has room before strcat to avoid a buffer overflow.

### YouTube

- **Title:** Build a Text Tool in C: Case Changer + Word Counter | EP 51
- **Description:** Module 7 project: build a tiny word processor in C. Read a line safely, count words and characters, and switch it to UPPER or lower case with your own functions. Plus the buffer overflow that strcat will happily cause if you let it. 0:00 Mini Word · 0:20 Title · 0:25 The plan · 1:00 ctype.h · 1:40 The tool functions · 3:20 main · 4:20 Running it · 4:45 Pun · 4:50 Bug of the Day · 6:00 Module 7 recap · 6:30 Challenge · 7:10 Next module
- **Tags:** c programming, c mini project, string project in c, toupper tolower c, word counter in c, ctype.h, buffer overflow, strings in c, learn c, c for beginners, koding konkani
- **Thumbnail:** big text "BUILD MINI WORD"; a retro text editor window with "KEEP CODING" in apricot; Xecxec typing with both claws; toolbar buttons Aa, abc, #words

### Scene list

| # | Start | Length | Template | On screen | Animation & SFX |
| --- | --- | --- | --- | --- | --- |
| 1 | 0:00 | 0:20 | Terminal | A line is typed; word count, UPPER and lower versions appear | Text flips case with a flash; typewriter clacks |
| 2 | 0:20 | 0:05 | Title card | EP 51 · MINI PROJECT: TEXT TOOLS | Title slams in; claw click |
| 3 | 0:25 | 0:35 | Concept slide | Plan: read line (EP 48), count words (EP 50), length (EP 49), change case (new) | Four blocks snap together like Lego; snap SFX |
| 4 | 1:00 | 0:40 | Concept slide | ctype.h: toupper('a') = 'A', tolower('G') = 'g', isspace(' ') = true | Letters bounce between small and capital; boing |
| 5 | 1:40 | 1:40 | Code explain | Lines 1–28 of ep51\_texttools.c: the three functions | Line highlights; tracker shows i, s\[i\], words, inWord |
| 6 | 3:20 | 1:00 | Code explain | Lines 30–46: main | Line highlights; tracker shows text |
| 7 | 4:20 | 0:25 | Terminal | gcc ep51\_texttools.c -o ep51 then ./ep51 | Input in apricot; four result lines print |
| 8 | 4:45 | 0:05 | Pun card | Pun | Xecxec rimshot |
| 9 | 4:50 | 1:10 | Bug of the Day | strcat into greeting\[10\]; letters spill past the end | Letters overflow the boxes like a monsoon drain; siren SFX |
| 10 | 6:00 | 0:30 | Concept slide | Module 7 recap: \\0, fgets not gets, string.h, loops to \\0, leave room | Five checkmarks tick in mint |
| 11 | 6:30 | 0:40 | Challenge | Add a Title Case tool | "kEEP coding" turns into "Keep Coding"; ticking clock |
| 12 | 7:10 | 0:20 | Outro | Next: Module 8 Pointers, EP 52 | Lilac arrows point at boxes; Xecxec points at the camera; sign-off |

### Narration script

**\[1 · Hook\]** Every word processor can count your words and switch your text to capitals. Today you build that yourself, in C, using everything from this module. Type a line, and your program tells you how many words it has, then shouts it in UPPER case, then whispers it in lower case. Your own mini Word.

**\[2 · Title\]** Episode 51. Mini project: text tools.

**\[3 · The plan\]** Here is the plan. Step one: read a whole line safely with fgets, from EP 48. Step two: count words with the inWord flag from EP 50's challenge. Step three: get the length with strlen from EP 49. Step four, the new part: change the case. And we will put each tool in its own function, like we did with arrays in EP 46.

**\[4 · ctype.h\]** For case, C has another header: ctype dot h. It works on one character at a time. toupper of small a gives capital A. tolower of capital G gives small g. If the char is not a letter, like a space or a comma, they give it back unchanged. And isspace tells you if a char is a space, a tab or a newline. That is better than checking for a space only.

**\[5 · The tool functions\]** Let's read the functions. \[HL 1\] Lines one to three include stdio, string and ctype. \[HL 5\] Line five, toUpperCase takes a char array s. No size needed this time. Why? \[HL 6\] Because line six loops until backslash zero. A string carries its own stop sign. \[HL 7\] Line seven: s i equals toupper of s i. Each letter is replaced by its capital. \[TRACK i=0 s\[i\]='K'\] And since arrays are passed by location, EP 46, this changes the caller's text. \[HL 11\] Lines eleven to fifteen, toLowerCase, the same idea with tolower. \[HL 17\] Line seventeen, countWords returns an int. \[HL 18\] words and inWord both start at zero. \[TRACK words=0 inWord=0\] \[HL 19\] Line nineteen, loop to backslash zero. \[HL 20\] Line twenty: if this char is a space, \[HL 21\] we are between words, so inWord is zero. \[HL 22\] Line twenty-two: else if we are not already in a word, exclamation mark inWord, \[HL 23\] then a new word has just started. inWord becomes one, \[HL 24\] and words goes up. \[TRACK words=1 inWord=1\] Extra spaces never start a new word, so they never fool the count. \[HL 27\] Line twenty-seven returns the total.

**\[6 · main\]** Now main. \[HL 31\] Line thirty-one, text with a hundred chars. \[HL 34\] Line thirty-four, fgets reads the line, never more than a hundred bytes. \[HL 35\] Line thirty-five, strcspn removes the newline, as in EP 48. \[TRACK text="Keep Coding says Xecxec in Goa"\] \[HL 37\] Line thirty-seven prints the word count by calling countWords. \[HL 38\] Line thirty-eight prints strlen, the number of characters, spaces included. \[HL 40\] Line forty calls toUpperCase, \[TRACK text="KEEP CODING SAYS XECXEC IN GOA"\] \[HL 41\] and line forty-one prints the result. \[HL 43\] Lines forty-three and forty-four do the same for lower case. \[TRACK text="keep coding says xecxec in goa"\]

**\[7 · Running it\]** Compile and run. Type: Keep Coding says Xecxec in Goa. Words: 6. Letters and symbols: 30, because the five spaces count too. Then the UPPER line, then the lower line. Your mini Word works.

**\[8 · Pun\]** Why did the lowercase letter go to the gym? It wanted to become a capital.

**\[9 · Bug of the Day\]** Our program was careful with sizes. Here is what happens when you are not. greeting is char ten, holding Hello comma space. That is seven chars plus backslash zero. Now strcat greeting with Xecxec the Crab, fifteen more letters. Twenty-three bytes into a ten-byte array. Plain gcc gives no error and no warning. On my test machine it even printed the full greeting, as if nothing was wrong. That is the trap. The extra letters were written over memory that does not belong to greeting. That is a buffer overflow, the same danger as gets in EP 48. Sometimes it looks fine, sometimes it crashes, sometimes it quietly breaks another variable. With optimisation and dash Wall on, GCC can catch it: it warns that the write is out of the bounds of greeting, and the program stops with: buffer overflow detected, terminated. Your exact message depends on your system. The fix: make the destination big enough, char thirty, and check the room first: if strlen greeting plus strlen name is less than sizeof greeting, then strcat.

**\[10 · Module 7 recap\]** Module 7 in five lines. One: a string is a char array ending in backslash zero. Two: read lines with fgets, never gets. Three: use string dot h to measure, copy, join and compare; never equals-equals. Four: loop through a string until backslash zero. Five: always leave room, for the stop sign and for anything you add.

**\[11 · Challenge\]** Your challenge. Add a fourth tool: toTitleCase. It makes the first letter of each word capital and every other letter small. So k E E P space coding becomes Keep Coding. Hint: reuse the idea of the inWord flag. Call it newWord, start it at one, and set it back to one after every space.

**\[12 · Outro\]** That is the end of Module 7. Next, the module everyone fears, and the one that will finally explain all those "location" hints we kept giving you. Module 8: pointers. Keep coding, says Xecxec!

### Code shown

```c
#include <stdio.h>
#include <string.h>
#include <ctype.h>

void toUpperCase(char s[]) {
    for (int i = 0; s[i] != '\0'; i++) {
        s[i] = toupper(s[i]);
    }
}

void toLowerCase(char s[]) {
    for (int i = 0; s[i] != '\0'; i++) {
        s[i] = tolower(s[i]);
    }
}

int countWords(char s[]) {
    int words = 0, inWord = 0;
    for (int i = 0; s[i] != '\0'; i++) {
        if (isspace(s[i])) {
            inWord = 0;
        } else if (!inWord) {
            inWord = 1;
            words++;
        }
    }
    return words;
}

int main() {
    char text[100];

    printf("Type a line: ");
    fgets(text, sizeof(text), stdin);
    text[strcspn(text, "\n")] = '\0';

    printf("Words: %d\n", countWords(text));
    printf("Letters and symbols: %zu\n", strlen(text));

    toUpperCase(text);
    printf("UPPER: %s\n", text);

    toLowerCase(text);
    printf("lower: %s\n", text);
    return 0;
}
```

**Expected output** (user input after the prompt)

```text
Type a line: Keep Coding says Xecxec in Goa
Words: 6
Letters and symbols: 30
UPPER: KEEP CODING SAYS XECXEC IN GOA
lower: keep coding says xecxec in goa
```

### Bug of the Day

```c
#include <stdio.h>
#include <string.h>

int main() {
    char greeting[10] = "Hello, ";
    char name[] = "Xecxec the Crab";

    strcat(greeting, name);
    printf("%s\n", greeting);
    return 0;
}
```

Plain `gcc overflow.c -o overflow`: no error, no warning, and on my test machine the output even looked right (on screen: "looks fine, is not fine"):

```text
Hello, Xecxec the Crab
```

With `gcc -Wall -O2 overflow.c -o overflow` (Linux GCC 13 with glibc; Windows wording and behaviour may differ), GCC warns and the program aborts:

```text
In function 'strcat',
    inlined from 'main' at overflow.c:8:5:
...: warning: '__builtin___strcat_chk' forming offset [10, 22] is out of the bounds [0, 10] of object 'greeting' with type 'char[10]' [-Warray-bounds=]
overflow.c:5:10: note: 'greeting' declared here
    5 |     char greeting[10] = "Hello, ";
      |          ^~~~~~~~
*** buffer overflow detected ***: terminated
```

Fixed:

```c
#include <stdio.h>
#include <string.h>

int main() {
    char greeting[30] = "Hello, ";
    char name[] = "Xecxec the Crab";

    if (strlen(greeting) + strlen(name) < sizeof(greeting)) {
        strcat(greeting, name);
    }
    printf("%s\n", greeting);
    return 0;
}
```

Fixed output:

```text
Hello, Xecxec the Crab
```

Why: strcat never checks the destination's size, so 22 letters plus '\\0' written into 10 bytes spill into memory that belongs to something else.

### Pun & challenge

- **Pun:** Why did the lowercase letter go to the gym? It wanted to become a capital.
- **Challenge:** Add void toTitleCase(char s\[\]) that capitalises the first letter of each word and lowercases the rest. "kEEP coding SAYS xecxec" becomes "Keep Coding Says Xecxec".
- **Challenge answer:**

```c
#include <stdio.h>
#include <ctype.h>

void toTitleCase(char s[]) {
    int newWord = 1;
    for (int i = 0; s[i] != '\0'; i++) {
        if (isspace(s[i])) {
            newWord = 1;
        } else if (newWord) {
            s[i] = toupper(s[i]);
            newWord = 0;
        } else {
            s[i] = tolower(s[i]);
        }
    }
}

int main() {
    char text[] = "kEEP coding SAYS xecxec";
    toTitleCase(text);
    printf("%s\n", text);
    return 0;
}
```

```text
Keep Coding Says Xecxec
```

### Shorts for EP 51

**S1 · I Built My Own Mini Word** — 0:22 · built from scenes 1, 7

- **Hook (first 1.5s):** A line flips to ALL CAPS with a flash.
- **Script:** I built my own mini Word in C. Type a line, and it counts the words, then switches it to upper case and lower case. About forty lines of code, using only what we learned in the strings module. Full build on the channel.
- **On-screen text:** MINI WORD IN 40 LINES OF C
- **Caption + hashtags:** Your first real text tool in C. #cprogramming #learntocode #kodingkonkani #cproject #codingforbeginners

**S2 · Change Case in 30 Seconds** — 0:30 · built from scenes 4–5

- **Hook (first 1.5s):** "a" jumps up and becomes "A".
- **Script:** To change case in C, include ctype dot h. toupper turns a small letter into a capital. tolower does the opposite. Anything that is not a letter comes back unchanged. Loop through the string until backslash zero, and replace each char with toupper of itself.
- **On-screen text:** s\[i\] = toupper(s\[i\]);
- **Caption + hashtags:** Upper case, lower case, one loop. #cprogramming #learntocode #kodingkonkani #ctype #cprogrammingtutorial

**S3 · It Worked... But It Was Wrong** — 0:40 · built from scene 9

- **Hook (first 1.5s):** Terminal shows a perfect greeting, then a red "buffer overflow detected".
- **Script:** This program printed the right answer, and it was still broken. I joined fifteen letters onto a ten-byte array with strcat. strcat never checks the size, so the extra letters landed in memory that is not mine. Sometimes it works, sometimes it crashes. Make the array bigger and check the room first.
- **On-screen text:** LOOKS FINE ≠ IS FINE
- **Caption + hashtags:** The scariest bugs are the quiet ones. #cprogramming #learntocode #kodingkonkani #bugoftheday #bufferoverflow

**S4 · Become a Capital** — 0:12 · built from scene 8

- **Hook (first 1.5s):** A tiny "a" lifting a dumbbell, growing into "A".
- **Script:** Why did the lowercase letter go to the gym? It wanted to become a capital.
- **On-screen text:** IT WANTED TO BECOME A CAPITAL
- **Caption + hashtags:** Gains, but make it ASCII. #cprogramming #codingmemes #kodingkonkani #programmerhumor #learntocode

**S5 · How Many Words?** — 0:20 · built from scene 5

- **Hook (first 1.5s):** ""  hello   goa " with extra spaces: how many words?"
- **Script:** Two spaces, hello, three spaces, goa, one space. How many words does our counter report? Pause and guess. Two. A new word only starts when a letter follows a space, so extra spaces never add to the count.
- **On-screen text:** "  hello   goa " → 2
- **Caption + hashtags:** Counting spaces would get this wrong. #cprogramming #codingquiz #kodingkonkani #learntocode #strings
