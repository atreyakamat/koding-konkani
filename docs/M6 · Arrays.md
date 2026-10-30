# Module 6 — Arrays

Episodes 41–46 · Peach + Dark blue

## EP 41 — Arrays: A Row of Numbered Lockers

**Module 6 · Arrays · 6:30 · Peach + Dark blue · Prerequisite: EP 40**

**Learning goals:** declare an array and give it starting values; read and change one element with an index from 0 to size minus 1; walk through every element with a for loop; explain why going past the last index is dangerous.

### YouTube

- **Title:** Arrays in C: Why Counting Starts at 0 | C Programming EP 41
- **Description:** Five marks, five variables? There is a better way. Learn how arrays store many values under one name, why the first index is 0, and how to loop through them all. Plus the out-of-bounds bug that GCC will not warn you about. 0:00 Five variables? No thanks · 0:20 Title · 0:25 Why arrays · 1:10 Arrays in memory · 2:00 Code walkthrough · 3:20 Running it · 3:50 Starting values and copying · 4:35 Pun · 4:40 Bug of the Day · 5:40 Challenge · 6:05 Next episode
- **Tags:** c programming, arrays in c, c arrays tutorial, array index, for loop array, learn c, c for beginners, index out of bounds, koding konkani, c programming in english, class 12 computer science
- **Thumbnail:** big text "COUNT FROM 0"; a row of five dark-blue lockers numbered 0 to 4 on peach; Xecxec pointing at locker 0 with a shocked face; tomato "\[5\]" crossed out above the row

### Scene list

| # | Start | Length | Template | On screen | Animation & SFX |
| --- | --- | --- | --- | --- | --- |
| 1 | 0:00 | 0:20 | Concept slide | Five separate boxes: mark1 to mark5, then 50 boxes flood in | Boxes pop in one by one, then flood; Xecxec buried under them, claw sticks out; pop SFX, rising whoosh |
| 2 | 0:20 | 0:05 | Title card | EP 41 · ARRAYS | Title slams in; claw click |
| 3 | 0:25 | 0:45 | Concept slide | "An array = many values, one name, same type"; row of numbered lockers | Lockers slide in left to right with labels 0–4; soft clack per locker |
| 4 | 1:10 | 0:50 | Memory boxes | int marks\[5\]: five boxes side by side, index under each, value inside | Values drop into boxes; index 0 glows tomato; "size 5, last index 4" badge stamps in |
| 5 | 2:00 | 1:20 | Code explain | ep41\_arrays.c types itself | Line highlights in butter; variable tracker shows marks\[\] and i |
| 6 | 3:20 | 0:30 | Terminal | gcc ep41\_arrays.c -o ep41 then ./ep41 | Output lines print one by one; marks\[2\] = 70 flashes mint |
| 7 | 3:50 | 0:45 | Memory boxes | {1, 2} into a\[5\] fills 1 2 0 0 0; b\[\] = {4, 5, 6} gets size 3; then b = a; with a red X and a copy loop | Zeros fade in grey; "compiler counts for you" sticker; b = a gets stamped with the GCC error, then values hop box to box one at a time |
| 8 | 4:35 | 0:05 | Pun card | Pun | Xecxec rimshot with claws |
| 9 | 4:40 | 1:00 | Bug of the Day | i <= 5 loop, garbage sixth value | Locker 5 appears dotted and red, door creaks open to a random number; alarm buzz |
| 10 | 5:40 | 0:25 | Challenge | Store 5 marks from the keyboard | Five empty lockers with question marks; ticking clock |
| 11 | 6:05 | 0:25 | Outro | Next: EP 42 Array operations | Xecxec wears a tiny crown (topper teaser); sign-off |

### Narration script

**\[1 · Hook\]** You want to store marks for five subjects. Easy. mark1, mark2, mark3, mark4, mark5. Five variables. Now your teacher says, store marks for the whole class. Fifty students. Are you really going to type fifty variable names? Xecxec tried. Look where he is now. There is a better way.

**\[2 · Title\]** Episode 41. Arrays.

**\[3 · Why arrays\]** An array is a group of values of the same type, stored under one name. Think of a row of lockers in your school corridor. All the lockers belong to one row, and each locker has a number on its door. To open one, you say the row name and the locker number. In C, the row name is the array name, and the locker number is called the index. One name, many values. That is the whole idea.

**\[4 · Arrays in memory\]** Here is how we write it. int marks, square bracket, five, square bracket. This asks C for five int boxes, sitting next to each other in memory. Now the important part. The first box is not number one. It is number zero. So the five boxes are marks zero, marks one, marks two, marks three, and marks four. Size five, last index four. Say it with me: the last index is always size minus one. Remember this, because almost every array bug comes from forgetting it.

**\[5 · Code walkthrough\]** Let's read the program. \[HL 1\] Line one, as always, stdio dot h for printf. \[HL 4\] Line four creates the array and fills it in one go. int marks five equals, curly brace, 78, 92, 65, 88, 71. \[TRACK marks={78,92,65,88,71}\] The values go into the boxes in order: 78 into box zero, 92 into box one, and so on. \[HL 6\] Line six prints marks zero, the first mark: 78. \[HL 7\] Line seven prints marks four, the last mark: 71. Not marks five. Marks four. \[HL 9\] Line nine changes a value. marks two equals 70. The 65 in box two is replaced. \[TRACK marks={78,92,70,88,71}\] Arrays are not frozen; each box is a normal variable. \[HL 11\] Now line eleven, a for loop, just like Module 4. i starts at zero, and the loop runs while i is less than five. \[TRACK i=0\] So i takes the values zero, one, two, three, four. \[TRACK i=4\] Exactly the five valid indexes. \[HL 12\] Inside, printf shows the index and the value at that index, marks i. The loop counter becomes the locker number. This loop pattern, i from zero while i less than size, is the one you will write a thousand times.

**\[6 · Running it\]** Compile with gcc ep41 underscore arrays dot c, dash o, ep41. Run it. First mark 78, last mark 71. Then the loop prints all five, and look: marks two is now 70, not 65. Our change worked.

**\[7 · Starting values\]** Two quick tricks. If you give fewer values than the size, like int a five equals one comma two, C fills the rest with zeros. So you get 1, 2, 0, 0, 0. And if you give all the values, you can leave the size empty. int b, empty brackets, equals 4, 5, 6. The compiler counts them and makes the size three. But be careful: an array with no starting values at all, inside main, holds random leftover numbers. Always fill it before you read it. And one rule that surprises everyone: you cannot copy a whole array with equals. Write b equals a, and GCC stops with an error: assignment to expression with array type. To copy an array, use a loop and copy it one element at a time: b i equals a i. Remember this; it comes back when we meet structures.

**\[8 · Pun\]** Why did the array break up with the index? It kept going out of bounds.

**\[9 · Bug of the Day\]** Today's bug looks innocent. The loop says i less than or equal to five. GCC compiles it without a single error. Run it, and you get the five marks, plus a sixth line: marks five equals some strange number. Your number will be different from mine, because there is no locker five. C does not check. It just opens whatever memory sits after the array and shows you what is inside. Sometimes it prints junk, sometimes it crashes, sometimes it quietly changes another variable. The fix: use i less than five. Less than the size, never less than or equal to.

**\[10 · Challenge\]** Your challenge. Make an array of five ints. Use a for loop with scanf to read five marks from the keyboard, one per subject. Then use a second loop to print them back as Subject 1, Subject 2, and so on. Hint: scanf needs ampersand marks i, and the subject number is i plus one.

**\[11 · Outro\]** Next episode, we put arrays to work: sum, average, and finding who topped the class. Keep coding, says Xecxec!

### Code shown

```c
#include <stdio.h>

int main() {
    int marks[5] = {78, 92, 65, 88, 71};

    printf("First mark: %d\n", marks[0]);
    printf("Last mark: %d\n", marks[4]);

    marks[2] = 70;

    for (int i = 0; i < 5; i++) {
        printf("marks[%d] = %d\n", i, marks[i]);
    }
    return 0;
}
```

**Expected output**

```text
First mark: 78
Last mark: 71
marks[0] = 78
marks[1] = 92
marks[2] = 70
marks[3] = 88
marks[4] = 71
```

Scene 7 snippet (starting values):

```c
#include <stdio.h>

int main() {
    int a[5] = {1, 2};
    int b[] = {4, 5, 6};

    for (int i = 0; i < 5; i++) {
        printf("%d ", a[i]);
    }
    printf("\n");
    printf("%d %d %d\n", b[0], b[1], b[2]);
    return 0;
}
```

**Expected output**

```text
1 2 0 0 0 
4 5 6
```

Scene 7 snippet (arrays cannot be copied with =):

```c
#include <stdio.h>

int main() {
    int a[3] = {1, 2, 3};
    int b[3];
    b = a;
    return 0;
}
```

GCC error (file saved as copy.c):

```text
copy.c: In function 'main':
copy.c:6:7: error: assignment to expression with array type
    6 |     b = a;
      |       ^
```

The fix shown on screen, copying element by element:

```c
#include <stdio.h>

int main() {
    int a[3] = {1, 2, 3};
    int b[3];

    for (int i = 0; i < 3; i++) {
        b[i] = a[i];
    }
    printf("%d %d %d\n", b[0], b[1], b[2]);
    return 0;
}
```

```text
1 2 3
```

### Bug of the Day

```c
#include <stdio.h>

int main() {
    int marks[5] = {78, 92, 65, 88, 71};

    for (int i = 0; i <= 5; i++) {
        printf("marks[%d] = %d\n", i, marks[i]);
    }
    return 0;
}
```

GCC gives no error and, with a plain `gcc file.c`, no warning. Wrong output (the last number is random; on screen: "your number will differ"):

```text
marks[0] = 78
marks[1] = 92
marks[2] = 65
marks[3] = 88
marks[4] = 71
marks[5] = 32767
```

Fixed:

```c
    for (int i = 0; i < 5; i++) {
        printf("marks[%d] = %d\n", i, marks[i]);
    }
```

Why: an array of size 5 has indexes 0 to 4, and C never checks the index, so marks\[5\] reads memory that does not belong to the array.

### Pun & challenge

- **Pun:** Why did the array break up with the index? It kept going out of bounds.
- **Challenge:** Read 5 marks into an array with scanf in a loop, then print them back as "Subject 1: 78" and so on.
- **Challenge answer:**

```c
#include <stdio.h>

int main() {
    int marks[5];

    for (int i = 0; i < 5; i++) {
        printf("Enter mark %d: ", i + 1);
        scanf("%d", &marks[i]);
    }
    for (int i = 0; i < 5; i++) {
        printf("Subject %d: %d\n", i + 1, marks[i]);
    }
    return 0;
}
```

### Shorts for EP 41

**S1 · 50 Variables? No Way** — 0:25 · built from scenes 1–3

- **Hook (first 1.5s):** Xecxec buried under 50 variable boxes. "Stop typing mark1, mark2, mark3..."
- **Script:** Stop typing mark1, mark2, mark3. If you need fifty marks, you need one array. An array is a row of lockers: one name, many values, each with its own number. int marks fifty, and you are done. Full episode on the channel.
- **On-screen text:** 50 VARIABLES? → 1 ARRAY
- **Caption + hashtags:** One name, fifty values. This is why arrays exist. #cprogramming #learntocode #kodingkonkani #arrays #codingforbeginners

**S2 · Arrays in 30 Seconds** — 0:30 · built from scenes 4–5

- **Hook (first 1.5s):** "The first box is not number one."
- **Script:** The first box is not number one. In C, int marks five gives you five boxes, numbered zero to four. marks zero is the first, marks four is the last. To visit all of them, loop i from zero while i is less than five. Size five, last index four. Always size minus one.
- **On-screen text:** SIZE 5 = INDEX 0 TO 4
- **Caption + hashtags:** The one rule every array bug forgets. #cprogramming #learntocode #kodingkonkani #arrays #cprogrammingtutorial

**S3 · The Locker That Doesn't Exist** — 0:35 · built from scene 9

- **Hook (first 1.5s):** Terminal shows "marks\[5\] = 32767". "Where did this number come from?"
- **Script:** Where did this number come from? My array has five marks, but my loop said i less than or equal to five. So C opened locker number five, which does not exist, and showed me random memory. No error, no warning. The fix is one character: less than, not less than or equal to.
- **On-screen text:** <= 5 ✗  < 5 ✓
- **Caption + hashtags:** GCC will not save you from this one. #cprogramming #learntocode #kodingkonkani #bugoftheday #debugging

**S4 · Out of Bounds** — 0:12 · built from scene 8

- **Hook (first 1.5s):** Xecxec holding a broken heart labelled "index".
- **Script:** Why did the array break up with the index? It kept going out of bounds.
- **On-screen text:** IT KEPT GOING OUT OF BOUNDS
- **Caption + hashtags:** Programmer heartbreak. #cprogramming #codingmemes #kodingkonkani #programmerhumor #learntocode

**S5 · What Does This Print?** — 0:20 · built from scene 7

- **Hook (first 1.5s):** "int a\[5\] = {1, 2}; What's in a\[4\]?"
- **Script:** int a five equals one comma two. What is inside a four? Garbage? Error? Pause and guess. The answer is zero. When you give fewer values than the size, C fills the rest with zeros. Comment if you got it.
- **On-screen text:** a\[4\] = ?   → 0
- **Caption + hashtags:** Most beginners guess wrong. Did you? #cprogramming #codingquiz #kodingkonkani #learntocode #arrays

## EP 42 — Array Operations: Who Topped the Class?

**Module 6 · Arrays · 6:30 · Peach + Dark blue · Prerequisite: EP 41**

**Learning goals:** add up all elements of an array in one loop; find the largest and smallest value by starting from the first element; compute a correct decimal average with a float cast; explain why starting max at 0 fails for negative data.

### YouTube

- **Title:** Find Max, Min & Average of an Array in C | EP 42
- **Description:** Who topped the class? One loop over an array answers it. Learn the sum, max, min and average patterns that show up in every exam and every interview, and the max = 0 bug that breaks on negative numbers. 0:00 Results day · 0:20 Title · 0:25 One walk, four answers · 1:05 Tracing max · 1:55 Code walkthrough · 3:35 Running it · 4:00 The average trap · 4:30 Pun · 4:35 Bug of the Day · 5:30 Challenge · 6:10 Next episode
- **Tags:** c programming, array sum in c, max and min in array, average of array c, arrays in c, learn c, c for beginners, c programming exercises, koding konkani, class 12 computer science, c interview questions
- **Thumbnail:** big text "WHO'S THE TOPPER?"; six dark-blue bars on peach, the tallest one in mint with a crown; Xecxec on top of the tallest bar holding a trophy

### Scene list

| # | Start | Length | Template | On screen | Animation & SFX |
| --- | --- | --- | --- | --- | --- |
| 1 | 0:00 | 0:20 | Concept slide | Notice board: six marks pinned up, "Topper? Lowest? Class average?" | Papers flutter onto the board; Xecxec squints with a magnifying glass; paper rustle |
| 2 | 0:20 | 0:05 | Title card | EP 42 · ARRAY OPERATIONS | Title slams in; claw click |
| 3 | 0:25 | 0:40 | Concept slide | "Walk the row once": sum, max, min, average as four counters riding along | Four labelled jars ride on a bus past six lockers; bus horn |
| 4 | 1:05 | 0:50 | Algorithm bars | Six bars 78 92 65 88 71 84; max pointer moves | Current bar in butter, max bar in mint, min bar in tomato; tick per step |
| 5 | 1:55 | 1:40 | Code explain | ep42\_stats.c types itself | Line highlights in butter; tracker shows i, sum, max, min |
| 6 | 3:35 | 0:25 | Terminal | gcc ep42\_stats.c -o ep42 then ./ep42 | Four lines print; "Max: 92" gets a crown |
| 7 | 4:00 | 0:30 | Concept slide | 478 / 6 = 79 (int) vs (float)478 / 6 = 79.67 | The .67 falls off the int version and bounces away; boing SFX |
| 8 | 4:30 | 0:05 | Pun card | Pun | Xecxec rimshot |
| 9 | 4:35 | 0:55 | Bug of the Day | Freezer temperatures, max starts at 0 | Thermometer icons in pastel blue; wrong answer 0 flashes tomato; alarm buzz |
| 10 | 5:30 | 0:40 | Challenge | Find the position of topper and lowest | Two empty name tags "roll ?"; ticking clock |
| 11 | 6:10 | 0:20 | Outro | Next: EP 43 Searching | Xecxec flipping through a register; sign-off |

### Narration script

**\[1 · Hook\]** Results day. Six marks are on the notice board. Everyone wants to know three things. Who topped? Who scored lowest? And what is the class average? You could check by eye for six students. But for six hundred? Let C do it, with one loop.

**\[2 · Title\]** Episode 42. Array operations.

**\[3 · One walk, four answers\]** Here is the plan. We walk along the array once, from the first element to the last, like a bus stopping at every stop on its route. We carry a few variables with us. sum collects every mark. max remembers the biggest mark seen so far. min remembers the smallest so far. When the walk ends, sum divided by the count gives the average. One walk, four answers.

**\[4 · Tracing max\]** Let's watch max. The big question is: what should max start as? We start it at the first element, 78. Now we walk. 92: bigger than 78? Yes. max becomes 92. 65: bigger than 92? No. 88? No. 71? No. 84? No. At the end, max is 92. min works the same way with less than. It starts at 78, drops to 65, and stays there. Notice that max always holds a real mark from the array, from the very first step.

**\[5 · Code walkthrough\]** Now the code. \[HL 4\] Line four, our six marks. \[HL 5\] Line five, n equals six, the number of elements, so we do not type six everywhere. \[HL 6\] Line six, sum starts at zero, because we have added nothing yet. \[TRACK sum=0\] \[HL 7\] Lines seven and eight, max and min both start at marks zero. \[TRACK max=78 min=78\] \[HL 10\] Line ten, our usual loop, i from zero while i is less than n. \[HL 11\] Line eleven, sum plus equals marks i. Each turn adds the current mark. \[TRACK i=0 sum=78\] \[HL 12\] Line twelve: if this mark is bigger than max, \[HL 13\] line thirteen makes it the new max. \[HL 15\] Lines fifteen and sixteen do the same for min, with less than. \[TRACK i=1 sum=170 max=92\] Watch the tracker as the loop runs. \[TRACK i=2 sum=235 min=65\] \[TRACK i=5 sum=478 max=92 min=65\] After the last turn, sum is 478, max is 92, min is 65. \[HL 20\] Line twenty, the average. float average equals, bracket float bracket sum, divided by n. That little float in brackets is a cast, from EP 13. We will see why we need it in a moment. \[HL 22\] Lines twenty-two to twenty-five print everything, and percent point two f shows the average with two decimal places.

**\[6 · Running it\]** Compile and run. Sum 478. Max 92. Min 65. Average 79.67. Our topper scored 92.

**\[7 · The average trap\]** Why the cast? sum is an int and n is an int. In C, int divided by int gives an int, and the decimal part is thrown away. 478 divided by 6 would give just 79. The student with 79.67 percent would not be happy. Putting float in front of sum turns it into 478.0 first, so the division keeps its decimals.

**\[8 · Pun\]** Why did the max variable feel lonely? Because everyone else was below it.

**\[9 · Bug of the Day\]** Today's bug. We want the warmest of four freezer temperatures: minus 18, minus 22, minus 15, minus 20. Someone writes int max equals zero. It compiles fine. But the output says: warmest freezer, zero. Zero is not even in the list. Every temperature is below zero, so no value ever beats the starting max, and max stays at zero. It works with exam marks only because marks are positive. The fix: start max at temps zero, the first real value. Then the answer is minus 15, which is correct.

**\[10 · Challenge\]** Your challenge. Using the same six marks, do not just print the topper's mark. Print the topper's roll number. Roll number one is index zero. Hint: instead of remembering the biggest value, remember the index of the biggest value. Same for the lowest. Expected output: Topper, roll 2 with 92. Lowest, roll 3 with 65.

**\[11 · Outro\]** Next episode: searching. How does a program find your name in a register of a thousand students, and how can it do it in just ten steps? Keep coding, says Xecxec!

### Code shown

```c
#include <stdio.h>

int main() {
    int marks[6] = {78, 92, 65, 88, 71, 84};
    int n = 6;
    int sum = 0;
    int max = marks[0];
    int min = marks[0];

    for (int i = 0; i < n; i++) {
        sum += marks[i];
        if (marks[i] > max) {
            max = marks[i];
        }
        if (marks[i] < min) {
            min = marks[i];
        }
    }

    float average = (float)sum / n;

    printf("Sum: %d\n", sum);
    printf("Max: %d\n", max);
    printf("Min: %d\n", min);
    printf("Average: %.2f\n", average);
    return 0;
}
```

**Expected output**

```text
Sum: 478
Max: 92
Min: 65
Average: 79.67
```

### Bug of the Day

```c
#include <stdio.h>

int main() {
    int temps[4] = {-18, -22, -15, -20};
    int max = 0;

    for (int i = 0; i < 4; i++) {
        if (temps[i] > max) {
            max = temps[i];
        }
    }
    printf("Warmest freezer: %d\n", max);
    return 0;
}
```

No error, no warning. Wrong output:

```text
Warmest freezer: 0
```

Fixed:

```c
    int max = temps[0];
```

Fixed output:

```text
Warmest freezer: -15
```

Why: when every value is below the starting max, nothing ever replaces it, so always start max and min at the array's first element.

### Pun & challenge

- **Pun:** Why did the max variable feel lonely? Because everyone else was below it.
- **Challenge:** Print the roll number (index + 1) of the topper and of the lowest scorer, not just their marks.
- **Challenge answer:**

```c
#include <stdio.h>

int main() {
    int marks[6] = {78, 92, 65, 88, 71, 84};
    int maxPos = 0;
    int minPos = 0;

    for (int i = 1; i < 6; i++) {
        if (marks[i] > marks[maxPos]) {
            maxPos = i;
        }
        if (marks[i] < marks[minPos]) {
            minPos = i;
        }
    }
    printf("Topper: roll %d with %d\n", maxPos + 1, marks[maxPos]);
    printf("Lowest: roll %d with %d\n", minPos + 1, marks[minPos]);
    return 0;
}
```

```text
Topper: roll 2 with 92
Lowest: roll 3 with 65
```

### Shorts for EP 42

**S1 · Find the Topper in One Loop** — 0:25 · built from scenes 1–3

- **Hook (first 1.5s):** Notice board with six marks: "Who topped? Find out with one loop."
- **Script:** Who topped the class? Who scored lowest? What is the average? One loop answers all three. Walk the array once, carry sum, max and min with you, and divide at the end. Six students or six hundred, same code.
- **On-screen text:** 1 LOOP = SUM + MAX + MIN + AVG
- **Caption + hashtags:** The array pattern every exam asks for. #cprogramming #learntocode #kodingkonkani #arrays #codingforbeginners

**S2 · Max of an Array in 30 Seconds** — 0:30 · built from scene 4

- **Hook (first 1.5s):** Six bars, a crown hovering. "How does C find the biggest?"
- **Script:** How does C find the biggest number? Start max at the first element. Then check each one. Bigger than max? It becomes the new max. Not bigger? Move on. At the end, max holds the biggest value. For the smallest, flip it to less than.
- **On-screen text:** START AT marks\[0\], THEN COMPARE
- **Caption + hashtags:** Finding max, explained with bars. #cprogramming #learntocode #kodingkonkani #algorithms #arrays

**S3 · The Freezer That Says 0** — 0:35 · built from scene 9

- **Hook (first 1.5s):** Terminal: "Warmest freezer: 0". "Zero isn't even in my data."
- **Script:** Zero is not even in my data. My temperatures are minus 18, minus 22, minus 15, minus 20. But I started max at zero, and no negative number is bigger than zero, so max never changed. Start max at the first element instead, and you get minus 15. Correct.
- **On-screen text:** max = 0 ✗  max = temps\[0\] ✓
- **Caption + hashtags:** Works for marks, fails for negatives. #cprogramming #learntocode #kodingkonkani #bugoftheday #debugging

**S4 · Lonely at the Top** — 0:12 · built from scene 8

- **Hook (first 1.5s):** Xecxec alone on the tallest bar, wind blowing.
- **Script:** Why did the max variable feel lonely? Because everyone else was below it.
- **On-screen text:** EVERYONE ELSE WAS BELOW IT
- **Caption + hashtags:** It is lonely at the top. #cprogramming #codingmemes #kodingkonkani #programmerhumor #learntocode

**S5 · 79 or 79.67?** — 0:22 · built from scene 7

- **Hook (first 1.5s):** "int sum = 478, n = 6; sum / n = ?"
- **Script:** sum is 478, n is 6, both ints. What does sum divided by n give? Pause and guess. It is 79, not 79.67. int divided by int throws away the decimals. Write bracket float sum divided by n to get 79.67.
- **On-screen text:** 478 / 6 = ?   → 79
- **Caption + hashtags:** Your average is lying to you. #cprogramming #codingquiz #kodingkonkani #learntocode #integerdivision

## EP 43 — Searching: Finding Your Name in the Register

**Module 6 · Arrays · 7:00 · Peach + Dark blue · Prerequisite: EP 42**

**Learning goals:** write a linear search that returns the index or -1; explain how binary search halves the range with low, mid and high; write a correct binary search loop; know that binary search only works on a sorted array.

### YouTube

- **Title:** Linear vs Binary Search in C, Explained | EP 43
- **Description:** How do you find one roll number among a thousand? Check every name, or cut the register in half again and again. Learn linear search and binary search in C, step by step, and why binary search gives wrong answers on unsorted data. 0:00 The register · 0:20 Title · 0:25 Linear search · 1:05 Linear code · 2:05 Binary search idea · 3:05 Binary code · 4:50 Running it · 5:10 How fast? · 5:30 Pun · 5:35 Bug of the Day · 6:25 Challenge · 6:50 Next episode
- **Tags:** c programming, linear search in c, binary search in c, searching in c, binary search explained, arrays in c, learn c, c for beginners, koding konkani, data structures c, c interview questions
- **Thumbnail:** big text "FIND IT IN 10 STEPS"; a stack of 1000 roll-number cards being cut in half by a giant claw; Xecxec smug with arms crossed; dark-blue "mid" arrow

### Scene list

| # | Start | Length | Template | On screen | Animation & SFX |
| --- | --- | --- | --- | --- | --- |
| 1 | 0:00 | 0:20 | Concept slide | Attendance register, 1000 roll numbers, "Find roll 26" | Pages flip fast; Xecxec yawning with a finger running down the page; page-flip SFX |
| 2 | 0:20 | 0:05 | Title card | EP 43 · SEARCHING | Title slams in; claw click |
| 3 | 0:25 | 0:40 | Algorithm bars | Eight boxes 3 8 12 17 21 26 30 35; checker moves left to right | Current box in butter, match turns mint; tick per check, ding on match |
| 4 | 1:05 | 1:00 | Code explain | Linear search part of ep43\_search.c | Line highlights; tracker shows i, found |
| 5 | 2:05 | 1:00 | Algorithm bars | Same eight boxes; low, mid, high arrows; half greys out each step | Grey-out sweep; snip SFX per halving |
| 6 | 3:05 | 1:45 | Code explain | Binary search part of ep43\_search.c | Line highlights; tracker shows low, high, mid, pos |
| 7 | 4:50 | 0:20 | Terminal | gcc ep43\_search.c -o ep43 then ./ep43 | Two lines print, both index 5 |
| 8 | 5:10 | 0:20 | Concept slide | Steps for 1,000 items: linear up to 1000, binary about 10 | Two counters race; binary finishes in a blink; whoosh |
| 9 | 5:30 | 0:05 | Pun card | Pun | Xecxec rimshot |
| 10 | 5:35 | 0:50 | Bug of the Day | Binary search on an unsorted array returns -1 for a value that is there | Boxes shuffled; arrows skip right past 21; alarm buzz |
| 11 | 6:25 | 0:25 | Challenge | Search a roll number typed by the user | Keyboard icon, ticking clock |
| 12 | 6:50 | 0:10 | Outro | Next: EP 44 Sorting intro | Xecxec lining up shells by size; sign-off |

### Narration script

**\[1 · Hook\]** The teacher hands you the attendance register and says, find roll number 26. You start at the top and go one by one. That works. But imagine the register had a thousand names. There is a smarter way, and by the end of this video your program will find any name in a thousand in about ten steps.

**\[2 · Title\]** Episode 43. Searching.

**\[3 · Linear search\]** The simple way is called linear search. Linear means in a line. Start at the first box. Is it 26? No. Next box. No. Keep going until you find it, or until you run out of boxes. Here, 26 sits at index five, so we checked six boxes. If the value is not there at all, we check every single box before we can say "not found".

**\[4 · Linear code\]** Here is the code. \[HL 4\] Line four: eight roll numbers. \[HL 6\] Line six: target is the number we want, 26. \[HL 9\] Line nine: found starts at minus one. Minus one can never be a real index, so it is our signal for "not found yet". \[TRACK found=-1\] \[HL 10\] Line ten, the usual loop over every index. \[HL 11\] Line eleven: if rolls i equals target, \[TRACK i=5\] \[HL 12\] save the index in found, \[TRACK found=5\] \[HL 13\] and break, from EP 29, to stop the loop early. No need to keep looking once we have it. \[HL 16\] Line sixteen prints the result: index five. Simple, and it works on any array, sorted or not.

**\[5 · Binary search idea\]** Now the smart way. Notice our roll numbers are sorted, smallest to largest. That is the key. Binary search looks at the middle box first. low is the first index, zero. high is the last, seven. mid is zero plus seven, divided by two, which is three in integer division. rolls three is 17. Is 26 bigger than 17? Yes. So 26 cannot be anywhere on the left half. Throw that half away. Now low becomes four. New mid is four plus seven by two, five. rolls five is 26. Found it, in two steps instead of six. Every step cuts the remaining boxes in half. It is like the Kadamba bus conductor who knows the stops are in order: if you say Panjim, he does not check every seat; he knows exactly which half of the route you belong to.

**\[6 · Binary code\]** Let's read it. \[HL 19\] Line nineteen sets up three variables. low equals zero, high equals n minus one, and pos equals minus one for "not found". \[TRACK low=0 high=7 pos=-1\] \[HL 20\] Line twenty: while low is less than or equal to high. As long as there is at least one box left to check, keep going. \[HL 21\] Line twenty-one finds the middle. \[TRACK mid=3\] \[HL 22\] Line twenty-two: if the middle value is our target, \[HL 23\] save it and break. \[HL 25\] Line twenty-five: else if the middle value is smaller than the target, the target must be on the right side. \[HL 26\] So low becomes mid plus one. \[TRACK low=4\] Plus one, because we already checked mid. \[HL 27\] Otherwise, the middle value is bigger, the target is on the left, \[HL 28\] and high becomes mid minus one. \[TRACK mid=5 pos=5\] Back to the top of the loop, new mid is five, rolls five is 26, pos becomes five, and we break. \[HL 31\] Line thirty-one prints the answer. And if the target is not there at all, low and high cross over, the loop ends, and pos stays minus one.

**\[7 · Running it\]** Compile and run. Linear: found at index five. Binary: found at index five. Same answer, but binary took two steps, linear took six.

**\[8 · How fast?\]** With a thousand sorted items, linear search may need a thousand checks. Binary search needs about ten, because halving a thousand ten times gets you down to one. With a million items, binary search needs about twenty. That is why it is one of the most famous ideas in computer science.

**\[9 · Pun\]** Why is binary search so calm? It never gets more than half worried.

**\[10 · Bug of the Day\]** Today's bug. Same binary search code, but the array is not sorted: 21, 3, 35, 12, 30, 8, 26, 17. We search for 21. It is right there at index zero. Compile, no errors. Run it. Binary: found at index minus one. Not found! Here is why. mid is three, the value is 12. 21 is bigger, so binary search throws away the left half, including index zero, where 21 actually was. Binary search trusts that the array is sorted. If it is not, it throws away the wrong half. The fix: sort the array first, or use linear search. And how do we sort? That is next episode.

**\[11 · Challenge\]** Your challenge. Use the sorted roll numbers. Ask the user to type a roll number with scanf. Use binary search to find it. If found, print "Roll 30 is at position 7", where position is the index plus one. If not found, print "Roll 9 is not in the class".

**\[12 · Outro\]** Next episode: why order matters, and how to swap two values. Keep coding, says Xecxec!

### Code shown

```c
#include <stdio.h>

int main() {
    int rolls[8] = {3, 8, 12, 17, 21, 26, 30, 35};
    int n = 8;
    int target = 26;

    /* Linear search */
    int found = -1;
    for (int i = 0; i < n; i++) {
        if (rolls[i] == target) {
            found = i;
            break;
        }
    }
    printf("Linear: found at index %d\n", found);

    /* Binary search (array must be sorted) */
    int low = 0, high = n - 1, pos = -1;
    while (low <= high) {
        int mid = (low + high) / 2;
        if (rolls[mid] == target) {
            pos = mid;
            break;
        } else if (rolls[mid] < target) {
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }
    printf("Binary: found at index %d\n", pos);
    return 0;
}
```

**Expected output**

```text
Linear: found at index 5
Binary: found at index 5
```

### Bug of the Day

```c
#include <stdio.h>

int main() {
    int rolls[8] = {21, 3, 35, 12, 30, 8, 26, 17};
    int n = 8;
    int target = 21;
    int low = 0, high = n - 1, pos = -1;

    while (low <= high) {
        int mid = (low + high) / 2;
        if (rolls[mid] == target) {
            pos = mid;
            break;
        } else if (rolls[mid] < target) {
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }
    printf("Binary: found at index %d\n", pos);
    return 0;
}
```

No error, no warning. Wrong output (21 is at index 0):

```text
Binary: found at index -1
```

Fixed: keep the data sorted before a binary search.

```c
    int rolls[8] = {3, 8, 12, 17, 21, 26, 30, 35};
```

Fixed output:

```text
Binary: found at index 4
```

Why: binary search throws away half the array based on the middle value, which is only safe when every value on the left is smaller and every value on the right is bigger.

### Pun & challenge

- **Pun:** Why is binary search so calm? It never gets more than half worried.
- **Challenge:** Read a roll number with scanf, binary search the sorted array, and print its position (index + 1) or "not in the class".
- **Challenge answer:**

```c
#include <stdio.h>

int main() {
    int rolls[8] = {3, 8, 12, 17, 21, 26, 30, 35};
    int n = 8;
    int target;

    printf("Enter roll number: ");
    scanf("%d", &target);

    int low = 0, high = n - 1, pos = -1;
    while (low <= high) {
        int mid = (low + high) / 2;
        if (rolls[mid] == target) {
            pos = mid;
            break;
        } else if (rolls[mid] < target) {
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }
    if (pos == -1) {
        printf("Roll %d is not in the class\n", target);
    } else {
        printf("Roll %d is at position %d\n", target, pos + 1);
    }
    return 0;
}
```

```text
Enter roll number: 30
Roll 30 is at position 7
```

### Shorts for EP 43

**S1 · 1000 Names, 10 Steps** — 0:25 · built from scenes 1, 5

- **Hook (first 1.5s):** Giant register: "Find one name in 1000. In 10 steps."
- **Script:** Find one name in a thousand, in about ten steps. Impossible? Not if the list is sorted. Look at the middle. Too small? Throw away the left half. Too big? Throw away the right half. Repeat. That is binary search.
- **On-screen text:** 1000 NAMES → 10 STEPS
- **Caption + hashtags:** The trick behind every fast search. #cprogramming #learntocode #kodingkonkani #binarysearch #algorithms

**S2 · Binary Search in 30 Seconds** — 0:30 · built from scenes 5–6

- **Hook (first 1.5s):** low, mid, high arrows over eight boxes.
- **Script:** Three arrows: low, mid, high. mid is low plus high, divided by two. If the middle value is your target, done. If it is smaller, move low to mid plus one. If it is bigger, move high to mid minus one. Keep going while low is less than or equal to high.
- **On-screen text:** low · mid · high
- **Caption + hashtags:** Binary search, the whole idea. #cprogramming #learntocode #kodingkonkani #binarysearch #codingforbeginners

**S3 · It's Right There!** — 0:35 · built from scene 10

- **Hook (first 1.5s):** Terminal: "found at index -1" with 21 glowing at index 0.
- **Script:** 21 is right there at index zero, but binary search says not found. Why? The array is not sorted. The middle value was 12, 21 is bigger, so it threw away the left half, the half that had 21. Binary search only works on sorted data.
- **On-screen text:** UNSORTED + BINARY SEARCH = WRONG
- **Caption + hashtags:** Binary search has one rule. Break it and it lies. #cprogramming #learntocode #kodingkonkani #bugoftheday #debugging

**S4 · Half Worried** — 0:12 · built from scene 9

- **Hook (first 1.5s):** Xecxec meditating on a split coconut half.
- **Script:** Why is binary search so calm? It never gets more than half worried.
- **On-screen text:** NEVER MORE THAN HALF WORRIED
- **Caption + hashtags:** Stay calm, cut in half. #cprogramming #codingmemes #kodingkonkani #programmerhumor #learntocode

**S5 · How Many Steps?** — 0:20 · built from scene 8

- **Hook (first 1.5s):** "1,000,000 sorted items. Binary search needs how many steps?"
- **Script:** A million sorted items. How many steps does binary search need? Pause and guess. About twenty. Each step halves the list, and halving a million about twenty times leaves one item. Linear search could need a million.
- **On-screen text:** 1,000,000 → ABOUT 20
- **Caption + hashtags:** Halving is a superpower. #cprogramming #codingquiz #kodingkonkani #learntocode #algorithms

## EP 44 — Sorting Intro: Line Up by Height

**Module 6 · Arrays · 6:00 · Peach + Dark blue · Prerequisite: EP 43**

**Learning goals:** explain why sorted data matters (binary search, toppers, ranks); swap two variables correctly with a temp variable; write one pass that compares neighbours and swaps them; use n - 1 as the bound whenever a loop reads h\[i + 1\].

### YouTube

- **Title:** How to Swap Two Values in C (Sorting Starts Here) | EP 44
- **Description:** Before you can sort anything, you need to swap two values without losing one. Learn the three-step temp swap, then use it to push the tallest value to the end of an array in one pass. Full sorting algorithms come in Module 12. 0:00 Line up by height · 0:20 Title · 0:25 Why order matters · 1:00 The broken swap · 1:30 The temp swap · 2:20 One pass · 3:40 Running it · 4:00 Pun · 4:05 Bug of the Day · 5:05 Challenge · 5:40 Next episode
- **Tags:** c programming, swap two numbers in c, swap using temp, sorting in c, sorting intro, arrays in c, learn c, c for beginners, koding konkani, bubble sort basics, class 12 computer science
- **Thumbnail:** big text "SWAP WITHOUT LOSING"; two glasses (feni and kokum) and an empty third glass labelled temp; Xecxec juggling the glasses; dark-blue arrows

### Scene list

| # | Start | Length | Template | On screen | Animation & SFX |
| --- | --- | --- | --- | --- | --- |
| 1 | 0:00 | 0:20 | Algorithm bars | Five students as bars 150 142 160 138 155, PT teacher whistle: "Line up by height!" | Bars wobble out of order; whistle SFX; Xecxec stands on tiptoe to look taller |
| 2 | 0:20 | 0:05 | Title card | EP 44 · SORTING INTRO | Title slams in; claw click |
| 3 | 0:25 | 0:35 | Concept slide | Three uses: binary search (EP 43), rank list, find median | Three cards flip in; tick per card |
| 4 | 1:00 | 0:30 | Memory boxes | a = b; b = a; both boxes end as 20 | 10 gets overwritten and vanishes in smoke; sad trombone |
| 5 | 1:30 | 0:50 | Memory boxes | Three glasses: a, b, temp; kokum and feni swap via the empty glass | Pour animation in three steps with step numbers; liquid pour SFX |
| 6 | 2:20 | 1:20 | Code explain | ep44\_swap.c types itself | Line highlights; tracker shows a, b, temp, i and the array as bars |
| 7 | 3:40 | 0:20 | Terminal | gcc ep44\_swap.c -o ep44 then ./ep44 | Output prints; 160 lands at the end in mint |
| 8 | 4:00 | 0:05 | Pun card | Pun | Xecxec rimshot |
| 9 | 4:05 | 1:00 | Bug of the Day | i < n with h\[i + 1\]; 160 replaced by a stranger | Ghost sixth bar appears beyond the array; 160 bar swaps with it and disappears; alarm buzz |
| 10 | 5:05 | 0:35 | Challenge | Put three numbers in descending order using swaps | Three shells, biggest to smallest; ticking clock |
| 11 | 5:40 | 0:20 | Outro | Next: EP 45 2D arrays; Module 12 teaser: full sorts | Cinema seat grid fades in; sign-off |

### Narration script

**\[1 · Hook\]** PT period. The teacher blows the whistle. "Line up by height!" Five students, all mixed up. Everyone shuffles around, swapping places with the person next to them, until the line looks right. Your computer has to do the same thing with numbers. Today we learn the one move that every sorting method is built on: the swap.

**\[2 · Title\]** Episode 44. Sorting, the first step.

**\[3 · Why order matters\]** Why do we care about order? Remember last episode: binary search only works on sorted data. Sorted marks give you a rank list straight away. And the middle value of a sorted list is the median. Sorting comes up so often that Module 12 has a whole set of sorting algorithms. Today is just the foundation: how to swap two values, and how to make one pass through an array.

**\[4 · The broken swap\]** Let's try swapping a equals 10 and b equals 20. The obvious way: a equals b, then b equals a. After the first line, a is 20. Good. After the second line, b gets a, which is now 20. So both are 20. The 10 is gone forever. When you write into a box, whatever was inside is lost.

**\[5 · The temp swap\]** Think of two glasses: one with kokum, one with feni. You want to swap them. You cannot pour one straight into the other. You need a third, empty glass. Step one: pour a into temp. Step two: pour b into a. Step three: pour temp into b. Three steps, nothing spilled. In C, that third glass is a variable called temp.

**\[6 · Code walkthrough\]** Here is the code. \[HL 4\] Line four, five heights in centimetres. \[HL 8\] Line eight, a is 10, b is 20. \[TRACK a=10 b=20\] \[HL 9\] Line nine, temp equals a. temp now holds the 10 safely. \[TRACK temp=10\] \[HL 10\] Line ten, a equals b. \[TRACK a=20\] \[HL 11\] Line eleven, b equals temp. \[TRACK b=10\] Swapped. \[HL 12\] Line twelve prints a equals 20, b equals 10. Now the array. \[HL 15\] Line fifteen, a loop where i goes from zero while i is less than n minus one. Why n minus one? Because inside, we look at h i and its neighbour h i plus one. When i is three, the neighbour is h four, the last element. If i went to four, the neighbour would be h five, which does not exist. \[HL 16\] Line sixteen: if the left student is taller than the right one, they are in the wrong order. \[TRACK i=0\] 150 is taller than 142, so \[HL 17\] lines seventeen to nineteen swap them with the same three steps. \[TRACK h={142,150,160,138,155}\] i equals one: 150 and 160 are fine, no swap. i equals two: 160 and 138, swap. \[TRACK h={142,150,138,160,155}\] i equals three: 160 and 155, swap. \[TRACK h={142,150,138,155,160}\] \[HL 23\] Lines twenty-three to twenty-five print the array. Notice what happened: the tallest, 160, moved all the way to the end. One pass puts the biggest value in its final place. The rest is not sorted yet. Repeating this pass is the idea behind bubble sort, which we build properly in EP 74.

**\[7 · Running it\]** Compile and run. a equals 20, b equals 10. Then 142, 150, 138, 155, 160. 160 is at the end. Not fully sorted yet, and that is fine. That is exactly what one pass does.

**\[8 · Pun\]** Why did the two variables need a third friend? Because swapping without temp is a temp-ting mistake.

**\[9 · Bug of the Day\]** Today's bug. Same pass, but the loop says i less than n instead of n minus one. Plain gcc compiles it without a word. When i is four, the code compares h four with h five, and h five is outside the array. If that unknown memory holds a smaller number, the code swaps, and our 160 is carried out of the array and lost. On my machine, with optimisation turned on, the last value printed was zero, and GCC with dash Wall gave a warning: iteration 4 invokes undefined behavior. Your output may differ, and that is the scary part. The fix: whenever the loop body uses i plus one, the bound is n minus one.

**\[10 · Challenge\]** Your challenge. Take three ints, x, y and z. Using only if statements and the temp swap, put them in descending order, so x is the biggest and z is the smallest. Test with 4, 9, 7. The output should be 9, 7, 4. Hint: three compare-and-swaps are enough.

**\[11 · Outro\]** Next episode: arrays get a second dimension, rows and columns, like a cinema seat map. And full sorting algorithms are waiting for you in Module 12. Keep coding, says Xecxec!

### Code shown

```c
#include <stdio.h>

int main() {
    int h[5] = {150, 142, 160, 138, 155};
    int n = 5;

    /* Swap two values with a temp */
    int a = 10, b = 20;
    int temp = a;
    a = b;
    b = temp;
    printf("a = %d, b = %d\n", a, b);

    /* One pass: compare neighbours, swap if out of order */
    for (int i = 0; i < n - 1; i++) {
        if (h[i] > h[i + 1]) {
            temp = h[i];
            h[i] = h[i + 1];
            h[i + 1] = temp;
        }
    }

    for (int i = 0; i < n; i++) {
        printf("%d ", h[i]);
    }
    printf("\n");
    return 0;
}
```

**Expected output**

```text
a = 20, b = 10
142 150 138 155 160 
```

Scene 4 snippet (the broken swap):

```c
#include <stdio.h>

int main() {
    int a = 10, b = 20;
    a = b;
    b = a;
    printf("a = %d, b = %d\n", a, b);
    return 0;
}
```

```text
a = 20, b = 20
```

### Bug of the Day

```c
#include <stdio.h>

int main() {
    int h[5] = {150, 142, 160, 138, 155};
    int n = 5;
    int temp;

    for (int i = 0; i < n; i++) {
        if (h[i] > h[i + 1]) {
            temp = h[i];
            h[i] = h[i + 1];
            h[i + 1] = temp;
        }
    }

    for (int i = 0; i < n; i++) {
        printf("%d ", h[i]);
    }
    printf("\n");
    return 0;
}
```

Compiled with `gcc -Wall -O2 sort_pass.c -o sort_pass`, GCC warns:

```text
sort_pass.c: In function 'main':
sort_pass.c:9:21: warning: iteration 4 invokes undefined behavior [-Waggressive-loop-optimizations]
    9 |         if (h[i] > h[i + 1]) {
      |                    ~^~~~~~~
sort_pass.c:8:23: note: within this loop
    8 |     for (int i = 0; i < n; i++) {
      |                     ~~^~~
```

Wrong output on that build (on screen: "your output may differ"; with plain `gcc` it can even look correct):

```text
142 150 138 155 0 
```

Fixed:

```c
    for (int i = 0; i < n - 1; i++) {
```

Why: the loop body reads h\[i + 1\], so i must stop at n - 2, or the last comparison reaches outside the array.

### Pun & challenge

- **Pun:** Why did the two variables need a third friend? Because swapping without temp is a temp-ting mistake.
- **Challenge:** Put three ints x, y, z into descending order using only if statements and temp swaps. Test with 4, 9, 7.
- **Challenge answer:**

```c
#include <stdio.h>

int main() {
    int x = 4, y = 9, z = 7;
    int temp;

    if (x < y) { temp = x; x = y; y = temp; }
    if (x < z) { temp = x; x = z; z = temp; }
    if (y < z) { temp = y; y = z; z = temp; }

    printf("%d %d %d\n", x, y, z);
    return 0;
}
```

```text
9 7 4
```

### Shorts for EP 44

**S1 · Can You Swap Two Numbers?** — 0:25 · built from scenes 1, 4

- **Hook (first 1.5s):** "a = b; b = a; Did it swap?"
- **Script:** a equals b, b equals a. Did that swap them? No. After the first line, the old value of a is gone, so both end up the same. Swapping needs one extra thing. Full episode on the channel.
- **On-screen text:** a = b; b = a; → 20, 20
- **Caption + hashtags:** The swap that every beginner gets wrong. #cprogramming #learntocode #kodingkonkani #codingforbeginners #sorting

**S2 · The Temp Swap in 30 Seconds** — 0:30 · built from scene 5

- **Hook (first 1.5s):** Two glasses and an empty one: "Swap them without spilling."
- **Script:** Two glasses, kokum and feni. To swap them, you need an empty third glass. Pour a into temp. Pour b into a. Pour temp into b. In C: temp equals a, a equals b, b equals temp. Three lines, nothing lost.
- **On-screen text:** temp = a; a = b; b = temp;
- **Caption + hashtags:** Three lines every sorting algorithm uses. #cprogramming #learntocode #kodingkonkani #sorting #cprogrammingtutorial

**S3 · Where Did 160 Go?** — 0:35 · built from scene 9

- **Hook (first 1.5s):** Terminal: "142 150 138 155 0". "My tallest student vanished."
- **Script:** My tallest student vanished. The loop compared h i with h i plus one, but it ran while i was less than n. So on the last turn it peeked outside the array, swapped with whatever was there, and 160 was gone. If you use i plus one, stop at n minus one.
- **On-screen text:** USE i + 1? STOP AT n - 1
- **Caption + hashtags:** One character, one lost value. #cprogramming #learntocode #kodingkonkani #bugoftheday #debugging

**S4 · Temp-ting** — 0:12 · built from scene 8

- **Hook (first 1.5s):** Xecxec holding two glasses, eyeing a third.
- **Script:** Why did the two variables need a third friend? Because swapping without temp is a temp-ting mistake.
- **On-screen text:** A TEMP-TING MISTAKE
- **Caption + hashtags:** Do not resist the temp. #cprogramming #codingmemes #kodingkonkani #programmerhumor #learntocode

**S5 · After One Pass?** — 0:22 · built from scene 6

- **Hook (first 1.5s):** "150 142 160 138 155: one pass. Which number is now last?"
- **Script:** One pass: compare each pair of neighbours and swap if the left is bigger. Which number ends up last? Pause and guess. 160. One pass always pushes the biggest value to the end. Repeat it and you have bubble sort.
- **On-screen text:** ONE PASS → BIGGEST GOES LAST
- **Caption + hashtags:** The first idea of bubble sort. #cprogramming #codingquiz #kodingkonkani #learntocode #sorting

## EP 45 — 2D Arrays: The Cinema Seat Map

**Module 6 · Arrays · 6:30 · Peach + Dark blue · Prerequisite: EP 44**

**Learning goals:** declare and initialise a 2D array with rows and columns; read and change one cell with \[row\]\[col\]; visit every cell with nested loops (EP 30); add two matrices cell by cell.

### YouTube

- **Title:** 2D Arrays in C: Rows, Columns & Matrices | EP 45
- **Description:** A cinema seat map is a 2D array: rows and columns of seats. Learn how to declare a grid in C, book a seat with \[row\]\[col\], loop through every cell with nested loops, and avoid the bug where rows and columns get swapped. 0:00 Book seat B3 · 0:20 Title · 0:25 Rows and columns · 1:10 Grid in memory · 1:55 Code walkthrough · 3:35 Running it · 3:55 Matrices · 4:30 Pun · 4:35 Bug of the Day · 5:35 Challenge · 6:10 Next episode
- **Tags:** c programming, 2d array in c, two dimensional array, matrix in c, matrix addition in c, nested loops, arrays in c, learn c, c for beginners, koding konkani, class 12 computer science
- **Thumbnail:** big text "ROW FIRST!"; 3 by 4 grid of cinema seats on peach, one seat glowing mint; Xecxec in 3D glasses with popcorn; dark-blue \[r\]\[c\] label

### Scene list

| # | Start | Length | Template | On screen | Animation & SFX |
| --- | --- | --- | --- | --- | --- |
| 1 | 0:00 | 0:20 | Concept slide | Cinema booking screen: 3 rows, 4 seats each, "Book row A, seat 3" | Seats pop in row by row; Xecxec taps a seat; booking ding |
| 2 | 0:20 | 0:05 | Title card | EP 45 · 2D ARRAYS | Title slams in; claw click |
| 3 | 0:25 | 0:45 | Concept slide | "An array of arrays": each row is a 1D array from EP 41 | Three locker rows stack into a grid; clack SFX |
| 4 | 1:10 | 0:45 | Memory boxes | seats\[3\]\[4\] grid with row index on the left, column index on top; then the same 12 boxes laid out in one line in memory | Grid unrolls into a single row: row 0, then row 1, then row 2; whoosh |
| 5 | 1:55 | 1:40 | Code explain | ep45\_seats.c types itself | Line highlights; tracker shows r, c, booked; current cell glows butter |
| 6 | 3:35 | 0:20 | Terminal | gcc ep45\_seats.c -o ep45 then ./ep45 | Grid prints; "Booked: 8 of 12" stamps in |
| 7 | 3:55 | 0:35 | Memory boxes | Matrix A + Matrix B = Sum, cell by cell | Matching cells light up together and their sums drop in; plink per cell |
| 8 | 4:30 | 0:05 | Pun card | Pun | Xecxec rimshot |
| 9 | 4:35 | 1:00 | Bug of the Day | Loop bounds swapped for m\[2\]\[3\] | Grid prints sideways, third row is junk; alarm buzz |
| 10 | 5:35 | 0:35 | Challenge | Add two 2x3 matrices | Two grids with a plus sign; ticking clock |
| 11 | 6:10 | 0:20 | Outro | Next: EP 46 Arrays and functions | Xecxec handing over a whole locker row; sign-off |

### Narration script

**\[1 · Hook\]** You are booking movie tickets. The screen shows a seat map. Row A, row B, row C. Each row has four seats. You tap row A, seat 3. The app needs to remember which seats are taken. One row of lockers is not enough any more. We need a grid.

**\[2 · Title\]** Episode 45. 2D arrays.

**\[3 · Rows and columns\]** A 2D array is an array of arrays. Each row is a normal 1D array, like the lockers from EP 41. Stack three of those rows, and you get a grid. To reach one seat, you need two numbers: the row, and then the column. Always in that order. Row first, column second. Both start at zero, as usual.

**\[4 · Grid in memory\]** We write int seats, bracket three, bracket four. Three rows, four columns, twelve boxes in total. On screen we draw it as a grid. But inside memory, there are no grids. C stores row zero first, then row one right after it, then row two. Twelve boxes in one long line. That is why the order matters: the first number picks which group of four, the second picks the box inside that group.

**\[5 · Code walkthrough\]** Let's read it. \[HL 4\] Line four declares seats with three rows and four columns. \[HL 5\] Lines five to seven give the starting values, one curly-brace group per row. One means booked, zero means free. \[HL 9\] Line nine, booked starts at zero; we will count booked seats. \[TRACK booked=0\] \[HL 11\] Line eleven books a seat. seats zero, two, equals one. Row zero, column two. That is row A, seat 3, because humans count from one. \[HL 13\] Line thirteen, the outer loop. r goes over the rows, zero to two. \[TRACK r=0\] \[HL 14\] Line fourteen, the inner loop, from EP 30. c goes over the columns, zero to three. \[TRACK c=0\] For every one row, the inner loop runs all four columns. \[HL 15\] Line fifteen prints the seat at row r, column c. \[HL 16\] Line sixteen adds it to booked. Since booked seats are one and free seats are zero, adding them counts the booked ones. \[TRACK r=0 c=3 booked=3\] \[HL 18\] Line eighteen, after a full row, prints a new line, so the output looks like a grid. \[TRACK r=2 c=3 booked=8\] \[HL 20\] Line twenty prints booked out of three times four, twelve.

**\[6 · Running it\]** Compile and run. Three rows of four. Row zero now shows 1 0 1 1, because we booked column two. And booked: 8 of 12.

**\[7 · Matrices\]** In maths class, a grid of numbers is called a matrix. Adding two matrices is easy: add the cells that sit in the same position. Top-left plus top-left, and so on. In C, that is the same nested loop, with sum r c equals a r c plus b r c. You will write this in today's challenge.

**\[8 · Pun\]** Why did the 2D array go to the cinema alone? It already had plenty of rows with its friends.

**\[9 · Bug of the Day\]** Today's bug. m is declared as two rows, three columns. But the loops say r less than three and c less than two. Rows and columns got swapped. GCC compiles it happily. The output is 1 2, then 4 5, and then a third line of random numbers. Your numbers will differ. The 3 and the 6 never print, and the third row does not exist, so C reads memory past the end of the array. The fix: the outer loop matches the first size, the inner loop matches the second. r less than two, c less than three.

**\[10 · Challenge\]** Your challenge. Make two 2 by 3 matrices. a is 1 2 3, 4 5 6. b is 6 5 4, 3 2 1. Make a third matrix, sum, and fill it with a plus b, cell by cell, then print it as a grid. If you get all sevens, you did it right.

**\[11 · Outro\]** Next episode: passing arrays to functions, and why sizeof suddenly lies to you inside a function. Keep coding, says Xecxec!

### Code shown

```c
#include <stdio.h>

int main() {
    int seats[3][4] = {
        {1, 0, 0, 1},
        {1, 1, 0, 0},
        {0, 1, 1, 1}
    };
    int booked = 0;

    seats[0][2] = 1;

    for (int r = 0; r < 3; r++) {
        for (int c = 0; c < 4; c++) {
            printf("%d ", seats[r][c]);
            booked += seats[r][c];
        }
        printf("\n");
    }
    printf("Booked: %d of %d\n", booked, 3 * 4);
    return 0;
}
```

**Expected output**

```text
1 0 1 1 
1 1 0 0 
0 1 1 1 
Booked: 8 of 12
```

### Bug of the Day

```c
#include <stdio.h>

int main() {
    int m[2][3] = {
        {1, 2, 3},
        {4, 5, 6}
    };

    for (int r = 0; r < 3; r++) {
        for (int c = 0; c < 2; c++) {
            printf("%d ", m[r][c]);
        }
        printf("\n");
    }
    return 0;
}
```

No error from plain `gcc`. Wrong output (third line is random; on screen: "your numbers will differ"):

```text
1 2 
4 5 
895724288 243280087 
```

Fixed:

```c
    for (int r = 0; r < 2; r++) {
        for (int c = 0; c < 3; c++) {
```

Fixed output:

```text
1 2 3 
4 5 6 
```

Why: m\[2\]\[3\] means 2 rows and 3 columns, so the outer (row) loop must use the first size and the inner (column) loop the second.

### Pun & challenge

- **Pun:** Why did the 2D array go to the cinema alone? It already had plenty of rows with its friends.
- **Challenge:** Add two 2x3 matrices a = {1 2 3, 4 5 6} and b = {6 5 4, 3 2 1} into sum and print it as a grid.
- **Challenge answer:**

```c
#include <stdio.h>

int main() {
    int a[2][3] = {{1, 2, 3}, {4, 5, 6}};
    int b[2][3] = {{6, 5, 4}, {3, 2, 1}};
    int sum[2][3];

    for (int r = 0; r < 2; r++) {
        for (int c = 0; c < 3; c++) {
            sum[r][c] = a[r][c] + b[r][c];
            printf("%d ", sum[r][c]);
        }
        printf("\n");
    }
    return 0;
}
```

```text
7 7 7 
7 7 7 
```

### Shorts for EP 45

**S1 · Your Cinema Seat Is a 2D Array** — 0:25 · built from scenes 1–3

- **Hook (first 1.5s):** Seat map with one glowing seat: "This is code."
- **Script:** Every cinema seat map is a 2D array. Rows and columns. To book row A, seat 3, the app writes seats zero, two, equals one. Row first, column second, both from zero. Full episode on the channel.
- **On-screen text:** seats\[0\]\[2\] = 1
- **Caption + hashtags:** Movie night, but make it C. #cprogramming #learntocode #kodingkonkani #2darray #codingforbeginners

**S2 · 2D Arrays in 30 Seconds** — 0:30 · built from scenes 4–5

- **Hook (first 1.5s):** A grid unrolls into one long line.
- **Script:** int seats three four: three rows, four columns, twelve boxes. Memory stores row zero, then row one, then row two, in one long line. To visit every cell, use two loops: the outer for rows, the inner for columns.
- **On-screen text:** \[ROW\]\[COLUMN\]
- **Caption + hashtags:** Grids are just rows in a line. #cprogramming #learntocode #kodingkonkani #2darray #nestedloops

**S3 · My Matrix Printed Sideways** — 0:35 · built from scene 9

- **Hook (first 1.5s):** Terminal: "1 2 / 4 5 / 895724288 ...". "Where did 3 and 6 go?"
- **Script:** Where did 3 and 6 go? The matrix is two rows, three columns, but the loops ran three rows and two columns. So it skipped real values and read a row that does not exist. Outer loop, first size. Inner loop, second size.
- **On-screen text:** m\[2\]\[3\] → r < 2, c < 3
- **Caption + hashtags:** Rows and columns are not interchangeable. #cprogramming #learntocode #kodingkonkani #bugoftheday #debugging

**S4 · Plenty of Rows** — 0:12 · built from scene 8

- **Hook (first 1.5s):** Xecxec alone in a cinema with popcorn.
- **Script:** Why did the 2D array go to the cinema alone? It already had plenty of rows with its friends.
- **On-screen text:** PLENTY OF ROWS WITH ITS FRIENDS
- **Caption + hashtags:** Arrays have drama too. #cprogramming #codingmemes #kodingkonkani #programmerhumor #learntocode

**S5 · How Many Boxes?** — 0:20 · built from scene 4

- **Hook (first 1.5s):** "int x\[4\]\[5\]; How many ints? What is the last cell?"
- **Script:** int x four five. How many ints is that, and what is the last cell? Pause and guess. Twenty ints, four rows times five columns. The last cell is x three, four, because both indexes start at zero.
- **On-screen text:** 20 · x\[3\]\[4\]
- **Caption + hashtags:** Two answers, one trap. #cprogramming #codingquiz #kodingkonkani #learntocode #2darray

## EP 46 — Arrays & Functions: Hand Over the Whole Locker Row

**Module 6 · Arrays · 6:30 · Peach + Dark blue · Prerequisite: EP 45**

**Learning goals:** write a function that takes an array and its size; count elements with sizeof(arr) / sizeof(arr\[0\]) in the place where the array is declared; explain why a function can change the caller's array (unlike EP 38's ints); avoid using sizeof on an array parameter.

### YouTube

- **Title:** Passing Arrays to Functions in C (sizeof Trap) | EP 46
- **Description:** In EP 38 a function could not change your variables. Pass an array, and suddenly it can. Learn how to pass arrays to functions, why you must also pass the size, and why sizeof gives the wrong answer inside a function. 0:00 The surprise · 0:20 Title · 0:25 Passing the row · 1:05 Counting with sizeof · 1:50 Code walkthrough · 3:40 Running it · 4:00 Why it changed · 4:30 Pun · 4:35 Bug of the Day · 5:40 Challenge · 6:10 Module 6 wrap
- **Tags:** c programming, pass array to function in c, sizeof array, arrays and functions, array parameter c, call by value array, learn c, c for beginners, koding konkani, c interview questions, class 12 computer science
- **Thumbnail:** big text "sizeof LIES?"; a function box receiving a whole row of lockers through a door; Xecxec holding a ruler that shows the wrong length; dark-blue on peach

### Scene list

| # | Start | Length | Template | On screen | Animation & SFX |
| --- | --- | --- | --- | --- | --- |
| 1 | 0:00 | 0:20 | Concept slide | Split screen: EP 38 int x unchanged vs today's array changed | Left box stays 5; right lockers all increase by 5; record-scratch SFX |
| 2 | 0:20 | 0:05 | Title card | EP 46 · ARRAYS & FUNCTIONS | Title slams in; claw click |
| 3 | 0:25 | 0:40 | Concept slide | Function header: void printArray(int arr\[\], int size) | arr\[\] and size labels pop out with arrows: "which row" and "how many"; pop SFX |
| 4 | 1:05 | 0:45 | Memory boxes | sizeof(marks) = 20 bytes, sizeof(marks\[0\]) = 4 bytes, 20 / 4 = 5 | Byte ruler slides under the lockers; "on most PCs" sticker |
| 5 | 1:50 | 1:50 | Code explain | ep46\_arrfunc.c types itself | Line highlights; tracker shows n, i, marks\[\] |
| 6 | 3:40 | 0:20 | Terminal | gcc ep46\_arrfunc.c -o ep46 then ./ep46 | Two lines print; second line glows mint |
| 7 | 4:00 | 0:30 | Memory boxes | main's marks and the function's arr both point to the same lockers | A single locker row with two name tags; arrow from arr to marks |
| 8 | 4:30 | 0:05 | Pun card | Pun | Xecxec rimshot |
| 9 | 4:35 | 1:05 | Bug of the Day | sizeof(arr) inside average(); warning, average 85.00 | Ruler inside the function shrinks to 8 bytes; only 2 lockers counted; alarm buzz |
| 10 | 5:40 | 0:30 | Challenge | Write float average(int arr\[\], int size) | Empty function box; ticking clock |
| 11 | 6:10 | 0:20 | Outro | Module 6 complete; next: EP 47 Strings | Lockers turn into letters H-E-L-L-O; Xecxec claps; sign-off |

### Narration script

**\[1 · Hook\]** Remember EP 38? We passed an int to a function, the function changed it, and back in main, nothing had changed. The function only got a copy. Today we pass an array to a function, the function adds five to every mark, and back in main... every mark has changed. What is going on?

**\[2 · Title\]** Episode 46. Arrays and functions.

**\[3 · Passing the row\]** To pass an array, write the type, the name, and empty square brackets: int arr, square brackets. That tells C, this function receives a row of ints. But here is the catch. The function does not know how many lockers are in the row. So we always pass a second parameter, int size. One parameter says which row. The other says how many lockers it has.

**\[4 · Counting with sizeof\]** In main, there is a neat trick to count the elements. sizeof marks gives the size of the whole array in bytes. On most PCs an int is four bytes, so five ints make twenty bytes. sizeof marks zero gives the size of one element, four. Twenty divided by four is five. The nice part: if you add a sixth mark later, n updates by itself. But remember where we did this: in main, where the array was declared. Hold that thought for the Bug of the Day.

**\[5 · Code walkthrough\]** Let's read it. \[HL 3\] Line three, printArray takes int arr, brackets, and int size. It returns nothing, so void. \[HL 4\] Line four loops i from zero while i is less than size, \[HL 5\] and line five prints each element. Exactly the loop from EP 41, just inside a function now. \[HL 10\] Line ten, addBonus takes the array, the size, and a bonus. \[HL 12\] Line twelve: arr i plus equals bonus. This changes the actual elements. \[HL 17\] Down in main, line seventeen. marks with empty brackets; the compiler counts five values. \[HL 18\] Line eighteen, n equals sizeof marks divided by sizeof marks zero. \[TRACK n=5\] \[HL 20\] Line twenty calls printArray. Look at how we pass it: just the name, marks. No brackets. \[TRACK marks={78,92,65,88,71}\] \[HL 21\] Line twenty-one calls addBonus with marks, n and five. \[TRACK marks={83,97,70,93,76}\] \[HL 22\] Line twenty-two prints again.

**\[6 · Running it\]** Compile and run. First line: 78, 92, 65, 88, 71. Second line: 83, 97, 70, 93, 76. Every mark went up by five, and the change happened in main's array.

**\[7 · Why it changed\]** Here is why. When you pass an int, C copies the value. But C never copies a whole array into a function. Instead, it passes the location of the array, where the lockers are. So arr inside the function and marks in main are two name tags on the same row of lockers. Change a locker through arr, and marks sees it. How exactly that works is a pointer story, and pointers get their own module, starting with EP 52.

**\[8 · Pun\]** Why do arrays make great friends? They never come to a function alone; they always bring their size.

**\[9 · Bug of the Day\]** Today's bug. Someone writes float average, int arr, brackets, and inside, n equals sizeof arr divided by sizeof arr zero. The trick from main, right? Compile it. GCC gives a warning: sizeof on array function parameter arr will return size of int star. Run it anyway. Average: 85.00. The real average is 78.80. Here is what happened. Inside the function, arr is not the whole array, it is only the location of the array. On a 64-bit PC that location takes eight bytes. Eight divided by four is two. So the function averaged only the first two marks: 78 and 92, which gives 85. The fix: count with sizeof in main, where the array lives, and pass the size in as a parameter.

**\[10 · Challenge\]** Your challenge. Write a function float average, int arr brackets, int size. It returns the average as a float, using the cast from EP 13. Call it from main with the five marks. The correct answer is 78.80.

**\[11 · Outro\]** That is Module 6 done. You can store, search, swap and pass arrays. Next module, we look at a special kind of array, one full of letters. Strings. Keep coding, says Xecxec!

### Code shown

```c
#include <stdio.h>

void printArray(int arr[], int size) {
    for (int i = 0; i < size; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
}

void addBonus(int arr[], int size, int bonus) {
    for (int i = 0; i < size; i++) {
        arr[i] += bonus;
    }
}

int main() {
    int marks[] = {78, 92, 65, 88, 71};
    int n = sizeof(marks) / sizeof(marks[0]);

    printArray(marks, n);
    addBonus(marks, n, 5);
    printArray(marks, n);
    return 0;
}
```

**Expected output**

```text
78 92 65 88 71 
83 97 70 93 76 
```

### Bug of the Day

```c
#include <stdio.h>

float average(int arr[]) {
    int n = sizeof(arr) / sizeof(arr[0]);
    int sum = 0;
    for (int i = 0; i < n; i++) {
        sum += arr[i];
    }
    return (float)sum / n;
}

int main() {
    int marks[] = {78, 92, 65, 88, 71};
    printf("Average: %.2f\n", average(marks));
    return 0;
}
```

GCC warning (plain `gcc avg_bug.c -o avg_bug`, no flags needed):

```text
avg_bug.c: In function 'average':
avg_bug.c:4:19: warning: 'sizeof' on array function parameter 'arr' will return size of 'int *' [-Wsizeof-array-argument]
    4 |     int n = sizeof(arr) / sizeof(arr[0]);
      |                   ^
avg_bug.c:3:19: note: declared here
    3 | float average(int arr[]) {
      |               ~~~~^~~~~
```

Wrong output on a 64-bit PC (8-byte address / 4-byte int = 2 elements; on screen: "depends on your machine"):

```text
Average: 85.00
```

Fixed:

```c
float average(int arr[], int size) {
    int sum = 0;
    for (int i = 0; i < size; i++) {
        sum += arr[i];
    }
    return (float)sum / size;
}
```

Why: inside a function an array parameter is really just the array's address, so sizeof measures the address, not the array; count in the caller and pass the size.

### Pun & challenge

- **Pun:** Why do arrays make great friends? They never come to a function alone; they always bring their size.
- **Challenge:** Write float average(int arr\[\], int size) and call it from main with {78, 92, 65, 88, 71}.
- **Challenge answer:**

```c
#include <stdio.h>

float average(int arr[], int size) {
    int sum = 0;
    for (int i = 0; i < size; i++) {
        sum += arr[i];
    }
    return (float)sum / size;
}

int main() {
    int marks[] = {78, 92, 65, 88, 71};
    int n = sizeof(marks) / sizeof(marks[0]);
    printf("Average: %.2f\n", average(marks, n));
    return 0;
}
```

```text
Average: 78.80
```

### Shorts for EP 46

**S1 · This Function Changed My Array!** — 0:25 · built from scenes 1, 6

- **Hook (first 1.5s):** Split screen: int stays 5, array marks all jump by 5.
- **Script:** Pass an int to a function, change it, and main does not see the change. Pass an array, change it, and main does see it. Same language, different rules. The reason is in the full episode.
- **On-screen text:** int: NO CHANGE · ARRAY: CHANGED
- **Caption + hashtags:** Why arrays break the call-by-value rule. #cprogramming #learntocode #kodingkonkani #arrays #functions

**S2 · Count an Array in 30 Seconds** — 0:30 · built from scene 4

- **Hook (first 1.5s):** "How many elements? Let C count."
- **Script:** Want C to count your array for you? sizeof marks gives the total bytes. sizeof marks zero gives the bytes of one element. Divide them, and you get the number of elements. Twenty bytes divided by four is five. Only works where the array is declared.
- **On-screen text:** sizeof(arr) / sizeof(arr\[0\])
- **Caption + hashtags:** The array-length trick every C coder uses. #cprogramming #learntocode #kodingkonkani #sizeof #codingforbeginners

**S3 · sizeof Lied to Me** — 0:40 · built from scene 9

- **Hook (first 1.5s):** Terminal: "Average: 85.00" next to the real answer 78.80.
- **Script:** My average says 85, but the real answer is 78.80. I used sizeof inside the function. There, the array is just an address, eight bytes on a 64-bit PC. Eight divided by four is two, so it averaged only two marks. GCC even warned me. Count in main, pass the size.
- **On-screen text:** sizeof INSIDE A FUNCTION = WRONG
- **Caption + hashtags:** The warning you should never ignore. #cprogramming #learntocode #kodingkonkani #bugoftheday #debugging

**S4 · Bring Your Size** — 0:12 · built from scene 8

- **Hook (first 1.5s):** Xecxec walking a locker row on a leash, with a size tag.
- **Script:** Why do arrays make great friends? They never come to a function alone; they always bring their size.
- **On-screen text:** THEY ALWAYS BRING THEIR SIZE
- **Caption + hashtags:** Good manners, C style. #cprogramming #codingmemes #kodingkonkani #programmerhumor #learntocode

**S5 · What Gets Printed?** — 0:22 · built from scenes 5–7

- **Hook (first 1.5s):** "addBonus(marks, 5, 10); marks\[0\] was 78. Now?"
- **Script:** marks zero is 78. We call addBonus with marks, five, and ten, which adds ten to every element. What is marks zero in main now? Pause and guess. 88. Arrays are not copied into functions, so the change sticks.
- **On-screen text:** 78 → ?   → 88
- **Caption + hashtags:** Did you think it would stay 78? #cprogramming #codingquiz #kodingkonkani #learntocode #arrays
