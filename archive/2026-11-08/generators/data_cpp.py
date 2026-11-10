# C++ course, Module 0 (EP1-4)
MOD = dict(module=0, mod_name="Welcome & setup", bgacc="Peach + Tomato")
TC = "Title card"; CS = "Concept slide"; CE = "Code explain"; MB = "Memory boxes"; TM = "Terminal"; BG = "Bug of the Day"; PC = "Pun card"; CH = "Challenge"; OU = "Outro"

def std_scenes(title_line, title_narr, s2, s3, s4, s5, s6, s7, pun, ch, ou):
    return [
        dict(tpl=TC, name="Title", on=f"EP {title_line[0]:02d} · {title_line[1]}", anim="Tomato title card: EP sticker thuds in, title stamps with a whoosh, Xecxec scuttles in and waves; thud, whoosh, claw-click, sting", narr=title_narr, min=15),
        dict(tpl=CS, name=s2[0], on=s2[1], anim=s2[2], narr=s2[3], min=30),
        dict(tpl=CE, name=s3[0], on=s3[1], anim="Code types in with key-tick; butter [HL n] highlight sweeps line by line with marker-swipe; explanation card on the right", narr=s3[2], min=40),
        dict(tpl=s4[4], name=s4[0], on=s4[1], anim=s4[2], narr=s4[3], min=30),
        dict(tpl=CE, name=s5[0], on=s5[1], anim="Same code; the output panel fills line by line with a ding per output line; [TRACK] cards update", narr=s5[2], min=40),
        dict(tpl=TM, name=s6[0], on=s6[1], anim="Dark-blue terminal: the command types with key-tick, output prints in mint with a ding", narr=s6[2], min=20),
        dict(tpl=BG, name=s7[0], on=s7[1], anim="Butter banner drops in with a buzzer; wrong code shakes; the g++ error lines appear in tomato; the fix slides in and the terminal turns mint with a ding", narr=s7[2], min=40),
        dict(tpl=PC, name="Pun", on=pun[0], anim="Full tomato screen, card flips in with a rimshot, Xecxec snaps his claw", narr=pun[1], min=4),
        dict(tpl=CH, name="Challenge", on=ch[0], anim="Task card pops in; checklist ticks with a pop; Xecxec holds a tiny pen", narr=ch[1], min=20),
        dict(tpl=OU, name="Outro", on=ou[0], anim="Next-episode card slides up with a whoosh; right side stays empty for end-screen elements; sign-off text types in", narr=ou[1], min=15),
    ]

EP1_CODE = '''#include <iostream>

int main() {
    std::cout << "Hello, Goa!" << std::endl;
    std::cout << "Keep coding, says Xecxec!" << std::endl;
    return 0;
}'''
EP1_BUG = '''#include <iostream>

int main() {
    std::cout << "Hello, Goa!" << std::endl
    return 0;
}'''
EP1_FIX = EP1_BUG.replace("std::endl\n", "std::endl;\n")

EP1 = dict(ep=1, title="Hello, C++!", prereq="none (the C course helps, but is not required)", **MOD,
 goals=["write and run a first C++ program", "name its three parts: include, main and cout", "know that every statement ends with a semicolon"],
 yt=dict(title="Hello, C++! Your First Program | C++ Programming EP 01",
   desc="Write, compile and run your very first C++ program with Xecxec the crab. No experience needed, just bring curiosity.",
   tags=["c++", "c++ for beginners", "c++ tutorial", "hello world c++", "cout", "koding konkani", "learn programming", "class 11 computer science", "first year engineering", "coding in goa"],
   thumb_text="HELLO, C++!", thumb_visual="in tomato on peach; Xecxec waving a claw at a dark-blue terminal card showing Hello, Goa!; thin black border and drop shadow.",
   chapters={1: "Intro", 2: "What is C++?", 3: "The program line by line", 4: "From code to program", 5: "Run it in your head", 6: "Compile and run", 7: "Bug of the Day", 9: "Challenge", 10: "Next episode"}),
 files=[dict(name="hello.cpp", source=EP1_CODE, scene="3, 5")],
 scenes=std_scenes((1, "HELLO, C++!"),
   "Welcome to Koding Konkani! I am your narrator, and this little crab is Xecxec. In this series you will learn C plus plus, one small idea at a time. Today, we write our very first program.",
   ("What is C++", '"What is C++?": three numbered lines and a fish-curry recipe card on the right', "Lines spring in one by one with a pop; the recipe card slides in from the right",
    "C plus plus is a programming language. You write instructions in plain text. Then a tool called the compiler turns those instructions into a real program. Think of a recipe card for fish curry. The card is your code, and the kitchen is the computer. The card does nothing until someone cooks it."),
   ("The program", "`hello.cpp`: the 7-line first program, line 4 is the star",
    "[HL 1] The first line says, include iostream. It brings in the tools for printing to the screen. [HL 3] Every C plus plus program starts running at main. [HL 4] Here is the star. std colon colon cout sends text to the screen. The two arrows push the text towards it. [HL 5] A second line prints the sign-off. [HL 6] Return zero tells the computer, all went well."),
   ("From code to program", "Three boxes: your code, the compiler, the program; arrows between them",
    "Three boxes appear left to right; arrows draw on between them with a whoosh; a tomato cross pops on the compiler box for the error case",
    "Here is the journey. Your code goes into the compiler. The compiler checks every word. If it is happy, it builds a program. Only then can the computer run it. If the compiler is not happy, it tells you the line number.", CS),
   ("Run it in your head", "`hello.cpp` again, with the output panel on the right",
    "[HL 4] When this line runs, Hello, Goa appears. [HL 5] Next, the second line prints below it. The word endl means end of line, so the next text starts fresh underneath. Change the words inside the quotes and the output changes too. Try your own name."),
   ("Compile and run", "Terminal: `g++ hello.cpp -o hello`, then `./hello`",
    "In the terminal, type g plus plus, the file name, dash o, hello. No message means success. Now run it with dot slash hello. There it is. Our first program."),
   ("Bug of the Day", "BUG OF THE DAY: a statement with no semicolon",
    "Bug of the Day. Our code has no semicolon after endl. The compiler says, expected semicolon before return. Notice it points at the end of the line, and shows the next line underneath. Add the semicolon, and it compiles. If you ever see this message, look at the line above the one it names."),
   ("I told my compiler a joke. It said: expected ';' before 'laugh'.", "I told my compiler a joke. It said: expected semicolon before laugh."),
   ("Task card: print your name, then your favourite beach", "Your challenge: print your name on one line, and your favourite beach on the next. Comment your answer below."),
   ("Next: EP 02 · Setting up and compiling", "Next time: setting up your computer and compiling properly. Keep coding, says Xecxec!")),
 bug=dict(file="hello.cpp", intro="line 4 has no semicolon", wrong=EP1_BUG, fix_intro="semicolon added", fixed=EP1_FIX, expect=["expected ';' before 'return'"],
   why="g++ only notices a missing semicolon when it reaches the next statement, so the real mistake is usually on the line above the one it names."),
 pun="\"I told my compiler a joke. It said: expected ';' before 'laugh'.\"",
 challenge="Print your name on one line and your favourite beach on the next.",
 answer="Use two cout lines, for example Atreya, then Palolem, each ending with std::endl.",
 answer_code='''#include <iostream>

int main() {
    std::cout << "Atreya" << std::endl;
    std::cout << "Palolem" << std::endl;
    return 0;
}''',
 shorts=[
  dict(id="S1", title="The smallest C++ program", built=[3], hook="Seven lines make a real program.", script="Seven lines make a real program. Three of them matter most: include, main and cout. Everything else in C plus plus is built on these three.", on="THE SMALLEST C++ PROGRAM", caption="Your first C++ program in 30 seconds.", tags=["cpp", "learntocode", "kodingkonkani", "codingforbeginners", "goa"]),
  dict(id="S2", title="From code to program", built=[4], hook="What does a compiler actually do?", script="What does a compiler actually do? Your code goes in. The compiler checks every word. If all is fine, out comes a program you can run. If not, you get a line number. The compiler is your first teacher.", on="CODE, COMPILER, PROGRAM", caption="The compiler is your first teacher.", tags=["cpp", "compiler", "programming", "kodingkonkani", "learntocode"]),
  dict(id="S3", title="What does cout do?", built=[3, 5], hook="Two little arrows, one big job.", script="Two little arrows, one big job. cout is the screen. The arrows push text towards it. Put words in quotes and they appear exactly as written. And endl moves to the next line.", on="COUT: ARROWS TO THE SCREEN", caption="cout explained slowly.", tags=["cpp", "cout", "helloworld", "kodingkonkani", "coding"]),
  dict(id="S4", title="The missing semicolon", built=[7], hook="One missing character, one angry compiler.", script="One missing character, one angry compiler. Remove a single semicolon and g plus plus says, expected semicolon before return. The error points at the next line, so always check the line above.", on="EXPECTED ';' BEFORE 'RETURN'", caption="Always check the line above.", tags=["cpp", "bugfix", "compilererror", "kodingkonkani", "coding"]),
  dict(id="S5", title="Pun and challenge", built=[8, 9], hook="Can your compiler take a joke?", script="Can your compiler take a joke? I told mine one and it said, expected semicolon before laugh. Your challenge: print your name, then your favourite beach. Full video: EP 1.", on="PRINT YOUR NAME + YOUR BEACH", caption="Try the challenge in the comments.", tags=["cpp", "codingchallenge", "kodingkonkani", "programmingjokes", "goa"]),
 ])

EP2_CODE = '''#include <iostream>

int main() {
    int fish = 3;
    int price = 120;
    std::cout << "Fish: " << fish << std::endl;
    std::cout << "Total: " << fish * price << std::endl;
    return 0;
}'''
EP2_BUG = '''int main() {
    int fish = 3;
    std::cout << "Fish: " << fish << std::endl;
    return 0;
}'''
EP2_FIX = "#include <iostream>\n\n" + EP2_BUG

EP2 = dict(ep=2, title="Setting up and compiling", prereq="EP 01", **MOD,
 goals=["install a C++ compiler and check it with g++ --version", "compile and run a program from the terminal", "read the parts of a compile command: file name, -o and ./name"],
 yt=dict(title="Install C++ and Compile Your First File | C++ Programming EP 02",
   desc="Set up g++ and VS Code on Windows, Mac or Linux, then compile and run a program with Xecxec.",
   tags=["install c++", "g++", "vs code c++", "compile c++", "c++ for beginners", "koding konkani", "mingw", "c++ tutorial", "class 11 computer science", "coding in goa"],
   thumb_text="SET UP C++", thumb_visual="in tomato on peach; Xecxec raising both claws beside a terminal showing g++ --version; thin black border and drop shadow.",
   chapters={1: "Intro", 2: "What you need", 3: "Install g++", 4: "How g++ builds a file", 5: "A program with numbers", 6: "Compile and run", 7: "Bug of the Day", 9: "Challenge", 10: "Next episode"}),
 files=[dict(name="fish.cpp", source=EP2_CODE, scene="5")],
 scenes=std_scenes((2, "SET UP AND COMPILE"),
   "Welcome back! Last time we wrote a program. Today we set up your computer so you can run it yourself. It takes about ten minutes, and you only do it once.",
   ("What you need", '"What you need": three numbered lines and a kitchen analogy card', "Lines spring in one by one with a pop; the kitchen card slides in with a chopping board, a stove and a chef",
    "You need three things. A compiler, which is g plus plus. An editor, where you type your code, like VS Code. And a terminal, where you give commands. Think of a kitchen. The compiler is the stove, the editor is the chopping board, and the terminal is you, giving the orders."),
   ("Install g++", "Install steps for Windows, Mac and Linux, shown as three tabs",
    "First, install the compiler. On Windows, install MinGW-w64 through MSYS2, then add its bin folder to your path. On a Mac, open the terminal and type xcode-select dash dash install. On Linux, install g plus plus with your package manager, for example sudo apt install g plus plus. Then check it. Type g plus plus, space, dash dash version. If you see a version number, you are ready."),
   ("How g++ builds a file", "Three boxes: fish.cpp, g++, fish; the command written under the arrows",
    "Three boxes appear; arrows draw on between them; the dash o part of the command glows tomato",
    "Here is what g plus plus does. It reads fish dot cpp, checks it, and writes a new file, the program. The dash o part names that new file. Without it, you get a default name, and that is easy to forget.", CS),
   ("A program with numbers", "`fish.cpp`: two numbers, a label and a total",
    "[HL 4] [TRACK fish=3] Here we make a whole number called fish, and put three in it. [HL 5] [TRACK price=120] Another number called price, one hundred twenty. [HL 6] Print the label, then the value of fish. [HL 7] And here, C plus plus does the maths for us: fish times price. Three times one hundred twenty is three hundred sixty."),
   ("Compile and run", "Terminal: `g++ fish.cpp -o fish`, then `./fish`",
    "Save the file as fish dot cpp. Compile with g plus plus, fish dot cpp, dash o, fish. Then run it. On Mac and Linux, type dot slash fish. On Windows, type fish. Fish, three. Total, three hundred sixty."),
   ("Bug of the Day", "BUG OF THE DAY: no include line",
    "Bug of the Day. We forgot the include line at the top. The compiler says, cout is not a member of std. Read the small note below it. It even tells you, did you forget to include iostream? Add the line back and it works."),
   ("Why did the programmer bring a ladder to the compiler? To reach the high-level language.", "Why did the programmer bring a ladder to the compiler? To reach the high-level language."),
   ("Task card: install, check, compile, change the price", "Your challenge: install g plus plus, run g plus plus dash dash version, and compile fish dot cpp. Then change the price and run it again."),
   ("Next: EP 03 · C vs C++: what changed", "Next: how C plus plus is different from C. Keep coding, says Xecxec!")),
 bug=dict(file="fish.cpp", intro="no #include line", wrong=EP2_BUG, fix_intro="include line added", fixed=EP2_FIX, expect=["'cout' is not a member of 'std'", "did you forget to '#include <iostream>'"],
   why="The compiler only knows the names you bring in. The note under the error says which header to include."),
 pun="\"Why did the programmer bring a ladder to the compiler? To reach the high-level language.\"",
 challenge="Install g++, check the version, compile fish.cpp, then change the price and run it again.",
 answer="Change int price = 120; to int price = 150; and recompile: the total becomes 450.",
 answer_code=EP2_CODE.replace("price = 120", "price = 150"),
 shorts=[
  dict(id="S1", title="What you need for C++", built=[2], hook="Three tools, ten minutes.", script="Three tools, ten minutes. A compiler, an editor and a terminal. g plus plus is the stove, VS Code is the chopping board, and the terminal is you, giving the orders.", on="3 TOOLS FOR C++", caption="Set up C++ in three steps.", tags=["cpp", "setup", "beginners", "kodingkonkani", "goa"]),
  dict(id="S2", title="Check your compiler", built=[3], hook="Is g++ really installed?", script="Is g plus plus really installed? Open the terminal and type g plus plus, dash dash version. A version number means you are ready. An error means the install needs a second look.", on="G++ --VERSION", caption="One command to check your setup.", tags=["cpp", "gpp", "terminal", "kodingkonkani", "learntocode"]),
  dict(id="S3", title="Decode the compile command", built=[4, 6], hook="g++ fish.cpp -o fish: what does it mean?", script="g plus plus fish dot cpp dash o fish. What does it mean? g plus plus is the compiler. Fish dot cpp is your source. Dash o names the result. Then run it with dot slash fish.", on="G++ FISH.CPP -O FISH", caption="Decode the command.", tags=["cpp", "compile", "learncoding", "kodingkonkani", "terminal"]),
  dict(id="S4", title="cout is not a member of std", built=[7], hook="The line you always forget.", script="The line you always forget. Remove the include line and g plus plus says, cout is not a member of std. Then the note below tells you the fix. Always read the note.", on="'COUT' IS NOT A MEMBER OF 'STD'", caption="Read the note under the error.", tags=["cpp", "bugfix", "iostream", "kodingkonkani", "compilererror"]),
  dict(id="S5", title="Pun and challenge", built=[8, 9], hook="A ladder for the compiler?", script="A ladder for the compiler? Why did the programmer bring one? To reach the high-level language. Your challenge: compile fish dot cpp, change the price, and run it again. Full video: EP 2.", on="COMPILE FISH.CPP + CHANGE THE PRICE", caption="Do the challenge.", tags=["cpp", "codingchallenge", "kodingkonkani", "programmingjokes", "goa"]),
 ])

EP3_CODE = '''#include <iostream>
using namespace std;

int main() {
    int age = 17;
    cout << "Age: " << age << endl;
    cout << "Next year: " << age + 1 << endl;
    return 0;
}'''
EP3_BUG = '''#include <iostream>

int main() {
    int age = 17;
    cout << "Age: " << age << endl;
    return 0;
}'''
EP3_FIX = EP3_BUG.replace("#include <iostream>\n", "#include <iostream>\nusing namespace std;\n")

EP3 = dict(ep=3, title="C vs C++: what changed", prereq="EP 02", **MOD,
 goals=["see how cout replaces printf and cin replaces scanf", "understand using namespace std and what std:: means", "know why C++ was built on top of C"],
 yt=dict(title="C vs C++: What Changed? | C++ Programming EP 03",
   desc="Compare C and C++ side by side: printf versus cout, headers and namespaces, with Xecxec.",
   tags=["c vs c++", "cout vs printf", "namespace std", "using namespace std", "c++ for beginners", "koding konkani", "c++ tutorial", "class 11 computer science", "coding in goa", "learn c++"],
   thumb_text="C vs C++", thumb_visual="in tomato on peach; Xecxec shaking his shell between two code cards, C on the left and C++ on the right; thin black border and drop shadow.",
   chapters={1: "Intro", 2: "Why C++ exists", 3: "printf versus cout", 4: "What is std?", 5: "A full example", 6: "Run it", 7: "Bug of the Day", 9: "Challenge", 10: "Next episode"}),
 files=[dict(name="age.cpp", source=EP3_CODE, scene="5")],
 scenes=std_scenes((3, "C vs C++: WHAT CHANGED"),
   "If you watched our C course, welcome back. If not, welcome anyway. Today we see what C plus plus changed, and why.",
   ("Why C++ exists", '"Why C++?": three numbered lines and a phone-and-newer-phone analogy card', "Lines spring in with a pop; the analogy card slides in with two phones side by side",
    "C plus plus began as C with extras. Almost everything you know from C still works. But C plus plus adds friendlier tools, like safer text, and ways to organise big programs. Think of a phone and its newer model. Same calls, same texts, but more things you can do."),
   ("printf versus cout", "Two code panels side by side: C with printf on the left, C++ with cout on the right",
    "On the left, C prints with printf and a format code. On the right, C plus plus uses cout. You do not need a format code. The value just goes in, and the arrows push it to the screen. And for input, C used scanf, and C plus plus uses cin, with the arrows pointing the other way."),
   ("What is std?", "A box labelled std holding cout, cin, endl and string; a second box labelled your code",
    "The std box pops in with its four items; an arrow runs from your code to the box with a whoosh; the words using namespace std stamp across the arrow",
    "Where do cout and endl live? In a box called std, short for standard. To use them you write std colon colon cout. Or you say once, at the top, using namespace std, and the box is opened for the whole file.", CS),
   ("A full example", "`age.cpp`: a number, a label and a calculation inside the line",
    "[HL 2] This line opens the std box. [HL 5] [TRACK age=17] Make a number called age, with seventeen. [HL 6] Print the label and the age. See how easy it is to mix text and numbers. [HL 7] And we can calculate inside the line. Age plus one is eighteen."),
   ("Run it", "Terminal: `g++ age.cpp -o age`, then `./age`",
    "Compile and run. Age, seventeen. Next year, eighteen. No format codes, and no mistakes with percent d."),
   ("Bug of the Day", "BUG OF THE DAY: cout without using namespace std",
    "Bug of the Day. We use cout, but we forgot using namespace std. The compiler says, cout was not declared in this scope. Did you mean std colon colon cout? Yes! Add the using line, or write std colon colon in front."),
   ("C++ is just C with a bigger toolbox, and a lot more places to drop a screw.", "C plus plus is just C with a bigger toolbox, and a lot more places to drop a screw."),
   ("Task card: print your age now and in ten years", "Your challenge: a program with a number called age. Print your age now, and your age in ten years."),
   ("Next: EP 04 · Anatomy of a C++ program", "Next: the anatomy of a C plus plus program. Keep coding, says Xecxec!")),
 bug=dict(file="age.cpp", intro="cout used without std", wrong=EP3_BUG, fix_intro="using namespace std added", fixed=EP3_FIX, expect=["'cout' was not declared in this scope", "did you mean 'std::cout'"],
   why="Names from the standard library live in the std box, so you either write std:: in front or open the box once with using namespace std."),
 pun="\"C++ is just C with a bigger toolbox, and a lot more places to drop a screw.\"",
 challenge="Print your age now and your age in ten years.",
 answer="Make int age = 17; then print age and age + 10 with cout.",
 answer_code='''#include <iostream>
using namespace std;

int main() {
    int age = 17;
    cout << "Now: " << age << endl;
    cout << "In ten years: " << age + 10 << endl;
    return 0;
}''',
 shorts=[
  dict(id="S1", title="printf versus cout", built=[3], hook="No more percent d.", script="No more percent d. In C you write printf with a format code. In C plus plus you push the value into cout with arrows. Fewer codes, fewer mistakes.", on="PRINTF VS COUT", caption="printf versus cout in 30 seconds.", tags=["cpp", "cprogramming", "beginners", "kodingkonkani", "learntocode"]),
  dict(id="S2", title="What is std?", built=[4], hook="A box that holds cout.", script="A box that holds cout. std is the standard box. cout, cin and endl live inside it. Write std colon colon cout, or open the box once with using namespace std.", on="WHAT IS STD?", caption="std explained.", tags=["cpp", "namespace", "std", "kodingkonkani", "coding"]),
  dict(id="S3", title="Mix text and numbers", built=[5], hook="One line, text and a number.", script="One line, text and a number. cout, arrows, a label, an arrow, the age. Arrows can be chained, and each arrow pushes one thing to the screen.", on="COUT << \"AGE: \" << AGE", caption="Chain your arrows.", tags=["cpp", "cout", "coding", "kodingkonkani", "beginners"]),
  dict(id="S4", title="cout was not declared", built=[7], hook="The did-you-mean that saves you.", script="The did-you-mean that saves you. Forget using namespace std and g plus plus says, cout was not declared. Then it suggests std colon colon cout. Read the suggestion.", on="'COUT' WAS NOT DECLARED", caption="Read the suggestion!", tags=["cpp", "bugfix", "compiler", "kodingkonkani", "coding"]),
  dict(id="S5", title="Pun and challenge", built=[8, 9], hook="A screw in the toolbox?", script="A screw in the toolbox? C plus plus is just C with a bigger toolbox, and a lot more places to drop a screw. Your challenge: print your age now and in ten years. Full video: EP 3.", on="AGE NOW + AGE IN 10 YEARS", caption="Comment your answer.", tags=["cpp", "challenge", "kodingkonkani", "programmingjokes", "goa"]),
 ])

EP4_CODE = '''#include <iostream>
using namespace std;

// Xecxec counts the beach shacks
int main() {
    int shacks = 12;
    int open_now = 9;
    cout << "Shacks: " << shacks << endl;
    cout << "Open: " << open_now << endl;
    cout << "Closed: " << shacks - open_now << endl;
    return 0;
}'''
EP4_BUG = '''#include <iostream>
using namespace std;

int main() {
    int shacks = 12;
    cout << "Shacks: " << shacks << endl;
    return 0;'''
EP4_FIX = EP4_BUG + "\n}"

EP4 = dict(ep=4, title="Anatomy of a C++ program", prereq="EP 03", **MOD,
 goals=["name the parts: include, main, statements, braces, comments and return 0", "write a single-line comment with //", "recognise a missing closing brace error"],
 yt=dict(title="Anatomy of a C++ Program | C++ Programming EP 04",
   desc="Take a C++ program apart piece by piece: main, braces, statements and comments, with Xecxec.",
   tags=["c++ program structure", "main function", "comments in c++", "braces", "c++ for beginners", "koding konkani", "c++ tutorial", "class 11 computer science", "coding in goa", "learn c++"],
   thumb_text="ANATOMY OF A PROGRAM", thumb_visual="in tomato on peach; Xecxec holding a magnifying glass over a code card with coloured labels; thin black border and drop shadow.",
   chapters={1: "Intro", 2: "The parts", 3: "Walk through the code", 4: "Numbers in memory", 5: "Comments", 6: "Run it", 7: "Bug of the Day", 9: "Challenge", 10: "Next module"}),
 files=[dict(name="shacks.cpp", source=EP4_CODE, scene="3, 5")],
 scenes=std_scenes((4, "ANATOMY OF A PROGRAM"),
   "Today we open up a C plus plus program and name every part, like a biology class, but nobody gets hurt.",
   ("The parts", '"The parts": three numbered lines and a bus-route analogy card', "Lines spring in with a pop; the bus-route card slides in with three stops",
    "A program is like a bus route. It has a starting stop, which is main. Then it visits stops in order, which are statements. Each statement ends with a semicolon, like a ticket stamp. And the route ends with return zero."),
   ("Walk through the code", "`shacks.cpp`: a 12-line program with coloured labels on each part",
    "[HL 1] Include brings in a toolbox. [HL 2] Using namespace std opens the std box. [HL 5] Main is where the bus starts. The curly brace after it opens the body. [HL 6] The body holds our statements. Each one ends with a semicolon. [HL 11] Return zero means, finished, no problems. [HL 12] And the last curly brace closes main."),
   ("Numbers in memory", "Two memory boxes: shacks = 12 and open_now = 9, and a printed result Closed: 3",
    "Two labelled boxes pop in with their values and addresses; a subtraction arrow draws on and the result 3 is printed, not stored; pop per box",
    "Our program keeps two numbers in memory. Shacks holds twelve. Open now holds nine. When we calculate shacks minus open now, the answer, three, is not stored anywhere. It is printed straight away.", MB),
   ("Comments", "`shacks.cpp` again; the comment line glows and the output panel fills",
    "[HL 4] This line starts with two slashes. That is a comment. The compiler ignores it, but humans love it. [HL 6] [TRACK shacks=12] Twelve shacks on the beach. [HL 7] [TRACK open_now=9] Nine are open. [HL 10] Closed is twelve minus nine, which is three. Use comments to explain why, not what."),
   ("Run it", "Terminal: `g++ shacks.cpp -o shacks`, then `./shacks`",
    "Compile it and run. Shacks, twelve. Open, nine. Closed, three. The comment is nowhere in the output, because the compiler threw it away."),
   ("Bug of the Day", "BUG OF THE DAY: a missing closing brace",
    "Bug of the Day. We forgot the closing curly brace at the end. The compiler says, expected closing brace at end of input. And a note says, to match this opening brace. Always count your braces. Open, close, open, close."),
   ("Why did the brace feel lonely? Its partner never showed up at end of input.", "Why did the brace feel lonely? Its partner never showed up at end of input."),
   ("Task card: boys plus girls, print the total", "Your challenge: write a program with a comment, two numbers called boys and girls in your class, and print the total."),
   ("Next: Module 1 · Variables and types", "Module zero is done! Next: variables and types. Keep coding, says Xecxec!")),
 bug=dict(file="shacks.cpp", intro="the closing brace of main is missing", wrong=EP4_BUG, fix_intro="closing brace added", fixed=EP4_FIX, expect=["expected '}' at end of input", "to match this '{'"],
   why="Every opening brace needs a matching closing brace. The note under the error shows which opening brace is still waiting."),
 pun="\"Why did the brace feel lonely? Its partner never showed up at end of input.\"",
 challenge="Write a program with a comment, two numbers (boys and girls) and print the total.",
 answer="Use int boys = 20; and int girls = 18; then print boys + girls, which gives 38.",
 answer_code='''#include <iostream>
using namespace std;

// Total students in my class
int main() {
    int boys = 20;
    int girls = 18;
    cout << "Total: " << boys + girls << endl;
    return 0;
}''',
 shorts=[
  dict(id="S1", title="A program is a bus route", built=[2], hook="Start at main, stop at return.", script="Start at main, stop at return. Every program begins at main, visits each statement in order, and ends at return zero. Like a bus route through Panaji.", on="A PROGRAM IS A BUS ROUTE", caption="Think of a bus route.", tags=["cpp", "programming", "beginners", "kodingkonkani", "goa"]),
  dict(id="S2", title="Name every part", built=[3], hook="Twelve lines, five parts.", script="Twelve lines, five parts. Include, using, main, statements and return. Coloured labels point at each part, so you never have to guess again.", on="12 LINES, 5 PARTS", caption="Label the code.", tags=["cpp", "structure", "learntocode", "kodingkonkani", "coding"]),
  dict(id="S3", title="Comments", built=[5], hook="The line the compiler ignores.", script="The line the compiler ignores. Two slashes make a comment. The compiler skips it, but humans read it. Explain why you did something, not what the code does.", on="// COMMENTS", caption="Comment your code.", tags=["cpp", "comments", "coding", "kodingkonkani", "beginners"]),
  dict(id="S4", title="Expected } at end of input", built=[7], hook="Count your braces.", script="Count your braces. A missing closing brace gives, expected closing brace at end of input. And a note shows which opening brace is still waiting.", on="EXPECTED '}' AT END OF INPUT", caption="Open, close, open, close.", tags=["cpp", "bugfix", "braces", "kodingkonkani", "compilererror"]),
  dict(id="S5", title="Pun and challenge", built=[8, 9], hook="A lonely brace.", script="A lonely brace. Why did the brace feel lonely? Its partner never showed up at end of input. Your challenge: boys plus girls, print the total. Full video: EP 4.", on="BOYS + GIRLS = ?", caption="Try it!", tags=["cpp", "challenge", "kodingkonkani", "programmingjokes", "goa"]),
 ])

EPS = [EP1, EP2, EP3, EP4]

RECAP = {
 1: ("Recap: four ideas on one card", "Let us recap. One: every C plus plus program starts at main. Two: include iostream gives you cout, and cout prints text with arrows. Three: every statement ends with a semicolon. And remember the journey: code, compiler, program. If you can say those four things out loud, you have understood today's episode. Pause the video, and say them once, slowly."),
 2: ("Recap: four steps on one card", "Recap time. One: you need a compiler, an editor and a terminal. Two: check the compiler with g plus plus, dash dash version. Three: compile with g plus plus, the file name, dash o, and a name for the program. Four: run it with dot slash and that name. If any step fails, do not panic. Read the message, check the spelling, and try again. Every programmer does this, every single day."),
 3: ("Recap: four ideas on one card", "Recap. One: C plus plus keeps almost everything from C, and adds friendlier tools. Two: cout replaces printf, and cin replaces scanf, with arrows pointing the way. Three: cout and cin live in the std box, so write std colon colon, or say using namespace std once at the top. Four: you can mix text and numbers in one line. That is a lot already. Well done."),
 4: ("Recap: four rules on one card", "Recap. One: a program starts at main and ends at return zero. Two: every statement ends with a semicolon. Three: curly braces come in pairs, one to open and one to close. Four: a comment starts with two slashes, and the compiler ignores it. Say these four rules out loud, and you can read any beginner program. Try it on the shacks program, line by line."),
}
for _e in EPS:
    on, narr = RECAP[_e["ep"]]
    _e["scenes"].insert(6, dict(tpl=CS, name="Recap", on=on, anim="Four recap lines tick in one by one with a pop; Xecxec nods after each tick", narr=narr, min=30))
    for _s in _e["shorts"]:
        _s["built"] = [b + 1 if b >= 7 else b for b in _s["built"]]
    _e["yt"]["chapters"] = {(k + 1 if k >= 7 else k): v for k, v in _e["yt"]["chapters"].items()}
    _e["yt"]["chapters"][7] = "Recap"

EXTRA = {
 1: {1: " Computers only understand ones and zeros. The compiler translates your words into those numbers, so you never have to.",
     3: " That is why you will see two kinds of messages: compiler errors before the program runs, and results after.",
     4: " Before you run it, predict the output. Two lines. The second one says, Keep coding, says Xecxec. Were you right? Predicting before running is the habit that makes you fast."},
 2: {1: " Do not worry if the names sound strange. By the end of today, you will have typed every one of these commands yourself.",
     3: " Run this same command again after every change you make to the file.",
     4: " Predict first: if we change the price to one hundred fifty, what should the total be? Four hundred fifty. Keep that in mind, it is today's challenge."},
 3: {1: " C plus plus was created in the early nineteen eighties, and it is still used today for games, browsers and banking systems.",
     3: " Just remember: std is a box, and the using line opens it.",
     4: " Predict first: with age seventeen, what does the second line print? Eighteen. The calculation happens first, and then the result is printed."},
 4: {1: " Every program you will ever write, from a tiny calculator to a banking app, follows this same route.",
     3: " Each box has a name, a value and an address, like a house number on a street in Panaji.",
     4: " Predict before you run: the closed line prints twelve minus nine. Three. Always predict first."},
}
for _e in EPS:
    for _idx, _txt in EXTRA[_e["ep"]].items():
        _e["scenes"][_idx]["narr"] += _txt

EPS[3]["scenes"][1]["min"] = 40


import re
for _e in EPS:
    _mapped = set()
    for _f in _e["files"]:
        _mapped |= {int(x) for x in re.findall(r"\d+", _f.get("scene", ""))}
    for _i, _s in enumerate(_e["scenes"], 1):
        if _s["tpl"] == CE and _i not in _mapped:
            print("cpp patch", _e["ep"], _i, _s["name"])
            _s["tpl"] = CS
            _s["anim"] = "Three tabs (Windows, Mac, Linux) switch with a pop; the active steps tick in one by one" if "Install" in _s["name"] else "Lines spring in one by one with a pop; the explanation card slides in from the right"
