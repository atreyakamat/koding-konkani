"""Module 6 — Classes and objects (EP 51-60)."""
from lib import flow, mem, table

MODULE = {"id": 6, "name": "Classes and objects", "range": "51–60", "colours": "Peach + Dark blue", "bg": "peach"}
NEXT_AFTER = ("Next: EP 61 · Inheritance", "We end module six here. Next time: inheritance, where one class builds on another.")
EPISODES = []

EPISODES.append(dict(
    n=51, title="Structs", spoken="structs", yt="C++ Structs: Group Your Data",
    thumb="STRUCTS", vis="a student ID card with name and marks",
    goals=["define a struct with several fields", "make and fill a struct variable", "pass a struct to a function"],
    tags=["c++ struct", "struct vs class", "user defined type", "dot operator"],
    analogy="an ID card: one card, many fields",
    c_pts=["A struct groups related variables", "Each variable is a field", "The dot reaches a field"],
    hook="One variable, many fields.",
    intro="Today we make our own type. A struct groups related data, like the fields on an ID card.",
    concept="A struct groups related variables under one name. Each variable inside is a field. You define the struct once, and then you make as many variables of it as you like.\n"
            "The dot operator reaches one field. Think of an ID card. It is one card, but it holds a name, a class and a number.",
    A=dict(file="student.cpp", label="A student struct", on="a struct with a name and marks",
           src='''
#include <iostream>
#include <string>
using namespace std;

struct Student {
    string name;
    int marks;
};

int main() {
    Student s;
    s.name = "Asha";
    s.marks = 91;
    cout << s.name << " scored " << s.marks << endl;
    return 0;
}
''',
           narr="[HL: struct Student] The struct has a name for the new type. [HL: string name] The first field is a string. [HL: int marks] The second field is an int. [HL: };] Do not forget the semicolon after the closing brace. "
                "[HL: Student s;] Here we make a variable of the new type. [HL: s.name = ] The dot reaches a field. We set the name. [HL: s.marks = ] Then we set the marks. [HL: cout << s.name] We print both fields."),
    ill=dict(label="Fields in memory", on="the struct s holds two fields, side by side",
             data=mem([("s.name", "std::string", "Asha"), ("s.marks", "int", "91")], caption="The fields of one struct sit next to each other in memory"),
             narr="Look at the struct in memory. It has two fields. The name sits first, and the marks come next. "
                  "The compiler may add small gaps between fields, to keep them aligned."),
    B=dict(file="list.cpp", label="A struct in a function", on="a function takes a struct by const reference",
           src='''
#include <iostream>
#include <string>
using namespace std;

struct Student {
    string name;
    int marks;
};

void show(const Student& s) {
    cout << s.name << ": " << s.marks << endl;
}

int main() {
    Student a = {"Asha", 91};
    Student b = {"Ravi", 78};
    show(a);
    show(b);
    return 0;
}
''',
           narr="[HL: void show] The function takes a const reference, as in episode twenty-five. No copy is made. [HL: Student a = ] Braces fill the fields in order. Asha gets the name, and ninety-one gets the marks. "
                "[HL: Student b = ] Ravi has seventy-eight. [HL: show(a)] We call show for each student. The output has two lines."),
    term="The program prints Asha colon ninety-one, and then Ravi colon seventy-eight.",
    recap=["A struct groups related variables.", "Each variable inside is a field.",
           "The dot operator reaches a field.", "Pass a big struct by const reference."],
    bug=dict(title="A missing semicolon after a struct", file="student.cpp", kind="compile", wrong_note="the struct has no semicolon after its brace",
             wrong='''
#include <iostream>
#include <string>
using namespace std;

struct Student {
    string name;
    int marks;
}

int main() {
    Student s;
    s.marks = 91;
    cout << s.marks << endl;
    return 0;
}
''', fixed_note="the semicolon is back",
             fixed='''
#include <iostream>
#include <string>
using namespace std;

struct Student {
    string name;
    int marks;
};

int main() {
    Student s;
    s.marks = 91;
    cout << s.marks << endl;
    return 0;
}
''',
             why="A struct definition is a declaration, and every declaration ends with a semicolon. The compiler reads on and gets confused.",
             narr="Bug of the Day. The struct has no semicolon after its closing brace. The compiler says expected semicolon after struct definition. "
                  "A struct is a declaration, so it needs a semicolon. This is one of the most common beginner errors."),
    pun="I made a struct for my fish. It has two fields: name and price. The price is always a catch.",
    task="make a book struct", challenge="Make a struct called Book with a title and a price. Make two books and print them with a function.",
    answer="Define struct Book with a string and a double. Write a show function with a const reference. Call it for both books.",
))

EPISODES.append(dict(
    n=52, title="Classes and objects", spoken="classes and objects", yt="C++ Classes and Objects for Beginners",
    thumb="CLASSES", vis="a blueprint and a house built from it",
    goals=["define a class with private data and public functions", "make objects from a class", "explain public and private"],
    tags=["c++ class", "object oriented programming", "public private", "member function"],
    analogy="a blueprint and the houses built from it",
    c_pts=["A class is a blueprint", "An object is one thing built from it", "Private data is hidden, public functions are open"],
    hook="Hide the data. Show only the buttons.",
    intro="Today we meet classes. A class bundles data and the functions that work on it, and it hides the data from the outside.",
    concept="A class is a blueprint. An object is one thing built from the blueprint. A class has data and member functions.\n"
            "Data is private by default. Only the class itself can touch it. The public functions are the buttons that everyone may press. Think of a lift. You press a button, but you never touch the motor.",
    A=dict(file="counter.cpp", label="A Counter class", on="a class with private data and public functions",
           src='''
#include <iostream>
using namespace std;

class Counter {
    int count_ = 0;

public:
    void increment() { count_++; }
    int get() const { return count_; }
};

int main() {
    Counter c;
    c.increment();
    c.increment();
    cout << c.get() << endl;
    return 0;
}
''',
           narr="[HL: class Counter] This is the class. [HL: int count_] The data is private by default. The trailing underscore is a habit that marks member data. [HL: public:] Everything below this label is open to all. "
                "[HL: void increment] This function adds one. [HL: int get() const] This function reads the value. [HL: Counter c;] Here we make one object. [HL: c.increment();] We press the button twice. [HL: cout << c.get()] The count is two."),
    ill=dict(label="Public and private", on="a table of what code outside the class may do",
             data=table(["Member", "Access", "Outside code may"], [["count_", "private", "not touch it"], ["increment()", "public", "call it"], ["get()", "public", "call it"]]),
             narr="The table shows the rule. Count is private, so outside code cannot touch it. Increment and get are public, so anyone may call them. "
                  "This protects the data. Only the class decides how it changes."),
    B=dict(file="twocounters.cpp", label="Two objects", on="each object has its own data",
           src='''
#include <iostream>
using namespace std;

class Counter {
    int count_ = 0;

public:
    void increment() { count_++; }
    int get() const { return count_; }
};

int main() {
    Counter a, b;
    a.increment();
    a.increment();
    b.increment();
    cout << a.get() << " " << b.get() << endl;
    return 0;
}
''',
           narr="[HL: Counter a, b] We make two objects from one class. [HL: a.increment();] Each object has its own count. We add one twice to a. [HL: b.increment();] We add one to b once. "
                "[HL: cout << a.get()] A has two, and b has one. The objects do not affect each other."),
    term="The program prints two and one.",
    recap=["A class is a blueprint, and an object is one thing built from it.", "Data is private by default.",
           "Public member functions are the buttons.", "Each object has its own data."],
    bug=dict(title="Touching private data", file="counter.cpp", kind="compile", wrong_note="main reads a private member",
             wrong='''
#include <iostream>
using namespace std;

class Counter {
    int count_ = 0;

public:
    void increment() { count_++; }
};

int main() {
    Counter c;
    c.count_ = 5;
    cout << "done" << endl;
    return 0;
}
''', fixed_note="main uses the public function",
             fixed='''
#include <iostream>
using namespace std;

class Counter {
    int count_ = 0;

public:
    void increment() { count_++; }
};

int main() {
    Counter c;
    c.increment();
    cout << "done" << endl;
    return 0;
}
''',
             why="Private data is only for the class. Outside code must use the public functions.",
             narr="Bug of the Day. Main tries to set the private count. The compiler says count is private within this context. "
                  "That is the whole point of private. Use a public function, such as increment, instead."),
    pun="I tried to read my class private data. It said, mind your own members.",
    task="build a Light class", challenge="Write a class called Light with a private bool on. Add public functions turn on, turn off, and is on.",
    answer="Keep the bool private. The functions set it to true or false, and is on returns it. Mark is on as const.",
))

EPISODES.append(dict(
    n=53, title="Constructors", spoken="constructors", yt="C++ Constructors: Start Every Object Right",
    thumb="CONSTRUCTORS", vis="a factory that builds a ready toy",
    goals=["write a constructor", "write several constructors", "explain the default constructor"],
    tags=["c++ constructor", "default constructor", "constructor overloading", "object initialization"],
    analogy="a new phone: it comes ready, with the setup already done",
    c_pts=["A constructor runs when an object is made", "It has the class name and no return type", "A class can have several constructors"],
    hook="Make every object ready from the first moment.",
    intro="Today we make objects that start in a good state. A constructor runs the moment an object is born.",
    concept="A constructor is a special function. It has the same name as the class, and it has no return type. It runs when an object is made.\n"
            "A class can have several constructors with different parameters. If you write none, the compiler gives you an empty default one. If you write any, it does not. Think of a new phone that comes with the setup already done.",
    A=dict(file="point.cpp", label="Constructors", on="a Point class with two constructors",
           src='''
#include <iostream>
using namespace std;

class Point {
    int x_, y_;

public:
    Point() : x_(0), y_(0) {}
    Point(int x, int y) : x_(x), y_(y) {}
    void show() const { cout << x_ << "," << y_ << endl; }
};

int main() {
    Point origin;
    Point p(3, 4);
    origin.show();
    p.show();
    return 0;
}
''',
           narr="[HL: Point() :] This is the default constructor. It sets both numbers to zero. [HL: Point(int x, int y)] This constructor takes two values. [HL: void show] The show function prints the point. "
                "[HL: Point origin;] This object uses the default constructor. [HL: Point p(3, 4);] This object uses the second one. [HL: origin.show()] The first prints zero, zero. [HL: p.show()] The second prints three, four."),
    ill=dict(label="Which constructor runs?", on="a table of declarations and the constructor that runs",
             data=table(["Code", "Constructor", "x_ and y_"], [["Point a;", "Point()", "0, 0"], ["Point b(3, 4);", "Point(int, int)", "3, 4"], ["Point c{5, 6};", "Point(int, int)", "5, 6"]]),
             narr="The compiler chooses a constructor by the arguments. No arguments means the default one. Two ints mean the second one. "
                  "Round brackets and curly braces both work."),
    B=dict(file="defaults.cpp", label="Default arguments", on="one constructor with default values replaces two",
           src='''
#include <iostream>
#include <string>
using namespace std;

class Pet {
    string name_;
    int age_;

public:
    Pet(string name = "Unknown", int age = 1) : name_(name), age_(age) {}
    void show() const { cout << name_ << " " << age_ << endl; }
};

int main() {
    Pet a;
    Pet b("Moti");
    Pet c("Kali", 4);
    a.show();
    b.show();
    c.show();
    return 0;
}
''',
           narr="[HL: Pet(string name] One constructor has two default values. [HL: Pet a;] No arguments: the name is Unknown and the age is one. [HL: Pet b(] One argument: the age is still one. "
                "[HL: Pet c(] Two arguments: both defaults are replaced. The output has three lines."),
    term="The program prints Unknown one, Moti one, and Kali four.",
    recap=["A constructor runs when an object is made.", "It has the class name and no return type.",
           "A class can have several constructors.", "Default arguments can replace several constructors."],
    bug=dict(title="No default constructor", file="point.cpp", kind="compile", wrong_note="only a two-value constructor exists",
             wrong='''
#include <iostream>
using namespace std;

class Point {
    int x_, y_;

public:
    Point(int x, int y) : x_(x), y_(y) {}
    int sum() const { return x_ + y_; }
};

int main() {
    Point p;
    cout << p.sum() << endl;
    return 0;
}
''', fixed_note="a default constructor is added",
             fixed='''
#include <iostream>
using namespace std;

class Point {
    int x_, y_;

public:
    Point() : x_(0), y_(0) {}
    Point(int x, int y) : x_(x), y_(y) {}
    int sum() const { return x_ + y_; }
};

int main() {
    Point p;
    cout << p.sum() << endl;
    return 0;
}
''',
             why="When you write any constructor, the compiler stops making the empty default one. Write your own if you need it.",
             narr="Bug of the Day. The class has only a two-value constructor. Main makes a point with no values. The compiler says no matching function for call to Point. "
                  "When you write any constructor, the free default one disappears. Add your own."),
    pun="The constructor told the object, do not worry. I will get you started.",
    task="write a Rectangle constructor", challenge="Write a class called Rectangle with width and height. Add a constructor with two values and a function that returns the area.",
    answer="Keep the two numbers private. The constructor stores them. The area function returns width times height.",
))

EPISODES.append(dict(
    n=54, title="Member initializer lists", spoken="member initializer lists", yt="C++ Member Initializer Lists",
    thumb="INIT LISTS", vis="a checklist stuck to a toolbox",
    goals=["write a member initializer list", "explain why const members need it", "avoid the order warning"],
    tags=["member initializer list", "constructor init list", "const member", "wreorder"],
    analogy="a school bag checklist: pack things in the order of the list on the door",
    c_pts=["The list runs before the constructor body", "Const and reference members must use it", "Members start in the order they are declared"],
    hook="Initialize before the body runs.",
    intro="Today we learn the right way to set up members. The colon list runs before the body, and some members need it.",
    concept="A member initializer list sits after the constructor brackets. It starts with a colon. It builds each member directly, before the body runs.\n"
            "Const members and reference members must use it. Members are always built in the order of their declaration, not in the order of your list. Think of a school bag. You pack in the order of the checklist on the door.",
    A=dict(file="initlist.cpp", label="An initializer list", on="a constructor sets two members before its body runs",
           src='''
#include <iostream>
#include <string>
using namespace std;

class Book {
    string title_;
    int pages_;

public:
    Book(string title, int pages) : title_(title), pages_(pages) {
        cout << "Book made" << endl;
    }
    void show() const { cout << title_ << " " << pages_ << endl; }
};

int main() {
    Book b("Goa Tales", 120);
    b.show();
    return 0;
}
''',
           narr="[HL: Book(string title] The colon starts the initializer list. [HL: title_(title)] Each entry names a member, and gives it a value in round brackets. [HL: cout << \"Book made\"] The body runs after the list. "
                "[HL: Book b(] We make a book. The list runs first, then the body prints Book made. [HL: b.show()] Then show prints the title and the pages."),
    ill=dict(label="Order of events", on="a flow: list, body, object ready",
             data=flow([("Members built", "In declaration order"), ("List values", "title_ and pages_ get values"), ("Body runs", "Prints Book made"), ("Object ready", "Use it")]),
             narr="Follow the order. First, the members are built. They get the values from the list. Then the body runs. "
                  "Only then is the object ready for use."),
    B=dict(file="constmember.cpp", label="A const member", on="a const member can only be set by the list",
           src='''
#include <iostream>
using namespace std;

class Ticket {
    const int id_;
    int price_;

public:
    Ticket(int id, int price) : id_(id), price_(price) {}
    void show() const { cout << id_ << " " << price_ << endl; }
};

int main() {
    Ticket t(101, 50);
    t.show();
    return 0;
}
''',
           narr="[HL: const int id_] The id is const. It must never change. [HL: id_(id)] A const member can only get its value in the list. Setting it in the body is too late. "
                "[HL: Ticket t(101, 50)] We make a ticket with id one hundred and one, and price fifty. [HL: t.show()] The output shows both numbers."),
    term="The program prints one hundred one, then fifty.",
    recap=["The initializer list sits between the colon and the body.", "It builds each member directly.",
           "Const and reference members must use the list.", "Members are built in declaration order."],
    bug=dict(title="A list in the wrong order", file="initlist.cpp", kind="warn", wrong_note="the list order differs from the declaration order",
             wrong='''
#include <iostream>
using namespace std;

class Pair {
    int first_;
    int second_;

public:
    Pair(int a, int b) : second_(b), first_(a) {}
    int sum() const { return first_ + second_; }
};

int main() {
    Pair p(1, 2);
    cout << p.sum() << endl;
    return 0;
}
''', fixed_note="the list follows the declaration order",
             fixed='''
#include <iostream>
using namespace std;

class Pair {
    int first_;
    int second_;

public:
    Pair(int a, int b) : first_(a), second_(b) {}
    int sum() const { return first_ + second_; }
};

int main() {
    Pair p(1, 2);
    cout << p.sum() << endl;
    return 0;
}
''',
             why="The compiler builds members in the order of the declaration. A list in a different order is misleading, and it can cause real bugs.",
             narr="Bug of the Day. The list names second before first. But members are always built in the order of the declaration. "
                  "The compiler warns about the wrong order. Write the list in the same order as the members."),
    pun="The initializer list is like a packing list. It never lets the constructor forget its socks.",
    task="use an initializer list with a const", challenge="Write a class called Student with a const roll number and a name. Use an initializer list.",
    answer="Declare a const int for the roll number and a string for the name. In the constructor, write a colon, then each member with its value in round brackets.",
))

EPISODES.append(dict(
    n=55, title="Destructors", spoken="destructors", yt="C++ Destructors: Clean Up After Yourself",
    thumb="DESTRUCTORS", vis="a crab switching off the lights",
    goals=["write a destructor", "free heap memory in a destructor", "predict the order of destruction"],
    tags=["c++ destructor", "raii class", "object lifetime", "cleanup"],
    analogy="a hotel check-out: the room is cleaned in the reverse order of the check-in",
    c_pts=["A destructor has a tilde and the class name", "It runs when the object dies", "Objects die in reverse order"],
    hook="Objects die in the reverse order of birth.",
    intro="Today we write the last function of an object. The destructor runs when the object dies, and it cleans up.",
    concept="A destructor has a tilde, then the class name. It has no parameters and no return type. It runs when the object goes out of scope.\n"
            "Use it to free memory, close files and release other resources. Objects die in the reverse order of their birth. Think of a hotel. The last guest to arrive is the first to leave.",
    A=dict(file="buffer.cpp", label="A destructor that frees memory", on="a class owns a heap array and frees it",
           src='''
#include <iostream>
using namespace std;

class Buffer {
    int* data_;
    int size_;

public:
    Buffer(int size) : data_(new int[size]), size_(size) {
        cout << "made " << size_ << endl;
    }
    ~Buffer() {
        delete[] data_;
        cout << "freed" << endl;
    }
};

int main() {
    Buffer b(4);
    cout << "using it" << endl;
    return 0;
}
''',
           narr="[HL: int* data_] The class owns a heap array. [HL: new int[size]] The constructor asks for the memory. [HL: ~Buffer()] The destructor has a tilde in front of the name. [HL: delete[] data_] It gives the memory back. "
                "[HL: Buffer b(4)] Main makes one buffer. Made four prints. [HL: using it] Then using it prints. [HL: return 0] At the end of main, b dies, and freed prints."),
    ill=dict(label="Heap memory owned by an object", on="the object on the stack owns an array on the heap",
             data=mem([("b.data_", "int*", None, "stack"), ("b.size_", "int", "4", "stack"), ("items", "int[4]", "0, 0, 0, 0", "heap")], arrows=[("b.data_", "items[0]", "owns")], caption="The destructor deletes the heap array when b dies"),
             narr="Look at the object b. It has a pointer and a size. The pointer owns four boxes on the heap. "
                  "When b dies, the destructor frees them. The user of the class does not need to remember anything."),
    B=dict(file="order.cpp", label="Order of destruction", on="the last object made is the first to die",
           src='''
#include <iostream>
#include <string>
using namespace std;

class Tag {
    string name_;

public:
    Tag(string name) : name_(name) { cout << "hello " << name_ << endl; }
    ~Tag() { cout << "bye " << name_ << endl; }
};

int main() {
    Tag a("A");
    Tag b("B");
    Tag c("C");
    return 0;
}
''',
           narr="[HL: Tag a(] Three tags are made in the order A, B, C. Each prints hello. [HL: ~Tag()] At the end of main, the destructors run. "
                "They run in the reverse order. C dies first, then B, then A. The output ends with bye C, bye B, bye A."),
    term="The program prints three hello lines, and then bye C, bye B and bye A.",
    recap=["A destructor has a tilde and the class name.", "It runs when the object dies.",
           "Free memory and other resources in it.", "Objects die in the reverse order of their birth."],
    bug=dict(title="A destructor with a parameter", file="buffer.cpp", kind="compile", wrong_note="the destructor takes a parameter",
             wrong='''
#include <iostream>
using namespace std;

class Buffer {
public:
    ~Buffer(int code) { cout << code << endl; }
};

int main() {
    Buffer b;
    return 0;
}
''', fixed_note="the destructor has no parameter",
             fixed='''
#include <iostream>
using namespace std;

class Buffer {
public:
    ~Buffer() { cout << "freed" << endl; }
};

int main() {
    Buffer b;
    return 0;
}
''',
             why="Nobody can pass an argument to a destructor, because it runs by itself. A class has exactly one destructor with no parameters.",
             narr="Bug of the Day. The destructor takes an int. The compiler says destructors may not have parameters. "
                  "A destructor runs by itself, so nobody could pass an argument. Remove the parameter."),
    pun="The destructor never gets invited to the party. It only comes at the end to clean up.",
    task="watch the order of destruction", challenge="Make a class that prints in its constructor and its destructor. Make two objects in main. Predict the output before you run it.",
    answer="Two hello lines come first. Then the destructors run in the reverse order, so the second object says bye first.",
))

EPISODES.append(dict(
    n=56, title="Encapsulation", spoken="encapsulation", yt="C++ Encapsulation: Getters, Setters and Safe Data",
    thumb="ENCAPSULATION", vis="a bank vault with a small window for deposits",
    goals=["hide data and offer safe functions", "validate input in a setter", "keep a class in a valid state"],
    tags=["encapsulation c++", "getter setter", "data hiding", "class invariant"],
    analogy="a bank counter: you cannot reach the vault, but the clerk checks every deposit",
    c_pts=["Keep data private", "Offer public functions that check the input", "The class keeps itself valid"],
    hook="A class can protect its own rules.",
    intro="Today we see why classes hide their data. The class checks every change, so it never ends up in a bad state.",
    concept="Encapsulation means hiding the data and offering checked functions. A setter can refuse a bad value. A getter lets others read the value.\n"
            "Then the class always stays valid. Think of a bank counter. You cannot reach the vault, but the clerk checks every deposit.",
    A=dict(file="account.cpp", label="A safe account", on="deposit refuses a negative amount",
           src='''
#include <iostream>
using namespace std;

class Account {
    double balance_ = 0;

public:
    bool deposit(double amount) {
        if (amount <= 0) {
            return false;
        }
        balance_ += amount;
        return true;
    }
    double balance() const { return balance_; }
};

int main() {
    Account acc;
    acc.deposit(500);
    cout << boolalpha << acc.deposit(-20) << endl;
    cout << acc.balance() << endl;
    return 0;
}
''',
           narr="[HL: double balance_] The balance is private. [HL: bool deposit] Deposit is the only way to add money. [HL: if (amount <= 0)] It refuses an amount of zero or less. [HL: balance_ += amount] A good amount is added. "
                "[HL: acc.deposit(500)] Main deposits five hundred. [HL: acc.deposit(-20)] Then it tries to deposit minus twenty. The answer is false. [HL: cout << acc.balance()] The balance is still five hundred."),
    ill=dict(label="Checked access", on="a flow: call, check, change or refuse",
             data=flow([("Call", "acc.deposit(-20)"), ("Check", "amount <= 0 ?"), ("Refuse", "Return false, no change"), ("Balance", "Stays 500")]),
             narr="Follow the call. Deposit receives minus twenty. The check finds a bad amount. The function refuses, and returns false. "
                  "The balance never changes. The outside code cannot break the rule."),
    B=dict(file="getset.cpp", label="A getter and a setter", on="a setter that keeps age in range",
           src='''
#include <iostream>
using namespace std;

class Person {
    int age_ = 0;

public:
    int age() const { return age_; }
    void set_age(int age) {
        if (age >= 0 && age <= 120) {
            age_ = age;
        }
    }
};

int main() {
    Person p;
    p.set_age(17);
    p.set_age(500);
    cout << p.age() << endl;
    return 0;
}
''',
           narr="[HL: int age() const] The getter reads the age. [HL: void set_age] The setter checks the range. [HL: if (age >= 0] Only an age from zero to one hundred twenty is accepted. "
                "[HL: p.set_age(17)] Seventeen is accepted. [HL: p.set_age(500)] Five hundred is refused. [HL: cout << p.age()] The age is still seventeen."),
    term="The program prints seventeen.",
    recap=["Keep data private.", "Offer public functions that check the input.",
           "A setter can refuse a bad value.", "The class always stays in a valid state."],
    bug=dict(title="A setter that does not check", file="getset.cpp", kind="output", wrong_note="the setter stores any value",
             wrong='''
#include <iostream>
using namespace std;

class Person {
    int age_ = 0;

public:
    int age() const { return age_; }
    void set_age(int age) { age_ = age; }
};

int main() {
    Person p;
    p.set_age(-5);
    cout << p.age() << endl;
    return 0;
}
''', fixed_note="the setter checks the range",
             fixed='''
#include <iostream>
using namespace std;

class Person {
    int age_ = 0;

public:
    int age() const { return age_; }
    void set_age(int age) {
        if (age >= 0 && age <= 120) {
            age_ = age;
        }
    }
};

int main() {
    Person p;
    p.set_age(-5);
    cout << p.age() << endl;
    return 0;
}
''',
             why="A setter without a check is the same as a public field. The age of minus five breaks the rules of the class.",
             narr="Bug of the Day. The setter stores any number. The program prints an age of minus five. "
                  "The data is private, but the setter gives no protection. Add a check, so that the class stays valid."),
    pun="The vault told the thief, you can only deposit your complaints at the window.",
    task="write a safe class", challenge="Write a Thermostat class. The setter must accept only temperatures from ten to thirty degrees.",
    answer="Keep the temperature private. In the setter, test that the value is at least ten and at most thirty. Store it only then.",
))

EPISODES.append(dict(
    n=57, title="this and const methods", spoken="this and const methods", yt="C++ this Pointer and const Member Functions",
    thumb="THIS + CONST", vis="a crab pointing at itself",
    goals=["explain the this pointer", "chain calls by returning a reference", "mark read-only functions const"],
    tags=["this pointer", "const member function", "method chaining", "c++ const correctness"],
    analogy="saying me: every object can talk about itself",
    c_pts=["This points to the current object", "Return star this to chain calls", "A const function promises not to change the object"],
    hook="Every object knows its own address.",
    intro="Today we meet the hidden pointer that every member function receives. It points to the object that made the call.",
    concept="Inside a member function, the name this is a pointer to the current object. You rarely need to write it, but it explains how member functions work.\n"
            "A function that returns star this lets you chain calls. A const function promises not to change the object. Think of the word me. Every object can talk about itself.",
    A=dict(file="chain.cpp", label="Chain the calls", on="each function returns the object, so calls chain",
           src='''
#include <iostream>
using namespace std;

class Counter {
    int count_ = 0;

public:
    Counter& add(int n) {
        count_ += n;
        return *this;
    }
    int get() const { return count_; }
};

int main() {
    Counter c;
    c.add(2).add(3).add(10);
    cout << c.get() << endl;
    return 0;
}
''',
           narr="[HL: Counter& add] Add returns a reference to a Counter. [HL: count_ += n] It adds n to the count. [HL: return *this] This is a pointer to the current object. Star this is the object itself. "
                "[HL: c.add(2).add(3)] Because add returns the object, we can call add again on the result. [HL: cout << c.get()] Two plus three plus ten gives fifteen."),
    ill=dict(label="Where this points", on="the pointer this points at the object c",
             data=mem([("c.count_", "int", "15"), ("this", "Counter*", None)], arrows=[("this", "c.count_", "points to the object")], caption="Inside add, this holds the address of c"),
             narr="Inside add, the hidden pointer this holds the address of c. That is how add knows which count to change. "
                  "Each object has its own address, so each call changes the right object."),
    B=dict(file="constfunc.cpp", label="A const member function", on="show promises not to change the object",
           src='''
#include <iostream>
using namespace std;

class Counter {
    int count_ = 7;

public:
    void increment() { count_++; }
    int get() const { return count_; }
};

int main() {
    const Counter c;
    cout << c.get() << endl;
    return 0;
}
''',
           narr="[HL: void increment] This function changes the object, so it is not const. [HL: int get() const] The word const after the brackets is a promise. This function does not change the object. "
                "[HL: const Counter c] Here the object is const. [HL: c.get()] A const object may only call const functions. Get is const, so the call is fine."),
    term="The program prints seven.",
    recap=["This is a pointer to the current object.", "Return star this to chain calls.",
           "Const after the brackets is a promise not to change the object.", "A const object can only call const functions."],
    bug=dict(title="A non-const call on a const object", file="constfunc.cpp", kind="compile", wrong_note="increment is not const",
             wrong='''
#include <iostream>
using namespace std;

class Counter {
    int count_ = 7;

public:
    void increment() { count_++; }
    int get() const { return count_; }
};

int main() {
    const Counter c;
    c.increment();
    cout << c.get() << endl;
    return 0;
}
''', fixed_note="the object is not const",
             fixed='''
#include <iostream>
using namespace std;

class Counter {
    int count_ = 7;

public:
    void increment() { count_++; }
    int get() const { return count_; }
};

int main() {
    Counter c;
    c.increment();
    cout << c.get() << endl;
    return 0;
}
''',
             why="A const object may not change, so it may not call a function that can change it. Remove const from the object, or do not call that function.",
             narr="Bug of the Day. The object is const, but we call increment. The compiler says passing const Counter as this argument discards qualifiers. "
                  "That sounds hard, but it means this. A const object cannot call a function that may change it."),
    pun="The object looked in the mirror and said, I like this.",
    task="mark the right functions const", challenge="Write a class with a private value. Add three functions: set, get and print. Mark every function that does not change the object as const.",
    answer="Get and print do not change the object, so mark both const. Set changes the value, so it stays non-const.",
))

EPISODES.append(dict(
    n=58, title="Static members", spoken="static members", yt="C++ Static Members: Shared by All Objects",
    thumb="STATIC", vis="a shared notice board for all classrooms",
    goals=["share one value among all objects", "write a static member function", "know that static functions have no this"],
    tags=["static member c++", "static function", "class variable", "inline static"],
    analogy="a school notice board: one board, shared by every classroom",
    c_pts=["A static member belongs to the class", "All objects share one copy", "A static function has no this"],
    hook="One value, shared by every object.",
    intro="Today we share data between objects. A static member belongs to the class, and every object sees the same one.",
    concept="A normal member belongs to each object. A static member belongs to the class. There is only one copy, and every object shares it.\n"
            "Since C plus plus seventeen, you can write inline static and set the value inside the class. A static function has no this pointer, so it can only use static members. Think of a school notice board. There is one board, and every classroom reads it.",
    A=dict(file="tally.cpp", label="Count the objects", on="a static counter counts how many objects exist",
           src='''
#include <iostream>
using namespace std;

class Ticket {
public:
    inline static int sold = 0;
    Ticket() { sold++; }
};

int main() {
    Ticket a, b, c;
    cout << Ticket::sold << endl;
    return 0;
}
''',
           narr="[HL: inline static int sold] Sold is static. It belongs to the class, and there is one copy. [HL: Ticket() { sold++; }] Each constructor adds one to the shared count. [HL: Ticket a, b, c;] Three objects are made, so the count goes up three times. "
                "[HL: Ticket::sold] We reach a static member with the class name and two colons. The answer is three."),
    ill=dict(label="One shared copy", on="three objects, and one static value in the static region",
             data=mem([("Ticket::sold", "int", "3", "static"), ("a", "char", "'a'"), ("b", "char", "'b'"), ("c", "char", "'c'")], caption="The three objects hold no sold member. One shared copy lives in the static region"),
             narr="Look at the static region. One box holds sold. The three objects do not each have their own copy. "
                  "They all read and write the same box."),
    B=dict(file="statfunc.cpp", label="A static function", on="a static function works without an object",
           src='''
#include <iostream>
using namespace std;

class Temperature {
public:
    static double to_fahrenheit(double c) { return c * 9 / 5 + 32; }
};

int main() {
    cout << Temperature::to_fahrenheit(100) << endl;
    return 0;
}
''',
           narr="[HL: static double to_fahrenheit] A static function belongs to the class. We can call it without an object. [HL: Temperature::to_fahrenheit] We write the class name, two colons, and the function name. "
                "One hundred degrees Celsius is two hundred twelve degrees Fahrenheit."),
    term="The program prints two hundred twelve.",
    recap=["A static member belongs to the class.", "All objects share one copy.",
           "Reach it with the class name and two colons.", "A static function has no this pointer."],
    bug=dict(title="A static function that uses a normal member", file="statfunc.cpp", kind="compile", wrong_note="the static function reads a normal member",
             wrong='''
#include <iostream>
using namespace std;

class Counter {
    int count_ = 0;

public:
    static int peek() { return count_; }
};

int main() {
    cout << Counter::peek() << endl;
    return 0;
}
''', fixed_note="the function is not static",
             fixed='''
#include <iostream>
using namespace std;

class Counter {
    int count_ = 0;

public:
    int peek() const { return count_; }
};

int main() {
    Counter c;
    cout << c.peek() << endl;
    return 0;
}
''',
             why="A normal member belongs to an object. A static function has no object, so it has no count to read.",
             narr="Bug of the Day. A static function tries to read a normal member. The compiler says invalid use of member in static member function. "
                  "A static function has no object, so it has no count. Make the function normal, and call it on an object."),
    pun="Why is the static member so popular? Everybody shares it, and nobody pays rent.",
    task="count the objects", challenge="Write a class with a static counter. Count how many objects exist. Print the count after you make five.",
    answer="Use inline static int count equals zero. Add one in the constructor. Print the class name, two colons, and count. It shows five.",
))

EPISODES.append(dict(
    n=59, title="Operator overloading", spoken="operator overloading", yt="C++ Operator Overloading: + and << for Your Class",
    thumb="OPERATORS", vis="a plus sign wearing a class badge",
    goals=["overload plus for a class", "overload the output operator", "keep operators natural"],
    tags=["operator overloading", "c++ operator+", "overload <<", "vector class"],
    analogy="a language: the word add means something different for numbers and for fractions",
    c_pts=["An operator is a function with a special name", "Plus for a class is operator plus", "Output uses operator with two arrows"],
    hook="Teach plus to add your own objects.",
    intro="Today we teach operators new tricks. With your own plus, you can add two points as easily as two numbers.",
    concept="An operator is a function with a special name. The plus operator for your class is a function called operator plus. When you write a plus b, the compiler calls it.\n"
            "The output operator is a free function that takes a stream and your object. Keep operators natural. Plus should add, and not delete files.",
    A=dict(file="vec.cpp", label="Add two points", on="operator plus adds two Vec objects",
           src='''
#include <iostream>
using namespace std;

struct Vec {
    int x, y;
    Vec operator+(const Vec& other) const {
        return {x + other.x, y + other.y};
    }
};

int main() {
    Vec a{1, 2};
    Vec b{10, 20};
    Vec c = a + b;
    cout << c.x << " " << c.y << endl;
    return 0;
}
''',
           narr="[HL: Vec operator+] The function name is operator plus. It takes another Vec by const reference. [HL: return {x + other.x] It returns a new Vec with the sums of the parts. [HL: Vec a{1, 2}] A is one, two. [HL: Vec b{10, 20}] B is ten, twenty. "
                "[HL: Vec c = a + b] The compiler turns this into a dot operator plus of b. [HL: cout << c.x] C is eleven, twenty-two."),
    ill=dict(label="What the compiler calls", on="a table: the expression and the call behind it",
             data=table(["You write", "The compiler calls"], [["a + b", "a.operator+(b)"], ["cout << a", "operator<<(cout, a)"], ["a == b", "a.operator==(b)"]]),
             narr="The table shows what happens. A plus b becomes a call to a dot operator plus, with b. Cout arrows a becomes a call to a free function called operator with two arrows. "
                  "The operators are only a nicer way to write function calls."),
    B=dict(file="print.cpp", label="Print with arrows", on="operator<< prints a Vec with cout",
           src='''
#include <iostream>
using namespace std;

struct Vec {
    int x, y;
};

ostream& operator<<(ostream& out, const Vec& v) {
    return out << "(" << v.x << ", " << v.y << ")";
}

int main() {
    Vec a{3, 4};
    cout << "Point " << a << endl;
    return 0;
}
''',
           narr="[HL: ostream& operator<<] The first parameter is the output stream. The second is the object. [HL: return out <<] The function prints the parts, and returns the stream. This lets us chain more arrows. "
                "[HL: cout << \"Point \" << a] Now cout can print a Vec as easily as a number. The output is Point, three, four, in brackets."),
    term="The program prints Point followed by three comma four in round brackets.",
    recap=["An operator is a function with a special name.", "Operator plus lets you add objects.",
           "The output operator takes a stream and an object.", "Keep the meaning natural."],
    bug=dict(title="An operator that does not exist", file="vec.cpp", kind="compile", wrong_note="plus is used before it is defined",
             wrong='''
#include <iostream>
using namespace std;

struct Vec {
    int x, y;
};

int main() {
    Vec a{1, 2};
    Vec b{3, 4};
    Vec c = a + b;
    cout << c.x << endl;
    return 0;
}
''', fixed_note="operator plus is defined",
             fixed='''
#include <iostream>
using namespace std;

struct Vec {
    int x, y;
    Vec operator+(const Vec& other) const {
        return {x + other.x, y + other.y};
    }
};

int main() {
    Vec a{1, 2};
    Vec b{3, 4};
    Vec c = a + b;
    cout << c.x << endl;
    return 0;
}
''',
             why="The compiler does not know how to add two Vec objects, until you write operator plus for them.",
             narr="Bug of the Day. We add two Vec objects, but there is no operator plus. The compiler says no match for operator plus, with the operand types. "
                  "It does not know how to add two points. Write operator plus in the struct."),
    pun="I overloaded plus so that it adds fish. Now my program is full of surplus.",
    task="overload minus", challenge="Add operator minus to Vec. Subtract one point from another, and print the result.",
    answer="Write Vec operator minus with a const reference. Return x minus other x, and y minus other y.",
))

EPISODES.append(dict(
    n=60, title="Rule of three, five and zero", spoken="the rule of three, five and zero", yt="C++ Rule of Three, Five and Zero",
    thumb="RULE OF 3-5-0", vis="three keys: copy, assign, destroy",
    goals=["explain deep copy and shallow copy", "write a copy constructor", "prefer the rule of zero"],
    tags=["rule of three", "rule of five", "copy constructor", "rule of zero"],
    analogy="photocopying a key: copy the key itself, not just the label on it",
    c_pts=["A shallow copy shares the memory", "A deep copy makes new memory", "Best: let vector and string do the work"],
    hook="If you write a destructor, you must write a copy too.",
    intro="Today we finish the module with the most important rule. It tells you when to write copy functions, and when to write none.",
    concept="A class that owns heap memory needs care. The default copy copies the pointer, not the memory. That is a shallow copy. Two objects then share one box, and both try to delete it.\n"
            "The rule of three says: if you write a destructor, a copy constructor or a copy assignment, write all three. The rule of zero is better. Use vector and string, and write none of them.",
    A=dict(file="deep.cpp", label="A deep copy", on="a copy constructor makes new memory",
           src='''
#include <iostream>
using namespace std;

class Box {
    int* data_;

public:
    Box(int v) : data_(new int(v)) {}
    Box(const Box& other) : data_(new int(*other.data_)) {}
    ~Box() { delete data_; }
    void set(int v) { *data_ = v; }
    int get() const { return *data_; }
};

int main() {
    Box a(5);
    Box b = a;
    b.set(9);
    cout << a.get() << " " << b.get() << endl;
    return 0;
}
''',
           narr="[HL: int* data_] The box owns one int on the heap. [HL: Box(const Box& other)] The copy constructor makes a new int, with the same value. That is a deep copy. [HL: ~Box()] The destructor deletes the box. "
                "[HL: Box b = a] This line calls the copy constructor. [HL: b.set(9)] We change b only. [HL: cout << a.get()] A still holds five, and b holds nine. They have separate memory."),
    ill=dict(label="Shallow and deep copy", on="a shallow copy shares one box, and a deep copy makes two",
             data=mem([("a", "Box*", None, "stack"), ("b", "Box*", None, "stack"), ("boxA", "int", "5", "heap"), ("boxB", "int", "5", "heap")],
                      arrows=[("a", "boxA", "deep copy: own box"), ("b", "boxB", "deep copy: own box")], caption="With a deep copy, each object owns its own heap box"),
             narr="Here is a deep copy. A owns its box. B owns another box with the same value. A change to one does not affect the other. "
                  "In a shallow copy, both pointers would point to the first box, and both would delete it. That is a crash."),
    B=dict(file="zero.cpp", label="The rule of zero", on="a class that uses vector needs no copy code",
           src='''
#include <iostream>
#include <vector>
using namespace std;

class Scores {
    vector<int> data_;

public:
    void add(int v) { data_.push_back(v); }
    int count() const { return static_cast<int>(data_.size()); }
};

int main() {
    Scores a;
    a.add(10);
    a.add(20);
    Scores b = a;
    b.add(30);
    cout << a.count() << " " << b.count() << endl;
    return 0;
}
''',
           narr="[HL: vector<int> data_] The vector owns the memory. [HL: void add] We write no destructor and no copy functions. [HL: Scores b = a] The default copy copies the vector, and the vector copies its items. "
                "[HL: b.add(30)] We add to b only. [HL: cout << a.count()] A has two items, and b has three. The rule of zero gives us the right result for free."),
    term="The program prints two and three.",
    recap=["A shallow copy shares memory, and a deep copy makes new memory.", "If you write a destructor, write the copy functions too.",
           "That is the rule of three.", "The rule of zero is best. Let vector and string manage the memory."],
    bug=dict(title="A copy that was switched off", file="deep.cpp", kind="compile", wrong_note="the copy constructor is deleted",
             wrong='''
#include <iostream>
using namespace std;

class Box {
    int value_;

public:
    Box(int v) : value_(v) {}
    Box(const Box& other) = delete;
    int get() const { return value_; }
};

int main() {
    Box a(5);
    Box b = a;
    cout << b.get() << endl;
    return 0;
}
''', fixed_note="the default copy is allowed",
             fixed='''
#include <iostream>
using namespace std;

class Box {
    int value_;

public:
    Box(int v) : value_(v) {}
    int get() const { return value_; }
};

int main() {
    Box a(5);
    Box b = a;
    cout << b.get() << endl;
    return 0;
}
''',
             why="Writing equals delete switches a function off. The compiler then refuses any code that calls it. Use it when copying makes no sense.",
             narr="Bug of the Day. The copy constructor is marked equals delete. The compiler says use of deleted function. "
                  "That is on purpose. It switches a function off. Remove the delete line if the class should be copyable."),
    pun="The programmer said, I will copy my homework. The compiler replied, that is a shallow excuse.",
    task="decide: rule of three or zero", challenge="Make a class that holds a name and a list of marks. Decide if it needs a destructor. Explain in a comment.",
    answer="It needs no destructor, because string and vector manage their own memory. That is the rule of zero.",
))
