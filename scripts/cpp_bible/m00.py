"""Module 0 — Meet C++ (EP 1-4)."""
from lib import flow, table

MODULE = {"id": 0, "name": "Meet C++", "range": "1–4", "colours": "Peach + Tomato", "bg": "peach"}
NEXT_AFTER = ("Next: EP 05 · Variables and types", "We end module zero here. Next time: variables and types.")
EPISODES = []

EPISODES.append(dict(
    n=1, title="Hello, C++!", spoken="your first program, hello C plus plus", yt="Your First C++ Program: Hello, World",
    thumb="HELLO, C++!", vis="a glowing screen that says Namaskar, Goa!",
    goals=["say what C++ is", "write a five-line program", "print text with cout"],
    tags=["hello world c++", "first c++ program", "what is c++", "cout"],
    analogy="a recipe: you write the steps, the cook follows them",
    c_pts=["C++ is a programming language", "A compiler turns your text into a program", "Games, browsers and apps use C++"],
    hook="Five lines of code can say hello to Goa.",
    intro="Today you write your first C plus plus program. It has only five lines. At the end, your computer says hello to Goa.",
    concept="C plus plus is a programming language. You write instructions in a text file. The computer cannot read that file directly.\n"
            "A tool called a compiler changes your text into a program. Then the computer can run it. Games, web browsers and phone apps use C plus plus. "
            "Think of a recipe. You write the steps, and the cook follows them.",
    A=dict(file="hello.cpp", label="Your first program", on="a five-line program that prints Namaskar, Goa!",
           src='''
#include <iostream>

int main() {
    std::cout << "Namaskar, Goa!" << std::endl;
    return 0;
}
''',
           narr="[HL 1] This line adds the iostream header. It gives us cout, the tool that prints text. "
                "[HL 3] Every program has a function called main. The computer starts here. "
                "[HL 4] This line prints the words Namaskar, Goa. Text goes inside double quotes. The word endl ends the line. "
                "[HL 5] Return zero tells the computer that all is well. [HL 6] The closing brace ends main."),
    ill=dict(label="Write, compile, run", on="three steps: write the code, compile it, run the program",
             data=flow([("Write", "Type the code in hello.cpp"), ("Compile", "g++ builds a program"), ("Run", "The screen shows Namaskar, Goa!")]),
             narr="Here is the full journey. First, you write the code in a text file. Second, the compiler turns the text into a program. "
                  "Third, you run the program, and the words appear on the screen. You repeat these three steps in every episode."),
    B=dict(file="twolines.cpp", label="Two lines", on="two cout lines run from top to bottom",
           src='''
#include <iostream>

int main() {
    std::cout << "I am learning C++." << std::endl;
    std::cout << "Keep coding, says Xecxec!" << std::endl;
    return 0;
}
''',
           narr="[HL 4] The first cout prints a line about you. [HL 5] The second cout prints our sign-off. "
                "The computer runs the lines in order, from top to bottom. [HL 6] Then main returns zero and the program ends."),
    term="The two lines appear, one under the other.",
    recap=["C plus plus is a language that you compile.", "Every program starts in a function called main.",
           "The tool cout prints text to the screen.", "You write, compile and run, in that order."],
    bug=dict(title="A missing semicolon", file="hello.cpp", kind="compile", wrong_note="the cout line has no semicolon",
             wrong='''
#include <iostream>

int main() {
    std::cout << "Namaskar, Goa!" << std::endl
    return 0;
}
''', fixed_note="the semicolon is back",
             fixed='''
#include <iostream>

int main() {
    std::cout << "Namaskar, Goa!" << std::endl;
    return 0;
}
''',
             why="A semicolon ends a statement. Without it, the compiler cannot see where one instruction stops.",
             narr="Bug of the Day. Here the cout line has no semicolon at the end. The compiler stops and shows an error. "
                  "It says expected semicolon before return. Every statement in C plus plus must end with a semicolon. Add it, and the program builds."),
    pun="I told my compiler a joke. It said, I do not get it. Expected semicolon.",
    task="print your name and your village", challenge="Write a program that prints your name on one line and your village on the next line.",
    answer="Use two cout lines, each with endl at the end. For example, print Asha on the first line and Mapusa on the second.",
))

EPISODES.append(dict(
    n=2, title="Setting up and compiling", spoken="setting up and compiling", yt="C++ Setup on Windows: VS Code and GCC",
    thumb="SET UP C++", vis="three tool cards: editor, compiler, terminal",
    goals=["name the three tools you need", "compile a file with g++", "run the program you built"],
    tags=["install c++ windows", "g++ compile", "vs code c++", "msys2 gcc"],
    analogy="a kitchen: the editor is the notebook, the compiler is the stove, the terminal is the table",
    c_pts=["An editor is where you type code", "A compiler builds the program", "A terminal runs commands"],
    hook="Three tools are all you need to write C plus plus.",
    intro="Today we set up your computer. You need only three tools. By the end, you build and run a real program.",
    concept="You need three tools. The editor is where you type your code. We use Visual Studio Code.\n"
            "The compiler builds your program. We use g plus plus, from the GCC family. The terminal is where you type commands and run programs. "
            "Think of a kitchen. The editor is the notebook with the recipe. The compiler is the stove. The terminal is the table where you eat.",
    A=dict(file="setup.cpp", label="A setup check", on="a program that prints three ready messages",
           src='''
#include <iostream>

int main() {
    std::cout << "Editor: ready" << std::endl;
    std::cout << "Compiler: ready" << std::endl;
    std::cout << "Terminal: ready" << std::endl;
    return 0;
}
''',
           narr="Type this program in your editor and save it as setup dot cpp. "
                "[HL 4] The first line of main reports on the editor. [HL 5] The second line reports on the compiler. [HL 6] The third line reports on the terminal. "
                "If you see all three lines at the end, your setup works."),
    ill=dict(label="Three tools", on="a table: tool, job and example",
             data=table(["Tool", "Job", "Example"], [["Editor", "You type code", "VS Code"], ["Compiler", "Builds the program", "g++"], ["Terminal", "Runs commands", "PowerShell"]]),
             narr="Look at the table. The editor lets you type and save code. The compiler reads your file and builds a program. "
                  "The terminal lets you type the compile command and run the result. Every episode uses all three."),
    B=dict(file="standard.cpp", label="Which C++ version?", on="a program that prints the language version code",
           src='''
#include <iostream>

int main() {
    std::cout << "Language version code: " << __cplusplus << std::endl;
    return 0;
}
''',
           narr="[HL 4] A built-in name holds a number for the language version. The name starts with two underscores, then c plus plus. "
                "With the flag std equals c plus plus twenty, the number is two zero two zero zero two. "
                "That number means C plus plus twenty. We use this version in the whole course."),
    term="Type g plus plus, then the flags dash std equals c plus plus twenty, dash Wall and dash Wextra. The program prints the version code.",
    recap=["You need an editor, a compiler and a terminal.", "The command g plus plus builds your file into a program.",
           "The flag dash Wall shows helpful warnings.", "Always compile again after you change the code."],
    bug=dict(title="A missing include", file="setup.cpp", kind="compile", wrong_note="the include line for iostream is missing",
             wrong='''
int main() {
    std::cout << "Editor: ready" << std::endl;
    return 0;
}
''', fixed_note="the include line is back",
             fixed='''
#include <iostream>

int main() {
    std::cout << "Editor: ready" << std::endl;
    return 0;
}
''',
             why="The compiler only knows cout after you include the iostream header. Add the include line at the top of the file.",
             narr="Bug of the Day. Here the include line is missing. The compiler says cout is not a member of std. "
                  "It even tells you what to do. It asks if you forgot to include iostream. Add the include line at the top, and the error goes away."),
    pun="Why did the programmer install three tools? Because two was a bug, and four was a feature.",
    task="compile and run setup dot cpp", challenge="Type setup dot cpp, compile it with g plus plus, and run it. Then change one message and compile again.",
    answer="Run g plus plus with the file name and dash o setup. Then type dot slash setup. After a change, you must compile again.",
))

EPISODES.append(dict(
    n=3, title="C vs C++: what changed", spoken="what changed from C to C plus plus", yt="C vs C++: What Changed?",
    thumb="C VS C++", vis="two signs: a C sign and a C++ sign",
    goals=["name four differences between C and C++", "print with cout instead of printf", "use std:: in front of library names"],
    tags=["c vs c++", "difference between c and c++", "printf vs cout", "std namespace"],
    analogy="a bicycle and a motorbike: both carry you, but one has more features",
    c_pts=["C++ grew out of C", "C++ adds classes and a bigger library", "Most C code still works in C++"],
    hook="C plus plus is C with superpowers.",
    intro="Today we compare C and C plus plus. You will see what stayed the same, and what is new.",
    concept="C plus plus grew out of the C language. Most C code still works in C plus plus. "
            "But C plus plus adds many features. It has classes, a bigger library, and safer ways to handle memory.\n"
            "Think of a bicycle and a motorbike. Both carry you to school. The motorbike has more parts, so you must learn more.",
    A=dict(file="cstyle.cpp", label="The C way", on="printf prints text, as in C",
           src='''
#include <cstdio>

int main() {
    std::printf("Hello from C style\\n");
    return 0;
}
''',
           narr="[HL 1] The header cstdio gives us printf, the C way to print. "
                "[HL 4] Printf works in C plus plus too. The backslash n at the end starts a new line. "
                "Notice the prefix std colon colon. C plus plus keeps its library names inside the std namespace."),
    ill=dict(label="C and C++ side by side", on="a table: feature, C way, C++ way",
             data=table(["Feature", "C", "C++"], [["Print", "printf", "std::cout"], ["Read", "scanf", "std::cin"], ["Text", "char array", "std::string"],
                                                  ["Memory", "malloc and free", "new, delete, smart pointers"], ["Grouping", "struct", "class"]]),
             narr="Here are five differences. For printing, C uses printf, and C plus plus uses cout. For reading, C uses scanf, and C plus plus uses cin. "
                  "For text, C uses char arrays, and C plus plus has std string. For memory, C plus plus gives you smart pointers. "
                  "For grouping data, C plus plus has classes. We will learn each one."),
    B=dict(file="cppstyle.cpp", label="The C++ way", on="cout prints text, as in C++",
           src='''
#include <iostream>

int main() {
    std::cout << "Hello from C++ style" << std::endl;
    return 0;
}
''',
           narr="[HL 4] Now the C plus plus way. The cout tool takes the text with the insertion operator, which looks like two arrows. "
                "The endl word ends the line. [HL 5] The program returns zero, as before. Both styles give the same result on the screen."),
    term="Both programs print one hello line. C plus plus lets you choose either style.",
    recap=["C plus plus grew out of C.", "Printf is the C way, and cout is the C plus plus way.",
           "Library names live in the std namespace.", "C plus plus adds classes, strings and smart pointers."],
    bug=dict(title="Forgetting std", file="cppstyle.cpp", kind="compile", wrong_note="cout has no std prefix",
             wrong='''
#include <iostream>

int main() {
    cout << "Hello from C++ style" << std::endl;
    return 0;
}
''', fixed_note="std colon colon is back",
             fixed='''
#include <iostream>

int main() {
    std::cout << "Hello from C++ style" << std::endl;
    return 0;
}
''',
             why="Library names such as cout live in the std namespace. Write std colon colon in front, or use a using line, which we learn soon.",
             narr="Bug of the Day. Here we write cout without std in front. The compiler says cout was not declared in this scope. "
                  "It also suggests std colon colon cout. Library names live in the std namespace. Add the prefix, and the error goes away."),
    pun="Why did C plus plus not invite C to the party? C said, I will be there, but only as a subset.",
    task="print with printf and cout in one program", challenge="Write one program that prints one line with printf and one line with cout.",
    answer="Include both cstdio and iostream. Call std printf with a backslash n, then use std cout with endl.",
))

EPISODES.append(dict(
    n=4, title="Anatomy of a C++ program", spoken="the parts of a C plus plus program", yt="Anatomy of a C++ Program",
    thumb="PARTS OF C++", vis="a program cut into labelled parts, like a fish diagram",
    goals=["name the parts of a small program", "write comments", "use a using line to shorten names"],
    tags=["structure of c++ program", "c++ comments", "using namespace std", "main function"],
    analogy="a thali: every dish has its own spot on the plate",
    c_pts=["Comments are notes for people", "Includes bring in library tools", "Main is where the program starts"],
    hook="Every C plus plus program has the same parts.",
    intro="Today we cut a program into parts, like a fish on a plate. You will name every part.",
    concept="Every C plus plus program has the same parts. A comment is a note for people. The compiler ignores it.\n"
            "An include line brings in library tools. The main function is where the program starts. Statements do the work, and each ends with a semicolon. "
            "Think of a thali. Each dish has its own spot on the plate.",
    A=dict(file="parts.cpp", label="Name the parts", on="a small program with a comment on every important line",
           src='''
// A small program
#include <iostream>

int main() {
    std::cout << "Anatomy lesson" << std::endl;  // print a line
    return 0;
}
''',
           narr="[HL 1] The two slashes start a comment. The compiler skips it. [HL 2] The include line brings in iostream. "
                "[HL 4] The main function starts here, and the open brace starts its body. [HL 5] This statement prints a line. A comment can also sit at the end of a line. "
                "[HL 6] The return statement ends the program. [HL 7] The close brace ends main."),
    ill=dict(label="The parts in order", on="five parts of a program, from top to bottom",
             data=flow([("Comment", "A note for people"), ("Include", "Brings in iostream"), ("main", "The program starts here"),
                        ("Statement", "Does one job, ends with a semicolon"), ("return", "Gives zero back")]),
             narr="Here are the parts in order. First, the comment. Second, the include line. Third, the main function. "
                  "Inside main, the statements do the work. At the end, return sends zero back to the computer. Every program you write follows this shape."),
    B=dict(file="shortnames.cpp", label="A using line", on="using namespace std shortens every name",
           src='''
#include <iostream>
using namespace std;

int main() {
    cout << "Short names work now." << endl;
    return 0;
}
''',
           narr="[HL 2] This using line tells the compiler to look inside std. [HL 5] Now we can write cout and endl without the prefix. "
                "The program is shorter. In big projects, the prefix is safer, so we use both styles in this course. [HL 6] The return statement is the same as before."),
    term="The program prints one line. The output is the same as with std colon colon.",
    recap=["A comment is a note for people.", "The include line brings in library tools.",
           "Main is where the program starts.", "A using line lets you drop the std prefix."],
    bug=dict(title="A missing closing brace", file="parts.cpp", kind="compile", wrong_note="the closing brace of main is missing",
             wrong='''
#include <iostream>

int main() {
    std::cout << "Anatomy lesson" << std::endl;
    return 0;
''', fixed_note="the closing brace is back",
             fixed='''
#include <iostream>

int main() {
    std::cout << "Anatomy lesson" << std::endl;
    return 0;
}
''',
             why="Every open brace needs a close brace. The compiler reaches the end of the file and still waits for the last one.",
             narr="Bug of the Day. Here the closing brace of main is missing. The compiler reads to the end of the file. "
                  "Then it says expected close brace at end of input. Every open brace needs a close brace. Add it, and the program builds."),
    pun="My program has a comment, an include, and a main. It is a very well-balanced meal.",
    task="label the parts of your own program", challenge="Write a program with one comment, one include line and one cout. Add a comment at the end of the cout line.",
    answer="Start with a double slash comment. Add the include line for iostream. Write main with a cout line, then add a double slash comment after the semicolon.",
))
