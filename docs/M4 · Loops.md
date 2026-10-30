# Module 4 — Loops

Episodes 26–33 · Butter + Dark blue

## EP 26 — Why Loops? The while Loop

**Module 4 · Loops · 6:15 · Butter + Dark blue · Prerequisite: EP 25**

**Learning goals:** explain why we use loops instead of copy-pasting lines; write a `while` loop with a counter, a condition and an update; trace a loop by hand, iteration by iteration; spot and stop an infinite loop (Ctrl+C).

### YouTube

- **Title:** Stop Copy-Pasting! The while Loop | C Programming EP 26
- **Description:** Your teacher says "write sorry 100 times". In C, you write it once and let a while loop do the rest. We build a while loop line by line, trace it on screen, and learn how to escape the dreaded infinite loop. 0:00 Write sorry 100 times 0:25 Why loops? 1:05 How a while loop works 1:50 Your first while loop, line by line 3:45 Fish that double every day 4:45 Bug of the Day: the infinite loop 5:35 Challenge
- **Tags:** c programming, while loop in c, loops in c, c tutorial for beginners, learn c, infinite loop, c programming class 11, c programming class 12, koding konkani, gcc, iteration
- **Thumbnail:** big text "STOP COPY-PASTING"; a stack of 100 identical `printf` lines crossed out next to a tiny 4-line while loop; Xecxec holding a red pen, smug; Butter background, Dark blue text blocks.

### Scene list

| # | Start | Length | Template | On screen | Animation & SFX |
| --- | --- | --- | --- | --- | --- |
| 1 | 0:00 | 0:20 | Concept slide | Notebook page: "I will not talk in class" written 100 times; a hand cramping | Lines multiply fast down the page, page flips, groan SFX; Xecxec faints onto the notebook |
| 2 | 0:20 | 0:05 | Title card | EP 26 · WHY LOOPS? THE WHILE LOOP | Butter card slides in, Dark blue text, claw-click |
| 3 | 0:25 | 0:40 | Concept slide | Five `printf("Sorry\n");` lines vs one loop box with "repeat 5 times" | Copy-paste stack grows to 100 and topples; loop box glows; whoosh |
| 4 | 1:05 | 0:45 | Concept slide | Flowchart: start → condition? → yes: body → update → back to condition; no: exit | Arrow traces the cycle 3 times; the condition diamond flashes Mint (true) then Tomato (false) |
| 5 | 1:50 | 1:30 | Code explain | `sorry.c` with variable tracker for `i` | Line highlights in Butter; tracker box for `i` ticks 1→6; each iteration adds a line to a mini terminal on the right |
| 6 | 3:20 | 0:20 | Terminal | `gcc sorry.c -o sorry` then `./sorry` | Typing SFX, output lines appear one by one |
| 7 | 3:40 | 0:05 | Pun card | Pun | Xecxec spins in a circle, rimshot |
| 8 | 3:45 | 1:00 | Code explain | `double.c` with trackers for `fish` and `day` | Fish icons double in a basket each iteration; tracker table fills row by row |
| 9 | 4:45 | 0:50 | Bug of the Day | `i++` deleted; terminal floods with "Sorry 1" | Butter frame, alarm SFX, terminal scrolls endlessly, "Ctrl+C" keycap slams down |
| 10 | 5:35 | 0:25 | Challenge | "Print 1 to 50 on one line" | Timer ring, Xecxec taps a clipboard |
| 11 | 6:00 | 0:15 | Outro | Next: EP 27, the for loop | Xecxec waves, claw-click, end card |

### Narration script

**\[1 · Hook\]** Your teacher says: write "I will not talk in class" one hundred times. By line twenty, your hand hurts. By line fifty, you are spelling "class" with three S's. Computers never get tired of repeating. Today we teach C to do the boring part for us.

**\[2 · Title\]** Episode twenty-six. Why loops? The while loop.

**\[3 · Why loops\]** Suppose we want to print "Sorry" five times. We could write printf five times. It works. But what about a hundred times? Or a number the user types in? Copy-paste breaks down fast, and if you need to change the message, you change it in a hundred places. A loop says: here is one block of code, now repeat it while some condition is true. Write once, run many times. That is the whole idea.

**\[4 · How while works\]** A while loop has a simple shape. The word while, a condition in round brackets, and a body in curly braces. C checks the condition. If it is true, it runs the body, then goes back and checks again. If it is false, it skips the body and moves on. Think of a Panjim bus conductor shouting "Panjim, Panjim!" while there are empty seats. Seats empty? Shout again. Bus full? Stop shouting and drive. Almost every loop needs three things: a starting value, a condition, and an update that moves us towards the end.

**\[5 · Code explain\]** Here is our program. \[HL 4\] Line four: int i equals 1. This is our counter, and it starts at one. \[TRACK i=1\] \[HL 6\] Line six: while, i less than or equal to 5. C checks: is 1 less than or equal to 5? Yes. So we go inside. \[HL 7\] Line seven: printf, Sorry, percent d, and we pass i. So it prints "Sorry 1". \[HL 8\] Line eight: i plus plus. This adds one to i. \[TRACK i=2\] Now we hit the closing brace, and C jumps back up to line six. Is 2 less than or equal to 5? Yes. Print "Sorry 2", i becomes 3. \[TRACK i=3\] Again: "Sorry 3", i becomes 4. \[TRACK i=4\] "Sorry 4", i becomes 5. \[TRACK i=5\] Is 5 less than or equal to 5? Yes, equal counts. Print "Sorry 5", and i becomes 6. \[TRACK i=6\] Now the check: is 6 less than or equal to 5? No. The condition is false, so C jumps past the closing brace. \[HL 11\] Line eleven prints "Done! i is now 6". Notice that: after the loop, i is one more than the last value printed. Remember this, it will save you in exams. \[HL 12\] And return 0 ends the program. Each trip through the body is called an iteration. This loop did five iterations.

**\[6 · Terminal\]** Let's compile and run. gcc sorry dot c, dash o sorry. Then dot slash sorry. Five sorries, and "Done! i is now 6". Change the 5 to 100, and you get a hundred sorries. Same four lines of code.

**\[7 · Pun\]** Why did the while loop never get bored? Because it always had something to repeat to itself.

**\[8 · Fish doubling\]** While loops shine when you don't know how many times you'll repeat. A fisherman at Mapusa market starts with 1 fish. Every day, his catch doubles. How many days until he has at least 100? \[HL 4\] fish starts at 1. \[HL 5\] day starts at 1. \[TRACK fish=1 day=1\] \[HL 7\] While fish is less than 100. \[HL 8\] fish equals fish times 2. \[HL 9\] day plus plus. Watch the tracker. 2 on day 2. 4 on day 3. 8, 16, 32, 64. \[TRACK fish=64 day=7\] 64 is still less than 100, so one more trip: 128 on day 8. \[TRACK fish=128 day=8\] Now 128 is not less than 100, so the loop stops. \[HL 12\] We print "Day 8: 128 fish". We never told C "repeat seven times". The condition decided.

**\[9 · Bug of the Day\]** Today's bug is the most famous loop bug of all. Go back to sorry dot c and delete the i plus plus line. Compile. No error. No warning. Run it. "Sorry 1, Sorry 1, Sorry 1" and it never stops. Why? i stays 1 forever, so i less than or equal to 5 is always true. This is an infinite loop. To escape, click on the terminal and press Control plus C. That stops the running program. The fix: make sure something inside the loop moves you towards the exit. Put i plus plus back.

**\[10 · Challenge\]** Your challenge: use a while loop to print the numbers 1 to 50 on one line, separated by spaces. Hint: use percent d followed by a space, and print the newline only after the loop. Answer in the next episode.

**\[11 · Outro\]** Next episode: the for loop, a loop that packs start, condition and update into one neat line. Keep coding, says Xecxec!

### Code shown

```c
#include <stdio.h>

int main(void) {
    int i = 1;

    while (i <= 5) {
        printf("Sorry %d\n", i);
        i++;
    }

    printf("Done! i is now %d\n", i);
    return 0;
}
```

```text
Sorry 1
Sorry 2
Sorry 3
Sorry 4
Sorry 5
Done! i is now 6
```

```c
#include <stdio.h>

int main(void) {
    int fish = 1;
    int day = 1;

    while (fish < 100) {
        fish = fish * 2;
        day++;
    }

    printf("Day %d: %d fish\n", day, fish);
    return 0;
}
```

```text
Day 8: 128 fish
```

### Bug of the Day

```c
#include <stdio.h>

int main(void) {
    int i = 1;

    while (i <= 5) {
        printf("Sorry %d\n", i);
    }

    return 0;
}
```

GCC gives no error and no warning (even with `-Wall -Wextra`). The program prints this forever until you press Ctrl+C:

```text
Sorry 1
Sorry 1
Sorry 1
...
```

Fixed:

```c
    while (i <= 5) {
        printf("Sorry %d\n", i);
        i++;
    }
```

Without `i++` the counter never changes, so the condition `i <= 5` stays true forever.

### Pun & challenge

- **Pun:** Why did the while loop never get bored? Because it always had something to repeat to itself.
- **Challenge:** Use a while loop to print 1 to 50 on one line, separated by spaces.
- **Challenge answer:**

```c
int i = 1;
while (i <= 50) {
    printf("%d ", i);
    i++;
}
printf("\n");
```

### Shorts for EP 26

**S1 · Write Sorry 100 Times? Never Again** — 0:25 · built from scenes 1–3

- **Hook (first 1.5s):** Notebook with lines multiplying, "100 TIMES?!"
- **Script:** Your teacher says write "sorry" one hundred times. Your hand gives up at twenty. In C, you write it once. A while loop repeats a block of code as long as a condition is true. Four lines, a hundred sorries. Full episode on Koding Konkani.
- **On-screen text:** 100 TIMES? / WRITE IT ONCE / while (i <= 100)
- **Caption + hashtags:** Let C write your punishment lines. #cprogramming #learntocode #kodingkonkani #whileloop #codingforbeginners

**S2 · The while Loop in 30 Seconds** — 0:30 · built from scenes 4–5

- **Hook (first 1.5s):** Flowchart arrow spinning round the loop
- **Script:** A while loop in thirty seconds. Start a counter: int i equals 1. Write while, and a condition: i less than or equal to 5. Inside, do your work, then i plus plus. C checks the condition, runs the body, comes back, checks again. When the condition turns false, it exits. Start, check, update. That's every loop.
- **On-screen text:** START / CHECK / UPDATE
- **Caption + hashtags:** Three parts of every loop. #cprogramming #learntocode #kodingkonkani #whileloop #ctutorial

**S3 · The Loop That Never Ends** — 0:25 · built from scene 9

- **Hook (first 1.5s):** Terminal flooding with "Sorry 1"
- **Script:** This program prints "Sorry 1" forever. No error, no warning. Why? We forgot i plus plus, so i stays 1, and the condition is always true. Press Control C to stop it. Then put the update back.
- **On-screen text:** INFINITE LOOP / CTRL + C / FORGOT i++
- **Caption + hashtags:** Every coder's first infinite loop. #cprogramming #learntocode #kodingkonkani #debugging #infiniteloop

**S4 · Pun: The Loop Who Talks to Itself** — 0:10 · built from scene 7

- **Hook (first 1.5s):** Xecxec spinning in circles
- **Script:** Why did the while loop never get bored? Because it always had something to repeat to itself.
- **On-screen text:** REPEAT TO ITSELF
- **Caption + hashtags:** Loop humour, repeat as needed. #cprogramming #codingmemes #kodingkonkani #programmerhumor

**S5 · What Is i After the Loop?** — 0:20 · built from scenes 5 and 10

- **Hook (first 1.5s):** "Exam question!" stamp
- **Script:** Quick quiz. i starts at 1. while i is less than or equal to 5, print i, then i plus plus. After the loop ends, what is i? Five? No. Six. The loop only stops when the check fails, and that happens at 6. Comment if you got it.
- **On-screen text:** WHAT IS i? / 5 or 6? / ANSWER: 6
- **Caption + hashtags:** The exam trap everyone falls for. #cprogramming #learntocode #kodingkonkani #cquiz #class12

## EP 27 — The for Loop

**Module 4 · Loops · 5:30 · Butter + Dark blue · Prerequisite: EP 26**

**Learning goals:** write a `for` loop and name its three parts (init, condition, update); count up, count down and add up a range with `for`; choose between `for` and `while`; avoid off-by-one errors with `<` vs `<=`.

### YouTube

- **Title:** The for Loop: A Loop With a Plan | C Programming EP 27
- **Description:** The for loop puts start, condition and update in one line, so you can see the whole plan at a glance. We count bus stops, add 1 to 10, do a countdown, and catch the off-by-one bug that costs students marks. 0:00 Last episode's challenge 0:25 Anatomy of a for loop 1:15 Three for loops, line by line 2:55 Run it 3:20 Bug of the Day: off-by-one 4:10 for or while? 4:50 Challenge
- **Tags:** c programming, for loop in c, loops in c, off by one error, c tutorial for beginners, learn c, c programming class 11, countdown loop, sum of numbers in c, koding konkani
- **Thumbnail:** big text "ONE LINE PLAN"; the line `for (int i = 1; i <= 5; i++)` split into three coloured chunks labelled START / CHECK / STEP; Xecxec pointing with a claw like a teacher; Butter background, Dark blue blocks.

### Scene list

| # | Start | Length | Template | On screen | Animation & SFX |
| --- | --- | --- | --- | --- | --- |
| 1 | 0:00 | 0:20 | Code explain | EP 26 challenge answer (while loop 1 to 50), then the same thing as a `for` loop | Four scattered lines slide together into one line; snap SFX |
| 2 | 0:20 | 0:05 | Title card | EP 27 · THE FOR LOOP | Butter card, claw-click |
| 3 | 0:25 | 0:50 | Concept slide | `for (init; condition; update)` with three labelled boxes and arrows showing run order 1→2→body→3→2… | Numbers pop onto each part in order; arrow loops 3 times |
| 4 | 1:15 | 1:40 | Code explain | `for1.c` with trackers for `i`, `sum`, `t` | Bus icon moves stop to stop for loop 1; `sum` tracker climbs to 55; countdown digits shrink |
| 5 | 2:55 | 0:20 | Terminal | Compile and run `for1.c` | Typing SFX, output appears line by line, "Go!" with a horn honk |
| 6 | 3:15 | 0:05 | Pun card | Pun | Xecxec holds up a calendar, rimshot |
| 7 | 3:20 | 0:50 | Bug of the Day | `i < 10` prints 1 to 9 | Butter frame, a missing "10" box blinks Tomato; buzzer |
| 8 | 4:10 | 0:40 | Concept slide | Two-column card: for = you know the count; while = you wait for a condition | Cards flip, Mint tick on each example |
| 9 | 4:50 | 0:25 | Challenge | "Print the multiplication table of any number" | Timer ring |
| 10 | 5:15 | 0:15 | Outro | Next: EP 28, do-while | Xecxec waves, end card |

### Narration script

**\[1 · Challenge recap\]** Last time, the challenge was to print 1 to 50 with a while loop. Start i at 1, while i is at most 50, print i and a space, then i plus plus. And print the newline after the loop. Did you get it? Now look at this. The start, the check and the update were spread over three lines. Today we squeeze all three into one line.

**\[2 · Title\]** Episode twenty-seven. The for loop.

**\[3 · Anatomy\]** A for loop has three parts inside the round brackets, separated by semicolons. First, the init: int i equals 1. This runs only once, at the very start. Second, the condition: i less than or equal to 5. This is checked before every iteration. Third, the update: i plus plus. This runs after every iteration, at the end of the body. So the order is: init, check, body, update, check, body, update, and so on, until the check is false. It's like planning a trip: where you start, where you stop, and how big each step is. All on one line, before you even begin.

**\[4 · Code explain\]** Let's read three for loops. \[HL 4\] Line four: for, int i equals 1, i less than or equal to 5, i plus plus. The variable i is created right here, inside the for. \[TRACK i=1\] \[HL 5\] Line five prints "Bus stop" and i. So: Bus stop 1. Then update, i is 2. \[TRACK i=2\] Check, print Bus stop 2. And so on up to Bus stop 5. When i becomes 6, the check fails and we leave. One small thing: because i was declared inside the for, it only exists inside that loop. Outside, i is gone. Second loop. \[HL 8\] int sum equals 0. Always start a total at zero. \[TRACK sum=0\] \[HL 9\] for, int n equals 1, n less than or equal to 10, n plus plus. \[HL 10\] sum equals sum plus n. Watch the tracker. n is 1, sum is 1. \[TRACK n=1 sum=1\] n is 2, sum is 3. \[TRACK n=2 sum=3\] n is 3, sum is 6. Then 10, 15, 21, 28, 36, 45, and finally 55. \[TRACK n=10 sum=55\] \[HL 12\] Line twelve prints "Sum of 1 to 10 = 55". Third loop counts down. \[HL 14\] for, int t equals 3, t greater than or equal to 1, t minus minus. Start at 3, keep going while t is at least 1, and subtract one each time. \[TRACK t=3\] \[HL 15\] Print t, then three dots and a space, no newline. So we get 3, 2, 1 on the same line. \[TRACK t=0\] When t hits 0, the check fails. \[HL 17\] Then we print "Go!" and a newline.

**\[5 · Terminal\]** Compile with gcc for1 dot c dash o for1, and run. Five bus stops. The sum is 55. And three, two, one, Go!

**\[6 · Pun\]** Why did the for loop always arrive on time? Because it planned everything in advance.

**\[7 · Bug of the Day\]** Today's bug: off-by-one. The task says print 1 to 10. A student writes: for int i equals 1, i less than 10, i plus plus. Compile: no error. Run: 1 2 3 4 5 6 7 8 9. Where is 10? When i is 10, is 10 less than 10? No. So the loop stops one step early. The fix: use less than or equal to 10. A quick check that always works: ask "what is the last value I want?" and test that value in your condition by hand.

**\[8 · for or while\]** So when do you use which? If you know how many times, use for. Ten bus stops, fifty numbers, the length of a list. If you are waiting for something to happen, use while. Waiting until the fish count passes 100, or until the user types zero. Both can do the same job. Choose the one that makes your code easier to read.

**\[9 · Challenge\]** Your challenge: ask the user for a number, and print its multiplication table from 1 to 10. For 7 it should print 7 x 1 = 7, all the way to 7 x 10 = 70. Use a for loop. Answer next episode.

**\[10 · Outro\]** Next episode: the do-while loop, the loop that acts first and asks questions later. Keep coding, says Xecxec!

### Code shown

```c
#include <stdio.h>

int main(void) {
    for (int i = 1; i <= 5; i++) {
        printf("Bus stop %d\n", i);
    }

    int sum = 0;
    for (int n = 1; n <= 10; n++) {
        sum = sum + n;
    }
    printf("Sum of 1 to 10 = %d\n", sum);

    for (int t = 3; t >= 1; t--) {
        printf("%d... ", t);
    }
    printf("Go!\n");
    return 0;
}
```

```text
Bus stop 1
Bus stop 2
Bus stop 3
Bus stop 4
Bus stop 5
Sum of 1 to 10 = 55
3... 2... 1... Go!
```

### Bug of the Day

```c
#include <stdio.h>

int main(void) {
    for (int i = 1; i < 10; i++) {
        printf("%d ", i);
    }
    printf("\n");
    return 0;
}
```

No compiler error or warning. Wrong output (task was 1 to 10):

```text
1 2 3 4 5 6 7 8 9
```

Fixed:

```c
    for (int i = 1; i <= 10; i++) {
```

With `<`, the loop stops when `i` equals 10, so the last value is never printed; `<=` includes it.

### Pun & challenge

- **Pun:** Why did the for loop always arrive on time? Because it planned everything in advance.
- **Challenge:** Read a number and print its multiplication table from 1 to 10.
- **Challenge answer:**

```c
int n;
printf("Enter a number: ");
scanf("%d", &n);
for (int i = 1; i <= 10; i++) {
    printf("%d x %d = %d\n", n, i, n * i);
}
```

### Shorts for EP 27

**S1 · One Line, Whole Plan** — 0:20 · built from scene 1

- **Hook (first 1.5s):** Three scattered code lines snapping into one
- **Script:** This while loop needs three separate lines: start, check, update. The for loop puts all three in one line. for int i equals 1, i less than or equal to 50, i plus plus. Same job, cleaner code.
- **On-screen text:** 3 LINES / 1 LINE / for loop
- **Caption + hashtags:** Same loop, half the clutter. #cprogramming #learntocode #kodingkonkani #forloop #cleancode

**S2 · The for Loop in 30 Seconds** — 0:30 · built from scene 3

- **Hook (first 1.5s):** The for line split into START / CHECK / STEP
- **Script:** Three parts, two semicolons. Init runs once at the start. The condition is checked before every round. The update runs after every round. Init, check, body, update, check, body, update, until the check is false. That's the for loop.
- **On-screen text:** START ; CHECK ; STEP
- **Caption + hashtags:** The for loop, decoded. #cprogramming #learntocode #kodingkonkani #forloop #ctutorial

**S3 · Where Did 10 Go?** — 0:25 · built from scene 7

- **Hook (first 1.5s):** Output "1 2 3 4 5 6 7 8 9" with a blinking empty box
- **Script:** Task: print 1 to 10. Output: 1 to 9. Where did 10 go? The condition says i less than 10, and 10 is not less than 10. Off-by-one. Use less than or equal to, and always test your last value by hand.
- **On-screen text:** WHERE IS 10? / i < 10 / i <= 10
- **Caption + hashtags:** The off-by-one bug costs marks. #cprogramming #learntocode #kodingkonkani #debugging #offbyone

**S4 · Pun: Always on Time** — 0:10 · built from scene 6

- **Hook (first 1.5s):** Xecxec with a calendar and a watch
- **Script:** Why did the for loop always arrive on time? Because it planned everything in advance.
- **On-screen text:** PLANNED IN ADVANCE
- **Caption + hashtags:** The most organised loop in C. #cprogramming #codingmemes #kodingkonkani #programmerhumor

**S5 · How Many Times Does It Run?** — 0:20 · built from scene 4

- **Hook (first 1.5s):** "Count the iterations!"
- **Script:** Quiz. for int t equals 3, t greater than or equal to 1, t minus minus. How many times does the body run? Three. t is 3, then 2, then 1. At 0 the check fails. Did you say 4? Comment your answer.
- **On-screen text:** HOW MANY TIMES? / ANSWER: 3
- **Caption + hashtags:** Count carefully. #cprogramming #learntocode #kodingkonkani #cquiz #forloop

## EP 28 — do-while: Ask First, Check Later

**Module 4 · Loops · 6:00 · Butter + Dark blue · Prerequisite: EP 27**

**Learning goals:** write a `do-while` loop and explain why its body always runs at least once; use `do-while` to re-ask for input until it is valid; build a repeating text menu; remember the semicolon after `while (...)`.

### YouTube

- **Title:** do-while: The Loop That Runs at Least Once | C EP 28
- **Description:** Some things must happen once before you can check them, like asking a user for input. The do-while loop runs first and checks later. We build an input checker and a repeating menu, and fix the missing-semicolon error. 0:00 Challenge answer and hook 0:25 while vs do-while 1:20 Input validation, line by line 2:30 A menu that repeats 4:00 Bug of the Day: missing semicolon 4:50 Challenge
- **Tags:** c programming, do while loop in c, do while vs while, menu driven program in c, input validation c, c tutorial for beginners, learn c, c programming class 12, koding konkani, loops in c
- **Thumbnail:** big text "RUNS ONCE. ALWAYS."; a door labelled `do` opening before a guard labelled `while`; Xecxec already inside, waving; Butter background, Dark blue blocks.

### Scene list

| # | Start | Length | Template | On screen | Animation & SFX |
| --- | --- | --- | --- | --- | --- |
| 1 | 0:00 | 0:20 | Code explain | EP 27 challenge answer: multiplication table of 7, then the hook "What if the user types 150 as their age?" | Table rows cascade in; "150?!" pops in Tomato |
| 2 | 0:20 | 0:05 | Title card | EP 28 · DO-WHILE | Butter card, claw-click |
| 3 | 0:25 | 0:55 | Code explain | `once.c`: while vs do-while with x = 10 | Split screen; left guard blocks entry (Tomato X), right door opens then guard checks; terminal shows only "do-while ran" |
| 4 | 1:20 | 1:10 | Code explain | `dowhile.c` age validation | Input bubbles 0, 150, 19 drop in; tracker for `age`; loop arrow turns Mint on 19 |
| 5 | 2:30 | 0:05 | Pun card | Pun | Xecxec tastes a feni-cashew, nods, rimshot |
| 6 | 2:35 | 1:15 | Code explain | `menu.c` balance menu | Menu card appears, choice bubbles 1, 2, 7, 3; `balance` tracker 500 → 600 |
| 7 | 3:50 | 0:10 | Terminal | Run `menu.c` with inputs 1, 2, 7, 3 | Typing SFX, output scrolls |
| 8 | 4:00 | 0:50 | Bug of the Day | Missing `;` after `while (n <= 3)` with GCC error | Butter frame, caret `^` bounces under the gap, a semicolon drops in with a click |
| 9 | 4:50 | 0:55 | Concept slide | Summary: while (check first, 0+ times), for (known count), do-while (1+ times) | Three cards, Xecxec stamps each |
| 10 | 5:45 | 0:15 | Challenge + Outro | "Build a chai shop menu" and Next: EP 29 | Timer ring, end card, wave |

### Narration script

**\[1 · Recap and hook\]** Last episode's challenge: a multiplication table. Read n, then for i from 1 to 10, print n times i. For 7 you get 7, 14, 21, all the way to 70. Now, a new problem. You ask a user for their age, and they type 150. Or zero. You want to keep asking until they type something sensible. But you must ask at least once before you can check anything.

**\[2 · Title\]** Episode twenty-eight. The do-while loop.

**\[3 · while vs do-while\]** Look at this program. \[HL 4\] x is 10. \[TRACK x=10\] \[HL 6\] A while loop: while x is less than 5. C checks first. 10 is not less than 5, so the body never runs. Zero times. \[HL 10\] Now a do-while. The word do, then the body in braces, \[HL 12\] then while and the condition at the bottom, with a semicolon. C runs the body first. It prints "do-while ran". Then it checks: is 10 less than 5? No. So it stops. But the body already ran once. That is the whole difference. while checks at the door. do-while lets you in, then checks.

**\[4 · Input validation\]** Here is where do-while really helps. \[HL 4\] int age, no value yet. \[HL 6\] do, open brace. \[HL 7\] Print "Enter your age, 1 to 120". \[HL 8\] scanf reads a number into age. Say the user types 0. \[TRACK age=0\] \[HL 9\] Now the check: while age less than 1, OR age greater than 120. Remember the OR from Episode 16: true if either side is true. 0 is less than 1, so the condition is true, and we loop back and ask again. The user types 150. \[TRACK age=150\] 150 is greater than 120: true again, ask again. The user types 19. \[TRACK age=19\] Is 19 less than 1? No. Greater than 120? No. Both false, so the condition is false. We exit. \[HL 11\] Print "Thanks! You are 19". We could not check age before reading it. That is why do-while fits.

**\[5 · Pun\]** Why does do-while love Goan feni? Because it always tries it once before deciding.

**\[6 · Menu\]** Now, a menu that repeats, like an ATM. \[HL 4\] int choice. \[HL 5\] balance starts at 500. \[TRACK balance=500\] \[HL 7\] do. \[HL 8\] Print the menu: 1, check balance. 2, add 100. 3, exit. \[HL 9\] \[HL 10\] Ask for the choice and read it. The user types 1. \[TRACK choice=1\] \[HL 12\] if choice equals 1, \[HL 13\] print the balance: 500. \[HL 20\] Now the check at the bottom: while choice is not equal to 3. 1 is not 3, so we show the menu again. The user types 2. \[TRACK choice=2\] \[HL 14\] else if choice equals 2, \[HL 15\] balance becomes 600, \[TRACK balance=600\] \[HL 16\] and we print "Added! Balance: 600". Not 3, so loop again. The user types 7. \[TRACK choice=7\] It is not 1, not 2. \[HL 17\] else if choice is not 3: \[HL 18\] "Invalid choice". Loop again. Finally, 3. \[TRACK choice=3\] None of the ifs print anything, and the check, choice not equal to 3, is false. We exit. \[HL 22\] "Bye!" Every menu-driven program in your practical exam follows this exact shape.

**\[7 · Terminal\]** Let's run it and type 1, 2, 7 and 3. Balance 500. Added, 600. Invalid choice. Bye.

**\[8 · Bug of the Day\]** Today's bug is tiny. One semicolon. Look at line nine: close brace, while, n less than or equal to 3, and nothing after. Compile. GCC says: error, expected semicolon before return. And the caret points just after the closing bracket. In a while loop you never put a semicolon after the condition. In a do-while you must, because the while is the end of the statement. The fix: add the semicolon. Then it prints 1, 2, 3.

**\[9 · Summary\]** So now you have three loops. while checks first and may run zero times. for is while with a plan, best when you know the count. do-while runs at least once, best for menus and input checks. Same engine, three different shapes.

**\[10 · Challenge and outro\]** Your challenge: build a chai shop menu. 1 for tea, 2 for coffee, 3 to exit. Print a message for each choice, and "Not on the menu" for anything else. Keep showing it until the user picks 3. Next episode: break and continue, the emergency exit and the skip button. Keep coding, says Xecxec!

### Code shown

```c
#include <stdio.h>

int main(void) {
    int x = 10;

    while (x < 5) {
        printf("while ran\n");
    }

    do {
        printf("do-while ran\n");
    } while (x < 5);

    return 0;
}
```

```text
do-while ran
```

```c
#include <stdio.h>

int main(void) {
    int age;

    do {
        printf("Enter your age (1-120): ");
        scanf("%d", &age);
    } while (age < 1 || age > 120);

    printf("Thanks! You are %d.\n", age);
    return 0;
}
```

```text
Enter your age (1-120): 0
Enter your age (1-120): 150
Enter your age (1-120): 19
Thanks! You are 19.
```

```c
#include <stdio.h>

int main(void) {
    int choice;
    int balance = 500;

    do {
        printf("\n1. Check balance\n2. Add 100\n3. Exit\n");
        printf("Choice: ");
        scanf("%d", &choice);

        if (choice == 1) {
            printf("Balance: %d\n", balance);
        } else if (choice == 2) {
            balance = balance + 100;
            printf("Added! Balance: %d\n", balance);
        } else if (choice != 3) {
            printf("Invalid choice\n");
        }
    } while (choice != 3);

    printf("Bye!\n");
    return 0;
}
```

```text

1. Check balance
2. Add 100
3. Exit
Choice: 1
Balance: 500

1. Check balance
2. Add 100
3. Exit
Choice: 2
Added! Balance: 600

1. Check balance
2. Add 100
3. Exit
Choice: 7
Invalid choice

1. Check balance
2. Add 100
3. Exit
Choice: 3
Bye!
```

Note on screen: the numbers after "Choice:" and after the age prompts are what the user types.

### Bug of the Day

```c
#include <stdio.h>

int main(void) {
    int n = 1;

    do {
        printf("%d\n", n);
        n++;
    } while (n <= 3)

    return 0;
}
```

```text
count.c: In function 'main':
count.c:9:21: error: expected ';' before 'return'
    9 |     } while (n <= 3)
      |                     ^
      |                     ;
   10 |
   11 |     return 0;
      |     ~~~~~~
```

Fixed:

```c
    } while (n <= 3);
```

The `while (...)` at the end of a do-while closes the whole statement, so it needs a semicolon, unlike a normal while loop.

### Pun & challenge

- **Pun:** Why does do-while love Goan feni? Because it always tries it once before deciding.
- **Challenge:** Build a chai shop menu: 1 = tea, 2 = coffee, 3 = exit, anything else = "Not on the menu". Repeat until the user picks 3.
- **Challenge answer:**

```c
int choice;
do {
    printf("1. Tea  2. Coffee  3. Exit\nChoice: ");
    scanf("%d", &choice);
    if (choice == 1) printf("One chai coming!\n");
    else if (choice == 2) printf("One coffee coming!\n");
    else if (choice != 3) printf("Not on the menu\n");
} while (choice != 3);
printf("Bye!\n");
```

### Shorts for EP 28

**S1 · The User Typed 150 as Their Age** — 0:25 · built from scenes 1 and 4

- **Hook (first 1.5s):** "Age: 150" in Tomato with a shocked Xecxec
- **Script:** Your program asks for age. The user types 150. Then zero. You need to keep asking until the answer makes sense, and you must ask at least once first. That's the job of the do-while loop. It runs, then checks. Full episode on Koding Konkani.
- **On-screen text:** AGE: 150?! / ASK AGAIN / do-while
- **Caption + hashtags:** Never trust user input. #cprogramming #learntocode #kodingkonkani #dowhile #inputvalidation

**S2 · while vs do-while in 30 Seconds** — 0:30 · built from scene 3

- **Hook (first 1.5s):** Guard at a door vs an open door
- **Script:** x is 10. while x is less than 5: the check happens first, it's false, the body runs zero times. do-while x is less than 5: the body runs first, prints once, then the check fails. while checks at the door. do-while lets you in, then checks. That's the only difference.
- **On-screen text:** CHECK FIRST / RUN FIRST / 0 vs 1
- **Caption + hashtags:** One difference, many exam marks. #cprogramming #learntocode #kodingkonkani #dowhile #ctutorial

**S3 · One Missing Semicolon** — 0:20 · built from scene 8

- **Hook (first 1.5s):** GCC error "expected ';' before 'return'"
- **Script:** expected semicolon before return. The culprit? The do-while's last line. A normal while has no semicolon after the condition. A do-while must have one. Add it, and the error is gone.
- **On-screen text:** } while (n <= 3); / DON'T FORGET ;
- **Caption + hashtags:** The semicolon that do-while needs. #cprogramming #learntocode #kodingkonkani #debugging #gcc

**S4 · Pun: Feni Logic** — 0:10 · built from scene 5

- **Hook (first 1.5s):** Xecxec holding a tiny cup
- **Script:** Why does do-while love Goan feni? Because it always tries it once before deciding.
- **On-screen text:** TRY ONCE, THEN DECIDE
- **Caption + hashtags:** do-while has a policy. #cprogramming #codingmemes #kodingkonkani #goa #programmerhumor

**S5 · Which Loop Runs at Least Once?** — 0:15 · built from scene 9

- **Hook (first 1.5s):** Three loop cards face down
- **Script:** Quiz: which loop is guaranteed to run its body at least once? while, for, or do-while? Answer: do-while. The other two can run zero times.
- **On-screen text:** WHICH ONE? / ANSWER: do-while
- **Caption + hashtags:** Viva favourite. #cprogramming #learntocode #kodingkonkani #cquiz #loops

## EP 29 — break & continue

**Module 4 · Loops · 6:00 · Butter + Dark blue · Prerequisite: EP 28**

**Learning goals:** use `break` to leave a loop early; use `continue` to skip the rest of one iteration; trace a loop that uses both; know that `break` leaves only the innermost loop, and use a flag to leave two.

### YouTube

- **Title:** break vs continue: Exit or Skip? | C Programming EP 29
- **Description:** Sometimes you need to leave a loop early, or skip just one round. break is the emergency exit, continue is the skip button. We trace both line by line and fix the classic "break only left one loop" bug. 0:00 Challenge answer and hook 0:25 break: the emergency exit 1:05 continue: the skip button 1:35 Both together, line by line 3:25 Bug of the Day: break in the wrong loop 4:55 Challenge
- **Tags:** c programming, break statement in c, continue statement in c, break vs continue, loops in c, nested loop break, c tutorial for beginners, learn c, koding konkani, c programming class 11
- **Thumbnail:** big text "EXIT OR SKIP?"; a red EXIT door and a yellow SKIP arrow; Xecxec mid-jump through the exit door; Butter background, Dark blue blocks.

### Scene list

| # | Start | Length | Template | On screen | Animation & SFX |
| --- | --- | --- | --- | --- | --- |
| 1 | 0:00 | 0:20 | Terminal | EP 28 challenge: chai menu run with 1, 5, 3 | Typing SFX; then a fire alarm rings over a looping track |
| 2 | 0:20 | 0:05 | Title card | EP 29 · BREAK & CONTINUE | Butter card, claw-click |
| 3 | 0:25 | 0:40 | Concept slide | Loop track with a red EXIT door: `break` jumps straight out | Xecxec runs laps, hits break, exits through door; door slam SFX |
| 4 | 1:05 | 0:30 | Concept slide | Same track: `continue` jumps from mid-lap back to the check | Xecxec skips a hurdle via a shortcut arrow; whoosh |
| 5 | 1:35 | 1:20 | Code explain | `brk.c` with trackers for `i`, `num` | Inputs 4, -3, 6, 0 drop in; skipped line greys out on continue; break arrow flies past the brace |
| 6 | 2:55 | 0:20 | Terminal | Run `brk.c` with 4, -3, 6, 0 | Output appears line by line |
| 7 | 3:15 | 0:05 | Pun card | Pun | Xecxec in a traffic police hat, whistle SFX |
| 8 | 3:20 | 0:15 | Code explain | `skip3.c` quick example | Multiples of 3 fade out from a number strip |
| 9 | 3:35 | 1:20 | Bug of the Day | `brkbug.c` nested search: break leaves only the inner loop; fix with a `found` flag | Butter frame; two nested tracks; break exits inner track only, outer keeps running (Tomato); fix shows flag flipping to 1 then second break |
| 10 | 4:55 | 0:50 | Concept slide | Rules card: break = leave loop, continue = next round, both only affect the innermost loop | Two icons stamp in |
| 11 | 5:45 | 0:15 | Challenge + Outro | "Print 1 to 30, skip multiples of 4, stop at the first number above 25 divisible by 7" and Next: EP 30 | Timer ring, end card |

### Narration script

**\[1 · Recap and hook\]** Last challenge: a chai shop menu with do-while. Show the menu, read a choice, print a message, and repeat while choice is not 3. Here it is running: 1, chai coming. 5, not on the menu. 3, bye. Now imagine you are running laps at Campal ground and the fire alarm rings. You don't finish your laps. You leave right now. C has a keyword for that.

**\[2 · Title\]** Episode twenty-nine. break and continue.

**\[3 · break\]** The word break, followed by a semicolon, means: leave this loop immediately. Don't run the rest of the body. Don't check the condition again. Jump to the first line after the loop's closing brace. You met break once already, in the switch statement. Same keyword, same idea: get out.

**\[4 · continue\]** continue is gentler. It means: skip the rest of this round, and go to the next one. In a for loop, it jumps to the update, then the check. In a while loop, it jumps straight to the check. The loop keeps going. Only this one round is cut short.

**\[5 · Code explain\]** Let's use both. \[HL 4\] int num, to hold the user's number. \[HL 6\] for i from 1 to 5. Up to five numbers. \[TRACK i=1\] \[HL 7\] \[HL 8\] Ask for number 1, and read it. The user types 4. \[TRACK num=4\] \[HL 10\] if num equals 0. No. \[HL 14\] if num less than 0. No. \[HL 18\] Print "Square = 16". Next round. \[TRACK i=2\] The user types minus 3. \[TRACK num=-3\] Is it 0? No. \[HL 14\] Is it less than 0? Yes. \[HL 15\] Print "Negative, skipped." \[HL 16\] continue. So we skip line eighteen, no square, and go straight to i plus plus. \[TRACK i=3\] The user types 6. \[TRACK num=6\] Square = 36. \[TRACK i=4\] Now the user types 0. \[TRACK num=0\] \[HL 10\] num equals 0, yes. \[HL 11\] Print "Stopping early." \[HL 12\] break. We leave the loop right now. i was only 4. The fifth number is never asked. \[HL 21\] We land on "Loop over."

**\[6 · Terminal\]** Run it with 4, minus 3, 6 and 0. Square 16. Negative, skipped. Square 36. Stopping early. Loop over. Exactly as we traced.

**\[7 · Pun\]** Why did the loop get a ticket from the traffic police? It took a break in the middle of the road.

**\[8 · Skip multiples\]** A quick one. For i from 1 to 20, if i mod 3 equals 0, continue. Otherwise print i. Mod 3 equals 0 means "divisible by 3". So 3, 6, 9 and the rest are skipped. We get 1, 2, 4, 5, 7, 8 and so on up to 20.

**\[9 · Bug of the Day\]** Today's bug catches almost everyone. We search a 3 by 3 grid for the cell at row 2, column 2. When we find it, we break. Run it. We see 1 comma 1, 1 comma 2, 1 comma 3, 2 comma 1, "Found it!"... and then 3 comma 1, 3 comma 2, 3 comma 3. The search kept going! Why? break only leaves the loop it is directly inside. Here that is the inner col loop. The outer row loop simply moves on to row 3. The fix: use a flag. Before the loops, int found equals 0. When we find it, set found to 1, then break the inner loop. Right after the inner loop, inside the outer one, check: if found, break again. Now the output stops right after "Found it!". No compiler error helps you here. You have to know the rule.

**\[10 · Rules\]** Two rules to remember. break leaves the loop. continue jumps to the next round. And both work only on the innermost loop they are inside. Use them when they make code clearer, not to patch messy logic.

**\[11 · Challenge and outro\]** Your challenge: loop i from 1 to 30. Skip any number divisible by 4, using continue. And stop the whole loop, using break, at the first number greater than 25 that is divisible by 7. Print each number that survives. Next episode: nested loops, loops inside loops. Keep coding, says Xecxec!

### Code shown

```c
#include <stdio.h>

int main(void) {
    int num;

    for (int i = 1; i <= 5; i++) {
        printf("Enter number %d (0 to stop): ", i);
        scanf("%d", &num);

        if (num == 0) {
            printf("Stopping early.\n");
            break;
        }
        if (num < 0) {
            printf("Negative, skipped.\n");
            continue;
        }
        printf("Square = %d\n", num * num);
    }

    printf("Loop over.\n");
    return 0;
}
```

```text
Enter number 1 (0 to stop): 4
Square = 16
Enter number 2 (0 to stop): -3
Negative, skipped.
Enter number 3 (0 to stop): 6
Square = 36
Enter number 4 (0 to stop): 0
Stopping early.
Loop over.
```

```c
#include <stdio.h>

int main(void) {
    for (int i = 1; i <= 20; i++) {
        if (i % 3 == 0) {
            continue;
        }
        printf("%d ", i);
    }
    printf("\n");
    return 0;
}
```

```text
1 2 4 5 7 8 10 11 13 14 16 17 19 20
```

### Bug of the Day

```c
#include <stdio.h>

int main(void) {
    for (int row = 1; row <= 3; row++) {
        for (int col = 1; col <= 3; col++) {
            if (row == 2 && col == 2) {
                printf("Found it!\n");
                break;
            }
            printf("(%d,%d) ", row, col);
        }
    }
    printf("\nSearch finished.\n");
    return 0;
}
```

No compiler error. Wrong output (the search continues into row 3):

```text
(1,1) (1,2) (1,3) (2,1) Found it!
(3,1) (3,2) (3,3) 
Search finished.
```

Fixed:

```c
#include <stdio.h>

int main(void) {
    int found = 0;
    for (int row = 1; row <= 3; row++) {
        for (int col = 1; col <= 3; col++) {
            if (row == 2 && col == 2) {
                printf("Found it!\n");
                found = 1;
                break;
            }
            printf("(%d,%d) ", row, col);
        }
        if (found) {
            break;
        }
    }
    printf("\nSearch finished.\n");
    return 0;
}
```

```text
(1,1) (1,2) (1,3) (2,1) Found it!

Search finished.
```

`break` exits only the innermost loop, so a flag is needed to stop the outer loop too.

### Pun & challenge

- **Pun:** Why did the loop get a ticket from the traffic police? It took a break in the middle of the road.
- **Challenge:** Loop 1 to 30. Skip numbers divisible by 4 (continue). Stop at the first number above 25 divisible by 7 (break). Print the rest.
- **Challenge answer:** prints `1 2 3 5 6 7 9 10 11 13 14 15 17 18 19 21 22 23 25 26 27`, then stops at 28 (above 25 and divisible by 7).

```c
for (int i = 1; i <= 30; i++) {
    if (i > 25 && i % 7 == 0) {
        break;
    }
    if (i % 4 == 0) {
        continue;
    }
    printf("%d ", i);
}
printf("\n");
```

### Shorts for EP 29

**S1 · The Fire Alarm Rings Mid-Loop** — 0:20 · built from scenes 1 and 3

- **Hook (first 1.5s):** Xecxec running laps, alarm bell rings
- **Script:** You're running laps. The fire alarm rings. You don't finish your laps, you leave now. In C, that's break. One word, and your loop is over, right there. Full episode on Koding Konkani.
- **On-screen text:** ALARM! / break; / LEAVE NOW
- **Caption + hashtags:** The emergency exit for loops. #cprogramming #learntocode #kodingkonkani #break #loops

**S2 · break vs continue in 30 Seconds** — 0:30 · built from scenes 3–4

- **Hook (first 1.5s):** EXIT door vs SKIP arrow
- **Script:** break and continue. break leaves the loop completely and jumps past the closing brace. continue skips only the rest of this round and moves to the next one. Exit versus skip. And both only affect the innermost loop.
- **On-screen text:** break = EXIT / continue = SKIP
- **Caption + hashtags:** Never mix them up again. #cprogramming #learntocode #kodingkonkani #continue #ctutorial

**S3 · Why Didn't break Stop My Search?** — 0:35 · built from scene 9

- **Hook (first 1.5s):** "Found it!" then more output keeps printing
- **Script:** We found the cell and called break. But the program kept searching row 3. Why? break only leaves the loop it's directly inside, the inner one. The outer loop carried on. Fix: set a found flag, and check it after the inner loop to break again.
- **On-screen text:** FOUND IT... AND KEPT GOING? / break = 1 LOOP ONLY / USE A FLAG
- **Caption + hashtags:** The nested-loop break trap. #cprogramming #learntocode #kodingkonkani #debugging #nestedloops

**S4 · Pun: Traffic Ticket** — 0:10 · built from scene 7

- **Hook (first 1.5s):** Xecxec blowing a whistle
- **Script:** Why did the loop get a ticket from the traffic police? It took a break in the middle of the road.
- **On-screen text:** BREAK IN THE MIDDLE OF THE ROAD
- **Caption + hashtags:** Loops must follow traffic rules too. #cprogramming #codingmemes #kodingkonkani #programmerhumor

**S5 · Predict the Output** — 0:20 · built from scene 8

- **Hook (first 1.5s):** "Predict it!" stamp
- **Script:** for i from 1 to 10. If i mod 3 is 0, continue. Print i. What prints? 1, 2, 4, 5, 7, 8, 10. The multiples of 3 are skipped. Comment if you got it right.
- **On-screen text:** PREDICT IT / 1 2 4 5 7 8 10
- **Caption + hashtags:** Can you trace continue? #cprogramming #learntocode #kodingkonkani #cquiz #continue

## EP 30 — Nested Loops

**Module 4 · Loops · 6:00 · Butter + Dark blue · Prerequisite: EP 29**

**Learning goals:** explain how an inner loop runs completely for each round of the outer loop; count total iterations (outer × inner); print a grid and a times table with nested `for` loops; use different counter variables for each loop.

### YouTube

- **Title:** Nested Loops: Rows and Columns Made Easy | C EP 30
- **Description:** A loop inside a loop sounds scary, but it's just rows of chairs: for every row, go through every seat. We trace nested loops step by step, build a 5×5 times table, and fix the bug where both loops share one variable. 0:00 Challenge answer and hook 0:25 How nested loops work 1:15 Rows and seats, line by line 2:40 A 5×5 times table 3:45 Bug of the Day: same variable in both loops 5:00 Challenge
- **Tags:** c programming, nested loops in c, nested for loop, loop inside loop, multiplication table in c, c tutorial for beginners, learn c, c programming class 11, koding konkani, 2d grid c
- **Thumbnail:** big text "LOOP IN A LOOP"; a grid of chairs with a highlighted row and an arrow sweeping across seats; Xecxec sitting in one chair with popcorn; Butter background, Dark blue blocks.

### Scene list

| # | Start | Length | Template | On screen | Animation & SFX |
| --- | --- | --- | --- | --- | --- |
| 1 | 0:00 | 0:20 | Terminal | EP 29 challenge output; then a school hall with 3 rows of 4 chairs | Chairs drop in row by row, thud SFX |
| 2 | 0:20 | 0:05 | Title card | EP 30 · NESTED LOOPS | Butter card, claw-click |
| 3 | 0:25 | 0:50 | Concept slide | Clock analogy: hour hand (outer) moves once while minute hand (inner) goes round fully | Minute hand spins 60 ticks, hour hand clicks once; tick SFX |
| 4 | 1:15 | 1:10 | Code explain | `nested.c` with trackers `row`, `seat` and a counter "prints: n/12" | Spotlight moves seat by seat; on each `\n` the spotlight drops a row |
| 5 | 2:25 | 0:15 | Terminal | Run `nested.c` | Output grid fills |
| 6 | 2:40 | 1:00 | Code explain | `times.c` 5×5 table with `%4d` | Cells fill row by row; `%4d` padding shown as dotted boxes |
| 7 | 3:40 | 0:05 | Pun card | Pun | Xecxec inside a box inside a bigger box, rimshot |
| 8 | 3:45 | 1:15 | Bug of the Day | `nestbug.c` shares `i`: prints only one row; fixed with `j` | Butter frame; single `i` tracker jumps to 5 and the outer check fails (Tomato); split into `i` and `j` trackers (Mint) |
| 9 | 5:00 | 0:45 | Challenge | "Ask rows and columns, print a grid of #" with sample 3×5 | Grid builds, timer ring |
| 10 | 5:45 | 0:15 | Outro | Next: EP 31, star patterns | Xecxec waves, end card |

### Narration script

**\[1 · Recap and hook\]** Last challenge: loop 1 to 30, skip multiples of 4 with continue, and break at the first number above 25 divisible by 7. The output ends at 27, because 28 triggers the break. Now picture the school hall on annual day. Three rows of chairs, four chairs in each row. The teacher checks every chair: row 1, seat 1, 2, 3, 4. Then row 2, seat 1, 2, 3, 4. That's a loop inside a loop.

**\[2 · Title\]** Episode thirty. Nested loops.

**\[3 · How it works\]** A nested loop is simply a loop inside the body of another loop. The outer loop is like the hour hand on a clock. The inner loop is the minute hand. For the hour hand to move once, the minute hand goes all the way round. In code: for every single round of the outer loop, the inner loop runs completely, from start to finish. So if the outer loop runs 3 times and the inner runs 4 times, the inner body runs 3 times 4, which is 12 times.

**\[4 · Code explain\]** \[HL 4\] Outer loop: for row from 1 to 3. \[TRACK row=1\] \[HL 5\] Inner loop: for seat from 1 to 4. \[TRACK seat=1\] \[HL 6\] Print R, row, S, seat, and a space. So "R1S1". The inner loop continues: seat 2, "R1S2". \[TRACK seat=2\] Seat 3, seat 4. \[TRACK seat=4\] Now seat becomes 5, the inner check fails, and the inner loop is done. \[HL 8\] We print a newline, so the cursor goes to the next line. That ends one round of the outer loop. Now row becomes 2. \[TRACK row=2\] And here's the key: the inner loop starts fresh. seat is created again, starting at 1. \[TRACK seat=1\] So we print R2S1, R2S2, R2S3, R2S4, then a newline. Same again for row 3. When row becomes 4, the outer check fails and we're done. Twelve prints in total. Inner loop prints across. Outer loop moves down.

**\[5 · Terminal\]** Compile and run. Three lines, four seats on each. A perfect grid.

**\[6 · Times table\]** Nested loops can build tables. \[HL 4\] Outer loop i from 1 to 5. \[HL 5\] Inner loop j from 1 to 5. \[HL 6\] printf percent 4 d, and i times j. Percent 4 d means: print this number using at least 4 character spaces, padded on the left. So every number lines up in neat columns, whether it's 1 or 25. \[TRACK i=1 j=1\] Row 1: 1, 2, 3, 4, 5. \[HL 8\] Newline. \[TRACK i=2\] Row 2: 2, 4, 6, 8, 10. \[TRACK i=5 j=5\] And row 5 ends with 25. Twenty-five calculations from five lines of code.

**\[7 · Pun\]** Why are nested loops so good at hide and seek? Because they always look inside every row.

**\[8 · Bug of the Day\]** Today's bug: same variable in both loops. A student declares int i at the top and uses i for both loops. The outer loop is for i from 1 to 3, the inner loop is also for i from 1 to 4. They expect 3 rows of 4 stars. Compile: no error, no warning. Run it: only one row of 4 stars. What happened? The inner loop takes over i. When the inner loop finishes, i is 5. Back in the outer loop, i plus plus makes it 6. Is 6 less than or equal to 3? No. The outer loop quits after one round. The fix: give each loop its own variable. Outer uses i, inner uses j. Now we get 3 rows of 4 stars. Tip: declaring the counter inside the for, like for int j, helps keep loops separate.

**\[9 · Challenge\]** Your challenge: ask the user for rows and columns, then print a grid of hash symbols with a space after each. For 3 and 5, you get 3 lines of 5 hashes. Next episode we'll use this exact grid to start drawing stars.

**\[10 · Outro\]** Next episode: pattern printing, the famous star triangles every exam loves. Keep coding, says Xecxec!

### Code shown

```c
#include <stdio.h>

int main(void) {
    for (int row = 1; row <= 3; row++) {
        for (int seat = 1; seat <= 4; seat++) {
            printf("R%dS%d ", row, seat);
        }
        printf("\n");
    }
    return 0;
}
```

```text
R1S1 R1S2 R1S3 R1S4
R2S1 R2S2 R2S3 R2S4
R3S1 R3S2 R3S3 R3S4
```

```c
#include <stdio.h>

int main(void) {
    for (int i = 1; i <= 5; i++) {
        for (int j = 1; j <= 5; j++) {
            printf("%4d", i * j);
        }
        printf("\n");
    }
    return 0;
}
```

```text
   1   2   3   4   5
   2   4   6   8  10
   3   6   9  12  15
   4   8  12  16  20
   5  10  15  20  25
```

### Bug of the Day

```c
#include <stdio.h>

int main(void) {
    int i;
    for (i = 1; i <= 3; i++) {
        for (i = 1; i <= 4; i++) {
            printf("* ");
        }
        printf("\n");
    }
    return 0;
}
```

No compiler error or warning. Wrong output (expected 3 rows):

```text
* * * *
```

Fixed:

```c
#include <stdio.h>

int main(void) {
    int i, j;
    for (i = 1; i <= 3; i++) {
        for (j = 1; j <= 4; j++) {
            printf("* ");
        }
        printf("\n");
    }
    return 0;
}
```

```text
* * * *
* * * *
* * * *
```

The inner loop leaves `i` at 5, so the outer loop's `i++` makes it 6 and its condition `i <= 3` fails after one row.

### Pun & challenge

- **Pun:** Why are nested loops so good at hide and seek? Because they always look inside every row.
- **Challenge:** Read rows and columns, then print a grid of ` #  ` of that size.
- **Challenge answer:**

```c
int rows, cols;
printf("Rows and columns: ");
scanf("%d %d", &rows, &cols);
for (int r = 1; r <= rows; r++) {
    for (int c = 1; c <= cols; c++) {
        printf("# ");
    }
    printf("\n");
}
```

### Shorts for EP 30

**S1 · 3 Rows, 4 Chairs, 1 Loop Inside Another** — 0:20 · built from scene 1

- **Hook (first 1.5s):** School hall chairs dropping in
- **Script:** Three rows of chairs, four in each row. To check every chair, you go row by row, and inside each row, seat by seat. That's a nested loop: a loop inside a loop. Full episode on Koding Konkani.
- **On-screen text:** ROW BY ROW / SEAT BY SEAT
- **Caption + hashtags:** Nested loops are just chairs in a hall. #cprogramming #learntocode #kodingkonkani #nestedloops #codingforbeginners

**S2 · Nested Loops in 30 Seconds** — 0:30 · built from scenes 3–4

- **Hook (first 1.5s):** Clock, minute hand spinning
- **Script:** Nested loops work like a clock. The minute hand goes all the way round for every single move of the hour hand. In C, the inner loop runs completely for each round of the outer loop. Outer 3, inner 4: the inner body runs 12 times. Inner prints across, outer moves down.
- **On-screen text:** INNER RUNS FULLY / 3 x 4 = 12
- **Caption + hashtags:** The clock trick for nested loops. #cprogramming #learntocode #kodingkonkani #nestedloops #ctutorial

**S3 · Why Did My Grid Print Only One Row?** — 0:30 · built from scene 8

- **Hook (first 1.5s):** One sad row of stars
- **Script:** Expected 3 rows of stars. Got one. The bug: both loops use i. The inner loop pushes i to 5, then the outer loop adds one, 6, and quits. Give the inner loop its own variable, j, and all 3 rows appear.
- **On-screen text:** ONLY 1 ROW? / SAME i TWICE / USE j
- **Caption + hashtags:** One variable, two loops, zero luck. #cprogramming #learntocode #kodingkonkani #debugging #nestedloops

**S4 · Pun: Hide and Seek** — 0:10 · built from scene 7

- **Hook (first 1.5s):** Xecxec peeking out of a box in a box
- **Script:** Why are nested loops so good at hide and seek? Because they always look inside every row.
- **On-screen text:** EVERY ROW. EVERY SEAT.
- **Caption + hashtags:** You can't hide from a nested loop. #cprogramming #codingmemes #kodingkonkani #programmerhumor

**S5 · How Many Stars?** — 0:15 · built from scenes 3 and 6

- **Hook (first 1.5s):** "Count them!"
- **Script:** Outer loop runs 5 times. Inner loop runs 5 times. The inner body prints one star. How many stars in total? 25. Five times five.
- **On-screen text:** 5 x 5 = ? / 25
- **Caption + hashtags:** Quick maths, nested style. #cprogramming #learntocode #kodingkonkani #cquiz #loops

## EP 31 — Pattern Printing 1: Stars and Triangles

**Module 4 · Loops · 7:00 · Butter + Dark blue · Prerequisite: EP 30**

**Learning goals:** use a row table (row number → how many stars) to plan any pattern; print a left triangle and an inverted triangle with nested loops; right-align a triangle using a separate spaces loop; match the width of a space to the width of a star.

### YouTube

- **Title:** The Star Pattern Exam Question, Solved | C Programming EP 31
- **Description:** Every C exam has a star pattern question. The secret is not memorising code: it is making a small row table first. We build a triangle, flip it upside down, push it to the right, and fix the spacing bug that turns a triangle into a pyramid. 0:00 Challenge answer and hook 0:30 The row table trick 1:20 Left triangle, line by line 2:45 Upside-down triangle 3:35 Right-aligned triangle 5:10 Bug of the Day: wrong spaces 6:20 Challenge
- **Tags:** c programming, star pattern in c, pattern printing in c, triangle pattern c, nested loops, c programming exam questions, c tutorial for beginners, learn c, koding konkani, c programming class 11
- **Thumbnail:** big text "STAR PATTERNS EASY"; a glowing star triangle beside a small row table (row / stars); Xecxec wearing sunglasses holding a star; Butter background, Dark blue blocks.

### Scene list

| # | Start | Length | Template | On screen | Animation & SFX |
| --- | --- | --- | --- | --- | --- |
| 1 | 0:00 | 0:30 | Terminal | EP 30 challenge: 3×5 grid of `#`, then an exam paper with "Print this pattern" and a star triangle | Grid prints; exam paper slides in, dramatic sting |
| 2 | 0:30 | 0:05 | Title card | EP 31 · PATTERN PRINTING 1 | Butter card, claw-click |
| 3 | 0:35 | 0:45 | Concept slide | Row table: row 1 → 1 star, row 2 → 2 … row 5 → 5; rule "stars = i" | Table rows appear beside the triangle; arrow links each row to its stars |
| 4 | 1:20 | 1:25 | Code explain | `tri.c` with trackers `i`, `j` | Stars drop in one by one; inner loop limit `j <= i` glows each row |
| 5 | 2:45 | 0:50 | Code explain | `invtri.c` (outer loop counts down) | Triangle flips upside down with a whoosh; tracker `i` 5 → 1 |
| 6 | 3:35 | 0:05 | Pun card | Pun | Xecxec with stars circling his head, rimshot |
| 7 | 3:40 | 1:30 | Code explain | `rt4.c` right-aligned triangle; row table now has two columns: spaces and stars | Spaces drawn as dotted grey boxes, stars in Tomato; each row shows "2 spaces per missing star" |
| 8 | 5:10 | 1:10 | Bug of the Day | `printf(" ")` instead of `printf("  ")`: a pyramid appears instead | Butter frame; triangle collapses into a pyramid; measuring tape shows `"* "` = 2 chars vs `" "` = 1 char |
| 9 | 6:20 | 0:25 | Challenge | "Print the upside-down right-aligned triangle" with target picture | Picture builds, timer ring |
| 10 | 6:45 | 0:15 | Outro | Next: EP 32, pyramids | Xecxec waves, end card |

### Narration script

**\[1 · Recap and hook\]** Last challenge: read rows and columns, then print a grid of hashes. Outer loop for rows, inner loop for columns, and a newline after each row. Three by five gives three lines of five hashes. Hold on to that grid. Because this question, "print the following pattern", appears in almost every C exam. And once you know the trick, it is free marks.

**\[2 · Title\]** Episode thirty-one. Pattern printing, part one.

**\[3 · Row table\]** Here is the trick. Don't look at the whole pattern. Look at it row by row, and make a little table. Row 1 has 1 star. Row 2 has 2 stars. Row 3, 3 stars. Row 5, 5 stars. So the rule is: in row i, print i stars. Outer loop: which row am I on. Inner loop: how many stars in this row. Every pattern in this episode and the next is just a different row table.

**\[4 · Left triangle\]** \[HL 4\] int n equals 5, the height. \[HL 6\] Outer loop: for i from 1 to n. One round per row. \[TRACK i=1\] \[HL 7\] Inner loop: for j from 1 to i. This is the rule from our table: row i has i stars. On row 1, j goes from 1 to 1, so one star. \[HL 8\] printf star space. \[HL 10\] After the inner loop, printf newline. Row 1 done: one star. \[TRACK i=2\] Row 2: j goes 1 to 2, two stars, then newline. \[TRACK i=3\] Row 3: three stars. And so on until row 5, five stars. Compare this with last episode's grid. The only change is the inner limit: j less than or equal to i, instead of j less than or equal to cols. That one change turns a rectangle into a triangle.

**\[5 · Upside-down\]** Now flip it. Row table: row 1 has 5 stars, row 2 has 4, down to 1. \[HL 6\] The easy way: make the outer loop count down. for i equals n, i greater than or equal to 1, i minus minus. \[TRACK i=5\] \[HL 7\] The inner loop stays the same: j from 1 to i. So the first row prints 5 stars, \[TRACK i=4\] then 4, then 3, then 2, \[TRACK i=1\] then 1. One small change, and the triangle stands on its head.

**\[6 · Pun\]** Why did the star pattern pass the exam? Because it knew its place, row by row.

**\[7 · Right-aligned\]** Now the harder one: a triangle leaning against the right wall. The stars are the same, 1, 2, 3, 4. But each row has empty space on the left. Our row table gets a second column. With n equals 4: row 1 has 3 missing stars, row 2 has 2, row 3 has 1, row 4 has none. So missing stars equals n minus i. \[HL 6\] Outer loop: i from 1 to n. \[TRACK i=1\] \[HL 7\] First inner loop: for s from 1 to n minus i. This one prints the blank space. \[HL 8\] printf, and in quotes, two spaces. Why two? Because each star we print is a star plus a space, which is two characters wide. So each missing star must be filled with two spaces. \[HL 10\] Second inner loop: for j from 1 to i, \[HL 11\] print star space. \[HL 13\] Then newline. Row 1: three gaps of two spaces, then one star. \[TRACK i=2\] Row 2: two gaps, two stars. \[TRACK i=4\] Row 4: no gaps, four stars. Two inner loops, one after the other, inside one outer loop. First the spaces, then the stars.

**\[8 · Bug of the Day\]** Today's bug: wrong spaces. Take the right-aligned triangle, and change the two spaces in line 8 to one space. Compile: no error. Run it. Surprise! Instead of a right-aligned triangle, we get a pyramid, nicely centred. Why? Each star is two characters wide, star plus space, but each gap is now only one character wide. So the gaps are half as wide as they should be, and the stars shift to the middle. The fix: the width of a gap must match the width of a star. Star space needs two spaces. Hold on to this accident, though. Next episode, we'll build pyramids on purpose.

**\[9 · Challenge\]** Your challenge: print this upside-down right-aligned triangle, with n equals 4. Four stars on top, then three, two, one, all touching the right wall. Hint: start from the right-aligned triangle and make the outer loop count down.

**\[10 · Outro\]** Next episode: pyramids and number patterns, crab-style. Keep coding, says Xecxec!

### Code shown

```c
#include <stdio.h>

int main(void) {
    int n = 5;

    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= i; j++) {
            printf("* ");
        }
        printf("\n");
    }
    return 0;
}
```

```text
*
* *
* * *
* * * *
* * * * *
```

```c
#include <stdio.h>

int main(void) {
    int n = 5;

    for (int i = n; i >= 1; i--) {
        for (int j = 1; j <= i; j++) {
            printf("* ");
        }
        printf("\n");
    }
    return 0;
}
```

```text
* * * * *
* * * *
* * *
* *
*
```

```c
#include <stdio.h>

int main(void) {
    int n = 4;

    for (int i = 1; i <= n; i++) {
        for (int s = 1; s <= n - i; s++) {
            printf("  ");
        }
        for (int j = 1; j <= i; j++) {
            printf("* ");
        }
        printf("\n");
    }
    return 0;
}
```

```text
      *
    * *
  * * *
* * * *
```

Note on screen: each printed line also has one trailing space after the last star (invisible in the terminal).

### Bug of the Day

```c
        for (int s = 1; s <= n - i; s++) {
            printf(" ");
        }
```

No compiler error. Wrong output (a centred pyramid instead of a right-aligned triangle):

```text
   *
  * *
 * * *
* * * *
```

Fixed:

```c
        for (int s = 1; s <= n - i; s++) {
            printf("  ");
        }
```

Each star is printed as `"* "` (2 characters), so each missing star must be filled with 2 spaces, not 1.

### Pun & challenge

- **Pun:** Why did the star pattern pass the exam? Because it knew its place, row by row.
- **Challenge:** With n = 4, print an upside-down right-aligned triangle (4 stars, then 3, 2, 1, all against the right edge).
- **Challenge answer:** output is `* * * *` / `   * * * ` / `     * * ` / `       * `.

```c
int n = 4;
for (int i = n; i >= 1; i--) {
    for (int s = 1; s <= n - i; s++) printf("  ");
    for (int j = 1; j <= i; j++) printf("* ");
    printf("\n");
}
```

### Shorts for EP 31

**S1 · The Exam Question Everyone Fears** — 0:20 · built from scenes 1 and 3

- **Hook (first 1.5s):** Exam paper: "Print the following pattern"
- **Script:** "Print the following pattern." Every C exam has it. Here's the secret: don't look at the whole triangle. Make a row table. Row 1, one star. Row 2, two stars. Row i, i stars. Now the code writes itself. Full episode on Koding Konkani.
- **On-screen text:** EXAM QUESTION / MAKE A ROW TABLE / ROW i = i STARS
- **Caption + hashtags:** Free marks in every C exam. #cprogramming #learntocode #kodingkonkani #starpattern #exampreparation

**S2 · Star Triangle in 30 Seconds** — 0:30 · built from scene 4

- **Hook (first 1.5s):** Stars dropping into a triangle
- **Script:** Outer loop: for i from 1 to 5, one round per row. Inner loop: for j from 1 to i, because row i has i stars. Print star space. After the inner loop, a newline. That's the triangle. Change the inner limit from a fixed number to i, and a rectangle becomes a triangle.
- **On-screen text:** for i: ROWS / for j <= i: STARS
- **Caption + hashtags:** One change: rectangle to triangle. #cprogramming #learntocode #kodingkonkani #patternprinting #ctutorial

**S3 · I Wanted a Triangle and Got a Pyramid** — 0:30 · built from scene 8

- **Hook (first 1.5s):** Triangle collapsing into a pyramid
- **Script:** I wanted a triangle on the right. I got a pyramid in the middle. Why? Each star prints as star plus space, two characters wide. But I filled each gap with one space. Gaps half as wide, stars slide to the centre. Use two spaces, and the triangle snaps back to the right.
- **On-screen text:** WRONG SPACES / "\* " = 2 CHARS / USE "  "
- **Caption + hashtags:** The happiest accident in C. #cprogramming #learntocode #kodingkonkani #debugging #starpattern

**S4 · Pun: Knows Its Place** — 0:10 · built from scene 6

- **Hook (first 1.5s):** Xecxec dizzy with stars around his head
- **Script:** Why did the star pattern pass the exam? Because it knew its place, row by row.
- **On-screen text:** ROW BY ROW
- **Caption + hashtags:** Stars that study. #cprogramming #codingmemes #kodingkonkani #programmerhumor

**S5 · What Does This Print?** — 0:20 · built from scene 4

- **Hook (first 1.5s):** Code with `printf("%d ", j)` highlighted
- **Script:** Same triangle code, but instead of a star, we print j. What do you get? Row 1: 1. Row 2: 1 2. Row 3: 1 2 3. Up to 1 2 3 4 5. A number triangle, for free. Comment if you guessed it.
- **On-screen text:** PRINT j INSTEAD? / 1 / 1 2 / 1 2 3
- **Caption + hashtags:** Stars to numbers in one change. #cprogramming #learntocode #kodingkonkani #cquiz #patternprinting

## EP 32 — Pattern Printing 2: Pyramids and Number Patterns

**Module 4 · Loops · 7:00 · Butter + Dark blue · Prerequisite: EP 31**

**Learning goals:** build a centred pyramid using a row table with spaces = n − i and stars = 2i − 1; join a pyramid and an inverted pyramid into a diamond; print Floyd's triangle using a counter that lives outside both loops; check star counts by testing one row by hand.

### YouTube

- **Title:** Build a Star Pyramid in C (and a Diamond) | C EP 32
- **Description:** Pyramids look hard until you write their row table: n minus i spaces, then 2i minus 1 stars. We build a pyramid, turn it into a diamond, print Floyd's triangle, and fix the bug where the pyramid comes out lopsided. 0:00 Challenge answer and hook 0:25 The pyramid row table 1:30 Pyramid, line by line 3:00 Diamond 3:55 Floyd's triangle 5:00 Bug of the Day: space vs star count 6:20 Challenge
- **Tags:** c programming, pyramid pattern in c, diamond pattern in c, floyd's triangle in c, number pattern in c, star pattern, nested loops, c programming exam questions, learn c, koding konkani
- **Thumbnail:** big text "PYRAMID CRAB-STYLE"; a golden star pyramid on a beach with Xecxec on top waving a flag; formula "2i − 1" in a badge; Butter background, Dark blue blocks.

### Scene list

| # | Start | Length | Template | On screen | Animation & SFX |
| --- | --- | --- | --- | --- | --- |
| 1 | 0:00 | 0:20 | Terminal | EP 31 challenge output (upside-down right triangle); then Xecxec building a sandcastle pyramid at Calangute | Sand pours, castle rises; waves SFX |
| 2 | 0:20 | 0:05 | Title card | EP 32 · PATTERN PRINTING 2 | Butter card, claw-click |
| 3 | 0:25 | 1:05 | Concept slide | Row table for n = 5: row, spaces (4,3,2,1,0), stars (1,3,5,7,9); rules "spaces = n − i", "stars = 2i − 1" | Columns fill one by one; the odd-number sequence 1,3,5,7,9 pulses |
| 4 | 1:30 | 1:30 | Code explain | `pyr.c` with trackers `i`, `s`, `k` | Spaces as dotted boxes, stars in Tomato, row by row; counter shows "2\*i-1 = …" |
| 5 | 3:00 | 0:50 | Code explain | `diamond.c`: top half then bottom half | Pyramid builds, then a mirrored half drops below; shimmer SFX |
| 6 | 3:50 | 0:05 | Pun card | Pun | Xecxec in a pharaoh hat, rimshot |
| 7 | 3:55 | 1:05 | Code explain | `floyd.c` with trackers `i`, `j`, `num` | `num` tracker keeps rising across rows (never resets), numbers drop into place |
| 8 | 5:00 | 1:20 | Bug of the Day | Inner star limit `k <= i` gives a lopsided shape | Butter frame; row table check: row 3 needs 5 stars but gets 3 (Tomato); fixed to `2 * i - 1` (Mint) |
| 9 | 6:20 | 0:25 | Challenge | "Number pyramid" target picture: 1 / 121 / 12321 / 1234321 / 123454321 | Digits pop in, timer ring |
| 10 | 6:45 | 0:15 | Outro | Next: EP 33, Number games mini project | Xecxec waves, end card |

### Narration script

**\[1 · Recap and hook\]** Last challenge: the upside-down right-aligned triangle. Take the right-aligned triangle and make the outer loop count down: four stars, then three, two, one, all touching the right edge. Today, Xecxec is building a sandcastle at Calangute. Not a triangle. A proper pyramid. Wide at the bottom, pointed on top, perfectly centred.

**\[2 · Title\]** Episode thirty-two. Pattern printing, part two.

**\[3 · Row table\]** Same trick as last time: the row table. Let n be 5. Row 1 has 4 spaces and 1 star. Row 2 has 3 spaces and 3 stars. Row 3: 2 spaces, 5 stars. Row 4: 1 space, 7 stars. Row 5: no spaces, 9 stars. The spaces column is easy: n minus i, like last episode. The stars column goes 1, 3, 5, 7, 9. Those are odd numbers. And the formula for the i-th odd number is 2 times i, minus 1. Check row 3: 2 times 3 is 6, minus 1 is 5. Yes. Two rules: spaces equal n minus i, stars equal 2i minus 1. This time we print stars with no space after them, so one space fills one star's width.

**\[4 · Pyramid\]** \[HL 4\] n equals 5. \[HL 6\] Outer loop: i from 1 to n. \[TRACK i=1\] \[HL 7\] First inner loop: s from 1 to n minus i. That's 4 on row 1. \[HL 8\] Each time, print one space. \[HL 10\] Second inner loop: k from 1 to 2 times i minus 1. On row 1 that's 1. \[HL 11\] Print one star. \[HL 13\] Then newline. Row 1: four spaces, one star. \[TRACK i=2\] Row 2: 3 spaces, and 2 times 2 minus 1, 3 stars. \[TRACK i=3\] Row 3: 2 spaces, 5 stars. \[TRACK i=5\] Row 5: zero spaces, the s loop doesn't run at all, then 9 stars. And we have a pyramid. Notice the stars grow by 2 each row, one on each side, while the spaces shrink by 1. That's what keeps it centred.

**\[5 · Diamond\]** Want a diamond? It's a pyramid with an upside-down pyramid under it. With n equals 4, the top half is our pyramid code. \[HL 11\] The bottom half uses the same two inner loops, but the outer loop counts down: i from n minus 1 down to 1. Why n minus 1? Because the widest row, 7 stars, is already printed by the top half. We don't want it twice. Top half: 1, 3, 5, 7 stars. Bottom half: 5, 3, 1. A diamond.

**\[6 · Pun\]** Why do pyramids make great programmers? They always have a solid base.

**\[7 · Floyd's triangle\]** One more famous exam pattern: Floyd's triangle. \[HL 5\] int num equals 1, declared outside both loops. \[TRACK num=1\] \[HL 7\] Outer loop: i from 1 to n, with n equal to 4. \[HL 8\] Inner loop: j from 1 to i, the same as our left triangle. \[HL 9\] printf percent 3 d, num. The 3 makes each number take 3 spaces, so columns line up. \[HL 10\] num plus plus. Row 1: 1. \[TRACK num=2\] Row 2: 2, 3. \[TRACK num=4\] Row 3: 4, 5, 6. Row 4: 7, 8, 9, 10. \[TRACK num=11\] The key is where num lives. Because it's outside both loops, it never resets. It just keeps counting across rows. If you declared it inside the outer loop, every row would restart at 1.

**\[8 · Bug of the Day\]** Today's bug: space versus star count. A student writes the pyramid but uses k less than or equal to i for the stars, copying from the triangle. Compile: no error. Run it. The output is a right-aligned triangle: 1 star, 2 stars, 3 stars, all pushed to the right. Not a pyramid. Let's check with the row table. Row 3 should have 5 stars. The code gives 3. The spaces shrink by 1 each row, so the stars must grow by 2 to stay centred, but they only grow by 1. The fix: k less than or equal to 2 times i minus 1. The lesson: before you run, test one row of your loop limits against your row table.

**\[9 · Challenge\]** Your challenge: the number pyramid. With n equals 5: 1 on top, then 1 2 1, then 1 2 3 2 1, up to 1 2 3 4 5 4 3 2 1, all centred. Hint: on each row, after the spaces, count up from 1 to i, then count down from i minus 1 to 1.

**\[10 · Outro\]** Next episode: our first mini project. Is 97 prime? Let's ask C. Keep coding, says Xecxec!

### Code shown

```c
#include <stdio.h>

int main(void) {
    int n = 5;

    for (int i = 1; i <= n; i++) {
        for (int s = 1; s <= n - i; s++) {
            printf(" ");
        }
        for (int k = 1; k <= 2 * i - 1; k++) {
            printf("*");
        }
        printf("\n");
    }
    return 0;
}
```

```text
    *
   ***
  *****
 *******
*********
```

```c
#include <stdio.h>

int main(void) {
    int n = 4;

    for (int i = 1; i <= n; i++) {
        for (int s = 1; s <= n - i; s++) printf(" ");
        for (int k = 1; k <= 2 * i - 1; k++) printf("*");
        printf("\n");
    }
    for (int i = n - 1; i >= 1; i--) {
        for (int s = 1; s <= n - i; s++) printf(" ");
        for (int k = 1; k <= 2 * i - 1; k++) printf("*");
        printf("\n");
    }
    return 0;
}
```

```text
   *
  ***
 *****
*******
 *****
  ***
   *
```

```c
#include <stdio.h>

int main(void) {
    int n = 4;
    int num = 1;

    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= i; j++) {
            printf("%3d", num);
            num++;
        }
        printf("\n");
    }
    return 0;
}
```

```text
  1
  2  3
  4  5  6
  7  8  9 10
```

### Bug of the Day

```c
        for (int k = 1; k <= i; k++) {
            printf("*");
        }
```

No compiler error. Wrong output (a right-aligned triangle, not a pyramid):

```text
    *
   **
  ***
 ****
*****
```

Fixed:

```c
        for (int k = 1; k <= 2 * i - 1; k++) {
            printf("*");
        }
```

The spaces shrink by 1 per row, so the stars must grow by 2 per row (1, 3, 5 … = 2i − 1) to stay centred.

### Pun & challenge

- **Pun:** Why do pyramids make great programmers? They always have a solid base.
- **Challenge:** With n = 5, print the number pyramid: `1`, `121`, `12321`, `1234321`, `123454321`, centred.
- **Challenge answer:**

```c
int n = 5;
for (int i = 1; i <= n; i++) {
    for (int s = 1; s <= n - i; s++) {
        printf(" ");
    }
    for (int k = 1; k <= i; k++) {
        printf("%d", k);
    }
    for (int k = i - 1; k >= 1; k--) {
        printf("%d", k);
    }
    printf("\n");
}
```

```text
    1
   121
  12321
 1234321
123454321
```

### Shorts for EP 32

**S1 · Xecxec Builds a Pyramid** — 0:20 · built from scenes 1 and 4

- **Hook (first 1.5s):** Sand pyramid rising on Calangute beach
- **Script:** Xecxec wants a pyramid. Not a triangle, a real pyramid, centred and pointy. In C it takes two inner loops: one for spaces, one for stars. And one tiny formula: 2i minus 1. Full episode on Koding Konkani.
- **On-screen text:** PYRAMID IN C / SPACES + STARS / 2i - 1
- **Caption + hashtags:** Sandcastle, but make it C. #cprogramming #learntocode #kodingkonkani #pyramidpattern #goa

**S2 · The Pyramid Formula in 30 Seconds** — 0:30 · built from scene 3

- **Hook (first 1.5s):** Row table appearing beside the pyramid
- **Script:** Every pyramid follows two rules. Spaces on row i: n minus i. Stars on row i: 2i minus 1. For n equals 5, that's 4 spaces and 1 star, then 3 and 3, then 2 and 5, then 1 and 7, then 0 and 9. Write those two rules as loop limits, and you're done.
- **On-screen text:** SPACES = n - i / STARS = 2i - 1
- **Caption + hashtags:** Two rules, every pyramid. #cprogramming #learntocode #kodingkonkani #starpattern #ctutorial

**S3 · My Pyramid Came Out Lopsided** — 0:25 · built from scene 8

- **Hook (first 1.5s):** A leaning half-pyramid in Tomato
- **Script:** This should be a pyramid. It's a lopsided triangle. The stars loop says k up to i, so stars grow by 1. But spaces shrink by 1, so stars must grow by 2 to stay centred. Change it to 2i minus 1. Fixed.
- **On-screen text:** LOPSIDED? / k <= i / k <= 2\*i - 1
- **Caption + hashtags:** Check your row table first. #cprogramming #learntocode #kodingkonkani #debugging #patternprinting

**S4 · Pun: Solid Base** — 0:10 · built from scene 6

- **Hook (first 1.5s):** Xecxec in a pharaoh hat
- **Script:** Why do pyramids make great programmers? They always have a solid base.
- **On-screen text:** SOLID BASE
- **Caption + hashtags:** Built different. #cprogramming #codingmemes #kodingkonkani #programmerhumor

**S5 · How Many Stars on Row 6?** — 0:15 · built from scene 3

- **Hook (first 1.5s):** Pyramid with a blank row 6
- **Script:** Quick quiz. In a pyramid, row i has 2i minus 1 stars. How many on row 6? 2 times 6 is 12, minus 1. Eleven stars.
- **On-screen text:** ROW 6 = ? / 2(6) - 1 = 11
- **Caption + hashtags:** Pyramid maths in 10 seconds. #cprogramming #learntocode #kodingkonkani #cquiz #starpattern

## EP 33 — Mini Project: Number Games

**Module 4 · Loops · 7:30 · Butter + Dark blue · Prerequisite: EP 32**

**Learning goals:** test whether a number is prime using a loop with an early `break`; compute a factorial with a `for` loop and `long long`; reverse a number's digits with `% 10` and `/ 10` in a `while` loop; choose the correct loop bound so a test does not defeat itself.

### YouTube

- **Title:** Is 97 Prime? Ask C! Loops Mini Project | C Programming EP 33
- **Description:** Module 4 ends with a mini project: one program, three number games. Prime check, factorial and reverse digits, each built from the loops you've learned. Plus the loop-bound bug that makes C say 97 is not prime. 0:00 Challenge answer and hook 0:30 The plan 1:00 Game 1: prime check 2:45 Game 2: factorial 3:45 Game 3: reverse the digits 5:15 Run all three 5:45 Bug of the Day: wrong loop bound 6:55 Challenge
- **Tags:** c programming, prime number program in c, factorial program in c, reverse a number in c, loops mini project, c programming exam questions, while loop, for loop, learn c, koding konkani
- **Thumbnail:** big text "IS 97 PRIME?"; giant "97" with a question mark; Xecxec holding a magnifying glass over it; Butter background, Dark blue blocks.

### Scene list

| # | Start | Length | Template | On screen | Animation & SFX |
| --- | --- | --- | --- | --- | --- |
| 1 | 0:00 | 0:25 | Terminal | EP 32 challenge: number pyramid output; then "Is 97 prime?" in huge digits | Digits pop in; quiz-show sting |
| 2 | 0:25 | 0:05 | Title card | EP 33 · MINI PROJECT: NUMBER GAMES | Butter card, claw-click |
| 3 | 0:30 | 0:30 | Concept slide | Plan: read n → Game 1 prime → Game 2 factorial → Game 3 reverse | Three game tokens slide onto a board |
| 4 | 1:00 | 1:45 | Code explain | `games.c` lines 1–16 (prime check), trackers `n`, `d`, `isPrime` | Divisors 2, 3 tested against 12; `d * d <= n` shown as a square growing; break arrow |
| 5 | 2:45 | 0:05 | Pun card | Pun | Xecxec counting on his claws, rimshot |
| 6 | 2:50 | 0:55 | Code explain | `games.c` lines 18–23 (factorial), tracker `fact` | `fact` tracker climbs 1, 2, 6, 24 … 479001600; `long long` badge |
| 7 | 3:45 | 1:30 | Code explain | `games.c` lines 25–33 (reverse), trackers `temp`, `digit`, `reversed` | Digits peel off the right end of 1234 and stack onto `reversed` |
| 8 | 5:15 | 0:30 | Terminal | Run `games.c` with 12 and 17 | Typing SFX, outputs appear |
| 9 | 5:45 | 1:10 | Bug of the Day | `prime97.c` with `d <= n` says 97 is not prime | Butter frame; divisor counter runs all the way to 97 and hits 97 % 97 == 0 (Tomato); fixed bound (Mint) |
| 10 | 6:55 | 0:20 | Challenge | "Find all 3-digit Armstrong numbers" with 153 = 1³ + 5³ + 3³ | Cubes pop up, timer ring |
| 11 | 7:15 | 0:15 | Outro | Module 4 complete badge; Next: EP 34 | Badge stamp, Xecxec dance, end card |

### Narration script

**\[1 · Recap and hook\]** Last challenge: the number pyramid. Spaces first, then count up from 1 to i, then count down from i minus 1 to 1. You get 1, then 121, then 12321, up to 123454321. Now, a question for you. Is 97 a prime number? You could start dividing by hand. Or you could write a program once and ask it any number you like. Today, we build three number games in one program, using only loops you already know.

**\[2 · Title\]** Episode thirty-three. Mini project: number games.

**\[3 · Plan\]** Here's the plan. Read one number, n. Game one: is n prime? Game two: what is n factorial? Game three: what is n with its digits reversed? Each game is one loop. Factorial grows very fast, so for this program we accept numbers from 1 to 20.

**\[4 · Prime check\]** \[HL 5\] \[HL 6\] We ask for a number and read it into n. Say the user types 12. \[TRACK n=12\] \[HL 9\] int isPrime equals, in brackets, n greater than or equal to 2. A comparison gives 1 for true and 0 for false. 0 and 1 are not prime, so they start as 0. 12 is at least 2, so isPrime starts at 1. We assume it's prime until we find a divisor. \[TRACK isPrime=1\] \[HL 10\] for d from 2, while d times d is less than or equal to n, d plus plus. Why d times d? If 12 has a divisor bigger than its square root, it must also have a partner divisor smaller than its square root. Like 12 is 2 times 6. Checking up to the square root is enough. \[TRACK d=2\] \[HL 11\] if n mod d equals 0. 12 mod 2 is 0. So 2 divides 12. \[HL 12\] isPrime becomes 0. \[TRACK isPrime=0\] \[HL 13\] break. One divisor is enough proof, no need to check more. \[HL 16\] Print "12 is not prime". Here we use the ternary operator from Episode 19: if isPrime is true, print "prime", otherwise "not prime". For 97, d goes 2, 3, up to 9, because 10 times 10 is 100, which is more than 97. None of them divide 97, so isPrime stays 1. 97 is prime. Only 8 checks instead of 95.

**\[5 · Pun\]** Why was 7 so confident in maths class? Because it was in its prime.

**\[6 · Factorial\]** Game two. Factorial of n means 1 times 2 times 3, all the way up to n. \[HL 19\] long long fact equals 1. Why long long? Factorials explode. 13 factorial is already more than six billion, too big for an int, which only goes up to about 2.1 billion. A long long can hold numbers up to about 9 quintillion, enough for 20 factorial. And we start at 1, not 0, because we're multiplying. Zero times anything is zero. \[TRACK fact=1\] \[HL 20\] for i from 2 to n. \[HL 21\] fact equals fact times i. For 12: 2, 6, 24, 120, 720, and on until 479001600. \[TRACK fact=479001600\] \[HL 23\] We print it with percent l l d, the format for long long.

**\[7 · Reverse\]** Game three, the cleverest one. Reverse the digits. We'll trace it with 1234 to make it clear. \[HL 26\] int temp equals n. We work on a copy so n stays safe. \[TRACK temp=1234\] \[HL 27\] reversed starts at 0. \[TRACK reversed=0\] \[HL 28\] while temp is greater than 0. \[HL 29\] digit equals temp mod 10. Mod 10 gives the last digit. 1234 mod 10 is 4. \[TRACK digit=4\] \[HL 30\] reversed equals reversed times 10, plus digit. 0 times 10 plus 4 is 4. \[TRACK reversed=4\] \[HL 31\] temp equals temp divided by 10. Integer division drops the last digit: 1234 becomes 123. \[TRACK temp=123\] Round two: digit is 3, reversed is 4 times 10 plus 3, 43. temp is 12. \[TRACK reversed=43 temp=12\] Round three: digit 2, reversed 432, temp 1. \[TRACK reversed=432 temp=1\] Round four: digit 1, reversed 4321, temp 0. \[TRACK reversed=4321 temp=0\] Now temp is not greater than 0, so we stop. \[HL 33\] Print "Reversed: 4321". Mod 10 takes the last digit off. Times 10 makes room for it on the other side. It's like moving people from the back of one bus queue to the front of another.

**\[8 · Terminal\]** Let's run it. Type 12: 12 is not prime, 12 factorial is 479001600, reversed is 21. Run again with 17: 17 is prime, 17 factorial is 355687428096000, reversed is 71.

**\[9 · Bug of the Day\]** Today's bug: wrong loop bound. A student writes the prime check with for d from 2, d less than or equal to n. Compile: no error. Run with 97. Output: "97 is not prime". But 97 is prime! What went wrong? The loop goes all the way up to d equals 97. And 97 mod 97 is 0. Every number divides itself, so every number fails the test. The loop bound was one step too far. The fix: stop before n, with d less than n, or better, use d times d less than or equal to n, which is also much faster. Always ask: does my loop test values it should not?

**\[10 · Challenge\]** Your challenge: find all three-digit Armstrong numbers. An Armstrong number equals the sum of the cubes of its digits. For example 153: 1 cubed is 1, 5 cubed is 125, 3 cubed is 27, and 1 plus 125 plus 27 is 153. Loop from 100 to 999, take the digits apart with mod 10 and divide by 10, and print each number that matches. There are exactly four. Can you find them all?

**\[11 · Outro\]** That's Module 4 complete! You can now repeat anything, skip, stop, nest and draw with loops. Next episode starts Module 5: functions, where we teach C to remember whole recipes. Keep coding, says Xecxec!

### Code shown

```c
#include <stdio.h>

int main(void) {
    int n;
    printf("Enter a number (1-20): ");
    scanf("%d", &n);

    /* Game 1: is it prime? */
    int isPrime = (n >= 2);
    for (int d = 2; d * d <= n; d++) {
        if (n % d == 0) {
            isPrime = 0;
            break;
        }
    }
    printf("%d is %s\n", n, isPrime ? "prime" : "not prime");

    /* Game 2: factorial */
    long long fact = 1;
    for (int i = 2; i <= n; i++) {
        fact = fact * i;
    }
    printf("%d! = %lld\n", n, fact);

    /* Game 3: reverse the digits */
    int temp = n;
    int reversed = 0;
    while (temp > 0) {
        int digit = temp % 10;
        reversed = reversed * 10 + digit;
        temp = temp / 10;
    }
    printf("Reversed: %d\n", reversed);

    return 0;
}
```

```text
Enter a number (1-20): 12
12 is not prime
12! = 479001600
Reversed: 21
```

```text
Enter a number (1-20): 17
17 is prime
17! = 355687428096000
Reversed: 71
```

Note on screen: the reverse trace with 1234 is a whiteboard demo of lines 26–33; the program itself accepts 1–20 so the factorial fits in `long long`.

### Bug of the Day

```c
#include <stdio.h>

int main(void) {
    int n = 97;
    int isPrime = (n >= 2);

    for (int d = 2; d <= n; d++) {
        if (n % d == 0) {
            isPrime = 0;
            break;
        }
    }
    printf("%d is %s\n", n, isPrime ? "prime" : "not prime");
    return 0;
}
```

No compiler error. Wrong output:

```text
97 is not prime
```

Fixed:

```c
    for (int d = 2; d * d <= n; d++) {
```

```text
97 is prime
```

With `d <= n` the loop finally tests `d = 97`, and every number divides itself, so every number looks "not prime".

### Pun & challenge

- **Pun:** Why was 7 so confident in maths class? Because it was in its prime.
- **Challenge:** Print all three-digit Armstrong numbers (a number equal to the sum of the cubes of its digits, like 153).
- **Challenge answer:** `153 370 371 407`

```c
for (int n = 100; n <= 999; n++) {
    int temp = n;
    int sum = 0;
    while (temp > 0) {
        int d = temp % 10;
        sum = sum + d * d * d;
        temp = temp / 10;
    }
    if (sum == n) {
        printf("%d ", n);
    }
}
printf("\n");
```

### Shorts for EP 33

**S1 · Is 97 Prime? Ask C** — 0:20 · built from scenes 1 and 4

- **Hook (first 1.5s):** Giant "97?" with Xecxec and a magnifying glass
- **Script:** Is 97 prime? You could divide by hand. Or write a loop: try every divisor from 2 up to the square root. If nothing divides it, it's prime. C checks 97 in eight steps. Answer: prime. Full episode on Koding Konkani.
- **On-screen text:** IS 97 PRIME? / 8 CHECKS / YES!
- **Caption + hashtags:** Let the loop do the maths. #cprogramming #learntocode #kodingkonkani #primenumbers #codingforbeginners

**S2 · Reverse a Number in 30 Seconds** — 0:30 · built from scene 7

- **Hook (first 1.5s):** 1234 turning into 4321
- **Script:** Reverse 1234 with two tricks. Mod 10 gives the last digit: 4. Divide by 10 removes it: 123. Build the answer with reversed times 10 plus digit. 4, then 43, then 432, then 4321. Loop while the number is more than zero. Done.
- **On-screen text:** % 10 = LAST DIGIT / / 10 = DROP IT / 1234 to 4321
- **Caption + hashtags:** The classic reverse-digits trick. #cprogramming #learntocode #kodingkonkani #whileloop #ctutorial

**S3 · C Says 97 Is Not Prime?!** — 0:25 · built from scene 9

- **Hook (first 1.5s):** Terminal: "97 is not prime" in Tomato
- **Script:** My program says 97 is not prime. That's wrong. The loop runs d up to n, so it finally tests 97 divided by 97, which has no remainder. Every number divides itself. Stop before n, or use d times d less than or equal to n.
- **On-screen text:** 97 NOT PRIME?! / d <= n / d \* d <= n
- **Caption + hashtags:** One wrong bound, every answer wrong. #cprogramming #learntocode #kodingkonkani #debugging #primenumbers

**S4 · Pun: In Its Prime** — 0:10 · built from scene 5

- **Hook (first 1.5s):** Number 7 in sunglasses
- **Script:** Why was 7 so confident in maths class? Because it was in its prime.
- **On-screen text:** IN ITS PRIME
- **Caption + hashtags:** 7 is thriving. #cprogramming #codingmemes #kodingkonkani #mathsjokes

**S5 · Is 153 Special?** — 0:20 · built from scene 10

- **Hook (first 1.5s):** "153" with cubes floating around
- **Script:** 1 cubed plus 5 cubed plus 3 cubed. 1 plus 125 plus 27. That's 153, the number itself. It's called an Armstrong number. There are exactly four with three digits. Can you write a loop to find the other three? Comment your answer.
- **On-screen text:** 1³ + 5³ + 3³ = 153 / FIND THE OTHER 3
- **Caption + hashtags:** A number that equals its own digits. #cprogramming #learntocode #kodingkonkani #cquiz #armstrongnumber
