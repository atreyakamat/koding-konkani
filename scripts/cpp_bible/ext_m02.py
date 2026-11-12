"""Longer narration for module 2 (EP 13-20). Each text is added to the end of the matching text in m02.py.

Keys: intro, concept, A, ill, B, term, bug, hint (hint goes into the challenge scene).
Rules: docs/cpp-bible/STE.md. Cues [HL n] point at lines of the code file for that scene.
"""
EXT = {
    13: dict(
        concept="Every program you use makes decisions. A phone checks the password before it opens. A bank app checks your balance before it pays. "
                "All of this starts with a plain if.\n"
                "The curly braces hold the body of each branch. Even for one line, write the braces. They stop many mistakes when you add a second line later.",
        A="[HL 6] The test must give true or false. Here, the comparison gives a bool, and that is exactly what if needs. "
          "[HL 7] This line runs only when the test is true. Our marks are above thirty-five, so the program prints Pass. "
          "[HL 8] Notice that else has no test of its own. It means, in all other cases. "
          "[HL 9] Change marks to thirty, and this line runs instead.",
        ill="Notice that only one path runs in each run of the program. The other path stays silent, and the computer does not even look at it. "
            "A tree like this is a good way to plan code before you type it.",
        B="[HL 7] The remainder of a number divided by two tells us if the number is even. "
          "Every even number gives zero, and every odd number gives one. "
          "[HL 10] You can use this trick for any test on odd and even, such as seats in a bus.",
        term="Try more numbers. Type ten, and then type zero. Zero is even, because the remainder is zero.",
        bug="This mistake is hard to see, because the code looks almost right. The semicolon ends the if statement early. "
            "The braces then belong to nothing, and they run every time. So read every if line slowly, and look at the end of the line.",
        hint="Hint: the test is the number greater than zero, and the else branch covers zero and all negative numbers.",
    ),
    14: dict(
        concept="Why a ladder, and not many separate ifs? With separate ifs, every test runs, and more than one message may print. "
                "With a ladder, the program stops at the first true test.\n"
                "The final else is optional. But it is a good habit. It tells the reader what happens when nothing else fits.",
        A="[HL 6] The strictest test goes first. A mark of ninety or more gets the top grade. "
          "[HL 8] We reach this test only if the first one was false. So we already know that marks are below ninety. "
          "[HL 10] The same idea repeats. Each rung only needs the lower limit. "
          "[HL 13] If every test fails, the final else runs, and it prints Grade D.",
        ill="Notice how the bands cover all numbers with no gap. Every mark from zero to one hundred lands in exactly one band. "
            "When you write a ladder, check the edges by hand. Test ninety, test eighty-nine, and test zero.",
        B="[HL 6] The price starts with no value, and one branch gives it a value. Every branch must set the price, or the program prints garbage. "
          "[HL 9] Children from five to seventeen pay fifty. "
          "[HL 13] The final else covers all ages from sixty up. That is why we do not need a test there.",
        term="Try the age ten, and then the age four. Each age falls into a different band.",
        bug="Read the ladder like the computer does. It checks from the top, and it stops at the first true test. "
            "A loose test at the top catches everything below it. So put the hardest test first, and the easiest test last.",
        hint="Hint: test the highest temperature first, and let the final else print cool.",
    ),
    15: dict(
        concept="Use a switch when you compare one value with many fixed choices. The code is shorter than a long ladder, and it is easier to read. "
                "But a switch works only with whole numbers and characters. It cannot compare text or decimals.\n"
                "The break keyword is the most important part. Without it, the program keeps running into the next case.",
        A="[HL 6] The switch looks at day only once. Then it jumps straight to the right label. "
          "[HL 9] A match prints Wednesday. The break on the same line jumps out of the switch. "
          "[HL 10] The default case is last. It has no break, because nothing follows it. "
          "Always write a default case. It tells the reader that you thought about the other values.",
        ill="Notice that the table has one row for each label. The switch reads the value, finds its row, and runs the code from that row down to the first break. "
            "That last part is the key. Remember it when you see fall-through.",
        B="[HL 7] A case label with no code under it falls through on purpose. Two letters share one action. "
          "This is the one time when missing break is useful. "
          "[HL 13] Add a comment when you do this, so the next reader knows it is on purpose.",
        term="Try the capital letter B as well. It must print Buy too.",
        bug="Fall-through is a feature, but it surprises beginners. The program runs every line from the matching case until it finds a break. "
            "Turn on warnings with the Wall flag, and the compiler tells you when a break is missing.",
        hint="Hint: use the char type for the choice, and print one result in each case.",
    ),
    16: dict(
        concept="Loops save you from typing the same line again and again. If you must print one thousand lines, you write one loop. "
                "The computer does the repeating, and it never gets tired.\n"
                "Every loop needs three things. A start value, a test, and a change. If one of the three is missing, the loop breaks.",
        A="[HL 5] This is the start value. Without it, the test has nothing to look at. "
          "[HL 6] The test runs first. If it is false at the start, the body never runs at all. "
          "[HL 8] This line is the change. Remove it, and n stays three forever. The loop then never ends. "
          "[HL 10] After the loop, the program carries on with the next line.",
        ill="Notice that the test runs four times, but the body runs only three times. The last test is the one that fails. "
            "This detail explains many off-by-one mistakes, so remember it.",
        B="[HL 8] The plus-equals line adds the current value of i to the sum. "
          "The sum grows by one, then two, then three, then four, then five. "
          "[HL 9] Without this line, the loop never ends, and the program hangs. If that happens, press control and C to stop it.",
        term="You can check this sum with a trick. One plus five is six, two plus four is six, and three stays. Six, six and three give fifteen.",
        bug="Always test the first round and the last round by hand. For the first round, i is one. For the last round, you want i to be five. "
            "If the test says less than five, then i is never five in the body. That is the whole bug.",
        hint="Hint: start the counter at one, and print two times the counter.",
    ),
    17: dict(
        concept="A for loop puts the start, the test and the step in one line. That keeps all the loop rules in one place. "
                "When you read the first line, you already know how many times it runs.\n"
                "Use a for loop when you know the count. Use a while loop when you wait for something to happen.",
        A="[HL 5] Read the first line as a sentence. Start at one, go on while i is at most five, and add one after each round. "
          "[HL 6] The variable i is a box that lives only inside the loop. After the loop, it is gone. "
          "The name i is the usual name for a counter, so other programmers will understand it at once.",
        ill="Notice that the test happens before the body. If the test is false the first time, the body never runs. "
            "The step happens after the body, and right before the next test.",
        B="[HL 5] This loop starts at one and goes up to five. Each round prints one row of the table. "
          "[HL 8] A loop can also count down. It starts high, and the step takes one away. "
          "[HL 9] The test says k is at least one, so the loop stops when k reaches zero.",
        term="Check the third row of the table by hand. Seven times three is twenty-one.",
        bug="This mistake looks harmless, and the compiler usually warns about it. The semicolon makes the loop body empty. "
            "So the loop spins, and nothing happens. Then your block runs once, with the counter at six. Read the end of every for line.",
        hint="Hint: start at two, and let the step add two each time.",
    ),
    18: dict(
        concept="Why use this loop? It is safe. You cannot count one too many, and you cannot start at the wrong place.\n"
                "Use a normal for loop when you need the position of an item. Use the range-based loop when you only need the item itself.",
        A="[HL 7] Read the colon as the word in. For each char c in word. "
          "The loop takes one letter at a time, from the first to the last. "
          "[HL 10] The curly braces make a small list of numbers right inside the loop line. "
          "The loop visits them in the same order as you wrote them.",
        ill="Notice what is missing. There is no counter, no test and no step. The loop does all three jobs by itself. "
            "That is why it is shorter, and why it has fewer places for a mistake.",
        B="[HL 9] The or operator joins five tests. If any of them is true, the letter is a vowel. "
          "This list is a little long, but it is clear. In a later episode, we shorten it with a string search. "
          "[HL 10] The count grows only when a vowel appears.",
        term="Try your own name next. Count the vowels by hand first, and then compare with the program.",
        bug="Remember what a copy means. A copy is a second box with the same value. When you change the copy, the original box does not feel it. "
            "An ampersand makes a nickname instead. The nickname and the real letter are one and the same box.",
        hint="Hint: compare each letter with the character a inside the loop, and add one to a counter.",
    ),
    19: dict(
        concept="Use break when you found what you were looking for. There is no reason to keep searching. "
                "Use continue when one item does not fit, and you want to skip it.\n"
                "Break and continue affect only the loop they sit in. In a nested loop, they touch the inner loop only.",
        A="[HL 5] The loop would run twenty-one times, from ten to thirty. "
          "[HL 6] But we want only the first multiple of seven, so we stop early. "
          "[HL 8] Break saves time. In a big list, this can save millions of steps. "
          "[HL 11] This line runs after the loop ends, whether the loop ended by break or by the test.",
        ill="Notice the picture. Break jumps out of the loop to the code below it. Continue jumps back up to the start of the next round. "
            "The step of a for loop still runs after continue, so the counter keeps growing.",
        B="[HL 6] The test is true only for the number three. "
          "[HL 7] Continue jumps to the step of the loop, so i becomes four. "
          "The print line below is skipped for this round only. All the other rounds print normally.",
        term="Look for the gap in the output. After two, the next number is four.",
        bug="The two keywords sound alike, but they do different jobs. Think of the bus. Break means the bus ends its trip. "
            "Continue means the bus skips one stop and drives on. Choose the one that matches your plan.",
        hint="Hint: test the multiple of three with the remainder operator, and use continue.",
    ),
    20: dict(
        concept="Nested loops build tables, grids and patterns. A chess board is eight rows with eight columns. A seat plan in a cinema works the same way.\n"
                "Count the work. If the outer loop runs four times and the inner loop runs four times, the body runs sixteen times. "
                "Nested loops grow fast, so be careful with big numbers.",
        A="[HL 5] The outer loop runs four times, one time for each row. "
          "[HL 6] The inner loop starts again from one for every new row. Its limit is the row number, so each row is one star longer. "
          "[HL 7] The body prints one star and no line break, so the stars stay on the same line. "
          "[HL 9] The line break belongs to the outer loop. It runs once for each row.",
        ill="Notice the shape of the table. The number of stars equals the row number. "
            "To plan a pattern, write the rows on paper first. Then find the rule that links the row number to the count.",
        B="[HL 5] Think of r as the row and c as the column. "
          "[HL 7] Every cell holds the product of its row and its column. This is a small multiplication table. "
          "[HL 9] Always check that the line break is in the right loop.",
        term="Check the corner cell. Row three and column three give nine.",
        bug="The two loops look alike, so it is easy to put the line break in the wrong place. "
            "Look at the braces. The line break belongs after the inner loop, and before the closing brace of the outer loop. "
            "Many editors show you which brace closes which loop.",
        hint="Hint: the inner loop prints the row number, and endl goes after the inner loop.",
    ),
}
