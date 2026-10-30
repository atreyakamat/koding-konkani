# Module 3 — Decisions

Episodes 20–25 · Mint + Dark blue

## EP 20 — if and else

**Module 3 · Decisions · 5:50 · Mint + Dark blue · Prerequisite: EP 19**

**Learning goals:** write an `if` with a condition in brackets and a body in braces; add an `else` for the other path; predict which branch runs for a given input; spot the stray semicolon after `if (...)`.

### YouTube

- **Title:** if and else: Teach Your Code to Decide | C Programming EP 20
- **Description:** Until now every program ran every line, top to bottom. Today your code learns to choose: if it rains, take the umbrella, else take the sunglasses. We build a pass/fail checker line by line and meet the semicolon that silently breaks every if. Chapters: 0:00 Rain or shine · 0:25 What if does · 1:15 Code line by line · 2:45 Running it · 3:25 Three rules · 4:05 Bug of the Day · 5:00 Challenge
- **Tags:** c programming, if else in c, c if statement, decision making in c, learn c, c for beginners, conditional statements, c tutorial english, koding konkani, gcc
- **Thumbnail:** big text "IF... ELSE?"; a road splitting in two with a green PASS sign and a red FAIL sign; Xecxec standing at the fork holding an umbrella in one claw and sunglasses in the other; mint background, dark blue text blocks

### Scene list

| # | Start | Length | Template | On screen | Animation & SFX |
| --- | --- | --- | --- | --- | --- |
| 1 | 0:00 | 0:20 | Concept slide | Rain cloud over Panaji; Xecxec at his door choosing umbrella or sunglasses | Cloud slides in, rain drops; claw-click as he grabs the umbrella |
| 2 | 0:20 | 0:05 | Title card | EP 20 · IF AND ELSE | Title slam, whoosh |
| 3 | 0:25 | 0:50 | Concept slide | Flowchart: diamond "marks >= 35?" with YES and NO arrows to two boxes | Diamond pops, arrows draw in, ding on YES, buzz on NO |
| 4 | 1:15 | 1:30 | Code explain | ep20.c, 17 lines; variable tracker for marks | Line highlights in butter; tracker box updates; key-tap SFX |
| 5 | 2:45 | 0:35 | Terminal | Three runs: 72, 20, 35 | Typing SFX, output lines fade in; Xecxec cheers on 35 |
| 6 | 3:20 | 0:05 | Pun card | Pun line | Drum hit, Xecxec claw-click laugh |
| 7 | 3:25 | 0:40 | Concept slide | Three rules: braces, non-zero is true, else is optional | Each rule card stamps in |
| 8 | 4:05 | 0:55 | Bug of the Day | if (marks >= 35); with marks = 20 still printing Pass! | Red flash on the semicolon, error buzz, fix swoosh |
| 9 | 5:00 | 0:30 | Challenge | Two-subject pass/fail checker | Timer ring, Xecxec points at the screen |
| 10 | 5:30 | 0:20 | Outro | Next: EP 21 else-if ladders; sign-off | Module tiles, claw-click, music out |

### Narration script

**\[1 · Rain or shine\]** Morning in Panaji. Dark clouds over the Mandovi. Xecxec stands at his door with an umbrella in one claw and sunglasses in the other. If it rains, he takes the umbrella. Else, the sunglasses. You make this kind of choice a hundred times a day. Today, your C program learns to make it too.

**\[2 · Title\]** Episode 20. if and else.

**\[3 · What if does\]** Every program we wrote so far ran every line, from top to bottom, like a bus that stops at every stop. An if statement lets the program skip stops. Here is the picture. We have a question in a diamond: are the marks 35 or more? That question is a condition, and you already know conditions from EP 16. It is either true or false. If it is true, we follow the YES arrow and print Pass. If it is false, we follow the NO arrow and print Fail. Only one arrow is followed. Never both. After that, both roads join again and the program carries on.

**\[4 · Code line by line\]** Let's turn that diamond into C. \[HL 4\] Line 4 makes a box called marks. \[HL 6\] Line 6 asks the user to type marks. \[HL 7\] Line 7 reads them with scanf, with the ampersand, just like EP 12. Say the user types 72. \[TRACK marks=72\] Now the important part. \[HL 9\] Line 9: the word if, then the condition inside round brackets: marks greater than or equal to 35. Is 72 greater than or equal to 35? Yes, true. So C runs the block inside the curly braces. \[HL 10\] Line 10 prints "Pass! Party at Baga." \[HL 11\] Line 11 has the closing brace, then the word else, then a new opening brace. Else means: run this only when the condition was false. The condition was true, so C jumps over the whole else block, lines 11 to 13. \[HL 15\] Line 15 runs no matter what, because it is outside both blocks. It prints "Result checked." Now run it again with 20. \[TRACK marks=20\] \[HL 9\] Is 20 greater than or equal to 35? No. False. So C skips line 10 completely, \[HL 12\] and runs the else block, line 12: "Fail. Try again, crab." \[HL 15\] And again line 15 runs. One question, two roads, one meeting point.

**\[5 · Running it\]** Let's compile and run. gcc ep20.c -o ep20, then dot slash ep20. Type 72: Pass. Run again, type 20: Fail. Now the tricky one: 35. Is 35 greater than or equal to 35? Yes, equal counts. Pass. If we had written only greater than, 35 would fail, and one very angry student would be at your door. Always check the edge value.

**\[6 · Pun\]** I told my code a joke about if statements. It only laughed on one condition.

**\[7 · Three rules\]** Three rules to remember. Rule one: put the body in curly braces, even if it is one line. C allows you to skip them for a single line, but braces keep you safe when you add a second line later. Rule two: in C, any value that is not zero counts as true, and zero counts as false. So if (5) always runs, and if (0) never runs. Rule three: else is optional. An if alone is fine. If the condition is false, the program just skips the block and moves on. But an else can never stand alone. It must follow an if.

**\[8 · Bug of the Day\]** Today's bug is one tiny dot with a tail: a semicolon. Look at this code. marks is 20. The if says marks greater than or equal to 35, and then, a semicolon. We run it. It prints Pass! With 20 marks! Why? In C, a semicolon on its own is an empty statement. So the if controls that empty statement and nothing else. The block in braces underneath is just a normal block, and it runs every time. Plain gcc gives no error at all. Compile with -Wall and GCC warns: suggest braces around empty body in an if statement. And if you add an else, it becomes a hard error: else without a previous if. The fix: delete the semicolon. Never put a semicolon right after the closing bracket of an if.

**\[9 · Challenge\]** Your challenge. Read marks for two subjects, maths and English. Print PASS only if both are 35 or more. Otherwise print FAIL. Hint: you need the double ampersand from EP 16. Pause the video, open VS Code, and type it yourself. The answer is pinned in the comments.

**\[10 · Outro\]** Next episode: what if there are more than two roads? Grades A, B, C, D, and something worse. We climb the else-if ladder in EP 21. Keep coding, says Xecxec!

### Code shown

```c
#include <stdio.h>

int main(void) {
    int marks;

    printf("Enter your marks: ");
    scanf("%d", &marks);

    if (marks >= 35) {
        printf("Pass! Party at Baga.\n");
    } else {
        printf("Fail. Try again, crab.\n");
    }

    printf("Result checked.\n");
    return 0;
}
```

**Expected output** (three runs; user input shown after the prompt):

```text
Enter your marks: 72
Pass! Party at Baga.
Result checked.

Enter your marks: 20
Fail. Try again, crab.
Result checked.

Enter your marks: 35
Pass! Party at Baga.
Result checked.
```

### Bug of the Day

Wrong code:

```c
#include <stdio.h>

int main(void) {
    int marks = 20;

    if (marks >= 35);
    {
        printf("Pass!\n");
    }

    return 0;
}
```

With plain `gcc` there is no error, and the wrong output is:

```text
Pass!
```

With `gcc -Wall` (GCC 13):

```text
ep20bug.c:6:21: warning: suggest braces around empty body in an 'if' statement [-Wempty-body]
    6 |     if (marks >= 35);
      |                     ^
ep20bug.c:6:5: warning: this 'if' clause does not guard... [-Wmisleading-indentation]
```

If an `else` follows the block, it becomes a hard error: `error: 'else' without a previous 'if'`.

Fixed code:

```c
#include <stdio.h>

int main(void) {
    int marks = 20;

    if (marks >= 35) {
        printf("Pass!\n");
    }

    return 0;
}
```

Why: a lone `;` is an empty statement, so the `if` guards nothing and the braced block below it always runs.

### Pun & challenge

- **Pun:** I told my code a joke about if statements. It only laughed on one condition.
- **Challenge:** Read marks for maths and English. Print PASS only if both are 35 or more; otherwise print FAIL.
- **Challenge answer:**

```c
int maths, english;
scanf("%d %d", &maths, &english);
if (maths >= 35 && english >= 35) {
    printf("PASS\n");
} else {
    printf("FAIL\n");
}
```

### Shorts for EP 20

**S1 · Your code can finally choose** — 0:25 · built from scenes 1–3

- **Hook (first 1.5s):** Xecxec freezes between an umbrella and sunglasses: "Rain or shine?"
- **Script:** Every program you wrote so far runs every single line. Like a bus that stops at every stop. Today that changes. With one word, if, your program asks a question. Are the marks 35 or more? True, it prints Pass. False, it prints Fail. Only one road is taken, never both. Full episode on Koding Konkani.
- **On-screen text:** YOUR CODE CAN CHOOSE
- **Caption + hashtags:** One word turns your program into a decision maker. #cprogramming #learntocode #kodingkonkani #ifelse #codingforbeginners

**S2 · if/else in 30 seconds** — 0:30 · built from scene 4

- **Hook (first 1.5s):** Code line 9 glows: "if (marks >= 35)"
- **Script:** if and else in 30 seconds. Write if, then a condition in round brackets. If it is true, C runs the block in curly braces. If it is false, C jumps to else and runs that block instead. Code after both blocks runs every time. Type 72: Pass. Type 20: Fail. Type 35? Greater than or equal, so Pass. Always test the edge value.
- **On-screen text:** TRUE = IF BLOCK · FALSE = ELSE BLOCK
- **Caption + hashtags:** The whole if/else idea, line by line. #cprogramming #learntocode #kodingkonkani #ctutorial #programming

**S3 · The semicolon that lies** — 0:35 · built from scene 8

- **Hook (first 1.5s):** Terminal shows "Pass!" next to "marks = 20". Xecxec's jaw drops.
- **Script:** 20 marks. The program says Pass. What? Look closely. There is a semicolon right after the if. In C, a lone semicolon is an empty statement. So the if controls nothing, and the block below runs every time. Plain gcc does not even complain. Compile with -Wall and it warns you. Fix: delete that semicolon. Always compile with -Wall.
- **On-screen text:** if (...); IS A TRAP
- **Caption + hashtags:** One semicolon, zero errors, totally wrong output. #cprogramming #debugging #kodingkonkani #learntocode #codinglife

**S4 · One condition** — 0:12 · built from scene 6

- **Hook (first 1.5s):** Xecxec holds up a card: "Joke incoming"
- **Script:** I told my code a joke about if statements. It only laughed on one condition.
- **On-screen text:** IT ONLY LAUGHED ON ONE CONDITION
- **Caption + hashtags:** Tag the friend who only laughs on conditions. #programmerhumor #cprogramming #kodingkonkani #codingjokes

**S5 · What does it print?** — 0:25 · built from scenes 7 and 9

- **Hook (first 1.5s):** "if (0)" on screen with a big question mark
- **Script:** Quick quiz. int x = 0. if (x) print yes, else print no. What prints? Think. Three, two, one. It prints no. In C, zero is false and any other number is true. Now your challenge: read two marks and print PASS only if both are 35 or more. Answer in the comments.
- **On-screen text:** if (0) → ???
- **Caption + hashtags:** Zero is false. Everything else is true. Did you get it? #cprogramming #codingquiz #kodingkonkani #learntocode #ifelse

## EP 21 — else-if ladders

**Module 3 · Decisions · 6:05 · Mint + Dark blue · Prerequisite: EP 20**

**Learning goals:** chain several conditions with `else if`; explain that C stops at the first true condition; order checks from strictest to loosest; guard against invalid input as the first rung.

### YouTube

- **Title:** else if Ladder: Marks to Grades in C | C Programming EP 21
- **Description:** Two roads were not enough. Today we build an else-if ladder that turns marks into grades A, B, C, D and one very special grade for crabs. You will also see why the order of your checks can turn a topper into a D student. Chapters: 0:00 Too many roads · 0:25 The ladder · 1:10 Code line by line · 3:00 Running it · 3:40 First true wins · 4:15 Bug of the Day · 5:15 Challenge
- **Tags:** c programming, else if in c, else if ladder, grade program in c, decision making in c, learn c, c for beginners, c tutorial english, koding konkani, conditional statements
- **Thumbnail:** big text "95 = GRADE D?!"; a ladder with rungs labelled A, B, C, D, CRAB; Xecxec hanging off the bottom rung looking shocked; mint background, dark blue blocks

### Scene list

| # | Start | Length | Template | On screen | Animation & SFX |
| --- | --- | --- | --- | --- | --- |
| 1 | 0:00 | 0:20 | Concept slide | A report card with 5 grade boxes; one if/else only fits 2 | Card flips in, two boxes light, three stay grey; confused boing |
| 2 | 0:20 | 0:05 | Title card | EP 21 · ELSE-IF LADDERS | Title slam, whoosh |
| 3 | 0:25 | 0:45 | Concept slide | Ladder of diamonds: invalid? → >=90? → >=75? → >=60? → >=35? → else | Xecxec climbs down rung by rung, stops at the first green YES |
| 4 | 1:10 | 1:50 | Code explain | ep21.c, 24 lines; tracker for marks | Line highlights; each checked rung ticks red or green; key-tap SFX |
| 5 | 3:00 | 0:35 | Terminal | Runs: 95, 80, 60, 40, 12, 150 | Typing SFX, grade badge stamps next to each run |
| 6 | 3:35 | 0:05 | Pun card | Pun line | Drum hit, claw-click |
| 7 | 3:40 | 0:35 | Concept slide | "First true wins" with 80 sliding down the ladder | 80 stops at B; lower rungs grey out with a soft thud |
| 8 | 4:15 | 1:00 | Bug of the Day | Ladder upside down: 95 prints Grade D | Red flash, error buzz, rungs swap order with a swoosh |
| 9 | 5:15 | 0:30 | Challenge | Kadamba bus fare by distance | Timer ring, bus horn SFX |
| 10 | 5:45 | 0:20 | Outro | Next: EP 22 nested if; sign-off | Module tiles, claw-click, music out |

### Narration script

**\[1 · Too many roads\]** In EP 20, our program could choose between two roads: pass or fail. But your report card does not say just pass or fail. It says A, B, C, D, or something your parents will not like. That is five roads. One if and one else cannot hold five roads. We need a ladder.

**\[2 · Title\]** Episode 21. else-if ladders.

**\[3 · The ladder\]** Picture a ladder going down. On each rung there is a question. Xecxec starts at the top. Rung one: are the marks invalid, below 0 or above 100? If yes, stop and complain. If no, step down. Rung two: 90 or more? If yes, grade A, and stop. If no, step down. 75 or more? Grade B. 60 or more? Grade C. 35 or more? Grade D. And if he reaches the bottom without a single yes, he lands in the else: grade crab. The key word is stop. The moment one question says yes, Xecxec gets off the ladder. He never checks the rungs below.

**\[4 · Code line by line\]** Here is the ladder in C. \[HL 4\] Line 4 makes our box, marks. \[HL 6\] \[HL 7\] Lines 6 and 7 print a prompt and read the number with scanf. The user types 80. \[TRACK marks=80\] \[HL 9\] Line 9 is the top rung. It says: if marks is less than 0, or marks is greater than 100. That is the double pipe, the OR operator from EP 16. 80 is neither, so the condition is false. We skip line 10. \[HL 11\] Line 11 starts with else if. That means: only check this if everything above was false. Is 80 greater than or equal to 90? No. Skip line 12. \[HL 13\] Line 13: is 80 greater than or equal to 75? Yes! \[HL 14\] So line 14 runs and prints Grade B. And now, the important part. C jumps straight past the rest of the ladder, lines 15 to 21. It does not check 60. It does not check 35. \[HL 23\] It lands on line 23, return 0. Notice something clever. On line 13 we did not write marks greater than or equal to 75 AND marks less than 90. We did not need to. If marks were 90 or more, the line 11 rung would have caught them already. Reaching line 13 already means the marks are below 90. The ladder does that work for free. \[HL 19\] \[HL 20\] Finally, lines 19 and 20: the plain else at the bottom. No condition. It catches everything that fell through every rung: any mark from 0 to 34. Grade crab. Please study.

**\[5 · Running it\]** Let's run it six times. 95: Grade A. 80: Grade B. 60: exactly 60, greater than or equal, so Grade C. 40: Grade D. 12: Grade crab. And 150: the top rung catches it. Invalid marks. Always test the edges and at least one silly value. Users will type silly values. Trust me.

**\[6 · Pun\]** Why did the else-if ladder never get lonely? It always had a few conditions to fall back on.

**\[7 · First true wins\]** One rule to remember from today: first true wins. C checks the rungs from top to bottom, and only the first true condition runs. Even if three conditions below are also true, they are ignored. 80 is also greater than 60, and greater than 35. But B came first, so B wins. This is very different from writing five separate if statements. Five separate ifs would check all five, and 80 would print B, C and D. Three grades for one student. An else-if ladder gives exactly one answer.

**\[8 · Bug of the Day\]** Today's bug has no error message. No warning, even with -Wall. Look at this ladder. The first rung checks 35 or more. Then 60. Then 90. Our topper has 95 marks. We run it, and it prints Grade D. Ninety-five, Grade D! Why? First true wins. Is 95 greater than or equal to 35? Yes. So the first rung catches it, and the program never reaches the 90 rung. The 60 and 90 rungs can never run for anyone. The fix: put the strictest check at the top. 90 first, then 75, then 60, then 35. When your conditions overlap, order is everything.

**\[9 · Challenge\]** Your challenge. A Kadamba bus charges by distance. Up to 5 kilometres: 10 rupees. Up to 15: 20 rupees. Up to 30: 35 rupees. More than 30: 50 rupees. And if the distance is 0 or negative, print Invalid distance. Read the distance and print the fare using one else-if ladder. Pause, type, run. The answer is in the comments.

**\[10 · Outro\]** Next episode: what if one decision lives inside another? First check the ticket, then check the ID. That is nested if, in EP 22. Keep coding, says Xecxec!

### Code shown

```c
#include <stdio.h>

int main(void) {
    int marks;

    printf("Enter marks (0-100): ");
    scanf("%d", &marks);

    if (marks < 0 || marks > 100) {
        printf("Invalid marks!\n");
    } else if (marks >= 90) {
        printf("Grade A\n");
    } else if (marks >= 75) {
        printf("Grade B\n");
    } else if (marks >= 60) {
        printf("Grade C\n");
    } else if (marks >= 35) {
        printf("Grade D\n");
    } else {
        printf("Grade: CRAB (please study)\n");
    }

    return 0;
}
```

**Expected output** (six runs; user input shown after the prompt):

```text
Enter marks (0-100): 95
Grade A

Enter marks (0-100): 80
Grade B

Enter marks (0-100): 60
Grade C

Enter marks (0-100): 40
Grade D

Enter marks (0-100): 12
Grade: CRAB (please study)

Enter marks (0-100): 150
Invalid marks!
```

### Bug of the Day

Wrong code:

```c
#include <stdio.h>

int main(void) {
    int marks = 95;

    if (marks >= 35) {
        printf("Grade D\n");
    } else if (marks >= 60) {
        printf("Grade C\n");
    } else if (marks >= 90) {
        printf("Grade A\n");
    }

    return 0;
}
```

No error and no warning, even with `gcc -Wall -Wextra`. Wrong output:

```text
Grade D
```

Fixed code:

```c
#include <stdio.h>

int main(void) {
    int marks = 95;

    if (marks >= 90) {
        printf("Grade A\n");
    } else if (marks >= 60) {
        printf("Grade C\n");
    } else if (marks >= 35) {
        printf("Grade D\n");
    }

    return 0;
}
```

Why: an else-if ladder stops at the first true condition, so with overlapping checks the strictest one must come first.

### Pun & challenge

- **Pun:** Why did the else-if ladder never get lonely? It always had a few conditions to fall back on.
- **Challenge:** Kadamba bus fare: distance up to 5 km costs Rs 10, up to 15 km Rs 20, up to 30 km Rs 35, above 30 km Rs 50; 0 or less prints "Invalid distance". Use one else-if ladder.
- **Challenge answer:**

```c
int km;
scanf("%d", &km);
if (km <= 0) {
    printf("Invalid distance\n");
} else if (km <= 5) {
    printf("Fare: Rs 10\n");
} else if (km <= 15) {
    printf("Fare: Rs 20\n");
} else if (km <= 30) {
    printf("Fare: Rs 35\n");
} else {
    printf("Fare: Rs 50\n");
}
```

### Shorts for EP 21

**S1 · Five grades, one ladder** — 0:25 · built from scenes 1–3

- **Hook (first 1.5s):** Report card slams down: "A? B? C? D? ...CRAB?"
- **Script:** if and else give you two roads. Your report card needs five. So C gives you a ladder. Each rung asks one question. 90 or more? Grade A. 75 or more? Grade B. And so on, down to the bottom. The moment one rung says yes, you get off. That is the else-if ladder.
- **On-screen text:** 5 GRADES, 1 LADDER
- **Caption + hashtags:** Turning marks into grades with one else-if ladder. #cprogramming #learntocode #kodingkonkani #elseif #codingforbeginners

**S2 · First true wins** — 0:30 · built from scenes 4 and 7

- **Hook (first 1.5s):** "80" slides down a ladder and stops at B.
- **Script:** else-if in 30 seconds. C checks each condition from the top. 80: is it 90 or more? No. 75 or more? Yes. Print Grade B, and stop. It never checks 60 or 35, even though those are true too. First true wins. And because of that, you never need to write "and less than 90". The rung above already handled it.
- **On-screen text:** FIRST TRUE WINS
- **Caption + hashtags:** The one rule that makes else-if ladders click. #cprogramming #learntocode #kodingkonkani #ctutorial #programming

**S3 · Topper gets a D** — 0:35 · built from scene 8

- **Hook (first 1.5s):** Terminal: "marks = 95" then "Grade D". Xecxec faints.
- **Script:** 95 marks. Grade D. No error. No warning. What happened? The first check was 35 or more. 95 is more than 35, so it is caught right there. The 90 check never runs, for anyone, ever. Fix: put the strictest check first. 90, then 75, then 60, then 35. In an else-if ladder, order is everything.
- **On-screen text:** 95 MARKS = GRADE D?!
- **Caption + hashtags:** No error, no warning, completely wrong grade. #cprogramming #debugging #kodingkonkani #learntocode #codinglife

**S4 · Conditions to fall back on** — 0:12 · built from scene 6

- **Hook (first 1.5s):** Xecxec sitting alone on a ladder rung
- **Script:** Why did the else-if ladder never get lonely? It always had a few conditions to fall back on.
- **On-screen text:** CONDITIONS TO FALL BACK ON
- **Caption + hashtags:** Send this to your else-if friend. #programmerhumor #cprogramming #kodingkonkani #codingjokes

**S5 · Ladder or five ifs?** — 0:30 · built from scenes 7 and 9

- **Hook (first 1.5s):** "80 marks. How many grades print?"
- **Script:** Quiz. Five separate if statements: 90 or more prints A, 75 prints B, 60 prints C, 35 prints D. Marks are 80. How many lines print? Three, two, one. Three lines: B, C and D. Separate ifs check everything. An else-if ladder prints only B. Now try the challenge: a bus fare calculator by distance. Answer in the comments.
- **On-screen text:** HOW MANY GRADES PRINT?
- **Caption + hashtags:** Separate ifs vs an else-if ladder. Did you get it? #cprogramming #codingquiz #kodingkonkani #learntocode #elseif

## EP 22 — Nested if

**Module 3 · Decisions · 6:10 · Mint + Dark blue · Prerequisite: EP 21**

**Learning goals:** put an if inside another if when the second question only makes sense after the first; trace which inner and outer branches run; know that an `else` pairs with the nearest unmatched `if`; use braces to stop the dangling else.

### YouTube

- **Title:** Nested if and the Dangling else Trap | C Programming EP 22
- **Description:** Some questions only make sense after another question says yes. First the bouncer checks your ticket, then your ID. Today we put an if inside an if, trace every path, and catch the dangling else that hides behind neat indentation. Chapters: 0:00 The beach concert gate · 0:25 If inside if · 1:10 Code line by line · 2:55 Running it · 3:30 Reading nested code · 4:10 Bug of the Day · 5:20 Challenge
- **Tags:** c programming, nested if in c, dangling else, if inside if, decision making in c, learn c, c for beginners, c tutorial english, koding konkani, leap year program
- **Thumbnail:** big text "WHICH IF?"; one lonely else block with two if blocks pulling it from both sides; Xecxec as a bouncer with sunglasses at a gate; mint background, dark blue blocks

### Scene list

| # | Start | Length | Template | On screen | Animation & SFX |
| --- | --- | --- | --- | --- | --- |
| 1 | 0:00 | 0:20 | Concept slide | Beach concert gate at Vagator; Xecxec bouncer checks ticket, then ID | Waves, crowd murmur; stamp SFX on ticket |
| 2 | 0:20 | 0:05 | Title card | EP 22 · NESTED IF | Title slam, whoosh |
| 3 | 0:25 | 0:45 | Concept slide | Flowchart: "ticket?" diamond, YES leads into a second diamond "age >= 18?" drawn inside a box | Outer box draws, inner diamond zooms in like a door inside a door |
| 4 | 1:10 | 1:45 | Code explain | ep22.c, 23 lines; trackers hasTicket and age | Outer block tinted dark blue, inner block tinted mint; line highlights; key-tap SFX |
| 5 | 2:55 | 0:30 | Terminal | Runs: 1 + 20, 1 + 15, 0 | Typing SFX; gate opens or closes per run |
| 6 | 3:25 | 0:05 | Pun card | Pun line | Drum hit, claw-click |
| 7 | 3:30 | 0:40 | Concept slide | Three paths table: ticket and adult, ticket and minor, no ticket | Rows light up one by one |
| 8 | 4:10 | 1:10 | Bug of the Day | Dangling else: no ticket prints nothing | Else block slides from outer if to inner if; error buzz; braces snap in |
| 9 | 5:20 | 0:30 | Challenge | Leap year checker | Calendar flip SFX, timer ring |
| 10 | 5:50 | 0:20 | Outro | Next: EP 23 switch-case; sign-off | Module tiles, claw-click, music out |

### Narration script

**\[1 · The beach concert gate\]** Saturday night at Vagator. There is a beach concert, and Xecxec is the bouncer. First question: do you have a ticket? If not, go home. If yes, second question: are you 18 or older? Notice something. He never asks a person without a ticket for their ID. The second question only happens after the first one says yes. That is a nested if.

**\[2 · Title\]** Episode 22. Nested if.

**\[3 · If inside if\]** Nested just means inside. A nest is a home inside a tree. A nested if is an if that lives inside the block of another if. Look at the flowchart. The outer diamond asks about the ticket. On the NO side, we print no entry, done. On the YES side, we walk into a box, and inside that box is a second diamond, asking about age. That inner question has its own YES and NO. So we have three possible endings, not two: welcome, adults only, or no ticket.

**\[4 · Code line by line\]** Here is the gate in C. \[HL 4\] Line 4 makes two boxes, hasTicket and age. \[HL 6\] \[HL 7\] Lines 6 and 7 ask: do you have a ticket, 1 for yes, 0 for no, and read the answer. The user types 1. \[TRACK hasTicket=1\] \[HL 9\] Line 9 is the outer if: is hasTicket equal to 1? Double equals, a comparison, not single equals, remember EP 16. Yes, it is 1. So we enter the outer block, which runs from line 9 all the way to line 18. \[HL 10\] \[HL 11\] Lines 10 and 11 ask for the age and read it. Notice: we only ask for age inside the outer block. No ticket, no age question. The user types 20. \[TRACK age=20\] \[HL 13\] Line 13 is the inner if: is age greater than or equal to 18? Yes. \[HL 14\] Line 14 prints "Welcome to the beach concert!" \[HL 15\] C skips the inner else on lines 15 to 17. \[HL 18\] Then on line 18 we hit the outer else. The outer condition was true, so C skips that too. \[HL 22\] Return 0. Now run it again and type 0 for the ticket. \[TRACK hasTicket=0\] \[HL 9\] Line 9 is false. C skips the whole outer block, including the inner if. It never asks for age. \[HL 19\] It jumps to line 19: "No ticket, no entry." See the indentation? Each level moves four spaces to the right. Your eyes can follow the nesting like steps going in.

**\[5 · Running it\]** Compile and run three times. Ticket 1, age 20: welcome. Ticket 1, age 15: sorry, adults only tonight. Ticket 0: no ticket, no entry, and notice it never even asked for the age. Three runs, three different paths. When you test nested code, test every path at least once.

**\[6 · Pun\]** Why did the nested if feel so safe? Because it was surrounded by a lot of support from its parent.

**\[7 · Reading nested code\]** How do you read nested code without getting lost? Match the braces. Every opening brace has a closing brace at the same indentation level. VS Code helps: click next to a brace and its partner lights up. And a tip: if you are three or four levels deep, stop. Usually an else-if ladder or the AND operator can flatten it. For example, ticket AND adult could be one condition. We use nesting here because the inner question needs extra input that only makes sense after the outer yes.

**\[8 · Bug of the Day\]** Today's bug is famous. It is called the dangling else. Look at this code. No braces. if hasTicket equals 1, then if age is 18 or more, print welcome. Then an else, lined up neatly under the first if, printing "No ticket, no entry." hasTicket is 0. We run it. And it prints nothing. Nothing at all! Why? C does not care about your spaces. The rule is: an else belongs to the nearest if above it that does not already have an else. The nearest one is the inner if, the age check. So C actually reads this as: if ticket, then if age, welcome, else no ticket. With no ticket, the outer if is false, and the whole thing is skipped. Plain gcc stays silent. With -Wall, GCC says: suggest explicit braces to avoid ambiguous else. That is GCC telling you: I see the trap. The fix: braces. Put the inner if inside braces, and the else now clearly belongs to the outer if. Now it prints "No ticket, no entry."

**\[9 · Challenge\]** Your challenge: the leap year checker. A year is a leap year if it divides by 4. But if it also divides by 100, it is not a leap year, unless it also divides by 400. So 2024 is a leap year. 1900 is not. 2000 is. Use nested ifs and the modulo operator from EP 15. Test with those three years. Answer in the comments.

**\[10 · Outro\]** Next episode: when you have one value and many exact choices, like a restaurant menu, there is a neater tool than a ladder. switch-case, in EP 23. Keep coding, says Xecxec!

### Code shown

```c
#include <stdio.h>

int main(void) {
    int hasTicket, age;

    printf("Do you have a ticket? (1 = yes, 0 = no): ");
    scanf("%d", &hasTicket);

    if (hasTicket == 1) {
        printf("Enter your age: ");
        scanf("%d", &age);

        if (age >= 18) {
            printf("Welcome to the beach concert!\n");
        } else {
            printf("Sorry, adults only tonight.\n");
        }
    } else {
        printf("No ticket, no entry.\n");
    }

    return 0;
}
```

**Expected output** (three runs; user input shown after each prompt):

```text
Do you have a ticket? (1 = yes, 0 = no): 1
Enter your age: 20
Welcome to the beach concert!

Do you have a ticket? (1 = yes, 0 = no): 1
Enter your age: 15
Sorry, adults only tonight.

Do you have a ticket? (1 = yes, 0 = no): 0
No ticket, no entry.
```

### Bug of the Day

Wrong code:

```c
#include <stdio.h>

int main(void) {
    int hasTicket = 0;
    int age = 20;

    if (hasTicket == 1)
        if (age >= 18)
            printf("Welcome!\n");
    else
        printf("No ticket, no entry.\n");

    return 0;
}
```

With plain `gcc` there is no error, and the program prints nothing (empty output). With `gcc -Wall` (GCC 13):

```text
ep22bug.c:7:8: warning: suggest explicit braces to avoid ambiguous 'else' [-Wdangling-else]
    7 |     if (hasTicket == 1)
      |        ^
```

Fixed code:

```c
#include <stdio.h>

int main(void) {
    int hasTicket = 0;
    int age = 20;

    if (hasTicket == 1) {
        if (age >= 18)
            printf("Welcome!\n");
    } else {
        printf("No ticket, no entry.\n");
    }

    return 0;
}
```

Output after the fix:

```text
No ticket, no entry.
```

Why: an `else` always pairs with the nearest unmatched `if`, whatever the indentation says, so braces are needed to attach it to the outer `if`.

### Pun & challenge

- **Pun:** Why did the nested if feel so safe? Because it was surrounded by a lot of support from its parent.
- **Challenge:** Leap year checker with nested ifs: divisible by 4 is a leap year, except years divisible by 100, unless also divisible by 400. Test 2024, 1900, 2000.
- **Challenge answer:**

```c
int year;
scanf("%d", &year);
if (year % 4 == 0) {
    if (year % 100 == 0) {
        if (year % 400 == 0)
            printf("%d is a leap year\n", year);
        else
            printf("%d is not a leap year\n", year);
    } else {
        printf("%d is a leap year\n", year);
    }
} else {
    printf("%d is not a leap year\n", year);
}
/* 2024: leap, 1900: not leap, 2000: leap */
```

### Shorts for EP 22

**S1 · The bouncer's two questions** — 0:25 · built from scenes 1–3

- **Hook (first 1.5s):** Xecxec in sunglasses blocks the gate: "Ticket?"
- **Script:** A bouncer at a beach concert asks two questions. Ticket? Then ID. But he never asks for ID if you have no ticket. The second question lives inside the first. In C, that is a nested if: an if inside the block of another if. Three paths, one gate.
- **On-screen text:** AN IF INSIDE AN IF
- **Caption + hashtags:** Nested if, explained by a crab bouncer. #cprogramming #learntocode #kodingkonkani #nestedif #codingforbeginners

**S2 · Nested if in 30 seconds** — 0:30 · built from scene 4

- **Hook (first 1.5s):** Code with outer block tinted dark blue, inner block mint
- **Script:** Nested if in 30 seconds. The outer if checks the ticket. Only if that is true do we enter its block, ask for age, and reach the inner if. Inner true: welcome. Inner false: adults only. Outer false: we skip everything inside, and go to the outer else. No ticket, no entry. Indent each level so your eyes can follow it.
- **On-screen text:** OUTER FIRST, THEN INNER
- **Caption + hashtags:** Three paths, two ifs, one clean program. #cprogramming #learntocode #kodingkonkani #ctutorial #programming

**S3 · The dangling else** — 0:40 · built from scene 8

- **Hook (first 1.5s):** Terminal shows an empty output. Xecxec taps the screen. "Hello?"
- **Script:** This code should print no ticket, no entry. It prints nothing. The else is lined up with the outer if, but C ignores spaces. An else always belongs to the nearest if without an else. That is the inner if. So the whole thing is skipped. Compile with -Wall and GCC warns: suggest explicit braces to avoid ambiguous else. Add braces, and it works.
- **On-screen text:** ELSE GOES TO THE NEAREST IF
- **Caption + hashtags:** Your indentation lied. C did not listen. #cprogramming #debugging #kodingkonkani #learntocode #codinglife

**S4 · Support from its parent** — 0:12 · built from scene 6

- **Hook (first 1.5s):** Small if block hugged by a bigger if block
- **Script:** Why did the nested if feel so safe? Because it was surrounded by a lot of support from its parent.
- **On-screen text:** SUPPORT FROM ITS PARENT
- **Caption + hashtags:** Wholesome code content. #programmerhumor #cprogramming #kodingkonkani #codingjokes

**S5 · Is 1900 a leap year?** — 0:25 · built from scene 9

- **Hook (first 1.5s):** Calendar page "1900" with a big question mark
- **Script:** Quick quiz. 1900 divides by 4. Is it a leap year? Three, two, one. No! Years that divide by 100 are not leap years, unless they also divide by 400. So 1900 is not, but 2000 is. Your challenge: write this rule in C with nested ifs. Answer in the comments.
- **On-screen text:** 1900: LEAP YEAR?
- **Caption + hashtags:** Most people get this wrong. Did you? #cprogramming #codingquiz #kodingkonkani #learntocode #leapyear

## EP 23 — switch-case

**Module 3 · Decisions · 6:20 · Mint + Dark blue · Prerequisite: EP 22**

**Learning goals:** write a `switch` on an int or char with `case` labels, `break` and `default`; explain fall-through and why `break` stops it; group cases that share one action; know when switch fits (exact values) and when an else-if ladder fits (ranges).

### YouTube

- **Title:** switch-case: Build a Restaurant Menu in C | C Programming EP 23
- **Description:** When one value can match many exact choices, a long else-if ladder gets messy. Today we build Xecxec's beach shack menu with switch, case, break and default. Then we remove one break and watch the whole menu fall through onto your bill. Chapters: 0:00 The menu machine · 0:25 How switch works · 1:10 Code line by line · 3:00 Running it · 3:25 Grouping cases · 4:15 Bug of the Day · 5:30 Challenge
- **Tags:** c programming, switch case in c, switch statement, break and default, fall through in c, menu program in c, learn c, c for beginners, koding konkani, c tutorial english
- **Thumbnail:** big text "WHO ORDERED ALL THIS?"; a bill sliding out of a machine with 4 items; Xecxec as a waiter with a tray piled high, sweating; mint background, dark blue blocks

### Scene list

| # | Start | Length | Template | On screen | Animation & SFX |
| --- | --- | --- | --- | --- | --- |
| 1 | 0:00 | 0:20 | Concept slide | Xecxec's beach shack menu board: 1 Fish thali, 2 Prawn curry rice, 3 Bebinca | Chalkboard draws in, waves SFX, order bell |
| 2 | 0:20 | 0:05 | Title card | EP 23 · SWITCH-CASE | Title slam, whoosh |
| 3 | 0:25 | 0:45 | Concept slide | A sorting machine: value drops in, lands on the matching case door; "default" door at the end | Value ball rolls, door clicks open, ding |
| 4 | 1:10 | 1:50 | Code explain | ep23.c, 28 lines; tracker for choice | Line highlights; arrow jumps from switch to the matching case; break shown as an exit sign; key-tap SFX |
| 5 | 3:00 | 0:20 | Terminal | Runs: 1, 2, 3, 7 | Typing SFX, a bill slip prints each time |
| 6 | 3:20 | 0:05 | Pun card | Pun line | Drum hit, claw-click |
| 7 | 3:25 | 0:50 | Code explain | ep23b.c, grouped cases 'A' and 'B' on a char | Two case labels glow together; tracker for grade |
| 8 | 4:15 | 1:15 | Bug of the Day | Missing breaks: ordering 1 prints all four lines | Items pile onto the tray one by one; error buzz; break signs snap in |
| 9 | 5:30 | 0:30 | Challenge | Day number to day name | Calendar flip, timer ring |
| 10 | 6:00 | 0:20 | Outro | Next: EP 24 logic puzzles; sign-off | Module tiles, claw-click, music out |

### Narration script

**\[1 · The menu machine\]** Xecxec has opened a beach shack. The menu has numbers. 1 is fish thali, 2 is prawn curry rice, 3 is bebinca. A customer says a number, and the kitchen makes that dish. You could write this with the else-if ladder from EP 21. If choice is 1, else if choice is 2, else if choice is 3. It works. But C has a tool made exactly for this job.

**\[2 · Title\]** Episode 23. switch-case.

**\[3 · How switch works\]** Think of a sorting machine. You drop one value in at the top. The machine looks at the value once, and jumps straight to the door with the same number on it. That door is called a case. Each case ends with a break, which is the exit. And if no door matches, the value rolls to the last door, called default. One value in, one exact match, one exit. Two rules: switch works only with whole-number values, like int and char. And each case must be a constant, like 1 or the letter A, not a variable and not a range.

**\[4 · Code line by line\]** Here is the shack in C. \[HL 4\] Line 4 makes the box choice. \[HL 6\] Lines 6 to 10 print the menu. \[HL 11\] Line 11 reads the number. The customer types 2. \[TRACK choice=2\] \[HL 13\] Line 13: switch, and inside the round brackets, the value we are checking: choice. Then an opening curly brace. Everything up to the closing brace on line 25 belongs to this switch. Now the jump. C looks at choice, sees 2, and goes directly to the label case 2. It does not check case 1 first. \[HL 17\] Line 17: case 2, then a colon. Notice the colon, not a semicolon. A case is a label, a sign on a door. \[HL 18\] Line 18 prints "Prawn curry rice: Rs 300". \[HL 19\] Line 19: break. Break means: leave the switch right now. C jumps to the closing brace on line 25 and carries on from line 27. \[HL 23\] Now look at line 23: default, with a colon. If the customer types 7, no case matches, so C jumps here and prints "Not on the menu!" Default is like the else at the bottom of a ladder. It is optional, but always add one. Customers will order things that do not exist.

**\[5 · Running it\]** Compile and run. 1: fish thali, 250 rupees. 2: prawn curry rice, 300. 3: bebinca, 120. And 7: not on the menu. Four runs, four correct bills.

**\[6 · Pun\]** Why did the switch statement never finish its meal? It kept taking a break.

**\[7 · Grouping cases\]** Sometimes two values should do the same thing. Here is ep23b.c. We switch on a char, grade, which holds the letter B. \[TRACK grade='B'\] \[HL 6\] Line 6: switch on grade. \[HL 7\] \[HL 8\] Lines 7 and 8 are case 'A' and case 'B', stacked with nothing between them. Character cases use single quotes, as in EP 8. C jumps to case 'B'. There is nothing under it except the next line, so it flows down into line 9 and prints "Well done!" \[HL 10\] Then break. So A and B share one action. Stacking empty case labels like this is normal and useful. Keep this idea of flowing down in mind. In a second it will bite us.

**\[8 · Bug of the Day\]** Today's bug: the missing break. Here is the shack code, but someone forgot every break. The customer orders 1. We run it. The output: fish thali, prawn curry rice, bebinca, and not on the menu! Four lines for one order. Why? A case is only a label. It is where C starts, not where C stops. Without a break, C keeps running every line below, through every other case, all the way to the end. This is called fall-through. In the last scene we used it on purpose. Here it is a disaster. Plain gcc compiles it silently. With -Wextra, GCC warns: this statement may fall through, and points at each case below. The fix: put break at the end of every case. You can skip it on the last one, default, but many programmers add it there too, so a new case added later is safe.

**\[9 · Challenge\]** Your challenge: read a day number from 1 to 7 and print the day name. 1 is Monday, 7 is Sunday. Anything else prints Invalid day. Use switch, break and default. Answer in the comments.

**\[10 · Outro\]** Next episode: we put AND, OR and NOT together and solve real logic puzzles, including a triangle riddle from Xecxec. EP 24. Keep coding, says Xecxec!

### Code shown

File 1, ep23.c:

```c
#include <stdio.h>

int main(void) {
    int choice;

    printf("--- Xecxec's Shack ---\n");
    printf("1. Fish thali\n");
    printf("2. Prawn curry rice\n");
    printf("3. Bebinca\n");
    printf("Your choice: ");
    scanf("%d", &choice);

    switch (choice) {
        case 1:
            printf("Fish thali: Rs 250\n");
            break;
        case 2:
            printf("Prawn curry rice: Rs 300\n");
            break;
        case 3:
            printf("Bebinca: Rs 120\n");
            break;
        default:
            printf("Not on the menu!\n");
    }

    return 0;
}
```

**Expected output** (run with input 2; inputs 1, 3 and 7 print the matching line instead):

```text
--- Xecxec's Shack ---
1. Fish thali
2. Prawn curry rice
3. Bebinca
Your choice: 2
Prawn curry rice: Rs 300
```

Last line for the other runs:

```text
1 -> Fish thali: Rs 250
3 -> Bebinca: Rs 120
7 -> Not on the menu!
```

File 2, ep23b.c:

```c
#include <stdio.h>

int main(void) {
    char grade = 'B';

    switch (grade) {
        case 'A':
        case 'B':
            printf("Well done!\n");
            break;
        case 'C':
            printf("Good effort.\n");
            break;
        default:
            printf("Keep practising.\n");
    }

    return 0;
}
```

**Expected output:**

```text
Well done!
```

### Bug of the Day

Wrong code:

```c
#include <stdio.h>

int main(void) {
    int choice = 1;

    switch (choice) {
        case 1:
            printf("Fish thali: Rs 250\n");
        case 2:
            printf("Prawn curry rice: Rs 300\n");
        case 3:
            printf("Bebinca: Rs 120\n");
        default:
            printf("Not on the menu!\n");
    }

    return 0;
}
```

Plain `gcc` compiles it with no message. Wrong output:

```text
Fish thali: Rs 250
Prawn curry rice: Rs 300
Bebinca: Rs 120
Not on the menu!
```

With `gcc -Wall -Wextra` (GCC 13), one warning per missing break, the first being:

```text
ep23bug.c:8:13: warning: this statement may fall through [-Wimplicit-fallthrough=]
    8 |             printf("Fish thali: Rs 250\n");
      |             ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
ep23bug.c:9:9: note: here
    9 |         case 2:
      |         ^~~~
```

Fixed code: identical to ep23.c above, with `break;` after each case's `printf`.

Why: a `case` is only a starting label, so without `break` C keeps running every statement below it until the switch ends.

### Pun & challenge

- **Pun:** Why did the switch statement never finish its meal? It kept taking a break.
- **Challenge:** Read a day number 1–7 and print the day name (1 = Monday ... 7 = Sunday); anything else prints "Invalid day". Use switch, break and default.
- **Challenge answer:**

```c
int day;
scanf("%d", &day);
switch (day) {
    case 1: printf("Monday\n"); break;
    case 2: printf("Tuesday\n"); break;
    case 3: printf("Wednesday\n"); break;
    case 4: printf("Thursday\n"); break;
    case 5: printf("Friday\n"); break;
    case 6: printf("Saturday\n"); break;
    case 7: printf("Sunday\n"); break;
    default: printf("Invalid day\n");
}
```

### Shorts for EP 23

**S1 · The menu machine** — 0:25 · built from scenes 1–3

- **Hook (first 1.5s):** Order bell rings, chalkboard menu: "1, 2 or 3?"
- **Script:** A customer says a number. The kitchen makes that dish. You could write a long else-if ladder. Or you could use switch. Drop one value in, and C jumps straight to the matching case. No match? It goes to default. One value in, one exact match, one exit.
- **On-screen text:** ONE VALUE, ONE DOOR
- **Caption + hashtags:** Building a beach shack menu with switch-case. #cprogramming #learntocode #kodingkonkani #switchcase #codingforbeginners

**S2 · switch in 30 seconds** — 0:30 · built from scene 4

- **Hook (first 1.5s):** Arrow jumps from "switch (choice)" straight to "case 2:"
- **Script:** switch in 30 seconds. Write switch and the value in brackets. Each case is a label with a colon. C jumps straight to the matching case and runs from there. break means leave the switch now. default catches anything that does not match. It only works with whole numbers and characters, and each case must be a constant.
- **On-screen text:** CASE · BREAK · DEFAULT
- **Caption + hashtags:** Three keywords, one clean menu. #cprogramming #learntocode #kodingkonkani #ctutorial #programming

**S3 · Who ordered all this?** — 0:35 · built from scene 8

- **Hook (first 1.5s):** Xecxec's tray piles up with four dishes. "I ordered ONE thing!"
- **Script:** Order number 1. The bill shows fish thali, prawn curry, bebinca, and not on the menu. Four lines! Someone forgot the breaks. A case is where C starts, not where it stops. Without break, it falls through every case below. Compile with -Wextra and GCC warns: this statement may fall through. Add break to every case.
- **On-screen text:** NO BREAK = FALL-THROUGH
- **Caption + hashtags:** One missing word, four dishes on the bill. #cprogramming #debugging #kodingkonkani #learntocode #codinglife

**S4 · Taking a break** — 0:12 · built from scene 6

- **Hook (first 1.5s):** Xecxec lounging on a beach chair beside a half-eaten thali
- **Script:** Why did the switch statement never finish its meal? It kept taking a break.
- **On-screen text:** IT KEPT TAKING A BREAK
- **Caption + hashtags:** Relatable. #programmerhumor #cprogramming #kodingkonkani #codingjokes

**S5 · switch or ladder?** — 0:25 · built from scenes 3 and 9

- **Hook (first 1.5s):** "case marks >= 90:" with a red question mark
- **Script:** Quiz. Can you write case marks greater than or equal to 90 in a switch? Three, two, one. No! Each case must be a constant value, not a range. For ranges, use an else-if ladder. For exact values, like menu numbers or day numbers, use switch. Challenge: print the day name from a number 1 to 7. Answer in the comments.
- **On-screen text:** SWITCH: EXACT VALUES ONLY
- **Caption + hashtags:** Ranges go in ladders, exact values go in switch. #cprogramming #codingquiz #kodingkonkani #learntocode #switchcase

## EP 24 — Logic puzzles in C

**Module 3 · Decisions · 6:15 · Mint + Dark blue · Prerequisite: EP 23**

**Learning goals:** combine `&&`, `||` and `!` inside if conditions; turn a word rule ("the sum of any two sides must be greater than the third") into a C condition; order checks so invalid cases are rejected first; recognise that `a == b == c` does not mean "all three equal".

### YouTube

- **Title:** Can You Solve Xecxec's Triangle Riddle? | C Programming EP 24
- **Description:** Give a program three numbers. Is it a triangle? What kind? Today we solve Xecxec's riddle by combining AND, OR and NOT into clear conditions, and we meet a condition that looks perfectly right but quietly lies. Chapters: 0:00 The riddle · 0:25 Rules to conditions · 1:15 Code line by line · 3:05 Running it · 3:40 Keep conditions simple · 4:20 Bug of the Day · 5:25 Challenge
- **Tags:** c programming, logical operators in c, triangle program in c, and or not in c, if else in c, decision making in c, learn c, c for beginners, koding konkani, c logic puzzles
- **Thumbnail:** big text "a == b == c ?"; three sticks forming a triangle with a red question mark in the middle; Xecxec in a detective cap with a magnifying glass; mint background, dark blue blocks

### Scene list

| # | Start | Length | Template | On screen | Animation & SFX |
| --- | --- | --- | --- | --- | --- |
| 1 | 0:00 | 0:20 | Concept slide | Xecxec holds three sticks of driftwood: 1, 2 and 10. "Make a triangle." | Sticks drop on sand, fail to meet; boing |
| 2 | 0:20 | 0:05 | Title card | EP 24 · LOGIC PUZZLES IN C | Title slam, whoosh |
| 3 | 0:25 | 0:50 | Concept slide | Four word rules on cards, each turning into a C condition | Card flips: words on front, C on back; clicks |
| 4 | 1:15 | 1:50 | Code explain | ep24.c, 22 lines; trackers a, b, c | Line highlights; each sub-condition gets a true/false badge; key-tap SFX |
| 5 | 3:05 | 0:30 | Terminal | Runs: 3 3 3, 5 5 8, 3 4 5, 1 2 10, 0 4 4 | Typing SFX; matching triangle shape draws beside each output |
| 6 | 3:35 | 0:05 | Pun card | Pun line | Drum hit, claw-click |
| 7 | 3:40 | 0:40 | Concept slide | "Keep it simple": a long tangled condition untangled into three short rungs | Knot untangles animation |
| 8 | 4:20 | 1:05 | Bug of the Day | a == b == c with 2, 2, 2 prints Not equilateral | Expression evaluates step by step in boxes; error buzz; fix swoosh |
| 9 | 5:25 | 0:30 | Challenge | Largest of 3 numbers | Three bars race up; timer ring |
| 10 | 5:55 | 0:20 | Outro | Next: EP 25 mini project quiz app; sign-off | Module tiles, claw-click, music out |

### Narration script

**\[1 · The riddle\]** Xecxec found three sticks of driftwood on Morjim beach. Lengths 1, 2 and 10. He tries to make a triangle. The two short sticks cannot even reach each other. So here is his riddle: given any three lengths, can your program tell if they make a triangle, and what kind? By the end of this video, it will.

**\[2 · Title\]** Episode 24. Logic puzzles in C.

**\[3 · Rules to conditions\]** A logic puzzle is just rules in words. Our job is to turn each rule into a C condition, using the operators from EP 16. Rule one: every side must be more than zero. In C: if a is less than or equal to 0, OR b is, OR c is, reject it. Rule two: any two sides together must be longer than the third. If even one pair fails, it is not a triangle. In C: a plus b less than or equal to c, OR b plus c less than or equal to a, OR a plus c less than or equal to b. Rule three: all sides equal is equilateral. That is a equals b AND b equals c. Rule four: exactly two sides equal is isosceles. a equals b, OR b equals c, OR a equals c. Notice the pattern. "Any one of these" becomes OR. "All of these" becomes AND.

**\[4 · Code line by line\]** Here is the solution. \[HL 4\] Line 4 makes three boxes, a, b and c. \[HL 7\] Line 7 reads all three with one scanf, three percent d's and three ampersands. The user types 5, 5 and 8. \[TRACK a=5\] \[TRACK b=5\] \[TRACK c=8\] \[HL 9\] Line 9 checks rule one. Is any side zero or less? 5, 5, 8. All positive, so false. Skip. \[HL 11\] Line 11 checks rule two. 5 plus 5 is 10. Is 10 less than or equal to 8? No. 5 plus 8 is 13, less than or equal to 5? No. 5 plus 8 again, less than or equal to 5? No. All three parts false, so the OR is false. It is a real triangle. \[HL 13\] Line 13: is a equal to b, AND b equal to c? 5 equals 5, true. 5 equals 8, false. True AND false is false. Not equilateral. \[HL 15\] Line 15: a equals b, OR b equals c, OR a equals c? The first part is already true. And here is a nice fact: with OR, once one part is true, C does not even check the rest. With AND, once one part is false, C stops too. This is called short-circuit evaluation. \[HL 16\] Line 16 prints "Isosceles triangle". Now notice the order of the ladder. Invalid first. Not-a-triangle second. Then the shapes. Why does line 15 not wrongly catch equilateral triangles? Because line 13 already caught them. First true wins, from EP 21. \[HL 17\] \[HL 18\] And the final else needs no condition at all. If we got here, it is a real triangle with no equal sides. Scalene.

**\[5 · Running it\]** Let's test every path. 3, 3, 3: equilateral. 5, 5, 8: isosceles. 3, 4, 5: scalene. 1, 2, 10: Xecxec's driftwood. Not a triangle! And 0, 4, 4: sides must be positive. Five inputs, five different paths. That is how you test a decision program: one input per path.

**\[6 · Pun\]** Why did the triangle refuse to argue? Because it already had all the right angles. Well, the scalene one did.

**\[7 · Keep conditions simple\]** You could write this whole program as one giant if with ten ANDs and ORs. Please don't. Long conditions are hard to read and easy to get wrong. Three tips. One: one rule per rung of the ladder. Two: when you mix AND and OR, add brackets so the order is obvious. Remember EP 19, AND is checked before OR. Three: if a condition does not fit on one line, it is probably doing too much. Split it. Short rungs, clear answers.

**\[8 · Bug of the Day\]** Today's bug looks perfectly right. a, b and c are all 2. The code says: if a equals equals b equals equals c, print equilateral. In maths, that reads "all three are equal". We run it, and it prints "Not equilateral"! Why? C does not read it like maths. It reads left to right, one comparison at a time. First, a equals b. 2 equals 2, true. And true in C is the number 1. Now C checks 1 equals c. Is 1 equal to 2? No. False. Plain gcc gives no error. With -Wall, GCC warns: suggest parentheses around comparison in operand of equals equals. That is GCC saying: are you sure this is what you meant? The fix: a equals b AND b equals c. Two separate comparisons joined with AND. Funny thing: with 1, 1 and 1, the broken version prints equilateral, by pure luck. That is why bugs like this survive testing.

**\[9 · Challenge\]** Your challenge: read three numbers and print the largest. Use AND to check if a is at least as big as both others. Then think: if a is not the largest, how many comparisons do you still need? Hint: only one. Answer in the comments.

**\[10 · Outro\]** Next episode is our first mini project of this module. We take if, else, switch and a score counter, and build a quiz app for your friends. EP 25. Keep coding, says Xecxec!

### Code shown

```c
#include <stdio.h>

int main(void) {
    int a, b, c;

    printf("Enter three sides: ");
    scanf("%d %d %d", &a, &b, &c);

    if (a <= 0 || b <= 0 || c <= 0) {
        printf("Sides must be positive.\n");
    } else if (a + b <= c || b + c <= a || a + c <= b) {
        printf("Not a triangle!\n");
    } else if (a == b && b == c) {
        printf("Equilateral triangle\n");
    } else if (a == b || b == c || a == c) {
        printf("Isosceles triangle\n");
    } else {
        printf("Scalene triangle\n");
    }

    return 0;
}
```

**Expected output** (five runs; user input shown after the prompt):

```text
Enter three sides: 3 3 3
Equilateral triangle

Enter three sides: 5 5 8
Isosceles triangle

Enter three sides: 3 4 5
Scalene triangle

Enter three sides: 1 2 10
Not a triangle!

Enter three sides: 0 4 4
Sides must be positive.
```

### Bug of the Day

Wrong code:

```c
#include <stdio.h>

int main(void) {
    int a = 2, b = 2, c = 2;

    if (a == b == c) {
        printf("Equilateral triangle\n");
    } else {
        printf("Not equilateral\n");
    }

    return 0;
}
```

Plain `gcc` gives no error. Wrong output:

```text
Not equilateral
```

With `gcc -Wall` (GCC 13):

```text
ep24bug.c:6:11: warning: suggest parentheses around comparison in operand of '==' [-Wparentheses]
    6 |     if (a == b == c) {
      |         ~~^~~~
```

Fixed code:

```c
#include <stdio.h>

int main(void) {
    int a = 2, b = 2, c = 2;

    if (a == b && b == c) {
        printf("Equilateral triangle\n");
    } else {
        printf("Not equilateral\n");
    }

    return 0;
}
```

Output after the fix:

```text
Equilateral triangle
```

Why: `a == b == c` is read as `(a == b) == c`, which compares the result 1 (true) with `c`, so it only "works" when `c` happens to be 1.

### Pun & challenge

- **Pun:** Why did the triangle refuse to argue? Because it already had all the right angles. Well, the scalene one did.
- **Challenge:** Read three numbers and print the largest, using `&&` and as few comparisons as possible.
- **Challenge answer:**

```c
int a, b, c;
scanf("%d %d %d", &a, &b, &c);
if (a >= b && a >= c)
    printf("Largest: %d\n", a);
else if (b >= c)
    printf("Largest: %d\n", b);
else
    printf("Largest: %d\n", c);
/* 4 9 2 -> Largest: 9 */
```

### Shorts for EP 24

**S1 · Xecxec's driftwood riddle** — 0:25 · built from scenes 1 and 3

- **Hook (first 1.5s):** Three driftwood sticks (1, 2, 10) drop on sand and fail to meet. "Triangle?"
- **Script:** Three sticks: 1, 2 and 10. Can they make a triangle? No. Any two sides together must be longer than the third. Your program can check that with one line of C: a plus b less than or equal to c, OR b plus c less than or equal to a, OR a plus c less than or equal to b. If any is true, it is not a triangle.
- **On-screen text:** TRIANGLE OR NOT?
- **Caption + hashtags:** Turning a maths rule into one line of C. #cprogramming #learntocode #kodingkonkani #logicpuzzle #codingforbeginners

**S2 · AND vs OR in 30 seconds** — 0:30 · built from scenes 3–4

- **Hook (first 1.5s):** Two cards: "ALL of these" and "ANY of these"
- **Script:** Turning words into conditions in 30 seconds. "All of these are true" becomes AND. "Any one of these is true" becomes OR. And C is lazy in a good way. With OR, the moment one part is true, it stops checking. With AND, the moment one part is false, it stops. That is called short-circuit evaluation.
- **On-screen text:** ALL = && · ANY = ||
- **Caption + hashtags:** The one trick for writing any condition in C. #cprogramming #learntocode #kodingkonkani #ctutorial #programming

**S3 · a == b == c lies** — 0:35 · built from scene 8

- **Hook (first 1.5s):** a = 2, b = 2, c = 2. Output: "Not equilateral". Xecxec drops his magnifying glass.
- **Script:** All three are 2. The program says not equal. Why? C reads a equals b equals c left to right. a equals b is true, and true is 1. Then it checks: is 1 equal to c? c is 2. False. With -Wall, GCC warns: suggest parentheses around comparison. Fix: a equals b AND b equals c.
- **On-screen text:** a == b == c IS NOT MATHS
- **Caption + hashtags:** Looks right, compiles fine, totally wrong. #cprogramming #debugging #kodingkonkani #learntocode #codinglife

**S4 · All the right angles** — 0:12 · built from scene 6

- **Hook (first 1.5s):** A smug right triangle with sunglasses
- **Script:** Why did the triangle refuse to argue? Because it already had all the right angles.
- **On-screen text:** ALL THE RIGHT ANGLES
- **Caption + hashtags:** Geometry jokes, C edition. #programmerhumor #cprogramming #kodingkonkani #codingjokes

**S5 · What does 1 == 1 == 1 give?** — 0:25 · built from scenes 8–9

- **Hook (first 1.5s):** "1 == 1 == 1 → ?"
- **Script:** Quiz. In C, what is 1 equals equals 1 equals equals 1? Three, two, one. True! 1 equals 1 gives 1, and 1 equals 1 gives 1. So the broken code works by luck when the sides are 1. Try 2, 2, 2 and it fails. Now your challenge: print the largest of three numbers. Answer in the comments.
- **On-screen text:** 1 == 1 == 1 → ???
- **Caption + hashtags:** Lucky bugs are the worst bugs. #cprogramming #codingquiz #kodingkonkani #learntocode #logicpuzzle

## EP 25 — Mini project: Quiz app

**Module 3 · Decisions · 7:30 · Mint + Dark blue · Prerequisite: EP 24**

**Learning goals:** combine if, else-if, switch and a score counter in one complete program; read a single character answer with `scanf(" %c", ...)` and explain the leading space; accept both upper- and lower-case answers; plan a program in blocks before typing it.

### YouTube

- **Title:** Build a Quiz App in C (Beginner Project) | C Programming EP 25
- **Description:** Module 3 ends with a real project. We plan and build Xecxec's Goa Quiz: questions, answers, a score and a final verdict, using everything from EP 20 to EP 24. You will also see why typing a capital B can make a correct answer wrong. Chapters: 0:00 Your first app · 0:25 Plan in blocks · 1:10 Question 1 with if · 2:35 Question 2 with switch · 3:45 The final verdict · 4:30 Full run · 5:10 Bug of the Day · 6:15 The space in " %c" · 6:50 Challenge
- **Tags:** c programming, quiz program in c, c mini project, c project for beginners, switch case in c, if else in c, scanf char, learn c, koding konkani, c tutorial english
- **Thumbnail:** big text "BUILD A QUIZ APP"; a game-show screen with "Q1" and options a, b, c; Xecxec as quiz host with a microphone; mint background, dark blue blocks; small "PROJECT" badge

### Scene list

| # | Start | Length | Template | On screen | Animation & SFX |
| --- | --- | --- | --- | --- | --- |
| 1 | 0:00 | 0:20 | Concept slide | Game-show stage, Xecxec as host, "Xecxec's Goa Quiz" sign | Spotlights, crowd cheer, claw-click |
| 2 | 0:20 | 0:05 | Title card | EP 25 · MINI PROJECT: QUIZ APP | Title slam, whoosh |
| 3 | 0:25 | 0:45 | Concept slide | Plan in 4 blocks: setup, Q1, Q2, verdict | Blocks stack like Lego, click per block |
| 4 | 1:10 | 1:25 | Code explain | quiz.c lines 1–20; trackers answer, score | Line highlights; score counter pops +1; key-tap SFX |
| 5 | 2:35 | 1:10 | Code explain | quiz.c lines 22–42 | Case labels glow in groups; tracker updates |
| 6 | 3:45 | 0:40 | Code explain | quiz.c lines 44–56 | Verdict ladder; score badge; key-tap SFX |
| 7 | 4:25 | 0:05 | Pun card | Pun line | Drum hit, claw-click |
| 8 | 4:30 | 0:40 | Terminal | Two full runs: B, b and a, z | Typing SFX; game-show ding on correct, buzzer on wrong |
| 9 | 5:10 | 1:05 | Bug of the Day | Q1 checks only 'b'; typing B prints Wrong | Capital B bounces off a lowercase lock; error buzz; |
| 10 | 6:15 | 0:35 | Concept slide | The space in " %c": input buffer shows B then the Enter key | Buffer boxes; newline box glows; space sweeps it away |
| 11 | 6:50 | 0:25 | Challenge | Add 3 more questions | Timer ring, crowd cheer |
| 12 | 7:15 | 0:15 | Outro | Module 3 complete badge; next: EP 26 Module 4 Loops; sign-off | Badge stamp, module tiles, music out |

### Narration script

**\[1 · Your first app\]** Lights! Music! Welcome to Xecxec's Goa Quiz! For five episodes we learnt how programs make decisions. Today we stop learning pieces and build something whole. A quiz app you can give to your friends. It asks questions, checks answers, keeps a score, and gives a verdict at the end.

**\[2 · Title\]** Episode 25. Mini project: quiz app.

**\[3 · Plan in blocks\]** Before typing a single line, plan. Real programmers do this. Our quiz has four blocks. Block one, setup: a box for the answer and a box for the score, starting at zero. Block two: question 1, checked with if and else. Block three: question 2, checked with switch. We use both on purpose, so you practise both. Block four, the verdict: an else-if ladder on the score. Four small blocks are easy. One big program in your head is hard.

**\[4 · Question 1 with if\]** Let's build it. \[HL 4\] Line 4: char answer. The answer is one letter, so a char is enough, from EP 8. \[HL 5\] Line 5: int score equals 0. Always start a counter at zero. An uninitialised score could start at any random number, as we saw in EP 7. \[TRACK score=0\] \[HL 7\] Line 7 prints the title. \[HL 10\] \[HL 11\] \[HL 12\] Lines 10 to 12 print question 1, the options, and a prompt. \[HL 13\] Line 13 reads the answer: scanf, space, percent c. Notice that space before percent c. It is important, and we will explain it at the end of the episode. The player types b. \[TRACK answer='b'\] \[HL 15\] Line 15: if answer equals small b, OR answer equals capital B. One letter, two ways to type it, so we accept both. \[HL 16\] Correct! \[HL 17\] Line 17: score plus plus, from EP 17. Score goes up by one. \[TRACK score=1\] \[HL 18\] \[HL 19\] If the answer was anything else, the else on line 18 prints the right answer, and score stays the same. That is teaching while testing.

**\[5 · Question 2 with switch\]** Question 2 uses switch. \[HL 23\] \[HL 24\] Lines 23 and 24 print the question and options. Look at line 24 carefully: percent percent. In printf, a single percent starts a format code. To print an actual percent sign, you write two. \[HL 26\] Line 26 reads the answer again, into the same box. The player types capital B. \[TRACK answer='B'\] \[HL 28\] Line 28: switch on answer. \[HL 29\] \[HL 30\] Lines 29 and 30: case small b and case capital B, stacked, just like the grouped cases from EP 23. \[HL 31\] \[HL 32\] \[HL 33\] Correct, score plus plus, break. \[TRACK score=2\] \[HL 34\] Now lines 34 to 37 group four cases: a, A, c, C. All the wrong options. \[HL 38\] They share one message. \[HL 40\] And default on line 40 catches anything that is not an option at all. If someone types z, they get "That is not even an option!" So switch gives us three kinds of answer: right, wrong, and nonsense. An if-else would need extra work for that.

**\[6 · The final verdict\]** \[HL 45\] Line 45 prints the score: You scored 2 out of 2. \[HL 47\] Lines 47 to 53 are an else-if ladder on the score, from EP 21. \[HL 48\] 2 means perfect. \[HL 50\] 1 means not bad. \[HL 52\] Anything else, which here means 0: back to the beach to study. \[HL 55\] Return 0. Done. Fifty-six lines, and every single one is something you already know.

**\[7 · Pun\]** Why did Xecxec fail his own quiz? He kept answering every question with a crab-ital letter.

**\[8 · Full run\]** Let's play. gcc quiz.c -o quiz, then dot slash quiz. Question 1: capital B. Correct! Question 2: small b. Correct! You scored 2 out of 2. Perfect, Xecxec is proud. Play again. Question 1: a. Wrong, it is Panaji. Question 2: z. That is not even an option! 0 out of 2. Back to the beach to study.

**\[9 · Bug of the Day\]** Today's bug: case-sensitive answers. Here is an early version of question 1. It only checks if answer equals small b. Your friend types capital B, because their caps lock is on. And the program says: Wrong! It is Panaji. But B is Panaji! No compiler error. No warning. The code does exactly what we wrote. Why? To C, small b and capital B are two different characters with two different numbers. Small b is 98. Capital B is 66. 66 is not 98, so the condition is false. The fix: answer equals small b, OR answer equals capital B. In later modules you will meet a function called tolower that turns any letter into small letters, but for now, OR does the job.

**\[10 · The space in " %c"\]** Now the mystery space. When you type b and press Enter, the keyboard sends two characters: the b, and an invisible newline from the Enter key. The first scanf takes the b. The newline stays waiting. Without the space, the second scanf with percent c would grab that leftover newline as the answer, and skip question 2 completely. The space before percent c tells scanf: first, skip any spaces, tabs or newlines. Then read one character. One tiny space saves your whole quiz. Use it every time you read a char with scanf.

**\[11 · Challenge\]** Your challenge: add three more questions to the quiz. Use if for some, switch for others. Then change the verdict ladder so it works out of 5. For example, 5 is perfect, 3 or 4 is good, and below 3 is back to the beach. Then send it to a friend and see who wins. Answer in the comments.

**\[12 · Outro\]** And that completes Module 3! Your programs can now make decisions. But they still do everything only once. What if the quiz should ask until you get it right? Next is Module 4: loops, starting with EP 26. Keep coding, says Xecxec!

### Code shown

```c
#include <stdio.h>

int main(void) {
    char answer;
    int score = 0;

    printf("=== Xecxec's Goa Quiz ===\n\n");

    /* Question 1 */
    printf("Q1. What is the capital of Goa?\n");
    printf("a) Margao  b) Panaji  c) Mapusa\n");
    printf("Your answer: ");
    scanf(" %c", &answer);

    if (answer == 'b' || answer == 'B') {
        printf("Correct!\n\n");
        score++;
    } else {
        printf("Wrong! It is Panaji.\n\n");
    }

    /* Question 2 */
    printf("Q2. Which operator gives the remainder in C?\n");
    printf("a) /  b) %%  c) &\n");
    printf("Your answer: ");
    scanf(" %c", &answer);

    switch (answer) {
        case 'b':
        case 'B':
            printf("Correct!\n\n");
            score++;
            break;
        case 'a':
        case 'A':
        case 'c':
        case 'C':
            printf("Wrong! It is %%.\n\n");
            break;
        default:
            printf("That is not even an option!\n\n");
    }

    /* Final result */
    printf("You scored %d out of 2\n", score);

    if (score == 2) {
        printf("Perfect! Xecxec is proud.\n");
    } else if (score == 1) {
        printf("Not bad. One more try?\n");
    } else {
        printf("Back to the beach to study!\n");
    }

    return 0;
}
```

**Expected output** (run 1, answers B then b):

```text
=== Xecxec's Goa Quiz ===

Q1. What is the capital of Goa?
a) Margao  b) Panaji  c) Mapusa
Your answer: B
Correct!

Q2. Which operator gives the remainder in C?
a) /  b) %  c) &
Your answer: b
Correct!

You scored 2 out of 2
Perfect! Xecxec is proud.
```

**Expected output** (run 2, answers a then z):

```text
=== Xecxec's Goa Quiz ===

Q1. What is the capital of Goa?
a) Margao  b) Panaji  c) Mapusa
Your answer: a
Wrong! It is Panaji.

Q2. Which operator gives the remainder in C?
a) /  b) %  c) &
Your answer: z
That is not even an option!

You scored 0 out of 2
Back to the beach to study!
```

### Bug of the Day

Wrong code:

```c
#include <stdio.h>

int main(void) {
    char answer;
    int score = 0;

    printf("Q1. What is the capital of Goa?\n");
    printf("a) Margao  b) Panaji  c) Mapusa\n");
    printf("Your answer: ");
    scanf(" %c", &answer);

    if (answer == 'b') {
        printf("Correct!\n");
        score++;
    } else {
        printf("Wrong! It is Panaji.\n");
    }

    printf("Score: %d\n", score);
    return 0;
}
```

No error and no warning, even with `gcc -Wall -Wextra`. Wrong output when the player types `B`:

```text
Q1. What is the capital of Goa?
a) Margao  b) Panaji  c) Mapusa
Your answer: B
Wrong! It is Panaji.
Score: 0
```

Fixed line (everything else unchanged):

```c
    if (answer == 'b' || answer == 'B') {
```

Output after the fix with `B`: `Correct!` then `Score: 1`.

Why: `'b'` (ASCII 98) and `'B'` (ASCII 66) are different characters, so a comparison with only one of them rejects the other.

### Pun & challenge

- **Pun:** Why did Xecxec fail his own quiz? He kept answering every question with a crab-ital letter.
- **Challenge:** Add 3 more questions (mix if and switch) and change the verdict to work out of 5: 5 is perfect, 3–4 is good, below 3 is "back to the beach".
- **Challenge answer:** one extra question block (repeat the pattern for the other two), plus the new verdict:

```c
/* Question 3 */
printf("Q3. Which keyword leaves a switch?\n");
printf("a) stop  b) exit  c) break\n");
printf("Your answer: ");
scanf(" %c", &answer);
if (answer == 'c' || answer == 'C') {
    printf("Correct!\n\n");
    score++;
} else {
    printf("Wrong! It is break.\n\n");
}

/* Verdict out of 5 */
printf("You scored %d out of 5\n", score);
if (score == 5) {
    printf("Perfect! Xecxec is proud.\n");
} else if (score >= 3) {
    printf("Good job!\n");
} else {
    printf("Back to the beach to study!\n");
}
```

### Shorts for EP 25

**S1 · Build a quiz app in C** — 0:25 · built from scenes 1, 3 and 8

- **Hook (first 1.5s):** Game-show lights, Xecxec with a microphone: "Q1!"
- **Script:** You know if, else, switch and a counter. That is enough to build a real app. A quiz for your friends. Plan it in four blocks: setup, question 1, question 2, verdict. Ask, check, add to the score, and give a verdict at the end. Fifty-six lines, all things you already know.
- **On-screen text:** YOUR FIRST C APP
- **Caption + hashtags:** Beginner C project: a quiz app for your friends. #cprogramming #learntocode #kodingkonkani #cproject #codingforbeginners

**S2 · Right, wrong or nonsense** — 0:30 · built from scene 5

- **Hook (first 1.5s):** Three buttons: RIGHT, WRONG, ???
- **Script:** Why use switch for a quiz question? Because it gives you three kinds of answer for free. Stack case small b and capital B for the right answer. Stack all the wrong letters for one wrong message. And default catches anything that is not even an option. Right, wrong or nonsense, in one switch.
- **On-screen text:** RIGHT · WRONG · NONSENSE
- **Caption + hashtags:** Grouped cases make quiz checking easy. #cprogramming #learntocode #kodingkonkani #switchcase #ctutorial

**S3 · B is not b** — 0:30 · built from scene 9

- **Hook (first 1.5s):** Player types B. Screen: "Wrong! It is Panaji." Xecxec: "But that IS Panaji!"
- **Script:** The answer is b, Panaji. Your friend types capital B. The program says wrong. No error, no warning. To C, small b is 98 and capital B is 66. Different characters. Fix: check answer equals small b, OR answer equals capital B. Your users will always type the letter you did not expect.
- **On-screen text:** 'b' != 'B'
- **Caption + hashtags:** Caps lock broke my quiz app. #cprogramming #debugging #kodingkonkani #learntocode #codinglife

**S4 · Crab-ital letters** — 0:12 · built from scene 7

- **Hook (first 1.5s):** Xecxec holding a giant capital letter B with both claws
- **Script:** Why did Xecxec fail his own quiz? He kept answering every question with a crab-ital letter.
- **On-screen text:** CRAB-ITAL LETTERS
- **Caption + hashtags:** Groan now, laugh later. #programmerhumor #cprogramming #kodingkonkani #codingjokes

**S5 · The mystery space** — 0:35 · built from scenes 10–11

- **Hook (first 1.5s):** `scanf(" %c")` with the space circled in red: "Why is this here?"
- **Script:** Quiz. Why is there a space before percent c? Three, two, one. When you press Enter, a hidden newline character stays behind. Without the space, the next percent c reads that newline and skips your question. The space tells scanf to skip whitespace first. Now your challenge: add three more questions and score out of 5. Answer in the comments.
- **On-screen text:** WHY THE SPACE?
- **Caption + hashtags:** One space that saves your whole program. #cprogramming #codingquiz #kodingkonkani #learntocode #scanf
