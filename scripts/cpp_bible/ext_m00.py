"""Longer narration for module 0 (EP 1-4). Each text is added to the end of the matching text in m00.py.

Keys: intro, concept, A, ill, B, term, bug, hint (hint goes into the challenge scene).
Rules: docs/cpp-bible/STE.md. Cues [HL n] point at lines of the code file for that scene.
"""
EXT = {
    1: dict(
        concept="Why does the computer need a compiler? A processor understands only tiny steps made of ones and zeros. "
                "Your text is easy for you to read, but it is hard for the processor. The compiler is the translator between the two.\n"
                "Bjarne Stroustrup created C plus plus. He started in nineteen seventy-nine and gave it the name in nineteen eighty-three. "
                "The language still grows, and a new version arrives about every three years. Banks, games, cars and rockets run on C plus plus code.",
        A="[HL 1] Think of the include line as a loan from a library. Without it, the computer does not know the word cout. "
          "[HL 3] The word int before main means that the function gives back a whole number when it ends. "
          "[HL 4] Look at the arrows. They point from the text toward cout, as if you push the words onto the screen. "
          "Double quotes hold the text exactly as you type it, so every space and every letter counts. "
          "[HL 5] The value zero is a polite message to the operating system. Any other number tells it that something went wrong.",
        ill="Notice that most mistakes appear in the compile step. The compiler checks every line before it builds the program. "
            "If it finds a mistake, it stops and tells you which line to fix. The run step is quick, because the program is already built. "
            "Remember the order. Write, compile, run.",
        B="[HL 4] Each cout line is one statement, and each statement ends with a semicolon. "
          "[HL 5] Order matters here. If you swap these two lines, the sign-off prints first. "
          "Try it yourself after the video. Swap the lines, compile again, and watch the output change.",
        term="Each endl moves the cursor to the next line, so the two messages do not join together.",
        bug="Here is a tip for reading errors. Read the message from the top. The first line names the file and the line number. "
            "The compiler often points to the line after the real mistake. It notices the problem only when the next statement starts. "
            "So when you see an error, look at the line above it too.",
        hint="Hint: use one cout line for each line of output, and end each line with endl.",
    ),
    2: dict(
        concept="Here is how the three tools work together. First, you open the editor and type your code. Then you save the file with the dot cpp ending. "
                "Next, you open the terminal in the same folder. There you run the compiler on your file.\n"
                "If the compiler finds no mistakes, it creates a program. Then you run that program from the terminal. "
                "On Windows, we get the compiler from M S Y S two. Linux users often have g plus plus ready already.",
        A="[HL 4] Notice that all three lines look the same. Only the words inside the quotes change. "
          "[HL 5] This is the pattern of a first program. You write one statement for each message. "
          "[HL 6] If a line is missing in your output, check the semicolon and the closing quote. "
          "[HL 7] The return line stays at the end of main.",
        ill="Pick one editor and stay with it for the whole course. Visual Studio Code is free, and it works on Windows, Mac and Linux. "
            "The terminal must know where the compiler lives on your computer. If the terminal says command not found, this is the usual reason. "
            "Close the terminal, open it again, and try once more.",
        B="The compiler fills in this number by itself. You never type it. Each language version has its own code, so you can always check which version the compiler uses. "
          "If you forget the flag, the compiler may use a different version, and some new features will not work.",
        term="If the program prints a different number, check how you spelled the flag.",
        bug="Think of an include line as packing your bag for school. If you forget the iostream book, cout is not in your bag. "
            "The compiler cannot guess where cout lives, so it stops. "
            "Remember this rule. If a message says not declared or not a member, check your include lines first.",
        hint="Hint: after every change, compile again before you run the program.",
    ),
    3: dict(
        concept="Bjarne Stroustrup built C plus plus on top of C, because C is fast. He wanted to keep that speed and add tools for big programs. "
                "That is why a lot of old C code still compiles in C plus plus.\n"
                "But C plus plus is not only C with extra parts. It has its own style, and good C plus plus code looks different from C code. "
                "In this episode, we compare the two styles side by side.",
        A="[HL 1] The name cstdio starts with the letter c. In C plus plus, a header from C gets a c in front. It also loses the dot h. "
          "[HL 4] The printf function needs a format string. Here, the format string is plain text with a new line at the end. "
          "[HL 5] Nothing else changes in main. This is why many C programs still run as C plus plus.",
        ill="Do not worry if the table feels long. You do not need to learn it by heart now. Each row gets its own episode. "
            "For now, remember the big idea. C plus plus gives you safer and shorter ways to do the same jobs. You can still use the C way when you need it.",
        B="[HL 1] This time, we include iostream instead of cstdio. "
          "[HL 4] Cout does not need a format string. You push the text into it with the arrows, and you can add more pieces with more arrows. "
          "Later, we chain values this way, and you will see why it is handy.",
        term="The C style and the C plus plus style print the same text. The difference is in how you write it.",
        bug="The name cout lives inside std. The compiler looks in the global space first, and it finds nothing. "
            "Many beginners meet this error in the first week, so do not worry. The fix is a small prefix. "
            "You will type std colon colon many times, and soon it feels natural.",
        hint="Hint: printf needs the header cstdio, and cout needs the header iostream.",
    ),
    4: dict(
        concept="Let us look at each part in more detail. Comments help you and other people read the code later. "
                "Good programmers write comments that explain why, not what.\n"
                "The include line asks the compiler to read a library first. The main function is the front door of the program. "
                "The statements inside it run in order, from top to bottom. The close brace is the last piece.",
        A="[HL 1] A comment can say who wrote the program or what it does. "
          "[HL 5] The comment at the end of this line explains the statement. Use comments with care. Too many comments make code harder to read. "
          "[HL 6] The return statement is optional in main, but we write it so the ending is clear. "
          "[HL 7] Always match every open brace with a close brace.",
        ill="Notice the order from top to bottom. A comment can go anywhere, but the include line must come before the code that uses it. "
            "The main function holds the statements. Return is the last statement. If you keep this order, your programs stay easy to read.",
        B="[HL 2] A using line saves typing in small programs. But two libraries can use the same name for different things. "
          "Then the compiler cannot tell which one you mean. That is why big projects keep the std prefix. "
          "[HL 5] For now, both styles are fine.",
        term="The compiler treats both styles in the same way, so choose the one that is clear to you.",
        bug="Braces come in pairs, like the two covers of a book. When a close brace is missing, the compiler keeps reading until the file ends. "
            "Then it complains about the end of input. If you see that message, count your braces. "
            "Many editors highlight the matching brace when you click on one, and that helps a lot.",
        hint="Hint: write the comment first, then the include line, then main.",
    ),
}
