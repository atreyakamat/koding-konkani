"""Module 9 — The standard library and modern C++ (EP 77-84)."""
from lib import flow, table, mem

MODULE = {"id": 9, "name": "Library and modern C++", "range": "77–84", "colours": "Cream + Tomato", "bg": "cream"}
NEXT_AFTER = ("Next: EP 85 · Linked list", "We end module nine here. Next time: data structures, starting with the linked list.")
EPISODES = []

EPISODES.append(dict(
    n=77, title="Algorithms from the library", spoken="algorithms from the library", yt="C++ STL Algorithms: sort, find, count, accumulate",
    thumb="ONE LINE SORT", vis="a magic wand sorting a messy shelf of books",
    goals=["sort a vector with one call", "find and count values", "add up a range with accumulate"],
    tags=["c++ stl algorithms", "std::sort", "std::find", "accumulate", "c++ for beginners"],
    analogy="a toolbox where every tool already exists",
    c_pts=["Algorithms work on a range of iterators", "A range is a begin and an end", "Do not write loops the library already has"],
    hook="Sort a whole vector with one line.",
    intro="Today we stop writing loops by hand. The standard library already has tools for sorting, searching and counting.",
    concept="The algorithm header holds many ready tools. Each tool takes a range, which is a begin iterator and an end iterator.\n"
            "The tools are tested and fast. Think of a toolbox. You pick the tool, and you do not build it again.",
    A=dict(file="algos.cpp", label="Sort, max and reverse", on="a vector is sorted, searched for its biggest, and reversed",
           src='''
#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

int main() {
    vector<int> v = {5, 2, 9, 1, 7};
    sort(v.begin(), v.end());
    for (int x : v) {
        cout << x << " ";
    }
    cout << endl;
    cout << *max_element(v.begin(), v.end()) << endl;
    reverse(v.begin(), v.end());
    cout << v[0] << endl;
    return 0;
}
''',
           narr="[HL: sort(v.begin(), v.end())] Sort takes the begin and the end of the vector. It puts the numbers in order. [HL: for (int x : v)] The loop prints one two five seven nine. "
                "[HL: max_element] Max element returns an iterator to the biggest value. [HL: *max_element] The star reads the value, which is nine. [HL: reverse(v.begin(), v.end())] Reverse flips the order. "
                "[HL: cout << v[0]] The first item is now nine."),
    ill=dict(label="Common algorithms", on="a table of five library algorithms and what each one does",
             data=table(["Algorithm", "Header", "What it does"], [["sort", "algorithm", "puts items in order"], ["find", "algorithm", "returns an iterator to a match"], ["count", "algorithm", "counts equal items"],
                                                                  ["reverse", "algorithm", "flips the order"], ["accumulate", "numeric", "adds up a range"]]),
             narr="Here are five tools. Sort, find, count and reverse live in the algorithm header. Accumulate lives in the numeric header. "
                  "All five take a range."),
    B=dict(file="find.cpp", label="Find, count and accumulate", on="find a value, count a value, and add up all values",
           src='''
#include <algorithm>
#include <iostream>
#include <numeric>
#include <vector>
using namespace std;

int main() {
    vector<int> v = {4, 8, 4, 1, 4};
    auto it = find(v.begin(), v.end(), 8);
    if (it != v.end()) {
        cout << "found at " << (it - v.begin()) << endl;
    }
    cout << count(v.begin(), v.end(), 4) << endl;
    cout << accumulate(v.begin(), v.end(), 0) << endl;
    return 0;
}
''',
           narr="[HL: auto it = find] Find returns an iterator to the first match. [HL: if (it != v.end())] If the result is not the end, the value exists. [HL: it - v.begin()] Subtracting the begin gives the index, which is one. "
                "[HL: count(v.begin(), v.end(), 4)] Count returns how many fours there are, which is three. [HL: accumulate] Accumulate adds all values, starting from zero. The sum is twenty-one."),
    term="The program prints found at one, then three, then twenty-one.",
    recap=["Algorithms work on a range of iterators.", "Sort puts a range in order.", "Find returns an iterator, and the end means not found.", "Accumulate adds up a range."],
    bug=dict(title="Sort with no iterators", file="sortbug.cpp", kind="compile", wrong_note="sort gets the vector, not a begin and an end",
             wrong='''
#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

int main() {
    vector<int> v = {3, 1, 2};
    sort(v);
    cout << v[0] << endl;
    return 0;
}
''', fixed_note="sort gets begin and end",
             fixed='''
#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

int main() {
    vector<int> v = {3, 1, 2};
    sort(v.begin(), v.end());
    cout << v[0] << endl;
    return 0;
}
''',
             why="The classic sort needs two iterators. Pass v dot begin and v dot end. In C plus plus twenty, ranges sort accepts the whole vector.",
             narr="Bug of the Day. We call sort with only the vector. The compiler says there is no matching function. "
                  "Sort needs a begin and an end. Pass both iterators."),
    pun="Why did the vector go to the library? It wanted to be sorted out.",
    task="find the smallest value", challenge="Use a library algorithm to print the smallest value of a vector. Do not write a loop.",
    answer="Call min element with begin and end. Put a star in front of the result to read the value.",
))

EPISODES.append(dict(
    n=78, title="Lambdas with algorithms", spoken="lambdas with algorithms", yt="C++ Lambdas with STL Algorithms",
    thumb="LAMBDA", vis="a tiny rule card handed to a sorting machine",
    goals=["write a lambda", "sort with your own rule", "capture a variable in a lambda"],
    tags=["c++ lambda", "lambda capture", "std::sort custom", "count_if"],
    analogy="a sticky note with a small rule, handed to the algorithm",
    c_pts=["A lambda is a function with no name", "Square brackets hold the captures", "Algorithms accept lambdas as rules"],
    hook="Give any algorithm your own rule.",
    intro="Today we hand rules to algorithms. A lambda is a small function you write in the same place where you use it.",
    concept="A lambda has square brackets, a parameter list and a body. The square brackets are the capture list. They name outside variables that the lambda may read.\n"
            "Think of a sticky note with a small rule. You hand the note to the algorithm, and it follows the rule.",
    A=dict(file="lambda.cpp", label="Sort descending and count_if", on="a lambda sorts in reverse and another lambda counts big numbers",
           src='''
#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

int main() {
    vector<int> v = {5, 2, 9, 1, 7};
    sort(v.begin(), v.end(), [](int a, int b) { return a > b; });
    for (int x : v) {
        cout << x << " ";
    }
    cout << endl;
    int limit = 4;
    int big = count_if(v.begin(), v.end(), [limit](int x) { return x > limit; });
    cout << big << endl;
    return 0;
}
''',
           narr="[HL: [](int a, int b)] The empty square brackets mean the lambda captures nothing. It takes two ints. [HL: return a > b] It says that a comes first when a is bigger. The result is nine seven five two one. "
                "[HL: int limit = 4] Now we make a local variable. [HL: [limit](int x)] Putting limit in the brackets captures it. The lambda can now read it. [HL: count_if] Count if counts the items for which the lambda says true. Three items are bigger than four."),
    ill=dict(label="Anatomy of a lambda", on="a table that names each part of a lambda",
             data=table(["Part", "Example", "Meaning"], [["capture", "[limit]", "outside variables the lambda may read"], ["parameters", "(int x)", "values the algorithm passes in"], ["body", "{ return x > limit; }", "the rule itself"]]),
             narr="A lambda has three parts. The capture list names outside variables. The parameters are the values the algorithm passes in. "
                  "The body holds the rule."),
    B=dict(file="students.cpp", label="Sort a struct by marks", on="students are sorted by marks with a lambda",
           src='''
#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

struct Student {
    string name;
    int marks;
};

int main() {
    vector<Student> s = {{"Asha", 91}, {"Ravi", 78}, {"Mia", 85}};
    sort(s.begin(), s.end(), [](const Student& a, const Student& b) { return a.marks > b.marks; });
    for_each(s.begin(), s.end(), [](const Student& st) { cout << st.name << " " << st.marks << endl; });
    return 0;
}
''',
           narr="[HL: struct Student] A student has a name and marks. [HL: sort(s.begin(), s.end()] We sort the students. [HL: a.marks > b.marks] The lambda compares marks, so the highest marks come first. "
                "[HL: for_each] For each calls a lambda on every item. [HL: cout << st.name] The lambda prints Asha ninety-one, then Mia eighty-five, then Ravi seventy-eight."),
    term="The program prints the three students, from the highest marks to the lowest.",
    recap=["A lambda is a small function with no name.", "The capture list names outside variables.", "Algorithms take lambdas as rules.", "Pass a struct by const reference to avoid a copy."],
    bug=dict(title="A variable that is not captured", file="capture.cpp", kind="compile", wrong_note="the lambda reads limit, but the capture list is empty",
             wrong='''
#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

int main() {
    vector<int> v = {1, 5, 9};
    int limit = 4;
    int big = count_if(v.begin(), v.end(), [](int x) { return x > limit; });
    cout << big << endl;
    return 0;
}
''', fixed_note="limit is in the capture list",
             fixed='''
#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

int main() {
    vector<int> v = {1, 5, 9};
    int limit = 4;
    int big = count_if(v.begin(), v.end(), [limit](int x) { return x > limit; });
    cout << big << endl;
    return 0;
}
''',
             why="A lambda cannot see local variables unless you capture them. Write the name in the square brackets. Use an ampersand in front of the name to capture by reference.",
             narr="Bug of the Day. The lambda reads limit, but the brackets are empty. The compiler says limit is not captured. "
                  "Put limit in the square brackets."),
    pun="Why did the lambda join the party? Nobody had to give it a name.",
    task="count the even numbers", challenge="Use count if and a lambda to count the even numbers in a vector.",
    answer="Call count if with begin and end. The lambda takes an int x and returns x modulo two equals zero.",
))

EPISODES.append(dict(
    n=79, title="Ranges in C++20", spoken="ranges in C plus plus twenty", yt="C++20 Ranges and Views: filter, transform, take",
    thumb="RANGES", vis="a conveyor belt with a filter gate and a squash press",
    goals=["build a pipeline with the pipe symbol", "filter and transform lazily", "sort a whole vector with ranges sort"],
    tags=["c++20 ranges", "std::views", "views::filter", "views::transform", "modern c++"],
    analogy="a conveyor belt: each station changes the items that pass",
    c_pts=["A view does not copy the data", "The pipe symbol joins stations", "Views work only when you read them"],
    hook="Filter and square numbers in one pipeline.",
    intro="Today we meet ranges, new in C plus plus twenty. They let you chain steps with the pipe symbol, like a conveyor belt.",
    concept="A view is a lazy window on a range. It does not copy the data, and it does no work until you read it.\n"
            "You join views with the pipe symbol. Think of a conveyor belt. Each station changes the items that pass, one at a time.",
    A=dict(file="ranges.cpp", label="Filter then transform", on="even numbers are kept, then squared, then printed",
           src='''
#include <algorithm>
#include <functional>
#include <iostream>
#include <ranges>
#include <vector>
using namespace std;

int main() {
    vector<int> v = {1, 2, 3, 4, 5, 6, 7, 8};
    auto result = v | views::filter([](int x) { return x % 2 == 0; })
                    | views::transform([](int x) { return x * x; });
    for (int x : result) {
        cout << x << " ";
    }
    cout << endl;
    ranges::sort(v, greater<>());
    cout << v[0] << endl;
    return 0;
}
''',
           narr="[HL: v | views::filter] The pipe sends the vector into a filter station. The lambda keeps only even numbers. [HL: | views::transform] The next station squares each number that passes. [HL: for (int x : result)] Nothing runs until this loop reads the view. "
                "The output is four sixteen thirty-six sixty-four. [HL: ranges::sort(v, greater<>())] Ranges sort takes the whole vector, and no iterators. Greater sorts from big to small. [HL: cout << v[0]] The first value is eight."),
    ill=dict(label="The pipeline", on="a flow from the vector, through the filter, to the transform",
             data=flow([("vector", "1 2 3 4 5 6 7 8"), ("filter", "keeps 2 4 6 8"), ("transform", "squares them: 4 16 36 64"), ("loop", "reads and prints the values")]),
             narr="The data flows left to right. The vector goes into the filter. The filter keeps the even numbers. "
                  "The transform squares them. The loop pulls the values out one by one."),
    B=dict(file="iota.cpp", label="iota and take", on="an endless counter is cut to the first five numbers",
           src='''
#include <iostream>
#include <ranges>
using namespace std;

int main() {
    for (int x : views::iota(1) | views::take(5)) {
        cout << x << " ";
    }
    cout << endl;
    return 0;
}
''',
           narr="[HL: views::iota(1)] Iota makes an endless counter that starts at one. It does not fill memory, because a view is lazy. [HL: views::take(5)] Take cuts the counter after five items. "
                "The output is one two three four five."),
    term="The program prints the squares of the even numbers, then eight, then one to five.",
    recap=["A view is a lazy window on a range.", "The pipe symbol joins stations.", "Views copy no data.", "Ranges sort takes the whole container."],
    bug=dict(title="A missing header", file="rangebug.cpp", kind="compile", wrong_note="the ranges header is missing",
             wrong='''
#include <iostream>
#include <vector>
using namespace std;

int main() {
    vector<int> v = {1, 2, 3, 4};
    for (int x : v | views::take(2)) {
        cout << x << " ";
    }
    cout << endl;
    return 0;
}
''', fixed_note="the ranges header is included",
             fixed='''
#include <iostream>
#include <ranges>
#include <vector>
using namespace std;

int main() {
    vector<int> v = {1, 2, 3, 4};
    for (int x : v | views::take(2)) {
        cout << x << " ";
    }
    cout << endl;
    return 0;
}
''',
             why="Views live in the ranges header. Include it. Also compile with the C plus plus twenty flag.",
             narr="Bug of the Day. We use views without the ranges header. The compiler says views has not been declared. "
                  "Add the include line for ranges."),
    pun="Why did the view stay calm? It never copied anything, so it had nothing to lose.",
    task="keep the odd numbers", challenge="Use a filter view to print only the odd numbers of a vector.",
    answer="Pipe the vector into views filter. The lambda returns x modulo two not equal to zero. Print the view with a loop.",
))

EPISODES.append(dict(
    n=80, title="Move semantics", spoken="move semantics", yt="C++ Move Semantics: std::move Explained",
    thumb="MOVE", vis="a crab handing over a treasure chest instead of copying it",
    goals=["tell a copy from a move", "use std move", "write a move constructor"],
    tags=["c++ move semantics", "std::move", "move constructor", "rvalue reference", "unique_ptr"],
    analogy="handing over the keys instead of building a second house",
    c_pts=["A copy duplicates the data", "A move steals the data", "Do not use an object after you move it"],
    hook="Move the data. Do not copy it.",
    intro="Today we learn to move data. A move hands over the data instead of copying it, so big objects stay fast.",
    concept="A copy makes a second set of data. A move hands the data to the new owner, and leaves the old owner empty.\n"
            "Think of handing over the keys of a house. You do not build a second house.",
    A=dict(file="move.cpp", label="Move a vector", on="a vector is moved, and the old vector is empty",
           src='''
#include <iostream>
#include <utility>
#include <vector>
using namespace std;

int main() {
    vector<int> a = {1, 2, 3};
    vector<int> b = move(a);
    cout << b.size() << endl;
    cout << a.empty() << endl;
    return 0;
}
''',
           narr="[HL: vector<int> a] Vector a owns three numbers on the heap. [HL: move(a)] Move does not move anything by itself. It marks a as safe to steal from. "
                "[HL: vector<int> b = ] The vector b takes the heap block from a. No number is copied. [HL: cout << b.size()] Vector b has three items. [HL: a.empty()] For a vector, the standard says the old vector is empty. The output is one."),
    ill=dict(label="Before and after the move", on="memory boxes: b now owns the block, a points to nothing",
             data=mem([("a.data_", "int*", "nullptr", "stack"), ("b.data_", "int*", None, "stack"), ("block", "int[3]", "1, 2, 3", "heap")], arrows=[("b.data_", "block[0]", "owns")],
                      caption="After the move, b owns the block and a points to nothing"),
             narr="After the move, b owns the heap block. The pointer inside a is null. "
                  "Only the pointer moved. The three numbers did not move at all."),
    B=dict(file="buffer.cpp", label="A move constructor", on="a class with a move constructor steals the pointer",
           src='''
#include <cstddef>
#include <iostream>
#include <utility>
using namespace std;

class Buffer {
public:
    explicit Buffer(size_t n) : data_(new int[n]), size_(n) {
        cout << "made" << endl;
    }
    Buffer(Buffer&& other) noexcept : data_(other.data_), size_(other.size_) {
        other.data_ = nullptr;
        other.size_ = 0;
        cout << "moved" << endl;
    }
    Buffer(const Buffer&) = delete;
    ~Buffer() { delete[] data_; }
    size_t size() const { return size_; }

private:
    int* data_;
    size_t size_;
};

int main() {
    Buffer a(100);
    Buffer b = move(a);
    cout << b.size() << " " << a.size() << endl;
    return 0;
}
''',
           narr="[HL: Buffer(Buffer&& other)] Two ampersands make an rvalue reference. This is the move constructor. [HL: data_(other.data_)] It copies only the pointer. [HL: other.data_ = nullptr] Then it sets the old pointer to null, so the old object frees nothing. "
                "[HL: Buffer(const Buffer&) = delete] We delete the copy constructor, because a copy would be wrong here. [HL: Buffer b = move(a)] This line calls the move constructor. "
                "The output is made, moved, and then one hundred and zero."),
    term="The program prints made, moved, and then one hundred and zero.",
    recap=["A copy duplicates the data.", "A move hands over the data.", "Move leaves the old object empty.", "Do not use an object after you move it."],
    bug=dict(title="Copying a unique pointer", file="unique.cpp", kind="compile", wrong_note="a unique pointer is copied",
             wrong='''
#include <iostream>
#include <memory>
using namespace std;

int main() {
    unique_ptr<int> a = make_unique<int>(5);
    unique_ptr<int> b = a;
    cout << *b << endl;
    return 0;
}
''', fixed_note="the pointer is moved",
             fixed='''
#include <iostream>
#include <memory>
#include <utility>
using namespace std;

int main() {
    unique_ptr<int> a = make_unique<int>(5);
    unique_ptr<int> b = move(a);
    cout << *b << endl;
    return 0;
}
''',
             why="A unique pointer has one owner only, so it cannot be copied. Move it to give the ownership to another pointer.",
             narr="Bug of the Day. We copy a unique pointer. The compiler says the copy constructor is deleted. "
                  "One owner only. Use move to hand over the ownership."),
    pun="Why did the string move out? It wanted its own space, with no copies.",
    task="move a string into a vector", challenge="Make a string, and push it into a vector of strings with move. Print the vector size.",
    answer="Call push back with move of the string. The vector size is one.",
))

EPISODES.append(dict(
    n=81, title="optional and variant", spoken="optional and variant", yt="C++ std::optional and std::variant",
    thumb="MAYBE", vis="a gift box that may be empty, and a box with two shapes",
    goals=["return a value that may be missing", "use value_or", "store one of several types in a variant"],
    tags=["std::optional", "std::variant", "std::visit", "modern c++", "nullopt"],
    analogy="a gift box that may be empty, and a lunch box that holds one of two meals",
    c_pts=["Optional holds a value or nothing", "Variant holds one of several types", "Check before you read"],
    hook="Return a value that may not exist.",
    intro="Today we handle missing values the safe way. Optional holds a value or nothing. Variant holds one of several types.",
    concept="Some functions may have no answer. Old code returned minus one, or a null pointer. That is easy to misuse.\n"
            "Optional says it in the type. It holds a value, or it holds nothing. Variant holds exactly one value from a list of types.",
    A=dict(file="optional.cpp", label="A search that may fail", on="find index returns an optional",
           src='''
#include <iostream>
#include <optional>
#include <vector>
using namespace std;

optional<int> find_index(const vector<int>& v, int x) {
    for (size_t i = 0; i < v.size(); ++i) {
        if (v[i] == x) {
            return static_cast<int>(i);
        }
    }
    return nullopt;
}

int main() {
    vector<int> v = {4, 8, 15};
    auto r = find_index(v, 8);
    if (r) {
        cout << "at " << *r << endl;
    }
    auto m = find_index(v, 99);
    cout << m.value_or(-1) << endl;
    return 0;
}
''',
           narr="[HL: optional<int> find_index] The function returns an optional int. [HL: return static_cast<int>(i)] When it finds the value, it returns the index. [HL: return nullopt] Otherwise it returns nullopt, which means no value. "
                "[HL: if (r)] An optional is true when it holds a value. [HL: *r] The star reads the value, which is one. [HL: m.value_or(-1)] Value or gives a default when the optional is empty. That prints minus one."),
    ill=dict(label="Two optionals", on="a table: one optional holds a value, one is empty",
             data=table(["Optional", "Has value", "value_or(-1)"], [["r", "yes, it holds 1", "1"], ["m", "no, it is empty", "-1"]]),
             narr="The optional r holds one, so value or gives one. The optional m is empty, so value or gives the default. "
                  "The default is minus one."),
    B=dict(file="variant.cpp", label="A variant", on="a variant holds an int, then a string",
           src='''
#include <iostream>
#include <string>
#include <variant>
using namespace std;

int main() {
    variant<int, string> v = 42;
    cout << get<int>(v) << endl;
    v = "hello";
    cout << holds_alternative<string>(v) << endl;
    visit([](const auto& x) { cout << x << endl; }, v);
    return 0;
}
''',
           narr="[HL: variant<int, string> v = 42] The variant holds an int or a string. Right now it holds an int. [HL: get<int>(v)] Get with a type reads that type. The output is forty-two. "
                "[HL: v = \"hello\"] Now the variant holds a string. [HL: holds_alternative<string>(v)] Holds alternative checks the current type. It prints one for true. [HL: visit] Visit calls the lambda with whatever type is inside. It prints hello."),
    term="The program prints forty-two, then one, then hello.",
    recap=["Optional holds a value or nothing.", "Value or gives a default.", "Variant holds one value from a list of types.", "Check the type before you read a variant."],
    bug=dict(title="Reading the wrong type", file="variantbug.cpp", kind="runtime", wrong_note="the variant holds an int, but the code reads a string",
             wrong='''
#include <iostream>
#include <string>
#include <variant>
using namespace std;

int main() {
    variant<int, string> v = 42;
    cout << get<string>(v) << endl;
    return 0;
}
''', fixed_note="the code checks the type first",
             fixed='''
#include <iostream>
#include <string>
#include <variant>
using namespace std;

int main() {
    variant<int, string> v = 42;
    if (holds_alternative<string>(v)) {
        cout << get<string>(v) << endl;
    } else {
        cout << "not a string" << endl;
    }
    return 0;
}
''',
             why="Get throws an exception when the variant holds another type. Check with holds alternative first, or use visit.",
             narr="Bug of the Day. The variant holds an int, but we read a string. The program stops with a bad variant access error. "
                  "Check the type first with holds alternative."),
    pun="Why did the optional feel calm? It never promised to hold anything.",
    task="return a safe square root", challenge="Write a function that returns an optional double. It returns nothing for a negative input.",
    answer="If the input is below zero, return nullopt. Otherwise return the square root.",
))

EPISODES.append(dict(
    n=82, title="Exceptions", spoken="exceptions", yt="C++ Exceptions: try, catch and throw",
    thumb="TRY / CATCH", vis="a crab catching a falling red ball with a net",
    goals=["throw an exception", "catch it with try and catch", "order catch blocks correctly"],
    tags=["c++ exceptions", "try catch", "throw", "runtime_error", "error handling"],
    analogy="a ball thrown up the stairs until someone catches it",
    c_pts=["Throw raises an error", "Catch handles it", "Put the specific catch first"],
    hook="Stop a crash before it happens.",
    intro="Today we handle errors without crashing. We throw an exception, and we catch it where we know what to do.",
    concept="When code cannot go on, it throws an exception. The program leaves the current function, and looks up the stack for a matching catch block.\n"
            "Think of a ball thrown up the stairs. It goes up until someone catches it. If nobody catches it, the program stops.",
    A=dict(file="throw.cpp", label="Throw and catch", on="divide throws, and main catches",
           src='''
#include <iostream>
#include <stdexcept>
using namespace std;

int divide(int a, int b) {
    if (b == 0) {
        throw runtime_error("cannot divide by zero");
    }
    return a / b;
}

int main() {
    try {
        cout << divide(8, 2) << endl;
        cout << divide(8, 0) << endl;
        cout << "not reached" << endl;
    } catch (const exception& e) {
        cout << "error: " << e.what() << endl;
    }
    cout << "done" << endl;
    return 0;
}
''',
           narr="[HL: if (b == 0)] The function checks for a bad input. [HL: throw runtime_error] Throw raises a runtime error with a message. [HL: try {] Main puts the risky calls inside a try block. "
                "[HL: cout << divide(8, 2)] The first call works, and prints four. [HL: cout << divide(8, 0)] The second call throws. The program jumps out of the try block. The line after it never runs. "
                "[HL: catch (const exception& e)] The catch block receives the exception by const reference. [HL: e.what()] What returns the message. [HL: cout << \"done\"] After the catch, the program goes on."),
    ill=dict(label="The path of an exception", on="a flow: throw, unwind, catch",
             data=flow([("throw", "divide throws"), ("unwind", "divide ends at once"), ("catch", "main catches it"), ("continue", "the program goes on")]),
             narr="The exception leaves divide at once. This is called unwinding. The program looks for a matching catch in main. "
                  "When it finds one, the program goes on after the catch block."),
    B=dict(file="catchorder.cpp", label="Specific before general", on="two catch blocks, the specific one first",
           src='''
#include <iostream>
#include <stdexcept>
#include <string>
using namespace std;

int main() {
    try {
        int n = stoi("abc");
        cout << n << endl;
    } catch (const invalid_argument&) {
        cout << "bad number" << endl;
    } catch (const exception&) {
        cout << "something else" << endl;
    }
    return 0;
}
''',
           narr="[HL: stoi(\"abc\")] Stoi cannot read a number from this text, so it throws invalid argument. [HL: catch (const invalid_argument&)] The first catch is specific, so it matches. [HL: cout << \"bad number\"] It prints bad number. "
                "[HL: catch (const exception&)] The general catch comes last. It catches every other standard error. Always put the specific catch first."),
    term="The program prints bad number.",
    recap=["Throw raises an exception.", "Catch handles it.", "The program unwinds until a catch matches.", "Put specific catch blocks before general ones."],
    bug=dict(title="An exception nobody catches", file="uncaught.cpp", kind="runtime", wrong_note="the throw has no try and no catch",
             wrong='''
#include <iostream>
#include <stdexcept>
using namespace std;

int main() {
    throw runtime_error("boom");
    cout << "never printed" << endl;
    return 0;
}
''', fixed_note="main catches the exception",
             fixed='''
#include <iostream>
#include <stdexcept>
using namespace std;

int main() {
    try {
        throw runtime_error("boom");
    } catch (const exception& e) {
        cout << "caught: " << e.what() << endl;
    }
    return 0;
}
''',
             why="An exception that nobody catches ends the program. Catch it where you can recover, or at the top of main.",
             narr="Bug of the Day. We throw, and nobody catches. The program ends with terminate called after throwing. "
                  "Add a try block and a catch block."),
    pun="Why did the exception get a medal? It was thrown, and someone finally caught it.",
    task="catch an out of range index", challenge="Call at with a bad index on a vector. Catch the out of range exception, and print a friendly message.",
    answer="Put the at call in a try block. Catch const out of range reference, and print your own message.",
))

EPISODES.append(dict(
    n=83, title="File input and output", spoken="file input and output", yt="C++ File I/O: ifstream and ofstream",
    thumb="FILES", vis="a notebook being written, closed and read back",
    goals=["write text to a file", "read lines from a file", "check that a file opened"],
    tags=["c++ file io", "ofstream", "ifstream", "getline", "read file"],
    analogy="a notebook you write in, close, and open again later",
    c_pts=["Ofstream writes to a file", "Ifstream reads from a file", "Always check that the file opened"],
    hook="Save data so it survives after the program ends.",
    intro="Today we save data in files. A file keeps its data after the program ends, so you can read it again later.",
    concept="Ofstream writes to a file. Ifstream reads from a file. You use them like cout and cin.\n"
            "Think of a notebook. You write in it, close it, and open it again later.",
    A=dict(file="files.cpp", label="Write then read lines", on="two lines are written to a file, then read back",
           src='''
#include <cstdio>
#include <fstream>
#include <iostream>
#include <string>
using namespace std;

int main() {
    ofstream out("notes.txt");
    out << "Asha 91\\n";
    out << "Ravi 78\\n";
    out.close();

    ifstream in("notes.txt");
    string line;
    while (getline(in, line)) {
        cout << line << endl;
    }
    in.close();
    remove("notes.txt");
    return 0;
}
''',
           narr="[HL: ofstream out(\"notes.txt\")] Ofstream opens the file for writing. It makes the file if it does not exist. [HL: out << \"Asha 91\\n\"] We write to it with the insert operator, like cout. "
                "[HL: out.close()] Close saves the data. [HL: ifstream in(\"notes.txt\")] Ifstream opens the same file for reading. [HL: while (getline(in, line))] Getline reads one line at a time. The loop stops at the end of the file. "
                "[HL: cout << line] We print Asha ninety-one, and Ravi seventy-eight. [HL: remove(\"notes.txt\")] Remove deletes the file, to keep the folder clean."),
    ill=dict(label="Stream directions", on="a table of the two stream types",
             data=table(["Stream", "Direction", "Like"], [["ofstream", "program to file", "cout"], ["ifstream", "file to program", "cin"], ["fstream", "both directions", "cin and cout"]]),
             narr="Ofstream sends data from the program to a file, like cout. Ifstream brings data from a file into the program, like cin. "
                  "Fstream can do both."),
    B=dict(file="marks.cpp", label="Read words and numbers", on="a file of names and marks is added up",
           src='''
#include <cstdio>
#include <fstream>
#include <iostream>
#include <string>
using namespace std;

int main() {
    ofstream out("marks.txt");
    out << "Asha 91 Ravi 78 Mia 85";
    out.close();

    ifstream in("marks.txt");
    string name;
    int mark = 0;
    int total = 0;
    while (in >> name >> mark) {
        total += mark;
    }
    cout << total << endl;
    in.close();
    remove("marks.txt");
    return 0;
}
''',
           narr="[HL: ofstream out(\"marks.txt\")] We write three names with marks into a file. [HL: while (in >> name >> mark)] The extraction operator reads one word and then one number. It works like cin. "
                "The loop ends when a read fails, at the end of the file. [HL: total += mark] Each mark goes into the total. [HL: cout << total] The total is ninety-one plus seventy-eight plus eighty-five, which is two hundred and fifty-four."),
    term="The program prints Asha ninety-one, Ravi seventy-eight, and then two hundred and fifty-four.",
    recap=["Ofstream writes to a file.", "Ifstream reads from a file.", "Getline reads a whole line.", "Check that the file opened."],
    bug=dict(title="A file that did not open", file="missing.cpp", kind="output", wrong_note="the code never checks that the file opened",
             wrong='''
#include <fstream>
#include <iostream>
#include <string>
using namespace std;

int main() {
    ifstream in("missing_file.txt");
    string line;
    getline(in, line);
    cout << "First line: " << line << endl;
    return 0;
}
''', fixed_note="the code checks is_open first",
             fixed='''
#include <fstream>
#include <iostream>
#include <string>
using namespace std;

int main() {
    ifstream in("missing_file.txt");
    if (!in.is_open()) {
        cout << "Cannot open missing_file.txt" << endl;
        return 0;
    }
    string line;
    getline(in, line);
    cout << "First line: " << line << endl;
    return 0;
}
''',
             why="A stream that fails to open gives no error. It reads nothing. Check is open, or the stream itself, before you read.",
             narr="Bug of the Day. The file does not exist, but the program prints First line and nothing else. No error shows up. "
                  "Always check that the file opened."),
    pun="Why did the file feel safe? Someone always closed it properly.",
    task="count the lines in a file", challenge="Write a program that saves three lines to a file. Then read them back, and print how many lines you found.",
    answer="Write the lines with ofstream. Read with getline in a loop. Add one to a counter on each pass.",
))

EPISODES.append(dict(
    n=84, title="Namespaces and organising code", spoken="namespaces and organising code", yt="C++ Namespaces and Header Files Explained",
    thumb="NAMESPACES", vis="two labelled drawers that hold tools with the same name",
    goals=["write a namespace", "avoid name clashes", "know how headers and source files work together"],
    tags=["c++ namespace", "header files", "using namespace", "multiple files", "scope resolution"],
    analogy="labelled drawers: two tools with one name, in two drawers",
    c_pts=["A namespace is a labelled drawer", "Use the double colon to open it", "A header holds declarations"],
    hook="Two functions with the same name. No clash.",
    intro="Today we organise bigger programs. Namespaces stop name clashes, and header files split code across many files.",
    concept="A namespace is a labelled drawer for names. Two drawers can each hold a function called area. You open a drawer with the double colon.\n"
            "In a bigger program, a header file holds declarations, and a source file holds the code. You compile the source files together.",
    A=dict(file="space.cpp", label="Two namespaces", on="two area functions live in two namespaces",
           src='''
#include <iostream>
using namespace std;

namespace circle {
const double pi = 3.14159;
double area(double r) {
    return pi * r * r;
}
}

namespace square {
double area(double s) {
    return s * s;
}
}

int main() {
    cout << circle::area(2) << endl;
    cout << square::area(3) << endl;
    return 0;
}
''',
           narr="[HL: namespace circle] This namespace is the circle drawer. [HL: double area(double r)] It holds an area function for a radius. [HL: namespace square] This is the square drawer. It also holds a function named area. "
                "There is no clash, because the drawers are different. [HL: circle::area(2)] The double colon opens the circle drawer. The area is twelve point five six six four. [HL: square::area(3)] This call opens the square drawer. The area is nine."),
    ill=dict(label="Two drawers", on="a table of the two namespaces and their members",
             data=table(["Namespace", "Member", "Call"], [["circle", "pi and area(r)", "circle::area(2)"], ["square", "area(s)", "square::area(3)"]]),
             narr="The circle namespace holds pi and area. The square namespace holds its own area. "
                  "The double colon tells the compiler which drawer to open."),
    B=dict(file="alias.cpp", label="Nested namespace and alias", on="a nested namespace gets a short alias",
           src='''
#include <iostream>
using namespace std;

namespace shapes::round {
double circumference(double r) {
    return 2 * 3.14159 * r;
}
}

namespace sr = shapes::round;

int main() {
    cout << sr::circumference(1) << endl;
    return 0;
}
''',
           narr="[HL: namespace shapes::round] Since C plus plus seventeen, you can write a nested namespace on one line. [HL: namespace sr = shapes::round] An alias gives a long name a short one. "
                "[HL: sr::circumference(1)] We call the function through the alias. The result is six point two eight three one eight."),
    term="The program prints twelve point five six six four, nine, and then six point two eight three one eight.",
    recap=["A namespace is a labelled drawer for names.", "Use the double colon to open a drawer.", "A header holds declarations, and a source file holds the code.", "Compile all source files together."],
    bug=dict(title="An ambiguous call", file="ambiguous.cpp", kind="compile", wrong_note="two namespaces are opened, and both hold area",
             wrong='''
#include <iostream>
using namespace std;

namespace circle {
double area(double r) { return 3.14159 * r * r; }
}

namespace square {
double area(double s) { return s * s; }
}

using namespace circle;
using namespace square;

int main() {
    cout << area(2) << endl;
    return 0;
}
''', fixed_note="the call names its namespace",
             fixed='''
#include <iostream>
using namespace std;

namespace circle {
double area(double r) { return 3.14159 * r * r; }
}

namespace square {
double area(double s) { return s * s; }
}

int main() {
    cout << square::area(2) << endl;
    return 0;
}
''',
             why="Using namespace opens the drawers, and the names clash again. Write the namespace name in front of the call, and avoid using namespace in big programs.",
             narr="Bug of the Day. We open both namespaces, and then call area. The compiler says the call is ambiguous. "
                  "Write the namespace name in front of the call."),
    pun="Why do namespaces never fight? Everyone stays in their own drawer.",
    task="make a math namespace", challenge="Write a namespace called mymath with a function square. Call it from main with the double colon.",
    answer="Write namespace mymath, and put the function inside the braces. In main, call mymath double colon square.",
))
