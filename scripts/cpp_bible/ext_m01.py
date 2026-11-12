"""Longer narration for module 1 (EP 5-12). Each text is added to the end of the matching text in m01.py.

Keys: intro, concept, A, ill, B, term, bug, hint (hint goes into the challenge scene).
Rules: docs/cpp-bible/STE.md. Cues [HL n] point at lines of the code file for that scene.
"""
EXT = {
    5: dict(
        concept="Why does C plus plus ask for a type at all? The type tells the compiler how much room the box needs. "
                "It also tells the compiler what the bits inside mean. The same bits can be a number or a letter, so the type decides.\n"
                "A good name helps as much as a good type. Write fish count, not x. When you read the code next month, the name tells you the story.",
        A="[HL 5] Read this line from left to right. The type is int, the name is fish, and the value is three. The equals sign here puts the value into the box. "
          "[HL 7] A char holds exactly one letter, so we use single quotes. Double quotes are for whole words, and they mean a different type. "
          "[HL 8] Bool prints as one for true and zero for false, unless you ask for words. "
          "[HL 12] So the last line prints the number one on your screen.",
        ill="Notice that two variables never share a box. Each name has its own address. "
            "The address is where the box starts in memory. The computer reads exactly as many bytes as the type needs, and then it stops.",
        B="[HL 5] The sizeof operator does not run any code at all. The compiler works out the answer while it builds the program. "
          "The numbers four and eight are common, but the language does not promise them for every computer. "
          "Use sizeof when you need to be sure on your own machine.",
        term="Your numbers may differ on another computer, but these four are normal on a modern laptop.",
        bug="Garbage values are tricky, because the program may print zero on one run and a strange number on the next. "
            "That makes the bug hard to catch. So make it a habit. Whenever you write a variable, write its first value in the same line.",
        hint="Hint: pick one type for each value. A height has decimals, so it is a double.",
    ),
    6: dict(
        concept="Think about what the program does while it waits. It stops at the cin line and does nothing else. "
                "The keyboard fills a small buffer, and cin reads from that buffer when you press Enter.\n"
                "Cin skips spaces and new lines before a number. That is why you can type the numbers on one line or on two lines. "
                "Both ways work the same.",
        A="[HL 5] The variable age has no value yet, but cin gives it one on line seven, so this is safe. "
          "[HL 6] A good program always tells the user what to type. Without the question, the user only sees a blinking cursor. "
          "[HL 7] If you type a word instead of a number, cin fails, and age gets no good value. We handle that later in the course. "
          "[HL 8] The plus one happens first, and then cout prints the result.",
        ill="Notice that the flow goes in one direction only. The keyboard sends characters, and cin turns them into a number. "
            "The number lands in the variable. After that, the variable is an ordinary box, and you can use it as often as you like.",
        B="[HL 6] The prompt says two numbers, so the user knows what to do. "
          "[HL 7] The arrows can chain. Each pair of arrows reads one value, from left to right. "
          "Cin splits the input at the spaces, so one space, a tab or a new line all work.",
        term="Try a few more pairs yourself. Type two large numbers, and check the sum with a calculator.",
        bug="This error message is long, but the cause is short. The compiler tries every version of the arrows it knows, and none fits. "
            "So it lists them all. Skip the list. Read only the first line, and look at the arrows in your own code.",
        hint="Hint: read the length and the width first, then multiply them in the cout line.",
    ),
    7: dict(
        concept="The order of the operators matters. Times, divide and remainder go first. Plus and minus come after. "
                "So two plus three times four gives fourteen, not twenty.\n"
                "Use brackets when you want to be clear. Brackets always go first. A short, clear line is better than a clever line that nobody can read.",
        A="[HL 5] We can make two variables in one line, if they have the same type. "
          "[HL 9] Integer divide gives only the whole part. Seventeen divided by five is three point four, and the point four is cut. "
          "[HL 10] The remainder operator works only with ints. Programmers use it to test for even numbers and to wrap around a clock. "
          "Remember this pair. Divide gives the groups, and remainder gives the leftovers.",
        ill="Notice how divide and remainder work as a team. Three groups of five make fifteen, and two more make seventeen. "
            "If you ever doubt the answer, multiply the divide result by the second number, and add the remainder. You must get the first number back.",
        B="[HL 6] The plus-equals operator is a short way to write visitors equals visitors plus five. "
          "[HL 7] The plus-plus operator is the short way to add one. You will see it in every loop later. "
          "[HL 9] Compare this line with the bug in the next scene. One decimal point changes the whole answer.",
        term="Check the first number. Ten plus five plus one is sixteen. Then half of seven is three point five.",
        bug="Many beginners think the compiler is wrong here. It is not. The rule is simple. "
            "If both sides of a divide are ints, the answer is an int. Make at least one side a double, and the answer keeps its decimals.",
        hint="Hint: use the divide operator for the share and the remainder operator for what is left.",
    ),
    8: dict(
        concept="A comparison never changes the values. It only asks a question and gives back true or false. "
                "You can store the answer in a bool variable, or use it directly in an if.\n"
                "Be careful with equal to. It uses two equals signs. One equals sign stores a value, and that is a different job.",
        A="[HL 5] The age is seventeen. [HL 6] The pass is true. "
          "[HL 8] The brackets around the comparison matter. Without them, the arrows of cout would mix with the comparison. "
          "[HL 9] And is strict. If one side is false, the whole answer is false. "
          "[HL 11] The exclamation mark is the not operator. It turns true into false, and false into true.",
        ill="Look at the rows again. For and, you need two yes answers. For or, one yes is enough. "
            "A cinema gate is a good picture. The guard asks for a ticket and the right age, and both must be fine.",
        B="[HL 6] Read this line aloud. The mark is at least zero, and the mark is at most one hundred. "
          "That sounds like normal speech, which makes the code easy to check. "
          "[HL 8] Both bools print as words because of boolalpha.",
        term="Change the mark to one hundred and fifty, and run it again. Then valid turns false.",
        bug="This bug is quiet. The program builds, and it may even run. "
            "But the test is always true or always false, and the wrong branch runs. "
            "Turn on warnings with the Wall flag. Then the compiler tells you about this mistake at once.",
        hint="Hint: use the remainder operator to test for even, and the and operator to join both tests.",
    ),
    9: dict(
        concept="There are two kinds of conversion. The compiler does the first kind by itself, and we call it implicit. "
                "You ask for the second kind with a cast, and we call it explicit.\n"
                "Explicit is better, because the reader can see your intent. A cast says, yes, I know data may change here.",
        A="[HL 6] Seven becomes seven point zero. This conversion is safe, because every int fits inside a double. "
          "[HL 8] This conversion is not safe. The decimals are cut off, not rounded. "
          "Nine point nine nine becomes nine, and the program stays quiet about it. "
          "[HL 9] The first print shows the double with no decimals, because it ends in zero.",
        ill="Notice the direction of each arrow. A small box into a big box is safe. A big box into a small box can lose data. "
            "Think of the jug and the glass again. Water poured from a glass into a jug is never lost.",
        B="[HL 6] Read the cast first. It turns a copy of passed into a double. The original variable does not change. "
          "After that, the double divided by an int gives a double. "
          "[HL 9] The letter A is stored as the number sixty-five. Every letter has its own code number.",
        term="The ratio is zero point eight seven five, because seven out of eight is a little less than one.",
        bug="Think of the order of work. First the division happens, and then the cast. "
            "If the division uses two ints, the damage is done before the cast starts. "
            "So cast one of the numbers first. Then the division already works with doubles.",
        hint="Hint: add the three marks as ints, and cast the sum to a double before you divide.",
    ),
    10: dict(
        concept="Why use const? It protects you from your own mistakes. If a value must never change, say so, and the compiler guards it for you.\n"
                "Auto saves typing, but use it with care. When the type is obvious from the value, auto is fine. When the type is not clear, write it out.",
        A="[HL 5] A const variable must get its value in the same line. You cannot add the value later. "
          "[HL 6] Constexpr goes one step further. The compiler can use the value while it builds, for example to set the size of an array. "
          "[HL 7] Auto looks at the right side of the equals sign. A number with a decimal point is a double. "
          "[HL 8] A plain whole number is an int. [HL 10] An int times a double gives a double, so the answer keeps its decimals.",
        ill="Notice the lock on two of the boxes. The program may read them as often as it likes. "
            "But any line that tries to change them stops the build. Auto boxes have no lock. They are ordinary boxes whose type came from the compiler.",
        B="[HL 5] Constants have names, and names tell the story. A reader sees pi and knows what it means at once. "
          "[HL 7] Three variables go into one line, and auto still finds the right type. "
          "Here, every part of the formula is a double, so the area is a double.",
        term="Check the number by hand. Pi times two times two is about twelve point five six.",
        bug="Read the message slowly. It says read-only variable, and it names the variable and the line. "
            "That is all you need. You can fix it in one of two ways. Remove the changing line, or ask yourself why the variable was const in the first place.",
        hint="Hint: the circumference is two times pi times the radius.",
    ),
    11: dict(
        concept="A string is a row of characters, stored one after the other. Because it is a class, it comes with many helpers. "
                "The size function, the find function and the substr function are three of them.\n"
                "You never worry about the memory of a std string. It grows when you add letters, and it cleans up after itself.",
        A="[HL 6] Quotes around the word make a string literal, and the string variable keeps a copy. "
          "[HL 8] Plus joins two strings and gives a new one. The first two stay as they were. "
          "[HL 10] Size counts every character, including spaces. Goa has three letters, the space is one more, and beach has five. "
          "[HL 11] Square brackets pick one letter. Remember that the first letter has index zero.",
        ill="Notice that the numbers under the beads start at zero, and the last index is one less than the size. "
            "This rule causes many mistakes in beginner code. If a string has nine letters, the last index is eight.",
        B="[HL 7] If the word is not in the string, find gives a huge number as a signal. "
          "In a real program, you test for that before you cut. "
          "[HL 9] Substr needs two numbers. The first is where to start, and the second is how many letters to take.",
        term="Count the letters by hand. Goa, a space, is, a space, and then sunny starts at index seven.",
        bug="Think about what the compiler sees. Two quoted texts are two plain arrays of characters. "
            "The plus sign has no meaning for them. Start the chain with a real string, and each plus then works from left to right.",
        hint="Hint: join the strings with plus, and add the spaces yourself.",
    ),
    12: dict(
        concept="The format tools only change how output looks. The numbers themselves stay the same inside the program.\n"
                "Fixed and setprecision stay active until you change them. Setw is different. It works for the next item only, so you repeat it each time.",
        A="[HL 6] You write this line once at the top. Every number after it uses two decimals. "
          "[HL 7] Setw comes before each item, not after it. The name Fish gets eight places, and so does the price. "
          "[HL 8] Both rows line up, because every item has the same width. "
          "[HL 9] A total that lines up is easy to read, and that is what a good bill needs.",
        ill="Notice the two groups in the table. Some tools stay on, like fixed and setprecision. One tool, setw, works for a single item. "
            "That small difference explains most of the surprises in the first week.",
        B="[HL 7] Curly braces are holes, and the values after the pattern fill them in order. "
          "The first hole takes the first value, and the second hole takes the second. "
          "The text outside the braces stays exactly as you wrote it.",
        term="Notice the two zeros after the point. The pattern asked for two decimals, so they stay.",
        bug="Scientific form is a shorthand for big and small numbers. It is correct, but it is hard for a customer to read. "
            "So write fixed first, and setprecision after it. In that order, the number two means two decimals.",
        hint="Hint: set fixed and setprecision once, and use setw before every name and every price.",
    ),
}
