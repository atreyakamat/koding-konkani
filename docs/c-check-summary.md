# C compiler check

gcc: `gcc.exe (Rev6, Built by MSYS2 project) 16.2.0`

## Counts

- PASS: 242
- OUTPUT-MISMATCH: 11
- COMPILE-ERROR: 5
- BUG-MESSAGE-DIFFERS: 3
- NEEDS-INPUT: 3
- NONDETERMINISTIC: 6
- TIMEOUT: 6
- SKIPPED: 15

Fixed code was a snippet (not a full program) and had to be reconstructed by patching the wrong code for 29 episodes: EP25, EP26, EP27, EP28, EP33, EP41, EP42, EP43, EP44, EP45, EP46, EP47, EP50, EP52, EP54, EP55, EP56, EP58, EP62, EP66, EP67, EP70, EP71, EP72, EP73, EP74, EP75, EP76, EP78.

## Non-PASS results (34)

| EP | Title | Kind | File | Status | Expected (first 10 lines) | Actual (first 10 lines) |
| --- | --- | --- | --- | --- | --- | --- |
| 5 | How a C Program Is Built | code | file1.c | OUTPUT-MISMATCH | Namaskar, Goa!<br>0 | Namaskar, Goa! |
| 12 | scanf: Taking Input | code | ep12_sum.c | OUTPUT-MISMATCH | Enter two numbers: 12 30<br>Sum: | Enter two numbers: Sum: 144702354 |
| 14 | Mini Project: Unit Converter | code | file1.c | OUTPUT-MISMATCH | === Xecxec's Unit Converter ===<br>Distance in km:<br>Amount in rupees:<br>Temperature in Celsius: | === Xecxec's Unit Converter ===<br>Distance in km: Amount in rupees: Temperature in Celsius: <br>--- Results ---<br>   60.00 km      =    37.28 miles<br>  500.00 rupees  =     5.68 dollars<br>      37 Celsius =     98.6 Fahrenheit |
| 24 | Logic puzzles in C | code | file1.c | NEEDS-INPUT |  | program reads scanf but no stdin was captured from the Bible text |
| 25 | Mini project: Quiz app | code | file1.c | NEEDS-INPUT |  | program reads scanf but no stdin was captured from the Bible text |
| 26 | Why Loops? The while Loop | bug-wrong | wrong.c | TIMEOUT |  |  |
| 28 | do-while: Ask First, Check Later | code | file3.c | TIMEOUT |  |  |
| 33 | Mini Project: Number Games | code | file1.c | OUTPUT-MISMATCH | Enter a number (1-20):<br>12 is not prime<br>12! = 479001600<br>Reversed: | Enter a number (1-20): 12 is not prime<br>12! = 479001600<br>Reversed: 21 |
| 41 | Arrays: A Row of Numbered Lockers | code | file3.c | COMPILE-ERROR |  | file3.c: In function 'main':<br>file3.c:6:7: error: assignment to expression with array type<br>    6 \|     b = a;<br>      \|       ^<br>file3.c:5:9: warning: variable 'b' set but not used [-Wunused-but-set-variable=]<br>    5 \|     int b[3];<br>      \|         ^ |
| 46 | Arrays & Functions: Hand Over the Whole Locker Row | bug-fixed | fixed.c | COMPILE-ERROR |  | fixed.c:10:1: error: expected identifier or '(' before '}' token<br>   10 \| }<br>      \| ^<br>fixed.c: In function 'main':<br>fixed.c:14:31: error: too few arguments to function 'average'; expected 2, have 1<br>   14 \|     printf("Average: %.2f\n", average(marks));<br>      \|                               ^~~~~~~<br>fixed.c:3:7: note: declared here<br>    3 \| float average(int arr[], int size) {<br>      \|       ^~~~~~~ |
| 48 | Reading Strings: Why Your Full Name Got Cut | code | file1.c | OUTPUT-MISMATCH | Enter your name: Atreya Kamat<br>scanf got:<br>Enter your address: 221B Fontainhas, Panjim<br>fgets got: 221B Fontainhas, Panjim | Enter your name: scanf got: Atreya<br>Enter your address: fgets got:  |
| 51 | Mini Project: Text Tools (Build Your Own Mini Word) | code | file1.c | OUTPUT-MISMATCH | Type a line: Keep Coding says Xecxec in Goa<br>Words: 6<br>Letters and symbols: 30<br>UPPER: KEEP CODING SAYS XECXEC IN GOA<br>lower: keep coding says xecxec in goa | Type a line: Words: 1<br>Letters and symbols: 1<br>UPPER: <br>lower:  |
| 52 | Memory & Addresses | code | file1.c | NONDETERMINISTIC |  | uses rand/time/clock/%p or marked [MEASURED]/'may differ' |
| 53 | What Is a Pointer? | code | file1.c | NONDETERMINISTIC |  | uses rand/time/clock/%p or marked [MEASURED]/'may differ' |
| 54 | Dereferencing | bug-wrong | wrong.c | BUG-MESSAGE-DIFFERS | GCC (`gcc -Wall bug.c`) prints:<br><br>bug.c: In function 'main':<br>bug.c:5:14: warning: initialization of 'int *' from 'int' makes pointer from integer without a cast [-Wint-conversion]<br>    5 \|     int *p = fish;<br>      \|              ^~~~<br><br>Running it crashes with a segmentation fault (on Windows the program usually just exits without printing anything).<br><br>Note: GCC 14 and later turn this warning into an e | wrong.c: In function 'main':<br>wrong.c:5:14: error: initialization of 'int *' from 'int' makes pointer from integer without a cast [-Wint-conversion]<br>    5 \|     int *p = fish;<br>      \|              ^~~~ |
| 55 | Call by Reference | bug-wrong | wrong.c | BUG-MESSAGE-DIFFERS | GCC 13 (`gcc -Wall bug.c`) prints:<br><br>bug.c: In function 'main':<br>bug.c:11:10: warning: passing argument 1 of 'swap' makes pointer from integer without a cast [-Wint-conversion]<br>   11 \|     swap(x, y);<br>      \|          ^<br>      \|          \|<br>      \|          int<br>bug.c:3:16: note: expected 'int *' but argument is of type 'int'<br>    3 \| void swap(int *a, int *b) { | wrong.c: In function 'main':<br>wrong.c:11:10: error: passing argument 1 of 'swap' makes pointer from integer without a cast [-Wint-conversion]<br>   11 \|     swap(x, y);<br>      \|          ^<br>      \|          \|<br>      \|          int<br>wrong.c:11:10: note: possible fix: take the address with '&'<br>   11 \|     swap(x, y);<br>      \|          ^<br>      \|          & |
| 56 | Pointer Arithmetic | code | file1.c | NONDETERMINISTIC |  | uses rand/time/clock/%p or marked [MEASURED]/'may differ' |
| 57 | Pointers & Arrays | code | file1.c | NONDETERMINISTIC |  | uses rand/time/clock/%p or marked [MEASURED]/'may differ' |
| 60 | Function Pointers | bug-wrong | wrong.c | BUG-MESSAGE-DIFFERS | GCC 13 (`gcc -Wall bug.c`) prints:<br><br>bug.c: In function 'main':<br>bug.c:6:26: warning: initialization of 'int (*)(int,  int)' from incompatible pointer type 'double (*)(double)' [-Wincompatible-pointer-types]<br>    6 \|     int (*f)(int, int) = half;<br>      \|                          ^~~~<br><br>It still builds, and running it prints a nonsense number that changes from run to run (for example `1012736329`). GC | wrong.c: In function 'main':<br>wrong.c:6:26: error: initialization of 'int (*)(int,  int)' from incompatible pointer type 'double (*)(double)' [-Wincompatible-pointer-types]<br>    6 \|     int (*f)(int, int) = half;<br>      \|                          ^~~~<br>wrong.c:3:8: note: 'half' declared here<br>    3 \| double half(double x) { return x / 2; }<br>      \|        ^~~~ |
| 65 | Stack vs Heap | code | file1.c | NONDETERMINISTIC |  | uses rand/time/clock/%p or marked [MEASURED]/'may differ' |
| 66 | malloc & free | code | file1.c | OUTPUT-MISMATCH | How many students? 3<br>Student 1:<br>Student 2:<br>Student 3: | How many students? Student 1: 60<br>Student 2: 70<br>Student 3: 80<br>Student 4: 90<br>Student 5: 100<br>Student 6: 110<br>Student 7: 120<br>Student 8: 130<br>Student 9: 140<br>Student 10: 150 |
| 70 | Reading Files | code | file1.c | OUTPUT-MISMATCH | 1: Day 1: Learned files in C<br>2: Fish caught: 7<br>3: Mood: happy<br>4: Day 2: Monsoon, stayed home and coded<br>Read 4 lines |  |
| 70 | Reading Files | code | file2.c | OUTPUT-MISMATCH | Ravi      72<br>Anjali    88<br>Xecxec    95<br>Average: |  |
| 71 | Binary Files and Records | code | file2.c | OUTPUT-MISMATCH | 1  Ravi     72.5<br>2  Anjali   88.0<br>3  Xecxec   95.5<br>Record 2 is Anjali<br>File size: 84 bytes, 3 records |  |
| 71 | Binary Files and Records | code | file3.c | OUTPUT-MISMATCH | Updated Xecxec to 99.0 |  |
| 71 | Binary Files and Records | bug-fixed | fixed.c | COMPILE-ERROR |  | fixed.c: In function 'main':<br>fixed.c:7:5: error: expected expression before '...' token<br>    7 \|     ...<br>      \|     ^~~<br>fixed.c:6:11: warning: unused variable 'fp' [-Wunused-variable]<br>    6 \|     FILE *fp = fopen("rolls.dat", "wb");<br>      \|           ^~<br>fixed.c:4:9: warning: unused variable 'rolls' [-Wunused-variable]<br>    4 \|     int rolls[3] = {10, 26, 30};<br>      \|         ^~~~~ |
| 73 | Linear vs binary search, visualised | bug-wrong | wrong.c | TIMEOUT |  |  |
| 76 | Insertion sort | bug-fixed | fixed.c | COMPILE-ERROR |  | fixed.c: In function 'main':<br>fixed.c:16:29: error: 'i' undeclared (first use in this function)<br>   16 \|         printf("%d ", cards[i]);<br>      \|                             ^<br>fixed.c:16:29: note: each undeclared identifier is reported only once for each function it appears in |
| 78 | Merge sort | bug-fixed | fixed.c | COMPILE-ERROR |  | fixed.c: In function 'merge':<br>fixed.c:4:9: warning: variable 'temp' set but not used [-Wunused-but-set-variable=]<br>    4 \|     int temp[100];<br>      \|         ^~~~<br>fixed.c: At top level:<br>fixed.c:14:5: error: expected identifier or '(' before 'for'<br>   14 \|     for (int t = 0; t < k; t++)<br>      \|     ^~~<br>fixed.c:14:23: error: expected '=', ',', ';', 'asm' or '__attribute__' before '<' token<br>   14 \|     for (int t = 0; t < k; t++) |
| 81 | Sorting showdown | code | file1.c | NONDETERMINISTIC |  | uses rand/time/clock/%p or marked [MEASURED]/'may differ' |
| 84 | Project: Student Record System | code | students.c | TIMEOUT |  |  |
| 84 | Project: Student Record System | bug-wrong | wrong.c | TIMEOUT |  |  |
| 84 | Project: Student Record System | bug-fixed | fixed.c | TIMEOUT |  |  |
| 85 | Project: Bank / ATM Simulator | code | atm.c | NEEDS-INPUT |  | program reads scanf but no stdin was captured from the Bible text |