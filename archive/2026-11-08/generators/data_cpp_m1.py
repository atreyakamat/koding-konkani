# C++ course, Module 1 (EP5-12)
import re
MOD = dict(module=1, mod_name="Variables and types", bgacc="Pastel Blue + Tomato")
TC = "Title card"; CS = "Concept slide"; CE = "Code explain"; MB = "Memory boxes"; TM = "Terminal"; BG = "Bug of the Day"; PC = "Pun card"; CH = "Challenge"; OU = "Outro"

def std_scenes(title_line, title_narr, s2, s3, s4, s5, s6, s7, pun, ch, ou):
    return [
        dict(tpl=TC, name="Title", on=f"EP {title_line[0]:02d} · {title_line[1]}", anim="Tomato title card: EP sticker thuds in, title stamps with a whoosh, Xecxec scuttles in and waves; thud, whoosh, claw-click, sting", narr=title_narr, min=15),
        dict(tpl=CS, name=s2[0], on=s2[1], anim=s2[2], narr=s2[3], min=30),
        dict(tpl=CE, name=s3[0], on=s3[1], anim="Code types in with key-tick; butter [HL n] highlight sweeps line by line with marker-swipe; explanation card on the right", narr=s3[2], min=40),
        dict(tpl=s4[4], name=s4[0], on=s4[1], anim=s4[2], narr=s4[3], min=30),
        dict(tpl=CE, name=s5[0], on=s5[1], anim="Same code; the output panel fills line by line with a ding per output line; [TRACK] cards update", narr=s5[2], min=40),
        dict(tpl=TM, name=s6[0], on=s6[1], anim="Dark-blue terminal: the command types with key-tick, output prints in mint with a ding", narr=s6[2], min=20),
        dict(tpl=BG, name=s7[0], on=s7[1], anim=s7[3] if len(s7) > 3 else "Butter banner drops in with a buzzer; wrong code shakes; the g++ error lines appear in tomato; the fix slides in and the terminal turns mint with a ding", narr=s7[2], min=40),
        dict(tpl=PC, name="Pun", on=pun[0], anim="Full tomato screen, card flips in with a rimshot, Xecxec snaps his claw", narr=pun[1], min=4),
        dict(tpl=CH, name="Challenge", on=ch[0], anim="Task card pops in; checklist ticks with a pop; Xecxec holds a tiny pen", narr=ch[1], min=20),
        dict(tpl=OU, name="Outro", on=ou[0], anim="Next-episode card slides up with a whoosh; right side stays empty for end-screen elements; sign-off text types in", narr=ou[1], min=15),
    ]

RT_ANIM = "Butter banner drops in with a buzzer; the program compiles and runs; the wrong output appears in tomato; the fix slides in and the output turns mint with a ding"
WARN_ANIM = "Butter banner drops in with a buzzer; the g++ warning appears in tomato, then the program runs and prints the wrong result; the fix slides in and the output turns mint with a ding"
def tags(*extra): return list(extra)

# ---------------------------------------------------------------- EP5
EP5_CODE = '''#include <iostream>
using namespace std;

int main() {
    int fish = 3;
    double price = 120.5;
    char grade = 'A';
    bool open_now = true;
    cout << "Fish: " << fish << endl;
    cout << "Price: " << price << endl;
    cout << "Grade: " << grade << endl;
    cout << "Open: " << open_now << endl;
    return 0;
}'''
EP5_BUG = '''#include <iostream>
using namespace std;

int main() {
    int packets;
    cout << "Packets: " << packets << endl;
    return 0;
}'''
EP5_FIX = EP5_BUG.replace("int packets;", "int packets = 0;")
EP5 = dict(ep=5, title="Variables and types", prereq="EP 04", **MOD,
 goals=["create variables of type int, double, char and bool", "pick the right type for a value", "always give a variable a starting value"],
 yt=dict(title="Variables and Types in C++: int, double, char, bool | C++ Programming EP 05",
   desc="Learn how C++ stores whole numbers, decimals, letters and true or false values in variables, with Xecxec the crab.",
   tags=["c++ variables", "c++ data types", "int double char bool", "c++ for beginners", "koding konkani", "c++ tutorial", "uninitialized variable", "class 11 computer science", "first year engineering", "coding in goa"],
   thumb_text="VARIABLES + TYPES", thumb_visual="in tomato on pastel blue; Xecxec holding four labelled boxes marked int, double, char and bool; thin black border and drop shadow.",
   chapters={1: "Intro", 2: "Boxes with types", 3: "Declaring variables", 4: "Variables in memory", 5: "Run it in your head", 6: "Compile and run", 7: "Bug of the Day", 9: "Challenge", 10: "Next episode"}),
 files=[dict(name="vars.cpp", source=EP5_CODE, scene="3, 5")],
 scenes=std_scenes((5, "VARIABLES AND TYPES"),
   "Welcome back! So far our programs only printed words. Today they learn to remember things. A variable is a little labelled box, and C plus plus has a different kind of box for every kind of data.",
   ("Boxes with types", '"Boxes with types": four numbered lines (int, double, char, bool) and a fridge-shelves analogy card', "Four lines spring in one by one with a pop; the fridge card slides in with a bottle shelf, an ice tray and a lemon drawer",
    "A variable is a named box in memory. Every box has a type, and the type says what can go inside. Int holds whole numbers, like three fish. Double holds numbers with a decimal point, like one hundred twenty point five. Char holds one single character, written in single quotes. And bool holds only true or false. Think of a beach shack fridge. One shelf for bottles, one tray for ice. Each place is shaped for one job."),
   ("Declaring variables", "`vars.cpp`: four variables, each line shows type, name and value",
    "[HL 5] Int fish equals three. First the type, then the name, then the value. [HL 6] Double price equals one hundred twenty point five. [HL 7] Char grade equals A. Notice the single quotes around the letter. [HL 8] And bool open now equals true. [HL 9] Now we print each one. The names have no quotes, so cout prints the value stored inside, not the word itself."),
   ("Variables in memory", "Four memory boxes: fish = 3, price = 120.5, grade = 'A', open_now = true, each with a size and an address",
    "Four labelled boxes pop in one by one, each with its value, its size in bytes and an address tag; boxes differ in width to show their sizes; pop per box",
    "Here is what memory looks like. Each variable is a box with a name, a value and an address. On most computers, an int takes four bytes, so fish needs four. A double is bigger, eight bytes. A char takes one byte, and so does a bool. Different types, different sizes. The address tells the computer where on the street each box lives.", MB),
   ("Run it in your head", "`vars.cpp` again, with the output panel on the right",
    "[HL 5] [TRACK fish=3] Fish holds three. [HL 6] [TRACK price=120.5] Price holds one hundred twenty point five. [HL 7] [TRACK grade=A] Grade holds A. [HL 8] [TRACK open_now=true] Open now holds true. [HL 12] Look at the last output line. A bool prints as one for true, and zero for false. So the screen says, Open, one."),
   ("Compile and run", "Terminal: `g++ vars.cpp -o vars`, then `./vars`",
    "Compile with g plus plus, vars dot cpp, dash o, vars. Then run it. Fish, three. Price, one hundred twenty point five. Grade, A. Open, one. Each value comes out in the shape of its type."),
   ("Bug of the Day", "BUG OF THE DAY: a variable with no starting value",
    "Bug of the Day. Here we make an int called packets, but we never give it a value. The compiler warns us: packets is used uninitialized. It is only a warning, so the program still runs, and prints a strange number. Run it again and the number may change. That is garbage left behind in memory. Give every variable a value when you make it. With equals zero, the output is a clean zero.", WARN_ANIM),
   ("An uninitialised variable walks into a bar. The bartender asks, what will you have? It says: whatever was there before.", "An uninitialised variable walks into a bar. The bartender asks, what will you have? It says, whatever was there before."),
   ("Task card: four variables, four types", "Your challenge: make four variables. Your age, your height in metres, your first initial, and whether you like fish. Print all four. Comment your answer below."),
   ("Next: EP 06 · Reading input with cin", "Next time: reading input with cin, so your program can ask a question and listen. Keep coding, says Xecxec!")),
 bug=dict(file="packets.cpp", mode="runtime", show_fixed_out=True, intro="packets is never given a value", wrong=EP5_BUG, fix_intro="starting value added", fixed=EP5_FIX, expect=["'packets' is used uninitialized"],
   why="A variable you do not set holds whatever was left in that memory before, so always write int packets = 0; or another starting value."),
 pun="\"An uninitialised variable walks into a bar. The bartender asks, what will you have? It says: whatever was there before.\"",
 challenge="Make four variables: your age, your height in metres, your first initial and whether you like fish. Print all four.",
 answer="Use int, double, char and bool, for example 17, 1.65, 'A' and true; the bool prints as 1.",
 answer_code='''#include <iostream>
using namespace std;

int main() {
    int age = 17;
    double height = 1.65;
    char initial = 'A';
    bool likes_fish = true;
    cout << age << endl;
    cout << height << endl;
    cout << initial << endl;
    cout << likes_fish << endl;
    return 0;
}''',
 shorts=[
  dict(id="S1", title="Four boxes, four types", built=[2], hook="Four boxes for four kinds of data.", script="Four boxes for four kinds of data. Int for whole numbers. Double for decimals. Char for one letter in single quotes. Bool for true or false. Pick the box that fits the value.", on="INT, DOUBLE, CHAR, BOOL", caption="Four types in 30 seconds.", tags=["cpp", "datatypes", "beginners", "kodingkonkani", "learntocode"]),
  dict(id="S2", title="Declaring a variable", built=[3], hook="Type, name, value: three words.", script="Type, name, value: three words make a variable. Int fish equals three. Double price equals one hundred twenty point five. Char grade equals A, with single quotes around the letter.", on="TYPE + NAME = VALUE", caption="Declare a variable.", tags=["cpp", "variables", "coding", "kodingkonkani", "beginners"]),
  dict(id="S3", title="Boxes in memory", built=[4], hook="Every variable has an address.", script="Every variable has an address. Each box has a name, a value, a size and an address. On most computers an int takes four bytes, a double takes eight, and a char takes one.", on="NAME, VALUE, SIZE, ADDRESS", caption="Memory is a street of boxes.", tags=["cpp", "memory", "programming", "kodingkonkani", "learntocode"]),
  dict(id="S4", title="Used uninitialized", built=[7], hook="The variable you forgot to set.", script="The variable you forgot to set. Make an int and never give it a value, and g plus plus warns, used uninitialized. The program still runs and prints garbage. Always set a starting value.", on="'PACKETS' IS USED UNINITIALIZED", caption="Always give a starting value.", tags=["cpp", "bugfix", "uninitialized", "kodingkonkani", "compilerwarning"]),
  dict(id="S5", title="Pun and challenge", built=[8, 9], hook="A variable walks into a bar.", script="A variable walks into a bar. The bartender asks what it will have. Whatever was there before. Your challenge: make four variables and print them all. Full video: EP 5.", on="4 VARIABLES, 4 TYPES", caption="Try the challenge in the comments.", tags=["cpp", "codingchallenge", "kodingkonkani", "programmingjokes", "goa"]),
 ])

# ---------------------------------------------------------------- EP6
EP6_CODE = '''#include <iostream>
#include <string>
using namespace std;

int main() {
    string name, city;
    int age;
    cout << "Name, age, city? ";
    cin >> name >> age;
    cin >> ws;
    getline(cin, city);
    cout << "Hello, " << name << " from " << city << "!" << endl;
    cout << "Next year you will be " << age + 1 << "." << endl;
    return 0;
}'''
EP6_STDIN = "Priya 17 Old Goa\n"
EP6_BUG = '''#include <iostream>
#include <string>
using namespace std;

int main() {
    string full_name;
    cout << "Full name? ";
    cin >> full_name;
    cout << "Hello, " << full_name << "!" << endl;
    return 0;
}'''
EP6_FIX = EP6_BUG.replace("cin >> full_name;", "getline(cin, full_name);")
EP6 = dict(ep=6, title="Reading input with cin", prereq="EP 05", **MOD,
 goals=["read numbers and words with cin >>", "read a whole line with getline", "know that cin >> stops at the first space"],
 yt=dict(title="Reading Input with cin and getline in C++ | C++ Programming EP 06",
   desc="Make your C++ program ask questions and listen: cin, getline and why cin stops at a space, with Xecxec.",
   tags=["c++ cin", "c++ getline", "c++ input", "cin vs getline", "c++ for beginners", "koding konkani", "c++ tutorial", "class 11 computer science", "first year engineering", "coding in goa"],
   thumb_text="READ INPUT: CIN", thumb_visual="in tomato on pastel blue; Xecxec with a claw cupped to an ear beside a speech bubble reading cin >> name; thin black border and drop shadow.",
   chapters={1: "Intro", 2: "How input works", 3: "cin and getline", 4: "Where the input goes", 5: "Run it in your head", 6: "Compile and run", 7: "Bug of the Day", 9: "Challenge", 10: "Next episode"}),
 files=[dict(name="greet.cpp", source=EP6_CODE, stdin=EP6_STDIN, scene="3, 5")],
 scenes=std_scenes((6, "READING INPUT WITH CIN"),
   "Until now our programs only talked. Today they listen. We will ask the user a question and read the answer, using cin and getline.",
   ("How input works", '"How input works": three numbered lines and a waiter-taking-an-order analogy card', "Lines spring in with a pop; the waiter card slides in with a notepad and a pencil",
    "Reading input is the opposite of printing. With cout, the arrows point at the screen. With cin, the arrows point at a variable, because the typed value flows into it. Cin reads one word at a time, and it stops at any space. When you want a whole line, with spaces, use getline. Think of a waiter. Cin writes down one item at a time. Getline writes down the whole order."),
   ("cin and getline", "`greet.cpp`: two variables, a prompt, then cin and getline",
    "[HL 6] We make two strings, name and city. [HL 7] And a whole number, age. [HL 8] The prompt asks for all three. [HL 9] Cin pushes the first word into name, and the next word into age. [HL 10] Cin ws skips the leftover spaces. [HL 11] Then getline reads everything left on the line, spaces and all, into city. [HL 12] Finally, we greet the user."),
   ("Where the input goes", "Three memory boxes: name = Priya, age = 17, city = Old Goa, with the typed line shown above them",
    "The typed line Priya 17 Old Goa appears; a bracket slides over each piece in turn and drops it into its box; the boxes fill with a pop, the last one taking two words",
    "Watch where each piece goes. The user types one line: Priya, seventeen, Old Goa. Cin takes the first word, Priya, and drops it in the name box. It takes the next, seventeen, and drops it in the age box. Then getline grabs the rest of the line, Old Goa, with the space inside, and drops it in the city box.", MB),
   ("Run it in your head", "`greet.cpp` again, with the typed input and the output panel on the right",
    "[HL 9] [TRACK name=Priya] Name becomes Priya. [TRACK age=17] Age becomes seventeen. [HL 11] [TRACK city=Old Goa] City becomes Old Goa. [HL 12] The first message prints Hello, Priya, from Old Goa. [HL 13] The second adds one to age, so it says eighteen."),
   ("Compile and run", "Terminal: `g++ greet.cpp -o greet`, then `./greet`, then the typed line",
    "Compile it and run it. The prompt appears. Type Priya, seventeen, Old Goa, and press enter. Hello, Priya, from Old Goa. Next year you will be eighteen. Your program just listened."),
   ("Bug of the Day", "BUG OF THE DAY: cin stops at the first space",
    "Bug of the Day. We ask for a full name, and the user types Priya Naik. But the program says, Hello, Priya. Where did Naik go? There is no error, because cin did exactly what it should. It stopped at the first space. The second word waits in the input, and nobody reads it. Use getline instead, and the whole name arrives.", RT_ANIM),
   ("Why is cin so polite? It stops listening at the first space.", "Why is cin so polite? It stops listening at the first space."),
   ("Task card: name, then favourite beach", "Your challenge: read a first name with cin, then a favourite beach with getline, and greet the user using both. Comment your answer below."),
   ("Next: EP 07 · Operators and expressions", "Next time: operators, and how C plus plus does arithmetic. Keep coding, says Xecxec!")),
 bug=dict(file="fullname.cpp", mode="runtime", show_fixed_out=True, stdin="Priya Naik\n", intro="cin >> reads only up to the first space", wrong=EP6_BUG, fix_intro="getline reads the whole line", fixed=EP6_FIX, expect=[],
   why="The >> operator stops at whitespace, so use getline(cin, variable) when the input can contain spaces."),
 pun="\"Why is cin so polite? It stops listening at the first space.\"",
 challenge="Read a first name with cin, then a favourite beach with getline, and greet the user with both.",
 answer="Use cin >> name >> ws; then getline(cin, beach); and print both in one greeting.",
 answer_code='''#include <iostream>
#include <string>
using namespace std;

int main() {
    string name, beach;
    cout << "Name and beach? ";
    cin >> name >> ws;
    getline(cin, beach);
    cout << "Hi " << name << ", enjoy " << beach << "!" << endl;
    return 0;
}''',
 answer_stdin="Rhea Palolem Beach\n",
 shorts=[
  dict(id="S1", title="cout versus cin", built=[2], hook="Arrows that point at a variable.", script="Arrows that point at a variable. With cout, the arrows point at the screen. With cin, they point the other way, into your variable. Type a value, and it flows in.", on="COUT >> SCREEN, CIN >> VARIABLE", caption="Which way do the arrows point?", tags=["cpp", "cin", "beginners", "kodingkonkani", "learntocode"]),
  dict(id="S2", title="cin then getline", built=[3], hook="One line, three kinds of reading.", script="One line, three kinds of reading. Cin takes a word. Cin takes a number. Then getline takes the rest of the line, spaces and all. Skip leftover spaces first with cin ws.", on="CIN, CIN, GETLINE", caption="Read words, numbers and lines.", tags=["cpp", "getline", "input", "kodingkonkani", "coding"]),
  dict(id="S3", title="Where does the input go?", built=[4], hook="Follow the typed line.", script="Follow the typed line. Priya, seventeen, Old Goa. Cin drops Priya into name, seventeen into age, and getline drops Old Goa into city. Each piece finds its box.", on="PRIYA 17 OLD GOA", caption="Follow the input.", tags=["cpp", "memory", "cin", "kodingkonkani", "beginners"]),
  dict(id="S4", title="Where did the surname go?", built=[7], hook="The surname that disappeared.", script="The surname that disappeared. Type Priya Naik, and cin only reads Priya, because it stops at the first space. No error, no warning. Use getline for full names.", on="CIN STOPS AT THE FIRST SPACE", caption="Use getline for full names.", tags=["cpp", "bugfix", "getline", "kodingkonkani", "coding"]),
  dict(id="S5", title="Pun and challenge", built=[8, 9], hook="Why is cin so polite?", script="Why is cin so polite? It stops listening at the first space. Your challenge: read a name with cin, a beach with getline, and greet the user. Full video: EP 6.", on="CIN + GETLINE GREETING", caption="Try the challenge.", tags=["cpp", "codingchallenge", "kodingkonkani", "programmingjokes", "goa"]),
 ])

# ---------------------------------------------------------------- EP7
EP7_CODE = '''#include <iostream>
using namespace std;

int main() {
    int students = 17;
    int groups = 5;
    cout << "Sum: " << students + groups << endl;
    cout << "Product: " << students * groups << endl;
    cout << "Quotient: " << students / groups << endl;
    cout << "Remainder: " << students % groups << endl;
    cout << "Mixed: " << 2 + 3 * 4 << endl;
    return 0;
}'''
EP7_BUG = '''#include <iostream>
using namespace std;

int main() {
    double half = 5 / 2;
    cout << "Half of 5: " << half << endl;
    return 0;
}'''
EP7_FIX = EP7_BUG.replace("5 / 2", "5.0 / 2")
EP7 = dict(ep=7, title="Operators and expressions", prereq="EP 06", **MOD,
 goals=["use + - * / and % on numbers", "predict the result of an expression using precedence", "know that dividing two ints throws away the decimal part"],
 yt=dict(title="C++ Operators: + - * / % and Precedence | C++ Programming EP 07",
   desc="Do arithmetic in C++: the five operators, the remainder, operator precedence and the integer division trap, with Xecxec.",
   tags=["c++ operators", "c++ arithmetic", "modulus operator", "integer division", "operator precedence", "koding konkani", "c++ for beginners", "c++ tutorial", "class 11 computer science", "coding in goa"],
   thumb_text="C++ MATHS", thumb_visual="in tomato on pastel blue; Xecxec juggling plus, minus, times, divide and percent signs; thin black border and drop shadow.",
   chapters={1: "Intro", 2: "The five operators", 3: "Maths in code", 4: "Who goes first?", 5: "Run it in your head", 6: "Compile and run", 7: "Bug of the Day", 9: "Challenge", 10: "Next episode"}),
 files=[dict(name="ops.cpp", source=EP7_CODE, scene="3, 5")],
 scenes=std_scenes((7, "OPERATORS AND EXPRESSIONS"),
   "Computers are brilliant at maths, but only if we ask in their language. Today we learn the symbols for adding, multiplying, dividing, and a surprising one for leftovers.",
   ("The five operators", '"The five operators": five numbered lines and a sharing-samosas analogy card', "Five lines spring in one by one with a pop; the samosa card slides in showing seventeen samosas on five plates",
    "C plus plus has five arithmetic operators. Plus adds. Minus subtracts. Star multiplies. Slash divides. And percent gives the remainder, what is left over after dividing. Imagine sharing seventeen samosas between five plates. Each plate gets three. That is the slash. Two samosas are left over. That is the percent. Try it on paper first: eleven divided by four, and eleven percent four."),
   ("Maths in code", "`ops.cpp`: two ints and five printed expressions",
    "[HL 5] Seventeen students. [HL 6] Five groups. [HL 7] Students plus groups is twenty-two. [HL 8] Students times groups is eighty-five. [HL 9] Now watch this. Students divided by groups is three, not three point four. Both numbers are ints, so C plus plus keeps only the whole part. [HL 10] Percent gives the remainder, which is two."),
   ("Who goes first?", "The expression 2 + 3 * 4 with the multiplication glowing first, then the addition, then the answer 14",
    "The expression appears; a bracket wraps 3 * 4 and turns it into 12; then 2 + 12 becomes 14; a tomato cross pops on the wrong answer 20; pop per step",
    "What does two plus three times four give? Not twenty. Multiplication, division and remainder go first. Addition and subtraction come after. So three times four is twelve, then two plus twelve is fourteen. If you want addition first, use round brackets. Two plus three, in brackets, times four, is twenty.", CS),
   ("Run it in your head", "`ops.cpp` again, with the output panel on the right",
    "[HL 5] [TRACK students=17] Students is seventeen. [HL 6] [TRACK groups=5] Groups is five. [HL 7] Twenty-two. [HL 8] Eighty-five. [HL 9] Three. [HL 10] Two. [HL 11] And fourteen, because the star goes first."),
   ("Compile and run", "Terminal: `g++ ops.cpp -o ops`, then `./ops`",
    "Compile and run. Sum, twenty-two. Product, eighty-five. Quotient, three. Remainder, two. Mixed, fourteen. All five answers match our predictions."),
   ("Bug of the Day", "BUG OF THE DAY: five divided by two gives two",
    "Bug of the Day. We want half of five, so we write double half equals five divided by two. It compiles with no warning, and prints two. Not two point five. Both five and two are ints, so the division happens on whole numbers first, and only then is the answer stored as a double. Make one side a decimal, write five point zero, and the answer is two point five.", RT_ANIM),
   ("I divided five by two and got two. The point got lost along the way.", "I divided five by two and got two. The point got lost along the way."),
   ("Task card: 250 minutes in hours and minutes", "Your challenge: turn two hundred fifty minutes into hours and minutes, using slash and percent. Comment your answer below."),
   ("Next: EP 08 · Comparison and logical operators", "Next time: comparing values and making decisions with true and false. Keep coding, says Xecxec!")),
 bug=dict(file="half.cpp", mode="runtime", show_fixed_out=True, intro="5 / 2 divides two ints", wrong=EP7_BUG, fix_intro="5.0 makes it a decimal division", fixed=EP7_FIX, expect=[],
   why="If both sides of a slash are ints, C++ divides as whole numbers and drops the decimal part; make at least one side a double."),
 pun="\"I divided five by two and got two. The point got lost along the way.\"",
 challenge="Turn 250 minutes into hours and minutes using / and %.",
 answer="Hours is 250 / 60, which is 4, and minutes is 250 % 60, which is 10.",
 answer_code='''#include <iostream>
using namespace std;

int main() {
    int total = 250;
    cout << total / 60 << " hours " << total % 60 << " minutes" << endl;
    return 0;
}''',
 shorts=[
  dict(id="S1", title="The five operators", built=[2], hook="Five symbols do all the maths.", script="Five symbols do all the maths. Plus, minus, star, slash, and percent. Seventeen samosas on five plates: slash says three each, percent says two left over.", on="+  -  *  /  %", caption="Five operators, one minute.", tags=["cpp", "operators", "beginners", "kodingkonkani", "learntocode"]),
  dict(id="S2", title="Integer division", built=[3], hook="Seventeen divided by five is three.", script="Seventeen divided by five is three. Not three point four. Two ints give an int, so the decimal part is thrown away. The remainder, with percent, is two.", on="17 / 5 = 3 AND 17 % 5 = 2", caption="Ints divide into ints.", tags=["cpp", "integerdivision", "maths", "kodingkonkani", "coding"]),
  dict(id="S3", title="Who goes first?", built=[4], hook="Two plus three times four.", script="Two plus three times four. Is it twenty? No, it is fourteen. Multiplication goes before addition. Use round brackets if you want the addition to go first.", on="2 + 3 * 4 = 14", caption="Precedence in 30 seconds.", tags=["cpp", "precedence", "maths", "kodingkonkani", "beginners"]),
  dict(id="S4", title="5 / 2 is 2", built=[7], hook="Half of five is two?", script="Half of five is two? Write five divided by two, and C plus plus prints two. Both numbers are ints. Write five point zero, and you get two point five.", on="5 / 2 = 2  BUT  5.0 / 2 = 2.5", caption="Make one side a decimal.", tags=["cpp", "bugfix", "integerdivision", "kodingkonkani", "coding"]),
  dict(id="S5", title="Pun and challenge", built=[8, 9], hook="Where did the point go?", script="Where did the point go? I divided five by two and got two. The point got lost along the way. Your challenge: turn two hundred fifty minutes into hours and minutes. Full video: EP 7.", on="250 MINUTES = ? HOURS ? MINUTES", caption="Try the challenge.", tags=["cpp", "codingchallenge", "kodingkonkani", "programmingjokes", "goa"]),
 ])

# ---------------------------------------------------------------- EP8
EP8_CODE = '''#include <iostream>
using namespace std;

int main() {
    int marks = 72;
    bool passed = marks >= 40;
    bool distinction = marks >= 75;
    bool merit = marks >= 60 && marks < 75;
    cout << boolalpha;
    cout << "Passed: " << passed << endl;
    cout << "Distinction: " << distinction << endl;
    cout << "Merit: " << merit << endl;
    cout << "Not passed: " << !passed << endl;
    cout << "Fail or topper: " << (marks < 40 || marks > 90) << endl;
    return 0;
}'''
EP8_BUG = '''#include <iostream>
using namespace std;

int main() {
    int level = 3;
    if (level = 5) {
        cout << "Level five!" << endl;
    }
    cout << "Level is " << level << endl;
    return 0;
}'''
EP8_FIX = EP8_BUG.replace("level = 5", "level == 5")
EP8 = dict(ep=8, title="Comparison and logical operators", prereq="EP 07", **MOD,
 goals=["compare values with == != < > <= >=", "combine conditions with && || !", "never confuse = (store) with == (compare)"],
 yt=dict(title="C++ Comparison and Logical Operators: == && || ! | C++ Programming EP 08",
   desc="Make true-or-false decisions in C++ with comparison and logical operators, and avoid the famous = versus == mistake, with Xecxec.",
   tags=["c++ comparison operators", "c++ logical operators", "and or not", "== vs =", "c++ boolean", "koding konkani", "c++ for beginners", "c++ tutorial", "class 11 computer science", "coding in goa"],
   thumb_text="TRUE OR FALSE?", thumb_visual="in tomato on pastel blue; Xecxec holding a green TRUE card in one claw and a red FALSE card in the other; thin black border and drop shadow.",
   chapters={1: "Intro", 2: "Questions with yes or no", 3: "Comparing in code", 4: "AND, OR, NOT", 5: "Run it in your head", 6: "Compile and run", 7: "Bug of the Day", 9: "Challenge", 10: "Next episode"}),
 files=[dict(name="marks.cpp", source=EP8_CODE, scene="3, 5")],
 scenes=std_scenes((8, "COMPARE AND DECIDE"),
   "Programs make decisions, and every decision starts with a question that has only two answers: true, or false. Today we learn how to ask those questions.",
   ("Questions with two answers", '"Questions with two answers": three numbered lines and a bouncer-at-the-door analogy card', "Lines spring in with a pop; the bouncer card slides in with a checklist of entry rules",
    "A comparison asks a question about two values, and the answer is a bool. Double equals asks, are they equal? Exclamation equals asks, are they different? Then less than, greater than, and the versions with equals, for at least and at most. Think of a bouncer at a beach party. Are you eighteen or older? True, come in. False, sorry."),
   ("Comparing in code", "`marks.cpp`: three bool variables built from comparisons",
    "[HL 5] Marks is seventy-two. [HL 6] Passed asks, is marks at least forty? True. [HL 7] Distinction asks, is marks at least seventy-five? False. [HL 8] Merit uses two questions joined by double ampersand, which means and. Marks at least sixty, and marks below seventy-five. Both must be true. [HL 9] Boolalpha makes cout print true and false as words, instead of one and zero."),
   ("AND, OR, NOT", "A table with three rows: A && B, A || B, !A, and the four true/false combinations of A and B",
    "The table rows fill in one by one with mint ticks for true and tomato crosses for false; the row being explained glows butter; pop per row",
    "Three tools combine questions. And, written as double ampersand, is true only when both sides are true. Or, written as double bar, is true when at least one side is true. Not, an exclamation mark, flips true into false, and false into true. Say it as a sentence: passed and not distinction. Read your conditions aloud, and mistakes become easy to hear.", CS),
   ("Run it in your head", "`marks.cpp` again, with the output panel on the right",
    "[HL 5] [TRACK marks=72] Marks is seventy-two. [HL 10] Passed is true. [HL 11] Distinction is false. [HL 12] Merit is true, because seventy-two is between sixty and seventy-five. [HL 13] Not passed flips true into false. [HL 14] And fail or topper is false, because seventy-two is neither below forty nor above ninety."),
   ("Compile and run", "Terminal: `g++ marks.cpp -o marks`, then `./marks`",
    "Compile and run. Passed, true. Distinction, false. Merit, true. Not passed, false. Fail or topper, false. Five questions, five clear answers."),
   ("Bug of the Day", "BUG OF THE DAY: one equals sign instead of two",
    "Bug of the Day. We write if level equals five, with a single equals sign. The compiler warns: suggest parentheses around assignment used as truth value. It is only a warning, so the program runs. And it prints Level five, then Level is five. But level was three! A single equals sign stores five into level, and five counts as true. Use double equals to compare, and the message correctly stays hidden.", WARN_ANIM),
   ("Why did the single equals sign get arrested? It assigned when it should have compared.", "Why did the single equals sign get arrested? It assigned when it should have compared."),
   ("Task card: even and positive", "Your challenge: write a bool that is true only when a number is even and also greater than zero. Test it with minus four, then four. Comment your answer below."),
   ("Next: EP 09 · Type conversion and casting", "Next time: converting between int and double, safely. Keep coding, says Xecxec!")),
 bug=dict(file="level.cpp", mode="runtime", show_fixed_out=True, intro="if (level = 5) stores instead of comparing", wrong=EP8_BUG, fix_intro="double equals compares", fixed=EP8_FIX, expect=["suggest parentheses around assignment used as truth value"],
   why="A single = stores a value and the stored value counts as true, so use == whenever you want to compare."),
 pun="\"Why did the single equals sign get arrested? It assigned when it should have compared.\"",
 challenge="Write a bool that is true only when a number is even and greater than zero, and test it with -4 and 4.",
 answer="Use n % 2 == 0 && n > 0: it is false for -4 and true for 4.",
 answer_code='''#include <iostream>
using namespace std;

int main() {
    int a = -4;
    int b = 4;
    cout << boolalpha;
    cout << (a % 2 == 0 && a > 0) << endl;
    cout << (b % 2 == 0 && b > 0) << endl;
    return 0;
}''',
 shorts=[
  dict(id="S1", title="Comparison operators", built=[2], hook="Every question has two answers.", script="Every question has two answers. Double equals asks, are they equal? Exclamation equals asks, are they different? Less than and greater than ask which is bigger. The answer is always true or false.", on="==  !=  <  >  <=  >=", caption="Ask true-or-false questions.", tags=["cpp", "operators", "beginners", "kodingkonkani", "learntocode"]),
  dict(id="S2", title="Marks and merit", built=[3], hook="Between sixty and seventy-five.", script="Between sixty and seventy-five. Marks at least sixty, and marks below seventy-five. Two questions joined by double ampersand, and both must be true. Seventy-two passes the test.", on="MARKS >= 60 && MARKS < 75", caption="Join two questions.", tags=["cpp", "logicaloperators", "coding", "kodingkonkani", "beginners"]),
  dict(id="S3", title="AND, OR, NOT", built=[4], hook="And, or, not in thirty seconds.", script="And, or, not in thirty seconds. And needs both sides true. Or needs just one. Not flips the answer. Read your condition aloud as a sentence, and the mistakes jump out.", on="&&   ||   !", caption="Three tools, one truth table.", tags=["cpp", "truthtable", "logic", "kodingkonkani", "learntocode"]),
  dict(id="S4", title="= versus ==", built=[7], hook="One missing equals sign.", script="One missing equals sign. Write if level equals five with a single equals, and the program stores five instead of asking. g plus plus only warns, so the bug hides. Use double equals to compare.", on="IF (LEVEL = 5) IS A BUG", caption="Store with =, compare with ==.", tags=["cpp", "bugfix", "comparison", "kodingkonkani", "coding"]),
  dict(id="S5", title="Pun and challenge", built=[8, 9], hook="The equals sign got arrested.", script="The equals sign got arrested. It assigned when it should have compared. Your challenge: a bool that is true only for even numbers above zero. Test minus four and four. Full video: EP 8.", on="EVEN AND POSITIVE?", caption="Try the challenge.", tags=["cpp", "codingchallenge", "kodingkonkani", "programmingjokes", "goa"]),
 ])

# ---------------------------------------------------------------- EP9
EP9_CODE = '''#include <iostream>
using namespace std;

int main() {
    int total = 17;
    int people = 5;
    double average = static_cast<double>(total) / people;
    int rounded = static_cast<int>(average);
    cout << "Average: " << average << endl;
    cout << "Rounded down: " << rounded << endl;
    return 0;
}'''
EP9_BUG = '''#include <iostream>
using namespace std;

int main() {
    int whole{3.7};
    cout << "Whole: " << whole << endl;
    return 0;
}'''
EP9_FIX = EP9_BUG.replace("int whole{3.7};", "int whole = static_cast<int>(3.7);")
EP9 = dict(ep=9, title="Type conversion and casting", prereq="EP 08", **MOD,
 goals=["explain implicit conversion between int and double", "convert on purpose with static_cast", "recognise a narrowing conversion error in braces"],
 yt=dict(title="Type Conversion and static_cast in C++ | C++ Programming EP 09",
   desc="See how C++ converts between int and double, how to convert on purpose with static_cast, and why braces refuse to lose data, with Xecxec.",
   tags=["c++ type conversion", "static_cast", "implicit conversion", "narrowing conversion", "int to double", "koding konkani", "c++ for beginners", "c++ tutorial", "class 11 computer science", "coding in goa"],
   thumb_text="CASTING TYPES", thumb_visual="in tomato on pastel blue; Xecxec pouring a double-shaped jug into an int-shaped glass with drops spilling; thin black border and drop shadow.",
   chapters={1: "Intro", 2: "Changing types", 3: "static_cast in code", 4: "Widening and narrowing", 5: "Run it in your head", 6: "Compile and run", 7: "Bug of the Day", 9: "Challenge", 10: "Next episode"}),
 files=[dict(name="convert.cpp", source=EP9_CODE, scene="3, 5")],
 scenes=std_scenes((9, "TYPE CONVERSION AND CASTING"),
   "Sometimes a value is the wrong type for the job. An int needs to become a double, or a double needs to become an int. Today we learn to convert between types, on purpose and safely.",
   ("Changing types", '"Changing types": three numbered lines and a measuring-jug analogy card', "Lines spring in with a pop; the jug card slides in with a big jug, a small glass and drops spilling",
    "C plus plus converts types in two ways. Implicit conversion happens by itself. Add an int and a double, and the int quietly becomes a double. That is safe, like pouring a small glass into a big jug. The other way is risky. Putting a double into an int throws away the decimal part, like pouring a big jug into a small glass. So when you really want that, say it out loud, with static cast."),
   ("static_cast in code", "`convert.cpp`: total and people, then two static_cast lines",
    "[HL 5] Total is seventeen. [HL 6] People is five. [HL 7] Here is the fix for integer division. Static cast to double turns total into seventeen point zero before dividing. Now a double divided by an int is a decimal division, so the average is three point four. [HL 8] And going back, static cast to int cuts off the decimal part. Three point four becomes three. It does not round, it truncates."),
   ("Widening and narrowing", "Two jugs: int to double with a tick and no loss; double to int with a cross and the .4 dropped",
    "A small int glass pours into a big double jug and everything fits, mint tick; then the double jug pours into the int glass and the decimal drops are lost, tomato cross; pop per step",
    "Widening means going to a bigger type, like int to double. Nothing is lost. Narrowing means going to a smaller type, like double to int. Something is lost, here the decimal part. Narrowing is where bugs hide, so C plus plus gives you a safety net. When you use curly braces to create a variable, the compiler refuses any narrowing it can see.", CS),
   ("Run it in your head", "`convert.cpp` again, with the output panel on the right",
    "[HL 5] [TRACK total=17] Total is seventeen. [HL 6] [TRACK people=5] People is five. [HL 7] [TRACK average=3.4] Average is seventeen divided by five, which is three point four. [HL 8] [TRACK rounded=3] Rounded is three. [HL 9] The first line prints three point four. [HL 10] The second prints three."),
   ("Compile and run", "Terminal: `g++ convert.cpp -o convert`, then `./convert`",
    "Compile and run. Average, three point four. Rounded down, three. Without the cast, the average would have been three. The cast made all the difference."),
   ("Bug of the Day", "BUG OF THE DAY: a double squeezed into an int with braces",
    "Bug of the Day. We write int whole in curly braces with three point seven inside. The compiler says, narrowing conversion of three point seven from double to int. This time it is a real error, so nothing is built. Braces refuse to lose data silently. If you truly want three, say so with static cast to int. Then the program prints Whole, three.", "Butter banner drops in with a buzzer; wrong code shakes; the g++ narrowing error appears in tomato; the fix slides in and the output turns mint with a ding"),
   ("A double tried to fit into an int. The compiler said: sorry, no extra decimals allowed.", "A double tried to fit into an int. The compiler said, sorry, no extra decimals allowed."),
   ("Task card: average of three marks", "Your challenge: the marks are seventy-two, sixty-five and ninety. Find their average as a double, then print it rounded down as an int. Comment your answer below."),
   ("Next: EP 10 · auto, const and constexpr", "Next time: auto, const and constexpr, the keywords that protect your values. Keep coding, says Xecxec!")),
 bug=dict(file="whole.cpp", intro="int whole{3.7} narrows a double", wrong=EP9_BUG, fix_intro="static_cast says it on purpose", fixed=EP9_FIX, expect=["narrowing conversion of", "from 'double' to 'int'"], show_fixed_out=True,
   why="Curly braces refuse to lose data by accident; if you really want to drop the decimal part, say so with static_cast<int>."),
 pun="\"A double tried to fit into an int. The compiler said: sorry, no extra decimals allowed.\"",
 challenge="Find the average of the marks 72, 65 and 90 as a double, then print it rounded down as an int.",
 answer="Cast the sum to double before dividing by 3; the average is about 75.6667 and the int is 75.",
 answer_code='''#include <iostream>
using namespace std;

int main() {
    int sum = 72 + 65 + 90;
    double average = static_cast<double>(sum) / 3;
    cout << average << endl;
    cout << static_cast<int>(average) << endl;
    return 0;
}''',
 shorts=[
  dict(id="S1", title="Big jug, small glass", built=[2], hook="Pouring a jug into a glass.", script="Pouring a jug into a glass. An int into a double fits easily. A double into an int spills the decimals. When you want that, say it out loud with static cast.", on="INT TO DOUBLE IS SAFE", caption="Widening is safe, narrowing spills.", tags=["cpp", "typeconversion", "beginners", "kodingkonkani", "learntocode"]),
  dict(id="S2", title="Fix integer division", built=[3], hook="Make seventeen divided by five exact.", script="Make seventeen divided by five exact. Cast the total to double first, then divide. Three point four, not three. One small cast saves your decimals.", on="STATIC_CAST<DOUBLE>(TOTAL) / PEOPLE", caption="Cast before you divide.", tags=["cpp", "staticcast", "coding", "kodingkonkani", "maths"]),
  dict(id="S3", title="Truncate, not round", built=[4], hook="Three point nine becomes three.", script="Three point nine becomes three. Casting a double to an int cuts the decimals off. It does not round. If you want rounding, that is a different tool.", on="STATIC_CAST<INT>(3.9) = 3", caption="Casting truncates.", tags=["cpp", "casting", "programming", "kodingkonkani", "beginners"]),
  dict(id="S4", title="Narrowing conversion", built=[7], hook="Braces refuse to lose data.", script="Braces refuse to lose data. Write int whole in braces with three point seven, and g plus plus says, narrowing conversion from double to int. It is a real error. Use static cast instead.", on="NARROWING CONVERSION OF 3.7", caption="Braces are a safety net.", tags=["cpp", "bugfix", "narrowing", "kodingkonkani", "compilererror"]),
  dict(id="S5", title="Pun and challenge", built=[8, 9], hook="No extra decimals allowed.", script="No extra decimals allowed. A double tried to fit into an int, and the compiler said sorry. Your challenge: the average of seventy-two, sixty-five and ninety. Full video: EP 9.", on="AVERAGE OF 72, 65, 90", caption="Try the challenge.", tags=["cpp", "codingchallenge", "kodingkonkani", "programmingjokes", "goa"]),
 ])

# ---------------------------------------------------------------- EP10
EP10_CODE = '''#include <iostream>
using namespace std;

constexpr double kGst = 0.18;

int main() {
    const int tables = 8;
    auto price = 250.0;
    auto seats = 4;
    auto total = price * (1 + kGst);
    cout << "Tables: " << tables << endl;
    cout << "Seats: " << seats << endl;
    cout << "Total: " << total << endl;
    return 0;
}'''
EP10_BUG = '''#include <iostream>
using namespace std;

int main() {
    const int tables = 8;
    tables = 9;
    cout << "Tables: " << tables << endl;
    return 0;
}'''
EP10_FIX = EP10_BUG.replace("const int tables = 8;\n    tables = 9;", "const int tables = 9;")
EP10 = dict(ep=10, title="auto, const and constexpr", prereq="EP 09", **MOD,
 goals=["let the compiler pick a type with auto", "protect a value with const", "name a fixed number with constexpr"],
 yt=dict(title="auto, const and constexpr in C++ | C++ Programming EP 10",
   desc="Let the compiler guess types with auto, lock values with const and name fixed numbers with constexpr, with Xecxec.",
   tags=["c++ auto", "c++ const", "c++ constexpr", "const vs constexpr", "read-only variable", "koding konkani", "c++ for beginners", "c++ tutorial", "class 11 computer science", "coding in goa"],
   thumb_text="AUTO + CONST", thumb_visual="in tomato on pastel blue; Xecxec locking a box with a padlock labelled const; thin black border and drop shadow.",
   chapters={1: "Intro", 2: "Three keywords", 3: "Reading the code", 4: "A locked box", 5: "Run it in your head", 6: "Compile and run", 7: "Bug of the Day", 9: "Challenge", 10: "Next episode"}),
 files=[dict(name="shop.cpp", source=EP10_CODE, scene="3, 5")],
 scenes=std_scenes((10, "AUTO, CONST, CONSTEXPR"),
   "Three little keywords make your code shorter and safer. Auto lets the compiler pick the type. Const locks a value. And constexpr names a number that never changes. Let us meet them.",
   ("Three keywords", '"Three keywords": three numbered lines and a padlock-on-a-locker analogy card', "Lines spring in with a pop; the locker card slides in with a padlock clicking shut",
    "Auto says, you work out the type from the value. Write auto x equals four, and x is an int. Const says, once this has a value, nobody may change it. Constexpr goes one step further. It says, this value is known before the program even runs, so it is perfect for fixed numbers like a tax rate. Think of a locker at the shack. Once you lock your bag, nobody changes what is inside."),
   ("Reading the code", "`shop.cpp`: a constexpr at the top, then const and three auto variables",
    "[HL 4] A constexpr double, the tax rate, eighteen percent, named with a k in front. It lives outside main, so every function can see it. [HL 7] Const int tables is eight. This one is locked. [HL 8] Auto price equals two hundred fifty point zero. The compiler sees a decimal, so price is a double. [HL 9] Auto seats equals four. A whole number, so seats is an int. [HL 10] And auto total takes its type from the maths, a double."),
   ("A locked box", "Two memory boxes: tables = 8 with a padlock icon and a read-only tag, price = 250.0 open and editable",
    "The two boxes pop in; a padlock snaps onto the tables box with a click; an arrow tries to write 9 into it and bounces off with a buzzer; an arrow writes into price and succeeds",
    "Here is const in memory. The tables box has a padlock. You can read it as much as you like, but any attempt to write into it is blocked, and the compiler stops you before the program runs. The price box has no lock, so we can still change it later. Use const for everything that should not change. It tells readers, and the compiler, what you meant.", MB),
   ("Run it in your head", "`shop.cpp` again, with the output panel on the right",
    "[HL 7] [TRACK tables=8] Tables is eight, locked. [HL 8] [TRACK price=250.0] Price is two hundred fifty. [HL 9] [TRACK seats=4] Seats is four. [HL 10] [TRACK total=295] Total is price times one point one eight, which is two hundred ninety-five. [HL 11] The first line prints eight. [HL 13] The last prints two hundred ninety-five."),
   ("Compile and run", "Terminal: `g++ shop.cpp -o shop`, then `./shop`",
    "Compile and run. Tables, eight. Seats, four. Total, two hundred ninety-five. Notice we never wrote the word double or int on the three auto lines, yet the numbers came out right."),
   ("Bug of the Day", "BUG OF THE DAY: assigning to a const",
    "Bug of the Day. We lock tables with const, then try to set it to nine. The compiler says, assignment of read-only variable tables. That is the padlock doing its job. This is a real error, so no program is built. If the value truly must change, remove const. If it must not, fix the line that tries to change it. Here, we simply start with nine.", "Butter banner drops in with a buzzer; wrong code shakes; the g++ read-only error appears in tomato; the fix slides in and the output turns mint with a ding"),
   ("Why can't a const go to parties? It refuses to change.", "Why can't a const go to parties? It refuses to change."),
   ("Task card: circle area with pi", "Your challenge: make a constexpr for pi, three point one four one five nine. Make a const radius of five. Print the area, pi times radius times radius. Comment your answer below."),
   ("Next: EP 11 · Strings with std::string", "Next time: strings, which are text you can join, measure and change. Keep coding, says Xecxec!")),
 bug=dict(file="locked.cpp", intro="tables is const but gets a new value", wrong=EP10_BUG, fix_intro="start with the value we want", fixed=EP10_FIX, expect=["assignment of read-only variable 'tables'"], show_fixed_out=True,
   why="A const variable can be set only once, when it is created, so the compiler rejects any later assignment."),
 pun="\"Why can't a const go to parties? It refuses to change.\"",
 challenge="Make a constexpr for pi (3.14159) and a const radius of 5, then print the area of the circle.",
 answer="Print kPi * radius * radius; the area is about 78.5397.",
 answer_code='''#include <iostream>
using namespace std;

constexpr double kPi = 3.14159;

int main() {
    const int radius = 5;
    cout << "Area: " << kPi * radius * radius << endl;
    return 0;
}''',
 shorts=[
  dict(id="S1", title="Three keywords", built=[2], hook="Three keywords, three jobs.", script="Three keywords, three jobs. Auto lets the compiler pick the type. Const locks a value after it is set. Constexpr names a number that is known before the program even runs.", on="AUTO  CONST  CONSTEXPR", caption="Three keywords in 30 seconds.", tags=["cpp", "constexpr", "beginners", "kodingkonkani", "learntocode"]),
  dict(id="S2", title="auto picks the type", built=[3], hook="You do not always have to say int.", script="You do not always have to say int. Write auto price equals two hundred fifty point zero, and the compiler sees a decimal, so price is a double. Auto seats equals four becomes an int.", on="AUTO PRICE = 250.0", caption="Let the compiler decide.", tags=["cpp", "auto", "coding", "kodingkonkani", "beginners"]),
  dict(id="S3", title="A padlock for a variable", built=[4], hook="Lock a value with one word.", script="Lock a value with one word. Const puts a padlock on the box. You can read what is inside as often as you like, but nobody can change it. The compiler enforces it.", on="CONST = A PADLOCK", caption="Const protects your values.", tags=["cpp", "const", "programming", "kodingkonkani", "learntocode"]),
  dict(id="S4", title="Assignment of read-only variable", built=[7], hook="You cannot change a const.", script="You cannot change a const. Try, and g plus plus says, assignment of read-only variable tables. It is a real error, so nothing is built. Remove the extra line, or start with the value you want.", on="ASSIGNMENT OF READ-ONLY VARIABLE", caption="Const means set once.", tags=["cpp", "bugfix", "const", "kodingkonkani", "compilererror"]),
  dict(id="S5", title="Pun and challenge", built=[8, 9], hook="A const at a party.", script="A const at a party. Why can't a const go? It refuses to change. Your challenge: a constexpr pi, a const radius, and the area of a circle. Full video: EP 10.", on="AREA = PI * R * R", caption="Try the challenge.", tags=["cpp", "codingchallenge", "kodingkonkani", "programmingjokes", "goa"]),
 ])

# ---------------------------------------------------------------- EP11
EP11_CODE = '''#include <iostream>
#include <string>
using namespace std;

int main() {
    string first = "Goa";
    string second = "Beach";
    string full = first + " " + second;
    cout << full << endl;
    cout << "Length: " << full.length() << endl;
    cout << "First letter: " << full[0] << endl;
    full += "es";
    cout << full << endl;
    return 0;
}'''
EP11_BUG = '''#include <iostream>
#include <string>
using namespace std;

int main() {
    string msg = "Hello, " + "Goa";
    cout << msg << endl;
    return 0;
}'''
EP11_FIX = EP11_BUG.replace('"Hello, " + "Goa"', 'string("Hello, ") + "Goa"')
EP11 = dict(ep=11, title="Strings with std::string", prereq="EP 10", **MOD,
 goals=["create and join strings with +", "measure a string with .length() and read a letter with [ ]", "know why two string literals cannot be added"],
 yt=dict(title="C++ Strings: std::string, +, length() | C++ Programming EP 11",
   desc="Store, join and measure text in C++ with std::string, and find out why adding two quoted pieces of text fails, with Xecxec.",
   tags=["c++ string", "std::string", "string length", "string concatenation", "c++ for beginners", "koding konkani", "c++ tutorial", "invalid operands", "class 11 computer science", "coding in goa"],
   thumb_text="C++ STRINGS", thumb_visual="in tomato on pastel blue; Xecxec threading letter beads G, O, A onto a string; thin black border and drop shadow.",
   chapters={1: "Intro", 2: "Text as a string", 3: "Joining and measuring", 4: "Letters in memory", 5: "Run it in your head", 6: "Compile and run", 7: "Bug of the Day", 9: "Challenge", 10: "Next episode"}),
 files=[dict(name="strings.cpp", source=EP11_CODE, scene="3, 5")],
 scenes=std_scenes((11, "STRINGS WITH STD::STRING"),
   "Numbers are only half of programming. The other half is text: names, messages and words. In C plus plus, text lives in a type called string, and today we learn to join it, measure it and pick it apart.",
   ("Text as a string", '"Text as a string": three numbered lines and a bead-necklace analogy card', "Lines spring in with a pop; the necklace card slides in with letter beads numbered from zero",
    "A string is a row of characters. To use it, include the string header, then write string, a name, and a value in double quotes. Plus joins two strings together. Dot length tells you how many characters it holds. And square brackets pick out one character, counting from zero, not from one. Think of a necklace of letter beads. The first bead is bead zero."),
   ("Joining and measuring", "`strings.cpp`: two strings, a joined one, then length, first letter and an append",
    "[HL 6] First is Goa. [HL 7] Second is Beach. [HL 8] Full joins first, a space in quotes, and second. Without the space, the words would stick together. [HL 9] Printing full gives Goa Beach. [HL 10] Dot length counts every character, including the space. [HL 11] Full in square brackets with zero picks the first letter. [HL 12] And plus equals adds the letters e and s to the end."),
   ("Letters in memory", "Nine character boxes holding G, o, a, space, B, e, a, c, h, numbered 0 to 8, under the label full",
    "The nine boxes pop in left to right with index numbers underneath; a pointer arrow marks box 0 and the letter G lifts out; the length bracket 9 spans all boxes; pop per box",
    "Here is the string full in memory. Nine boxes, one per character, numbered from zero to eight. The space is a character too, in box three. That is why the length is nine, not eight. And index zero is the letter G. If you ask for an index past the end, you reach outside the string, so always stay between zero and length minus one.", MB),
   ("Run it in your head", "`strings.cpp` again, with the output panel on the right",
    "[HL 6] [TRACK first=Goa] First is Goa. [HL 7] [TRACK second=Beach] Second is Beach. [HL 8] [TRACK full=Goa Beach] Full is Goa Beach. [HL 9] The first print says, Goa Beach. [HL 10] The length is nine. [HL 11] The first letter is G. [HL 12] [TRACK full=Goa Beaches] After plus equals, full becomes Goa Beaches. [HL 13] And that is the last line."),
   ("Compile and run", "Terminal: `g++ strings.cpp -o strings`, then `./strings`",
    "Compile and run. Goa Beach. Length, nine. First letter, G. And Goa Beaches. Four lines, four string tools, one tidy program."),
   ("Bug of the Day", "BUG OF THE DAY: adding two string literals",
    "Bug of the Day. We try to build a message by adding hello comma, in quotes, and Goa, in quotes. The compiler says, invalid operands of types const char array and const char array to binary operator plus. Quoted text is not a string yet. It is a plain array of characters, and plus does not work on two of those. Wrap one side in string, and plus works.", "Butter banner drops in with a buzzer; wrong code shakes; the g++ invalid operands error appears in tomato; the fix slides in and the output turns mint with a ding"),
   ("I tried to add two string literals. The compiler said we are not compatible: invalid operands.", "I tried to add two string literals. The compiler said we are not compatible: invalid operands."),
   ("Task card: your full name and its length", "Your challenge: join your first and last name with a space between them. Print the full name and how many characters it has. Comment your answer below."),
   ("Next: EP 12 · Formatting output", "Next time: formatting output, so numbers line up like a proper price list. Keep coding, says Xecxec!")),
 bug=dict(file="hello_goa.cpp", intro="two quoted pieces of text are added", wrong=EP11_BUG, fix_intro="one side is wrapped in string", fixed=EP11_FIX, expect=["invalid operands of types"], show_fixed_out=True,
   why="Text in double quotes is a plain character array, not a string, so at least one side of + must be a std::string."),
 pun="\"I tried to add two string literals. The compiler said we are not compatible: invalid operands.\"",
 challenge="Join your first and last name with a space between them, then print the full name and its length.",
 answer="Use first + \" \" + last, then print full and full.length().",
 answer_code='''#include <iostream>
#include <string>
using namespace std;

int main() {
    string first = "Priya";
    string last = "Naik";
    string full = first + " " + last;
    cout << full << endl;
    cout << full.length() << endl;
    return 0;
}''',
 shorts=[
  dict(id="S1", title="Text is a string", built=[2], hook="Text in C++ is a row of beads.", script="Text in C plus plus is a row of beads. Include string, then write string, a name and a value in quotes. Plus joins strings. Dot length counts the characters.", on="STRING = A ROW OF CHARACTERS", caption="Meet std::string.", tags=["cpp", "strings", "beginners", "kodingkonkani", "learntocode"]),
  dict(id="S2", title="Join and measure", built=[3], hook="Goa plus Beach equals Goa Beach.", script="Goa plus Beach equals Goa Beach, if you add the space yourself. Then dot length says nine, because the space counts. Square brackets with zero give the first letter, G.", on="\"GOA\" + \" \" + \"BEACH\"", caption="Join strings with plus.", tags=["cpp", "stringconcatenation", "coding", "kodingkonkani", "beginners"]),
  dict(id="S3", title="Count from zero", built=[4], hook="The first letter is number zero.", script="The first letter is number zero. A string of nine characters has places zero to eight. The space counts as a character too. Always stay between zero and length minus one.", on="INDEX 0 TO 8", caption="Strings count from zero.", tags=["cpp", "index", "programming", "kodingkonkani", "learntocode"]),
  dict(id="S4", title="Invalid operands", built=[7], hook="Two quoted texts cannot be added.", script="Two quoted texts cannot be added. Write hello in quotes plus Goa in quotes, and g plus plus says, invalid operands. Quoted text is not a string yet. Wrap one side in string.", on="INVALID OPERANDS TO BINARY +", caption="Wrap one side in string().", tags=["cpp", "bugfix", "strings", "kodingkonkani", "compilererror"]),
  dict(id="S5", title="Pun and challenge", built=[8, 9], hook="Two literals, not compatible.", script="Two literals, not compatible. I tried to add two string literals, and the compiler said, invalid operands. Your challenge: join your first and last name and print the length. Full video: EP 11.", on="FULL NAME + LENGTH", caption="Try the challenge.", tags=["cpp", "codingchallenge", "kodingkonkani", "programmingjokes", "goa"]),
 ])

# ---------------------------------------------------------------- EP12
EP12_CODE = '''#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    double price = 249.5;
    cout << fixed << setprecision(2);
    cout << left << setw(10) << "Item" << right << setw(8) << "Price" << endl;
    cout << left << setw(10) << "Fish" << right << setw(8) << price << endl;
    cout << left << setw(10) << "Prawns" << right << setw(8) << 399.0 << endl;
    return 0;
}'''
EP12_BUG = '''#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    double pi = 3.14159;
    cout << setprecision(2) << pi << endl;
    return 0;
}'''
EP12_FIX = EP12_BUG.replace("setprecision(2)", "fixed << setprecision(2)")
EP12 = dict(ep=12, title="Formatting output", prereq="EP 11", **MOD,
 goals=["set column widths with setw and alignment with left and right", "control decimals with fixed and setprecision", "know that setprecision alone counts all digits"],
 yt=dict(title="Formatting Output in C++: setw, setprecision, fixed | C++ Programming EP 12",
   desc="Make C++ output look tidy: line up columns with setw and control decimal places with fixed and setprecision, with Xecxec.",
   tags=["c++ setw", "c++ setprecision", "c++ fixed", "iomanip", "format output c++", "koding konkani", "c++ for beginners", "c++ tutorial", "class 11 computer science", "coding in goa"],
   thumb_text="TIDY OUTPUT", thumb_visual="in tomato on pastel blue; Xecxec holding a neat price-list card with aligned columns; thin black border and drop shadow.",
   chapters={1: "Intro", 2: "Why format?", 3: "A price list", 4: "Width and precision", 5: "Run it in your head", 6: "Compile and run", 7: "Bug of the Day", 9: "Challenge", 10: "Next module"}),
 files=[dict(name="menu.cpp", source=EP12_CODE, scene="3, 5")],
 scenes=std_scenes((12, "FORMATTING OUTPUT"),
   "Your numbers are correct, but do they look good? Today we make output tidy, with neat columns and exactly the number of decimals we want, using a header called iomanip.",
   ("Why format?", '"Why format?": three numbered lines and a messy-versus-neat price-board analogy card', "Lines spring in with a pop; the card slides in showing a crooked chalkboard menu next to a tidy printed one",
    "Raw output is honest but untidy. Prices of different lengths wobble out of line, and decimals run on. Include iomanip, and you get tools. Setw sets the width of the next item. Left and right choose which side the text sticks to. Fixed tells cout to count decimals after the point. And setprecision says how many. Think of a menu board at a shack. A tidy board sells more fish."),
   ("A price list", "`menu.cpp`: setup line, a header row and two item rows",
    "[HL 7] Fixed and setprecision two, set once, stay for the rest of the program. Every double now shows two decimals. [HL 8] The header row. Left and setw ten, so Item sits in a ten-wide column, pushed to the left. Then right and setw eight, so Price sits in an eight-wide column, pushed to the right. [HL 9] Same pattern for Fish and its price. [HL 10] And again for Prawns."),
   ("Width and precision", "Two rows of boxes: a ten-box strip with Fish at the left and an eight-box strip with 249.50 at the right",
    "Empty column strips appear; the text Fish drops into the left of the ten-wide strip and the number 249.50 into the right of the eight-wide strip; spare boxes fill with dots; pop per placement", 
    "Setw reserves boxes. Ten boxes for the name, and the word Fish fills four of them. Left alignment pushes it to the start, and the spare six stay empty. Eight boxes for the price. The number two hundred forty-nine point five zero fills six, and right alignment pushes it to the end. Setw only affects the very next item, which is why we repeat it on every column.", CS),
   ("Run it in your head", "`menu.cpp` again, with the output panel on the right",
    "[HL 6] [TRACK price=249.5] Price is two hundred forty-nine point five. [HL 7] From here on, doubles show two decimals. [HL 8] The header is Item, then Price on the right edge. [HL 9] Fish and two hundred forty-nine point five zero. Notice the extra zero, added by fixed. [HL 10] And Prawns with three hundred ninety-nine point zero zero."),
   ("Compile and run", "Terminal: `g++ menu.cpp -o menu`, then `./menu`",
    "Compile and run. A tidy table appears. Names line up on the left. Prices line up on the right, each with two decimals. That is the same data as before, but now it is easy to read."),
   ("Bug of the Day", "BUG OF THE DAY: setprecision without fixed",
    "Bug of the Day. We want pi with two decimals, so we write setprecision two. It prints three point one. Only two digits in total! Without fixed, setprecision counts all digits, before and after the point. Add fixed, and setprecision counts only the digits after the point. Now the output is three point one four. No error, so you have to notice the output.", RT_ANIM),
   ("setprecision without fixed is like a Goa thali with no rice: something important is missing.", "Setprecision without fixed is like a Goa thali with no rice. Something important is missing."),
   ("Task card: a three-row price table", "Your challenge: print a table with three items. Names on the left, prices on the right, every price with two decimals. Comment your answer below."),
   ("Next: Module 2 · Making decisions", "Module one is done! Next time: making decisions with if and else. Keep coding, says Xecxec!")),
 bug=dict(file="pi.cpp", mode="runtime", show_fixed_out=True, intro="setprecision(2) without fixed", wrong=EP12_BUG, fix_intro="fixed added before setprecision", fixed=EP12_FIX, expect=[],
   why="Without fixed, setprecision(2) means two digits in total; with fixed it means two digits after the decimal point."),
 pun="\"setprecision without fixed is like a Goa thali with no rice: something important is missing.\"",
 challenge="Print a table with three items, names on the left and prices on the right, every price with two decimals.",
 answer="Use fixed << setprecision(2), then left << setw(10) for names and right << setw(8) for prices.",
 answer_code='''#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    cout << fixed << setprecision(2);
    cout << left << setw(10) << "Tea" << right << setw(8) << 15.0 << endl;
    cout << left << setw(10) << "Bhaji" << right << setw(8) << 40.5 << endl;
    cout << left << setw(10) << "Thali" << right << setw(8) << 180.0 << endl;
    return 0;
}''',
 shorts=[
  dict(id="S1", title="Why format output?", built=[2], hook="Correct numbers can still look messy.", script="Correct numbers can still look messy. Include iomanip and use setw for width, left and right for sides, fixed and setprecision for decimals. A tidy menu board sells more fish.", on="SETW  FIXED  SETPRECISION", caption="Make output tidy.", tags=["cpp", "iomanip", "beginners", "kodingkonkani", "learntocode"]),
  dict(id="S2", title="A price list in code", built=[3], hook="Names left, prices right.", script="Names left, prices right. Left and setw ten for the name. Right and setw eight for the price. Fixed and setprecision two set the decimals once for the whole program.", on="LEFT + SETW(10), RIGHT + SETW(8)", caption="Build a price list.", tags=["cpp", "setw", "coding", "kodingkonkani", "beginners"]),
  dict(id="S3", title="How setw works", built=[4], hook="Setw reserves boxes.", script="Setw reserves boxes. Ten boxes for a name. The word fills four. Left alignment keeps it at the start. Remember, setw affects only the very next item.", on="SETW = RESERVED WIDTH", caption="Width applies to one item.", tags=["cpp", "setw", "programming", "kodingkonkani", "learntocode"]),
  dict(id="S4", title="setprecision needs fixed", built=[7], hook="Two decimals gave me three point one.", script="Two decimals gave me three point one. Set precision two without fixed counts all digits, so pi becomes three point one. Add fixed, and you get three point one four.", on="SETPRECISION(2) -> 3.1", caption="Always pair it with fixed.", tags=["cpp", "bugfix", "setprecision", "kodingkonkani", "coding"]),
  dict(id="S5", title="Pun and challenge", built=[8, 9], hook="A thali with no rice.", script="A thali with no rice. Setprecision without fixed is missing something important. Your challenge: print a three-row price table with two decimals. Full video: EP 12.", on="3-ROW PRICE TABLE", caption="Try the challenge.", tags=["cpp", "codingchallenge", "kodingkonkani", "programmingjokes", "goa"]),
 ])

EPS = [EP5, EP6, EP7, EP8, EP9, EP10, EP11, EP12]

# recap scene (scene 7) per episode
RECAP = {
 5: ("Recap: four ideas on one card", "Recap. One: a variable is a named box in memory. Two: every box has a type. Int for whole numbers, double for decimals, char for one letter, bool for true or false. Three: a bool prints as one or zero. Four: always give a variable a starting value when you make it. Say these four out loud, then change the grade to B and run the program again."),
 6: ("Recap: four rules on one card", "Recap. One: with cin, the arrows point at the variable that receives the value. Two: cin reads one word or number at a time, and stops at any space. Three: getline reads the whole line, spaces included. Four: after cin, use cin ws to skip leftover spaces before getline. Try typing your own name and city into the greeting program, and watch each piece land in its box."),
 7: ("Recap: four ideas on one card", "Recap. One: plus, minus, star, slash and percent do the arithmetic. Two: percent gives the remainder. Three: multiplication and division go before addition and subtraction, and brackets override both. Four: an int divided by an int is an int, so make one side a decimal when you need decimals. Test yourself: what is twenty-three percent five? The answer is three."),
 8: ("Recap: four ideas on one card", "Recap. One: a comparison asks a question and answers true or false. Two: double equals compares, a single equals stores. Three: and needs both sides true, or needs one, and not flips the answer. Four: boolalpha prints true and false as words. Pause the video, and write one condition that is true for seventy-two and false for eighty."),
 9: ("Recap: four ideas on one card", "Recap. One: widening, like int to double, is safe and happens by itself. Two: narrowing, like double to int, loses the decimal part. Three: static cast says you meant it, and truncates instead of rounding. Four: curly braces refuse any narrowing they can see. If you remember one thing, remember this: cast first, then divide."),
 10: ("Recap: four ideas on one card", "Recap. One: auto lets the compiler pick the type from the value. Two: const locks a value after it is set, and the compiler blocks any change. Three: constexpr names a value known before the program runs. Four: use const by default, and remove it only when a value truly must change. Try adding the word const to a variable of your own, then try to change it."),
 11: ("Recap: four ideas on one card", "Recap. One: a string is a row of characters, and you need the string header. Two: plus joins strings, and at least one side must be a real string. Three: dot length counts every character, including spaces. Four: indexes start at zero, so the last letter is at length minus one. Say them out loud, and you can handle any beginner text task."),
 12: ("Recap: four ideas on one card", "Recap. One: include iomanip to format output. Two: setw reserves a width, and works only on the very next item. Three: left and right choose the side the text sticks to. Four: fixed with setprecision gives an exact number of decimals. Without fixed, setprecision counts all digits. Print a price list of your own, and make the columns line up."),
}
for _e in EPS:
    on, narr = RECAP[_e["ep"]]
    _e["scenes"].insert(6, dict(tpl=CS, name="Recap", on=on, anim="Four recap lines tick in one by one with a pop; Xecxec nods after each tick", narr=narr, min=30))
    for _s in _e["shorts"]:
        _s["built"] = [b + 1 if b >= 7 else b for b in _s["built"]]
    _e["yt"]["chapters"] = {(k + 1 if k >= 7 else k): v for k, v in _e["yt"]["chapters"].items()}
    _e["yt"]["chapters"][7] = "Recap"


for _e in EPS:
    _mapped = set()
    for _f in _e["files"]:
        _mapped |= {int(x) for x in re.findall(r"\d+", _f.get("scene", ""))}
    for _i, _s in enumerate(_e["scenes"], 1):
        if _s["tpl"] == CE and _i not in _mapped:
            print("cpp m1 patch", _e["ep"], _i, _s["name"])
            _s["tpl"] = CS
