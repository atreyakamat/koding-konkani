"""Module 7 — Object-oriented Python (EP 61-72)."""

MODULE = {"id": 7, "name": "Object-oriented Python", "range": "61–72", "colours": "PastelBlue + Apricot"}
EPISODES = []
NEXT_AFTER = ("Next: EP 73 · Iterators", "Module seven is done! Next time: iterators, and how a for loop really works.")

EPISODES.append(dict(
    n=61, title="Why classes?", spoken="why classes",
    yt="Python Classes: Why We Need Them (Beginner)", thumb="WHY CLASSES?",
    vis="Xecxec holding two tangled strings of data, then one neat labelled box",
    goals=["see why parallel lists are fragile", "meet the idea of bundling data and actions", "read a first tiny class"],
    tags=["python classes", "why use classes python", "python oop for beginners", "python class example"],
    hash=["#python", "#oop"],
    analogy="a student file: the name, the marks and the class all live in one folder, not in three different cupboards",
    c_title="One thing, one bundle",
    c_pts=["Data about one thing belongs together", "A class is a blueprint for such a bundle", "An object is one real bundle made from it"],
    intro="Until now, one student meant a name in one list and marks in another. Today we bundle them together.",
    concept="Imagine you track students. One list holds the names. Another list holds the marks. They line up only by position. Move one item, and everything goes wrong. A class fixes this. It is a blueprint for one type of thing. It says what data each thing carries, and what it can do. An object is one real thing built from the blueprint. Think of a student file. Name, marks and class live in one folder, so they can never get separated.",
    A=dict(file="parallel.py", label="Parallel lists", on="names and marks kept in two separate lists",
           src='''
names = ["Asha", "Ravi", "Meera"]
marks = [91, 78, 85]
for i in range(len(names)):
    print(names[i], marks[i])
best = marks.index(max(marks))
print("Top:", names[best])
''',
           narr="[HL 1] One list of names. [HL 2] Another list of marks. The two lists match only by position. [HL 3] We loop with an index. [HL 4] And print both lists at the same position. Asha ninety one, Ravi seventy eight, Meera eighty five. [HL 5] Find the position of the best mark. [HL 6] And look up the name at that position. Asha. It works, but only while the two lists stay perfectly in step."),
    c2=dict(label="Two cupboards, one student", on="A student whose name is in cupboard one and marks in cupboard two, then a single folder holding both", narr="Here is the problem. The name of Asha sits in one cupboard. Her marks sit in another. If you sort one cupboard, or delete from one, the match breaks, and Asha gets Ravi's marks. A class puts both into one folder. When you move the folder, everything inside moves together. That is the whole idea of bundling.", anim="Two cupboards with labelled drawers, an arrow pairs them by position, then both drawers merge into one folder"),
    B=dict(file="firstclass.py", label="A first tiny class", on="one class, two objects",
           src='''
class Student:
    pass

a = Student()
a.name = "Asha"
a.marks = 91
b = Student()
b.name = "Ravi"
b.marks = 78
print(a.name, a.marks)
print(b.name, b.marks)
''',
           narr="[HL 1] The word class starts a blueprint. The name is Student, with a capital letter. [HL 2] Pass means, nothing inside yet. [HL 4] Student with brackets builds one object, tied to a. [HL 5] We give it a name. [HL 6] And marks. [HL 7] A second student, tied to b. [HL 8] With its own name. [HL 9] And its own marks. [HL 10] Each object keeps its own data. Asha ninety one. [HL 11] Ravi seventy eight. Next episodes make this tidier."),
    term="Asha 91, then Ravi 78.",
    recap=["Parallel lists only match by position, so they break easily.", "A class is a blueprint for one type of thing.", "An object is one real thing built from the class.", "Each object keeps its own data."],
    bug=dict(title="parallel lists out of sync", kind="output", file="sync.py", wrong='''
names = ["Asha", "Ravi", "Meera"]
marks = [91, 78, 85]
names.sort(reverse=True)
for i in range(len(names)):
    print(names[i], marks[i])
''', fixed='''
students = [("Asha", 91), ("Ravi", 78), ("Meera", 85)]
students.sort(reverse=True)
for name, mark in students:
    print(name, mark)
''', wrong_note="Ravi has Asha's marks now", fixed_note="each name travels with its marks",
             why="Sorting one list moved the names but not the marks, so the pairs broke. Keeping each name and mark together in one bundle makes that impossible.",
             narr="Bug of the Day. We sort only the names. The marks stay where they were. Now Ravi is shown with ninety one, which belongs to Asha. No error appears. You get only wrong answers. That is the worst type of bug. Keep each name and its marks together in one bundle, and they can never drift apart."),
    pun="Why did the two lists break up? They could never stay in step.",
    task="bundle your own data", challenge="Make a class called Book, and two objects. Give each a title and a price, and print them.",
    answer="class Book: pass. Then b1 = Book(), b1.title = ..., b1.price = ..., and the same for b2. Print the attributes.",
    shorts=[
        ("Parallel lists", "Two lists, one for names, one for marks. They match only by position. Sort one list, and the match is gone. Asha gets Ravi's marks, and Python says nothing. Parallel lists are fragile. There is a better way, and it is called a class.", "Two lists + sort = wrong pairs", "Parallel lists break easily."),
        ("What is a class", "A class is a blueprint. It describes one type of thing, such as a student, a book or a bank account. Think of a cookie cutter. The cutter is the class. Each cookie you press out is an object. One blueprint, as many objects as you like.", "class = blueprint", "A class is a blueprint."),
        ("What is an object", "An object is one real thing made from a class. Write the class name with brackets, and Python builds one. Student with brackets gives a student. Do it twice, and you get two separate students. Each keeps its own name and its own marks.", "Student() builds an object", "An object is one thing made from a class."),
        ("The silent bug", "Here is a sneaky bug. You sort the names list, but not the marks list. No error appears. The output simply pairs the wrong name with the wrong marks. Silent bugs are the hardest. Keep each name and its marks in one bundle, and this cannot happen.", "No error, wrong answer", "Silent bugs are the worst."),
        ("Pun and challenge", "Why did the two lists break up? They could never stay in step. Your challenge. Make a class called Book, and two objects. Give each a title and a price, then print them. Write class, a name, and pass. Then set the attributes with a dot. Show me your books.", "Challenge: class Book", "Make two Book objects."),
    ],
))

EPISODES.append(dict(
    n=62, title="Classes and objects", spoken="classes and objects",
    yt="Python Classes and Objects Explained", thumb="CLASS + OBJECT",
    vis="Xecxec pressing cookies from a cutter labelled Dog",
    goals=["write a class with a method", "create objects from a class", "see that each object has its own data"],
    tags=["python class and object", "python self explained", "python create object", "python class tutorial"],
    hash=["#python", "#classes"],
    analogy="a cookie cutter and the cookies: one cutter, many cookies, each cookie its own",
    c_title="Blueprint and things",
    c_pts=["class Name: starts the blueprint", "Name() creates an object", "def inside a class makes a method"],
    intro="Last time we bundled data in a class. Today we add actions, called methods, and meet self.",
    concept="A class is a blueprint, and an object is one thing built from it. Inside a class, you write functions with def. These are called methods. Every method takes a first parameter, named self. Self means, this very object. When you call dog dot bark, Python passes the dog in as self for you. So you never type self when calling, but you always type it when defining. Think of a cookie cutter and cookies. Each cookie is separate, but all come from one cutter.",
    A=dict(file="dog.py", label="A class with a method", on="a Dog class and two dogs",
           src='''
class Dog:
    def bark(self):
        print("Woof!")

d1 = Dog()
d2 = Dog()
d1.bark()
d2.bark()
print(type(d1).__name__)
print(d1 is d2)
''',
           narr="[HL 1] The blueprint is called Dog. [HL 2] A method, written with def, inside the class. It takes self, which means, this dog. [HL 3] It prints Woof. [HL 5] Dog with brackets builds one dog, tied to d1. [HL 6] And another, tied to d2. [HL 7] Call bark on the first dog. We write no argument, Python passes the dog as self. Woof. [HL 8] The second dog barks too. [HL 9] The type name is Dog. [HL 10] And d1 is d2 is False. Two separate objects."),
    mem=dict(label="Two names, two objects", on="The names d1 and d2 tied to two separate Dog objects", names=["d1", "d2"], **{"from": "A"},
             narr="Here is the picture. The name d1 is tied to one dog object. The name d2 is tied to another. They look the same, but they are two separate objects in memory. Both come from the same class, so both know how to bark. Changing one does not touch the other."),
    B=dict(file="counter.py", label="Methods that use self", on="a method that changes the object",
           src='''
class Counter:
    def hit(self):
        self.count = 0

    def add(self):
        self.count = self.count + 1

c = Counter()
c.hit()
c.add()
c.add()
print(c.count)
d = Counter()
d.hit()
print(d.count)
''',
           narr="[HL 1] A Counter class. [HL 2] A method named hit. [HL 3] It sets the count of this object to zero. Self dot count is data stored inside the object. [HL 5] A second method. [HL 6] It adds one to this object's count. [HL 8] Build a counter, tied to c. [HL 9] Set its count to zero. [HL 10] Add one. [HL 11] And again. [HL 12] Print two. [HL 13] A second counter. [HL 14] Reset. [HL 15] Its count is zero. The first counter is unchanged."),
    term="Woof twice, Dog, False. Then two, then zero.",
    recap=["A class is a blueprint; Dog() builds an object.", "Functions inside a class are called methods.", "The first parameter of a method is self: this object.", "Each object keeps its own data."],
    bug=dict(title="missing self", file="dog.py", wrong='''
class Dog:
    def bark():
        print("Woof!")

d = Dog()
d.bark()
''', fixed='''
class Dog:
    def bark(self):
        print("Woof!")

d = Dog()
d.bark()
''', wrong_note="bark has no self parameter", fixed_note="self added",
             why="Python passes the object as the first argument when you call d.bark(), so the method must have a parameter ready to receive it.",
             narr="Bug of the Day. We forgot self in the definition. Calling d dot bark still passes the dog as the first argument. Python says, type error, bark takes zero positional arguments but one was given. The fix is simple. Put self as the first parameter of every method."),
    pun="Why did the dog sit in the class? It wanted to learn some new tricks.",
    task="make a Cat class", challenge="Write a Cat class with a method meow that prints Meow. Create two cats and call meow on each.",
    answer="class Cat: def meow(self): print(\"Meow\"). Then c1 = Cat(), c2 = Cat(), c1.meow(), c2.meow().",
    shorts=[
        ("Class and object", "A class is a blueprint, and an object is one thing built from it. Write class Dog, then Dog with brackets, and Python builds a dog. Build two, and you get two separate dogs. One blueprint, many objects.", "Dog() makes a dog", "One class, many objects."),
        ("What is self", "Self means, this very object. Every method takes self as its first parameter. When you call d dot bark, Python passes the dog d in as self, for free. You write self when defining, and never when calling.", "self = this object", "Self means this object."),
        ("Methods", "A function inside a class is called a method. It describes something the object can do. A dog can bark. A counter can add one. Define it with def, add self first, and call it with a dot after the object.", "def inside a class = method", "Methods are actions."),
        ("Missing self", "Here is a very common bug. You write def bark with empty brackets. Then d dot bark says, type error, takes zero positional arguments but one was given. Python passed the dog, but nothing was waiting for it. Add self as the first parameter.", "TypeError: takes 0 positional arguments", "Always add self."),
        ("Pun and challenge", "Why did the dog sit in the class? It wanted to learn some new tricks. Your challenge. Write a Cat class with a method called meow. It prints Meow. Build two cats and call meow on each. Remember self. Show me your cats.", "Challenge: Cat class", "Write a Cat class."),
    ],
))

EPISODES.append(dict(
    n=63, title="__init__ and attributes", spoken="dunder init and attributes",
    yt="Python __init__ and Attributes Explained", thumb="__INIT__",
    vis="Xecxec stamping name and marks onto a new student card",
    goals=["write an __init__ method", "store data in self attributes", "pass arguments when creating an object"],
    tags=["python __init__", "python constructor", "python self attributes", "python class init"],
    hash=["#python", "#init"],
    analogy="a form that every new student fills in at the door, before they enter the class",
    c_title="The setup method",
    c_pts=["__init__ runs when the object is created", "self.name = name stores data on the object", "Arguments go in the brackets of the class name"],
    intro="Setting attributes one by one is slow and error-prone. Today a special method sets them up for us.",
    concept="Python has a special method named init, with two underscores on each side. It runs automatically, the moment an object is created. Inside it, you store data on the object with self dot name equals name. The words after self are the arguments you pass when you build the object. Think of a form every new student fills in at the door. Nobody enters the class without name and marks. The values stored on the object are called attributes.",
    A=dict(file="student.py", label="Setting up with __init__", on="a Student built with a name and marks",
           src='''
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

a = Student("Asha", 91)
b = Student("Ravi", 78)
print(a.name, a.marks)
print(b.name, b.marks)
a.marks = 95
print(a.marks, b.marks)
''',
           narr="[HL 1] The Student blueprint. [HL 2] The special method init. Self first, then the values we want. [HL 3] Store the name on this object. [HL 4] Store the marks on this object. [HL 6] Build a student with a name and marks. Python calls init for us, and passes the arguments after self. [HL 7] A second student. [HL 8] Asha ninety one. [HL 9] Ravi seventy eight. [HL 10] We can change an attribute later. [HL 11] Asha is now ninety five, and Ravi is still seventy eight."),
    mem=dict(label="Attributes live inside each object", on="The names a and b tied to two Student objects, each holding its own name and marks", names=["a", "b"], **{"from": "A"},
             narr="Here is the picture. The name a is tied to one student object. Inside it live two attributes, name and marks. The name b is tied to another student, with its own attributes. Same blueprint, different data. Init filled both objects in, at the moment they were born."),
    B=dict(file="rectangle.py", label="Defaults and a method", on="init with a default value, and a method that uses the attributes",
           src='''
class Rectangle:
    def __init__(self, width, height=1):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

r1 = Rectangle(4, 3)
r2 = Rectangle(5)
print(r1.area())
print(r2.area())
print(r2.height)
''',
           narr="[HL 1] A Rectangle class. [HL 2] Init takes a width, and a height that defaults to one. [HL 3] Store the width. [HL 4] Store the height. [HL 6] A method named area. [HL 7] It multiplies the two attributes of this object, and returns the answer. [HL 9] Four by three. [HL 10] Five, with the default height of one. [HL 11] Twelve. [HL 12] Five. [HL 13] And the default height is one."),
    term="Asha 91, Ravi 78, then 95 78. Then 12, 5 and 1.",
    recap=["__init__ runs automatically when an object is created.", "self.name = name stores data on the object.", "Arguments in Student(...) go to __init__ after self.", "Default values work just like in functions."],
    bug=dict(title="forgot self. on the attribute", file="student.py", wrong='''
class Student:
    def __init__(self, name):
        name = name

s = Student("Asha")
print(s.name)
''', fixed='''
class Student:
    def __init__(self, name):
        self.name = name

s = Student("Asha")
print(s.name)
''', wrong_note="name = name makes only a local variable", fixed_note="self.name stores it on the object",
             why="Without self. the value is stored in a local variable that disappears when init ends. Only self.name = ... puts data on the object.",
             narr="Bug of the Day. We wrote name equals name, without self dot. That creates a plain local variable, which vanishes when init ends. The object has no name at all. So s dot name raises an attribute error, Student object has no attribute name. Always write self dot, to store data on the object."),
    pun="Why was the object so well prepared? It always had a good init.",
    task="build a Book class", challenge="Write a Book class whose init takes a title and a price. Add a method discount(percent) that returns the reduced price.",
    answer="class Book: def __init__(self, title, price): self.title = title; self.price = price. def discount(self, percent): return self.price * (100 - percent) / 100.",
    shorts=[
        ("What is init", "Init is a special method with two underscores on each side. Python runs it automatically, right when an object is created. Use it to set up the object's data. Think of a form every new student fills in at the door.", "__init__ runs on creation", "Init sets up the object."),
        ("self dot name", "Inside init, write self dot name equals name. That stores the value on the object, as an attribute. Without the self dot, the value is only a local variable, and it vanishes. Self dot is what makes data stick to the object.", "self.name = name", "Self dot makes data stick."),
        ("Passing arguments", "When you write Student with Asha and ninety one in brackets, Python builds the object and calls init. The two values go into init after self. Each object you build gets its own name and marks, stored in its own attributes.", "Student(\"Asha\", 91)", "Arguments go to init."),
        ("The missing self", "A silent beginner bug. In init you write name equals name, with no self dot. No error yet. Later you print s dot name, and Python says, attribute error, Student object has no attribute name. The value was never stored on the object.", "AttributeError: no attribute 'name'", "Always write self dot."),
        ("Pun and challenge", "Why was the object so well prepared? It always had a good init. Your challenge. Write a Book class. Init takes a title and a price. Add a method called discount that takes a percent and returns the lower price. Test it on one book.", "Challenge: Book with discount", "Write a Book class."),
    ],
))

EPISODES.append(dict(
    n=64, title="Methods", spoken="methods",
    yt="Python Methods: Give Objects Actions", thumb="METHODS",
    vis="Xecxec pressing buttons on a bank machine labelled deposit and withdraw",
    goals=["write methods that change an object", "return values from methods", "call methods with the right brackets"],
    tags=["python methods", "python class methods", "python self methods", "python bank account class"],
    hash=["#python", "#methods"],
    analogy="buttons on a vending machine: pressing one makes the machine do something to its own insides",
    c_title="Objects that do things",
    c_pts=["A method is a function that belongs to a class", "Methods change self's attributes", "Call with brackets: obj.method()"],
    intro="So far our objects only held data. Today they get actions, and can change themselves.",
    concept="A method is a function that lives inside a class. It can read and change the attributes of its object through self. Some methods return an answer. Others just change the object, and return nothing. A bank account is a good example. Deposit adds to the balance. Withdraw takes from it. Think of buttons on a vending machine. Each button changes the machine's own insides. To call a method, always use brackets, even with no arguments.",
    A=dict(file="account.py", label="Deposit and withdraw", on="a bank account that changes its own balance",
           src='''
class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdraw(self, amount):
        if amount > self.balance:
            return False
        self.balance = self.balance - amount
        return True

acc = Account("Asha", 100)
acc.deposit(50)
print(acc.balance)
print(acc.withdraw(500))
print(acc.withdraw(30))
print(acc.balance)
''',
           narr="[HL 1] An Account class. [HL 2] Init stores the owner and a starting balance. [HL 6] The deposit method adds the amount to this account's balance. [HL 9] Withdraw first checks the amount. [HL 10] Too much, so return False, and change nothing. [HL 12] Otherwise subtract the amount. [HL 13] And return True. [HL 15] An account for Asha, with one hundred. [HL 16] Deposit fifty. [HL 17] The balance is one fifty. [HL 18] Withdrawing five hundred fails, False. [HL 19] Withdrawing thirty works, True. [HL 20] The balance is one twenty."),
    mem=dict(label="One account object", on="The name acc tied to one Account object holding the owner and the balance", names=["acc"], **{"from": "A"},
             narr="Here is the picture. The name acc is tied to one account object. Inside live the owner and the balance. Each method call changes the balance inside this one object. The name stays the same, and the object quietly changes. That is the point of methods. The object looks after its own data."),
    B=dict(file="temperature.py", label="Methods that return", on="a method that returns a computed value, and one that calls another method",
           src='''
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    def to_fahrenheit(self):
        return self.celsius * 9 / 5 + 32

    def describe(self):
        f = self.to_fahrenheit()
        return f"{self.celsius}C is {f}F"

t = Temperature(100)
print(t.to_fahrenheit())
print(t.describe())
print(Temperature(0).describe())
''',
           narr="[HL 1] A Temperature class. [HL 2] Init stores the Celsius value. [HL 5] A method that converts. [HL 6] Nine fifths of the value, plus thirty two. [HL 8] A second method. [HL 9] It calls the first one through self, to reuse it. [HL 10] And builds a sentence. [HL 12] A hundred degrees. [HL 13] Two hundred twelve. [HL 14] The describe method gives the full sentence. [HL 15] And zero degrees makes thirty two."),
    term="150, False, True, 120. Then 212.0 and the two sentences.",
    recap=["Methods are functions inside a class.", "They use self to read and change the object's attributes.", "A method can return a value, or just change the object.", "Always call a method with brackets."],
    bug=dict(title="calling a method without brackets", kind="output", file="account.py", wrong='''
class Account:
    def __init__(self, balance):
        self.balance = balance

    def show(self):
        return f"Balance: {self.balance}"

acc = Account(100)
print(acc.show)
''', fixed='''
class Account:
    def __init__(self, balance):
        self.balance = balance

    def show(self):
        return f"Balance: {self.balance}"

acc = Account(100)
print(acc.show())
''', wrong_note="show has no brackets", fixed_note="show() actually runs the method",
             why="Without brackets you get the method object itself, not the result of running it. Brackets are what call it.",
             narr="Bug of the Day. We wrote acc dot show, with no brackets. Python does not run the method. It prints the method itself, a bound method, with a memory address. No error, and no answer. Add the brackets, and the method runs, and returns the balance."),
    pun="Why did the method go to therapy? It had too many unresolved calls.",
    task="a safer deposit", challenge="Change deposit so that it ignores amounts that are zero or negative, and returns False for them. Return True for a good deposit.",
    answer="def deposit(self, amount): if amount <= 0: return False; self.balance += amount; return True.",
    shorts=[
        ("Methods are actions", "A method is a function that belongs to a class. It gives an object things to do. A bank account can deposit and withdraw. Think of the buttons on a vending machine. Each button changes the machine's own insides.", "method = action of an object", "Methods are actions."),
        ("Methods change self", "Inside a method, self dot balance means, this account's balance. Write self dot balance equals self dot balance plus amount, and this one account changes. Other accounts stay untouched. Each object looks after its own data.", "self.balance += amount", "Methods change the object."),
        ("Return a value", "Methods can return answers, just like functions. A temperature object can return its value in Fahrenheit. A withdraw method can return True when it worked, and False when it failed. The caller decides what to do with the answer.", "return True / False", "Methods can return values."),
        ("No brackets", "A tricky one. You write acc dot show, without brackets. Python prints bound method show of account object, and an address. It did not run the method. It showed it. Add the brackets, and the method actually runs.", "acc.show vs acc.show()", "Brackets call the method."),
        ("Pun and challenge", "Why did the method go to therapy? It had too many unresolved calls. Your challenge. Change deposit so that it ignores zero and negative amounts. Return False for those, and True for a good deposit. Test it with a few numbers.", "Challenge: safer deposit", "Make deposit safer."),
    ],
))

EPISODES.append(dict(
    n=65, title="Class vs instance attributes", spoken="class versus instance attributes",
    yt="Python Class vs Instance Attributes", thumb="CLASS vs INSTANCE",
    vis="Xecxec with one shared notice board and many private notebooks",
    goals=["tell class attributes from instance attributes", "see which data is shared", "avoid a shared mutable list"],
    tags=["python class attribute", "python instance attribute", "python shared list bug", "python class variable"],
    hash=["#python", "#classes"],
    analogy="a school notice board that everyone sees, versus each student's private notebook",
    c_title="Shared or private?",
    c_pts=["Class attribute: written in the class body, shared by all", "Instance attribute: self.x, private to one object", "A shared list is shared by everyone"],
    intro="Some data belongs to the whole class, some to each object. Mixing them up causes a famous bug.",
    concept="Data can live in two places. A class attribute is written directly in the class body. All objects share it. Think of a school notice board that everyone can see. An instance attribute is set with self dot, inside init. Each object has its own copy, like a private notebook. Numbers and strings are safe either way, because assigning replaces them. But a list stored on the class is one single list, shared by every object. That is where the trouble starts.",
    A=dict(file="shared.py", label="Class and instance attributes", on="a class attribute shared by all dogs, and a list that is shared too",
           src='''
class Dog:
    species = "Canis"
    tricks = []

    def __init__(self, name):
        self.name = name

    def learn(self, trick):
        self.tricks.append(trick)

d1 = Dog("Rex")
d2 = Dog("Fido")
d1.learn("sit")
d2.learn("roll")
t1 = d1.tricks
t2 = d2.tricks
print(d1.species, d2.species)
print(t1)
print(t1 is t2)
''',
           narr="[HL 1] A Dog class. [HL 2] Species is a class attribute. All dogs share it. [HL 3] So is tricks, one single list. [HL 5] Init gives each dog its own name. That one is private. [HL 8] Learn appends a trick to the tricks list. [HL 11] Rex. [HL 12] Fido. [HL 13] Rex learns to sit. [HL 14] Fido learns to roll. [HL 15] Look at the list through Rex. [HL 16] And through Fido. [HL 17] Both dogs say Canis. [HL 18] The list has sit and roll, even though Rex only learned sit. [HL 19] And it is the very same list. True."),
    mem=dict(label="Two names, one shared list", on="The names t1 and t2 tied to the very same list object", names=["t1", "t2"], **{"from": "A"},
             narr="Here is the picture. The names t1 and t2 look like two lists, but they are two names tied to one single list object. That is why the tricks of Rex show up for Fido too. When two names are tied to one object, changing it through one name changes it for both. Remember this picture. It explains the whole bug."),
    B=dict(file="private.py", label="Each dog gets its own list", on="create the list inside init",
           src='''
class Dog:
    species = "Canis"

    def __init__(self, name):
        self.name = name
        self.tricks = []

    def learn(self, trick):
        self.tricks.append(trick)

d1 = Dog("Rex")
d2 = Dog("Fido")
d1.learn("sit")
d2.learn("roll")
print(d1.tricks)
print(d2.tricks)
print(d1.tricks is d2.tricks)
''',
           narr="[HL 1] The same Dog class. [HL 2] Species stays a class attribute, because it really is shared. [HL 5] Init sets the name. [HL 6] And now builds a brand new list for each dog. [HL 9] Learn appends to this dog's own list. [HL 11] Rex. [HL 12] Fido. [HL 13] Rex learns sit. [HL 14] Fido learns roll. [HL 15] Rex has only sit. [HL 16] Fido has only roll. [HL 17] And the two lists are different objects. False."),
    term="Canis Canis, then sit and roll twice over, True. Then sit, roll, False.",
    recap=["A class attribute is written in the class body and shared by all objects.", "An instance attribute is set with self dot inside init, and is private.", "A list in the class body is one list shared by everyone.", "Create lists inside init, so each object gets its own."],
    bug=dict(title="a list shared between objects", kind="output", file="team.py", wrong='''
class Team:
    members = []

    def __init__(self, name):
        self.name = name

    def add(self, person):
        self.members.append(person)

red = Team("Red")
blue = Team("Blue")
red.add("Asha")
blue.add("Ravi")
print(red.members)
''', fixed='''
class Team:
    def __init__(self, name):
        self.name = name
        self.members = []

    def add(self, person):
        self.members.append(person)

red = Team("Red")
blue = Team("Blue")
red.add("Asha")
blue.add("Ravi")
print(red.members)
''', wrong_note="the list is shared, so Ravi joined Red", fixed_note="each team has its own list",
             why="A list created in the class body is built once and shared by every object. A list created in init is built fresh for each object.",
             narr="Bug of the Day. Ravi joined the blue team, but he shows up in the red team too. The members list is in the class body, so there is only one list, shared by every team. No error appears. The fix is to create the list inside init, so every team gets its own."),
    pun="Why did the list refuse to be shared? It had too many members already.",
    task="spot the shared list", challenge="Write a Student class where every student has a list of grades. Make sure two students do not share one list. Prove it with the is operator.",
    answer="Create self.grades = [] inside __init__. Then s1.grades is s2.grades prints False.",
    shorts=[
        ("Class attribute", "A class attribute is written in the class body. Every object shares it. Think of a notice board in school that everyone can read. If you change it on the class, every object sees the change.", "species = \"Canis\"", "Class attributes are shared."),
        ("Instance attribute", "An instance attribute is set with self dot, inside init. Each object gets its own copy. Think of a private notebook. Rex's name does not change Fido's name. Put the data that differs between objects here.", "self.name = name", "Instance attributes are private."),
        ("Shared list", "Here is the trap. A list written in the class body is one single list. Every object shares it. Add Asha through one object, and she appears in every object. Two names, one list. The memory picture shows it clearly.", "list in class = shared", "Watch for shared lists."),
        ("The fix", "To give every object its own list, create the list inside init. Write self dot members equals empty brackets. Python runs init once for each object, so every object builds a fresh list. Now adding a member only changes one object.", "self.members = [] in __init__", "Make lists in init."),
        ("Pun and challenge", "Why did the list refuse to be shared? It had too many members already. Your challenge. Write a Student class, with a list of grades for each student. Make two students, add a grade to one, and use the is operator to prove the lists are different.", "Challenge: separate grade lists", "Prove the lists differ."),
    ],
))

EPISODES.append(dict(
    n=66, title="__str__ and __repr__", spoken="dunder str and dunder repr",
    yt="Python __str__ and __repr__ Explained", thumb="__STR__",
    vis="Xecxec holding a mystery box, then a neat label reading Student Asha",
    goals=["print an object in a readable way", "write __str__ and __repr__", "know when each one is used"],
    tags=["python __str__", "python __repr__", "python print object", "str vs repr python"],
    hash=["#python", "#dunder"],
    analogy="a name tag: without it the object is a stranger, with it everyone knows who is who",
    c_title="Name tags for objects",
    c_pts=["print(obj) uses __str__", "repr(obj) and the shell use __repr__", "Both must return a string"],
    intro="Printing an object often shows a strange line with a memory address. Today we give objects name tags.",
    concept="By default, an object prints as the class name and a memory address. That is not helpful. You can fix it with two special methods. Str is for people. It is what print uses. Repr is for programmers. It should show the object clearly, ideally as code that could rebuild it. If you only write one, write repr, because str falls back to it. Think of a name tag at a party. Without it, nobody knows who you are.",
    A=dict(file="point.py", label="Str and repr", on="a Point that prints nicely",
           src='''
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

p = Point(3, 4)
print(p)
print(repr(p))
print([p, Point(0, 0)])
print(f"Corner: {p}")
''',
           narr="[HL 1] A Point class. [HL 2] Init stores x and y. [HL 6] Str is the friendly version. [HL 7] It returns the text, three comma four, in brackets. [HL 9] Repr is the exact version. [HL 10] It returns Point of three comma four, which looks like the code that built it. [HL 12] A point at three, four. [HL 13] Print uses str. [HL 14] Repr gives the exact one. [HL 15] A list shows each item with repr. [HL 16] And an f string uses str."),
    mem=dict(label="One object, two descriptions", on="The name p tied to one Point object; str shows it for people, repr for programmers", names=["p"], **{"from": "A"},
             narr="Here is the picture. The name p is tied to one point object. The object does not change. What changes is the description. Print asks for the friendly string, and the shell, and lists, ask for the exact one. Both come from the same object. You only choose how it introduces itself."),
    B=dict(file="onlyrepr.py", label="Only repr", on="repr alone is enough; str falls back to it",
           src='''
class Book:
    def __init__(self, title):
        self.title = title

    def __repr__(self):
        return f"Book({self.title!r})"

b = Book("Python")
print(b)
print(str(b))
print([b])
''',
           narr="[HL 1] A Book class. [HL 2] Init stores the title. [HL 5] Only repr is written. [HL 6] The exclamation r asks for the repr of the title, so quotes appear. [HL 8] A book. [HL 9] Print has no str to use, so it falls back to repr. [HL 10] And str gives the same. [HL 11] A list shows the same text. One method, and every place is tidy."),
    term="Three comma four, then Point of three comma four, a list of two points, then Corner three comma four. Then the book Python three times.",
    recap=["print(obj) calls __str__, for people.", "repr(obj) and lists call __repr__, for programmers.", "If only __repr__ exists, str falls back to it.", "Both methods must return a string."],
    bug=dict(title="printing an object shows an address", kind="output", file="point.py", wrong='''
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(3, 4)
print(p)
''', fixed='''
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

p = Point(3, 4)
print(p)
''', wrong_note="no __str__ or __repr__", fixed_note="__repr__ added",
             why="Without these methods, Python falls back to the default text: the class name and a memory address. Adding repr gives a readable description.",
             narr="Bug of the Day. We print a point, and get the class name with at, and a long memory address. Nothing is wrong with the object. It just has no name tag. Add a repr method that returns a readable string, and print shows Point of three comma four."),
    pun="Why did the object need a repr? It had an identity crisis.",
    task="give Student a name tag", challenge="Write a Student class with a name and marks. Add __str__ so that print shows Asha: 91.",
    answer="def __str__(self): return f\"{self.name}: {self.marks}\".",
    shorts=[
        ("Ugly print", "Print an object, and you may see the class name with at, and a long memory address. That is Python's default. It is correct, but it is useless to people. We can do better with two special methods.", "<Point object at 0x...>", "Default print is ugly."),
        ("str for people", "Write a method called dunder str. It returns a friendly string. Print and f strings use it. For a point, return three comma four. Now print p shows the nice version, with no address in sight.", "__str__ = friendly", "Str is for people."),
        ("repr for programmers", "Write dunder repr for programmers. It should look like the code that builds the object, such as Point of three comma four. Lists, the shell, and debugging all use repr. It is the exact version of the description.", "__repr__ = exact", "Repr is for programmers."),
        ("Only one", "If you write only one, write repr. When str is missing, Python uses repr instead. So one tiny method makes print, lists and the shell all tidy. The default address text only appears when you write neither.", "repr is the fallback", "Write repr first."),
        ("Pun and challenge", "Why did the object need a repr? It had an identity crisis. Your challenge. Write a Student class with a name and marks. Add dunder str, so that print shows Asha, colon, ninety one. Make two students and print them both.", "Challenge: Student __str__", "Write a __str__."),
    ],
))

EPISODES.append(dict(
    n=67, title="Inheritance", spoken="inheritance",
    yt="Python Inheritance Explained Simply", thumb="INHERITANCE",
    vis="Xecxec handing a family recipe book from parent crab to child crab",
    goals=["write a child class from a parent class", "reuse parent attributes and methods", "call super().__init__"],
    tags=["python inheritance", "python super init", "python parent child class", "python oop inheritance"],
    hash=["#python", "#inheritance"],
    analogy="a family recipe book: children get all the recipes, and can add their own",
    c_title="Parent and child",
    c_pts=["class Child(Parent): inherits everything", "The child can add new methods", "super().__init__() runs the parent's setup"],
    intro="Dogs, cats and birds are all animals. Today we write the shared part once, and reuse it.",
    concept="Inheritance lets one class build on another. The parent class holds what is common. The child class gets all of it for free, and can add more. Write the parent's name in brackets after the child's name. If the child has its own init, it must call super dot init, to run the parent's setup too. Otherwise the parent's attributes are never created. Think of a family recipe book. The child gets every recipe, and adds new ones.",
    A=dict(file="animals.py", label="A child class", on="Dog inherits from Animal",
           src='''
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(self.name, "is eating")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def bark(self):
        print(self.name, "says Woof")

d = Dog("Rex", "Labrador")
d.eat()
d.bark()
print(d.breed)
''',
           narr="[HL 1] The parent class, Animal. [HL 2] Its init stores a name. [HL 5] And a method named eat. [HL 8] Dog, with Animal in brackets. Dog inherits from Animal. [HL 9] Dog has its own init, with a breed too. [HL 10] Super dot init runs the parent's init, so the name is stored. [HL 11] Then the breed is stored. [HL 13] A method only dogs have. [HL 16] Build a dog. [HL 17] Eat comes from the parent. Rex is eating. [HL 18] Bark comes from the child. [HL 19] And the breed is Labrador."),
    c2=dict(label="The family tree", on="Animal at the top with Dog and Cat below it; methods flow down the arrows", narr="Here is the family tree. Animal sits at the top, and holds the shared parts, name and eat. Dog and Cat hang below it. Everything flows down the arrows. A dog can eat, because Animal can eat. A dog can also bark, which Animal cannot. A child gets everything from its parent, and adds more of its own.", anim="A tree with Animal on top, Dog and Cat below, and glowing arrows carrying the eat method downward"),
    B=dict(file="checks.py", label="Is it a kind of?", on="isinstance and issubclass",
           src='''
class Animal:
    pass

class Dog(Animal):
    pass

class Cat(Animal):
    pass

d = Dog()
print(isinstance(d, Dog))
print(isinstance(d, Animal))
print(isinstance(d, Cat))
print(issubclass(Cat, Animal))
print(Dog.__bases__[0].__name__)
''',
           narr="[HL 1] An empty Animal class. [HL 4] Dog inherits from Animal. [HL 7] And so does Cat. [HL 10] One dog. [HL 11] Is it a Dog? True. [HL 12] Is it an Animal? Also True. A dog is a type of animal. [HL 13] Is it a Cat? False. [HL 14] Is Cat a subclass of Animal? True. [HL 15] And the parent of Dog is named Animal."),
    term="Rex is eating, Rex says Woof, Labrador. Then True, True, False, True, Animal.",
    recap=["class Child(Parent): inherits all of the parent's methods.", "The child can add its own attributes and methods.", "super().__init__() runs the parent's setup.", "isinstance(obj, Parent) is True for child objects too."],
    bug=dict(title="forgot super().__init__()", file="animals.py", wrong='''
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        self.breed = breed

d = Dog("Rex", "Labrador")
print(d.name)
''', fixed='''
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

d = Dog("Rex", "Labrador")
print(d.name)
''', wrong_note="Dog's init replaces Animal's init", fixed_note="super().__init__(name) added",
             why="When a child defines its own init, it replaces the parent's. The parent's setup only runs if the child calls super().__init__().",
             narr="Bug of the Day. Dog has its own init, which replaces the parent's init. So the name is never stored. Printing d dot name raises an attribute error, Dog object has no attribute name. The fix is one line. Call super dot init, with the name, at the start of the child's init."),
    pun="Why did the child class get all the money? It inherited everything.",
    task="add a Cat", challenge="Add a Cat class that inherits from Animal, and has a method meow. Make a cat, and call eat and meow on it.",
    answer="class Cat(Animal): def meow(self): print(self.name, \"says Meow\"). Then c = Cat(\"Tom\"), c.eat(), c.meow().",
    shorts=[
        ("What is inheritance", "Inheritance means a class builds on another class. The parent holds what is common. The child gets all of it for free. Think of a family recipe book. Children get every recipe, and then add their own.", "class Dog(Animal)", "Children inherit from parents."),
        ("Write a child class", "To make a child class, write the parent's name in brackets after the child's name. Class Dog, brackets, Animal. Now every dog can use every method of Animal, without a single copied line. Write shared code once, in the parent.", "class Dog(Animal):", "Write shared code once."),
        ("super init", "If the child has its own init, call super dot init, with the arguments the parent needs. That runs the parent's setup first. Then the child adds its own attributes. Super means, my parent. It saves you repeating the parent's code.", "super().__init__(name)", "Super means my parent."),
        ("The missing super", "A classic bug. The child writes its own init, and forgets super dot init. The parent's setup never runs. Later, d dot name raises, attribute error, no attribute name. A child's init replaces the parent's. Call super, and the name appears.", "AttributeError: no attribute 'name'", "Do not forget super."),
        ("Pun and challenge", "Why did the child class get all the money? It inherited everything. Your challenge. Add a Cat class that inherits from Animal. Give it a method called meow. Make a cat, and call both eat and meow on it. Which one comes from the parent?", "Challenge: add a Cat", "Add a Cat class."),
    ],
))

EPISODES.append(dict(
    n=68, title="Overriding and super()", spoken="overriding and super",
    yt="Python Method Overriding and super() Explained", thumb="OVERRIDE",
    vis="Xecxec singing the family song, but changing the last line",
    goals=["override a parent method in a child", "extend a method with super()", "call the parent's method correctly"],
    tags=["python method overriding", "python super", "python override method", "python oop super function"],
    hash=["#python", "#super"],
    analogy="a family song: the child sings the same tune but changes a verse, or sings the old verse and adds a new one",
    c_title="Change or extend",
    c_pts=["Same method name in the child replaces the parent's", "super().method() runs the parent's version", "Python looks in the child first"],
    intro="A child often needs to behave a little differently from its parent. Today we change methods, or extend them.",
    concept="If a child class defines a method with the same name as its parent, the child's version wins. This is called overriding. Python looks in the child first, then in the parent. Sometimes you want both. Call super dot method inside the child's version, to run the parent's code first, and then add more. Think of a family song. The child sings the same tune, but changes a verse, or sings the old verse and adds a new one.",
    A=dict(file="override.py", label="Overriding", on="each animal speaks in its own way",
           src='''
class Animal:
    def speak(self):
        return "..."

class Dog(Animal):
    def speak(self):
        return "Woof"

class Fish(Animal):
    pass

print(Animal().speak())
print(Dog().speak())
print(Fish().speak())
''',
           narr="[HL 1] The parent. [HL 2] Its speak method returns three dots. [HL 5] Dog inherits from Animal. [HL 6] And defines its own speak. [HL 7] It returns Woof. [HL 9] Fish inherits, but adds nothing. [HL 12] An animal says three dots. [HL 13] A dog says Woof, because the child's version wins. [HL 14] A fish has no speak of its own, so Python finds the parent's. Three dots."),
    c2=dict(label="Child first, then parent", on="A method call that checks the child class box first, then the parent class box", narr="Here is how Python finds a method. It looks in the object's own class first. If the method is there, it runs. If not, Python walks up to the parent, and checks there. The first match wins. So the child can override the parent, and objects with no override use the parent's version.", anim="A search arrow starts at the Dog box, finds no match for eat, then moves up to the Animal box and lights it"),
    B=dict(file="extend.py", label="Extend with super()", on="call the parent's method and then add more",
           src='''
class Greeter:
    def greet(self):
        return "Hello"

class LoudGreeter(Greeter):
    def greet(self):
        base = super().greet()
        return base.upper() + "!"

print(Greeter().greet())
print(LoudGreeter().greet())
''',
           narr="[HL 1] A parent that greets. [HL 2] Its greet method. [HL 3] Returns Hello. [HL 5] The child. [HL 6] Overrides greet. [HL 7] Super dot greet runs the parent's version, and keeps the result. [HL 8] Then we shout it, and add an exclamation mark. [HL 10] The parent says Hello. [HL 11] The child says HELLO with an exclamation mark. It built on the parent's answer."),
    term="Three dots, Woof, three dots. Then Hello, then HELLO!",
    recap=["A child's method with the same name overrides the parent's.", "Python looks in the child first, then the parent.", "super().method() runs the parent's version.", "Use super() to extend a method, not copy it."],
    bug=dict(title="calling the parent wrongly", file="parent.py", wrong='''
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name):
        Animal.__init__(name)

d = Dog("Rex")
''', fixed='''
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

d = Dog("Rex")
print(d.name)
''', wrong_note="Animal.__init__(name) passes no self", fixed_note="super() passes self automatically",
             why="Calling a method through the class name does not pass self for you. Calling it through super() does, so super() is the safe way.",
             narr="Bug of the Day. We call the parent's init through the class name, and pass only the name. Python needs self as the first argument, and it does not add it here. Our name is taken as self, and the real name is missing. Type error, init missing one required positional argument, name. Use super dot init instead. It passes self for you."),
    pun="Why did the method override its parent? It needed some independence.",
    task="shout the answer", challenge="Make a Dog subclass of Animal whose speak returns the parent's answer followed by the word Woof.",
    answer="def speak(self): return super().speak() + \" Woof\".",
    shorts=[
        ("Overriding", "Overriding means a child defines a method with the same name as the parent's. The child's version wins. A dog's speak returns Woof, while a plain animal's speak returns dots. Same name, different behaviour.", "Child method beats parent", "The child's version wins."),
        ("Python lookup", "How does Python find a method? It looks in the object's own class first. If it is not there, it goes up to the parent, and keeps going up. The first match wins. A fish with no speak of its own simply uses the parent's.", "Child first, then parent", "Python looks up the tree."),
        ("Extend with super", "You do not have to throw away the parent's method. Call super dot speak inside the child's version, to get the parent's answer. Then add your own part. Extending beats copying, because a fix in the parent reaches every child.", "super().greet()", "Extend, do not copy."),
        ("The wrong call", "A frequent mistake. You call Animal dot init with just the name. Python says, type error, init missing one required positional argument, name. Through the class name, self is not passed. Use super dot init, and Python passes self for you.", "TypeError: missing 'name'", "Use super()."),
        ("Pun and challenge", "Why did the method override its parent? It needed some independence. Your challenge. Make a Dog class that inherits from Animal. Its speak method must return the parent's answer, followed by the word Woof. Use super in your answer.", "Challenge: parent answer + Woof", "Extend with super."),
    ],
))

EPISODES.append(dict(
    n=69, title="Polymorphism and duck typing", spoken="polymorphism and duck typing",
    yt="Python Polymorphism and Duck Typing", thumb="DUCK TYPING",
    vis="Xecxec holding a duck mask: if it quacks like a duck, it is a duck",
    goals=["call the same method on different objects", "explain duck typing", "recognise an AttributeError from a missing method"],
    tags=["python polymorphism", "python duck typing", "python oop polymorphism", "attributeerror python"],
    hash=["#python", "#polymorphism"],
    analogy="a remote with a play button: it works on any device that knows how to play, whatever the brand",
    c_title="Same call, many shapes",
    c_pts=["Polymorphism: one call, many behaviours", "Python does not check the class, only the method", "If it quacks like a duck, treat it as a duck"],
    intro="One loop, many kinds of objects, each doing its own thing. That is polymorphism.",
    concept="Polymorphism means many shapes. You call the same method on different objects, and each one responds in its own way. Python goes further. It does not check the class at all. It only asks, does this object have the method I am calling? This is called duck typing. If it walks like a duck, and quacks like a duck, treat it as a duck. Think of a remote with a play button. It works on any device that knows how to play.",
    A=dict(file="shapes.py", label="One loop, many shapes", on="different classes with the same area method",
           src='''
class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return round(3.14159 * self.radius ** 2, 2)

shapes = [Square(3), Circle(2), Square(4)]
for shape in shapes:
    print(type(shape).__name__, shape.area())
''',
           narr="[HL 1] A Square class. [HL 2] Init stores the side. [HL 5] Its area method. [HL 6] Side times side. [HL 8] A Circle class. [HL 9] Init stores the radius. [HL 12] Its own area method. [HL 13] Pi times radius squared, rounded. [HL 15] A list with different kinds of shapes. [HL 16] Loop over them. [HL 17] The same call, shape dot area, on every object. Square nine. Circle twelve point five seven. Square sixteen. No class check anywhere."),
    mem=dict(label="One list, different objects", on="The name shapes tied to a list holding two Square objects and a Circle object", names=["shapes"], **{"from": "A"},
             narr="Here is the picture. The name shapes is tied to one list. Inside the list sit three objects, two squares and a circle. The classes are unrelated, there is no parent class at all. But all three know area, so the loop works. Python cares only about what an object can do, not what it is called."),
    B=dict(file="ducks.py", label="Duck typing", on="a function that works with any object that has speak",
           src='''
class Duck:
    def speak(self):
        return "Quack"

class Robot:
    def speak(self):
        return "Beep"

class Rock:
    pass

def talk(thing):
    return thing.speak()

print(talk(Duck()))
print(talk(Robot()))
print(hasattr(Rock(), "speak"))
''',
           narr="[HL 1] A Duck that can speak. [HL 2] It says Quack. [HL 5] A Robot, with no relation to Duck. [HL 6] It says Beep. [HL 9] A Rock that cannot speak. [HL 12] A function that takes anything. [HL 13] And simply calls speak on it. [HL 15] A duck quacks. [HL 16] A robot beeps. [HL 17] Has attribute asks, does a rock have speak? False. Calling talk on a rock fails."),
    term="Square 9, Circle 12.57, Square 16. Then Quack, Beep, False.",
    recap=["Polymorphism: the same call behaves differently on different objects.", "Python checks only that the method exists.", "That is duck typing: if it quacks, treat it as a duck.", "Use hasattr to test for a method."],
    bug=dict(title="calling a missing method", file="talk.py", wrong='''
class Robot:
    def beep(self):
        return "Beep"

def talk(thing):
    return thing.speak()

print(talk(Robot()))
''', fixed='''
class Robot:
    def speak(self):
        return "Beep"

def talk(thing):
    return thing.speak()

print(talk(Robot()))
''', wrong_note="Robot has beep, but not speak", fixed_note="the method is named speak",
             why="Duck typing only works if the object really has the method you call. Python finds out when the call happens, and raises an AttributeError.",
             narr="Bug of the Day. The talk function calls speak, but our Robot only has a method named beep. Python finds out at the moment of the call. Attribute error, Robot object has no attribute speak. Duck typing needs every object to offer the method that the function calls."),
    pun="Why did the duck get promoted? It really knew how to quack under pressure.",
    task="add a new shape", challenge="Add a Triangle class with a base and a height, and an area method. Add one to the shapes list and run the same loop.",
    answer="class Triangle: def __init__(self, base, height): ...; def area(self): return self.base * self.height / 2.",
    shorts=[
        ("Many shapes", "Polymorphism means many shapes. You call the same method on different objects, and each answers in its own way. Square area, circle area, triangle area. One loop, one call, three different calculations.", "shape.area()", "One call, many behaviours."),
        ("Duck typing", "Python does not ask, what class are you? It asks, do you have the method I want to call? If it walks like a duck, and quacks like a duck, treat it as a duck. The class does not matter at all.", "if it quacks, it is a duck", "Python trusts methods."),
        ("No parent needed", "Notice that Square and Circle share no parent class. They are unrelated. Yet one loop works on both, because both have an area method. Duck typing needs no inheritance. Just the right method name.", "no shared parent needed", "Only the method matters."),
        ("Missing method", "What if an object lacks the method? Calling thing dot speak on a robot that only has beep raises, attribute error, Robot object has no attribute speak. You can test first with hasattr, or just make sure every class offers the method.", "AttributeError: no attribute 'speak'", "Check the method name."),
        ("Pun and challenge", "Why did the duck get promoted? It really knew how to quack under pressure. Your challenge. Add a Triangle class with a base, a height and an area method. Put one in the shapes list, and run the same loop. Did you change the loop?", "Challenge: add a Triangle", "Add a new shape."),
    ],
))

EPISODES.append(dict(
    n=70, title="Encapsulation and properties", spoken="encapsulation and properties",
    yt="Python Encapsulation and @property Explained", thumb="@PROPERTY",
    vis="Xecxec guarding a safe, with a small window showing only the balance",
    goals=["protect data behind a property", "validate values in a setter", "understand the underscore convention"],
    tags=["python encapsulation", "python property decorator", "python getter setter", "python private attribute"],
    hash=["#python", "#property"],
    analogy="a bank counter: you cannot reach into the vault, you ask the clerk, who checks your request",
    c_title="Guard the data",
    c_pts=["A leading underscore means: please do not touch", "@property reads like an attribute but runs code", "A setter can reject bad values"],
    intro="Anyone can set marks to minus five. Today we put a guard in front of our data.",
    concept="Encapsulation means keeping data safe inside the object, and letting outsiders in only through checks. In Python, a name with one leading underscore means, please do not touch directly. A property is the polite doorway. The at property decorator lets you read the value like a plain attribute, while a function runs behind the scenes. A setter, written with at name dot setter, can reject bad values. Think of a bank counter. You cannot reach into the vault. You ask the clerk, who checks first.",
    A=dict(file="marks.py", label="A read-only property", on="a Student whose marks are readable through a property",
           src='''
class Student:
    def __init__(self, name, marks):
        self.name = name
        self._marks = marks

    @property
    def marks(self):
        return self._marks

    @property
    def grade(self):
        return "Pass" if self._marks >= 40 else "Fail"

s = Student("Asha", 91)
print(s.marks)
print(s.grade)
''',
           narr="[HL 1] A Student class. [HL 3] Init stores the name. [HL 4] And the marks, in an attribute with a leading underscore. That says, handle with care. [HL 6] At property turns the next method into an attribute. [HL 7] Marks. [HL 8] It returns the private value. [HL 10] Another property. [HL 11] Grade. [HL 12] It computes Pass or Fail from the marks. [HL 14] A student. [HL 15] We read marks, with no brackets. Ninety one. [HL 16] And grade, also with no brackets. Pass. The grade is never stored. It is worked out every time."),
    c2=dict(label="The clerk at the counter", on="A person at a counter takes requests, checks them, then reaches into a locked vault", narr="Here is the picture. The vault holds the real data. Outsiders cannot reach it directly. They talk to the clerk, which is the property. The clerk reads the value for you, or checks your new value before storing it. If your request is bad, the clerk refuses. That is encapsulation. The rules live in one place, next to the data.", anim="A vault box labelled _marks behind a counter; request cards pass through a clerk box and either get stamped or rejected"),
    B=dict(file="setter.py", label="A setter that checks", on="reject bad marks",
           src='''
class Student:
    def __init__(self, marks):
        self.marks = marks

    @property
    def marks(self):
        return self._marks

    @marks.setter
    def marks(self, value):
        if not 0 <= value <= 100:
            raise ValueError("marks must be 0 to 100")
        self._marks = value

s = Student(80)
s.marks = 95
print(s.marks)
try:
    s.marks = -5
except ValueError as e:
    print(e)
print(s.marks)
''',
           narr="[HL 1] A Student class. [HL 2] Init sets marks. [HL 3] Because marks is a property, this goes through the setter. [HL 5] The property. [HL 6] It returns the stored value. [HL 9] The setter, named after the property. [HL 11] It checks the range. [HL 12] A bad value raises a value error. [HL 13] A good value is stored. [HL 15] Eighty. [HL 16] Change to ninety five. [HL 17] It prints ninety five. [HL 19] Now try minus five. [HL 20] The setter refuses. [HL 21] And prints our message. [HL 22] The old value is safe. Ninety five."),
    term="91, Pass. Then 95, the message, and 95 again.",
    recap=["A leading underscore means: do not touch directly.", "@property lets a method be read like an attribute.", "A setter checks a value before storing it.", "Computed values can be properties too."],
    bug=dict(title="a property with no setter", file="item.py", wrong='''
class Item:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price

item = Item(50)
item.price = 60
''', fixed='''
class Item:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value

item = Item(50)
item.price = 60
print(item.price)
''', wrong_note="price has a getter only", fixed_note="a setter is added",
             why="A property with only a getter is read-only. To allow assignment, add a setter with the same name.",
             narr="Bug of the Day. Price is a read-only property, because it has no setter. Assigning item dot price equals sixty fails. Attribute error, property price of Item object has no setter. Add a setter with the same name, and assignment works. Or leave it out on purpose, to make the value read-only."),
    pun="Why did the property get a setter? Because it was tired of being read-only.",
    task="protect the price", challenge="Write an Item class whose price property rejects negative values with a ValueError.",
    answer="Use @property price, and @price.setter with if value < 0: raise ValueError(\"price must not be negative\").",
    shorts=[
        ("Encapsulation", "Encapsulation means keeping data safe inside the object. Outsiders go through checks. Think of a bank. You do not reach into the vault. You ask the clerk, who checks your request first. Your class can be the clerk.", "keep data behind a guard", "Guard your data."),
        ("The underscore", "In Python, a name with a leading underscore, like underscore marks, is a polite sign. It says, please do not touch this directly. Python does not stop you. But everyone who reads the code knows the rule.", "_marks = private by habit", "One underscore means careful."),
        ("The property", "At property turns a method into something you read like an attribute, with no brackets. The grade of a student can be worked out from the marks each time. Nothing extra is stored, and nothing can drift out of date.", "@property", "Read it like an attribute."),
        ("No setter", "A property with only a getter is read-only. Try item dot price equals sixty, and Python says, attribute error, property price of Item object has no setter. Want to allow changes? Add a setter with the same name.", "AttributeError: no setter", "Add a setter."),
        ("Pun and challenge", "Why did the property get a setter? Because it was tired of being read-only. Your challenge. Write an Item class with a price property. Its setter must reject negative values by raising a value error. Test it with minus ten.", "Challenge: price setter", "Reject negative prices."),
    ],
))

EPISODES.append(dict(
    n=71, title="Dunder methods", spoken="dunder methods",
    yt="Python Dunder (Magic) Methods Explained", thumb="DUNDER METHODS",
    vis="Xecxec waving a wand over a Point so that plus, equals and len work on it",
    goals=["make objects work with + and ==", "write __len__ and __lt__", "know that __eq__ needs __hash__ for sets"],
    tags=["python dunder methods", "python magic methods", "python __eq__", "python operator overloading"],
    hash=["#python", "#dunder"],
    analogy="secret handshakes: when Python sees a plus sign, it knocks on your object and asks for the add handshake",
    c_title="Python's secret handshakes",
    c_pts=["__add__ makes + work", "__eq__ makes == work", "__len__ makes len() work"],
    intro="How does plus know how to add two numbers? And how can we teach it to add two of our own objects?",
    concept="Dunder methods, short for double underscore, are special names Python looks for. When you write a plus b, Python calls a dot add of b. When you write a equals equals b, it calls eq. And len of a calls len. Define them in your class, and your objects work with operators, just like numbers. Think of secret handshakes. When Python sees a plus, it knocks on your object, and asks for the add handshake.",
    A=dict(file="vector.py", label="Teaching plus and equals", on="a Vector that adds and compares",
           src='''
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

a = Vector(1, 2)
b = Vector(3, 4)
c = a + b
print(c)
print(c == Vector(4, 6))
print(a == b)
''',
           narr="[HL 1] A Vector class. [HL 2] Init stores x and y. [HL 6] Dunder add, the handshake for plus. [HL 7] It returns a new vector, with the sums. [HL 9] Dunder eq, the handshake for equals equals. [HL 10] Equal when both parts match. [HL 12] Repr, so that printing is readable. [HL 15] A vector one, two. [HL 16] And three, four. [HL 17] Plus calls add. [HL 18] We get Vector four, six. [HL 19] Equals compares the parts. True. [HL 20] And a is not equal to b. False."),
    mem=dict(label="Plus builds a new object", on="The names a, b and c tied to three separate Vector objects; c is built from a and b", names=["a", "b", "c"], **{"from": "A"},
             narr="Here is the picture. The names a and b are tied to two vectors. Plus does not change either of them. It builds a third vector, a brand new object, and the name c is tied to it. Three names, three objects. Dunder add only decides how the new object is built."),
    B=dict(file="deck.py", label="len and less than", on="a Deck that supports len and sorting",
           src='''
class Deck:
    def __init__(self, cards):
        self.cards = cards

    def __len__(self):
        return len(self.cards)

class Box:
    def __init__(self, size):
        self.size = size

    def __lt__(self, other):
        return self.size < other.size

    def __repr__(self):
        return f"Box({self.size})"

d = Deck(["A", "K", "Q"])
print(len(d))
boxes = [Box(5), Box(2), Box(9)]
print(sorted(boxes))
print(max(boxes))
''',
           narr="[HL 1] A Deck class. [HL 2] Init stores a list of cards. [HL 5] Dunder len. [HL 6] It returns how many cards there are. [HL 8] A Box class. [HL 9] Init stores the size. [HL 12] Dunder lt, the handshake for less than. [HL 13] A box is less when its size is smaller. [HL 15] Repr for a readable print. [HL 18] A deck of three cards. [HL 19] Len works on our own object. Three. [HL 20] Three boxes. [HL 21] Sorted only needs less than. Two, five, nine. [HL 22] And max finds the biggest. Box nine."),
    term="Vector of four comma six, True, False. Then 3, the sorted boxes, and Box of nine.",
    recap=["Dunder methods are special names Python looks for.", "__add__, __eq__ and __lt__ teach operators to our objects.", "__len__ makes len() work.", "Operators build new objects; they do not change the old ones."],
    bug=dict(title="__eq__ without __hash__", file="points.py", wrong='''
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

seen = {Point(1, 2)}
''', fixed='''
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

seen = {Point(1, 2)}
print(Point(1, 2) in seen)
''', wrong_note="__eq__ alone removes the default hash", fixed_note="__hash__ added",
             why="When you define eq, Python removes the default hash, because equal objects must have equal hashes. Define hash too, from the same values, to use the object in sets and as dictionary keys.",
             narr="Bug of the Day. We defined eq, and then tried to put a Point in a set. Type error, unhashable type, Point. When you define eq, Python removes the default hash, so equal objects cannot be placed in the wrong bucket. Add a hash method that uses the same values as eq, and sets work again."),
    pun="Why did the object learn dunder methods? It wanted to be on speaking terms with Python.",
    task="make plus work for Money", challenge="Write a Money class with an amount. Add __add__ so that Money(5) + Money(3) gives a new Money with 8. Add __repr__ too.",
    answer="def __add__(self, other): return Money(self.amount + other.amount). def __repr__(self): return f\"Money({self.amount})\".",
    shorts=[
        ("Dunder methods", "Dunder means double underscore. These are special method names that Python looks for. When you write a plus b, Python quietly calls a dot add with b. Define the method, and your own objects can use plus.", "a + b calls __add__", "Python's secret handshakes."),
        ("Add and eq", "Dunder add tells Python how to add two of your objects. It should return a new object. Dunder eq tells Python what equal means. Write both for a Vector, and then a plus b, and a equals equals b, both just work.", "__add__ and __eq__", "Teach operators."),
        ("Len and sorting", "Dunder len makes the len function work on your object. Dunder lt, for less than, is all that sorted needs. Define lt for a box class, and a list of boxes sorts, and max finds the biggest. Two small methods give you much power.", "__len__ and __lt__", "Len and sorting."),
        ("Unhashable", "A surprise bug. You define dunder eq, and then put the object into a set. Python says, type error, unhashable type. Defining eq removes the default hash. Add dunder hash that uses the same values, and sets and dictionary keys work again.", "TypeError: unhashable type", "Define hash with eq."),
        ("Pun and challenge", "Why did the object learn dunder methods? It wanted to be on speaking terms with Python. Your challenge. Write a Money class. Add dunder add, so that Money five plus Money three gives Money eight. Add a repr, so that you can see it.", "Challenge: Money + Money", "Teach plus to Money."),
    ],
))

EPISODES.append(dict(
    n=72, title="Mini project: Library system", spoken="mini project, library system",
    yt="Python OOP Project: Build a Library System", thumb="LIBRARY PROJECT",
    vis="Xecxec stamping due dates in a library, with books on tiny shelves",
    goals=["design a small program with two classes", "let one object hold other objects", "avoid a shared mutable default"],
    tags=["python oop project", "python library system", "python class project beginners", "python mutable default argument"],
    hash=["#python", "#project"],
    analogy="a real library: books are things, and the library is the thing that looks after them",
    c_title="Two classes, one idea",
    c_pts=["Book: title, author, whether it is borrowed", "Library: a list of books and the actions on them", "Library methods use Book methods"],
    intro="Time to put classes together. We build a tiny library with books you can borrow and return.",
    concept="A good design starts by listing the things. Here we have books, and a library. A Book knows its title, its author, and whether it is out. A Library holds a list of books. It has actions, such as add a book, borrow, and list what is available. The library does not need to know how a book tracks borrowing. It just asks the book. Think of a real library. The books are things. The library looks after them.",
    A=dict(file="library.py", label="Book and Library", on="two classes working together",
           src='''
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.borrowed = False

    def __repr__(self):
        return f"{self.title} by {self.author}"

class Library:
    def __init__(self):
        self.books = []

    def add(self, book):
        self.books.append(book)

    def borrow(self, title):
        for book in self.books:
            if book.title == title and not book.borrowed:
                book.borrowed = True
                return book
        return None

    def available(self):
        return [b for b in self.books if not b.borrowed]

lib = Library()
lib.add(Book("Python 101", "Rao"))
lib.add(Book("Crab Tales", "Xecxec"))
print(lib.borrow("Python 101"))
print(lib.borrow("Python 101"))
print(lib.available())
''',
           narr="[HL 1] The Book class. [HL 2] Init stores a title and an author. [HL 5] And that the book is not borrowed. [HL 7] Repr gives a readable line. [HL 10] The Library class. [HL 12] Its own list of books, fresh for every library. [HL 14] Add puts a book on the list. [HL 17] Borrow looks through the books. [HL 19] Right title, and not already out. [HL 20] Mark it as borrowed. [HL 21] And hand it over. [HL 22] Otherwise, nothing, which is None. [HL 24] Available builds a list of books still on the shelf. [HL 27] A library. [HL 28] Add two books. [HL 30] Borrow Python 101. We get the book. [HL 31] Borrow again. It is out, so None. [HL 32] And only Crab Tales is available."),
    mem=dict(label="A library holds books", on="The name lib tied to a Library object; its list holds two Book objects", names=["lib"], **{"from": "A"},
             narr="Here is the picture. The name lib is tied to a library object. Inside it sits a list of books. Each book is its own object, with a title, an author, and a borrowed flag. Objects can hold other objects. That is how bigger programs are built, from small objects that each do one job."),
    B=dict(file="members.py", label="A member borrows", on="a Member class that uses the library",
           src='''
class Book:
    def __init__(self, title):
        self.title = title
        self.borrowed = False

class Member:
    def __init__(self, name):
        self.name = name
        self.loans = []

    def borrow(self, book):
        if book.borrowed:
            return False
        book.borrowed = True
        self.loans.append(book.title)
        return True

b = Book("Python 101")
m1 = Member("Asha")
m2 = Member("Ravi")
print(m1.borrow(b))
print(m2.borrow(b))
print(m1.loans, m2.loans)
''',
           narr="[HL 1] A small Book class. [HL 3] A title. [HL 4] And a borrowed flag. [HL 6] A Member class. [HL 8] Each member has a name. [HL 9] And a list of loans, new for each member. [HL 11] Borrow checks the book. [HL 12] Already out, so [HL 13] False. [HL 14] Otherwise mark it borrowed. [HL 15] Remember the title in the loans. [HL 16] And return True. [HL 18] One book. [HL 19] Two members. [HL 21] Asha borrows. True. [HL 22] Ravi tries the same book, and gets False. [HL 23] Only Asha has a loan."),
    term="Python 101 by Rao, then None, then a list with Crab Tales by Xecxec. Then True, False, and the two loan lists.",
    recap=["Design by listing the things: Book and Library.", "A Library object holds a list of Book objects.", "Each class does one job.", "Create lists inside init, not in a default argument."],
    bug=dict(title="a mutable default shared by every library", kind="output", file="shelf.py", wrong='''
class Library:
    def __init__(self, books=[]):
        self.books = books

    def add(self, title):
        self.books.append(title)

north = Library()
south = Library()
north.add("Python 101")
print(south.books)
''', fixed='''
class Library:
    def __init__(self, books=None):
        self.books = [] if books is None else books

    def add(self, title):
        self.books.append(title)

north = Library()
south = Library()
north.add("Python 101")
print(south.books)
''', wrong_note="the default list is created once and shared", fixed_note="None, then a fresh list per object",
             why="A default value is built once, when the function is defined. A list as a default is therefore shared by every call. Use None, and build a fresh list inside.",
             narr="Bug of the Day. We add a book to the north library, and it appears in the south library too. The default list in the init brackets is built only once, and every library without its own list shares it. No error appears. Use None as the default, and create a fresh list inside init."),
    pun="Why did the library project get a good grade? It was well catalogued.",
    task="add a return method", challenge="Add a give_back(title) method to the Library that marks a borrowed book as available again. Test it.",
    answer="def give_back(self, title): for book in self.books: if book.title == title: book.borrowed = False.",
    shorts=[
        ("Design first", "Start a program by listing the things. In a library, we have books, and the library itself. A book knows its title and whether it is out. A library holds the books and offers actions. List the things, then write one class for each.", "Book + Library", "Design by listing things."),
        ("Objects hold objects", "A library object holds a list of book objects. Objects can hold other objects, and that is how bigger programs are built. Each class does one small job. The library asks the book, is this one borrowed, and the book answers for itself.", "Library holds Books", "Objects hold objects."),
        ("Borrow method", "The borrow method loops over the books. If the title matches, and the book is not already out, it marks the book as borrowed, and returns it. If nothing matches, it returns None. The second borrow of the same book gives None.", "borrow() returns book or None", "Borrow and check."),
        ("Shared default", "A tricky bug. You write init with books equals empty list in the brackets. Add a book to the north library, and the south library has it too. A default value is built once, and shared. Use None, and build a new list inside.", "books=[] is shared", "Never default to a list."),
        ("Pun and challenge", "Why did the library project get a good grade? It was well catalogued. Your challenge. Add a method called give back to the Library. It takes a title, and marks the borrowed book as available again. Test it by borrowing and returning.", "Challenge: give_back()", "Add give back."),
    ],
))
