"""Module 7 — Inheritance and polymorphism (EP 61-68)."""
from lib import flow, graph, table

MODULE = {"id": 7, "name": "Inheritance and polymorphism", "range": "61–68", "colours": "Pastel blue + Apricot", "bg": "pastel blue"}
NEXT_AFTER = ("Next: EP 69 · Function templates", "We end module seven here. Next time: templates, code that works for any type.")
EPISODES = []

EPISODES.append(dict(
    n=61, title="Inheritance", spoken="inheritance", yt="C++ Inheritance: Reuse a Class",
    thumb="INHERITANCE", vis="a family tree of animals",
    goals=["write a derived class", "reuse the members of a base class", "say is-a to test a design"],
    tags=["c++ inheritance", "base class derived class", "is-a relationship", "public inheritance"],
    analogy="a family: a child gets the family name, and adds its own talents",
    c_pts=["A derived class gets the members of its base", "It can add new members", "Use inheritance only for an is-a relationship"],
    hook="Write it once in the base. Every child gets it.",
    intro="Today we reuse a class. A derived class gets everything from a base class, and then it adds its own things.",
    concept="Inheritance lets a new class build on an existing class. The existing class is the base. The new class is the derived class. It gets the public members of the base, and can add more.\n"
            "Use it only for an is-a relationship. A dog is an animal, so it works. Think of a family. A child gets the family name, and adds its own talents.",
    A=dict(file="animals.cpp", label="Animal and Dog", on="Dog inherits from Animal and adds a new function",
           src='''
#include <iostream>
#include <string>
using namespace std;

class Animal {
public:
    string name = "Moti";
    void eat() const { cout << name << " eats" << endl; }
};

class Dog : public Animal {
public:
    void fetch() const { cout << name << " fetches" << endl; }
};

int main() {
    Dog d;
    d.eat();
    d.fetch();
    return 0;
}
''',
           narr="[HL: class Animal] The base class has a name and an eat function. [HL: class Dog : public Animal] The colon and public Animal say that Dog inherits from Animal. [HL: void fetch] Dog adds a new function. "
                "[HL: Dog d;] Here we make a dog. [HL: d.eat()] Eat comes from Animal. [HL: d.fetch()] Fetch comes from Dog. One object has both."),
    ill=dict(label="A small family tree", on="Animal at the top, with Dog and Cat below",
             data=graph([("animal", "Animal", "name, eat()"), ("dog", "Dog", "adds fetch()"), ("cat", "Cat", "adds purr()")], [("animal", "dog", "is-a"), ("animal", "cat", "is-a")], layout="tree"),
             narr="Look at the tree. Animal sits at the top. It holds what all animals share. Dog and Cat sit below. "
                  "Each adds its own functions. The arrows read as is-a. A dog is an animal."),
    B=dict(file="hide.cpp", label="A derived function hides the base one", on="Dog writes its own speak",
           src='''
#include <iostream>
using namespace std;

class Animal {
public:
    void speak() const { cout << "..." << endl; }
};

class Dog : public Animal {
public:
    void speak() const { cout << "Woof" << endl; }
};

int main() {
    Dog d;
    d.speak();
    d.Animal::speak();
    return 0;
}
''',
           narr="[HL: void speak() const { cout << \"...\"] The base speak prints three dots. [HL: void speak() const { cout << \"Woof\"] Dog writes its own speak. It hides the base version. [HL: d.speak()] A call on a Dog finds the Dog version first. It prints Woof. "
                "[HL: d.Animal::speak()] We can still reach the base version with the class name and two colons. It prints three dots."),
    term="The program prints Woof, and then three dots.",
    recap=["A derived class gets the members of its base.", "The colon and public name the base class.",
           "A derived class can add or replace functions.", "Use inheritance for an is-a relationship."],
    bug=dict(title="Touching a private base member", file="animals.cpp", kind="compile", wrong_note="the base member is private",
             wrong='''
#include <iostream>
#include <string>
using namespace std;

class Animal {
    string name_ = "Moti";

public:
    void eat() const { cout << name_ << " eats" << endl; }
};

class Dog : public Animal {
public:
    void fetch() const { cout << name_ << " fetches" << endl; }
};

int main() {
    Dog d;
    d.fetch();
    return 0;
}
''', fixed_note="the base offers a public function",
             fixed='''
#include <iostream>
#include <string>
using namespace std;

class Animal {
    string name_ = "Moti";

public:
    const string& name() const { return name_; }
};

class Dog : public Animal {
public:
    void fetch() const { cout << name() << " fetches" << endl; }
};

int main() {
    Dog d;
    d.fetch();
    return 0;
}
''',
             why="Private members belong to the base class only. A derived class cannot touch them. It must use a public or protected function.",
             narr="Bug of the Day. Dog tries to use the private name of Animal. The compiler says the name is private within this context. "
                  "Private means private, even for children. Add a public getter in Animal, and call it from Dog."),
    pun="The base class told the derived class, you have your mother's functions.",
    task="build a Vehicle and a Bus", challenge="Write a class Vehicle with a function start. Write a class Bus that inherits from it and adds open doors.",
    answer="Write class Bus colon public Vehicle. Add an open doors function. A Bus object can call both start and open doors.",
))

EPISODES.append(dict(
    n=62, title="Constructor and destructor order", spoken="constructor and destructor order", yt="C++ Inheritance: Constructor and Destructor Order",
    thumb="WHO IS FIRST?", vis="a stack of nesting dolls opening in order",
    goals=["predict the order of constructors", "pass arguments to the base constructor", "predict the order of destructors"],
    tags=["constructor order inheritance", "base class constructor", "destructor order", "initializer list base"],
    analogy="building a house: the foundation comes first, and the roof comes last",
    c_pts=["The base is built first", "The derived part is built next", "Destruction runs in the reverse order"],
    hook="The base is always built first.",
    intro="Today we learn who is built first. The order matters a lot when classes depend on each other.",
    concept="When you make a derived object, the base part is built first. Then the derived part is built. When the object dies, the order reverses. The derived part goes first, and then the base part.\n"
            "To give arguments to the base constructor, call it in the initializer list. Think of building a house. The foundation comes first, and the roof comes last. Taking it down reverses the order.",
    A=dict(file="order.cpp", label="Build and destroy", on="messages show the order of construction and destruction",
           src='''
#include <iostream>
using namespace std;

class Base {
public:
    Base() { cout << "Base made" << endl; }
    ~Base() { cout << "Base gone" << endl; }
};

class Derived : public Base {
public:
    Derived() { cout << "Derived made" << endl; }
    ~Derived() { cout << "Derived gone" << endl; }
};

int main() {
    Derived d;
    return 0;
}
''',
           narr="[HL: Base() {] The base constructor prints Base made. [HL: Derived() {] The derived constructor prints Derived made. [HL: Derived d;] Main makes one Derived object. The base part is built first. "
                "Base made prints, and then Derived made. [HL: return 0] At the end, the order reverses. Derived gone prints first, and then Base gone."),
    ill=dict(label="Life of a Derived object", on="a flow: base built, derived built, derived destroyed, base destroyed",
             data=flow([("Base built", "Base made"), ("Derived built", "Derived made"), ("Derived destroyed", "Derived gone"), ("Base destroyed", "Base gone")]),
             narr="Follow the flow. The base is built first. Then the derived part. At the end, the derived part is destroyed first. "
                  "The base part is destroyed last. The derived part may depend on the base part, so the base must live longer."),
    B=dict(file="args.cpp", label="Arguments for the base", on="the derived constructor calls the base constructor with a value",
           src='''
#include <iostream>
#include <string>
using namespace std;

class Animal {
    string name_;

public:
    Animal(string name) : name_(name) {}
    const string& name() const { return name_; }
};

class Dog : public Animal {
    int age_;

public:
    Dog(string name, int age) : Animal(name), age_(age) {}
    void show() const { cout << name() << " " << age_ << endl; }
};

int main() {
    Dog d("Moti", 3);
    d.show();
    return 0;
}
''',
           narr="[HL: Animal(string name)] The base constructor needs a name. [HL: Dog(string name, int age)] The derived constructor takes a name and an age. [HL: Animal(name)] In the initializer list, we call the base constructor first. "
                "[HL: age_(age)] Then we set the age. [HL: Dog d(] Main passes both values. [HL: d.show()] The output is Moti, three."),
    term="The program prints Moti and three.",
    recap=["The base part is built first.", "The derived part is built next.",
           "Destruction runs in the reverse order.", "Call the base constructor in the initializer list."],
    bug=dict(title="A base with no default constructor", file="args.cpp", kind="compile", wrong_note="the derived constructor does not call the base constructor",
             wrong='''
#include <iostream>
#include <string>
using namespace std;

class Animal {
    string name_;

public:
    Animal(string name) : name_(name) {}
};

class Dog : public Animal {
public:
    Dog() {}
};

int main() {
    Dog d;
    return 0;
}
''', fixed_note="the base constructor is called with a name",
             fixed='''
#include <iostream>
#include <string>
using namespace std;

class Animal {
    string name_;

public:
    Animal(string name) : name_(name) {}
};

class Dog : public Animal {
public:
    Dog() : Animal("Unknown") {}
};

int main() {
    Dog d;
    return 0;
}
''',
             why="The base part must be built first. If the base has no default constructor, the derived constructor must say which one to call.",
             narr="Bug of the Day. Animal needs a name, but Dog does not give one. The compiler says no matching function for call to Animal. "
                  "The base part is built first, so the compiler must call a base constructor. Name it in the initializer list."),
    pun="The base class was always first in line. It said, I was here before you were derived.",
    task="trace the order", challenge="Write three classes: A, B inherits from A, and C inherits from B. Print a message in each constructor. Predict the order for a C object.",
    answer="A is built first, then B, then C. The destructors run in the reverse order: C, then B, then A.",
))

EPISODES.append(dict(
    n=63, title="protected and access control", spoken="protected and access control", yt="C++ public, protected and private Explained",
    thumb="PROTECTED", vis="three doors labelled public, protected and private",
    goals=["use the protected label", "read the access table", "choose the right label"],
    tags=["protected c++", "access specifiers", "public private protected", "inheritance access"],
    analogy="a family house: the street sees the gate, the family sees the hall, only you see your room",
    c_pts=["Public is open to everyone", "Protected is open to the class and its children", "Private is open to the class only"],
    hook="Protected is for the family only.",
    intro="Today we meet the third access label. It sits between public and private, and it is made for inheritance.",
    concept="Public members are open to everyone. Private members are open to the class only. Protected members are open to the class and to its derived classes, but not to the outside.\n"
            "Choose the strictest label that works. Think of a family house. The street sees the gate. The family sees the hall. Only you see your own room.",
    A=dict(file="protect.cpp", label="A protected member", on="the derived class reads a protected member",
           src='''
#include <iostream>
using namespace std;

class Account {
protected:
    double balance_ = 100;
};

class Savings : public Account {
public:
    void add_interest() { balance_ *= 1.1; }
    double balance() const { return balance_; }
};

int main() {
    Savings s;
    s.add_interest();
    cout << s.balance() << endl;
    return 0;
}
''',
           narr="[HL: protected:] Everything below this label is open to derived classes. [HL: double balance_] The balance is protected. [HL: class Savings : public Account] Savings inherits from Account. "
                "[HL: balance_ *= 1.1] Savings can change the protected balance. Interest adds ten percent. [HL: s.balance()] Main reads it through a public function. The result is one hundred ten."),
    ill=dict(label="Who can reach what", on="a table of the three labels and who can reach them",
             data=table(["Label", "The class", "A derived class", "Outside code"], [["public", "yes", "yes", "yes"], ["protected", "yes", "yes", "no"], ["private", "yes", "no", "no"]]),
             narr="Read the table row by row. Public is open to all. Protected is open to the class and its children, but closed to outside code. "
                  "Private is open to the class only."),
    B=dict(file="levels.cpp", label="All three labels", on="one class with public, protected and private data",
           src='''
#include <iostream>
using namespace std;

class Base {
public:
    int open_ = 1;

protected:
    int family_ = 2;

private:
    int secret_ = 3;

public:
    int secret() const { return secret_; }
};

class Child : public Base {
public:
    int sum() const { return open_ + family_ + secret(); }
};

int main() {
    Child c;
    cout << c.sum() << endl;
    cout << c.open_ << endl;
    return 0;
}
''',
           narr="[HL: int open_] Open is public. Everyone can read it. [HL: int family_] Family is protected. [HL: int secret_] Secret is private. [HL: int secret() const] A public getter lets others read the secret. "
                "[HL: int sum() const] The child adds all three parts. It reads family directly, and secret through the getter. The sum is six. [HL: cout << c.open_] Main may read the public part."),
    term="The program prints six, and then one.",
    recap=["Public is open to everyone.", "Protected is open to the class and its children.",
           "Private is open to the class only.", "Choose the strictest label that works."],
    bug=dict(title="Reaching protected data from outside", file="protect.cpp", kind="compile", wrong_note="main reads a protected member",
             wrong='''
#include <iostream>
using namespace std;

class Account {
protected:
    double balance_ = 100;
};

int main() {
    Account a;
    cout << a.balance_ << endl;
    return 0;
}
''', fixed_note="a public function gives access",
             fixed='''
#include <iostream>
using namespace std;

class Account {
protected:
    double balance_ = 100;

public:
    double balance() const { return balance_; }
};

int main() {
    Account a;
    cout << a.balance() << endl;
    return 0;
}
''',
             why="Protected members are for the class and its children. Main is outside code, so it cannot reach them.",
             narr="Bug of the Day. Main reads a protected member. The compiler says the balance is protected within this context. "
                  "Protected is open to children, not to outside code. Add a public getter."),
    pun="Protected is the middle child of access labels. It always gets along with the family.",
    task="pick the right label", challenge="Write a class with a name, an id and a secret code. Decide which label each one needs, and explain in a comment.",
    answer="The name can be public through a getter. The id can be protected for derived classes. The secret code stays private.",
))

EPISODES.append(dict(
    n=64, title="Virtual functions", spoken="virtual functions", yt="C++ Virtual Functions and Polymorphism",
    thumb="VIRTUAL!", vis="one remote control that works with many TVs",
    goals=["write a virtual function", "call it through a base pointer", "use override"],
    tags=["virtual function", "polymorphism c++", "override keyword", "base pointer"],
    analogy="a remote control: one button, and each TV does its own thing",
    c_pts=["A virtual function is chosen at run time", "A base pointer can hold a derived object", "Use override to catch mistakes"],
    hook="One call, many behaviours.",
    intro="Today we meet polymorphism. One call can do many different things, depending on the real object.",
    concept="A virtual function is chosen at run time, by the real type of the object. You can hold a Dog in an Animal pointer, and a call to speak still runs the Dog version.\n"
            "Write virtual in the base. Write override in the derived class, so that the compiler checks your spelling. Think of a remote control. One button, and each TV does its own thing.",
    A=dict(file="virtual.cpp", label="A virtual speak", on="a base pointer calls the derived version",
           src='''
#include <iostream>
#include <memory>
using namespace std;

class Animal {
public:
    virtual void speak() const { cout << "..." << endl; }
    virtual ~Animal() = default;
};

class Dog : public Animal {
public:
    void speak() const override { cout << "Woof" << endl; }
};

int main() {
    unique_ptr<Animal> a = make_unique<Dog>();
    a->speak();
    return 0;
}
''',
           narr="[HL: virtual void speak] The word virtual says that the real object decides. [HL: virtual ~Animal] A base class with virtual functions also needs a virtual destructor. We study it soon. "
                "[HL: void speak() const override] Dog overrides speak. The word override makes the compiler check that a base function exists. [HL: unique_ptr<Animal> a] The pointer type is Animal. [HL: make_unique<Dog>] But the object is a Dog. "
                "[HL: a->speak()] The call finds the Dog version at run time. It prints Woof."),
    ill=dict(label="How the call finds Dog", on="the object has a hidden pointer to a table of functions",
             data=graph([("obj", "Dog object", "hidden vptr"), ("vt", "Dog table", "speak, destructor"), ("fn", "Dog::speak", "prints Woof")], [("obj", "vt", "vptr"), ("vt", "fn", "speak")], layout="row"),
             narr="Here is how it works. An object with virtual functions has a hidden pointer. It points to a table of functions for its real type. "
                  "A call to speak looks in that table. For a Dog, the table holds the Dog version."),
    B=dict(file="zoo.cpp", label="Many animals, one loop", on="a vector of animal pointers, one loop",
           src='''
#include <iostream>
#include <memory>
#include <vector>
using namespace std;

class Animal {
public:
    virtual void speak() const = 0;
    virtual ~Animal() = default;
};

class Dog : public Animal {
public:
    void speak() const override { cout << "Woof" << endl; }
};

class Cat : public Animal {
public:
    void speak() const override { cout << "Meow" << endl; }
};

int main() {
    vector<unique_ptr<Animal>> zoo;
    zoo.push_back(make_unique<Dog>());
    zoo.push_back(make_unique<Cat>());
    for (const auto& a : zoo) {
        a->speak();
    }
    return 0;
}
''',
           narr="[HL: vector<unique_ptr<Animal>> zoo] The vector holds pointers to Animal. [HL: make_unique<Dog>()] One is a Dog. [HL: make_unique<Cat>()] One is a Cat. [HL: for (const auto& a : zoo)] The loop does not care which is which. "
                "[HL: a->speak()] It makes one call, and each animal does its own thing. The output is Woof, and then Meow."),
    term="The program prints Woof, and then Meow.",
    recap=["A virtual function is chosen by the real type, at run time.", "A base pointer can hold a derived object.",
           "Write virtual in the base and override in the derived class.", "One loop can serve many types."],
    bug=dict(title="A function that is not virtual", file="virtual.cpp", kind="output", wrong_note="speak is not virtual",
             wrong='''
#include <iostream>
using namespace std;

class Animal {
public:
    void speak() const { cout << "..." << endl; }
};

class Dog : public Animal {
public:
    void speak() const { cout << "Woof" << endl; }
};

int main() {
    Dog d;
    Animal* a = &d;
    a->speak();
    return 0;
}
''', fixed_note="speak is virtual",
             fixed='''
#include <iostream>
using namespace std;

class Animal {
public:
    virtual void speak() const { cout << "..." << endl; }
};

class Dog : public Animal {
public:
    void speak() const override { cout << "Woof" << endl; }
};

int main() {
    Dog d;
    Animal* a = &d;
    a->speak();
    return 0;
}
''',
             why="Without virtual, the compiler picks the function by the pointer type, which is Animal. With virtual, it picks by the real object.",
             narr="Bug of the Day. We call speak through an Animal pointer to a Dog. The program prints three dots, not Woof. "
                  "Speak is not virtual, so the pointer type decides. Add virtual in the base, and override in Dog."),
    pun="Why did the virtual function get a promotion? It always knew who it really was.",
    task="add a Cow to the zoo", challenge="Add a class Cow to the zoo program. Its speak prints Moo. Add one cow to the vector.",
    answer="Write class Cow colon public Animal, with a speak that prints Moo and the word override. Push back a make unique of Cow.",
))

EPISODES.append(dict(
    n=65, title="Abstract classes", spoken="abstract classes and interfaces", yt="C++ Abstract Classes and Interfaces",
    thumb="ABSTRACT", vis="a blueprint with a blank where the details go",
    goals=["write a pure virtual function", "explain that an abstract class cannot be built", "use a class as an interface"],
    tags=["abstract class", "pure virtual function", "interface c++", "shape example"],
    analogy="a contract: it says what must be done, but not how",
    c_pts=["Equals zero makes a function pure virtual", "A class with one is abstract", "Derived classes must fill the blank"],
    hook="Some classes are only a promise.",
    intro="Today we write a class that is only a promise. It says what every shape must do, but not how.",
    concept="A pure virtual function has equals zero after its declaration. It has no body in the base. A class with a pure virtual function is abstract. You cannot make an object of it.\n"
            "Derived classes must override every pure function. Then they can be built. Think of a contract. It says what must be done, but not how.",
    A=dict(file="shapes.cpp", label="A Shape interface", on="Shape is abstract, and Circle and Rect fill the blank",
           src='''
#include <iostream>
using namespace std;

class Shape {
public:
    virtual double area() const = 0;
    virtual ~Shape() = default;
};

class Rect : public Shape {
    double w_, h_;

public:
    Rect(double w, double h) : w_(w), h_(h) {}
    double area() const override { return w_ * h_; }
};

int main() {
    Rect r(3, 4);
    const Shape& s = r;
    cout << s.area() << endl;
    return 0;
}
''',
           narr="[HL: virtual double area() const = 0] Equals zero makes area a pure virtual function. Shape has no body for it. [HL: class Rect : public Shape] Rect inherits from Shape. [HL: Rect(double w, double h)] It takes a width and a height. "
                "[HL: double area() const override] Rect fills in the blank. It returns width times height. [HL: Rect r(3, 4)] Main makes a rectangle. [HL: const Shape& s = r] A Shape reference can refer to it. [HL: s.area()] The answer is twelve."),
    ill=dict(label="Shape and its children", on="Shape at the top, Circle and Rect below",
             data=graph([("shape", "Shape", "area() = 0"), ("circle", "Circle", "area() override"), ("rect", "Rect", "area() override")], [("shape", "circle", "is-a"), ("shape", "rect", "is-a")], layout="tree"),
             narr="Here is the family. Shape is abstract. It only declares area. Circle and Rect each write their own area. "
                  "You can make Circle and Rect objects, but never a plain Shape."),
    B=dict(file="total.cpp", label="Add the areas", on="a vector of shapes and one loop for the total area",
           src='''
#include <iostream>
#include <memory>
#include <vector>
using namespace std;

class Shape {
public:
    virtual double area() const = 0;
    virtual ~Shape() = default;
};

class Rect : public Shape {
    double w_, h_;

public:
    Rect(double w, double h) : w_(w), h_(h) {}
    double area() const override { return w_ * h_; }
};

class Square : public Shape {
    double s_;

public:
    Square(double s) : s_(s) {}
    double area() const override { return s_ * s_; }
};

int main() {
    vector<unique_ptr<Shape>> shapes;
    shapes.push_back(make_unique<Rect>(3, 4));
    shapes.push_back(make_unique<Square>(5));
    double total = 0;
    for (const auto& s : shapes) {
        total += s->area();
    }
    cout << total << endl;
    return 0;
}
''',
           narr="[HL: class Rect] Rect fills the blank one way. [HL: class Square] Square fills it another way. [HL: vector<unique_ptr<Shape>> shapes] The vector holds shapes of both kinds. [HL: total += s->area()] The loop adds their areas. "
                "It does not need to know which shape is which. Twelve plus twenty-five gives thirty-seven."),
    term="The program prints thirty-seven.",
    recap=["Equals zero makes a function pure virtual.", "A class with a pure virtual function is abstract.",
           "You cannot make an object of an abstract class.", "Derived classes must override every pure function."],
    bug=dict(title="Building an abstract class", file="shapes.cpp", kind="compile", wrong_note="main builds a plain Shape",
             wrong='''
#include <iostream>
using namespace std;

class Shape {
public:
    virtual double area() const = 0;
};

int main() {
    Shape s;
    cout << s.area() << endl;
    return 0;
}
''', fixed_note="a derived class fills in area",
             fixed='''
#include <iostream>
using namespace std;

class Shape {
public:
    virtual double area() const = 0;
};

class Unit : public Shape {
public:
    double area() const override { return 1; }
};

int main() {
    Unit s;
    cout << s.area() << endl;
    return 0;
}
''',
             why="A shape with no area has no meaning. The compiler blocks the object. Build a derived class that fills in every pure function.",
             narr="Bug of the Day. Main makes a plain Shape. The compiler says it cannot declare a variable of abstract type Shape. "
                  "A pure function has no body, so an object could never call it. Build a derived class instead."),
    pun="An abstract class is like a promise. It says, I will do it, but not how.",
    task="add a Circle", challenge="Add a class Circle to the shapes program. Its area is three point one four times the radius squared.",
    answer="Write class Circle colon public Shape. Store the radius. Override area, and return three point one four times r times r.",
))

EPISODES.append(dict(
    n=66, title="Virtual destructors", spoken="virtual destructors", yt="C++ Virtual Destructors: Avoid This Bug",
    thumb="VIRTUAL ~", vis="a tilde wearing a crown",
    goals=["explain why a base destructor must be virtual", "predict the output with and without virtual", "read the compiler warning"],
    tags=["virtual destructor", "delete base pointer", "polymorphic delete", "undefined behavior"],
    analogy="a cleaning crew: if the manager only knows the lobby, the back room is never cleaned",
    c_pts=["Deleting through a base pointer needs a virtual destructor", "Without it, only the base part is destroyed", "Smart pointers need it too"],
    hook="Without virtual, half of your object is never cleaned.",
    intro="Today we fix a classic bug. It hides in code that looks right, and it leaks memory.",
    concept="When you delete an object through a base pointer, the compiler must find the right destructor. If the base destructor is not virtual, only the base destructor runs. The derived part is never cleaned.\n"
            "The rule is simple. A class with any virtual function gets a virtual destructor. Think of a cleaning crew. If the manager only knows the lobby, the back room is never cleaned.",
    A=dict(file="vdtor.cpp", label="A virtual destructor", on="both destructors run, in the right order",
           src='''
#include <iostream>
using namespace std;

class Animal {
public:
    virtual ~Animal() { cout << "Animal gone" << endl; }
};

class Dog : public Animal {
public:
    ~Dog() override { cout << "Dog gone" << endl; }
};

int main() {
    Animal* a = new Dog;
    delete a;
    return 0;
}
''',
           narr="[HL: virtual ~Animal] The base destructor is virtual. [HL: ~Dog() override] The Dog destructor overrides it. [HL: Animal* a = new Dog] The pointer is an Animal pointer, and the object is a Dog. "
                "[HL: delete a] Delete finds the real type. Dog gone prints first. Then Animal gone prints. Both parts are cleaned."),
    ill=dict(label="What delete runs", on="a table: with and without a virtual destructor",
             data=table(["Base destructor", "Delete through base pointer", "Result"], [["virtual", "Dog runs, then Animal runs", "Correct"], ["not virtual", "Only Animal runs", "Dog part leaks, undefined"]]),
             narr="The table shows both cases. With a virtual destructor, delete runs the Dog destructor, and then the Animal one. "
                  "Without virtual, only the Animal destructor runs. The result is undefined behaviour."),
    B=dict(file="smart.cpp", label="With a smart pointer", on="unique_ptr needs the virtual destructor too",
           src='''
#include <iostream>
#include <memory>
using namespace std;

class Animal {
public:
    virtual ~Animal() { cout << "Animal gone" << endl; }
};

class Dog : public Animal {
public:
    ~Dog() override { cout << "Dog gone" << endl; }
};

int main() {
    unique_ptr<Animal> a = make_unique<Dog>();
    cout << "working" << endl;
    return 0;
}
''',
           narr="[HL: unique_ptr<Animal> a] A smart pointer to Animal holds a Dog. [HL: cout << \"working\"] The program prints working. [HL: return 0] At the end, the unique pointer deletes the object through the base type. "
                "Because the destructor is virtual, both Dog gone and Animal gone print. The rule is the same for smart pointers."),
    term="The program prints working, then Dog gone, then Animal gone.",
    recap=["Deleting through a base pointer needs a virtual destructor.", "Without it, only the base destructor runs.",
           "A class with a virtual function needs a virtual destructor.", "The same rule holds for smart pointers."],
    bug=dict(title="A base destructor that is not virtual", file="vdtor.cpp", kind="warn", wrong_note="the base destructor is not virtual",
             wrong='''
#include <iostream>
using namespace std;

class Animal {
public:
    virtual void speak() const { cout << "..." << endl; }
    ~Animal() { cout << "Animal gone" << endl; }
};

class Dog : public Animal {
public:
    ~Dog() { cout << "Dog gone" << endl; }
};

int main() {
    Animal* a = new Dog;
    delete a;
    return 0;
}
''', fixed_note="the base destructor is virtual",
             fixed='''
#include <iostream>
using namespace std;

class Animal {
public:
    virtual void speak() const { cout << "..." << endl; }
    virtual ~Animal() { cout << "Animal gone" << endl; }
};

class Dog : public Animal {
public:
    ~Dog() override { cout << "Dog gone" << endl; }
};

int main() {
    Animal* a = new Dog;
    delete a;
    return 0;
}
''',
             why="Delete through a base pointer only runs the base destructor, when it is not virtual. The Dog part is never destroyed.",
             narr="Bug of the Day. The class has a virtual function, but the destructor is not virtual. The compiler warns that deleting an object of polymorphic class type might cause undefined behaviour. "
                  "Only the Animal part would be destroyed. Make the destructor virtual."),
    pun="Why was the destructor so tired? It had to clean up after the whole family.",
    task="check the rule", challenge="Write a base class with one virtual function. Add a virtual destructor. Explain in a comment why it is needed.",
    answer="Delete through a base pointer needs the real destructor to run. A virtual destructor makes the compiler find it.",
))

EPISODES.append(dict(
    n=67, title="Multiple inheritance", spoken="multiple inheritance and the diamond", yt="C++ Multiple Inheritance and the Diamond Problem",
    thumb="THE DIAMOND", vis="a diamond made of four classes",
    goals=["inherit from two bases", "explain the diamond problem", "fix it with virtual inheritance"],
    tags=["multiple inheritance", "diamond problem", "virtual inheritance", "ambiguous member"],
    analogy="a child with two parents: both may have a family car, so which car is meant?",
    c_pts=["A class can have several bases", "Two bases may have the same member name", "Virtual inheritance keeps one shared base"],
    hook="Two parents can make one question ambiguous.",
    intro="Today a class gets two parents. This is powerful, but it brings the famous diamond problem.",
    concept="C plus plus lets a class inherit from more than one base. List them with commas. If both bases have a member with the same name, a call is ambiguous. You must say which one you mean.\n"
            "The diamond problem appears when two bases share one grandparent. Then the object holds two copies of it. Virtual inheritance keeps only one.",
    A=dict(file="two.cpp", label="Two bases", on="a class that inherits from two bases",
           src='''
#include <iostream>
using namespace std;

class Walker {
public:
    void walk() const { cout << "walks" << endl; }
};

class Swimmer {
public:
    void swim() const { cout << "swims" << endl; }
};

class Duck : public Walker, public Swimmer {};

int main() {
    Duck d;
    d.walk();
    d.swim();
    return 0;
}
''',
           narr="[HL: class Walker] Walker has a walk function. [HL: class Swimmer] Swimmer has a swim function. [HL: class Duck : public Walker, public Swimmer] Duck inherits from both. A comma separates the bases. "
                "[HL: d.walk()] A duck can walk. [HL: d.swim()] A duck can swim. The names are different, so there is no problem."),
    ill=dict(label="The diamond", on="two classes share one grandparent",
             data=graph([("animal", "Animal", "grandparent"), ("walker", "Walker", "left parent"), ("swimmer", "Swimmer", "right parent"), ("duck", "Duck", "child")],
                        [("animal", "walker", "is-a"), ("animal", "swimmer", "is-a"), ("walker", "duck", "is-a"), ("swimmer", "duck", "is-a")], layout="row"),
             narr="Look at the diamond. Animal is the grandparent. Walker and Swimmer both inherit from Animal. Duck inherits from both of them. "
                  "Without care, a Duck would hold two Animal parts, one through each parent."),
    B=dict(file="diamond.cpp", label="Virtual inheritance", on="virtual keeps one shared Animal part",
           src='''
#include <iostream>
using namespace std;

class Animal {
public:
    int legs = 2;
};

class Walker : virtual public Animal {};
class Swimmer : virtual public Animal {};
class Duck : public Walker, public Swimmer {};

int main() {
    Duck d;
    d.legs = 4;
    cout << d.legs << endl;
    return 0;
}
''',
           narr="[HL: class Animal] Animal has one member, legs. [HL: class Walker : virtual public Animal] The word virtual tells the compiler to share one Animal part. [HL: class Swimmer : virtual public Animal] Swimmer does the same. "
                "[HL: class Duck] Duck has only one Animal part. [HL: d.legs = 4] So the name legs is not ambiguous. We can use it directly. [HL: cout << d.legs] The output is four."),
    term="The program prints four.",
    recap=["A class can inherit from several bases.", "Equal member names in two bases make a call ambiguous.",
           "The diamond gives two copies of the grandparent.", "Virtual inheritance keeps one copy."],
    bug=dict(title="An ambiguous member", file="two.cpp", kind="compile", wrong_note="both bases have a function called hello",
             wrong='''
#include <iostream>
using namespace std;

class A {
public:
    void hello() const { cout << "A" << endl; }
};

class B {
public:
    void hello() const { cout << "B" << endl; }
};

class C : public A, public B {};

int main() {
    C c;
    c.hello();
    return 0;
}
''', fixed_note="the call names the base",
             fixed='''
#include <iostream>
using namespace std;

class A {
public:
    void hello() const { cout << "A" << endl; }
};

class B {
public:
    void hello() const { cout << "B" << endl; }
};

class C : public A, public B {};

int main() {
    C c;
    c.A::hello();
    return 0;
}
''',
             why="Both bases offer hello, so the compiler cannot guess. Write the name of the base and two colons to choose one.",
             narr="Bug of the Day. Both bases have a hello function. The call on C says hello, and the compiler says the request for hello is ambiguous. "
                  "It cannot guess. Write the base name and two colons to choose."),
    pun="A diamond is forever. So is the ambiguity, until you add virtual.",
    task="resolve an ambiguity", challenge="Make two base classes with the same function name. Inherit from both, and call each version.",
    answer="Write the base name, two colons, and the function name. Call a colon colon hello, and then b colon colon hello.",
))

EPISODES.append(dict(
    n=68, title="Composition and slicing", spoken="composition and slicing", yt="C++ Composition vs Inheritance and Object Slicing",
    thumb="HAS-A OR IS-A", vis="a car with an engine inside it",
    goals=["choose between has-a and is-a", "build a class from parts", "avoid object slicing"],
    tags=["composition vs inheritance", "has-a", "object slicing", "c++ design"],
    analogy="a car and its engine: a car has an engine, it is not an engine",
    c_pts=["Is-a means inheritance", "Has-a means composition", "Pass polymorphic objects by reference, never by value"],
    hook="A car is not an engine. A car has an engine.",
    intro="Today we choose the right tool for the design. We also meet slicing, a bug that cuts your object in half.",
    concept="Use inheritance for an is-a relationship. A dog is an animal. Use composition for a has-a relationship. A car has an engine. Composition makes a member out of another class.\n"
            "Prefer composition when you are not sure. It is simpler. A second danger is slicing. Passing a derived object by value to a base parameter cuts off the derived part. Pass by reference.",
    A=dict(file="car.cpp", label="A car has an engine", on="Car contains an Engine as a member",
           src='''
#include <iostream>
using namespace std;

class Engine {
public:
    void start() const { cout << "Engine starts" << endl; }
};

class Car {
    Engine engine_;

public:
    void drive() const {
        engine_.start();
        cout << "Car moves" << endl;
    }
};

int main() {
    Car c;
    c.drive();
    return 0;
}
''',
           narr="[HL: class Engine] Engine is a small class with one job. [HL: Engine engine_] Car has an engine as a member. This is composition. [HL: void drive() const] Drive uses the engine. [HL: engine_.start()] It calls start on the member. "
                "[HL: Car c;] Main makes a car. [HL: c.drive()] The output shows the engine start, and then the car moves."),
    ill=dict(label="Is-a or has-a?", on="a table of examples and the right tool",
             data=table(["Sentence", "Relationship", "Tool"], [["A dog is an animal", "is-a", "Inheritance"], ["A car has an engine", "has-a", "Composition"], ["A circle is a shape", "is-a", "Inheritance"], ["A library has books", "has-a", "Composition"]]),
             narr="Use the sentence test. If the sentence says is a, use inheritance. If it says has a, use composition. "
                  "A dog is an animal. A car has an engine. When in doubt, choose composition."),
    B=dict(file="slice.cpp", label="Object slicing", on="a derived object is passed by value and loses its derived part",
           src='''
#include <iostream>
using namespace std;

class Animal {
public:
    virtual void speak() const { cout << "..." << endl; }
};

class Dog : public Animal {
public:
    void speak() const override { cout << "Woof" << endl; }
};

void by_value(Animal a) { a.speak(); }
void by_ref(const Animal& a) { a.speak(); }

int main() {
    Dog d;
    by_value(d);
    by_ref(d);
    return 0;
}
''',
           narr="[HL: void by_value] This function takes an Animal by value. The compiler copies only the Animal part of the dog. The Dog part is sliced off. [HL: void by_ref] This one takes a reference. No copy is made. "
                "[HL: by_value(d)] The first call prints three dots. [HL: by_ref(d)] The second call prints Woof. Always pass polymorphic objects by reference or by pointer."),
    term="The program prints three dots, and then Woof.",
    recap=["Use inheritance for is-a.", "Use composition for has-a.",
           "When in doubt, prefer composition.", "Pass polymorphic objects by reference, never by value."],
    bug=dict(title="Slicing in a function call", file="slice.cpp", kind="output", wrong_note="the function takes the base by value",
             wrong='''
#include <iostream>
using namespace std;

class Animal {
public:
    virtual void speak() const { cout << "..." << endl; }
};

class Dog : public Animal {
public:
    void speak() const override { cout << "Woof" << endl; }
};

void talk(Animal a) { a.speak(); }

int main() {
    Dog d;
    talk(d);
    return 0;
}
''', fixed_note="the function takes a const reference",
             fixed='''
#include <iostream>
using namespace std;

class Animal {
public:
    virtual void speak() const { cout << "..." << endl; }
};

class Dog : public Animal {
public:
    void speak() const override { cout << "Woof" << endl; }
};

void talk(const Animal& a) { a.speak(); }

int main() {
    Dog d;
    talk(d);
    return 0;
}
''',
             why="Passing by value copies only the Animal part of the Dog. The copy is a plain Animal, so speak prints three dots.",
             narr="Bug of the Day. We pass a Dog to a function that takes an Animal by value. The function prints three dots, not Woof. "
                  "The Dog part was sliced off in the copy. Take a const reference instead."),
    pun="Object slicing is a bad deal. You asked for a whole dog, and you got half a dog.",
    task="redesign with composition", challenge="Write a class Computer that has a Processor and a Memory as members. Add a function that starts both.",
    answer="Make Processor and Memory small classes with a start function. In Computer, keep one of each as a member. The start function calls both.",
))
