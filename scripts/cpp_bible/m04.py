"""Module 4 — Arrays, vectors, strings, searching and sorting (EP 31-40)."""
from lib import flow, mem, table, trace

MODULE = {"id": 4, "name": "Arrays, vectors and sorting", "range": "31–40", "colours": "Butter + Dark blue", "bg": "butter"}
NEXT_AFTER = ("Next: EP 41 · Memory and addresses", "We end module four here. Next time: memory and addresses, the start of pointers.")
EPISODES = []

EPISODES.append(dict(
    n=31, title="Arrays", spoken="arrays", yt="C++ Arrays: Store Many Values in One Variable",
    thumb="ARRAYS", vis="a row of five numbered lockers",
    goals=["make an array with a starting list", "read and change items by index", "stay inside the array size"],
    tags=["c++ arrays", "array index", "array initialization", "too many initializers"],
    analogy="a row of lockers: one name on the row, one number on each door",
    c_pts=["An array holds many values of one type", "The size is fixed", "Indexes start at zero"],
    hook="One name, five boxes, side by side.",
    intro="Today we store many values under one name. An array is a row of boxes, side by side in memory.",
    concept="An array holds many values of the same type. You choose the size when you make it, and the size never changes. Each item has an index. The first index is zero.\n"
            "The items sit side by side in memory. Think of a row of lockers. The row has one name, and each door has its own number.",
    A=dict(file="marks.cpp", label="Five marks", on="an array of five marks, read by index",
           src='''
#include <iostream>
using namespace std;

int main() {
    int marks[5] = {72, 85, 64, 90, 58};
    cout << marks[0] << endl;
    cout << marks[4] << endl;
    marks[2] = 70;
    cout << marks[2] << endl;
    return 0;
}
''',
           narr="[HL: int marks[5]] The number in square brackets is the size. The list in braces gives the starting values. [HL: marks[0]] Index zero is the first item. It prints seventy-two. "
                "[HL: marks[4]] Index four is the last item. It prints fifty-eight. There is no index five. [HL: marks[2] = 70] We can change one item by its index. [HL: cout << marks[2]] Now the third item prints seventy."),
    ill=dict(label="Boxes side by side", on="five int boxes in a row, each with an address four bytes after the last",
             data=mem([("marks", "int[5]", "72, 85, 64, 90, 58")], caption="The addresses grow by four bytes, the size of an int"),
             narr="Look at the memory. Each box holds one mark. Each box is four bytes wide. So the addresses grow by four each time. "
                  "The computer finds any item by a simple sum. It takes the start address and adds the index times four."),
    B=dict(file="sumall.cpp", label="Add them up", on="a loop adds all five marks",
           src='''
#include <iostream>
using namespace std;

int main() {
    int marks[5] = {72, 85, 64, 90, 58};
    int sum = 0;
    for (int i = 0; i < 5; i++) {
        sum += marks[i];
    }
    cout << "Sum: " << sum << endl;
    return 0;
}
''',
           narr="[HL: int sum] The sum starts at zero. [HL: for (int i] The loop runs with i from zero up to four. The test says less than five, so five is never used. "
                "[HL: sum += marks[i]] Each round adds one item to the sum. [TRACK sum=72] After round one the sum is seventy-two. [HL: cout << \"Sum] At the end, the sum is three hundred and sixty-nine."),
    term="The program prints Sum colon three hundred sixty-nine.",
    recap=["An array holds many values of one type.", "The size is fixed when you make the array.",
           "Indexes start at zero, and the last index is size minus one.", "The items sit side by side in memory."],
    bug=dict(title="Too many starting values", file="marks.cpp", kind="compile", wrong_note="four values for three boxes",
             wrong='''
#include <iostream>
using namespace std;

int main() {
    int marks[3] = {72, 85, 64, 90};
    cout << marks[0] << endl;
    return 0;
}
''', fixed_note="the array has four boxes",
             fixed='''
#include <iostream>
using namespace std;

int main() {
    int marks[4] = {72, 85, 64, 90};
    cout << marks[0] << endl;
    return 0;
}
''',
             why="The size says three boxes, but the list has four values. The compiler stops, because the fourth value has no box.",
             narr="Bug of the Day. The array has three boxes, but the list has four values. The compiler says too many initializers. "
                  "The fourth value has no box to go in. Make the size four, or remove one value."),
    pun="I asked my array how it feels. It said, I am fine, but I count from zero.",
    task="store and print five numbers", challenge="Make an array of five temperatures. Print the first one and the last one.",
    answer="Write int temps with five values in braces. Print temps at index zero and temps at index four.",
))

EPISODES.append(dict(
    n=32, title="Looping over arrays", spoken="looping over arrays", yt="C++ Loop Over an Array: Sum, Maximum and Reverse",
    thumb="LOOP + ARRAY", vis="a crab walking along a row of boxes",
    goals=["visit every item with a loop", "find the biggest item", "start a maximum with the first item"],
    tags=["array loop c++", "find maximum", "range based for array", "reverse array"],
    analogy="a teacher checking each bench in a classroom, one by one",
    c_pts=["A for loop visits each index", "A range-based for visits each value", "Start the maximum with the first item"],
    hook="Never start a maximum at zero.",
    intro="Today we walk along an array. We find the biggest value, and we print the array backwards.",
    concept="A for loop with an index lets you read and change items. A range-based for loop is shorter, but it gives only the values.\n"
            "To find the biggest item, keep a variable called best. Compare every item with it. Think of a teacher who checks every bench in a classroom, one by one.",
    A=dict(file="biggest.cpp", label="Find the biggest", on="a loop keeps the biggest value so far",
           src='''
#include <iostream>
using namespace std;

int main() {
    int marks[5] = {72, 85, 64, 90, 58};
    int best = marks[0];
    for (int m : marks) {
        if (m > best) {
            best = m;
        }
    }
    cout << "Best: " << best << endl;
    return 0;
}
''',
           narr="[HL: int best] Best starts as the first item, seventy-two. [HL: for (int m] The range-based for gives each value in turn. [HL: if (m > best)] If the value is bigger than best, [HL: best = m] it becomes the new best. "
                "[TRACK best=85] Eighty-five replaces seventy-two. [TRACK best=90] Then ninety replaces eighty-five. [HL: cout << \"Best] The final answer is ninety."),
    ill=dict(label="Best so far", on="a table of the rounds: the value and the best so far",
             data=table(["Round", "Value m", "Best before", "Best after"], [["1", "72", "72", "72"], ["2", "85", "72", "85"], ["3", "64", "85", "85"], ["4", "90", "85", "90"], ["5", "58", "90", "90"]]),
             narr="The table shows each round. Best changes in round two and in round four. In the other rounds, the value is smaller, so best stays. "
                  "At the end, best holds the biggest value."),
    B=dict(file="backwards.cpp", label="Print backwards", on="a loop counts down from the last index",
           src='''
#include <iostream>
using namespace std;

int main() {
    int marks[5] = {72, 85, 64, 90, 58};
    for (int i = 4; i >= 0; i--) {
        cout << marks[i] << " ";
    }
    cout << endl;
    return 0;
}
''',
           narr="[HL: for (int i = 4] The loop starts at the last index, four. [HL: i >= 0] It runs while i is zero or more. [HL: i--] The step lowers i by one. "
                "[HL: cout << marks[i]] Each round prints one item. The output is fifty-eight, ninety, sixty-four, eighty-five, seventy-two."),
    term="The program prints the marks in reverse order.",
    recap=["A for loop with an index can read and change items.", "A range-based for loop gives each value.",
           "Start best with the first item.", "Count down from size minus one to go backwards."],
    bug=dict(title="A maximum that starts at zero", file="coldest.cpp", kind="output", wrong_note="best starts at zero",
             wrong='''
#include <iostream>
using namespace std;

int main() {
    int temps[3] = {-5, -2, -9};
    int best = 0;
    for (int t : temps) {
        if (t > best) {
            best = t;
        }
    }
    cout << "Warmest: " << best << endl;
    return 0;
}
''', fixed_note="best starts with the first item",
             fixed='''
#include <iostream>
using namespace std;

int main() {
    int temps[3] = {-5, -2, -9};
    int best = temps[0];
    for (int t : temps) {
        if (t > best) {
            best = t;
        }
    }
    cout << "Warmest: " << best << endl;
    return 0;
}
''',
             why="Every temperature is below zero, so none is bigger than the starting best of zero. Start with a real item from the array.",
             narr="Bug of the Day. All temperatures are below zero. The program prints zero as the warmest. But zero is not in the array. "
                  "Best started at zero, and no item beat it. Start best with the first item of the array."),
    pun="I asked the array who the biggest item is. It said, I will let you compare.",
    task="find the smallest value", challenge="Write a loop that finds the smallest mark in an array of five marks.",
    answer="Start small with the first item. In the loop, if an item is less than small, store it in small.",
))

EPISODES.append(dict(
    n=33, title="Two-dimensional arrays", spoken="two-dimensional arrays", yt="C++ 2D Arrays: Rows and Columns",
    thumb="2D ARRAYS", vis="a cinema seat plan with rows and columns",
    goals=["make a table with rows and columns", "read an item with two indexes", "loop over a grid"],
    tags=["2d array c++", "multidimensional array", "matrix c++", "nested loop array"],
    analogy="a cinema seat plan: you need a row and a seat number",
    c_pts=["A 2D array is an array of rows", "Two indexes: row first, then column", "Use nested loops to visit every cell"],
    hook="Rows and columns, in two lines of code.",
    intro="Today we make a table. A two-dimensional array has rows and columns, like a cinema seat plan.",
    concept="A two-dimensional array is an array of rows. Each row is an array of columns. You need two indexes. The first is the row, and the second is the column.\n"
            "In memory, the rows sit one after another. Think of a cinema seat plan. To find your seat, you need a row and a seat number.",
    A=dict(file="seats.cpp", label="A small grid", on="a grid with two rows and three columns",
           src='''
#include <iostream>
using namespace std;

int main() {
    int grid[2][3] = {{1, 2, 3}, {4, 5, 6}};
    cout << grid[0][2] << endl;
    cout << grid[1][0] << endl;
    return 0;
}
''',
           narr="[HL: int grid[2][3]] Two rows and three columns. Each inner pair of braces is one row. [HL: grid[0][2]] Row zero, column two is the number three. [HL: grid[1][0]] Row one, column zero is the number four."),
    ill=dict(label="Rows in memory", on="six int boxes in a row: row zero first, then row one",
             data=mem([("grid", "int[6]", "1, 2, 3, 4, 5, 6")], caption="Row zero holds the first three boxes. Row one holds the next three"),
             narr="In memory, the grid is one long row of six boxes. Row zero is the first three. Row one is the next three. "
                  "The computer finds a cell with the sum row times three plus column."),
    B=dict(file="rowsum.cpp", label="Sum each row", on="nested loops add each row",
           src='''
#include <iostream>
using namespace std;

int main() {
    int grid[2][3] = {{1, 2, 3}, {4, 5, 6}};
    for (int r = 0; r < 2; r++) {
        int sum = 0;
        for (int c = 0; c < 3; c++) {
            sum += grid[r][c];
        }
        cout << "Row " << r << ": " << sum << endl;
    }
    return 0;
}
''',
           narr="[HL: for (int r] The outer loop picks the row. [HL: int sum] Each row starts with a new sum of zero. [HL: for (int c] The inner loop visits the three columns. "
                "[HL: sum += grid] Each cell is added to the sum. [HL: cout << \"Row] Row zero sums to six. Row one sums to fifteen."),
    term="The program prints Row zero colon six, and Row one colon fifteen.",
    recap=["A two-dimensional array has rows and columns.", "Use the row index first, then the column index.",
           "Nested loops visit every cell.", "Only the first size may be left out."],
    bug=dict(title="A missing column size", file="seats.cpp", kind="compile", wrong_note="both sizes are empty",
             wrong='''
#include <iostream>
using namespace std;

int main() {
    int grid[][] = {{1, 2}, {3, 4}};
    cout << grid[0][1] << endl;
    return 0;
}
''', fixed_note="the column size is written",
             fixed='''
#include <iostream>
using namespace std;

int main() {
    int grid[][2] = {{1, 2}, {3, 4}};
    cout << grid[0][1] << endl;
    return 0;
}
''',
             why="The compiler can count the rows from your list. It needs the column size to find the start of each row.",
             narr="Bug of the Day. Both sizes are empty. The compiler says multidimensional array must have bounds for all dimensions except the first. "
                  "It can count the rows from your list. But it needs the column size. Write the number two in the second brackets."),
    pun="I made a grid of jokes. Every row had a punchline, and every column had a groan.",
    task="print a multiplication grid", challenge="Make a two by two grid with the numbers one, two, three and four. Print the diagonal: row zero column zero, and row one column one.",
    answer="Use int grid with two by two braces. Print grid at zero zero, which is one, and grid at one one, which is four.",
))

EPISODES.append(dict(
    n=34, title="std::array", spoken="std array", yt="C++ std::array: A Safer Array",
    thumb="STD::ARRAY", vis="an array with a safety helmet",
    goals=["make a std array", "use size and at", "read an out-of-range error"],
    tags=["std::array", "c++ array at", "out_of_range", "safe array"],
    analogy="a locker row with a guard: ask for door nine, and the guard says no such door",
    c_pts=["std array knows its own size", "at checks the index", "It costs nothing extra"],
    hook="An array that knows its own size.",
    intro="Today we meet std array. It is a normal array with a safety helmet. It knows its size, and it can check your index.",
    concept="The std array type wraps a plain array. It knows its own size. The size function tells you. The at function checks the index. If the index is wrong, it stops with an error.\n"
            "A plain array does not check anything, and a wrong index gives garbage. Think of a locker row with a guard. If you ask for door nine, the guard says there is no such door.",
    A=dict(file="stdarray.cpp", label="A std array", on="size, at and fill on a std array",
           src='''
#include <array>
#include <iostream>
using namespace std;

int main() {
    array<int, 3> a = {5, 6, 7};
    cout << a.size() << endl;
    cout << a.at(1) << endl;
    a.fill(0);
    cout << a[2] << endl;
    return 0;
}
''',
           narr="[HL: #include <array>] The array header gives us std array. [HL: array<int, 3> a] The type and the size go in angle brackets. [HL: a.size()] The size is three. [HL: a.at(1)] At one gives the second item, which is six. "
                "[HL: a.fill(0)] The fill function sets every item to zero. [HL: a[2]] So the last item is now zero."),
    ill=dict(label="Plain array or std::array", on="a table that compares the two",
             data=table(["Feature", "int a[3]", "std::array<int, 3>"], [["Knows its size", "no", "yes, a.size()"], ["Checks the index", "no", "yes, with at()"], ["Can be copied", "no", "yes"], ["Extra cost", "none", "none"]]),
             narr="Here are the two types side by side. The std array knows its size. It can check an index with at. You can copy it with a single equals sign. "
                  "And it costs no more memory than a plain array."),
    B=dict(file="same.cpp", label="Compare and copy", on="two std arrays compared with two equals signs",
           src='''
#include <array>
#include <iostream>
using namespace std;

int main() {
    array<int, 3> a = {1, 2, 3};
    array<int, 3> b = a;
    b[0] = 9;
    cout << boolalpha << (a == b) << endl;
    cout << a[0] << " " << b[0] << endl;
    return 0;
}
''',
           narr="[HL: array<int, 3> b = a] This line copies the whole array. A plain array cannot do this. [HL: b[0] = 9] We change the first item of b only. "
                "[HL: a == b] Two equals signs compare all items. The arrays differ now, so the answer is false. [HL: cout << a[0]] The original a still starts with one, and b starts with nine."),
    term="The program prints false, and then one and nine.",
    recap=["Std array wraps a plain array.", "It knows its own size.",
           "At checks the index and stops on a wrong one.", "You can copy and compare two std arrays."],
    bug=dict(title="An index that is too big", file="stdarray.cpp", kind="runtime", wrong_note="at is called with index five",
             wrong='''
#include <array>
#include <iostream>
using namespace std;

int main() {
    array<int, 3> a = {5, 6, 7};
    cout << a.at(5) << endl;
    return 0;
}
''', fixed_note="the index is checked first",
             fixed='''
#include <array>
#include <iostream>
using namespace std;

int main() {
    array<int, 3> a = {5, 6, 7};
    size_t i = 5;
    if (i < a.size()) {
        cout << a.at(i) << endl;
    } else {
        cout << "No such index" << endl;
    }
    return 0;
}
''',
             why="The array has three items, so the valid indexes are zero, one and two. At stops the program with an exception instead of reading garbage.",
             narr="Bug of the Day. The array has three items, and we ask for index five. At stops the program. It says terminate called after throwing an instance of out of range. "
                  "That is better than reading garbage. Check the index against the size before you use it."),
    pun="Std array put on a helmet. Now it has a safe place to fall.",
    task="fill and print a std array", challenge="Make a std array of four ints. Fill it with the number seven. Print every item with a range-based for.",
    answer="Write array of int, four. Call fill with seven. Then use for int x colon the array, and print x.",
))

EPISODES.append(dict(
    n=35, title="std::vector", spoken="std vector", yt="C++ std::vector: The Array That Grows",
    thumb="VECTOR!", vis="a stretchy shelf that grows with every box",
    goals=["make a vector and add items with push_back", "read the size and the items", "loop over a vector"],
    tags=["std::vector", "c++ vector", "push_back", "dynamic array"],
    analogy="a stretchy bag: it grows when you add more shopping",
    c_pts=["A vector grows and shrinks", "push_back adds an item at the end", "It manages its own memory"],
    hook="The array that grows when you need it.",
    intro="Today we meet the most useful container in C plus plus. A vector grows when you add items.",
    concept="A vector is an array that can grow and shrink. Push back adds an item at the end. The size function tells you how many items it holds.\n"
            "A vector looks after its own memory. You never write new or delete. Think of a stretchy shopping bag. It grows when you add more shopping.",
    A=dict(file="vec.cpp", label="Grow a vector", on="push_back adds items one by one",
           src='''
#include <iostream>
#include <vector>
using namespace std;

int main() {
    vector<int> v;
    v.push_back(10);
    v.push_back(20);
    v.push_back(30);
    cout << v.size() << endl;
    cout << v[1] << endl;
    return 0;
}
''',
           narr="[HL: #include <vector>] The vector header gives us the vector type. [HL: vector<int> v] The type goes in angle brackets. This vector is empty. [HL: v.push_back(10)] Push back adds ten at the end. "
                "[HL: v.push_back(30)] Two more pushes add twenty and thirty. [HL: v.size()] The size is three. [HL: v[1]] Index one is twenty."),
    ill=dict(label="A vector in memory", on="the vector object on the stack points to its items on the heap",
             data=mem([("v", "std::vector<int>", None, "stack"), ("items", "int[3]", "10, 20, 30", "heap")], arrows=[("v", "items[0]", "points to the first item")],
                      caption="The small vector object lives on the stack. The items live on the heap"),
             narr="The vector has two parts. The small vector object lives on the stack. The items live on the heap. The object points to the first item. "
                  "When you push back more items, the vector asks for a bigger block and moves the items."),
    B=dict(file="veclist.cpp", label="Start with a list", on="a vector made from a list, then a loop",
           src='''
#include <iostream>
#include <vector>
using namespace std;

int main() {
    vector<int> v = {4, 8, 15};
    v.push_back(16);
    for (int x : v) {
        cout << x << " ";
    }
    cout << endl;
    cout << v.back() << endl;
    v.pop_back();
    cout << v.size() << endl;
    return 0;
}
''',
           narr="[HL: vector<int> v = {4, 8, 15}] A vector can start with a list of values. [HL: v.push_back(16)] Push back adds sixteen at the end. [HL: for (int x : v)] A range-based for visits every item. "
                "[HL: v.back()] Back gives the last item, which is sixteen. [HL: v.pop_back()] Pop back removes the last item. [HL: cout << v.size()] Now the size is three."),
    term="The program prints the four numbers, then sixteen, then three.",
    recap=["A vector grows and shrinks.", "Push back adds an item at the end.",
           "Size tells you how many items it holds.", "A vector looks after its own memory."],
    bug=dict(title="A missing vector header", file="vec.cpp", kind="compile", wrong_note="the vector include line is missing",
             wrong='''
#include <iostream>
using namespace std;

int main() {
    vector<int> v;
    v.push_back(10);
    cout << v.size() << endl;
    return 0;
}
''', fixed_note="the vector header is back",
             fixed='''
#include <iostream>
#include <vector>
using namespace std;

int main() {
    vector<int> v;
    v.push_back(10);
    cout << v.size() << endl;
    return 0;
}
''',
             why="The vector type lives in its own header. Without the include line, the compiler has never heard of vector.",
             narr="Bug of the Day. The program uses vector, but there is no include line for it. The compiler says vector was not declared in this scope. "
                  "It suggests the header in a note. Add the include line for vector at the top."),
    pun="My vector told me it needs space. I said, you can grow, I believe in you.",
    task="collect numbers in a vector", challenge="Use a vector. Push back the numbers from one to five, then print their sum.",
    answer="Use a for loop with push back for each number. Then use a range-based for to add them. The sum is fifteen.",
))

EPISODES.append(dict(
    n=36, title="Vector operations", spoken="vector operations", yt="C++ Vector: insert, erase, sort and find",
    thumb="VECTOR TOOLS", vis="a toolbox with insert, erase and sort labels",
    goals=["insert and erase items", "sort a vector", "find a value in a vector"],
    tags=["vector insert erase", "std::sort", "std::find", "c++ vector operations"],
    analogy="a train: you can add a coach in the middle, remove one, or re-order them",
    c_pts=["Insert and erase use iterators", "begin points to the first item", "Sort and find come from the algorithm header"],
    hook="Insert, erase, sort and find in a few lines.",
    intro="Today we use the vector toolbox. You will insert, erase, sort and search with only a few lines.",
    concept="A vector has many tools. Insert adds an item at a position. Erase removes an item at a position. Both use an iterator. The begin function gives an iterator to the first item.\n"
            "The algorithm header adds sort and find. Think of a train. You can add a coach in the middle, take one out, or put them in order.",
    A=dict(file="edit.cpp", label="Insert and erase", on="insert 99 at position one, then erase the first item",
           src='''
#include <iostream>
#include <vector>
using namespace std;

int main() {
    vector<int> v = {10, 20, 30};
    v.insert(v.begin() + 1, 99);
    v.erase(v.begin());
    for (int x : v) {
        cout << x << " ";
    }
    cout << endl;
    return 0;
}
''',
           narr="[HL: vector<int> v] The vector starts as ten, twenty, thirty. [HL: v.insert] Begin plus one is the second position. Insert puts ninety-nine there. [TRACK size=4] The vector is now ten, ninety-nine, twenty, thirty. "
                "[HL: v.erase] Erase removes the first item. [HL: for (int x : v)] The loop prints ninety-nine, twenty, thirty."),
    ill=dict(label="The vector after each call", on="a table: each call and the vector after it",
             data=table(["Call", "Vector after"], [["start", "10 20 30"], ["insert(begin + 1, 99)", "10 99 20 30"], ["erase(begin)", "99 20 30"], ["push_back(5)", "99 20 30 5"]]),
             narr="Follow the table. The start is ten, twenty, thirty. Insert adds ninety-nine at position one. Erase removes the first item. "
                  "Push back adds five at the end. Items move to make room, or to close the gap."),
    B=dict(file="sortfind.cpp", label="Sort and find", on="sort puts the values in order, find looks for one",
           src='''
#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

int main() {
    vector<int> v = {40, 10, 30, 20};
    sort(v.begin(), v.end());
    for (int x : v) {
        cout << x << " ";
    }
    cout << endl;
    auto it = find(v.begin(), v.end(), 30);
    cout << (it - v.begin()) << endl;
    return 0;
}
''',
           narr="[HL: sort(v.begin()] Sort takes the start and the end of the vector. It puts the items in order. [HL: for (int x : v)] The loop prints ten, twenty, thirty, forty. "
                "[HL: auto it] Find looks for thirty. It returns an iterator to the item. [HL: it - v.begin()] Subtracting begin gives the index. Thirty is at index two."),
    term="The program prints the sorted numbers, and then the index two.",
    recap=["Insert and erase need an iterator.", "Begin gives an iterator to the first item.",
           "Sort puts the items in order.", "Find returns an iterator to the match."],
    bug=dict(title="Erase with a number", file="edit.cpp", kind="compile", wrong_note="erase gets a plain number, not an iterator",
             wrong='''
#include <iostream>
#include <vector>
using namespace std;

int main() {
    vector<int> v = {10, 20, 30};
    v.erase(1);
    cout << v.size() << endl;
    return 0;
}
''', fixed_note="erase gets an iterator",
             fixed='''
#include <iostream>
#include <vector>
using namespace std;

int main() {
    vector<int> v = {10, 20, 30};
    v.erase(v.begin() + 1);
    cout << v.size() << endl;
    return 0;
}
''',
             why="Erase wants a position in the form of an iterator, not an index. Add the index to begin to make an iterator.",
             narr="Bug of the Day. We call erase with the plain number one. The compiler says no matching function for call to erase. "
                  "Erase wants an iterator, not an index. Write begin plus one, and the call works."),
    pun="I tried to find my lost sock in a sorted vector. It was at the end, as always.",
    task="sort and print", challenge="Make a vector with five numbers. Sort it, and print the smallest and the biggest.",
    answer="After sort, the smallest is v front, and the biggest is v back. Print both.",
))

EPISODES.append(dict(
    n=37, title="More string tools", spoken="more string tools", yt="C++ Strings: replace, erase, stoi and to_string",
    thumb="STRING TOOLS", vis="a pair of scissors and a glue stick",
    goals=["change a string with replace and erase", "turn text into a number with stoi", "turn a number into text with to_string"],
    tags=["stoi c++", "to_string", "string replace", "invalid_argument"],
    analogy="a tailor: cut a piece, stitch a new piece, measure the cloth",
    c_pts=["Replace and erase edit a string", "stoi turns text into an int", "to_string turns a number into text"],
    hook="Turn text into numbers, and numbers into text.",
    intro="Today we edit text and we convert it. A string can become a number, and a number can become a string.",
    concept="A string has editing tools. Replace swaps a piece of text for another. Erase removes a piece. Insert adds a piece.\n"
            "Stoi turns text into an int. To string turns a number into text. Think of a tailor. He cuts a piece, stitches a new piece, and measures the cloth.",
    A=dict(file="edit.cpp", label="Edit a string", on="replace and erase change the text in place",
           src='''
#include <iostream>
#include <string>
using namespace std;

int main() {
    string s = "Goa is sunny";
    s.replace(7, 5, "warm");
    cout << s << endl;
    s.erase(3, 3);
    cout << s << endl;
    return 0;
}
''',
           narr="[HL: string s] The text is Goa is sunny. [HL: s.replace] Replace starts at index seven, cuts five letters, and puts in warm. The text is now Goa is warm. "
                "[HL: s.erase] Erase starts at index three and removes three letters. Those letters are a space, the letter i and the letter s. [HL: cout << s << endl;] The text is now Goa warm."),
    ill=dict(label="Edit tools", on="a table of string edit calls",
             data=table(["Call", "Result on Goa is sunny"], [["s.replace(7, 5, \"warm\")", "Goa is warm"], ["s.erase(3, 3)", "Goa warm"], ["s.insert(0, \"Sunny \")", "Sunny Goa warm"], ["s.substr(0, 3)", "Goa"]]),
             narr="The table lists four calls. Each call changes the text, or makes a new piece. Index and length are always the two numbers. "
                  "The first number is where to start. The second is how many letters."),
    B=dict(file="convert.cpp", label="Text and numbers", on="stoi and to_string convert between text and numbers",
           src='''
#include <iostream>
#include <string>
using namespace std;

int main() {
    string text = "42";
    int n = stoi(text);
    cout << n + 1 << endl;
    string label = "Total: " + to_string(n * 2);
    cout << label << endl;
    return 0;
}
''',
           narr="[HL: string text] The text holds the two characters four and two. [HL: stoi(text)] Stoi reads them as the number forty-two. [HL: n + 1] Now we can do maths. Forty-two plus one is forty-three. "
                "[HL: to_string(n * 2)] To string turns eighty-four into text. [HL: cout << label] Plus joins it to the label."),
    term="The program prints forty-three, then Total colon eighty-four.",
    recap=["Replace, erase and insert edit a string.", "The first number is the start, and the second is the length.",
           "Stoi turns text into an int.", "To string turns a number into text."],
    bug=dict(title="Stoi on text that is not a number", file="convert.cpp", kind="runtime", wrong_note="the text has no digits",
             wrong='''
#include <iostream>
#include <string>
using namespace std;

int main() {
    string text = "abc";
    int n = stoi(text);
    cout << n << endl;
    return 0;
}
''', fixed_note="the text is checked with try and catch",
             fixed='''
#include <iostream>
#include <string>
using namespace std;

int main() {
    string text = "abc";
    try {
        int n = stoi(text);
        cout << n << endl;
    } catch (const exception&) {
        cout << "Not a number" << endl;
    }
    return 0;
}
''',
             why="Stoi cannot read letters as a number, so it throws an exception. If nobody catches it, the program stops. Use try and catch to handle it.",
             narr="Bug of the Day. We call stoi on the text abc. The program stops. It says terminate called after throwing an instance of invalid argument. "
                  "Stoi cannot read letters as a number. Wrap the call in try and catch, and print a friendly message."),
    pun="I asked a string to become a number. It said, I need a moment to digit.",
    task="add two numbers from text", challenge="Convert the texts twelve and thirty to ints with stoi. Print their sum as text with to string.",
    answer="Call stoi on each text. Add the two ints, and pass the sum to to string. The answer is forty-two.",
))

EPISODES.append(dict(
    n=38, title="C-style strings", spoken="C-style strings", yt="C++ C-Style Strings: char Arrays and strlen",
    thumb="CHAR ARRAYS", vis="a necklace of letters ending in a null bead",
    goals=["explain what a char array is", "use strlen and strcmp", "avoid comparing C strings with equals equals"],
    tags=["c style string", "char array", "strlen strcmp", "null terminator"],
    analogy="a necklace of letter beads that ends in a special blank bead",
    c_pts=["A C string is a char array", "It ends with a null character", "Compare C strings with strcmp"],
    hook="Old C strings still hide in modern code.",
    intro="Today we look at the old way to store text. C strings are everywhere, so you must know how they work.",
    concept="A C string is an array of chars. The last char is a special null character. It marks the end of the text. The null character has the code zero.\n"
            "The cstring header has helpers. Strlen counts the letters. Strcmp compares two strings. Think of a necklace of letter beads that ends with one blank bead.",
    A=dict(file="cstring.cpp", label="A char array", on="a char array with strlen and sizeof",
           src='''
#include <cstring>
#include <iostream>
using namespace std;

int main() {
    char name[] = "Goa";
    cout << strlen(name) << endl;
    cout << sizeof(name) << endl;
    cout << name << endl;
    return 0;
}
''',
           narr="[HL: char name[]] The compiler counts the letters and makes room for them. [HL: strlen(name)] Strlen counts the letters before the null. It gives three. "
                "[HL: sizeof(name)] Sizeof counts all the bytes. It gives four, because the null character takes one byte. [HL: cout << name] Cout prints letters until it meets the null."),
    ill=dict(label="Four boxes for three letters", on="four char boxes: G, o, a and the null character",
             data=mem([("name", "char[4]", "'G', 'o', 'a', '\\0'")], caption="The last box holds the null character, which marks the end"),
             narr="Look at the four boxes. The first three hold the letters. The fourth holds the null character. "
                  "Cout and strlen stop when they meet it. If the null is missing, they read on into other memory."),
    B=dict(file="compare.cpp", label="Compare two C strings", on="strcmp compares the text, not the address",
           src='''
#include <cstring>
#include <iostream>
using namespace std;

int main() {
    char a[] = "goa";
    char b[] = "goa";
    cout << (strcmp(a, b) == 0) << endl;
    return 0;
}
''',
           narr="[HL: char a[]] Two arrays hold the same text. [HL: strcmp(a, b)] Strcmp compares the letters. It returns zero when the texts are equal. "
                "[HL: == 0] So we test the answer against zero. The result is true, so cout prints one."),
    term="The program prints one.",
    recap=["A C string is a char array that ends with a null character.", "Strlen counts the letters.",
           "Sizeof counts all the bytes.", "Use strcmp to compare two C strings."],
    bug=dict(title="Comparing C strings with equals", file="compare.cpp", kind="warn", wrong_note="two arrays are compared with two equals signs",
             wrong='''
#include <iostream>
using namespace std;

int main() {
    char a[] = "goa";
    char b[] = "goa";
    if (a == b) {
        cout << "Same" << endl;
    }
    return 0;
}
''', fixed_note="strcmp compares the text",
             fixed='''
#include <cstring>
#include <iostream>
using namespace std;

int main() {
    char a[] = "goa";
    char b[] = "goa";
    if (strcmp(a, b) == 0) {
        cout << "Same" << endl;
    }
    return 0;
}
''',
             why="Two equals signs compare the addresses of the two arrays, not their letters. The addresses always differ. Use strcmp, or use std string.",
             narr="Bug of the Day. Both arrays hold goa, but the test is never true. Two equals signs compare addresses, not letters. "
                  "The compiler warns that comparing two arrays is deprecated. Use strcmp, or better, use std string."),
    pun="Why did the C string feel empty? Its last bead was always null.",
    task="count the letters with a loop", challenge="Write a loop that counts the letters of a char array, without strlen. Stop at the null character.",
    answer="Start i at zero. While name at i is not the null character, add one to i. The final i is the length.",
))

EPISODES.append(dict(
    n=39, title="Searching", spoken="searching", yt="C++ Searching: Linear and Binary Search",
    thumb="FIND IT FAST", vis="a crab with a magnifying glass at a library shelf",
    goals=["write a linear search", "write a binary search on a sorted array", "explain why binary search needs sorted data"],
    tags=["linear search", "binary search", "c++ searching algorithms", "sorted array"],
    analogy="a dictionary: you open it in the middle, then choose the left or the right half",
    c_pts=["Linear search checks each item", "Binary search halves the range each time", "Binary search needs sorted data"],
    hook="Find one item among a million in about twenty steps.",
    intro="Today we search. One method is simple. The other is clever, and it finds one item among a million in about twenty steps.",
    concept="Linear search checks the items one by one, from the start. It works on any data, but it can be slow.\n"
            "Binary search needs sorted data. It looks at the middle item, and then it throws away half of the range. Think of a dictionary. You open it in the middle, then you pick the left or the right half.",
    A=dict(file="linear.cpp", label="Linear search", on="a function that returns the index of a value",
           src='''
#include <iostream>
using namespace std;

int find_index(const int a[], int n, int target) {
    for (int i = 0; i < n; i++) {
        if (a[i] == target) {
            return i;
        }
    }
    return -1;
}

int main() {
    int a[5] = {5, 1, 9, 3, 7};
    cout << find_index(a, 5, 3) << endl;
    cout << find_index(a, 5, 4) << endl;
    return 0;
}
''',
           narr="[HL: for (int i] The loop checks each index from zero. [HL: if (a[i] == target)] If the item equals the target, [HL: return i;] the function returns that index at once. "
                "[HL: return -1;] If the loop ends, the value is not there. We return minus one. [HL: find_index(a, 5, 3)] Three is at index three. [HL: find_index(a, 5, 4)] Four is not in the array, so the answer is minus one."),
    ill=dict(label="Binary search steps", on="a table: low, high, middle and the decision for each step",
             data=table(["Step", "low", "high", "mid", "Decision"], [["1", "0", "6", "3", "a[3] = 7 > 5, go left"], ["2", "0", "2", "1", "a[1] = 3 < 5, go right"], ["3", "2", "2", "2", "a[2] = 5, found"]]),
             narr="Here is a binary search for five in the sorted list one, three, five, seven, nine, eleven, thirteen. "
                  "Step one looks at the middle item, seven. Five is smaller, so go left. Step two looks at three. Five is bigger, so go right. Step three finds five. Only three steps were needed."),
    B=dict(file="binary.cpp", label="Binary search", on="binary search on a sorted array",
           src='''
#include <iostream>
using namespace std;

int binary_search_index(const int a[], int n, int target) {
    int low = 0, high = n - 1;
    while (low <= high) {
        int mid = (low + high) / 2;
        if (a[mid] == target) {
            return mid;
        } else if (a[mid] < target) {
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }
    return -1;
}

int main() {
    int a[7] = {1, 3, 5, 7, 9, 11, 13};
    cout << binary_search_index(a, 7, 5) << endl;
    return 0;
}
''',
           narr="[HL: int low = 0] Low and high mark the part of the array that is still possible. [HL: int mid] Mid is the middle index. [HL: if (a[mid] == target)] If the middle item is the target, we are done. "
                "[HL: low = mid + 1] If it is too small, we move low past mid. [HL: high = mid - 1] If it is too big, we move high below mid. [HL: return -1;] When low passes high, the target is not there."),
    term="The program prints two.",
    recap=["Linear search checks the items one by one.", "Binary search halves the range each time.",
           "Binary search needs sorted data.", "Both return minus one when the value is missing."],
    bug=dict(title="Binary search on unsorted data", file="binary.cpp", kind="output", wrong_note="the array is not sorted",
             wrong='''
#include <iostream>
using namespace std;

int binary_search_index(const int a[], int n, int target) {
    int low = 0, high = n - 1;
    while (low <= high) {
        int mid = (low + high) / 2;
        if (a[mid] == target) {
            return mid;
        } else if (a[mid] < target) {
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }
    return -1;
}

int main() {
    int a[5] = {5, 1, 9, 3, 7};
    cout << binary_search_index(a, 5, 3) << endl;
    return 0;
}
''', fixed_note="the array is sorted",
             fixed='''
#include <iostream>
using namespace std;

int binary_search_index(const int a[], int n, int target) {
    int low = 0, high = n - 1;
    while (low <= high) {
        int mid = (low + high) / 2;
        if (a[mid] == target) {
            return mid;
        } else if (a[mid] < target) {
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }
    return -1;
}

int main() {
    int a[5] = {1, 3, 5, 7, 9};
    cout << binary_search_index(a, 5, 3) << endl;
    return 0;
}
''',
             why="Binary search throws away half of the range using the order of the items. If the items are not in order, it throws away the wrong half.",
             narr="Bug of the Day. The array holds three, but the search says minus one. The array is not sorted. Binary search looks at nine in the middle. "
                  "Nine is bigger than three, so it throws away the right half. But the three was in the right half. Sort the array first."),
    pun="I use binary search to find my socks. Half of the drawer is always wrong.",
    task="search for a name", challenge="Write a linear search that finds a name in an array of five strings. Print the index, or minus one.",
    answer="Loop over the array. If the item equals the target string, return its index. After the loop, return minus one.",
))

EPISODES.append(dict(
    n=40, title="Sorting: bubble and selection", spoken="sorting, bubble and selection", yt="C++ Sorting: Bubble Sort and Selection Sort",
    thumb="SORT THE BARS", vis="five bars of different heights being swapped",
    goals=["trace a bubble sort", "write a selection sort", "count the compares and swaps"],
    tags=["bubble sort", "selection sort", "sorting algorithms c++", "swap"],
    analogy="students lining up by height: neighbours swap places until the line is right",
    c_pts=["Bubble sort swaps neighbours", "Selection sort picks the smallest", "Both use nested loops"],
    hook="Watch five bars sort themselves.",
    intro="Today we sort. You will watch bars move, and then you will write the code that moves them.",
    concept="Sorting puts items in order. Bubble sort compares two neighbours, and swaps them if they are in the wrong order. After each pass, the biggest item has moved to the end.\n"
            "Selection sort finds the smallest item, and puts it first. Think of students who line up by height. Neighbours swap places until the line is right.",
    A=dict(file="bubble.cpp", label="Bubble sort", on="bubble sort with two loops and a swap",
           src='''
#include <iostream>
using namespace std;

int main() {
    int a[5] = {5, 3, 8, 1, 4};
    int n = 5;
    for (int pass = 0; pass < n - 1; pass++) {
        for (int j = 0; j < n - 1 - pass; j++) {
            if (a[j] > a[j + 1]) {
                int t = a[j];
                a[j] = a[j + 1];
                a[j + 1] = t;
            }
        }
    }
    for (int x : a) {
        cout << x << " ";
    }
    cout << endl;
    return 0;
}
''',
           narr="[HL: for (int pass] Each pass moves the biggest unsorted item to its place at the end. [HL: for (int j] The inner loop visits each neighbour pair. The range gets shorter after each pass. "
                "[HL: if (a[j] > a[j + 1])] If the left item is bigger, [HL: int t = a[j]] we swap the two items with a helper box. [HL: for (int x : a)] When all passes end, the array reads one, three, four, five, eight."),
    ill=dict(label="Bubble sort on five bars", on="bars compare, swap and turn mint as they reach their place",
             data=trace("bubble", [5, 3, 8, 1, 4]),
             narr="Watch the bars. Two neighbours are compared. If the left one is taller, they swap. After the first pass, the tallest bar sits on the right. "
                  "After each pass, one more bar turns mint. At the end, all bars are in order."),
    B=dict(file="selection.cpp", label="Selection sort", on="selection sort picks the smallest item each time",
           src='''
#include <iostream>
using namespace std;

int main() {
    int a[5] = {5, 3, 8, 1, 4};
    int n = 5;
    for (int i = 0; i < n - 1; i++) {
        int m = i;
        for (int j = i + 1; j < n; j++) {
            if (a[j] < a[m]) {
                m = j;
            }
        }
        int t = a[i];
        a[i] = a[m];
        a[m] = t;
    }
    for (int x : a) {
        cout << x << " ";
    }
    cout << endl;
    return 0;
}
''',
           narr="[HL: int m = i] M holds the index of the smallest item that we know so far. [HL: for (int j] The inner loop looks at all the items to the right. [HL: if (a[j] < a[m])] A smaller item becomes the new m. "
                "[HL: int t = a[i]] After the inner loop, we swap the smallest item into position i. Selection sort makes at most one swap for each pass."),
    term="The program prints one, three, four, five, eight.",
    recap=["Bubble sort swaps neighbours that are out of order.", "Selection sort swaps the smallest item to the front.",
           "Both use nested loops.", "Count the compares and swaps to compare the methods."],
    bug=dict(title="A swap that loses a value", file="bubble.cpp", kind="output", wrong_note="the swap has no helper box",
             wrong='''
#include <iostream>
using namespace std;

int main() {
    int a[3] = {3, 1, 2};
    int n = 3;
    for (int pass = 0; pass < n - 1; pass++) {
        for (int j = 0; j < n - 1 - pass; j++) {
            if (a[j] > a[j + 1]) {
                a[j] = a[j + 1];
                a[j + 1] = a[j];
            }
        }
    }
    for (int x : a) {
        cout << x << " ";
    }
    cout << endl;
    return 0;
}
''', fixed_note="a helper box keeps the old value",
             fixed='''
#include <iostream>
using namespace std;

int main() {
    int a[3] = {3, 1, 2};
    int n = 3;
    for (int pass = 0; pass < n - 1; pass++) {
        for (int j = 0; j < n - 1 - pass; j++) {
            if (a[j] > a[j + 1]) {
                int t = a[j];
                a[j] = a[j + 1];
                a[j + 1] = t;
            }
        }
    }
    for (int x : a) {
        cout << x << " ";
    }
    cout << endl;
    return 0;
}
''',
             why="The first line overwrites a at j. The second line then copies the new value back, so both boxes hold the same number. A helper box keeps the old value.",
             narr="Bug of the Day. The array is three, one, two. The sorted output has repeated numbers. The swap has no helper box. "
                  "The first line overwrites a j. The second line copies the same value back. Both boxes now hold one. Save the old value in a helper box first."),
    pun="Bubble sort is a patient algorithm. It takes many passes, and it never complains.",
    task="count the swaps", challenge="Add a counter to bubble sort. Print how many swaps it made for the array five, three, eight, one, four.",
    answer="Add one to a counter inside the if, next to the swap. For this array, the counter ends at six.",
))
