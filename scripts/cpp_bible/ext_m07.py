"""Longer narration for module 7 (EP 61-68). Each text is added to the end of the matching text in m07.py.

Keys: intro, concept, A, ill, B, term, bug, hint (hint goes into the challenge scene).
Rules: docs/cpp-bible/STE.md. Cues [HL n] point at lines of the code file for that scene.
"""
EXT = {
    61: dict(
        concept="Why use inheritance? You avoid copying code. If many classes share the same members, you write them once in the base.\n"
                "A derived class is a specialised version of the base. A Dog does everything an Animal does, and it also does tricks. "
                "Anywhere you need an Animal, you can use a Dog.",
        A="[HL 5] Animal is the base class. It holds a name and a function that prints. "
          "[HL 11] The colon and the word public say that Dog is built on Animal. The word public keeps the public members of the base public. "
          "[HL 13] Dog can use name, because it inherited it. "
          "[HL 18] The Dog object calls eat, which lives in the base. [HL 19] It also calls fetch, which belongs to Dog.",
        ill="Notice the arrow in the picture. It points from the child to the parent. "
            "A Dog object holds an Animal part and a Dog part. Both parts live in one object in memory.",
        B="[HL 6] The base has a speak function. [HL 11] Dog defines a function with the same name. "
          "The new one hides the old one. "
          "[HL 16] A call on a Dog uses the Dog version. "
          "[HL 17] The class name and two colons reach the hidden base version.",
        term="Notice the two lines. The Dog version prints Woof, and the base version prints three dots.",
        bug="Private is stronger than you may think. Even a child class cannot touch the private members of its parent. "
            "If a child needs access, the base can offer a protected member, or a public function. Choose the lowest level that works.",
        hint="Hint: write public before the base name, so the start function stays public in Bus.",
    ),
    62: dict(
        concept="The order of construction matters. A derived part may use the base part, so the base part must exist first.\n"
                "Destruction runs the other way. The derived part may use the base part while it cleans up. So it goes first.",
        A="[HL 17] We make one Derived object. "
          "[HL 6] The base constructor runs first, and it prints Base made. "
          "[HL 12] Then the derived constructor runs, and it prints Derived made. "
          "[HL 13] At the end of main, the derived destructor runs first. [HL 7] The base destructor runs last.",
        ill="Notice that the lines of the output form a mirror. The first made is the last gone. "
            "The same pattern appeared in the episode about destructors, and it holds for every level of inheritance.",
        B="[HL 9] The base constructor takes a name. "
          "[HL 17] The Dog constructor calls the Animal constructor in its initializer list, and it passes the name. "
          "Then it sets its own age. "
          "[HL 18] The show function can use name, because the base has a public getter.",
        term="Notice that the output is Moti, then three. The name came from the base, and the age came from Dog.",
        bug="The compiler tries to build the base part first. If the base needs arguments, it cannot guess them. "
            "Call the base constructor yourself in the initializer list. Write the name of the base, and give it the values.",
        hint="Hint: the output for a C object is A made, B made, and then C made.",
    ),
    63: dict(
        concept="Access levels are a design tool. Each level says who may depend on a member. Fewer dependents mean easier changes later.\n"
                "Start with private. If a child class needs the member, change it to protected. "
                "Make a member public only if the outside world needs it.",
        A="[HL 5] The label protected opens the members below to the class and its children. "
          "[HL 6] The balance starts at one hundred. "
          "[HL 11] Savings is a child, so it can change balance. The interest raises it by ten percent. "
          "[HL 12] A public getter lets the outside read the value. The answer is one hundred and ten.",
        ill="Notice the three rings in the picture. The outer ring is public, the middle ring is protected, and the inner ring is private. "
            "The nearer the ring is to the centre, the fewer people can look in.",
        B="[HL 6] The public member is open to everyone. "
          "[HL 9] The protected member is open to Child, but not to main. "
          "[HL 12] The private member is open only to Base. Child reaches it through the public getter. "
          "[HL 20] Sum is one plus two plus three, which gives six.",
        term="Notice that main prints the open member, which is one. It cannot touch the other two.",
        bug="Main is not part of the class family, so protected is closed to it. The compiler says that the member is protected within this context. "
            "If main needs the value, add a public function. If main does not need it, leave the member as it is.",
        hint="Hint: the id may be public, the name may be protected, and the secret code should be private.",
    ),
    64: dict(
        concept="Virtual functions are the heart of object oriented design. You write code against the base, and it works with every derived class.\n"
                "A new class can join later, and the old code does not change. This is how big programs stay flexible.",
        A="[HL 7] The word virtual in the base tells the compiler to decide at run time. "
          "[HL 8] A virtual destructor is needed too, because we delete through a base pointer. "
          "[HL 13] The word override asks the compiler to check that the function does replace a base function. "
          "[HL 17] The pointer type is Animal, but the object is a Dog. [HL 18] The call prints Woof.",
        ill="Notice the table inside each object. A virtual call looks up the right function in that table. "
            "The look-up costs a tiny amount of time, and in return you get flexible code.",
        B="[HL 8] The equals zero makes the function pure. Every animal must say how it speaks. "
          "[HL 23] The vector holds unique pointers to Animal. It can hold any kind of animal. "
          "[HL 24] First we add a Dog, and then we add a Cat. "
          "[HL 27] The loop calls speak on each one, and each object answers in its own way.",
        term="Notice that the loop knows nothing about dogs or cats. It only knows about animals.",
        bug="Without the word virtual, the compiler decides early. It looks at the pointer type, which is Animal. "
            "So it calls the base function, even if the object is a Dog. Add virtual in the base, and the compiler waits until run time.",
        hint="Hint: write override after the brackets of speak, and make the cow with make unique.",
    ),
    65: dict(
        concept="Abstract classes describe ideas. A shape in general has no area. Only a rectangle or a circle has one.\n"
                "The abstract class sets the rules. Every derived class must follow them. "
                "Code that uses a Shape reference can work with any shape, now or in the future.",
        A="[HL 6] The equals zero makes this function pure. No body is needed, and none is allowed here. "
          "[HL 15] Rect gives the body, so Rect is a complete class. "
          "[HL 20] A reference to Shape can refer to a Rect. "
          "[HL 21] The call finds the Rect version, and the answer is twelve.",
        ill="Notice the dotted outline of the Shape box in the picture. You cannot make a Shape object, but you can make a Rect object that is a Shape. "
            "The outline marks an idea, and the solid boxes are things.",
        B="[HL 30] A vector of Shape pointers holds a Rect and a Square. "
          "[HL 31] The Square has side five. "
          "[HL 34] The loop adds each area to the total. Twelve plus twenty-five gives thirty-seven. "
          "New shapes can join the vector, and the loop never changes.",
        term="Check by hand. Three times four is twelve. Five times five is twenty-five. The total is thirty-seven.",
        bug="A shape without an area is only an idea. So the compiler stops you from making one. "
            "The message says that the class is abstract, and it names the pure function. Make a derived class that gives a body for every pure function.",
        hint="Hint: the area of a circle uses the radius twice, so write radius times radius.",
    ),
    66: dict(
        concept="This is one of the most important rules in C plus plus. A base class that is used through pointers needs a virtual destructor.\n"
                "Without it, the delete goes to the base destructor only. The derived part is never cleaned, and memory or files may leak.",
        A="[HL 6] The base destructor is virtual. "
          "[HL 11] The Dog destructor uses override, so the compiler checks the match. "
          "[HL 15] The pointer type is Animal, but the object is a Dog. "
          "[HL 16] Delete finds the real type. The output is Dog gone, and then Animal gone.",
        ill="Notice the order of the output. The derived destructor runs first, and the base destructor runs after it. "
            "Without the word virtual, the first line would be missing.",
        B="[HL 16] A unique pointer holds the Dog. "
          "[HL 17] The program prints working. "
          "[HL 18] When main ends, the unique pointer deletes the object. The virtual destructor makes the deletion complete.",
        term="Notice that we wrote no delete. The smart pointer did it, and the virtual destructor made it correct.",
        bug="This bug is silent. The program builds and runs, and it may look fine. But the Dog part is never destroyed, so its resources leak. "
            "Turn on warnings. Most compilers warn about a class with virtual functions and a non-virtual destructor.",
        hint="Hint: write the word virtual in front of the destructor, and add a comment that says why.",
    ),
    67: dict(
        concept="Multiple inheritance gives a class the powers of more than one base. A Duck can walk and swim. That fits real life.\n"
                "But it adds risks. Names may clash, and the diamond problem can appear. Many designers use it only for small, simple interfaces.",
        A="[HL 4] Walker can walk. [HL 9] Swimmer can swim. "
          "[HL 14] The Duck lists both bases, with a comma between them. The body is empty, because Duck needs nothing more. "
          "[HL 18] The Duck object can walk. [HL 19] It can also swim.",
        ill="Notice the two arrows that point from Duck to its two parents. "
            "Duck holds a Walker part and a Swimmer part. Each part brings its own members.",
        B="[HL 6] The base Animal has a number of legs. "
          "[HL 9] The word virtual before the base name makes both children share one Animal part. "
          "[HL 15] So there is only one legs member, and there is no clash. "
          "[HL 16] The output is four.",
        term="Notice that the program sets legs once and reads it once. Without virtual, this line would not compile.",
        bug="When two bases have a function with the same name, the compiler cannot decide. It reports that the call is ambiguous. "
            "Write the base name, then two colons, and then the function. Then the choice is clear.",
        hint="Hint: write the base name and two colons before each call, to pick the right version.",
    ),
    68: dict(
        concept="Choosing between inheritance and composition is a design skill. Ask a question. Is it an X, or does it have an X?\n"
                "A car is not an engine, so a car has an engine. Composition is often more flexible, because you can change the part without changing the class.",
        A="[HL 4] Engine is a small class with a start function. "
          "[HL 10] Car holds an Engine as a private member. We say that Car has an Engine. "
          "[HL 14] The drive function calls start on the engine, and then it moves. "
          "[HL 21] Main only knows about Car. The engine is a hidden detail.",
        ill="Notice the difference in the two pictures. Inheritance draws an arrow up to the parent. Composition draws a box inside a box. "
            "A car holds its engine, as a wallet holds money.",
        B="[HL 14] The first function takes the Animal by value. The compiler copies only the Animal part. "
          "The copy is a plain Animal, so the speak call prints three dots. "
          "[HL 15] The second function takes a reference. No copy is made, so the virtual call finds the Dog version.",
        term="Notice the difference between the two lines. The first prints three dots, and the second prints Woof.",
        bug="Slicing is silent. The compiler lets you copy a Dog into an Animal, and it cuts away the Dog part. "
            "So pass objects of a class family by reference or by pointer, never by value.",
        hint="Hint: make the Processor and the Memory members of Computer, and call start on both.",
    ),
}
