"""Module 8 — Templates and STL containers (EP 69-76)."""
from lib import flow, table

MODULE = {"id": 8, "name": "Templates and containers", "range": "69–76", "colours": "Lilac + Dark blue", "bg": "lilac"}
NEXT_AFTER = ("Next: EP 77 · Algorithms from the library", "We end module eight here. Next time: the algorithm library, and sorting with one line.")
EPISODES = []

EPISODES.append(dict(
    n=69, title="Function templates", spoken="function templates", yt="C++ Function Templates: One Function, Any Type",
    thumb="TEMPLATES", vis="a cookie cutter that makes any shape",
    goals=["write a function template", "let the compiler pick the type", "read a deduction error"],
    tags=["c++ templates", "function template", "typename", "generic programming"],
    analogy="a cookie cutter: one shape, any dough",
    c_pts=["A template is a recipe for functions", "T stands for any type", "The compiler writes the real function for you"],
    hook="Write one function. Use it with any type.",
    intro="Today we write code that works for any type. With one template, you replace many copies of the same function.",
    concept="A function template is a recipe. You write it once with a placeholder type, usually called T. When you call it, the compiler writes a real function for the type you used.\n"
            "This is called instantiation. Think of a cookie cutter. One shape works with any dough.",
    A=dict(file="biggest.cpp", label="One function, many types", on="biggest works for int and for double",
           src='''
#include <iostream>
using namespace std;

template <typename T>
T biggest(T a, T b) {
    return a > b ? a : b;
}

int main() {
    cout << biggest(3, 8) << endl;
    cout << biggest(2.5, 1.5) << endl;
    return 0;
}
''',
           narr="[HL: template <typename T>] This line says that T is a placeholder for a type. [HL: T biggest(T a, T b)] The function takes two values of type T, and returns a T. [HL: return a > b ? a : b] It returns the bigger one. "
                "[HL: biggest(3, 8)] The compiler sees two ints. It makes a version with T equal to int. [HL: biggest(2.5, 1.5)] Then it sees two doubles, and makes a second version. The output is eight, and two point five."),
    ill=dict(label="From template to real functions", on="a flow: template, call, deduced type, generated function",
             data=flow([("Template", "T biggest(T, T)"), ("Call", "biggest(3, 8)"), ("Deduce", "T is int"), ("Generated", "int biggest(int, int)")]),
             narr="Follow the steps. The template is the recipe. A call gives the types of the arguments. The compiler deduces T. "
                  "Then it writes a real function, made for that type."),
    B=dict(file="explicit.cpp", label="Name the type yourself", on="explicit template arguments in angle brackets",
           src='''
#include <iostream>
using namespace std;

template <typename T>
T biggest(T a, T b) {
    return a > b ? a : b;
}

int main() {
    cout << biggest<double>(3, 4.5) << endl;
    cout << biggest<string>("pear", "apple") << endl;
    return 0;
}
''',
           narr="[HL: biggest<double>(3, 4.5)] We can name the type in angle brackets. Here T is double, so the three is converted to a double. The answer is four point five. "
                "[HL: biggest<string>] Here T is string. Strings compare in alphabetical order. Pear comes after apple, so pear is bigger."),
    term="The program prints four point five, and then pear.",
    recap=["A template is a recipe for functions.", "T is a placeholder for a type.",
           "The compiler deduces T from the arguments.", "You can name the type in angle brackets."],
    bug=dict(title="Two different types", file="biggest.cpp", kind="compile", wrong_note="one argument is an int and one is a double",
             wrong='''
#include <iostream>
using namespace std;

template <typename T>
T biggest(T a, T b) {
    return a > b ? a : b;
}

int main() {
    cout << biggest(3, 4.5) << endl;
    return 0;
}
''', fixed_note="the type is named",
             fixed='''
#include <iostream>
using namespace std;

template <typename T>
T biggest(T a, T b) {
    return a > b ? a : b;
}

int main() {
    cout << biggest<double>(3, 4.5) << endl;
    return 0;
}
''',
             why="The compiler must find one T for both arguments. An int and a double give two different types, so deduction fails. Name the type yourself.",
             narr="Bug of the Day. We call biggest with an int and a double. The compiler says no matching function for call to biggest with int and double. "
                  "It must find one T for both. Name the type yourself, in angle brackets."),
    pun="I wrote a template for jokes. It works with any type of audience, but not always with the right one.",
    task="write a template for a smaller value", challenge="Write a function template called smallest. Test it with ints and with doubles.",
    answer="Write template typename T, then T smallest with two T parameters. Return a if a is less than b, otherwise b.",
))

EPISODES.append(dict(
    n=70, title="Class templates", spoken="class templates", yt="C++ Class Templates: Build Your Own Container",
    thumb="BOX<T>", vis="a labelled box that can hold anything",
    goals=["write a class template", "make objects with a type in angle brackets", "build a small stack"],
    tags=["class template", "c++ template class", "generic container", "stack class"],
    analogy="a storage box with a blank label: write int, double or string on it",
    c_pts=["A class template has a type placeholder", "You name the type when you make an object", "Each type gets its own class"],
    hook="Build your own container for any type.",
    intro="Today we build a container. With a class template, the same class can hold ints, doubles or strings.",
    concept="A class template puts a type placeholder on the whole class. When you make an object, you name the type in angle brackets. The compiler then builds a class for that type.\n"
            "The standard library containers, such as vector, are class templates. Think of a storage box with a blank label. You write int, double or string on it when you use it.",
    A=dict(file="box.cpp", label="A Box template", on="a Box holds one value of any type",
           src='''
#include <iostream>
#include <string>
using namespace std;

template <typename T>
class Box {
    T value_;

public:
    Box(T value) : value_(value) {}
    T get() const { return value_; }
};

int main() {
    Box<int> a(7);
    Box<string> b("Goa");
    cout << a.get() << " " << b.get() << endl;
    return 0;
}
''',
           narr="[HL: template <typename T>] T is the placeholder. [HL: T value_] The member has type T. [HL: Box(T value)] The constructor takes a T. [HL: T get() const] The getter returns a T. "
                "[HL: Box<int> a(7)] Here T is int. [HL: Box<string> b(] Here T is string. They are two different classes. The output is seven, and Goa."),
    ill=dict(label="One template, two classes", on="a table of the classes that the compiler builds",
             data=table(["You write", "T is", "The class holds"], [["Box<int>", "int", "one int"], ["Box<string>", "std::string", "one string"], ["Box<double>", "double", "one double"]]),
             narr="Each use of the template with a new type makes a new class. Box of int holds an int. Box of string holds a string. "
                  "They do not share anything, except the recipe."),
    B=dict(file="stack.cpp", label="A tiny stack", on="a Stack template built on a vector",
           src='''
#include <iostream>
#include <vector>
using namespace std;

template <typename T>
class Stack {
    vector<T> items_;

public:
    void push(const T& x) { items_.push_back(x); }
    T pop() {
        T x = items_.back();
        items_.pop_back();
        return x;
    }
    bool empty() const { return items_.empty(); }
};

int main() {
    Stack<int> s;
    s.push(1);
    s.push(2);
    s.push(3);
    while (!s.empty()) {
        cout << s.pop() << " ";
    }
    cout << endl;
    return 0;
}
''',
           narr="[HL: vector<T> items_] Inside, a vector of T holds the items. [HL: void push] Push adds an item at the end. [HL: T pop()] Pop removes the last item, and returns it. [HL: Stack<int> s] Here we make a stack of ints. "
                "[HL: s.push(1)] We push one, two and three. [HL: cout << s.pop()] Pop gives the last item first. The output is three, two, one."),
    term="The program prints three, two and one.",
    recap=["A class template has a type placeholder.", "Name the type in angle brackets when you make an object.",
           "Each type gets its own class.", "Library containers are class templates."],
    bug=dict(title="A missing template argument", file="box.cpp", kind="compile", wrong_note="no type is named",
             wrong='''
#include <iostream>
using namespace std;

template <typename T>
class Box {
public:
    T value;
};

int main() {
    Box b;
    cout << "made" << endl;
    return 0;
}
''', fixed_note="the type is named",
             fixed='''
#include <iostream>
using namespace std;

template <typename T>
class Box {
public:
    T value;
};

int main() {
    Box<int> b{};
    cout << b.value << endl;
    return 0;
}
''',
             why="The compiler cannot guess T when there is no constructor argument to learn it from. Write the type in angle brackets.",
             narr="Bug of the Day. We make a Box with no type. The compiler says class template argument deduction failed. "
                  "It has nothing to learn T from. Write the type in angle brackets, as in Box of int."),
    pun="My template is an open-minded class. It accepts any type, but it still wants a label.",
    task="make a Pair template", challenge="Write a class template Pair with two members of the same type T. Add a function that returns the bigger one.",
    answer="Store two T members. In the function, return the first if it is bigger than the second, otherwise the second.",
))

EPISODES.append(dict(
    n=71, title="pair and tuple", spoken="pair and tuple", yt="C++ std::pair and std::tuple",
    thumb="PAIR + TUPLE", vis="two shoes tied together, and a bundle of three",
    goals=["use std pair", "return two values from a function", "unpack with structured bindings"],
    tags=["std::pair", "std::tuple", "structured bindings", "return multiple values"],
    analogy="a pair of shoes, and a school bag with a few fixed items",
    c_pts=["A pair holds exactly two values", "A tuple holds any fixed number", "Structured bindings unpack them"],
    hook="Return two values from one function.",
    intro="Today we meet small bundles. A pair holds two values, a tuple holds more, and both are handy.",
    concept="A pair holds two values, called first and second. A tuple holds any fixed number of values of any types. Both live in the standard library.\n"
            "Since C plus plus seventeen, you can unpack them in one line with structured bindings. Think of a pair of shoes. Two items, always together.",
    A=dict(file="pair.cpp", label="A pair", on="a function returns the smallest and biggest in one pair",
           src='''
#include <iostream>
#include <utility>
using namespace std;

pair<int, int> min_max(int a, int b) {
    return a < b ? make_pair(a, b) : make_pair(b, a);
}

int main() {
    auto p = min_max(9, 4);
    cout << p.first << " " << p.second << endl;
    auto [lo, hi] = min_max(2, 7);
    cout << lo << " " << hi << endl;
    return 0;
}
''',
           narr="[HL: pair<int, int> min_max] The function returns a pair of ints. [HL: make_pair(a, b)] Make pair builds a pair from two values. [HL: auto p = min_max(9, 4)] The result goes in p. "
                "[HL: p.first] First is four, and second is nine. [HL: auto [lo, hi]] Square brackets after auto unpack the pair into two new names. [HL: cout << lo] Lo is two, and hi is seven."),
    ill=dict(label="Parts of a pair", on="a table: the pair and its two members",
             data=table(["Expression", "Value"], [["p", "pair(4, 9)"], ["p.first", "4"], ["p.second", "9"], ["auto [lo, hi] = p", "lo is 4, hi is 9"]]),
             narr="Here is the pair p. First is four, and second is nine. With a structured binding, you give the two parts their own names. "
                  "That makes the code easier to read."),
    B=dict(file="tuple.cpp", label="A tuple", on="a tuple holds a name, a mark and a pass flag",
           src='''
#include <iostream>
#include <string>
#include <tuple>
using namespace std;

int main() {
    tuple<string, int, bool> t = {"Asha", 91, true};
    cout << get<0>(t) << endl;
    auto [name, marks, passed] = t;
    cout << name << " " << marks << " " << boolalpha << passed << endl;
    return 0;
}
''',
           narr="[HL: tuple<string, int, bool> t] A tuple can hold values of different types. This one holds a string, an int and a bool. [HL: get<0>(t)] Get with an index in angle brackets reads one part. Index zero is the name. "
                "[HL: auto [name, marks, passed]] A structured binding unpacks all three parts. [HL: cout << name] The output is Asha, ninety-one, true."),
    term="The program prints Asha, and then Asha ninety-one true.",
    recap=["A pair holds two values.", "A tuple holds any fixed number of values.",
           "Use first and second for a pair.", "Structured bindings unpack a pair or a tuple."],
    bug=dict(title="A member that does not exist", file="pair.cpp", kind="compile", wrong_note="a pair has no third member",
             wrong='''
#include <iostream>
#include <utility>
using namespace std;

int main() {
    pair<int, int> p = {1, 2};
    cout << p.third << endl;
    return 0;
}
''', fixed_note="a tuple holds three values",
             fixed='''
#include <iostream>
#include <tuple>
using namespace std;

int main() {
    tuple<int, int, int> t = {1, 2, 3};
    cout << get<2>(t) << endl;
    return 0;
}
''',
             why="A pair has only first and second. For three or more values, use a tuple, or better, write a small struct with clear names.",
             narr="Bug of the Day. We ask a pair for its third member. The compiler says the pair has no member named third. "
                  "A pair holds exactly two values. For three, use a tuple, or write a small struct."),
    pun="Two values walked into a pair. They said, we are a perfect match, first and second.",
    task="return the quotient and the remainder", challenge="Write a function that returns the quotient and the remainder of two ints as a pair. Print both.",
    answer="Return make pair of a divided by b, and a remainder b. In main, print first and second.",
))

EPISODES.append(dict(
    n=72, title="std::map", spoken="std map", yt="C++ std::map: Key and Value",
    thumb="STD::MAP", vis="a phone book with names and numbers",
    goals=["store key and value pairs", "read and write with square brackets", "loop over a map in sorted order"],
    tags=["std::map", "c++ map", "key value", "associative container"],
    analogy="a phone book: look up a name, and get a number",
    c_pts=["A map stores key and value pairs", "Keys are unique and sorted", "Square brackets create a missing key"],
    hook="Look up a value by its name.",
    intro="Today we look things up by name. A map stores keys and values, and keeps the keys in sorted order.",
    concept="A map stores pairs. Each pair has a key and a value. Keys are unique, and the map keeps them sorted. You use the key to find the value.\n"
            "Square brackets read a value. But beware. If the key is missing, square brackets create it. Think of a phone book. You look up a name, and you get a number.",
    A=dict(file="phone.cpp", label="A phone book", on="a map from names to numbers",
           src='''
#include <iostream>
#include <map>
#include <string>
using namespace std;

int main() {
    map<string, int> book;
    book["Asha"] = 91;
    book["Ravi"] = 78;
    book["Asha"] = 95;
    cout << book["Asha"] << endl;
    cout << book.size() << endl;
    return 0;
}
''',
           narr="[HL: map<string, int> book] The map has string keys and int values. [HL: book[\"Asha\"] = 91] Square brackets with a key store a value. [HL: book[\"Ravi\"] = 78] A second key is added. "
                "[HL: book[\"Asha\"] = 95] Using the same key again replaces the value. [HL: cout << book[\"Asha\"]] Asha now has ninety-five. [HL: book.size()] The size is two, because keys are unique."),
    ill=dict(label="Sorted by key", on="a table: the map content in key order",
             data=table(["Key", "Value"], [["Asha", "95"], ["Ravi", "78"]]),
             narr="The map keeps the keys in sorted order. Asha comes before Ravi. Each key appears once. "
                  "The value of Asha was replaced, so the old ninety-one is gone."),
    B=dict(file="walk.cpp", label="Walk through a map", on="a range-based for gives each key and value",
           src='''
#include <iostream>
#include <map>
#include <string>
using namespace std;

int main() {
    map<string, int> book = {{"Ravi", 78}, {"Asha", 95}, {"Meera", 88}};
    for (const auto& [name, marks] : book) {
        cout << name << " " << marks << endl;
    }
    auto it = book.find("Meera");
    if (it != book.end()) {
        cout << "Found " << it->second << endl;
    }
    return 0;
}
''',
           narr="[HL: map<string, int> book =] We start the map with a list of pairs. [HL: for (const auto& [name, marks] : book)] The loop unpacks each pair into a name and marks. The order is sorted by key. Asha, Meera, then Ravi. "
                "[HL: book.find(\"Meera\")] Find looks up a key without creating it. [HL: it != book.end()] If it equals end, the key is missing. [HL: it->second] Otherwise, second is the value."),
    term="The program prints Asha, Meera and Ravi with their marks, and then Found eighty-eight.",
    recap=["A map stores key and value pairs.", "Keys are unique and sorted.",
           "Square brackets read or create a key.", "Find looks up a key without creating it."],
    bug=dict(title="A lookup that creates a key", file="phone.cpp", kind="output", wrong_note="square brackets create the missing key",
             wrong='''
#include <iostream>
#include <map>
#include <string>
using namespace std;

int main() {
    map<string, int> book;
    book["Asha"] = 91;
    if (book["Ravi"] == 0) {
        cout << "No Ravi" << endl;
    }
    cout << book.size() << endl;
    return 0;
}
''', fixed_note="count checks without creating",
             fixed='''
#include <iostream>
#include <map>
#include <string>
using namespace std;

int main() {
    map<string, int> book;
    book["Asha"] = 91;
    if (book.count("Ravi") == 0) {
        cout << "No Ravi" << endl;
    }
    cout << book.size() << endl;
    return 0;
}
''',
             why="Square brackets create a missing key with a default value. So a simple look-up grows the map. Use find or count to check.",
             narr="Bug of the Day. We only wanted to check for Ravi. But the size is two, not one. Square brackets created the key Ravi, with the value zero. "
                  "Use count or find to check without changing the map."),
    pun="My map was lost. It had all the keys, but no values.",
    task="count the marks", challenge="Make a map from names to marks. Add three students. Print the one with the highest marks.",
    answer="Loop over the map. Keep the best name and best marks. If a student has more marks than the best, replace both.",
))

EPISODES.append(dict(
    n=73, title="unordered_map", spoken="unordered map", yt="C++ unordered_map: Fast Look-Up",
    thumb="UNORDERED", vis="a pile of keys on a table",
    goals=["use unordered_map for fast look-up", "count words", "know when at throws"],
    tags=["unordered_map", "hash map c++", "word count", "map vs unordered_map"],
    analogy="a locker room: the key number takes you straight to the locker, but the lockers are not in order",
    c_pts=["It finds a key fast", "The order of the keys is not defined", "At throws an exception for a missing key"],
    hook="The fastest way to look up a key.",
    intro="Today we meet the map that trades order for speed. It is the right tool for counting and for fast look-up.",
    concept="An unordered map uses a hash table. It finds a key in about one step, even when the map is big. The price is that the keys have no order.\n"
            "It has the same functions as map. Use map when you need sorted keys. Use unordered map when you need speed. Think of a locker room. The key number takes you straight to the locker.",
    A=dict(file="count.cpp", label="Count the words", on="an unordered_map counts how many times each word appears",
           src='''
#include <iostream>
#include <sstream>
#include <string>
#include <unordered_map>
using namespace std;

int main() {
    unordered_map<string, int> counts;
    istringstream text("goa sun sea sun sand sun");
    string word;
    while (text >> word) {
        counts[word]++;
    }
    cout << counts["sun"] << " " << counts["sea"] << " " << counts.size() << endl;
    return 0;
}
''',
           narr="[HL: unordered_map<string, int> counts] The keys are words, and the values are counts. [HL: istringstream text] This stream lets us read the words of a text, one by one. [HL: while (text >> word)] The loop reads each word. "
                "[HL: counts[word]++] The first time, square brackets create the key with zero, and then plus plus makes it one. Later it counts up. [HL: cout << counts[\"sun\"]] Sun appears three times, sea once, and there are four different words."),
    ill=dict(label="Counts after the loop", on="a table: each word and its count",
             data=table(["Word", "Count"], [["goa", "1"], ["sun", "3"], ["sea", "1"], ["sand", "1"]]),
             narr="After the loop, each word has a count. Sun has three. The others have one. The table shows an example order. "
                  "A real unordered map may list them in any order, so never rely on it."),
    B=dict(file="lookup.cpp", label="Count and find", on="count and find check a key without creating it",
           src='''
#include <iostream>
#include <string>
#include <unordered_map>
using namespace std;

int main() {
    unordered_map<string, int> price = {{"fish", 120}, {"rice", 45}};
    cout << price.count("fish") << endl;
    cout << price.count("tea") << endl;
    auto it = price.find("rice");
    cout << it->second << endl;
    return 0;
}
''',
           narr="[HL: unordered_map<string, int> price] The map holds two prices. [HL: price.count(\"fish\")] Count returns one if the key exists. [HL: price.count(\"tea\")] It returns zero if it does not. [HL: price.find(\"rice\")] Find gives an iterator to the pair. "
                "[HL: it->second] The value is forty-five. Neither call changes the map."),
    term="The program prints one, zero, and forty-five.",
    recap=["An unordered map finds a key fast.", "The order of its keys is not defined.",
           "Use map when you need sorted keys.", "At throws an exception for a missing key."],
    bug=dict(title="At with a missing key", file="lookup.cpp", kind="runtime", wrong_note="at is called with a key that does not exist",
             wrong='''
#include <iostream>
#include <string>
#include <unordered_map>
using namespace std;

int main() {
    unordered_map<string, int> price = {{"fish", 120}};
    cout << price.at("tea") << endl;
    return 0;
}
''', fixed_note="the key is checked first",
             fixed='''
#include <iostream>
#include <string>
#include <unordered_map>
using namespace std;

int main() {
    unordered_map<string, int> price = {{"fish", 120}};
    if (price.count("tea") > 0) {
        cout << price.at("tea") << endl;
    } else {
        cout << "No tea" << endl;
    }
    return 0;
}
''',
             why="At checks the key, and it throws an exception when the key is missing. Check with count first, or catch the exception.",
             narr="Bug of the Day. We call at with a key that is not in the map. The program stops. It says terminate called after throwing an instance of out of range. "
                  "At is the safe way, because it tells you about the problem. Check with count first."),
    pun="The hash map said, I do not care about order. I only care that you find me fast.",
    task="count letters", challenge="Count how often each letter appears in the word Konkani. Print the count of the letter n.",
    answer="Loop over the letters. Add one to counts at the letter. Print counts of the letter n, which is two.",
))

EPISODES.append(dict(
    n=74, title="set and unordered_set", spoken="set and unordered set", yt="C++ std::set: Unique and Sorted",
    thumb="SETS", vis="a bag where every item is different",
    goals=["store unique values", "see that a set sorts its items", "check if an insert worked"],
    tags=["std::set", "unordered_set", "unique values", "remove duplicates"],
    analogy="a guest list: every name appears once, and the clerk keeps it in order",
    c_pts=["A set stores each value once", "A set keeps its values sorted", "Insert tells you if it added a new value"],
    hook="Remove every duplicate in one line.",
    intro="Today we meet the set. It stores each value once. It is the quickest way to remove duplicates.",
    concept="A set stores unique values. If you insert a value twice, the second insert does nothing. A set keeps its values sorted. An unordered set is faster, but it has no order.\n"
            "Insert returns a pair. The second part tells you if the value was new. Think of a guest list. Every name appears once, and the clerk keeps it in order.",
    A=dict(file="unique.cpp", label="A set of numbers", on="a set removes duplicates and sorts",
           src='''
#include <iostream>
#include <set>
#include <vector>
using namespace std;

int main() {
    vector<int> v = {5, 3, 5, 1, 3, 9};
    set<int> s(v.begin(), v.end());
    for (int x : s) {
        cout << x << " ";
    }
    cout << endl;
    cout << s.size() << endl;
    return 0;
}
''',
           narr="[HL: vector<int> v] The vector has six numbers, with duplicates. [HL: set<int> s(v.begin(), v.end())] We build a set from the whole vector. Duplicates disappear. [HL: for (int x : s)] The loop prints the values in sorted order. "
                "[HL: cout << s.size()] The output is one, three, five, nine, and the size is four."),
    ill=dict(label="From a vector to a set", on="a flow: vector with duplicates, set builds, sorted unique values",
             data=flow([("Vector", "5 3 5 1 3 9"), ("Build a set", "Each value once"), ("Sorted", "1 3 5 9"), ("Size", "4")]),
             narr="The vector has six items. The set keeps each value once, and in order. That leaves four items. "
                  "This is the shortest way to remove duplicates."),
    B=dict(file="insert.cpp", label="Did the insert work?", on="insert returns a pair with a flag",
           src='''
#include <iostream>
#include <set>
using namespace std;

int main() {
    set<int> s;
    auto first = s.insert(4);
    auto second = s.insert(4);
    cout << boolalpha << first.second << " " << second.second << endl;
    cout << s.count(4) << " " << s.count(7) << endl;
    return 0;
}
''',
           narr="[HL: s.insert(4)] The first insert adds four. [HL: second = s.insert(4)] The second insert finds four already there. [HL: first.second] The second part of the result is a flag. The first flag is true, and the second is false. "
                "[HL: s.count(4)] Count tells us if a value is in the set. Four is there, so one. [HL: s.count(7)] Seven is not, so zero."),
    term="The program prints true false, and then one zero.",
    recap=["A set stores each value once.", "A set keeps its values sorted.",
           "Insert tells you if the value was new.", "Count checks if a value is in the set."],
    bug=dict(title="Expecting duplicates", file="unique.cpp", kind="output", wrong_note="the code expects six items",
             wrong='''
#include <iostream>
#include <set>
using namespace std;

int main() {
    set<int> votes;
    int ballots[6] = {2, 1, 2, 2, 1, 3};
    for (int b : ballots) {
        votes.insert(b);
    }
    cout << "Total votes: " << votes.size() << endl;
    return 0;
}
''', fixed_note="a vector counts every ballot",
             fixed='''
#include <iostream>
#include <vector>
using namespace std;

int main() {
    vector<int> votes;
    int ballots[6] = {2, 1, 2, 2, 1, 3};
    for (int b : ballots) {
        votes.push_back(b);
    }
    cout << "Total votes: " << votes.size() << endl;
    return 0;
}
''',
             why="A set keeps each value once, so it counts the different values, not the total. To count every item, use a vector.",
             narr="Bug of the Day. We count six ballots, but the program says three. A set keeps each value once. It counts the different candidates, not the votes. "
                  "Use a vector, or a map of counts, when duplicates matter."),
    pun="A set told a joke twice. Nobody heard it the second time.",
    task="remove the duplicates from a vector", challenge="Read five numbers into a vector. Print them without duplicates, in sorted order.",
    answer="Build a set from the vector. Print every item of the set with a range-based for.",
))

EPISODES.append(dict(
    n=75, title="stack, queue and deque", spoken="stack, queue and deque", yt="C++ stack, queue and deque",
    thumb="STACK / QUEUE", vis="a pile of plates and a line of people",
    goals=["use a stack, last in first out", "use a queue, first in first out", "know what a deque is"],
    tags=["std::stack", "std::queue", "deque", "lifo fifo"],
    analogy="a pile of plates, and a line at the ration shop",
    c_pts=["A stack is last in, first out", "A queue is first in, first out", "A deque works at both ends"],
    hook="Last in, first out. First in, first out.",
    intro="Today we meet two simple containers with strict rules. One is a pile of plates, and the other is a queue at a shop.",
    concept="A stack is last in, first out. You push on top, and you pop from the top. A queue is first in, first out. You push at the back, and you pop from the front.\n"
            "A deque lets you push and pop at both ends. Think of a pile of plates for the stack, and a line at the ration shop for the queue.",
    A=dict(file="stack.cpp", label="A stack", on="push three, pop three, and see the order",
           src='''
#include <iostream>
#include <stack>
using namespace std;

int main() {
    stack<int> s;
    s.push(1);
    s.push(2);
    s.push(3);
    cout << s.top() << endl;
    s.pop();
    cout << s.top() << endl;
    cout << s.size() << endl;
    return 0;
}
''',
           narr="[HL: s.push(1)] We push one, two and three. The last one is on top. [HL: cout << s.top()] Top shows three, without removing it. [HL: s.pop()] Pop removes the top item. It gives nothing back. "
                "[HL: cout << s.top()] Now the top is two. [HL: cout << s.size()] Two items remain."),
    ill=dict(label="Stack and queue", on="a table that compares the two",
             data=table(["Container", "Add at", "Remove from", "Order"], [["stack", "top", "top", "last in, first out"], ["queue", "back", "front", "first in, first out"], ["deque", "both ends", "both ends", "your choice"]]),
             narr="The table compares the three. A stack adds and removes at the top. A queue adds at the back, and removes from the front. "
                  "A deque can do both at either end."),
    B=dict(file="queue.cpp", label="A queue", on="first in, first out",
           src='''
#include <iostream>
#include <queue>
#include <string>
using namespace std;

int main() {
    queue<string> q;
    q.push("Asha");
    q.push("Ravi");
    q.push("Meera");
    cout << q.front() << endl;
    q.pop();
    cout << q.front() << " " << q.back() << endl;
    return 0;
}
''',
           narr="[HL: q.push(\"Asha\")] Asha joins the queue first. [HL: q.push(\"Meera\")] Meera joins last. [HL: cout << q.front()] Front shows Asha, the first in line. [HL: q.pop()] Pop removes Asha. "
                "[HL: cout << q.front() << \" \" << q.back()] Now Ravi is at the front, and Meera is at the back."),
    term="The program prints Asha, and then Ravi Meera.",
    recap=["A stack is last in, first out.", "A queue is first in, first out.",
           "Top and front only look. Pop removes.", "A deque works at both ends."],
    bug=dict(title="Expecting pop to return the item", file="stack.cpp", kind="compile", wrong_note="pop is used to get the value",
             wrong='''
#include <iostream>
#include <stack>
using namespace std;

int main() {
    stack<int> s;
    s.push(5);
    int x = s.pop();
    cout << x << endl;
    return 0;
}
''', fixed_note="top reads, and pop removes",
             fixed='''
#include <iostream>
#include <stack>
using namespace std;

int main() {
    stack<int> s;
    s.push(5);
    int x = s.top();
    s.pop();
    cout << x << endl;
    return 0;
}
''',
             why="Pop returns nothing. This design keeps the stack safe when an exception happens. Read with top first, then pop.",
             narr="Bug of the Day. We store the result of pop in an int. The compiler says void value not ignored as it ought to be. "
                  "Pop returns nothing. First read with top, then remove with pop."),
    pun="The stack was proud. It said, I am always on top of things.",
    task="reverse a word with a stack", challenge="Use a stack of chars to reverse the word Goa. Push each letter, then pop them all.",
    answer="Push G, o and a. Then pop and print until the stack is empty. The output is aoG.",
))

EPISODES.append(dict(
    n=76, title="Iterators", spoken="iterators", yt="C++ Iterators: begin, end and More",
    thumb="ITERATORS", vis="a crab walking along any container",
    goals=["walk a container with begin and end", "use reverse iterators", "avoid skipping items when you erase"],
    tags=["c++ iterators", "begin end", "reverse iterator", "erase in loop"],
    analogy="a finger on a train timetable: it points to one line, and moves to the next",
    c_pts=["An iterator points at one item", "Star reads the item, plus plus moves on", "End is one past the last item"],
    hook="One way to walk any container.",
    intro="Today we learn the idea behind every loop in the library. An iterator is like a pointer for a container.",
    concept="An iterator points at one item in a container. Star reads the item. Plus plus moves to the next one. Begin points at the first item. End points one past the last item. You stop when you reach end.\n"
            "The same code works for vector, list, set and map. Think of a finger on a train timetable. It points at one line, and moves to the next.",
    A=dict(file="iter.cpp", label="Walk with an iterator", on="a for loop with begin and end",
           src='''
#include <iostream>
#include <vector>
using namespace std;

int main() {
    vector<int> v = {10, 20, 30};
    for (auto it = v.begin(); it != v.end(); ++it) {
        cout << *it << " ";
    }
    cout << endl;
    for (auto it = v.rbegin(); it != v.rend(); ++it) {
        cout << *it << " ";
    }
    cout << endl;
    return 0;
}
''',
           narr="[HL: auto it = v.begin()] The iterator starts at the first item. [HL: it != v.end()] The loop stops when it reaches end. [HL: ++it] Plus plus moves to the next item. [HL: cout << *it] Star reads the item. "
                "[HL: auto it = v.rbegin()] Rbegin starts at the last item. [HL: it != v.rend()] Rend marks the position before the first. Plus plus moves backwards. The output is thirty, twenty, ten."),
    ill=dict(label="Begin and end", on="a table: positions of begin and end",
             data=table(["Position", "Points at"], [["v.begin()", "10"], ["v.begin() + 1", "20"], ["v.begin() + 2", "30"], ["v.end()", "one past the last item"]]),
             narr="Begin points at ten. Begin plus one points at twenty. Begin plus two points at thirty. "
                  "End points one past the last item. You never read from end. You only compare against it."),
    B=dict(file="advance.cpp", label="Move an iterator", on="next and distance help with iterators",
           src='''
#include <iostream>
#include <iterator>
#include <list>
using namespace std;

int main() {
    list<int> items = {4, 8, 15, 16};
    auto it = next(items.begin(), 2);
    cout << *it << endl;
    cout << distance(items.begin(), it) << endl;
    return 0;
}
''',
           narr="[HL: list<int> items] A list is not an array. You cannot write begin plus two. [HL: next(items.begin(), 2)] Next moves an iterator forward by a number of steps. It works for every container. "
                "[HL: cout << *it] The item is fifteen. [HL: distance(items.begin(), it)] Distance counts the steps between two iterators. The answer is two."),
    term="The program prints fifteen, and then two.",
    recap=["An iterator points at one item.", "Star reads, and plus plus moves on.",
           "End is one past the last item.", "The same loop works for every container."],
    bug=dict(title="Erasing and skipping", file="erase.cpp", kind="output", wrong_note="the loop moves on after every erase",
             wrong='''
#include <iostream>
#include <vector>
using namespace std;

int main() {
    vector<int> v = {2, 4, 6, 7};
    for (auto it = v.begin(); it != v.end(); ++it) {
        if (*it % 2 == 0) {
            it = v.erase(it);
        }
    }
    for (int x : v) {
        cout << x << " ";
    }
    cout << endl;
    return 0;
}
''', fixed_note="the loop moves on only when nothing is erased",
             fixed='''
#include <iostream>
#include <vector>
using namespace std;

int main() {
    vector<int> v = {2, 4, 6, 7};
    for (auto it = v.begin(); it != v.end();) {
        if (*it % 2 == 0) {
            it = v.erase(it);
        } else {
            ++it;
        }
    }
    for (int x : v) {
        cout << x << " ";
    }
    cout << endl;
    return 0;
}
''',
             why="Erase returns the iterator of the next item. The loop then moves on again, and skips that item. Move on only in the else branch.",
             narr="Bug of the Day. We erase all even numbers, but four stays in the vector. Erase already returns the next item. "
                  "Then the loop moves on again, and skips it. Move the iterator only when you did not erase."),
    pun="Why did the iterator never get lost? It always knew where end was.",
    task="remove all negative numbers", challenge="Write a loop with iterators that removes all negative numbers from a vector. Do not skip any item.",
    answer="Use a for loop with no step. If the item is negative, set it to the result of erase. Otherwise, move it on.",
))
