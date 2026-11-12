"""Longer narration for module 5 (EP 41-50). Each text is added to the end of the matching text in m05.py.

Keys: intro, concept, A, ill, B, term, bug, hint (hint goes into the challenge scene).
Rules: docs/cpp-bible/STE.md. Cues [HL n] point at lines of the code file for that scene.
"""
EXT = {
    41: dict(
        concept="Why should a beginner care about addresses? Because the most powerful tools in C plus plus work with them. "
                "Pointers, arrays and the heap all depend on this idea.\n"
                "Addresses are long numbers, and we usually write them in a base that uses letters too. You do not need to read them. "
                "You only need to know that each variable has one, and that no two variables share the same bytes.",
        A="[HL 5] Three ints sit side by side in memory. "
          "[HL 6] The ampersand gives the address of the first item. We turn it into a char pointer, so we can count in single bytes. "
          "[HL 7] The same trick gives the address of the second item. "
          "[HL 8] The difference is four. An int takes four bytes, so the next item starts four bytes later.",
        ill="Notice that every box has an address, a size and a value. The address says where it starts. The size says where it ends. "
            "The value is what the bytes mean for that type.",
        B="[HL 5] A char takes one byte. [HL 6] An int takes four bytes on most machines. [HL 7] A double takes eight. "
          "[HL 8] A pointer to an int is also a fixed size. On a modern computer with sixty-four bits, it takes eight bytes. "
          "Every pointer has the same size, whatever it points to.",
        term="Notice that the size of a pointer does not depend on the type behind it. An int star and a double star are both eight.",
        bug="An address is not a number that you can store in an int. It has its own type, and the type remembers what lives at that address. "
            "The compiler stops the mistake, and that is good. Store the address in a pointer.",
        hint="Hint: a double takes eight bytes, so the answer should be eight.",
    ),
    42: dict(
        concept="Two symbols do all the work, and they look alike. The ampersand means, give me the address. The star means, go to that address. "
                "In a declaration, the star only says that the variable is a pointer.\n"
                "A pointer is a way to reach a variable from far away. A function can use a pointer to change a variable in main.",
        A="[HL 5] Fish is a plain int with the value three. "
          "[HL 6] The pointer p holds the address of fish. Read the line as, p is a pointer to int, and it points at fish. "
          "[HL 7] The star in front of p means, follow the address. We see three. "
          "[HL 8] Now we write through the pointer. Fish becomes ten. [HL 9] The print confirms it.",
        ill="Notice the arrow in the picture. The pointer box holds an address, and the arrow shows where it leads. "
            "The pointer is a separate box with its own address, and it takes up its own bytes.",
        B="[HL 4] The parameters are pointers, so the function receives addresses, not copies. "
          "[HL 5] The star reads the value at the first address. "
          "[HL 12] In main, the ampersand passes the addresses of x and y. "
          "This is the old C way to change a caller variable. In C plus plus, a reference does the same job with less typing.",
        term="Compare with the swap that used references. The result is the same, but the call has ampersands.",
        bug="A pointer to int promises that an int lives at the address. If it pointed to a double, the program would read the wrong bytes. "
            "So the compiler checks the types. Match the pointer type with the variable type.",
        hint="Hint: write star p plus equals five, and then print score.",
    ),
    43: dict(
        concept="This episode joins two ideas. An array is a row of boxes, and a pointer is an address. The array name is a handy address of the first box.\n"
                "That is why you can pass an array to a function. The function gets a pointer in truth. "
                "It is fast, because no copy is made, but the function does not know the length.",
        A="[HL 6] The array name turns into the address of its first item. "
          "[HL 7] The star gives the first item, which is ten. "
          "[HL 8] Square brackets work on pointers as well. P of one is the same as a of one. "
          "[HL 9] You can also add to the pointer. P plus two points at the third item, and the star reads it.",
        ill="Notice that the pointer holds only the start. It does not know where the array ends. "
            "If you walk too far, you read memory that does not belong to the array. So keep the size in another variable.",
        B="[HL 6] The pointer q starts at the first item. The loop stops when q reaches the address after the last item. "
          "[HL 7] The star reads the item, and q plus plus moves to the next one. "
          "This pattern is the base of the iterators that you met in the vector episodes.",
        term="The loop prints ten, twenty and thirty, the same as an index loop would.",
        bug="Look at the function line again. The square brackets in a parameter are only a disguise. The compiler turns them into a plain pointer. "
            "Sizeof then measures the pointer, not the array. So send the size as a second parameter.",
        hint="Hint: the function takes an int pointer and an int for the size, and a loop adds the items.",
    ),
    44: dict(
        concept="Pointer arithmetic is a big help, because the compiler does the byte counting for you. You think in items, and it works in bytes.\n"
                "The rules are strict. You may add a number to a pointer, subtract a number, or subtract two pointers. "
                "You may not add two pointers, multiply them or divide them. Those have no meaning.",
        A="[HL 5] The array holds five, six, seven and eight. "
          "[HL 6] The pointer p points at five. [HL 7] Adding one gives q, which points at six. "
          "[HL 8] The star on q gives six. "
          "[HL 9] The byte count between p and q is four, because one int is four bytes.",
        ill="Notice the two columns in the table. One column counts items, and the other counts bytes. "
            "The same step is one item for the compiler, and four bytes for the machine.",
        B="[HL 6] The pointer start points at the first item. "
          "[HL 7] The pointer end points right after the last item. This place is allowed, but you must not read it. "
          "[HL 8] Subtracting two pointers gives the number of items, which is five. "
          "[HL 9] End minus one points at the last item.",
        term="The two prints are five and then five again, because the last item is five.",
        bug="Two addresses added together point to nowhere useful. But the distance between two addresses is a real count. "
            "So to find the middle, add half of the distance to the low pointer. Binary search with pointers uses this rule.",
        hint="Hint: start the pointer at the array plus the size minus one, and move it back with minus minus.",
    ),
    45: dict(
        concept="Null and dangling pointers cause many crashes. A good habit is to give a pointer a safe value at birth. "
                "If you have no address yet, use nullptr.\n"
                "Before you follow a pointer that may be null, test it. The test is short, and it can save the program.",
        A="[HL 6] The pointer starts as nullptr. It points to nothing, and that is a safe state. "
          "[HL 7] This test asks, is the pointer null? Yes, so the message prints. "
          "[HL 10] Now the pointer gets a real address. "
          "[HL 11] A pointer works as a test by itself. It is true when it is not null. Then we may follow it.",
        ill="Notice the three states of a pointer. It may point to a live variable. It may be null. Or it may dangle, and that one is the worst. "
            "A null pointer is easy to test. A dangling pointer looks normal, so it hides the bug.",
        B="[HL 4] This function returns a pointer. It points to the item that we found, or to nothing. "
          "[HL 7] Returning the address of an array item is safe, because the array lives on in main. "
          "[HL 10] If the loop ends with no match, we return nullptr. The caller must test the result before it follows the pointer.",
        term="Notice that the program tests the pointer before the star. This habit prevents crashes.",
        bug="Local variables live on the stack, and they die when the function ends. The address of a dead variable is a trap. "
            "The pointer looks fine, but the box now belongs to someone else. Return the value, or use memory that lives longer.",
        hint="Hint: test the pointer in an if, and follow it only in the else branch.",
    ),
    46: dict(
        concept="Why do we need the heap? A stack variable lives only until its block ends. Sometimes data must live longer, or its size is not known early. "
                "The heap gives you that freedom.\n"
                "But freedom has a price. You must give every box back. Count your news and deletes. They must match, one for one.",
        A="[HL 5] New asks the heap for one int, and it sets the value to five. The answer is an address, and p stores it. "
          "[HL 6] The star follows the address and reads five. "
          "[HL 7] We can change the value through the pointer. "
          "[HL 9] Delete gives the box back. After the delete, we must not use p again.",
        ill="Notice the two regions. The pointer p lives on the stack, and the int lives on the heap. "
            "When main ends, p disappears. If we forgot the delete, the int would stay in the pool with nobody to reach it.",
        B="[HL 5] New with square brackets makes a row of three ints on the heap. "
          "[HL 7] Square brackets work on the pointer, as on any array. Each item is multiplied by ten. "
          "[HL 10] A row must be freed with delete and square brackets. Remember the pair, new with brackets, delete with brackets.",
        term="Notice the numbers. The items one, two and three become ten, twenty and thirty.",
        bug="The two forms of new and delete are a pair. The plain delete calls the destructor of one object only. "
            "For a row, the compiler needs the square brackets to free every item. A mismatch is undefined, and it may crash.",
        hint="Hint: use a loop for the squares, and call delete with square brackets at the end.",
    ),
    47: dict(
        concept="A dynamic array is a good lesson, but a vector does the same job with less risk. "
                "In real code, you rarely write new and delete by hand.\n"
                "Still, you must know what happens inside a vector. It owns a heap row, it tracks the size, and it deletes the row for you.",
        A="[HL 6] The user types the size n. The compiler could not know this number early. "
          "[HL 7] New makes a row of exactly n ints. "
          "[HL 9] The loop fills the row with squares. The first item is one, then four, then nine. "
          "[HL 15] We must free the row at the end, with the square brackets.",
        ill="Notice the steps. First we ask for n. Then we make the row. Then we use it. Last, we free it. "
            "If any step is missing, the program has a bug.",
        B="[HL 8] The vector takes the size in round brackets. All items start at zero. "
          "[HL 12] The range-based loop prints each item. "
          "There is no delete, and no leak. The vector cleans up when main ends.",
        term="Try the number five. The output should be one, four, nine, sixteen and twenty-five.",
        bug="Delete needs an address that came from new. A plain int variable is not such an address. "
            "Write delete with square brackets on the pointer named a, and leave n alone.",
        hint="Hint: add all items in a loop, and divide the sum by n as a double.",
    ),
    48: dict(
        concept="RAII is a long name for a simple idea. Let a variable own the resource. When the variable goes away, the resource goes with it.\n"
                "The compiler runs the destructor for you at the closing brace. This holds on every exit path. "
                "That includes an early return and an error.",
        A="[HL 5] The constructor runs when the object is made. It prints open. "
          "[HL 6] The destructor has a tilde in front of its name. It runs when the object dies, and it prints close. "
          "[HL 11] The object n is made here. [HL 12] The message working appears. "
          "[HL 13] At the closing brace, the destructor runs by itself, before the line after the block.",
        ill="Notice the order. Open comes first, then working, then close. The close appears at the closing brace, with no call from us. "
            "The compiler writes that call for us, every time.",
        B="[HL 10] This line makes a Noisy object on the heap, with new. "
          "[HL 11] When fail is true, the function returns early. "
          "[HL 14] The delete is skipped, so the destructor never runs. The first call prints open and close. The second call prints open only.",
        term="Count the lines. Open and close appear once. Then open appears again, with no close.",
        bug="You cannot see a leak in the output of most programs. The program works, and it is only a little bigger in memory. "
            "That makes leaks hard to catch. With a local object, the destructor runs on every exit. So the leak cannot happen.",
        hint="Hint: replace the new with a plain local variable, and the destructor runs on both returns.",
    ),
    49: dict(
        concept="Modern C plus plus advises you to avoid raw new and delete. Smart pointers do the work. Unique pointer is the first choice.\n"
                "It costs nothing extra. It is as fast as a raw pointer, and it deletes the object at the right time.",
        A="[HL 6] Make unique builds the int on the heap, and the unique pointer owns it. "
          "[HL 7] The star works as with a raw pointer. We see five. "
          "[HL 8] We can change the value, as before. "
          "[HL 10] When main ends, the unique pointer dies, and the heap box is freed. We wrote no delete.",
        ill="Notice the single owner. The key has one holder. If you hand the key to someone else, you no longer have it. "
            "This rule makes double delete impossible.",
        B="[HL 8] The move function hands the object from a to b. After that, a is empty. "
          "[HL 9] A moved-from pointer equals nullptr, so the test prints one. "
          "[HL 10] The new owner b still sees the value five.",
        term="Notice that a is empty, and b holds the value. Ownership moved, and nothing was copied.",
        bug="If two unique pointers owned one object, both would delete it. That is a crash. "
            "So the language does not allow a copy. When you want a new owner, say so with move. Then the old pointer becomes empty.",
        hint="Hint: make unique with the value twenty, and add one with the star.",
    ),
    50: dict(
        concept="Some objects have many owners. A shared pointer fits. It keeps a counter, and it deletes the object when the counter reaches zero.\n"
                "Weak pointer solves a problem. If two objects own each other with shared pointers, neither is ever freed. "
                "A weak pointer breaks the circle, because it does not own.",
        A="[HL 6] Make shared builds the object, and the count is one. "
          "[HL 7] The use count call reads the count. It prints one. "
          "[HL 9] Another shared pointer copies a, so the count grows to two. "
          "[HL 12] The inner block ends, b dies, and the count falls back to one.",
        ill="Notice the counter in the middle of the picture. Every new owner adds one, and every owner that leaves takes one away. "
            "At zero, the object is freed.",
        B="[HL 6] The weak pointer starts empty. "
          "[HL 9] It watches the object, but the count stays the same. "
          "[HL 11] Lock gives a shared pointer if the object is alive. If not, it gives an empty pointer. "
          "[HL 15] After the block, the object is gone, so expired is true.",
        term="Notice the order. The first expired call gives false. The second one gives true, after the object died.",
        bug="The constructor of a shared pointer is explicit, so the equals sign does not work. "
            "Do not wrap a raw pointer by hand. Use make shared. It is shorter, it is safe, and it does one memory request instead of two.",
        hint="Hint: the count is one after the first pointer, and two after the copy.",
    ),
}
