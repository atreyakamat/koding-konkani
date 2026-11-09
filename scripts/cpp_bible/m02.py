"""Module 2 — Decisions and loops (EP 13-20)."""
from lib import flow, graph, table

MODULE = {"id": 2, "name": "Decisions and loops", "range": "13–20", "colours": "Cream + Apricot", "bg": "cream"}
NEXT_AFTER = ("Next: EP 21 · Functions", "We end module two here. Next time: functions, the building blocks of every program.")
EPISODES = []

EPISODES.append(dict(
    n=13, title="if and else", spoken="if and else", yt="C++ if and else: Make Your Program Decide",
    thumb="IF OR ELSE?", vis="a road that splits into two paths",
    goals=["write an if statement", "add an else branch", "use braces around every branch"],
    tags=["c++ if else", "decision making c++", "conditional statements", "empty body warning"],
    analogy="a fork in the road: the sign decides which way you walk",
    c_pts=["An if statement tests a condition", "The body runs only when the test is true", "Else runs when the test is false"],
    hook="Your program can choose between two paths.",
    intro="Today your program learns to decide. It tests a condition, and then it takes one of two paths.",
    concept="An if statement tests a condition. If the condition is true, the body runs. If it is false, the body is skipped.\n"
            "Add an else branch for the false case. Exactly one branch runs. Think of a fork in the road. A sign says which way to walk, and you never take both paths.",
    A=dict(file="result.cpp", label="Pass or fail", on="an if and else branch decide on a mark",
           src='''
#include <iostream>
using namespace std;

int main() {
    int marks = 72;
    if (marks >= 35) {
        cout << "Pass" << endl;
    } else {
        cout << "Fail" << endl;
    }
    return 0;
}
''',
           narr="[HL 5] Marks is seventy-two. [HL 6] The if tests whether marks is at least thirty-five. The test sits inside round brackets. "
                "[HL 7] The test is true, so this line runs and prints Pass. [HL 8] The else branch is skipped. [HL 9] It would print Fail, but only for a mark below thirty-five."),
    ill=dict(label="Two paths", on="a decision tree: the test, and the true and false paths",
             data=graph([("test", "marks >= 35 ?"), ("pass", "Print Pass", "runs when true"), ("fail", "Print Fail", "runs when false")],
                        [("test", "pass", "true"), ("test", "fail", "false")], layout="tree"),
             narr="Here is the decision as a tree. The test is at the top. If it is true, we follow the left path and print Pass. "
                  "If it is false, we follow the right path and print Fail. The program never follows both paths."),
    B=dict(file="parity.cpp", label="Even or odd", on="the remainder decides if a number is even or odd",
           src='''
#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;
    if (n % 2 == 0) {
        cout << n << " is even" << endl;
    } else {
        cout << n << " is odd" << endl;
    }
    return 0;
}
''', stdin="7",
           narr="[HL 6] Cin reads a number. [HL 7] An even number has remainder zero when we divide by two. [HL 8] That branch prints even. "
                "[HL 9] Seven has remainder one, so the else branch runs. [HL 10] The program prints seven is odd."),
    term="Type seven and press Enter. The program prints seven is odd.",
    recap=["An if statement tests a condition.", "The body runs only when the test is true.",
           "Else runs when the test is false.", "Always use braces, even for one line."],
    bug=dict(title="A semicolon after the if", file="result.cpp", kind="warn", wrong_note="a semicolon sits after the test",
             wrong='''
#include <iostream>
using namespace std;

int main() {
    int marks = 20;
    if (marks >= 35);
    {
        cout << "Pass" << endl;
    }
    return 0;
}
''', fixed_note="the semicolon is gone",
             fixed='''
#include <iostream>
using namespace std;

int main() {
    int marks = 20;
    if (marks >= 35) {
        cout << "Pass" << endl;
    }
    return 0;
}
''',
             why="A semicolon after the test is an empty body. The block below it is then an ordinary block, and it always runs.",
             narr="Bug of the Day. A semicolon sits after the if test. C plus plus reads it as an empty body. The block below then always runs. "
                  "With marks equal to twenty, the program would still print Pass. The compiler warns about an empty body. Remove the semicolon."),
    pun="Why did the if statement break up with else? It said, you are always my second choice.",
    task="decide if a number is positive", challenge="Read a number. Print positive if it is greater than zero, and not positive in all other cases.",
    answer="Use cin to read n. Test n greater than zero. Print positive in the if branch, and not positive in the else branch.",
))

EPISODES.append(dict(
    n=14, title="else if ladders", spoken="else if ladders", yt="C++ else if Ladder: Grades and Choices",
    thumb="THE LADDER", vis="a ladder with a grade letter on each rung",
    goals=["chain several tests with else if", "order the tests from strict to loose", "use a final else for all other cases"],
    tags=["else if c++", "if else ladder", "grade calculator", "c++ conditions"],
    analogy="a ladder: you climb down until a rung fits",
    c_pts=["Tests run from the top down", "The first true test wins", "The last else catches everything else"],
    hook="The order of your tests changes the answer.",
    intro="Today we handle more than two cases. We build a grade calculator with an else if ladder.",
    concept="An else if ladder checks tests from the top down. The first true test runs, and the rest are skipped. A final else catches all other cases.\n"
            "The order matters. Put the strictest test first. Think of a ladder. You climb down from the top until you find a rung that fits.",
    A=dict(file="grade.cpp", label="A grade ladder", on="an else if ladder turns marks into a grade",
           src='''
#include <iostream>
using namespace std;

int main() {
    int marks = 82;
    if (marks >= 90) {
        cout << "Grade A" << endl;
    } else if (marks >= 75) {
        cout << "Grade B" << endl;
    } else if (marks >= 50) {
        cout << "Grade C" << endl;
    } else {
        cout << "Grade D" << endl;
    }
    return 0;
}
''',
           narr="[HL 5] Marks is eighty-two. [HL 6] Is it at least ninety? No, so we move down. [HL 8] Is it at least seventy-five? Yes. "
                "[HL 9] This branch prints Grade B. The ladder stops here. [HL 10] The tests below never run. [HL 12] The last else would catch every mark below fifty."),
    ill=dict(label="Grade bands", on="a table: marks and grade",
             data=table(["Marks", "Test", "Grade"], [["90 and up", "marks >= 90", "A"], ["75 to 89", "marks >= 75", "B"], ["50 to 74", "marks >= 50", "C"], ["Below 50", "else", "D"]]),
             narr="This table shows the bands. Each test only needs the lower limit. The tests above it have already removed the higher marks. "
                  "That is why order is so important."),
    B=dict(file="ticket.cpp", label="Ticket prices", on="the age picks the ticket price",
           src='''
#include <iostream>
using namespace std;

int main() {
    int age = 65;
    int price;
    if (age < 5) {
        price = 0;
    } else if (age < 18) {
        price = 50;
    } else if (age < 60) {
        price = 100;
    } else {
        price = 60;
    }
    cout << "Price: " << price << endl;
    return 0;
}
''',
           narr="[HL 5] The age is sixty-five. [HL 7] Under five is free. [HL 9] Under eighteen pays fifty. [HL 11] Under sixty pays one hundred. "
                "[HL 13] Everyone else gets the senior price of sixty. [TRACK price=60] Sixty-five matches the else branch. [HL 16] The program prints the price."),
    term="The program prints Price colon sixty.",
    recap=["An else if ladder checks tests from the top down.", "The first true test runs, and the rest are skipped.",
           "Put the strictest test first.", "A final else catches every other case."],
    bug=dict(title="Tests in the wrong order", file="grade.cpp", kind="output", wrong_note="the loose test comes first",
             wrong='''
#include <iostream>
using namespace std;

int main() {
    int marks = 82;
    if (marks >= 35) {
        cout << "Pass" << endl;
    } else if (marks >= 75) {
        cout << "Distinction" << endl;
    }
    return 0;
}
''', fixed_note="the strict test comes first",
             fixed='''
#include <iostream>
using namespace std;

int main() {
    int marks = 82;
    if (marks >= 75) {
        cout << "Distinction" << endl;
    } else if (marks >= 35) {
        cout << "Pass" << endl;
    }
    return 0;
}
''',
             why="Eighty-two passes the first test, so the ladder stops. The strict test below never gets a turn.",
             narr="Bug of the Day. A student has eighty-two marks. The program prints Pass, not Distinction. The loose test is first, and eighty-two passes it. "
                  "The ladder stops there. Always put the strictest test first. Then the ladder works from the top down."),
    pun="I built a ladder of else ifs. Now I cannot find the right rung to get down.",
    task="write a ladder for temperature", challenge="Write an else if ladder for a temperature. Print hot above thirty-five, warm above twenty-five, and cool for the rest.",
    answer="Test temperature greater than thirty-five first. Then test greater than twenty-five. End with an else that prints cool.",
))

EPISODES.append(dict(
    n=15, title="switch and case", spoken="switch and case", yt="C++ switch Statement: Menus Made Easy",
    thumb="SWITCH IT", vis="a menu board with numbered dishes",
    goals=["write a switch with case labels", "use break to end each case", "add a default case"],
    tags=["c++ switch case", "switch statement", "break in switch", "fall through"],
    analogy="a restaurant menu: you say a number and the kitchen makes that dish",
    c_pts=["Switch jumps to the matching case", "Break ends the case", "Default handles all other values"],
    hook="One missing word makes a switch run two cases.",
    intro="Today we build a menu with switch. It is a neat way to pick one action from many.",
    concept="A switch statement compares one value with many case labels. It jumps to the matching case. The break keyword ends that case.\n"
            "The default case handles all other values. Without break, the program falls through into the next case. Think of a menu board. You say a number, and the kitchen makes that dish.",
    A=dict(file="day.cpp", label="Name the day", on="a switch turns a number into a day name",
           src='''
#include <iostream>
using namespace std;

int main() {
    int day = 3;
    switch (day) {
        case 1: cout << "Monday" << endl; break;
        case 2: cout << "Tuesday" << endl; break;
        case 3: cout << "Wednesday" << endl; break;
        default: cout << "Another day" << endl;
    }
    return 0;
}
''',
           narr="[HL 5] Day is three. [HL 6] The switch looks at the value of day. [HL 7] Case one does not match. [HL 8] Case two does not match. "
                "[HL 9] Case three matches, so the program prints Wednesday. Then break leaves the switch. [HL 10] The default case runs when no case matches."),
    ill=dict(label="Jump to the case", on="a table: value, case and output",
             data=table(["day", "Matching case", "Output"], [["1", "case 1", "Monday"], ["2", "case 2", "Tuesday"], ["3", "case 3", "Wednesday"], ["Any other", "default", "Another day"]]),
             narr="The table shows how the switch picks a case. The value of day finds the matching row. "
                  "If no row matches, the default row runs. Case labels must be whole numbers or characters, not text."),
    B=dict(file="menu.cpp", label="A character menu", on="a switch on a character with a shared case",
           src='''
#include <iostream>
using namespace std;

int main() {
    char choice = 'b';
    switch (choice) {
        case 'a':
        case 'A':
            cout << "Add" << endl;
            break;
        case 'b':
        case 'B':
            cout << "Buy" << endl;
            break;
        default:
            cout << "Unknown" << endl;
    }
    return 0;
}
''',
           narr="[HL 5] The choice is the letter b. [HL 7] Two case labels can share one action. Here the letters a and A both add. "
                "[HL 11] Our letter b matches this case. [HL 13] It prints Buy. [HL 14] Break then ends the switch. [HL 15] Default would handle any other letter."),
    term="The program prints Buy.",
    recap=["Switch compares one value with many cases.", "Break ends a case.",
           "Default handles all other values.", "Two cases can share one action."],
    bug=dict(title="A missing break", file="day.cpp", kind="warn", wrong_note="case three has no break",
             wrong='''
#include <iostream>
using namespace std;

int main() {
    int day = 3;
    switch (day) {
        case 3: cout << "Wednesday" << endl;
        case 4: cout << "Thursday" << endl; break;
        default: cout << "Another day" << endl;
    }
    return 0;
}
''', fixed_note="case three has a break",
             fixed='''
#include <iostream>
using namespace std;

int main() {
    int day = 3;
    switch (day) {
        case 3: cout << "Wednesday" << endl; break;
        case 4: cout << "Thursday" << endl; break;
        default: cout << "Another day" << endl;
    }
    return 0;
}
''',
             why="Without break, the program keeps running into the next case. This is called fall-through.",
             narr="Bug of the Day. Case three has no break. The program prints Wednesday, and then Thursday too. "
                  "It falls through into the next case, and the compiler warns about it. Without a break, the switch does not stop. Add break at the end of each case."),
    pun="I asked the switch for a table at the restaurant. It gave me two, because I forgot the break.",
    task="make a calculator menu", challenge="Use a switch on a character. For plus, minus and times, print the result of seven and three.",
    answer="Use case with single quotes for each sign. Print seven plus three, seven minus three and seven times three, and add break after each.",
))

EPISODES.append(dict(
    n=16, title="while loops", spoken="while loops", yt="C++ while Loop: Repeat Until Done",
    thumb="LOOP IT", vis="a crab running in a circle",
    goals=["write a while loop", "update the loop variable", "predict the number of rounds"],
    tags=["c++ while loop", "loops in c++", "loop variable", "off by one"],
    analogy="a ceiling fan: it keeps turning while the switch is on",
    c_pts=["A loop repeats a block", "The test runs before each round", "Update the variable or the loop never ends"],
    hook="One small mistake can make a loop run forever.",
    intro="Today your program learns to repeat. A loop does the same job again and again, with no copy and paste.",
    concept="A while loop repeats a block as long as its test is true. The test runs before every round. When the test is false, the loop ends.\n"
            "You must change the loop variable inside the body. If you do not, the test stays true, and the loop never ends. Think of a ceiling fan. It keeps turning while the switch is on.",
    A=dict(file="countdown.cpp", label="A countdown", on="a while loop counts down from three",
           src='''
#include <iostream>
using namespace std;

int main() {
    int n = 3;
    while (n > 0) {
        cout << n << endl;
        n--;
    }
    cout << "Liftoff!" << endl;
    return 0;
}
''',
           narr="[HL 5] We start n at three. [HL 6] The loop tests whether n is greater than zero. [HL 7] It prints the value. [HL 8] Then n minus minus lowers n by one. "
                "[TRACK n=2] Now n is two, and the loop tests again. When n reaches zero, the test is false. [HL 10] The program prints Liftoff."),
    ill=dict(label="Round by round", on="a table of the rounds with the variable values",
             data=table(["Round", "n at the test", "Test", "Output"], [["1", "3", "true", "3"], ["2", "2", "true", "2"], ["3", "1", "true", "1"], ["4", "0", "false", "(loop ends)"]]),
             narr="Here are the rounds. In round one, n is three and the test is true. In rounds two and three, the same happens. "
                  "In round four, n is zero. The test is false, so the loop ends. Three rounds ran."),
    B=dict(file="total.cpp", label="A running total", on="a loop adds the numbers one to five",
           src='''
#include <iostream>
using namespace std;

int main() {
    int i = 1;
    int sum = 0;
    while (i <= 5) {
        sum += i;
        i++;
    }
    cout << "Sum: " << sum << endl;
    return 0;
}
''',
           narr="[HL 5] The counter i starts at one. [HL 6] The sum starts at zero. [HL 7] The loop runs while i is at most five. "
                "[HL 8] Each round adds i to the sum. [TRACK sum=3] After two rounds the sum is three. [HL 9] Then i goes up by one. [HL 11] At the end, the sum is fifteen."),
    term="The program prints Sum colon fifteen.",
    recap=["A while loop repeats while its test is true.", "The test runs before every round.",
           "Change the loop variable inside the body.", "Check the first and the last round, to avoid off-by-one errors."],
    bug=dict(title="An off-by-one error", file="total.cpp", kind="output", wrong_note="the test uses less than, not less than or equal",
             wrong='''
#include <iostream>
using namespace std;

int main() {
    int i = 1;
    int sum = 0;
    while (i < 5) {
        sum += i;
        i++;
    }
    cout << "Sum: " << sum << endl;
    return 0;
}
''', fixed_note="the test uses less than or equal",
             fixed='''
#include <iostream>
using namespace std;

int main() {
    int i = 1;
    int sum = 0;
    while (i <= 5) {
        sum += i;
        i++;
    }
    cout << "Sum: " << sum << endl;
    return 0;
}
''',
             why="With less than five, the loop stops before it adds five. The sum is ten, not fifteen.",
             narr="Bug of the Day. We want the sum of one to five. The program prints ten. The test says less than five, so the loop stops before it adds five. "
                  "This is an off-by-one error. Check the first round and the last round by hand. Use less than or equal."),
    pun="Why did the loop go to the doctor? It had a problem with its condition, and it kept coming back.",
    task="print a table of two", challenge="Use a while loop to print the table of two, from two times one to two times ten.",
    answer="Start i at one. While i is at most ten, print two times i, and then add one to i.",
))

EPISODES.append(dict(
    n=17, title="for loops", spoken="for loops", yt="C++ for Loop: Count with Confidence",
    thumb="FOR LOOP", vis="a counter with a start, a stop and a step",
    goals=["write the three parts of a for loop", "count up and down", "spot an empty loop body"],
    tags=["c++ for loop", "loop counter", "for loop syntax", "empty body"],
    analogy="a bus route: start at the first stop, check each stop, move to the next",
    c_pts=["Start, test and step live in one line", "The body runs once per round", "The loop variable belongs to the loop"],
    hook="One line holds the whole loop: start, test and step.",
    intro="Today we meet the for loop. It packs the start, the test and the step into one tidy line.",
    concept="A for loop has three parts in its round brackets. First, the start. It runs once. Second, the test. It runs before each round. Third, the step. It runs after each round.\n"
            "A variable made in the start belongs only to the loop. Think of a bus route. You begin at the first stop, check if there is a next stop, and move on.",
    A=dict(file="rounds.cpp", label="Count the rounds", on="a for loop prints five rounds",
           src='''
#include <iostream>
using namespace std;

int main() {
    for (int i = 1; i <= 5; i++) {
        cout << "Round " << i << endl;
    }
    return 0;
}
''',
           narr="[HL 5] The start makes i equal to one. The test checks that i is at most five. The step adds one to i. "
                "[HL 6] The body prints the round number. [TRACK i=1] Round one prints one. [TRACK i=2] Then i becomes two, and the body runs again. "
                "[TRACK i=6] When i is six, the test fails, and the loop ends."),
    ill=dict(label="Three parts, one loop", on="a flow: start, test, body, step",
             data=flow([("Start", "int i = 1 (once)"), ("Test", "i <= 5 ?"), ("Body", "print Round i"), ("Step", "i++ then test again")]),
             narr="Here is the order. The start runs once. Then the test runs. If it is true, the body runs, and then the step runs. "
                  "After the step, the test runs again. This repeats until the test is false."),
    B=dict(file="tableseven.cpp", label="Table of seven", on="a for loop prints seven times one to five",
           src='''
#include <iostream>
using namespace std;

int main() {
    for (int i = 1; i <= 5; i++) {
        cout << "7 x " << i << " = " << 7 * i << endl;
    }
    for (int k = 3; k >= 1; k--) {
        cout << k << " ";
    }
    cout << endl;
    return 0;
}
''',
           narr="[HL 6] The body prints one row of the table. The loop makes five rows. [HL 8] A second loop counts down. It starts at three. "
                "The step is k minus minus. [HL 9] It prints three, two and one. [HL 11] Then endl ends the line."),
    term="The table of seven prints five rows. Then the line, three two one, appears.",
    recap=["A for loop holds the start, the test and the step in one line.", "The start runs once, and the step runs after each round.",
           "Count down with minus minus.", "Never put a semicolon after the closing round bracket."],
    bug=dict(title="A semicolon after the for", file="rounds.cpp", kind="warn", wrong_note="a semicolon sits after the for line",
             wrong='''
#include <iostream>
using namespace std;

int main() {
    for (int i = 1; i <= 5; i++);
    {
        cout << "Round" << endl;
    }
    return 0;
}
''', fixed_note="the semicolon is gone",
             fixed='''
#include <iostream>
using namespace std;

int main() {
    for (int i = 1; i <= 5; i++) {
        cout << "Round" << endl;
    }
    return 0;
}
''',
             why="The semicolon is an empty loop body. The loop runs five times and does nothing. The block below then runs once.",
             narr="Bug of the Day. A semicolon sits after the for line. That is an empty body. The loop spins five times and does nothing. "
                  "Then the block runs only once. The compiler warns about the empty body. Remove the semicolon."),
    pun="Why do for loops make good friends? They always count on you.",
    task="print a triangle of numbers", challenge="Use a for loop to print the even numbers from two to twenty.",
    answer="Start i at two. Test i at most twenty. Step i by two, using i plus equals two.",
))

EPISODES.append(dict(
    n=18, title="Range-based for", spoken="range-based for loops", yt="C++ Range-Based for Loop",
    thumb="FOR EACH", vis="a crab picking up one shell at a time",
    goals=["loop over every item with a range-based for", "loop over the letters of a string", "change items with a reference"],
    tags=["range based for loop", "for each c++", "c++11 loops", "auto in for"],
    analogy="a teacher calling the roll: each name is called once, in order",
    c_pts=["Range-based for visits every item", "No counter is needed", "An ampersand lets you change the items"],
    hook="Visit every item without a counter.",
    intro="Today we loop without a counter. The range-based for visits every item for you, one at a time.",
    concept="A range-based for loop visits every item in a group. You do not need a counter, and you cannot go past the end.\n"
            "It works on strings, lists and many other groups. By default the loop variable is a copy. Add an ampersand to work on the real item. Think of a teacher calling the roll. Each name is called once, in order.",
    A=dict(file="foreach.cpp", label="Visit every item", on="a range-based for over letters and numbers",
           src='''
#include <iostream>
#include <string>
using namespace std;

int main() {
    string word = "Goa";
    for (char c : word) {
        cout << c << endl;
    }
    for (int n : {10, 20, 30}) {
        cout << n << endl;
    }
    return 0;
}
''',
           narr="[HL 6] Word holds Goa. [HL 7] The loop takes each letter in turn and puts it in c. [TRACK c=G] First c is G. [TRACK c=o] Then o. [TRACK c=a] Then a. "
                "[HL 10] This loop visits the numbers ten, twenty and thirty. [HL 11] It prints each one."),
    ill=dict(label="Round by round", on="a table: round, the item and the action",
             data=table(["Round", "Item", "Action"], [["1", "G", "print G"], ["2", "o", "print o"], ["3", "a", "print a"], ["End", "none left", "loop ends"]]),
             narr="Here is the loop over Goa. In each round, the loop gives us the next letter. After the last letter, no items remain. The loop ends by itself. "
                  "You never write a test or a step."),
    B=dict(file="vowels.cpp", label="Count the vowels", on="a range-based for counts vowels in a word",
           src='''
#include <iostream>
#include <string>
using namespace std;

int main() {
    string word = "Konkani";
    int vowels = 0;
    for (char c : word) {
        if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') {
            vowels++;
        }
    }
    cout << "Vowels: " << vowels << endl;
    return 0;
}
''',
           narr="[HL 6] Word holds Konkani. [HL 7] The count starts at zero. [HL 8] The loop visits each letter. [HL 9] An if tests the letter against five vowels. "
                "[HL 10] A vowel adds one to the count. [TRACK vowels=3] The word Konkani has three vowels, which are o, a and i. [HL 13] The program prints the count."),
    term="The program prints Vowels colon three.",
    recap=["A range-based for visits every item.", "You need no counter and no test.",
           "By default the loop variable is a copy.", "Add an ampersand to change the real item."],
    bug=dict(title="Changing a copy", file="shout.cpp", kind="output", wrong_note="the loop variable is a copy",
             wrong='''
#include <cctype>
#include <iostream>
#include <string>
using namespace std;

int main() {
    string word = "goa";
    for (char c : word) {
        c = toupper(c);
    }
    cout << word << endl;
    return 0;
}
''', fixed_note="the loop variable is a reference",
             fixed='''
#include <cctype>
#include <iostream>
#include <string>
using namespace std;

int main() {
    string word = "goa";
    for (char& c : word) {
        c = toupper(c);
    }
    cout << word << endl;
    return 0;
}
''',
             why="Without the ampersand, c is a copy of each letter. The code changes the copy, and the real string stays the same.",
             narr="Bug of the Day. We try to change goa into capital letters. But the program prints goa again. The loop variable c is a copy. "
                  "We change the copy and not the string. Add an ampersand after char. Then c is a nickname for the real letter."),
    pun="I wrote a for-each loop for my fish. Now every fish gets visited exactly once.",
    task="count the letter a", challenge="Read a word. Use a range-based for to count how many times the letter a appears.",
    answer="Read the word into a string. Loop over each char. If the char is the letter a, add one to a counter.",
))

EPISODES.append(dict(
    n=19, title="break and continue", spoken="break and continue", yt="C++ break and continue in Loops",
    thumb="BREAK / CONTINUE", vis="a stop sign and a skip sign",
    goals=["leave a loop with break", "skip a round with continue", "tell break and continue apart"],
    tags=["break continue c++", "loop control", "exit a loop", "skip iteration"],
    analogy="a school bus: break means the bus stops for good, continue means skip one stop",
    c_pts=["Break leaves the loop at once", "Continue skips to the next round", "Both work in while and for loops"],
    hook="Break stops a loop. Continue only skips one round.",
    intro="Today we take control of loops. Break stops the loop. Continue skips one round.",
    concept="Break leaves the loop at once. The program continues after the loop. Continue skips the rest of this round, and goes to the next round.\n"
            "Both keywords work in while loops and for loops. Think of a school bus. Break means the bus stops for good. Continue means the bus skips one stop.",
    A=dict(file="stopat.cpp", label="Stop at the first match", on="break leaves the loop at the first multiple of seven",
           src='''
#include <iostream>
using namespace std;

int main() {
    for (int i = 10; i <= 30; i++) {
        if (i % 7 == 0) {
            cout << "Found " << i << endl;
            break;
        }
    }
    cout << "Done" << endl;
    return 0;
}
''',
           narr="[HL 5] The loop counts from ten to thirty. [HL 6] The test checks if i divides evenly by seven. [HL 7] At fourteen, the test is true. The program prints Found fourteen. "
                "[HL 8] Break leaves the loop at once. Fifteen and the rest never run. [HL 11] The program continues after the loop and prints Done."),
    ill=dict(label="Break and continue", on="a table that compares break and continue",
             data=table(["Keyword", "What it does", "Next step"], [["break", "Leaves the loop", "Code after the loop"], ["continue", "Skips this round", "Next round of the loop"]]),
             narr="The table shows the difference. Break ends the loop. The next step is the code after the loop. "
                  "Continue only ends the current round. The next step is the next round of the same loop."),
    B=dict(file="skip.cpp", label="Skip one number", on="continue skips the number three",
           src='''
#include <iostream>
using namespace std;

int main() {
    for (int i = 1; i <= 5; i++) {
        if (i == 3) {
            continue;
        }
        cout << i << " ";
    }
    cout << endl;
    return 0;
}
''',
           narr="[HL 5] The loop counts from one to five. [HL 6] When i is three, the test is true. [HL 7] Continue skips the rest of this round. The print does not run. "
                "[HL 9] For the other numbers, the print runs. The output is one, two, four, five."),
    term="The program prints one two four five. The number three is missing.",
    recap=["Break leaves the loop at once.", "Continue skips to the next round.",
           "Code after the loop still runs after a break.", "Use them with a clear if test."],
    bug=dict(title="Break instead of continue", file="skip.cpp", kind="output", wrong_note="the code uses break to skip a number",
             wrong='''
#include <iostream>
using namespace std;

int main() {
    for (int i = 1; i <= 5; i++) {
        if (i == 3) {
            break;
        }
        cout << i << " ";
    }
    cout << endl;
    return 0;
}
''', fixed_note="the code uses continue",
             fixed='''
#include <iostream>
using namespace std;

int main() {
    for (int i = 1; i <= 5; i++) {
        if (i == 3) {
            continue;
        }
        cout << i << " ";
    }
    cout << endl;
    return 0;
}
''',
             why="Break ends the whole loop, so four and five never print. Continue skips only the round for three.",
             narr="Bug of the Day. We want to skip the number three. The program prints one and two, and then stops. We used break. Break ends the whole loop. "
                  "To skip only one round, use continue."),
    pun="Break and continue had an argument. Break left. Continue just kept going.",
    task="skip the multiples of three", challenge="Print the numbers from one to twenty. Skip every multiple of three.",
    answer="Use a for loop from one to twenty. If i remainder three equals zero, call continue. Otherwise print i.",
))

EPISODES.append(dict(
    n=20, title="Nested loops and patterns", spoken="nested loops and patterns", yt="C++ Nested Loops: Star Patterns and Tables",
    thumb="STAR PATTERNS", vis="a triangle made of stars",
    goals=["put one loop inside another", "print a star triangle", "print a grid of numbers"],
    tags=["nested loops c++", "star pattern", "pattern printing", "multiplication table"],
    analogy="a clock: the minute hand loops many times for each step of the hour hand",
    c_pts=["The inner loop runs fully for each outer round", "Rows use the outer loop", "Columns use the inner loop"],
    hook="A loop inside a loop draws pictures.",
    intro="Today we put a loop inside a loop. With it, you can print triangles, grids and tables.",
    concept="A nested loop is a loop inside another loop. For each round of the outer loop, the inner loop runs from start to finish.\n"
            "We use the outer loop for rows, and the inner loop for columns. Think of a clock. The minute hand goes all the way round for every small step of the hour hand.",
    A=dict(file="triangle.cpp", label="A star triangle", on="two loops print a triangle of stars",
           src='''
#include <iostream>
using namespace std;

int main() {
    for (int row = 1; row <= 4; row++) {
        for (int star = 1; star <= row; star++) {
            cout << "*";
        }
        cout << endl;
    }
    return 0;
}
''',
           narr="[HL 5] The outer loop counts the rows, from one to four. [HL 6] The inner loop prints one star for each count up to the row number. "
                "[HL 7] Row one prints one star. Row two prints two stars. [HL 9] After each row, endl moves to the next line. The result is a triangle."),
    ill=dict(label="Rows and stars", on="a table: row number and the stars printed",
             data=table(["Row", "Inner rounds", "Printed"], [["1", "1", "*"], ["2", "2", "**"], ["3", "3", "***"], ["4", "4", "****"]]),
             narr="Here is each row. The inner loop runs as many times as the row number. That is one star in row one, and four stars in row four. "
                  "The line break comes after the inner loop ends."),
    B=dict(file="grid.cpp", label="A number grid", on="a three by three table of products",
           src='''
#include <iostream>
using namespace std;

int main() {
    for (int r = 1; r <= 3; r++) {
        for (int c = 1; c <= 3; c++) {
            cout << r * c << " ";
        }
        cout << endl;
    }
    return 0;
}
''',
           narr="[HL 5] The outer loop gives the row r. [HL 6] The inner loop gives the column c. [HL 7] Each cell shows r times c. "
                "[TRACK r=2] In row two, the cells are two, four and six. [HL 9] The line break ends each row."),
    term="The program prints a grid with three rows. The last row shows three, six and nine.",
    recap=["A nested loop is a loop inside a loop.", "The inner loop runs fully for each round of the outer loop.",
           "Use the outer loop for rows and the inner loop for columns.", "Print the line break after the inner loop."],
    bug=dict(title="A missing line break", file="triangle.cpp", kind="output", wrong_note="endl is missing after the inner loop",
             wrong='''
#include <iostream>
using namespace std;

int main() {
    for (int row = 1; row <= 4; row++) {
        for (int star = 1; star <= row; star++) {
            cout << "*";
        }
    }
    cout << endl;
    return 0;
}
''', fixed_note="endl is inside the outer loop",
             fixed='''
#include <iostream>
using namespace std;

int main() {
    for (int row = 1; row <= 4; row++) {
        for (int star = 1; star <= row; star++) {
            cout << "*";
        }
        cout << endl;
    }
    return 0;
}
''',
             why="The line break sits after both loops, so all ten stars go on one line. It must run once per row, inside the outer loop.",
             narr="Bug of the Day. We want a triangle. The program prints ten stars in one long line. The line break is after both loops. "
                  "It runs only once. Move endl inside the outer loop, after the inner loop. Then each row gets its own line."),
    pun="I printed a triangle of stars. It was a very sharp piece of code.",
    task="print a number triangle", challenge="Print a triangle of numbers. Row one prints the number one. Row two prints the number two, two times. Go up to row four.",
    answer="Use two loops. In the inner loop, print the row number instead of a star. Print endl after the inner loop.",
))
