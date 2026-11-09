"""Module 1 — Variables and types (EP 5-12)."""
from lib import flow, mem, table

MODULE = {"id": 1, "name": "Variables and types", "range": "5–12", "colours": "Pastel blue + Tomato", "bg": "pastel blue"}
NEXT_AFTER = ("Next: EP 13 · if and else", "We end module one here. Next time: making decisions with if and else.")
EPISODES = []

EPISODES.append(dict(
    n=5, title="Variables and types", spoken="variables and types", yt="Variables and Types in C++: int, double, char, bool",
    thumb="VARIABLES + TYPES", vis="four labelled boxes marked int, double, char and bool",
    goals=["create variables of type int, double, char and bool", "pick the right type for a value", "give every variable a starting value"],
    tags=["c++ variables", "c++ data types", "int double char bool", "uninitialized variable"],
    analogy="a beach shack fridge: one shelf for bottles, one tray for ice",
    c_pts=["A variable is a named box in memory", "Every box has a type", "The type says what can go inside"],
    hook="Every value in your program lives in a box with a type.",
    intro="Until now, our programs only printed words. Today they learn to remember things. You will make boxes for numbers, letters and yes or no answers.",
    concept="A variable is a named box in memory. Every box has a type, and the type says what can go inside.\n"
            "Int holds whole numbers, like three fish. Double holds numbers with a decimal point. Char holds one single character. Bool holds only true or false. "
            "Think of a beach shack fridge. One shelf is for bottles, and one tray is for ice. Each place fits one job.",
    A=dict(file="vars.cpp", label="Four variables", on="four variables, each line shows type, name and value",
           src='''
#include <iostream>
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
}
''',
           narr="[HL 5] Int fish equals three. First comes the type, then the name, then the value. [HL 6] Double price equals one hundred twenty point five. "
                "[HL 7] Char grade equals A. Notice the single quotes around the letter. [HL 8] Bool open now equals true. "
                "[HL 9] Now we print each one. The names have no quotes, so cout prints the value inside the box, not the name."),
    ill=dict(label="Variables in memory", on="four memory boxes with value, size in bytes and address",
             data=mem([("fish", "int", "3"), ("price", "double", "120.5"), ("grade", "char", "'A'"), ("open_now", "bool", "true")],
                      caption="Each variable is a box with a name, a value, a size and an address"),
             narr="Here is what memory looks like. Each variable is a box with a name, a value and an address. An int takes four bytes on most computers. "
                  "A double is bigger. It takes eight bytes. A char takes one byte, and so does a bool. Different types have different sizes."),
    B=dict(file="sizes.cpp", label="Sizes of types", on="sizeof shows how many bytes each type uses",
           src='''
#include <iostream>
using namespace std;

int main() {
    cout << "int: " << sizeof(int) << endl;
    cout << "double: " << sizeof(double) << endl;
    cout << "char: " << sizeof(char) << endl;
    cout << "bool: " << sizeof(bool) << endl;
    return 0;
}
''',
           narr="[HL 5] The sizeof operator tells us how many bytes a type needs. [HL 5] For int, it prints four. [HL 6] A double needs eight bytes. "
                "[HL 7] A char needs one byte. [HL 8] A bool needs one byte as well. These numbers match the boxes we saw before."),
    term="Each line shows the size of one type. The numbers are four, eight, one and one.",
    recap=["A variable is a named box with a type.", "Use int for whole numbers and double for decimals.",
           "Use char for one letter and bool for true or false.", "Always give a variable a starting value."],
    bug=dict(title="A variable with no starting value", file="packets.cpp", kind="warn", show_fixed_out=True,
             wrong_note="packets never gets a value",
             wrong='''
#include <iostream>
using namespace std;

int main() {
    int packets;
    cout << "Packets: " << packets << endl;
    return 0;
}
''', fixed_note="packets starts at zero",
             fixed='''
#include <iostream>
using namespace std;

int main() {
    int packets = 0;
    cout << "Packets: " << packets << endl;
    return 0;
}
''',
             why="A variable that you do not set holds whatever was in that memory before. Always write a starting value, such as zero.",
             narr="Bug of the Day. Here we make an int called packets, but we never give it a value. The compiler warns us that packets is used uninitialized. "
                  "The program still builds, but it prints a strange number. That number is garbage left in memory. Give every variable a value when you make it."),
    pun="An uninitialised variable walks into a bar. The bartender asks, what will you have? It says, whatever was there before.",
    task="make four variables and print them", challenge="Make four variables: your age, your height in metres, your first initial and whether you like fish. Print all four.",
    answer="Use int, double, char and bool. For example, use seventeen, one point six five, the letter A and true. The bool prints as one.",
))

EPISODES.append(dict(
    n=6, title="Reading input with cin", spoken="reading input with cin", yt="C++ Input with cin: Ask the User a Question",
    thumb="ASK WITH CIN", vis="a speech bubble that asks a question",
    goals=["read a number with cin", "read two values in one line", "use the right arrows for input and output"],
    tags=["cin c++", "c++ input", "user input", "stream extraction operator"],
    analogy="a ticket counter: the program asks, and you answer through the window",
    c_pts=["cout sends data out", "cin brings data in", "The arrows show the direction"],
    hook="Make your program ask a question and listen.",
    intro="Today your program learns to listen. It asks a question, waits, and then uses your answer.",
    concept="Cout sends data out to the screen. Cin brings data in from the keyboard. The arrows show the direction of the data.\n"
            "For cout, the arrows point toward cout. For cin, they point toward the variable. Think of a ticket counter. The clerk asks where you go, and you answer.",
    A=dict(file="age.cpp", label="Ask for an age", on="the program asks for an age and adds one",
           src='''
#include <iostream>
using namespace std;

int main() {
    int age;
    cout << "Enter your age: ";
    cin >> age;
    cout << "Next year you will be " << age + 1 << endl;
    return 0;
}
''', stdin="17",
           narr="[HL 5] First we make an int called age. [HL 6] Then we print a question. There is no endl, so the cursor stays on the same line. "
                "[HL 7] Now cin reads a number from the keyboard and stores it in age. The arrows point at the variable. "
                "[HL 8] Last, we print age plus one. The program waits at line seven until you press Enter."),
    ill=dict(label="Data flows through arrows", on="a flow of data from the keyboard into the variable",
             data=flow([("Keyboard", "You type seventeen"), ("cin", "Reads the number"), ("age", "Stores seventeen"), ("cout", "Prints eighteen")]),
             narr="Follow the data. You type a number on the keyboard. The cin tool reads it. The variable age stores it. "
                  "Then cout prints a new number built from age."),
    B=dict(file="sum.cpp", label="Two numbers", on="one cin line reads two numbers",
           src='''
#include <iostream>
using namespace std;

int main() {
    int a, b;
    cout << "Enter two numbers: ";
    cin >> a >> b;
    cout << "Sum: " << a + b << endl;
    return 0;
}
''', stdin="4 9",
           narr="[HL 5] We make two ints in one line. [HL 7] One cin line reads both numbers. Type them with a space between. "
                "[TRACK a=4] The first number goes into a. [TRACK b=9] The second number goes into b. [HL 8] Then we print the sum, which is thirteen."),
    term="Type four, a space, and nine. Then press Enter. The program prints the sum.",
    recap=["Cout sends data out, and cin brings data in.", "The arrows point in the direction of the data.",
           "Cin stores the typed value in a variable.", "One cin line can read many values."],
    bug=dict(title="The arrows point the wrong way", file="age.cpp", kind="compile", stdin="17", wrong_note="cin uses the output arrows",
             wrong='''
#include <iostream>
using namespace std;

int main() {
    int age;
    cout << "Enter your age: ";
    cin << age;
    cout << "Next year you will be " << age + 1 << endl;
    return 0;
}
''', fixed_note="cin uses the input arrows",
             fixed='''
#include <iostream>
using namespace std;

int main() {
    int age;
    cout << "Enter your age: ";
    cin >> age;
    cout << "Next year you will be " << age + 1 << endl;
    return 0;
}
''',
             why="The arrows for cin point right, toward the variable. The arrows for cout point left, toward the stream.",
             narr="Bug of the Day. Here cin has arrows that point at cin. The compiler says no match for operator, with a long list. "
                  "Do not panic. The first line is the clue. Cin needs arrows that point at the variable. Change them, and the program builds."),
    pun="Why did the program wait for the user? It had a lot of input about commitment.",
    task="ask for two numbers and print their product", challenge="Ask the user for the length and width of a room. Print the area.",
    answer="Read two ints with one cin line. Print length times width, for example four times nine gives thirty-six.",
))

EPISODES.append(dict(
    n=7, title="Operators and expressions", spoken="operators and expressions", yt="C++ Operators: + - * / % Explained",
    thumb="MATH IN C++", vis="a calculator with plus, minus and percent keys",
    goals=["use the five arithmetic operators", "explain integer division and remainder", "use += and ++ to change a variable"],
    tags=["c++ operators", "modulus operator", "integer division", "increment operator"],
    analogy="sharing laddoos: the division gives each friend a share, the remainder is what is left",
    c_pts=["Plus, minus, times, divide and remainder", "Two ints divide to give an int", "Short forms: += and ++"],
    hook="Seventeen divided by five is three, not three point four.",
    intro="Today your program does maths. You will meet five operators, and one surprise about division.",
    concept="C plus plus has five arithmetic operators. They are plus, minus, times, divide and remainder. The remainder operator is the percent sign.\n"
            "When both numbers are ints, the answer is also an int. The decimal part is cut off. Think of sharing laddoos. Seventeen laddoos for five friends gives each friend three. Two laddoos stay in the box.",
    A=dict(file="ops.cpp", label="Five operators", on="seventeen and five with all five operators",
           src='''
#include <iostream>
using namespace std;

int main() {
    int a = 17, b = 5;
    cout << a + b << endl;
    cout << a - b << endl;
    cout << a * b << endl;
    cout << a / b << endl;
    cout << a % b << endl;
    return 0;
}
''',
           narr="[HL 5] We store seventeen in a and five in b. [HL 6] Plus gives twenty-two. [HL 7] Minus gives twelve. [HL 8] Times gives eighty-five. "
                "[HL 9] Divide gives three. Both are ints, so the decimal part is gone. [HL 10] Remainder gives two. That is what is left after sharing."),
    ill=dict(label="The operator table", on="a table: operator, meaning, example and result",
             data=table(["Operator", "Meaning", "Example", "Result"], [["+", "add", "17 + 5", "22"], ["-", "subtract", "17 - 5", "12"], ["*", "multiply", "17 * 5", "85"],
                                                                         ["/", "divide", "17 / 5", "3"], ["%", "remainder", "17 % 5", "2"]]),
             narr="Look at the table. Each row shows one operator, what it does, an example and the result. Pay attention to the last two rows. "
                  "Divide gives three, and remainder gives two. Together they say that five goes into seventeen three times, with two left."),
    B=dict(file="shorts.cpp", label="Short forms", on="plus-equals, plus-plus and a double division",
           src='''
#include <iostream>
using namespace std;

int main() {
    int visitors = 10;
    visitors += 5;
    visitors++;
    cout << "Visitors: " << visitors << endl;
    double half = 7 / 2.0;
    cout << "Half: " << half << endl;
    return 0;
}
''',
           narr="[HL 5] Visitors starts at ten. [HL 6] The plus-equals operator adds five. [TRACK visitors=15] Now visitors is fifteen. "
                "[HL 7] The plus-plus operator adds one. [TRACK visitors=16] Now it is sixteen. "
                "[HL 9] Here one number is a double, so the division keeps the decimal part. Seven divided by two point zero gives three point five."),
    term="The program prints sixteen visitors, and then three point five.",
    recap=["The five operators are plus, minus, times, divide and remainder.", "Two ints divide to give an int.",
           "The percent sign gives the remainder.", "The short forms plus-equals and plus-plus change a variable in place."],
    bug=dict(title="Integer division cuts the decimals", file="avg.cpp", kind="output", wrong_note="both numbers are ints",
             wrong='''
#include <iostream>
using namespace std;

int main() {
    double average = (7 + 8) / 2;
    cout << "Average: " << average << endl;
    return 0;
}
''', fixed_note="the divisor is a double",
             fixed='''
#include <iostream>
using namespace std;

int main() {
    double average = (7 + 8) / 2.0;
    cout << "Average: " << average << endl;
    return 0;
}
''',
             why="The division happens before the result goes into the double. Two ints give an int, so the decimal part is already gone.",
             narr="Bug of the Day. We want the average of seven and eight. The answer should be seven point five. But the program prints seven. "
                  "Both numbers in the division are ints, so C plus plus cuts the decimals before it stores the result. Write two point zero, and the answer is right."),
    pun="Why was the number seven so calm? It had no remainder.",
    task="split a bill between friends", challenge="A bill is two hundred and fifty rupees for four friends. Print the share and the remainder.",
    answer="Use int total equals two hundred fifty. Print total divided by four, which is sixty-two, and total remainder four, which is two.",
))

EPISODES.append(dict(
    n=8, title="Comparison and logical operators", spoken="comparison and logical operators", yt="C++ Comparison and Logical Operators",
    thumb="TRUE OR FALSE", vis="a traffic light with a green tick and a red cross",
    goals=["compare two values", "combine tests with and, or and not", "print bool values as true and false"],
    tags=["c++ logical operators", "comparison operators", "boolalpha", "and or not"],
    analogy="a cinema gate: you need a ticket and the right age",
    c_pts=["A comparison gives true or false", "And needs both tests true", "Or needs one test true"],
    hook="Every decision in your program starts as true or false.",
    intro="Today we ask questions in code. Is a number bigger? Are two values equal? Each answer is true or false.",
    concept="A comparison asks a question about two values. The answer is a bool, so it is true or false. The comparison operators are less than, greater than, equal to and not equal to.\n"
            "The logical operators join tests. And needs both tests to be true. Or needs only one. Not flips the answer. Think of a cinema gate. You need a ticket and the right age.",
    A=dict(file="logic.cpp", label="Four questions", on="four tests print true or false",
           src='''
#include <iostream>
using namespace std;

int main() {
    int age = 17;
    bool has_pass = true;
    cout << boolalpha;
    cout << (age >= 18) << endl;
    cout << (age < 18 && has_pass) << endl;
    cout << (age == 17 || age == 18) << endl;
    cout << !has_pass << endl;
    return 0;
}
''',
           narr="[HL 7] Boolalpha makes cout print true and false instead of one and zero. [HL 8] Is seventeen greater than or equal to eighteen? No, so false. "
                "[HL 9] Is age under eighteen, and does the person have a pass? Both are true, so the answer is true. "
                "[HL 10] Is age seventeen, or is it eighteen? One test is true, so the answer is true. [HL 11] Not has pass flips true into false."),
    ill=dict(label="Truth table", on="a table for and, or and not",
             data=table(["A", "B", "A && B", "A || B"], [["true", "true", "true", "true"], ["true", "false", "false", "true"],
                                                          ["false", "true", "false", "true"], ["false", "false", "false", "false"]]),
             narr="This table shows all cases for two tests, A and B. And is true only in the first row. Or is false only in the last row. "
                  "Not has one input. It always gives the opposite value."),
    B=dict(file="range.cpp", label="A range test", on="is a mark between zero and one hundred?",
           src='''
#include <iostream>
using namespace std;

int main() {
    int mark = 72;
    bool valid = mark >= 0 && mark <= 100;
    bool pass = mark >= 35;
    cout << boolalpha << valid << " " << pass << endl;
    return 0;
}
''',
           narr="[HL 5] The mark is seventy-two. [HL 6] A valid mark must be at least zero and at most one hundred. We join two tests with and. "
                "[HL 7] A pass needs at least thirty-five. [HL 8] Both bools print as true. Always write the two tests in full. Never write zero less than mark less than one hundred."),
    term="The program prints true and true.",
    recap=["A comparison gives a bool.", "Use two equals signs to test for equality.",
           "And needs both tests true, or needs one, and not flips the answer.", "Boolalpha prints true and false as words."],
    bug=dict(title="One equals sign instead of two", file="check.cpp", kind="warn", wrong_note="the test uses a single equals sign",
             wrong='''
#include <iostream>
using namespace std;

int main() {
    int seats = 40;
    if (seats = 0) {
        cout << "Bus is full" << endl;
    }
    return 0;
}
''', fixed_note="the test uses two equals signs",
             fixed='''
#include <iostream>
using namespace std;

int main() {
    int seats = 40;
    if (seats == 0) {
        cout << "Bus is full" << endl;
    }
    return 0;
}
''',
             why="A single equals sign stores a value. Two equals signs compare. The wrong test also changes seats to zero.",
             narr="Bug of the Day. Here the if test uses one equals sign. That does not compare. It stores zero in seats. The compiler warns about an assignment used as a truth value. "
                  "Use two equals signs to compare. Always read warnings. They often point at real bugs."),
    pun="Why was the boolean so honest? It only knew true or false.",
    task="test whether a year is a leap year", challenge="Write one bool expression that is true when a number is even and bigger than ten.",
    answer="Use n remainder two equals equals zero, and n greater than ten, joined with two ampersands.",
))

EPISODES.append(dict(
    n=9, title="Type conversion and casting", spoken="type conversion and casting", yt="C++ Type Conversion and static_cast",
    thumb="CHANGE THE TYPE", vis="a double crossing a bridge and becoming an int",
    goals=["predict what happens when types mix", "convert with static_cast", "avoid the integer-division trap"],
    tags=["c++ type casting", "static_cast", "implicit conversion", "narrowing"],
    analogy="pouring water from a jug into a small glass: some may be lost",
    c_pts=["C++ converts types for you", "A double becomes an int by cutting the decimals", "static_cast makes your choice clear"],
    hook="A double can lose its decimals without any error.",
    intro="Today we mix types. Sometimes C plus plus changes a type for you. You must know when, and what is lost.",
    concept="C plus plus converts types when you mix them. An int becomes a double with no loss. A double becomes an int by cutting off the decimals. It does not round.\n"
            "A cast is a clear request to convert. In modern C plus plus, we write static cast. Think of a jug and a small glass. Pour the jug into the glass, and some water is lost.",
    A=dict(file="convert.cpp", label="Automatic conversion", on="an int becomes a double, and a double becomes an int",
           src='''
#include <iostream>
using namespace std;

int main() {
    int fish = 7;
    double weight = fish;
    double price = 9.99;
    int whole = price;
    cout << weight << endl;
    cout << whole << endl;
    return 0;
}
''',
           narr="[HL 5] Fish is an int with the value seven. [HL 6] We store it in a double. No loss happens. The weight is seven. "
                "[HL 7] Price is nine point nine nine. [HL 8] We store it in an int. The compiler cuts the decimals. [TRACK whole=9] Whole is nine, not ten. "
                "[HL 9] The first print shows seven. [HL 10] The second print shows nine."),
    ill=dict(label="Conversion rules", on="a table: from type, to type and what happens",
             data=table(["From", "To", "What happens"], [["int", "double", "Exact value, no loss"], ["double", "int", "Decimals are cut off"],
                                                         ["char", "int", "You get the letter code"], ["bool", "int", "True is one, false is zero"]]),
             narr="Look at the rules. Int to double is safe. Double to int cuts the decimals, so you lose data. "
                  "Char to int gives the code of the letter. Bool to int gives one for true and zero for false."),
    B=dict(file="cast.cpp", label="static_cast", on="static_cast converts a value on purpose",
           src='''
#include <iostream>
using namespace std;

int main() {
    int passed = 7, total = 8;
    double ratio = static_cast<double>(passed) / total;
    cout << ratio << endl;
    char letter = 'A';
    cout << static_cast<int>(letter) << endl;
    return 0;
}
''',
           narr="[HL 5] We have seven passed students out of eight. [HL 6] We cast passed to a double first. Then the division keeps the decimals. "
                "The answer is zero point eight seven five. [HL 8] Here we cast the letter A to an int. [HL 9] It prints sixty-five. That is the code of the letter A."),
    term="The program prints zero point eight seven five, and then sixty-five.",
    recap=["C plus plus converts types for you.", "A double becomes an int by cutting the decimals.",
           "Use static cast to convert on purpose.", "Cast one number before you divide."],
    bug=dict(title="Casting too late", file="ratio.cpp", kind="output", wrong_note="the cast covers the division, not the numbers",
             wrong='''
#include <iostream>
using namespace std;

int main() {
    int passed = 7, total = 8;
    double ratio = static_cast<double>(passed / total);
    cout << ratio << endl;
    return 0;
}
''', fixed_note="the cast covers one number",
             fixed='''
#include <iostream>
using namespace std;

int main() {
    int passed = 7, total = 8;
    double ratio = static_cast<double>(passed) / total;
    cout << ratio << endl;
    return 0;
}
''',
             why="Seven divided by eight is already zero when both are ints. The cast then turns the zero into a double, which is too late.",
             narr="Bug of the Day. We cast the result of the division. The program prints zero. Why? Seven divided by eight is zero in int maths. "
                  "The cast comes too late. Put the cast on one number, before the division. Then the answer is zero point eight seven five."),
    pun="I tried to cast a spell on my double. It lost its decimals and its magic.",
    task="find the average of three marks", challenge="Store three int marks. Print their average as a double with decimals.",
    answer="Add the three marks, cast the sum to a double, and divide by three. Use static cast before the division.",
))

EPISODES.append(dict(
    n=10, title="auto, const and constexpr", spoken="auto, const and constexpr", yt="C++ auto, const and constexpr Explained",
    thumb="LOCK IT DOWN", vis="a padlock on a box",
    goals=["let the compiler pick a type with auto", "protect a value with const", "explain what constexpr adds"],
    tags=["c++ auto keyword", "const in c++", "constexpr", "read-only variable"],
    analogy="a sealed jar of masala: you can look at it, but you cannot change it",
    c_pts=["auto lets the compiler find the type", "const stops a value from changing", "constexpr fixes the value at compile time"],
    hook="Some values must never change.",
    intro="Today we learn three keywords. One saves typing, and two protect your values from mistakes.",
    concept="The keyword auto tells the compiler to find the type from the value. The keyword const makes a variable read-only. You cannot change it after you set it.\n"
            "The keyword constexpr is stronger. The value must be known when the program is compiled. Think of a sealed jar of masala. You can look at it, but you cannot change what is inside.",
    A=dict(file="keywords.cpp", label="Three keywords", on="auto, const and constexpr in one program",
           src='''
#include <iostream>
using namespace std;

int main() {
    const int max_seats = 40;
    constexpr double pi = 3.14159;
    auto fare = 25.5;
    auto seats = 12;
    cout << "Max: " << max_seats << endl;
    cout << "Fare: " << fare * seats << endl;
    cout << "Pi: " << pi << endl;
    return 0;
}
''',
           narr="[HL 5] Max seats is const. It stays forty for the whole program. [HL 6] Pi is constexpr. The compiler knows its value before the program runs. "
                "[HL 7] Auto sees twenty-five point five and picks double. [HL 8] Auto sees twelve and picks int. "
                "[HL 10] The fare is a double times an int. The answer is three hundred and six."),
    ill=dict(label="Types and locks", on="memory boxes: two locked boxes and two auto boxes",
             data=mem([("max_seats", "const int", "40"), ("pi", "constexpr double", "3.14159", "static"), ("fare", "double", "25.5"), ("seats", "int", "12")],
                      caption="The compiler found double and int for the auto variables"),
             narr="Here is the memory. Max seats and pi are locked. The program cannot change them. Pi lives in the static region, because the compiler fixed it early. "
                  "The auto variables fare and seats look like ordinary boxes. The compiler picked their types for us."),
    B=dict(file="area.cpp", label="A const in use", on="const protects a value used in a formula",
           src='''
#include <iostream>
using namespace std;

int main() {
    constexpr double pi = 3.14159;
    const double radius = 2.0;
    auto area = pi * radius * radius;
    cout << "Area: " << area << endl;
    return 0;
}
''',
           narr="[HL 5] Pi is a constexpr. [HL 6] The radius is const. We promise not to change it. "
                "[HL 7] Auto picks double for the area, because pi and radius are doubles. [HL 8] The area is twelve point five six."),
    term="The program prints the area, twelve point five six.",
    recap=["Auto lets the compiler find the type.", "Const makes a variable read-only.",
           "Constexpr needs a value known at compile time.", "Use const for every value that should not change."],
    bug=dict(title="Changing a const", file="seats.cpp", kind="compile", wrong_note="the code changes a const variable",
             wrong='''
#include <iostream>
using namespace std;

int main() {
    const int max_seats = 40;
    max_seats = 50;
    cout << max_seats << endl;
    return 0;
}
''', fixed_note="the extra line is gone",
             fixed='''
#include <iostream>
using namespace std;

int main() {
    const int max_seats = 40;
    cout << max_seats << endl;
    return 0;
}
''',
             why="A const variable is read-only. The compiler refuses any line that tries to change it. That is the whole point of const.",
             narr="Bug of the Day. Max seats is const, but line six tries to change it. The compiler says assignment of read-only variable. "
                  "That is a good error. It stops a real bug before the program runs. Remove the line, or remove const if the value must change."),
    pun="I put a const on my bank balance. Now it will never change, and that is the problem.",
    task="make a circle program with const", challenge="Use constexpr for pi and const for a radius that you choose. Print the area and the circumference.",
    answer="Area is pi times radius times radius. Circumference is two times pi times radius. Let auto pick the types.",
))

EPISODES.append(dict(
    n=11, title="Strings with std::string", spoken="strings with std string", yt="C++ Strings: std::string for Beginners",
    thumb="TEXT IN C++", vis="a string of beads, each bead a letter",
    goals=["create and join strings", "read the size and one letter of a string", "use substr and find"],
    tags=["std::string", "c++ strings", "string functions", "substr find"],
    analogy="a string of beads: each bead is one letter, counted from zero",
    c_pts=["std::string holds text of any length", "Plus joins two strings", "Letters are counted from zero"],
    hook="Strings in C plus plus grow and shrink as you need.",
    intro="Today we work with text. The std string type can hold a word, a sentence or a whole page.",
    concept="The std string type holds text of any length. Plus joins two strings. The size function tells you how many letters it holds.\n"
            "Each letter has a position, called an index. The first index is zero, not one. Think of a string of beads. Each bead is one letter, and you count from the first bead as zero.",
    A=dict(file="text.cpp", label="Join and measure", on="join two strings and read the size and the first letter",
           src='''
#include <iostream>
#include <string>
using namespace std;

int main() {
    string first = "Goa";
    string second = " beach";
    string full = first + second;
    cout << full << endl;
    cout << full.size() << endl;
    cout << full[0] << endl;
    return 0;
}
''',
           narr="[HL 3] The string header gives us the string type. [HL 6] First holds Goa. [HL 7] Second holds a space and then beach. "
                "[HL 8] Plus joins them into full. [HL 9] The print shows Goa beach. [HL 10] The size is nine letters, and the space counts. "
                "[HL 11] Index zero is the first letter, which is G."),
    ill=dict(label="Counting letters", on="a table of string calls and their results for the text Goa beach",
             data=table(["Call", "Result"], [["full.size()", "9"], ["full[0]", "G"], ["full[4]", "b"], ["full.substr(0, 3)", "Goa"], ["full.find(\"beach\")", "4"]]),
             narr="Here is the text Goa beach with its calls. The size is nine. Index zero is G. Index four is the letter b, after the space. "
                  "Substr cuts three letters from index zero, and gives Goa. Find gives the index where beach starts. That index is four."),
    B=dict(file="cut.cpp", label="substr and find", on="find a word and cut it out",
           src='''
#include <iostream>
#include <string>
using namespace std;

int main() {
    string line = "Goa is sunny today";
    size_t pos = line.find("sunny");
    cout << pos << endl;
    cout << line.substr(pos, 5) << endl;
    line.append("!");
    cout << line << endl;
    return 0;
}
''',
           narr="[HL 6] The find function looks for the word sunny. It returns the index where the word starts. [TRACK pos=7] Here that index is seven. "
                "[HL 8] The substr function cuts five letters from that index. It prints sunny. [HL 9] The append function adds an exclamation mark at the end. [HL 10] The full line is printed."),
    term="The program prints seven, then sunny, then the whole line with the exclamation mark.",
    recap=["The std string type holds text of any length.", "Plus joins two strings.",
           "The first index is zero.", "The functions size, find, substr and append do the common jobs."],
    bug=dict(title="Adding two quoted texts", file="join.cpp", kind="compile", wrong_note="plus joins two plain quoted texts",
             wrong='''
#include <iostream>
#include <string>
using namespace std;

int main() {
    string s = "Hi" + " there";
    cout << s << endl;
    return 0;
}
''', fixed_note="the first text is a string",
             fixed='''
#include <iostream>
#include <string>
using namespace std;

int main() {
    string s = string("Hi") + " there";
    cout << s << endl;
    return 0;
}
''',
             why="A text in quotes is a plain character array, not a std string. Plus works when at least one side is a std string.",
             narr="Bug of the Day. We try to add two quoted texts. The compiler says invalid operands to binary plus. "
                  "A quoted text is a plain character array, not a std string. Plus needs at least one real std string. Wrap the first text in string, and it works."),
    pun="Why did the string go to therapy? It could not stop feeling cut off.",
    task="build a greeting from two strings", challenge="Store a first name and a village in two strings. Print the sentence, Asha lives in Mapusa, with your own words.",
    answer="Join the strings with plus, and put the spaces and the words lives in between, inside quotes. At least one side must be a string.",
))

EPISODES.append(dict(
    n=12, title="Formatting output", spoken="formatting output", yt="C++ Output Formatting: setw, setprecision and std::format",
    thumb="TIDY OUTPUT", vis="a neat price list with aligned columns",
    goals=["set the number of decimals", "align columns with setw", "build a line with std::format"],
    tags=["setprecision", "setw", "std::format", "c++ output formatting"],
    analogy="a bill at a restaurant: every price lines up on the right",
    c_pts=["fixed and setprecision set the decimals", "setw sets the width of a column", "std::format builds a text from a pattern"],
    hook="Make your output look like a real bill.",
    intro="Today we make output tidy. Prices get two decimals, and columns line up like a real bill.",
    concept="Raw output can look messy. Fixed and setprecision give a set number of decimals. Setw sets the width of the next item, so columns line up.\n"
            "These tools live in the iomanip header. Since C plus plus twenty, std format builds a line from a pattern. Think of a restaurant bill, where all the prices line up on the right.",
    A=dict(file="bill.cpp", label="A neat bill", on="fixed, setprecision and setw make a bill",
           src='''
#include <iomanip>
#include <iostream>
using namespace std;

int main() {
    cout << fixed << setprecision(2);
    cout << setw(8) << "Fish" << setw(8) << 120.5 << endl;
    cout << setw(8) << "Rice" << setw(8) << 45.0 << endl;
    cout << setw(8) << "Total" << setw(8) << 165.5 << endl;
    return 0;
}
''',
           narr="[HL 1] The iomanip header gives us the format tools. [HL 6] Fixed means always show decimals. Setprecision two means exactly two decimals. "
                "[HL 7] Setw eight gives the next item a column eight characters wide. The text is pushed to the right. "
                "[HL 8] The next row lines up under the first row. [HL 9] The total row lines up as well."),
    ill=dict(label="Format tools", on="a table of the tools and what they do",
             data=table(["Tool", "Header", "Effect"], [["fixed", "iostream", "Always show decimals"], ["setprecision(n)", "iomanip", "Sets the decimals"],
                                                       ["setw(n)", "iomanip", "Width of the next item"], ["std::format", "format", "Builds text from a pattern"]]),
             narr="Four tools, one table. Fixed and setprecision control decimals. Setw controls the width of one item. "
                  "The std format function is new in C plus plus twenty. It builds text from a pattern with curly braces."),
    B=dict(file="pattern.cpp", label="std::format", on="a pattern with two holes fills a line",
           src='''
#include <format>
#include <iostream>
#include <string>
using namespace std;

int main() {
    string line = format("{} costs {:.2f} rupees", "Fish", 120.5);
    cout << line << endl;
    return 0;
}
''',
           narr="[HL 3] The format header gives us std format. [HL 8] The pattern has two holes, written as curly braces. "
                "The first hole takes the name. The second hole takes the price. The code colon dot two f means two decimals. [HL 9] Cout prints the finished line."),
    term="The program prints, Fish costs one hundred twenty point five zero rupees.",
    recap=["Fixed and setprecision control the decimals.", "Setw sets the width of the next item.",
           "Both live in the iomanip header.", "Std format builds a line from a pattern."],
    bug=dict(title="Precision without fixed", file="price.cpp", kind="output", wrong_note="setprecision is used without fixed",
             wrong='''
#include <iomanip>
#include <iostream>
using namespace std;

int main() {
    cout << setprecision(2) << 120.5 << endl;
    return 0;
}
''', fixed_note="fixed is added",
             fixed='''
#include <iomanip>
#include <iostream>
using namespace std;

int main() {
    cout << fixed << setprecision(2) << 120.5 << endl;
    return 0;
}
''',
             why="Without fixed, setprecision counts all digits, not only the decimals. Two digits is not enough for one hundred twenty, so cout uses a short scientific form.",
             narr="Bug of the Day. We want one hundred twenty point five zero. The program prints a strange short form, one point two e plus zero two. "
                  "Without fixed, setprecision counts all the digits. Add fixed before setprecision, and you get two decimals."),
    pun="My output was so untidy that even cout asked for a setw.",
    task="print a three-row bill", challenge="Print a bill with three items. Use fixed, setprecision and setw so that the prices line up.",
    answer="Use cout with fixed and setprecision two once, then setw eight before each name and each price.",
))
