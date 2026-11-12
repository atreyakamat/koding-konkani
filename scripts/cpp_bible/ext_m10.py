"""Longer narration for module 10 (EP 85-90). Each text is added to the end of the matching text in m10.py.

Keys: intro, concept, A, ill, B, term, bug, hint (hint goes into the challenge scene).
Rules: docs/cpp-bible/STE.md. Cues [HL n] point at lines of the code file for that scene.
"""
EXT = {
    85: dict(
        concept="Why learn a linked list when we have a vector? The list teaches you how data structures are built from nodes and pointers. "
                "Every tree and graph uses the same idea.\n"
                "A vector keeps its items side by side. A list keeps them anywhere, and the pointers join them. "
                "Adding to the front of a list is quick, because nothing else moves.",
        A="[HL 4] A node holds a value and a pointer to the next node. "
          "[HL 10] The first node holds ten, and head points at it. "
          "[HL 11] The second node is added through the next pointer of the first. "
          "[HL 13] The loop starts at head, and follows the next pointers. It stops at null. "
          "[HL 17] At the end, we free the nodes one by one. We save the next pointer first, or we would lose the rest of the list.",
        ill="Notice that the nodes can sit far apart in memory. Only the arrows connect them. "
            "If you lose the head, you lose the whole list. So never overwrite head before you save it.",
        B="[HL 9] This function makes a new node, and its next pointer is the old head. "
          "The new node becomes the new head. [HL 31] Pushing one, two and three gives the list three, two, one. "
          "[HL 33] The print function walks the list. [HL 34] The free function releases every node.",
        term="Notice the order. The last number pushed is the first one printed.",
        bug="Think about what the loop test means. When cur is the last node, its next pointer is null. "
            "If the test looks at next, the loop stops one node too early. Test cur itself, and the last node is included.",
        hint="Hint: start the count at zero, walk the list, and add one for each node.",
    ),
    86: dict(
        concept="Trees are everywhere. A file system is a tree. A family tree is a tree. The set and the map in the library are trees inside.\n"
                "In a balanced tree, each step halves the work. For a million keys, a search takes about twenty steps. "
                "A plain tree can lean, and then it behaves like a list. Real libraries keep the tree balanced.",
        A="[HL 10] The insert function returns the root of the tree. "
          "[HL 11] An empty spot is where the new node goes. "
          "[HL 14] A smaller key goes to the left. [HL 16] A bigger key goes to the right. "
          "[HL 26] The in order walk visits the left side, then the node, then the right side. The output is one, three, four, five, eight.",
        ill="Notice how the tree grows. Five is the first key, so it is the root. Three is smaller, so it goes left. Eight is bigger, so it goes right. "
            "Reading the tree from left to right gives a sorted list.",
        B="[HL 23] The contains function asks, is the key here? "
          "[HL 27] If the key matches, the answer is true. "
          "[HL 30] Otherwise, it goes left or right, and asks again. It never looks at the other side. "
          "[HL 37] The height is one plus the taller of the two sides. For our tree, it is three.",
        term="Notice the output. Four is in the tree, seven is not, and the height is three.",
        bug="The place of the print line decides the order. Left first, then the node, then the right side, gives sorted output. "
            "If you print the node before the left side, you get preorder, and the numbers come out in another order.",
        hint="Hint: loop while the left pointer is not null, and move to the left child each time.",
    ),
    87: dict(
        concept="Today a laptop has many cores. A program with threads can use them all at once.\n"
                "Threads share memory, which makes them powerful and dangerous. Two threads that write to one variable can overwrite each other. "
                "This is called a data race, and it gives wrong answers that change from run to run.",
        A="[HL 7] A thread starts at once, and it runs the lambda. "
          "The capture with an ampersand lets the lambda change result. "
          "[HL 12] Join waits until the thread is finished. Without it, main might print before the thread has done its work. "
          "[HL 13] The sum of one to one hundred is five thousand and fifty.",
        ill="Notice the two paths in the picture. Main and the thread run side by side, and the join is the point where they meet again.",
        B="[HL 8] The mutex is the key to the counter. "
          "[HL 11] The lock guard takes the key when it is made. It gives the key back when it dies at the end of the round. "
          "[HL 15] Two threads run the same work. "
          "[HL 19] Each thread adds one thousand, so the answer is always two thousand.",
        term="Notice that the answer is the same on every run. Without the lock, it could be lower.",
        bug="A thread object that is still joinable when it dies ends the whole program. "
            "Always call join before the end of the scope. Or detach the thread, if you want it to run alone.",
        hint="Hint: give each thread its own sum variable, so the two threads never touch the same data.",
    ),
    88: dict(
        concept="This project joins many ideas from the course. A struct holds one student. A class holds the roster and protects it. "
                "A vector stores the data, and a lambda sorts it.\n"
                "Design first. Decide what the roster must do. Then write one method for each job, and keep the data private.",
        A="[HL 8] The struct holds the facts about one student. "
          "[HL 15] Add stores a new student at the end. "
          "[HL 19] The average is a const method, because it only reads. "
          "[HL 24] If the roster is empty, we return zero, so we never divide by zero. "
          "[HL 28] The ranking works on a copy, so the original order stays the same.",
        ill="Notice the wall between the inside and the outside. Main can add students and ask questions, but it cannot touch the vector. "
            "If you later change the vector to a map, main does not change.",
        B="[HL 19] The best method returns an optional. If the roster is empty, there is no best student. "
          "[HL 23] Max element gives the student with the highest marks. The lambda says which of two students is smaller. "
          "[HL 34] The first call prints zero, because the roster is empty. "
          "[HL 39] The second call prints Asha with ninety-one.",
        term="Notice that the code checks the optional before it reads it. This habit avoids many bugs.",
        bug="A const object can call only const methods. If a method only reads, mark it const. "
            "Then it works on const references and const objects. It is a promise to your reader, and the compiler holds you to it.",
        hint="Hint: loop over the students, and return a student only if the name matches.",
    ),
    89: dict(
        concept="Exam questions love tricks. They are not unfair. They test whether you know how the language works in truth.\n"
                "Read every line slowly. Ask three questions. What is the type? What is the value now? Does anything change the value before it is used?",
        A="[HL 5] Both numbers are ints, so the division gives three, not three point five. "
          "[HL 6] An unsigned char holds numbers from zero to two hundred and fifty-five. "
          "[HL 7] Adding ten to two hundred and fifty gives two hundred and sixty, which does not fit. The value wraps around to four. "
          "[HL 8] The cast to int shows the number, and not a letter.",
        ill="Notice the shape of each trap. A value is too small, too big or not exact. Once you see the pattern, you spot the trap at once.",
        B="[HL 6] The numbers zero point one and zero point two cannot be stored exactly in binary. "
          "The sum is a tiny bit different from zero point three. "
          "[HL 7] So the test with equals is false. "
          "[HL 8] The safe way is to compare the difference with a small limit. Then the test is true.",
        term="Notice the two answers. False for the exact test, and true for the safe test.",
        bug="A reference is only a nickname for a box. When the box dies at the end of the function, the nickname points at nothing. "
            "Return small values by value. For big values, return by value too. Modern C plus plus makes this cheap with moves.",
        hint="Hint: make one of the two numbers a double, for example by dividing by two point zero.",
    ),
    90: dict(
        concept="Look back at what you can do now. You write loops and functions. You manage memory with care. You build classes, and you use the library.\n"
                "These are real skills. Companies use C plus plus for games, for banks, for phones and for rockets. "
                "You have the base to learn any of those areas.",
        A="[HL 8] A struct holds a title and a page count. "
          "[HL 13] The function returns an optional, because an empty list has no longest book. "
          "[HL 17] Max element finds the book with the most pages, and the lambda tells it how to compare. "
          "[HL 23] The if with a declaration checks the optional and names it in one line. "
          "[HL 26] The sort uses another lambda, and it orders the books by title.",
        ill="Notice how many ideas sit in this short program. Structs, vectors, lambdas, optional and algorithms all work together. "
            "A year ago, this code was a puzzle. Now you can read it.",
        B="[HL 7] The map holds names and marks. "
          "[HL 8] A structured binding unpacks each pair into two clear names. "
          "The loop prints the pairs in sorted order of name. "
          "This is modern C plus plus. Short, clear and safe.",
        term="Notice that you now understand every symbol on the screen. That is real progress.",
        bug="Here is the last classic. When a struct or a class has no semicolon at the end, the compiler gets confused. "
            "It often reports the error one line later. Remember the tip. When an error looks odd, read the line above it.",
        hint="Hint: start small. A program of fifty lines that you finish is worth more than one that you never end.",
    ),
}
