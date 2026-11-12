"""Longer narration for module 6 (EP 51-60). Each text is added to the end of the matching text in m06.py.

Keys: intro, concept, A, ill, B, term, bug, hint (hint goes into the challenge scene).
Rules: docs/cpp-bible/STE.md. Cues [HL n] point at lines of the code file for that scene.
"""
EXT = {
    51: dict(
        concept="Until now, a student would need two separate variables, one for the name and one for the marks. "
                "If you have fifty students, you must keep a hundred variables in step. A struct solves this.\n"
                "A struct is your own type. After you define it, you can use it like int or string. "
                "You can pass it to functions, store it in a vector, and copy it.",
        A="[HL 5] The word struct starts the definition. Student is the name of the new type. "
          "[HL 6] Each field has a type and a name, as in an ordinary variable. "
          "[HL 8] Do not forget the semicolon after the closing brace. "
          "[HL 11] Now we make a variable s of type Student. [HL 12] The dot reaches the name field, and we store Asha. "
          "[HL 13] The dot also reaches marks.",
        ill="Notice that the struct is only a plan. It uses no memory until you make a variable of it. "
            "Each variable gets its own set of fields, so two students never share one name.",
        B="[HL 10] The function takes a const reference, so there is no copy, and the function cannot change the student. "
          "[HL 15] The curly braces fill the fields in the order of the definition. Name comes first, and then marks. "
          "[HL 17] Each call to show prints one student.",
        term="Notice that one function shows any student. The struct makes the code short and clear.",
        bug="The struct definition looks like a block, but it is a declaration. A declaration needs the semicolon at its end. "
            "Without it, the compiler reads the next line as part of the struct. The error message then points to a strange place. "
            "When the error looks odd, check the line above it.",
        hint="Hint: write the struct above main, and end the closing brace with a semicolon.",
    ),
    52: dict(
        concept="A struct and a class are nearly the same in C plus plus. The one difference is the default access. A struct is public by default, and a class is private.\n"
                "By convention, we use a struct for plain data, and a class when the type has rules to protect. "
                "A good class hides its data, and it offers a few clear functions.",
        A="[HL 4] The class is the blueprint. [HL 5] The count is private, so outside code cannot touch it. "
          "[HL 7] The word public opens the door for the functions below. "
          "[HL 8] Increment adds one to the private count. "
          "[HL 9] The word const after the brackets promises that get does not change the object.",
        ill="Notice the line in the picture between the inside and the outside. Outside code may press the buttons, but it cannot reach the data. "
            "That wall is what makes classes safe.",
        B="[HL 13] Two objects come from one blueprint. Each has its own count. "
          "[HL 14] A is increased two times. [HL 16] B is increased one time. "
          "[HL 17] The output shows two and one. The objects do not affect each other.",
        term="Notice that each object keeps its own state. That is the main idea of objects.",
        bug="The compiler does not allow outside code to read a private member. This protects the class. "
            "If you need the value outside, add a public getter. If you need to change it, add a public function that checks the new value.",
        hint="Hint: keep the bool private, and let three public functions change and read it.",
    ),
    53: dict(
        concept="Why does an object need a constructor? Without it, the data inside starts with garbage. A constructor puts the object into a safe state from its first moment.\n"
                "An object that is never in a broken state is easier to trust. You do not have to ask whether it was set up.",
        A="[HL 8] The first constructor takes no values, and it sets both numbers to zero. "
          "[HL 9] The second constructor takes two values. The part after the colon sets the members. "
          "[HL 14] This object uses the first constructor. [HL 15] This object has two arguments, so the compiler picks the second. "
          "[HL 16] The origin prints zero, zero, and the point prints three, four.",
        ill="Notice that the compiler picks the constructor by the arguments, as it picks any overloaded function. "
            "With no arguments, it uses the default one. With two ints, it uses the one with two parameters.",
        B="[HL 10] One constructor does the work of three, because of the default values. "
          "[HL 15] No arguments, so both defaults are used. "
          "[HL 16] One argument gives the name, and the age stays at the default. "
          "[HL 17] Two arguments give both values.",
        term="Notice the three lines. Each object has a different mix of default and given values.",
        bug="This rule surprises many beginners. As soon as you write any constructor, the compiler assumes that you want full control. "
            "It stops making the empty one. If you still need an object with no arguments, write a default constructor, or give every parameter a default value.",
        hint="Hint: the area function multiplies the two members, and it is const.",
    ),
    54: dict(
        concept="There is a difference between building a member and assigning to it. In the body of a constructor, the members are already built, and then you change them. "
                "In the initializer list, each member is built with the right value at once.\n"
                "For a string, this saves work. For a const member, it is the only way.",
        A="[HL 10] The list sits between the brackets and the body. "
          "Title and pages each get their value in parentheses. "
          "[HL 11] The body runs after the list. This message proves that all members are already built. "
          "[HL 17] The object gets its name and its page count in one step.",
        ill="Notice the order of events. First all members are built, in the order of the declaration. Then the body runs. "
            "So the body is the place for extra work, not for setting values.",
        B="[HL 5] This member is const. After it is built, it can never change. "
          "[HL 9] The list gives it its value, so there is no assignment. "
          "[HL 14] The ticket gets id one hundred and one, and price fifty.",
        term="The id can never change after the ticket is made. That is the idea of const.",
        bug="Members are built in the order of the declaration. If your list says price first and id second, the compiler still builds id first. "
            "Warnings with the Wall flag point this out. Keep both in the same order, and you avoid surprises.",
        hint="Hint: a const member must be set in the initializer list, so the body can stay empty.",
    ),
    55: dict(
        concept="A destructor is the partner of the constructor. The constructor gets the resource, and the destructor gives it back.\n"
                "You never call a destructor yourself. The compiler calls it when the object goes out of scope. "
                "That is why destructors are so reliable.",
        A="[HL 9] The constructor asks the heap for a row of ints, and it prints the size. "
          "[HL 12] The destructor has a tilde and no parameters. "
          "[HL 13] It frees the row with delete and square brackets. "
          "[HL 19] The object b is made here. [HL 20] The program prints using it. [HL 21] At the closing brace, the destructor runs and prints freed.",
        ill="Notice that the heap row lives inside the object. The object is small, with a pointer and a size. "
            "The big data lives on the heap, and the destructor is the only owner who may free it.",
        B="[HL 14] Tag A is made first. [HL 15] Tag B second. [HL 16] Tag C third. "
          "[HL 17] At the end of main, the objects die in the opposite order. Tag C goes first, then B, then A.",
        term="Read the output from top to bottom. The three hellos come in order, and the three byes come in reverse.",
        bug="Nobody can give an argument to a destructor, because nobody calls it. So it has no parameters. "
            "A class may have only one destructor. If you need to pass information, store it in a member while the object lives.",
        hint="Hint: write down your guess first, then run the program. The destructors run in reverse order.",
    ),
    56: dict(
        concept="Encapsulation protects the rules of your class. If the balance is a public number, any code can set it to minus a million. "
                "If the balance is private, only the class decides what is allowed.\n"
                "A good class is easy to use and hard to misuse. Keep the data private, and keep the functions few.",
        A="[HL 5] The balance is private, and it starts at zero. "
          "[HL 9] The deposit function checks the amount first. A zero or negative amount is refused. "
          "[HL 12] Only a good amount reaches the balance. "
          "[HL 21] The deposit of minus twenty fails, so the output is false. [HL 22] The balance stays five hundred.",
        ill="Notice the guard at the door. Every change goes through a function that checks it. "
            "The class can promise that its balance is never below zero, because it has full control.",
        B="[HL 8] The getter returns the age and does not change anything, so it is const. "
          "[HL 10] The setter accepts only ages from zero to one hundred and twenty. "
          "[HL 19] An age of five hundred is refused, so the age stays at seventeen.",
        term="The output is seventeen. The bad value never entered the object.",
        bug="A setter that stores any value gives no protection at all. It is a public field with extra typing. "
            "Add a check in the setter. Then the class can promise that its data always follows the rules.",
        hint="Hint: the setter tests that the value is at least ten and at most thirty, and stores it only then.",
    ),
    57: dict(
        concept="Inside a member function, the object needs a way to refer to itself. The name this is that way. It holds the address of the current object.\n"
                "Most of the time, you do not write it. If you write count underscore, the compiler reads this arrow count underscore. "
                "You need this when you want to return the object itself.",
        A="[HL 8] The function returns a reference to a Counter. "
          "[HL 9] It adds the number to the count. "
          "[HL 10] Star this means, the object that I am running on. The function hands the object back. "
          "[HL 17] Because each call returns the same object, the next call can follow at once. Two, then three, then ten, give fifteen.",
        ill="Notice the chain. Each add returns the same object, so the calls link like beads on a string. "
            "Streams use this trick. That is why you can write many arrows in one cout line.",
        B="[HL 8] The increment function can change the object. [HL 9] The get function cannot, and it says so with const. "
          "[HL 13] The object c is const, so it may call only const functions. Get is fine, and it prints seven.",
        term="Notice that the program prints seven. The call to get is allowed on a const object.",
        bug="A const object is a promise that nothing changes. A function without const might change something, so the compiler refuses the call. "
            "The best fix is to mark every function that only reads as const. Then const objects work smoothly.",
        hint="Hint: put the word const after the brackets of get and print, but not of set.",
    ),
    58: dict(
        concept="Static members are useful for shared facts. How many tickets were sold? What is the tax rate? These facts belong to the class, not to one object.\n"
                "You reach a static member with the class name and two colons. You do not need an object.",
        A="[HL 6] The static member is made once, for the whole class. The word inline gives it its value inside the class. "
          "[HL 7] Each constructor adds one to the shared count. "
          "[HL 11] Three objects are made, so the constructor runs three times. "
          "[HL 12] The class name and two colons reach the count. The answer is three.",
        ill="Notice that the three objects have their own data, but they share one counter. "
            "The counter lives in the static region, so it stays until the program ends.",
        B="[HL 6] A static function does not need an object. "
          "It works only with its parameters and with other static members. "
          "[HL 10] We call it with the class name. The answer for one hundred degrees is two hundred and twelve.",
        term="Notice that no Temperature object exists in this program. The function still works.",
        bug="A static function has no object behind it, so it has no this pointer. A normal member belongs to an object, and none exists. "
            "The compiler cannot decide which count to read. Make the member static too, or make the function normal.",
        hint="Hint: add one to the static counter in the constructor, and print it after five objects.",
    ),
    59: dict(
        concept="When you overload an operator, you teach the language how your type behaves. A Vec class can add, subtract and print, like a number.\n"
                "Use this power with care. An operator should do what readers expect. If plus subtracts, your code is a puzzle for everyone.",
        A="[HL 6] The function is named operator plus. It takes another Vec by const reference. "
          "[HL 7] It adds the two x values and the two y values, and it returns a new Vec. "
          "[HL 14] The compiler turns a plus b into a call to this function. "
          "[HL 15] The result is eleven and twenty-two.",
        ill="Notice that the call a plus b is a short form. Behind the scenes, it is a call to a dot operator plus of b. "
            "Both forms mean the same thing. The short form is easier to read.",
        B="[HL 8] The output operator is a free function. The left side is the stream, and the right side is our object. "
          "[HL 9] It writes the parts to the stream, and it returns the stream. "
          "That return lets us chain more arrows. "
          "[HL 14] Now cout can print a Vec, as it prints an int.",
        term="Notice that the output looks like a normal point, in round brackets with a comma.",
        bug="The compiler knows how to add numbers, but it cannot guess what you mean by adding two Vec objects. "
            "So it complains. Write operator plus for the class, and the same line works.",
        hint="Hint: follow the pattern of plus, and use a minus sign in both lines of the body.",
    ),
    60: dict(
        concept="Copying is easy for a plain number. For an object that owns memory, copying is more subtle. A shallow copy copies only the pointer. "
                "Then both objects point at one box.\n"
                "The first object dies and frees the box. The second object dies and frees it again. That double free crashes the program. "
                "A deep copy makes a new box for each object.",
        A="[HL 8] The constructor makes a box on the heap with the value. "
          "[HL 9] The copy constructor makes a new box, and it copies the value into it. This is a deep copy. "
          "[HL 10] The destructor frees the box of this object only. "
          "[HL 17] The object b is a copy of a. [HL 18] Changing b does not change a. The output is five and nine.",
        ill="Notice the two pictures. In the shallow copy, two pointers lead to one box. In the deep copy, each pointer leads to its own box. "
            "Only the deep copy is safe.",
        B="[HL 6] The class holds a vector, and the vector knows how to copy itself. "
          "[HL 17] The copy gets its own list. "
          "So we need no destructor and no copy constructor. This is the rule of zero. "
          "[HL 19] The output is two and three.",
        term="Notice that the two counts differ. The change to b did not touch a.",
        bug="Sometimes copying makes no sense. A file handle or a network link cannot be copied. "
            "You write equals delete after the function, and the compiler refuses any call. The error appears at once, and not at run time.",
        hint="Hint: a vector of marks and a string name look after themselves, so no destructor is needed.",
    ),
}
