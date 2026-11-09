"""Module 3 — Functions (EP 21-30)."""
from lib import callstack, flow, mem, table

MODULE = {"id": 3, "name": "Functions", "range": "21–30", "colours": "Mint + Dark blue", "bg": "mint"}
NEXT_AFTER = ("Next: EP 31 · Arrays", "We end module three here. Next time: arrays, a row of boxes in memory.")
EPISODES = []

EPISODES.append(dict(
    n=21, title="Functions", spoken="functions", yt="C++ Functions: Write Code Once, Use It Many Times",
    thumb="FUNCTIONS", vis="a small machine with a call button",
    goals=["write a function", "call a function many times", "declare a function before main"],
    tags=["c++ functions", "void function", "function call", "function declaration"],
    analogy="a tea stall menu: one recipe, many cups",
    c_pts=["A function is a named block of code", "You call it by its name", "It runs, then control returns"],
    hook="Write the code once. Use it a hundred times.",
    intro="Today we stop repeating ourselves. A function is a named block of code that you can call whenever you want.",
    concept="A function is a named block of code. You write it once, and you call it by name as often as you like. When the function ends, the program returns to the line after the call.\n"
            "A function that gives nothing back has the type void. Think of a tea stall. There is one recipe, and it makes many cups.",
    A=dict(file="greet.cpp", label="Your first function", on="a void function prints a greeting",
           src='''
#include <iostream>
using namespace std;

void greet() {
    cout << "Namaskar from a function!" << endl;
}

int main() {
    greet();
    greet();
    return 0;
}
''',
           narr="[HL 4] The word void means this function gives nothing back. Greet is the name. The empty brackets mean it takes nothing in. "
                "[HL 5] The body prints a line. [HL 9] In main, we call greet by its name. The program jumps to the function. [HL 10] We call it a second time. "
                "The line prints twice, and we wrote it once."),
    ill=dict(label="The call and the return", on="a flow: main calls greet, greet runs, control returns",
             data=flow([("main", "Reaches greet()"), ("Jump", "Control goes to greet"), ("greet", "Prints the line"), ("Return", "Back to the next line in main")]),
             narr="Follow the path. Main reaches the call. The program jumps into greet. Greet prints its line. Then control returns to main, to the line after the call."),
    B=dict(file="order.cpp", label="Declare first", on="a declaration lets main come first",
           src='''
#include <iostream>
using namespace std;

void tea();

int main() {
    tea();
    return 0;
}

void tea() {
    cout << "One cup of tea" << endl;
}
''',
           narr="[HL 4] This line is a declaration. It tells the compiler that tea exists, and it ends with a semicolon. "
                "[HL 7] Now main can call tea, even though the body comes later. [HL 11] The full definition sits below main. "
                "Without the declaration, the compiler would not know the name tea at line seven."),
    term="The program prints One cup of tea.",
    recap=["A function is a named block of code.", "You call it by writing its name and brackets.",
           "Void means the function gives nothing back.", "Declare a function before you call it."],
    bug=dict(title="Calling a function before it exists", file="order.cpp", kind="compile", wrong_note="tea is called before the compiler knows it",
             wrong='''
#include <iostream>
using namespace std;

int main() {
    tea();
    return 0;
}

void tea() {
    cout << "One cup of tea" << endl;
}
''', fixed_note="a declaration comes first",
             fixed='''
#include <iostream>
using namespace std;

void tea();

int main() {
    tea();
    return 0;
}

void tea() {
    cout << "One cup of tea" << endl;
}
''',
             why="The compiler reads the file from top to bottom. It must see a function name before the line that uses it.",
             narr="Bug of the Day. Main calls tea, but the function is written below main. The compiler says tea was not declared in this scope. "
                  "It reads from top to bottom. Add a declaration above main, or move the whole function above main."),
    pun="I wrote a function to make tea. It returns void, and my cup is empty.",
    task="write a function that prints a banner", challenge="Write a function called banner. It prints a line of stars. Call it before and after a message.",
    answer="Write void banner with one cout of a line of stars. In main, call banner, print the message, and call banner again.",
))

EPISODES.append(dict(
    n=22, title="Parameters and return values", spoken="parameters and return values", yt="C++ Function Parameters and Return Values",
    thumb="IN AND OUT", vis="a machine with an input slot and an output tray",
    goals=["pass values into a function", "return a value from a function", "use the returned value"],
    tags=["function parameters", "return value", "c++ return", "function arguments"],
    analogy="a juice machine: you put in fruit and you get juice out",
    c_pts=["Parameters are inputs", "Return sends one value back", "The caller can store the result"],
    hook="Functions can take values in and give a value back.",
    intro="Today our functions take values in and send a value back. Now they can do real work.",
    concept="Parameters are the inputs of a function. They sit inside the brackets, each with a type and a name. The return statement sends one value back to the caller.\n"
            "The type before the function name says what kind of value comes back. Think of a juice machine. You put in fruit, and you get juice out.",
    A=dict(file="add.cpp", label="An add function", on="add takes two ints and returns their sum",
           src='''
#include <iostream>
using namespace std;

int add(int a, int b) {
    return a + b;
}

int main() {
    int total = add(4, 9);
    cout << "Total: " << total << endl;
    return 0;
}
''',
           narr="[HL 4] The type int before the name means the function returns an int. A and b are the parameters. Each has its own type. "
                "[HL 5] Return sends the sum back to the caller. [HL 9] The call passes four and nine. Those values are called arguments. "
                "[TRACK total=13] The returned thirteen goes into total. [HL 10] Then we print it."),
    ill=dict(label="Values in, value out", on="a flow: arguments go in, the result comes out",
             data=flow([("Call", "add(4, 9)"), ("Copy", "a = 4 and b = 9"), ("Compute", "a + b"), ("Return", "13 goes to total")]),
             narr="The call passes four and nine. The function gets them as a and b. It adds them. Then return sends thirteen back, and total stores it."),
    B=dict(file="bigger.cpp", label="Return a decision", on="a function returns the bigger of two numbers",
           src='''
#include <iostream>
using namespace std;

int bigger(int a, int b) {
    if (a > b) {
        return a;
    }
    return b;
}

int main() {
    cout << bigger(7, 12) << endl;
    cout << bigger(30, 5) << endl;
    return 0;
}
''',
           narr="[HL 5] If a is bigger, the function returns a and ends at once. [HL 8] Otherwise it returns b. [HL 12] The first call gives twelve. "
                "[HL 13] The second call gives thirty. A function can use the same code for any two numbers."),
    term="The program prints twelve and thirty on two lines.",
    recap=["Parameters are the inputs of a function.", "Return sends one value back.",
           "The type before the name is the return type.", "A return statement ends the function at once."],
    bug=dict(title="No return in a function", file="add.cpp", kind="warn", wrong_note="the function never returns a value",
             wrong='''
#include <iostream>
using namespace std;

int add(int a, int b) {
    int sum = a + b;
}

int main() {
    cout << add(4, 9) << endl;
    return 0;
}
''', fixed_note="return sends the sum back",
             fixed='''
#include <iostream>
using namespace std;

int add(int a, int b) {
    int sum = a + b;
    return sum;
}

int main() {
    cout << add(4, 9) << endl;
    return 0;
}
''',
             why="A function with a return type must return a value on every path. Without a return, the result is undefined.",
             narr="Bug of the Day. The function makes a sum, but it never returns it. The compiler warns that there is no return statement in a function returning non-void. "
                  "The caller gets garbage. Add return sum at the end."),
    pun="My function took two numbers and gave me back a headache.",
    task="write a function that finds the smaller number", challenge="Write a function called smaller. It takes two ints and returns the smaller one.",
    answer="Use an if. If a is less than b, return a. Otherwise return b. Call smaller from main and print the result.",
))

EPISODES.append(dict(
    n=23, title="Pass by value", spoken="pass by value", yt="C++ Pass by Value: Why Your Change Disappears",
    thumb="A COPY!", vis="a photocopier making a copy of a box",
    goals=["explain that arguments are copied", "show that the original does not change", "return a result instead"],
    tags=["pass by value", "function copy", "c++ parameters", "swap function"],
    analogy="a photocopy: you scribble on the copy, and the original stays clean",
    c_pts=["The function gets a copy of the argument", "Changes to the copy stay inside", "Return the result to send it out"],
    hook="A function changes a copy, not your variable.",
    intro="Today we meet a surprise. A function can change its input, and your variable still stays the same.",
    concept="When you pass a value to a function, C plus plus makes a copy. The function works on the copy. The original variable never changes.\n"
            "This is called pass by value. To send a result out, use return. Think of a photocopy. You can scribble on the copy, and the original stays clean.",
    A=dict(file="copy.cpp", label="A copy is changed", on="double_it changes its own copy",
           src='''
#include <iostream>
using namespace std;

void double_it(int n) {
    n = n * 2;
    cout << "Inside: " << n << endl;
}

int main() {
    int number = 10;
    double_it(number);
    cout << "Outside: " << number << endl;
    return 0;
}
''',
           narr="[HL 10] Number is ten. [HL 11] We call double it with number. C plus plus copies ten into the parameter n. "
                "[HL 5] The function doubles its copy. [HL 6] Inside the function, n is twenty. [HL 12] Back in main, number is still ten. The copy was changed, not the original."),
    ill=dict(label="Two separate boxes", on="memory boxes: number in main and n in double_it have different addresses",
             data=mem([("number", "int", "10"), ("n", "int", "20")], caption="n is a copy. It lives in its own box with its own address"),
             narr="Look at the two boxes. Number lives in main. N lives in the function. They have different addresses. "
                  "The function doubled n to twenty. The box named number still holds ten."),
    B=dict(file="noswap.cpp", label="A swap that fails", on="swap_values swaps copies, not the originals",
           src='''
#include <iostream>
using namespace std;

void swap_values(int a, int b) {
    int t = a;
    a = b;
    b = t;
}

int main() {
    int x = 1, y = 2;
    swap_values(x, y);
    cout << x << " " << y << endl;
    return 0;
}
''',
           narr="[HL 4] The function swaps a and b. [HL 5] It uses a helper box t. [HL 12] Main calls it with x and y. The function swaps only its copies. "
                "[HL 13] So x is still one, and y is still two. We need another way to change the originals. That is the next episode."),
    term="The program prints one and two. Nothing was swapped.",
    recap=["Arguments are copied into the parameters.", "A change to the copy does not reach the original.",
           "Use return to send a result out.", "Next episode: references change the original."],
    bug=dict(title="Expecting the original to change", file="tax.cpp", kind="output", wrong_note="add_tax changes only its copy",
             wrong='''
#include <iostream>
using namespace std;

void add_tax(double price) {
    price = price * 1.05;
}

int main() {
    double price = 100.0;
    add_tax(price);
    cout << "Price: " << price << endl;
    return 0;
}
''', fixed_note="the function returns the new price",
             fixed='''
#include <iostream>
using namespace std;

double add_tax(double price) {
    return price * 1.05;
}

int main() {
    double price = 100.0;
    price = add_tax(price);
    cout << "Price: " << price << endl;
    return 0;
}
''',
             why="The function changes its own copy of price, and then the copy disappears. Return the new value and store it in the variable.",
             narr="Bug of the Day. Add tax should raise the price to one hundred and five. But the program prints one hundred. "
                  "The function changed only a copy. Return the new price, and store it in the variable. Now the answer is right."),
    pun="I gave my function a copy of my homework. It said, nice try, I will only change the copy.",
    task="predict the output before you run", challenge="Write a function that adds one to its int parameter. Call it from main. Print the variable before and after.",
    answer="The variable does not change, because the function adds one to a copy. To change it, return the new value and store it.",
))

EPISODES.append(dict(
    n=24, title="Pass by reference", spoken="pass by reference", yt="C++ References: Pass by Reference and swap",
    thumb="PASS BY &", vis="two name tags tied to the same box",
    goals=["write a reference parameter", "change the original variable", "write a working swap function"],
    tags=["pass by reference", "c++ reference", "swap function c++", "ampersand"],
    analogy="a nickname: two names for the same person",
    c_pts=["An ampersand makes a reference", "A reference is another name for the same box", "Changes reach the original"],
    hook="One ampersand turns a copy into the real thing.",
    intro="Today we fix the broken swap. One small symbol, the ampersand, lets a function change the original.",
    concept="A reference is another name for an existing variable. You write an ampersand after the type. No copy is made.\n"
            "When a function takes a reference, it works on the original variable. Think of a nickname. Two names point to the same person.",
    A=dict(file="byref.cpp", label="A reference parameter", on="double_it changes the original with a reference",
           src='''
#include <iostream>
using namespace std;

void double_it(int& n) {
    n = n * 2;
}

int main() {
    int number = 10;
    double_it(number);
    cout << "Number: " << number << endl;
    return 0;
}
''',
           narr="[HL 4] The ampersand after int makes n a reference. N is another name for the caller variable. [HL 5] The function doubles n. "
                "[HL 10] Main passes number. No copy is made. [HL 11] Number is now twenty. The original changed."),
    ill=dict(label="One box, two names", on="memory boxes: n is a reference to number",
             data=mem([("number", "int", "20"), ("n", "int&", None)], arrows=[("n", "number", "alias of")],
                      caption="The reference n points at the same box as number"),
             narr="Look at the picture. There is one box that holds the value. Number is its name in main. N is its second name in the function. "
                  "A change through n changes the same box."),
    B=dict(file="swapref.cpp", label="A swap that works", on="swap_values with references swaps the originals",
           src='''
#include <iostream>
using namespace std;

void swap_values(int& a, int& b) {
    int t = a;
    a = b;
    b = t;
}

int main() {
    int x = 1, y = 2;
    swap_values(x, y);
    cout << x << " " << y << endl;
    return 0;
}
''',
           narr="[HL 4] Both parameters are references. [HL 5] The helper box t keeps the old value of a. [HL 6] A takes the value of b. [HL 7] B takes the old value from t. "
                "[HL 13] Now main prints two and one. The swap worked. The C plus plus library also has a function called swap."),
    term="The program prints two and one.",
    recap=["An ampersand after the type makes a reference.", "A reference is another name for the same variable.",
           "A reference parameter changes the original.", "Use it for swap and for functions that change their input."],
    bug=dict(title="A number cannot be a reference", file="inc.cpp", kind="compile", wrong_note="the call passes the plain number five",
             wrong='''
#include <iostream>
using namespace std;

void inc(int& n) {
    n++;
}

int main() {
    inc(5);
    return 0;
}
''', fixed_note="the call passes a variable",
             fixed='''
#include <iostream>
using namespace std;

void inc(int& n) {
    n++;
}

int main() {
    int count = 5;
    inc(count);
    cout << count << endl;
    return 0;
}
''',
             why="A reference must refer to a real variable. The plain number five has no box that the function could change.",
             narr="Bug of the Day. We call inc with the plain number five. The compiler says it cannot bind a non-const lvalue reference to an rvalue. "
                  "In simple words, five has no box to change. Pass a variable instead."),
    pun="A reference told a variable, I will always have your back. The variable said, I know, you are my alias.",
    task="write a function that doubles two numbers", challenge="Write a function that takes two int references and doubles both. Test it in main.",
    answer="Write a void function called double both with two int ampersand parameters. Inside, multiply each by two. Print both variables in main.",
))

EPISODES.append(dict(
    n=25, title="const references", spoken="const references", yt="C++ const References: Fast and Safe Parameters",
    thumb="CONST &", vis="a glass case around a big box",
    goals=["pass big values without copying", "protect a parameter with const", "know when to use const and ampersand"],
    tags=["const reference", "const &", "pass big objects", "c++ best practice"],
    analogy="a museum: you may look at the painting, but you may not touch it",
    c_pts=["A copy of a big value is slow", "A reference avoids the copy", "Const stops the function from changing it"],
    hook="Look, but do not touch. That is a const reference.",
    intro="Today we learn the most common parameter style in modern C plus plus. It is fast, and it is safe.",
    concept="Copying a big string for every call is slow. A reference avoids the copy. But a reference lets the function change the original. Add const, and the function may only read it.\n"
            "So a const reference is fast and safe. Think of a museum. You may look at the painting, but you may not touch it.",
    A=dict(file="show.cpp", label="A const reference", on="show reads a string without copying it",
           src='''
#include <iostream>
#include <string>
using namespace std;

void show(const string& text) {
    cout << "Text: " << text << endl;
}

int main() {
    string line = "Goa has many beaches";
    show(line);
    return 0;
}
''',
           narr="[HL 5] The parameter is a const reference to a string. No copy is made. [HL 6] The function may read text, but it may not change it. "
                "[HL 11] Main passes the string. [HL 6] The function prints it. Use this style for strings and other big values."),
    ill=dict(label="Which parameter style?", on="a table of three parameter styles",
             data=table(["Style", "Copy made?", "Can change the original?"], [["int n", "yes", "no"], ["int& n", "no", "yes"], ["const int& n", "no", "no"]]),
             narr="Here are three styles. A plain parameter makes a copy and cannot change the original. A reference makes no copy and can change the original. "
                  "A const reference makes no copy and cannot change the original. For big values that you only read, choose the last style."),
    B=dict(file="longer.cpp", label="Compare two strings", on="longer takes two const references",
           src='''
#include <iostream>
#include <string>
using namespace std;

bool longer(const string& a, const string& b) {
    return a.size() > b.size();
}

int main() {
    string x = "Panjim";
    string y = "Mapusa";
    cout << boolalpha << longer(x, y) << endl;
    cout << longer("Margao", "Goa") << endl;
    return 0;
}
''',
           narr="[HL 5] Both parameters are const references. Both strings are only read. [HL 6] The function compares the sizes. "
                "[HL 12] Panjim and Mapusa both have six letters, so the answer is false. [HL 13] A const reference can also take a plain quoted text. Margao is longer than Goa, so the answer is true."),
    term="The program prints false and then true.",
    recap=["A copy of a big value is slow.", "A const reference makes no copy.",
           "The function may read the value but not change it.", "A const reference can take a temporary value."],
    bug=dict(title="Changing a const reference", file="bump.cpp", kind="compile", wrong_note="the function changes a const reference",
             wrong='''
#include <iostream>
using namespace std;

void bump(const int& n) {
    n++;
}

int main() {
    int count = 1;
    bump(count);
    cout << count << endl;
    return 0;
}
''', fixed_note="the function uses a plain reference",
             fixed='''
#include <iostream>
using namespace std;

void bump(int& n) {
    n++;
}

int main() {
    int count = 1;
    bump(count);
    cout << count << endl;
    return 0;
}
''',
             why="A const reference is read-only. If the function must change the value, use a plain reference. If it must not, remove the change.",
             narr="Bug of the Day. The function takes a const reference, and then tries to add one. The compiler says increment of read-only reference. "
                  "Const means look, but do not touch. If the function must change the value, remove const."),
    pun="The museum guard loves const references. He says, look all you want, but do not touch the exhibit.",
    task="choose the right parameter style", challenge="Write a function that prints the size of a string. Choose the best parameter style, and explain your choice in a comment.",
    answer="Use const string ampersand. The function only reads the string, and a reference avoids a slow copy.",
))

EPISODES.append(dict(
    n=26, title="Default arguments and overloading", spoken="default arguments and overloading", yt="C++ Default Arguments and Function Overloading",
    thumb="SAME NAME", vis="three machines with the same name tag",
    goals=["give a parameter a default value", "write overloaded functions", "read an ambiguous call error"],
    tags=["default arguments", "function overloading", "c++ overload", "ambiguous call"],
    analogy="a tea stall: the usual order is chai, but you can ask for coffee",
    c_pts=["A default value fills a missing argument", "Overloads share a name but differ in parameters", "The compiler picks the best match"],
    hook="Many functions can share one name.",
    intro="Today we give functions more flexibility. They get default values, and they can share a name.",
    concept="A default argument is a value that the compiler uses when the caller leaves it out. Overloading means several functions share one name, but have different parameters.\n"
            "The compiler picks the one that matches the call best. Think of a tea stall. The usual order is chai, but you may ask for coffee.",
    A=dict(file="power.cpp", label="A default value", on="power has a default exponent of two",
           src='''
#include <iostream>
using namespace std;

int power(int base, int exp = 2) {
    int result = 1;
    for (int i = 0; i < exp; i++) {
        result *= base;
    }
    return result;
}

int main() {
    cout << power(5) << endl;
    cout << power(2, 10) << endl;
    return 0;
}
''',
           narr="[HL 4] The parameter exp has a default of two. [HL 6] The loop multiplies the base, exp times. [HL 13] The call power of five leaves out exp. The default of two is used. "
                "The answer is twenty-five. [HL 14] The call power of two and ten gives one thousand and twenty-four."),
    ill=dict(label="Which call matches?", on="a table of calls and the functions that the compiler picks",
             data=table(["Call", "Picks", "Why"], [["area(5)", "area(int)", "One int argument"], ["area(4, 6)", "area(int, int)", "Two int arguments"], ["area(2.5)", "area(double)", "One double argument"]]),
             narr="Look at the three calls. The compiler checks the number of arguments, and their types. One int picks the first function. "
                  "Two ints pick the second. One double picks the third."),
    B=dict(file="overload.cpp", label="Overloaded functions", on="three functions called area",
           src='''
#include <iostream>
using namespace std;

int area(int side) { return side * side; }
int area(int w, int h) { return w * h; }
double area(double radius) { return 3.14 * radius * radius; }

int main() {
    cout << area(5) << endl;
    cout << area(4, 6) << endl;
    cout << area(2.0) << endl;
    return 0;
}
''',
           narr="[HL 4] Area of one int is a square. [HL 5] Area of two ints is a rectangle. [HL 6] Area of a double is a circle. "
                "[HL 9] Five is an int, so we get twenty-five. [HL 10] Four and six give twenty-four. [HL 11] Two point zero is a double, so we get twelve point five six."),
    term="The program prints twenty-five, twenty-four and twelve point five six.",
    recap=["A default argument fills in a missing value.", "Defaults go at the end of the parameter list.",
           "Overloads share a name but have different parameters.", "The compiler picks the best match."],
    bug=dict(title="An ambiguous call", file="show.cpp", kind="compile", wrong_note="the call matches two functions equally well",
             wrong='''
#include <iostream>
using namespace std;

void show(long n) { cout << "long " << n << endl; }
void show(double n) { cout << "double " << n << endl; }

int main() {
    show(5);
    return 0;
}
''', fixed_note="the call names the exact type",
             fixed='''
#include <iostream>
using namespace std;

void show(long n) { cout << "long " << n << endl; }
void show(double n) { cout << "double " << n << endl; }

int main() {
    show(5L);
    return 0;
}
''',
             why="An int converts to long and to double with the same cost, so the compiler cannot choose. Make the type exact, or add an int overload.",
             narr="Bug of the Day. We call show with the plain number five. There is a long version and a double version. "
                  "The compiler says the call is ambiguous. An int fits both equally well. Write five with the letter L, or add an int version."),
    pun="I overloaded my function. Now it has a lot on its plate, but it keeps its name.",
    task="overload a print function", challenge="Write two functions called describe. One takes an int and one takes a string. Call both.",
    answer="Write void describe with an int parameter and void describe with a string parameter. Call describe with seven and with a quoted word.",
))

EPISODES.append(dict(
    n=27, title="Scope and lifetime", spoken="scope and lifetime", yt="C++ Scope: Local, Global and Block Variables",
    thumb="WHERE LIVES X?", vis="rooms in a house, each with its own box",
    goals=["tell local from global variables", "know that a block has its own scope", "use a static local variable"],
    tags=["c++ scope", "local variable", "global variable", "static local"],
    analogy="rooms in a house: a box in the kitchen is not visible in the bedroom",
    c_pts=["A variable lives inside its braces", "A global variable lives for the whole program", "A static local keeps its value between calls"],
    hook="A variable only lives inside its own braces.",
    intro="Today we ask where a variable lives. Scope decides where you can use a name, and for how long it exists.",
    concept="Scope is the part of the program where a name is visible. A variable made inside braces dies at the closing brace. A global variable lives for the whole program.\n"
            "A static local variable stays alive between calls. Think of rooms in a house. A box in the kitchen is not visible from the bedroom.",
    A=dict(file="scope.cpp", label="Local and global", on="a global counter and a local variable",
           src='''
#include <iostream>
using namespace std;

int visits = 0;

void enter() {
    int local = 10;
    visits++;
    cout << "visits=" << visits << " local=" << local << endl;
}

int main() {
    enter();
    enter();
    return 0;
}
''',
           narr="[HL 4] Visits lives outside every function, so it is global. It lives for the whole program. [HL 7] Local lives inside enter. It is created at each call. "
                "[HL 8] Each call adds one to visits. [HL 13] The first call prints visits one. [HL 14] The second call prints visits two. Local is ten each time, because it is made fresh."),
    ill=dict(label="Where each variable lives", on="memory boxes: a global in the static region and a local on the stack",
             data=mem([("visits", "int", "2", "static"), ("local", "int", "10", "stack")], caption="visits lives for the whole program. local lives only while enter runs"),
             narr="Look at the two regions. Visits lives in the static region. It stays until the program ends. Local lives on the stack. "
                  "It is made when enter starts, and it is destroyed when enter ends."),
    B=dict(file="counter.cpp", label="A static local", on="a static local keeps its value between calls",
           src='''
#include <iostream>
using namespace std;

int next_ticket() {
    static int ticket = 100;
    ticket++;
    return ticket;
}

int main() {
    cout << next_ticket() << endl;
    cout << next_ticket() << endl;
    cout << next_ticket() << endl;
    return 0;
}
''',
           narr="[HL 5] The word static makes ticket live for the whole program. The start value is set only once. [HL 6] Each call adds one. "
                "[HL 7] It returns the new ticket. [HL 11] The first call prints one hundred and one. [HL 12] The second prints one hundred and two, and so on."),
    term="The program prints one hundred and one, one hundred and two, and one hundred and three.",
    recap=["A local variable lives inside its braces.", "A global variable lives for the whole program.",
           "A block has its own scope.", "A static local keeps its value between calls."],
    bug=dict(title="Using a variable outside its block", file="block.cpp", kind="compile", wrong_note="total is used after its block ends",
             wrong='''
#include <iostream>
using namespace std;

int main() {
    for (int i = 1; i <= 3; i++) {
        int total = i * 10;
    }
    cout << total << endl;
    return 0;
}
''', fixed_note="total is made before the loop",
             fixed='''
#include <iostream>
using namespace std;

int main() {
    int total = 0;
    for (int i = 1; i <= 3; i++) {
        total = i * 10;
    }
    cout << total << endl;
    return 0;
}
''',
             why="Total dies at the closing brace of the loop. Make it before the loop, so it lives until the end of main.",
             narr="Bug of the Day. Total is made inside the loop, but we print it after the loop. The compiler says total was not declared in this scope. "
                  "The variable died at the closing brace. Make it before the loop."),
    pun="Why was the local variable sad? It knew that it would be gone at the closing brace.",
    task="count function calls", challenge="Write a function that counts how many times it was called. Use a static local variable. Call it four times.",
    answer="Write static int calls equals zero inside the function. Add one on each call, and print it. After four calls it shows four.",
))

EPISODES.append(dict(
    n=28, title="Recursion", spoken="recursion", yt="C++ Recursion: A Function That Calls Itself",
    thumb="RECURSION", vis="a stack of nested boxes, each smaller than the last",
    goals=["explain base case and recursive case", "trace a recursive call on the stack", "fix a wrong base case"],
    tags=["c++ recursion", "factorial", "base case", "call stack"],
    analogy="Russian dolls: open one, and a smaller one sits inside",
    c_pts=["A recursive function calls itself", "The base case stops the calls", "Each call has its own variables"],
    hook="A function that calls itself needs a way to stop.",
    intro="Today a function calls itself. It sounds strange, but it solves many problems with little code.",
    concept="A recursive function calls itself on a smaller problem. It needs a base case. The base case is the simplest problem, and it stops the calls.\n"
            "Each call has its own variables on the stack. When the base case returns, the calls finish one by one. Think of Russian dolls. You open one, and a smaller one sits inside.",
    A=dict(file="factorial.cpp", label="Factorial", on="factorial of five with recursion",
           src='''
#include <iostream>
using namespace std;

int factorial(int n) {
    if (n <= 1) {
        return 1;
    }
    return n * factorial(n - 1);
}

int main() {
    cout << factorial(5) << endl;
    return 0;
}
''',
           narr="[HL 5] This is the base case. When n is one or less, the answer is one. [HL 8] This is the recursive case. "
                "The answer is n times the factorial of n minus one. [HL 12] Main asks for factorial of five. "
                "Five times factorial of four. Four times factorial of three. This goes down to one. Then the answers multiply back up to one hundred and twenty."),
    ill=dict(label="The call stack", on="the stack grows to three calls, then unwinds",
             data=callstack([(["main()", "factorial(n=3)"], "main calls factorial with three"), (["main()", "factorial(n=3)", "factorial(n=2)"], "factorial three calls factorial two"),
                             (["main()", "factorial(n=3)", "factorial(n=2)", "factorial(n=1)"], "the base case: factorial one returns one"),
                             (["main()", "factorial(n=3)", "factorial(n=2)"], "factorial two returns two times one, which is two"),
                             (["main()", "factorial(n=3)"], "factorial three returns three times two, which is six"), (["main()"], "main receives six")]),
             narr="Watch the stack. Each call adds a frame. Factorial of three calls two. Two calls one. Now the base case returns one. "
                  "The frames leave one by one. Two returns two. Three returns six. Main receives the answer."),
    B=dict(file="sumto.cpp", label="Sum to n", on="a recursive sum from one to n",
           src='''
#include <iostream>
using namespace std;

int sum_to(int n) {
    if (n == 0) {
        return 0;
    }
    return n + sum_to(n - 1);
}

int main() {
    cout << sum_to(4) << endl;
    return 0;
}
''',
           narr="[HL 5] The base case is zero. The sum of nothing is zero. [HL 8] Otherwise, the sum to n is n plus the sum to n minus one. "
                "[TRACK n=4] Sum to four is four plus sum to three. That goes on down to zero. [HL 12] The answer is ten."),
    term="The program prints ten.",
    recap=["A recursive function calls itself.", "The base case stops the calls.",
           "Each call has its own variables.", "Every recursive call must move toward the base case."],
    bug=dict(title="A wrong base case", file="factorial.cpp", kind="output", wrong_note="the base case returns zero",
             wrong='''
#include <iostream>
using namespace std;

int factorial(int n) {
    if (n <= 1) {
        return 0;
    }
    return n * factorial(n - 1);
}

int main() {
    cout << factorial(5) << endl;
    return 0;
}
''', fixed_note="the base case returns one",
             fixed='''
#include <iostream>
using namespace std;

int factorial(int n) {
    if (n <= 1) {
        return 1;
    }
    return n * factorial(n - 1);
}

int main() {
    cout << factorial(5) << endl;
    return 0;
}
''',
             why="The base case value goes into every multiplication. With zero, every product becomes zero. For factorial the base value must be one.",
             narr="Bug of the Day. The program prints zero for factorial of five. The base case returns zero, and zero goes into every multiplication. "
                  "The whole answer becomes zero. For a product, the base case must return one."),
    pun="To understand recursion, you must first understand recursion.",
    task="trace a recursive call by hand", challenge="Write a recursive function that prints the numbers from n down to one. Call it with four.",
    answer="If n is zero, return. Otherwise print n, and call the function with n minus one.",
))

EPISODES.append(dict(
    n=29, title="Lambda functions", spoken="lambda functions", yt="C++ Lambdas: Small Functions Without a Name",
    thumb="LAMBDAS", vis="a tiny function wearing a lambda symbol",
    goals=["write a lambda", "capture a variable", "store a lambda with auto"],
    tags=["c++ lambda", "lambda capture", "anonymous function", "auto lambda"],
    analogy="a sticky note with an instruction: short, local, and thrown away after use",
    c_pts=["A lambda is a small unnamed function", "Square brackets capture outside variables", "Store it in an auto variable"],
    hook="A function that fits on one line.",
    intro="Today we write functions without names. Lambdas are small, quick and common in modern C plus plus.",
    concept="A lambda is a small function without a name. It has square brackets, then parameters, then a body. The square brackets say which outside variables the lambda may use.\n"
            "You can store a lambda in an auto variable and call it like a function. Think of a sticky note with one short instruction. You use it on the spot.",
    A=dict(file="lambda.cpp", label="A first lambda", on="a lambda that squares a number",
           src='''
#include <iostream>
using namespace std;

int main() {
    auto square = [](int x) {
        return x * x;
    };
    cout << square(6) << endl;
    cout << square(9) << endl;
    return 0;
}
''',
           narr="[HL 5] The square brackets start the lambda. Inside them nothing is captured. [HL 5] The parameter is x. [HL 6] The body returns x times x. "
                "[HL 5] We store the lambda in the auto variable square. [HL 8] We call it like a function. Six squared is thirty-six. [HL 9] Nine squared is eighty-one."),
    ill=dict(label="Parts of a lambda", on="a flow of the four parts of a lambda",
             data=flow([("[ ]", "Capture list"), ("( )", "Parameters"), ("{ }", "Body"), ("auto", "Variable that holds it")]),
             narr="Here are the four parts. The square brackets are the capture list. The round brackets hold the parameters. The curly braces hold the body. "
                  "The auto variable holds the whole lambda."),
    B=dict(file="capture.cpp", label="Capture a variable", on="a lambda captures offset by value",
           src='''
#include <iostream>
using namespace std;

int main() {
    int offset = 100;
    auto shift = [offset](int x) {
        return x + offset;
    };
    cout << shift(5) << endl;
    return 0;
}
''',
           narr="[HL 5] Offset is one hundred. [HL 6] The capture list names offset. The lambda keeps a copy of it. "
                "[HL 7] The body adds the offset to x. [HL 9] Shift of five gives one hundred and five."),
    term="The program prints one hundred and five.",
    recap=["A lambda is a small function without a name.", "Square brackets capture outside variables.",
           "Store a lambda in an auto variable.", "Call it with round brackets."],
    bug=dict(title="A variable that is not captured", file="capture.cpp", kind="compile", wrong_note="the capture list is empty",
             wrong='''
#include <iostream>
using namespace std;

int main() {
    int offset = 100;
    auto shift = [](int x) {
        return x + offset;
    };
    cout << shift(5) << endl;
    return 0;
}
''', fixed_note="offset is in the capture list",
             fixed='''
#include <iostream>
using namespace std;

int main() {
    int offset = 100;
    auto shift = [offset](int x) {
        return x + offset;
    };
    cout << shift(5) << endl;
    return 0;
}
''',
             why="A lambda can only use outside variables that you list in its square brackets. Add offset to the capture list.",
             narr="Bug of the Day. The lambda uses offset, but the capture list is empty. The compiler says offset is not captured. "
                  "A lambda cannot see outside variables unless you list them. Write offset between the square brackets."),
    pun="My lambda did not want to share. It said, I will only capture what I need.",
    task="write a lambda that doubles a number", challenge="Write a lambda that takes an int and returns double that number. Store it in auto and call it with eight.",
    answer="Write auto twice equals square brackets, round brackets with int x, and a body that returns x times two. Then print twice of eight, which is sixteen.",
))

EPISODES.append(dict(
    n=30, title="Mini project: calculator", spoken="a mini project, a calculator", yt="C++ Mini Project: Build a Calculator",
    thumb="BUILD A CALC", vis="a calculator made from code blocks",
    goals=["split a program into functions", "read an expression with cin", "choose an operation with switch"],
    tags=["c++ calculator", "c++ mini project", "functions project", "switch calculator"],
    analogy="a kitchen with stations: each cook does one job",
    c_pts=["Plan the functions first", "One function does one job", "main only joins the pieces"],
    hook="Build a real calculator from small functions.",
    intro="Today we build a mini project. You will join functions, input and switch into a working calculator.",
    concept="Good programs are made of small functions. Each function does one job. Main only joins them together.\n"
            "Our calculator has three jobs. First, read the numbers and the sign. Second, calculate. Third, print the answer. Think of a kitchen with stations. Each cook does one job.",
    A=dict(file="calc.cpp", label="The calculator", on="calc takes two numbers and a sign",
           src='''
#include <iostream>
using namespace std;

double calc(double a, char op, double b) {
    switch (op) {
        case '+': return a + b;
        case '-': return a - b;
        case '*': return a * b;
        case '/': return b != 0 ? a / b : 0;
        default: return 0;
    }
}

int main() {
    double a, b;
    char op;
    cin >> a >> op >> b;
    cout << a << " " << op << " " << b << " = " << calc(a, op, b) << endl;
    return 0;
}
''', stdin="12 * 3",
           narr="[HL 4] Calc takes two numbers and a sign. [HL 5] A switch picks the operation. [HL 6] Plus adds. [HL 8] Times multiplies. "
                "[HL 9] For divide, we first check that b is not zero. [HL 17] Main reads three values with one cin line. [HL 18] It prints the whole sum, and the answer. Twelve times three is thirty-six."),
    ill=dict(label="The plan", on="a flow: read, choose, calculate, print",
             data=flow([("Read", "cin reads a, op and b"), ("Choose", "switch picks the sign"), ("Calculate", "calc returns the answer"), ("Print", "cout shows the sum")]),
             narr="Here is the plan. First, cin reads the numbers and the sign. Next, the switch in calc picks the operation. "
                  "Then calc returns the answer. Last, cout prints the full line."),
    B=dict(file="convert.cpp", label="Unit converter", on="two small functions convert units",
           src='''
#include <iostream>
using namespace std;

double km_to_miles(double km) { return km * 0.621371; }
double c_to_f(double c) { return c * 9 / 5 + 32; }

int main() {
    cout << km_to_miles(10) << endl;
    cout << c_to_f(30) << endl;
    return 0;
}
''',
           narr="[HL 4] This function turns kilometres into miles. [HL 5] This one turns Celsius into Fahrenheit. "
                "[HL 8] Ten kilometres is about six point two one miles. [HL 9] Thirty degrees Celsius is eighty-six degrees Fahrenheit. "
                "Each function has one small job, so they are easy to test."),
    term="The program prints six point two one three seven one, and then eighty-six.",
    recap=["Plan the functions before you write the code.", "Each function does one job.",
           "Main joins the pieces together.", "Small functions are easy to test."],
    bug=dict(title="A function that forgets to return", file="calc.cpp", kind="warn", wrong_note="the default case has no return",
             wrong='''
#include <iostream>
using namespace std;

double calc(double a, char op, double b) {
    switch (op) {
        case '+': return a + b;
        case '-': return a - b;
    }
}

int main() {
    cout << calc(2, '+', 3) << endl;
    return 0;
}
''', fixed_note="a final return covers every path",
             fixed='''
#include <iostream>
using namespace std;

double calc(double a, char op, double b) {
    switch (op) {
        case '+': return a + b;
        case '-': return a - b;
    }
    return 0;
}

int main() {
    cout << calc(2, '+', 3) << endl;
    return 0;
}
''',
             why="If op is neither plus nor minus, the function reaches the end without a return. Every path must return a value.",
             narr="Bug of the Day. The calc function handles only plus and minus. For any other sign, it reaches the end with no return. "
                  "The compiler warns about control reaching the end of a non-void function. Add a final return for every other path."),
    pun="My calculator and I have a great relationship. We always add up.",
    task="add a power option to the calculator", challenge="Add a case for the sign caret in calc. It should return a raised to the power b. Use the pow function.",
    answer="Include cmath. Add case with the caret in single quotes. Return pow of a and b.",
))
