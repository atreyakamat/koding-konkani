"""Module 5 — Memory and pointers (EP 41-50)."""
from lib import flow, mem, table

MODULE = {"id": 5, "name": "Memory and pointers", "range": "41–50", "colours": "Lilac + Tomato", "bg": "lilac"}
NEXT_AFTER = ("Next: EP 51 · Structs", "We end module five here. Next time: structs, your own way to group data.")
EPISODES = []

EPISODES.append(dict(
    n=41, title="Memory and addresses", spoken="memory and addresses", yt="C++ Memory and Addresses: Where Do Variables Live?",
    thumb="ADDRESSES", vis="a street of numbered houses",
    goals=["explain that every variable has an address", "use the address-of operator", "tell an address from a value"],
    tags=["c++ memory", "address of operator", "variable address", "stack memory"],
    analogy="a street of houses: each house has a number, and a family inside",
    c_pts=["Memory is a long row of numbered bytes", "Every variable lives at an address", "The ampersand gives the address"],
    hook="Every variable has a home address.",
    intro="Today we look under the hood. Every variable lives at an address in memory. Soon you will use that address.",
    concept="Memory is a long row of bytes. Each byte has a number, called its address. A variable lives at one address, and it fills as many bytes as its type needs.\n"
            "The ampersand in front of a variable gives its address. Think of a street of houses. Each house has a number, and a family lives inside.",
    A=dict(file="gap.cpp", label="The gap between boxes", on="the distance in bytes between two neighbouring ints",
           src='''
#include <iostream>
using namespace std;

int main() {
    int a[3] = {10, 20, 30};
    char* first = reinterpret_cast<char*>(&a[0]);
    char* second = reinterpret_cast<char*>(&a[1]);
    cout << (second - first) << endl;
    return 0;
}
''',
           narr="[HL: int a] An array of three ints. [HL: &a[0]] The ampersand gives the address of the first item. We view it as a char address, so that we can count bytes. "
                "[HL: &a[1]] This is the address of the second item. [HL: second - first] The difference is four bytes. That is the size of one int. The real addresses change from run to run, but the gap is always four."),
    ill=dict(label="Addresses in a row", on="three int boxes and their addresses, four bytes apart",
             data=mem([("a", "int[3]", "10, 20, 30")], caption="Each address is four more than the last. The addresses here are examples"),
             narr="Look at the three boxes. The first sits at address one thousand. The next sits at one thousand and four. The last at one thousand and eight. "
                  "These addresses are examples. On a real computer, the numbers differ every time you run the program."),
    B=dict(file="sizes.cpp", label="Sizes decide the gap", on="sizeof for four types",
           src='''
#include <iostream>
using namespace std;

int main() {
    cout << sizeof(char) << endl;
    cout << sizeof(int) << endl;
    cout << sizeof(double) << endl;
    cout << sizeof(int*) << endl;
    return 0;
}
''',
           narr="[HL: sizeof(char)] A char takes one byte. [HL: sizeof(int)] An int takes four. [HL: sizeof(double)] A double takes eight. "
                "[HL: sizeof(int*)] An address itself takes eight bytes on a sixty-four-bit computer. Remember this. We will store addresses in variables soon."),
    term="The program prints one, four, eight and eight on four lines.",
    recap=["Memory is a long row of numbered bytes.", "Every variable lives at an address.",
           "The ampersand gives the address of a variable.", "An address is not the same as a value."],
    bug=dict(title="Storing an address in an int", file="addr.cpp", kind="compile", wrong_note="an address goes into a plain int",
             wrong='''
#include <iostream>
using namespace std;

int main() {
    int fish = 3;
    int where = &fish;
    cout << where << endl;
    return 0;
}
''', fixed_note="a pointer type holds the address",
             fixed='''
#include <iostream>
using namespace std;

int main() {
    int fish = 3;
    int* where = &fish;
    cout << (where != nullptr) << endl;
    return 0;
}
''',
             why="An address has its own type. For an int, the type is int star. A plain int cannot hold it.",
             narr="Bug of the Day. We store the address of fish in a plain int. The compiler says invalid conversion from int star to int. "
                  "An address has its own type. For the address of an int, that type is int star. We learn it in the next episode."),
    pun="My variable moved house. It left a new address, but it forgot to tell its neighbours.",
    task="find the gap between two doubles", challenge="Make an array of two doubles. Print the number of bytes between the two items.",
    answer="Take the address of each item, convert both to char star, and subtract. The answer is eight.",
))

EPISODES.append(dict(
    n=42, title="Pointers", spoken="pointers", yt="C++ Pointers Explained: &, * and nullptr",
    thumb="POINTERS", vis="a crab pointing at a box with a long claw",
    goals=["declare a pointer", "read and write through a pointer", "tell p from star p"],
    tags=["c++ pointers", "dereference operator", "pointer basics", "int pointer"],
    analogy="a house key tag: the tag is not the house, but it tells you where to go",
    c_pts=["A pointer holds an address", "Star in a declaration means pointer", "Star in front of a pointer means follow it"],
    hook="A pointer is a variable that holds an address.",
    intro="Today we meet pointers. A pointer is a variable that holds an address. With it, you can reach another variable from far away.",
    concept="A pointer is a variable that holds an address. You declare it with a star after the type. You give it the address of a variable with the ampersand.\n"
            "A star in front of the pointer means follow the address. You can then read or change the box it points to. Think of a key tag with an address. The tag is not the house, but it tells you where to go.",
    A=dict(file="pointer.cpp", label="Follow the pointer", on="a pointer reads and changes fish",
           src='''
#include <iostream>
using namespace std;

int main() {
    int fish = 3;
    int* p = &fish;
    cout << *p << endl;
    *p = 10;
    cout << fish << endl;
    return 0;
}
''',
           narr="[HL: int fish] Fish is an int with the value three. [HL: int* p] P is a pointer to an int. It holds the address of fish. "
                "[HL: cout << *p] Star p means follow the pointer. It reads the box at that address. It prints three. [HL: *p = 10] We can also write through the pointer. "
                "[HL: cout << fish] Fish is now ten. We changed fish without using its name."),
    ill=dict(label="A pointer and its target", on="the pointer p holds the address of fish, shown as an arrow",
             data=mem([("fish", "int", "10"), ("p", "int*", None)], arrows=[("p", "fish", "points to")], caption="The value of p is the address of fish"),
             narr="Look at the two boxes. Fish holds ten. P holds the address of fish. The arrow shows that link. "
                  "Star p follows the arrow to fish. Writing to star p changes fish."),
    B=dict(file="swapptr.cpp", label="Swap with pointers", on="a swap function that takes two addresses",
           src='''
#include <iostream>
using namespace std;

void swap_values(int* a, int* b) {
    int t = *a;
    *a = *b;
    *b = t;
}

int main() {
    int x = 1, y = 2;
    swap_values(&x, &y);
    cout << x << " " << y << endl;
    return 0;
}
''',
           narr="[HL: void swap_values] The function takes two pointers. [HL: int t = *a] T copies the value that a points to. [HL: *a = *b] The value at a becomes the value at b. [HL: *b = t] The value at b becomes the old value of a. "
                "[HL: swap_values(&x, &y)] The caller passes the addresses of x and y. Now x is two, and y is one. This is the C way to swap. Episode twenty-four showed the C plus plus way."),
    term="The program prints two and one.",
    recap=["A pointer holds an address.", "The ampersand gives the address of a variable.",
           "Star in front of a pointer follows it.", "Writing through a pointer changes the target."],
    bug=dict(title="A pointer to the wrong type", file="pointer.cpp", kind="compile", wrong_note="an int pointer holds the address of a double",
             wrong='''
#include <iostream>
using namespace std;

int main() {
    double price = 1.5;
    int* p = &price;
    cout << *p << endl;
    return 0;
}
''', fixed_note="the pointer type matches",
             fixed='''
#include <iostream>
using namespace std;

int main() {
    double price = 1.5;
    double* p = &price;
    cout << *p << endl;
    return 0;
}
''',
             why="The type of a pointer says how to read the bytes at the address. A pointer to int cannot point at a double.",
             narr="Bug of the Day. We point an int pointer at a double. The compiler says it cannot convert double star to int star. "
                  "The pointer type tells the computer how to read the bytes. Use a double pointer for a double."),
    pun="A pointer walked into a bar. It said, I am just here to point out the drinks.",
    task="change a variable through a pointer", challenge="Make an int called score. Make a pointer to it. Add five to score through the pointer, and print score.",
    answer="Write star p plus equals five. Then print score. It shows the new value.",
))

EPISODES.append(dict(
    n=43, title="Pointers and arrays", spoken="pointers and arrays", yt="C++ Pointers and Arrays: Array Decay",
    thumb="ARRAY = POINTER?", vis="an array name turning into a pointer",
    goals=["use an array name as a pointer", "read items through a pointer", "explain array decay"],
    tags=["pointer and array", "array decay", "c++ pointer index", "sizeof array parameter"],
    analogy="the first house on a street: its address starts the whole street",
    c_pts=["An array name acts as the address of the first item", "p[i] works the same as a[i]", "An array loses its size when it decays"],
    hook="An array name quietly turns into a pointer.",
    intro="Today we connect arrays and pointers. They look different, but they work together all the time.",
    concept="In most places, an array name turns into the address of its first item. We call this array decay. So you can store the array name in a pointer.\n"
            "Then p index i works like a index i. But there is a cost. A pointer does not know the size of the array. Think of the first house on a street. Its address starts the whole street.",
    A=dict(file="decay.cpp", label="An array and a pointer", on="a pointer reads the items of an array",
           src='''
#include <iostream>
using namespace std;

int main() {
    int a[3] = {10, 20, 30};
    int* p = a;
    cout << *p << endl;
    cout << p[1] << endl;
    cout << *(p + 2) << endl;
    return 0;
}
''',
           narr="[HL: int* p = a] The array name a becomes the address of the first item. P now points to ten. [HL: cout << *p] Star p reads ten. [HL: p[1]] Square brackets work on a pointer, too. P index one reads twenty. "
                "[HL: *(p + 2)] This form is the same. It moves two items on, and then follows the pointer. It reads thirty."),
    ill=dict(label="The pointer at the first item", on="p points at the first of three boxes",
             data=mem([("a", "int[3]", "10, 20, 30"), ("p", "int*", None)], arrows=[("p", "a[0]", "points to the first item")], caption="p holds the address of a[0]"),
             narr="Here is the picture. The array has three boxes. P points to the first box. P plus one would point to the second box. "
                  "P plus two would point to the third box."),
    B=dict(file="walk.cpp", label="Walk with a pointer", on="a pointer moves along the array",
           src='''
#include <iostream>
using namespace std;

int main() {
    int a[3] = {10, 20, 30};
    for (int* q = a; q != a + 3; q++) {
        cout << *q << " ";
    }
    cout << endl;
    return 0;
}
''',
           narr="[HL: for (int* q = a] Q starts at the first item. [HL: q != a + 3] A plus three is the address right after the last item. The loop stops when q reaches it. "
                "[HL: q++] Q plus plus moves q to the next item. [HL: cout << *q] Each round prints the item that q points to."),
    term="The program prints ten, twenty and thirty on one line.",
    recap=["An array name turns into the address of its first item.", "P index i works like a index i.",
           "A pointer does not know the size of an array.", "A loop can walk with a pointer from the start to the end."],
    bug=dict(title="Sizeof on an array parameter", file="count.cpp", kind="warn", wrong_note="sizeof is used on an array parameter",
             wrong='''
#include <iostream>
using namespace std;

int count_items(int a[]) {
    return sizeof(a) / sizeof(a[0]);
}

int main() {
    int a[5] = {1, 2, 3, 4, 5};
    cout << count_items(a) << endl;
    return 0;
}
''', fixed_note="the size is passed in",
             fixed='''
#include <iostream>
using namespace std;

int count_items(const int a[], int n) {
    int count = 0;
    for (int i = 0; i < n; i++) {
        count += a[i] > 0 ? 1 : 0;
    }
    return count;
}

int main() {
    int a[5] = {1, 2, 3, 4, 5};
    cout << count_items(a, 5) << endl;
    return 0;
}
''',
             why="An array parameter is a pointer in disguise. Sizeof then gives the size of the pointer, not the size of the array. Pass the size as a second argument.",
             narr="Bug of the Day. The function tries to count the items with sizeof. The compiler warns that sizeof on an array parameter returns the size of a pointer. "
                  "The array decayed to a pointer, and the size was lost. Pass the size as a second parameter."),
    pun="The array told the pointer, you complete me. The pointer said, I only know where you start.",
    task="sum an array through a pointer", challenge="Write a function that takes a pointer and a size. It returns the sum of the items.",
    answer="Use a loop from zero to size minus one. Add p index i to a total. Return the total.",
))

EPISODES.append(dict(
    n=44, title="Pointer arithmetic", spoken="pointer arithmetic", yt="C++ Pointer Arithmetic: p + 1 Explained",
    thumb="P + 1", vis="a pointer hopping along a row of boxes",
    goals=["explain what p plus one means", "subtract two pointers", "know which operations are allowed"],
    tags=["pointer arithmetic", "c++ pointer increment", "pointer difference", "pointer plus"],
    analogy="a bus conductor: one stop forward means one seat, not one metre",
    c_pts=["P plus one moves by one item, not one byte", "Two pointers can be subtracted", "Two pointers cannot be added"],
    hook="P plus one does not add one byte.",
    intro="Today we do maths with addresses. The rules are simple, but they surprise most beginners.",
    concept="When you add one to a pointer, it moves by one item, not by one byte. For an int pointer, the address grows by four. For a double pointer, it grows by eight.\n"
            "You may subtract two pointers into the same array. You get the number of items between them. You may not add two pointers. Think of a bus conductor. One stop forward means one seat, not one metre.",
    A=dict(file="hop.cpp", label="Hop by one item", on="p plus one moves four bytes for an int",
           src='''
#include <iostream>
using namespace std;

int main() {
    int a[4] = {5, 6, 7, 8};
    int* p = a;
    int* q = p + 1;
    cout << *q << endl;
    cout << (reinterpret_cast<char*>(q) - reinterpret_cast<char*>(p)) << endl;
    return 0;
}
''',
           narr="[HL: int* p = a] P points to the first item. [HL: int* q = p + 1] Q is p plus one. It points to the second item. [HL: cout << *q] It reads six. "
                "[HL: reinterpret_cast] Now we measure the distance in bytes. The answer is four. P plus one moved by the size of one int."),
    ill=dict(label="One step is one item", on="a table: expression, items moved and bytes moved",
             data=table(["Expression", "Items", "Bytes for int*", "Bytes for double*"], [["p + 1", "1", "4", "8"], ["p + 3", "3", "12", "24"], ["p - 1", "-1", "-4", "-8"], ["q - p", "q minus p", "items", "items"]]),
             narr="Look at the table. P plus one moves one item. For an int pointer that is four bytes. For a double pointer it is eight bytes. "
                  "The compiler does the multiplication for you. Subtracting two pointers gives a count of items, not bytes."),
    B=dict(file="distance.cpp", label="Subtract two pointers", on="end minus start gives the number of items",
           src='''
#include <iostream>
using namespace std;

int main() {
    int a[5] = {1, 2, 3, 4, 5};
    int* start = a;
    int* end = a + 5;
    cout << (end - start) << endl;
    cout << *(end - 1) << endl;
    return 0;
}
''',
           narr="[HL: int* start] Start points to the first item. [HL: int* end] End points right after the last item. [HL: end - start] The difference is five. That is the number of items. "
                "[HL: *(end - 1)] End minus one points to the last item. It reads five. This idea powers many library functions."),
    term="The program prints five and five.",
    recap=["P plus one moves by one item.", "The compiler scales the step by the size of the type.",
           "Subtracting two pointers gives a count of items.", "Adding two pointers is not allowed."],
    bug=dict(title="Adding two pointers", file="mid.cpp", kind="compile", wrong_note="two pointers are added to find the middle",
             wrong='''
#include <iostream>
using namespace std;

int main() {
    int a[5] = {1, 2, 3, 4, 5};
    int* low = a;
    int* high = a + 4;
    int* mid = (low + high) / 2;
    cout << *mid << endl;
    return 0;
}
''', fixed_note="the middle is low plus half the distance",
             fixed='''
#include <iostream>
using namespace std;

int main() {
    int a[5] = {1, 2, 3, 4, 5};
    int* low = a;
    int* high = a + 4;
    int* mid = low + (high - low) / 2;
    cout << *mid << endl;
    return 0;
}
''',
             why="The sum of two addresses has no meaning. The distance between two addresses does. Add half of the distance to the low pointer.",
             narr="Bug of the Day. We add two pointers to find the middle. The compiler says invalid operands to binary plus. "
                  "The sum of two addresses has no meaning. Take the distance between them, halve it, and add it to the low pointer."),
    pun="A pointer asked for directions. The answer was, just add one.",
    task="print an array backwards with a pointer", challenge="Use a pointer that starts at the last item. Print the array in reverse order.",
    answer="Start p at a plus size minus one. Loop while p is not before a. Print star p, and subtract one from p.",
))

EPISODES.append(dict(
    n=45, title="nullptr and dangling pointers", spoken="nullptr and dangling pointers", yt="C++ nullptr and Dangling Pointers",
    thumb="DANGER!", vis="a signpost that points at an empty field",
    goals=["use nullptr for a pointer that points nowhere", "check a pointer before you use it", "spot a dangling pointer"],
    tags=["nullptr", "dangling pointer", "null pointer check", "return local address"],
    analogy="a letter sent to a house that was pulled down: the address exists, but nobody lives there",
    c_pts=["nullptr means points to nothing", "Check a pointer before you follow it", "A dangling pointer points to a dead variable"],
    hook="A pointer can point at something that no longer exists.",
    intro="Today we learn about two dangerous pointers. One points nowhere. The other points at something that is gone.",
    concept="Nullptr is a pointer that points to nothing. You can test it in an if. Never follow a null pointer. The program will crash.\n"
            "A dangling pointer is worse. It holds the address of a variable that no longer exists. Think of a letter sent to a house that was pulled down. The address exists, but nobody lives there.",
    A=dict(file="nullcheck.cpp", label="Check before you follow", on="a pointer is tested before it is used",
           src='''
#include <iostream>
using namespace std;

int main() {
    int fish = 3;
    int* p = nullptr;
    if (p == nullptr) {
        cout << "p points to nothing" << endl;
    }
    p = &fish;
    if (p) {
        cout << *p << endl;
    }
    return 0;
}
''',
           narr="[HL: int* p = nullptr] P starts as nullptr. It points to nothing. [HL: if (p == nullptr)] We test it with two equals signs. The test is true. [HL: p = &fish] Now p points at fish. "
                "[HL: if (p)] A pointer works as a test by itself. Nullptr counts as false. Any real address counts as true. [HL: cout << *p] So it is safe to follow p here."),
    ill=dict(label="Null and dangling", on="three pointers: one valid, one null, one dangling",
             data=mem([("fish", "int", "3"), ("good", "int*", None), ("none", "int*", "nullptr")], arrows=[("good", "fish", "valid")], caption="good points at fish. none points nowhere"),
             narr="Here are two pointers. Good points at fish, and it is safe to follow. None holds nullptr, so it points nowhere. "
                  "Never follow none. A third kind, the dangling pointer, looks like good, but its target is gone."),
    B=dict(file="lookup.cpp", label="A safe lookup", on="a function returns nullptr when nothing matches",
           src='''
#include <iostream>
using namespace std;

int* find_item(int a[], int n, int target) {
    for (int i = 0; i < n; i++) {
        if (a[i] == target) {
            return &a[i];
        }
    }
    return nullptr;
}

int main() {
    int a[3] = {4, 8, 15};
    int* hit = find_item(a, 3, 8);
    if (hit != nullptr) {
        cout << "Found " << *hit << endl;
    }
    if (find_item(a, 3, 99) == nullptr) {
        cout << "Not found" << endl;
    }
    return 0;
}
''',
           narr="[HL: int* find_item] This function returns a pointer. [HL: return &a[i]] When it finds the target, it returns the address of that item. [HL: return nullptr] When nothing matches, it returns nullptr. "
                "[HL: if (hit != nullptr)] The caller must check the result first. [HL: cout << \"Found] Eight is in the array, so the program prints Found eight. [HL: == nullptr] Ninety-nine is not there, so the program prints Not found."),
    term="The program prints Found eight, and then Not found.",
    recap=["Nullptr is a pointer that points to nothing.", "Test a pointer before you follow it.",
           "A dangling pointer points to something that is gone.", "Never return the address of a local variable."],
    bug=dict(title="Returning the address of a local", file="dangle.cpp", kind="warn", wrong_note="the function returns the address of a local variable",
             wrong='''
#include <iostream>
using namespace std;

int* make_number() {
    int x = 5;
    return &x;
}

int main() {
    int* p = make_number();
    cout << (p != nullptr) << endl;
    return 0;
}
''', fixed_note="the function returns the value",
             fixed='''
#include <iostream>
using namespace std;

int make_number() {
    int x = 5;
    return x;
}

int main() {
    int n = make_number();
    cout << n << endl;
    return 0;
}
''',
             why="The local variable x dies when the function ends. The returned address then points to a dead box. Return the value instead.",
             narr="Bug of the Day. The function returns the address of its local variable x. But x dies when the function ends. "
                  "The compiler warns that the address of a local variable is returned. The pointer now dangles. Return the value instead."),
    pun="Why did the pointer see a therapist? It had too many unresolved references.",
    task="write a safe function", challenge="Write a function that takes a pointer to an int. If the pointer is null, print an error. Otherwise print the value.",
    answer="Start with if p equals equals nullptr. Print the error and return. After that, print star p.",
))

EPISODES.append(dict(
    n=46, title="new and delete", spoken="new and delete", yt="C++ new and delete: The Heap Explained",
    thumb="NEW + DELETE", vis="a crab borrowing a box from a warehouse and returning it",
    goals=["make a variable on the heap with new", "free it with delete", "explain stack and heap"],
    tags=["c++ new delete", "heap memory", "dynamic memory", "stack vs heap"],
    analogy="a library book: you borrow it with new, and you must return it with delete",
    c_pts=["New asks the heap for a box", "Delete gives the box back", "Every new needs one delete"],
    hook="Every new needs a delete.",
    intro="Today we ask for memory ourselves. We borrow a box from the heap, and we give it back when we finish.",
    concept="Local variables live on the stack. They appear and disappear by themselves. The heap is a big pool of memory that you manage yourself. New asks the heap for a box, and gives you its address.\n"
            "Delete returns the box. If you forget, the box is lost until the program ends. That is a memory leak. Think of a library book. You borrow it with new, and you must return it with delete.",
    A=dict(file="heap.cpp", label="One box on the heap", on="new makes an int on the heap, delete frees it",
           src='''
#include <iostream>
using namespace std;

int main() {
    int* p = new int(5);
    cout << *p << endl;
    *p = *p + 1;
    cout << *p << endl;
    delete p;
    return 0;
}
''',
           narr="[HL: new int(5)] New makes an int on the heap and sets it to five. It returns the address, and p stores it. [HL: cout << *p] Star p reads five. [HL: *p = *p + 1] We change the value to six. "
                "[HL: delete p] Delete gives the box back to the heap. After delete, p still holds the old address, so do not use p again."),
    ill=dict(label="Stack and heap", on="p lives on the stack, and the int lives on the heap",
             data=mem([("p", "int*", None, "stack"), ("value", "int", "6", "heap")], arrows=[("p", "value", "points to the heap box")], caption="The pointer is a local variable. The box it points to is on the heap"),
             narr="Look at the two regions. P is a normal local variable on the stack. It dies at the end of the function. "
                  "The int lives on the heap. It stays until you delete it. If you lose p before you delete, nobody can ever free that box."),
    B=dict(file="heaparray.cpp", label="An array on the heap", on="new with square brackets makes an array",
           src='''
#include <iostream>
using namespace std;

int main() {
    int* a = new int[3]{1, 2, 3};
    for (int i = 0; i < 3; i++) {
        a[i] = a[i] * 10;
    }
    cout << a[0] << " " << a[1] << " " << a[2] << endl;
    delete[] a;
    return 0;
}
''',
           narr="[HL: new int[3]] New with square brackets makes an array of three ints on the heap. [HL: for (int i] The loop multiplies each item by ten. [HL: cout << a[0]] The output is ten, twenty, thirty. "
                "[HL: delete[] a] An array made with new square brackets needs delete square brackets. A plain delete is a bug."),
    term="The program prints ten, twenty and thirty.",
    recap=["The stack holds local variables, and the heap holds boxes you manage.", "New asks the heap for a box.",
           "Delete gives the box back.", "Use delete with square brackets for an array."],
    bug=dict(title="The wrong delete", file="heaparray.cpp", kind="warn", wrong_note="an array is freed with plain delete",
             wrong='''
#include <iostream>
using namespace std;

int main() {
    int* a = new int[3]{1, 2, 3};
    cout << a[0] << endl;
    delete a;
    return 0;
}
''', fixed_note="delete with square brackets",
             fixed='''
#include <iostream>
using namespace std;

int main() {
    int* a = new int[3]{1, 2, 3};
    cout << a[0] << endl;
    delete[] a;
    return 0;
}
''',
             why="New with square brackets must pair with delete with square brackets. A plain delete frees the memory in the wrong way, and the result is undefined.",
             narr="Bug of the Day. We make an array with new square brackets, but we free it with plain delete. The compiler warns about a mismatched allocation function. "
                  "The two forms must match. New square brackets pairs with delete square brackets."),
    pun="I borrowed a box from the heap and forgot to return it. Now I have a leak in my budget.",
    task="make and free a heap array", challenge="Make an array of four ints on the heap. Fill it with the squares one, four, nine and sixteen. Print it, and free it.",
    answer="Use new int with four in square brackets. Fill with i plus one squared. Print the items, then call delete with square brackets.",
))

EPISODES.append(dict(
    n=47, title="Dynamic arrays", spoken="dynamic arrays", yt="C++ Dynamic Arrays: Size Chosen at Run Time",
    thumb="ANY SIZE", vis="a box that grows to fit the order",
    goals=["make an array with a size known only at run time", "free it correctly", "explain why vector is safer"],
    tags=["dynamic array c++", "new int[n]", "run time size", "vector vs array"],
    analogy="a tailor: he cuts the cloth only after you tell him your size",
    c_pts=["The size can come from the user", "You must free the array yourself", "A vector does the same job safely"],
    hook="The user decides the size, and the array fits.",
    intro="Today the user chooses the size. A plain array cannot do this, but an array on the heap can.",
    concept="A plain array needs a size that the compiler knows. An array on the heap can use a size that you read at run time. Use new with the size in square brackets.\n"
            "You must free it with delete square brackets. You must also remember its size yourself. This is why most programmers prefer a vector. Think of a tailor. He cuts the cloth only after you tell him your size.",
    A=dict(file="dyn.cpp", label="Size from the user", on="the user types the size, and the array fits",
           src='''
#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;
    int* a = new int[n];
    for (int i = 0; i < n; i++) {
        a[i] = (i + 1) * (i + 1);
    }
    for (int i = 0; i < n; i++) {
        cout << a[i] << " ";
    }
    cout << endl;
    delete[] a;
    return 0;
}
''', stdin="4",
           narr="[HL: cin >> n] The user types the size. We use four. [HL: new int[n]] New makes an array with n items. The compiler did not need to know n. [HL: a[i] = ] Each item gets the square of its position plus one. "
                "[HL: cout << a[i]] The output is one, four, nine, sixteen. [HL: delete[] a] We free the array at the end."),
    ill=dict(label="A pointer to n boxes", on="a points to four boxes on the heap",
             data=mem([("n", "int", "4"), ("a", "int*", None, "stack"), ("items", "int[4]", "1, 4, 9, 16", "heap")], arrows=[("a", "items[0]", "points to the first item")], caption="n is the size. a points to the heap array"),
             narr="N holds the size, four. A is a pointer on the stack. It points to the first of four boxes on the heap. "
                  "Note that the pointer does not know the size. You must keep n yourself."),
    B=dict(file="safer.cpp", label="The safer way", on="a vector does the same job in fewer lines",
           src='''
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> a(n);
    for (int i = 0; i < n; i++) {
        a[i] = (i + 1) * (i + 1);
    }
    for (int x : a) {
        cout << x << " ";
    }
    cout << endl;
    return 0;
}
''', stdin="4",
           narr="[HL: vector<int> a(n)] A vector with n items does the same job. [HL: a[i] = ] We fill it in the same way. [HL: for (int x : a)] A range-based for works too. "
                "There is no new and no delete. The vector frees its own memory. It also knows its size."),
    term="Type four and press Enter. The program prints one, four, nine and sixteen.",
    recap=["New with a size makes an array of any size at run time.", "Free it with delete square brackets.",
           "A pointer does not know the size of the array.", "A vector is safer and shorter."],
    bug=dict(title="Delete on a pointer to a local", file="dyn.cpp", kind="compile", wrong_note="delete is used on a plain int",
             wrong='''
#include <iostream>
using namespace std;

int main() {
    int n = 4;
    int* a = new int[n];
    a[0] = 1;
    cout << a[0] << endl;
    delete n;
    return 0;
}
''', fixed_note="delete is used on the pointer",
             fixed='''
#include <iostream>
using namespace std;

int main() {
    int n = 4;
    int* a = new int[n];
    a[0] = 1;
    cout << a[0] << endl;
    delete[] a;
    return 0;
}
''',
             why="Delete needs a pointer. The variable n is a plain int. Free the pointer that new returned, which is a.",
             narr="Bug of the Day. We call delete on n, which is a plain int. The compiler says the type int was given to delete, but a pointer is expected. "
                  "Delete must get the pointer that new returned. Here that is a, and it needs square brackets."),
    pun="A tailor and a programmer have one thing in common. They both measure twice and cut once.",
    task="average of n numbers", challenge="Ask for n. Make a vector of n numbers, read them, and print their average.",
    answer="Read n. Make vector of double with n items. Read each item with cin. Add them up, and divide by n.",
))

EPISODES.append(dict(
    n=48, title="Leaks and RAII", spoken="memory leaks and RAII", yt="C++ Memory Leaks and RAII Explained",
    thumb="NO LEAKS", vis="a leaking tap and a locked cupboard",
    goals=["explain what a memory leak is", "explain RAII", "see how a destructor cleans up"],
    tags=["memory leak c++", "raii", "destructor", "resource management"],
    analogy="a hotel room that locks and cleans itself when you check out",
    c_pts=["A leak happens when memory is never freed", "RAII ties cleanup to a variable's life", "A destructor runs when the variable ends"],
    hook="Let the variable clean up for you.",
    intro="Today we stop leaks for good. The trick is simple. Let a variable do the cleaning when it dies.",
    concept="A memory leak happens when you lose the address of a heap box before you free it. An early return or an error can cause it.\n"
            "The cure is RAII. It means that a resource belongs to a variable. When the variable dies, a special function called the destructor runs, and it frees the resource. Think of a hotel room. It cleans itself when you check out.",
    A=dict(file="raii.cpp", label="A destructor runs", on="a struct prints a message when it is made and when it dies",
           src='''
#include <iostream>
using namespace std;

struct Noisy {
    Noisy() { cout << "open" << endl; }
    ~Noisy() { cout << "close" << endl; }
};

int main() {
    {
        Noisy n;
        cout << "working" << endl;
    }
    cout << "after the block" << endl;
    return 0;
}
''',
           narr="[HL: struct Noisy] This struct has two special functions. We study them in module six. [HL: Noisy()] The first runs when a Noisy is made. [HL: ~Noisy()] The second, with a tilde, runs when it dies. "
                "[HL: Noisy n;] Here a Noisy is made, and open prints. [HL: cout << \"working\"] Then working prints. [HL: cout << \"after] The block ends, so n dies and close prints before the next line."),
    ill=dict(label="The life of a variable", on="a flow: made, used, closing brace, destructor runs",
             data=flow([("Made", "Constructor prints open"), ("Used", "The block prints working"), ("End of block", "n goes out of scope"), ("Cleanup", "Destructor prints close")]),
             narr="Follow the life of n. It is made, and open prints. The block uses it. At the closing brace, n goes out of scope. "
                  "The destructor runs at once, and close prints. You did not write any cleanup call."),
    B=dict(file="leak.cpp", label="A leak by early return", on="an early return skips the delete",
           src='''
#include <iostream>
using namespace std;

struct Noisy {
    Noisy() { cout << "open" << endl; }
    ~Noisy() { cout << "close" << endl; }
};

void work(bool fail) {
    Noisy* n = new Noisy;
    if (fail) {
        return;
    }
    delete n;
}

int main() {
    work(false);
    work(true);
    return 0;
}
''',
           narr="[HL: new Noisy] This function makes a Noisy on the heap with new. [HL: if (fail)] If fail is true, the function returns early. [HL: delete n] The delete is skipped. "
                "[HL: work(false)] The first call prints open and close. [HL: work(true)] The second call prints open only. The close is missing. That box is leaked."),
    term="The program prints open, close, and then open. The last close is missing.",
    recap=["A leak means that memory is never freed.", "An early return can skip a delete.",
           "RAII ties cleanup to the life of a variable.", "The destructor runs when the variable goes out of scope."],
    bug=dict(title="A leak you cannot see", file="leak.cpp", kind="output", wrong_note="the early return skips the delete",
             wrong='''
#include <iostream>
using namespace std;

struct Noisy {
    Noisy() { cout << "open" << endl; }
    ~Noisy() { cout << "close" << endl; }
};

void work(bool fail) {
    Noisy* n = new Noisy;
    if (fail) {
        return;
    }
    delete n;
}

int main() {
    work(true);
    return 0;
}
''', fixed_note="an ordinary variable cleans up by itself",
             fixed='''
#include <iostream>
using namespace std;

struct Noisy {
    Noisy() { cout << "open" << endl; }
    ~Noisy() { cout << "close" << endl; }
};

void work(bool fail) {
    Noisy n;
    if (fail) {
        return;
    }
}

int main() {
    work(true);
    return 0;
}
''',
             why="The early return skips the delete, so the destructor never runs. An ordinary local variable runs its destructor on every way out of the function.",
             narr="Bug of the Day. The program prints open, but it never prints close. The early return skips the delete, so the destructor never runs. "
                  "That is a leak. Use an ordinary local variable instead. Its destructor runs on every way out."),
    pun="My program had a leak. I tried to fix it with a bucket, but the bucket was on the heap.",
    task="spot the leak", challenge="Write a function with new and two return statements. Show which return leaks. Then fix it with a local variable.",
    answer="The return before the delete leaks. Replace the pointer with a local variable, and the destructor runs on both returns.",
))

EPISODES.append(dict(
    n=49, title="unique_ptr", spoken="unique pointers", yt="C++ unique_ptr: Smart Pointers, Part One",
    thumb="UNIQUE_PTR", vis="a single key for a single locker",
    goals=["make a unique_ptr with make_unique", "explain single ownership", "move ownership with std::move"],
    tags=["unique_ptr", "smart pointer", "make_unique", "std::move"],
    analogy="a house key with one owner: you can hand it over, but you cannot copy it",
    c_pts=["A unique_ptr owns one heap object", "It deletes the object by itself", "It cannot be copied, only moved"],
    hook="A pointer that frees itself.",
    intro="Today we meet the smart pointer that you will use most. It owns a heap object, and it frees the object for you.",
    concept="A unique pointer owns one heap object. When the unique pointer dies, it deletes the object. You never write delete. This is RAII for heap memory.\n"
            "A unique pointer has one owner. You cannot copy it, but you can move it to a new owner. Think of a house key with one owner. You can hand it over, but you cannot copy it.",
    A=dict(file="unique.cpp", label="make_unique", on="a unique_ptr owns an int",
           src='''
#include <iostream>
#include <memory>
using namespace std;

int main() {
    unique_ptr<int> p = make_unique<int>(5);
    cout << *p << endl;
    *p = 8;
    cout << *p << endl;
    return 0;
}
''',
           narr="[HL: #include <memory>] The memory header holds the smart pointers. [HL: make_unique<int>(5)] Make unique builds an int with the value five on the heap. The unique pointer p owns it. "
                "[HL: cout << *p] Star works as before. It reads five. [HL: *p = 8] We change it to eight. [HL: return 0] At the end of main, p dies and deletes the int. There is no delete in our code."),
    ill=dict(label="One owner", on="the unique_ptr on the stack owns the int on the heap",
             data=mem([("p", "std::unique_ptr<int>", None, "stack"), ("value", "int", "8", "heap")], arrows=[("p", "value", "owns")], caption="p owns the int. When p dies, the int is deleted"),
             narr="Look at the arrow. P owns the int on the heap. There is only one owner. When p goes out of scope, it deletes the int. "
                  "A raw pointer has no such duty. It only points."),
    B=dict(file="moveown.cpp", label="Move the ownership", on="std::move hands the object to another unique_ptr",
           src='''
#include <iostream>
#include <memory>
#include <utility>
using namespace std;

int main() {
    unique_ptr<int> a = make_unique<int>(5);
    unique_ptr<int> b = move(a);
    cout << (a == nullptr) << endl;
    cout << *b << endl;
    return 0;
}
''',
           narr="[HL: unique_ptr<int> a] A owns an int with the value five. [HL: move(a)] Move hands the ownership to b. [HL: cout << (a == nullptr)] A is now empty. It equals nullptr, so the program prints one. "
                "[HL: cout << *b] B owns the int and reads five. When b dies, the int is deleted exactly once."),
    term="The program prints one, and then five.",
    recap=["A unique pointer owns one heap object.", "It deletes the object when it dies.",
           "It cannot be copied.", "Use move to hand over the ownership."],
    bug=dict(title="Copying a unique_ptr", file="moveown.cpp", kind="compile", wrong_note="b is a copy of a",
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
''', fixed_note="b takes the ownership with move",
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
             why="Two unique pointers must never own the same object, or it would be deleted twice. The compiler blocks the copy. Use move.",
             narr="Bug of the Day. We copy a unique pointer. The compiler says use of deleted function. The copy is blocked on purpose. "
                  "Two owners would delete the object twice. Use move to hand over the ownership."),
    pun="A unique pointer never shares its umbrella. It is all about ownership.",
    task="own a heap int", challenge="Make a unique pointer to an int with the value twenty. Add one through the pointer, and print the result.",
    answer="Use make unique with twenty. Write star p plus plus, then print star p. The answer is twenty-one.",
))

EPISODES.append(dict(
    n=50, title="shared_ptr and weak_ptr", spoken="shared pointers and weak pointers", yt="C++ shared_ptr and weak_ptr Explained",
    thumb="SHARED_PTR", vis="three keys for one shared locker",
    goals=["share ownership with shared_ptr", "read use_count", "use weak_ptr to look without owning"],
    tags=["shared_ptr", "weak_ptr", "use_count", "reference counting"],
    analogy="a Wi-Fi password: many people share it, and the router stays on until the last one leaves",
    c_pts=["Many shared_ptr can own one object", "A counter tracks the owners", "A weak_ptr looks but does not own"],
    hook="Many owners, one object, deleted exactly once.",
    intro="Today the ownership is shared. Many pointers own one object, and the last one to leave switches off the light.",
    concept="A shared pointer lets many owners share one object. A counter inside tracks the owners. When the last owner dies, the object is deleted.\n"
            "A weak pointer looks at the object but does not own it. It does not change the counter. Think of a Wi-Fi password. Many people share it, and the router stays on until the last person leaves.",
    A=dict(file="shared.cpp", label="Count the owners", on="use_count goes up and down",
           src='''
#include <iostream>
#include <memory>
using namespace std;

int main() {
    shared_ptr<int> a = make_shared<int>(5);
    cout << a.use_count() << endl;
    {
        shared_ptr<int> b = a;
        cout << a.use_count() << endl;
    }
    cout << a.use_count() << endl;
    return 0;
}
''',
           narr="[HL: make_shared<int>(5)] Make shared builds an int and one shared pointer. [HL: cout << a.use_count()] The count is one. [HL: shared_ptr<int> b = a] B is a copy. Copying is allowed here. Both own the int. "
                "[HL: cout << a.use_count()] The count is two. [HL: }] At the closing brace, b dies. [HL: cout << a.use_count()] The count drops back to one."),
    ill=dict(label="Two owners, one object", on="two shared pointers point at the same int, which keeps a counter",
             data=mem([("a", "std::shared_ptr<int>", None, "stack"), ("b", "std::shared_ptr<int>", None, "stack"), ("value", "int", "5", "heap"), ("count", "int", "2", "heap")],
                      arrows=[("a", "value", "owns"), ("b", "value", "owns")], caption="The counter says two owners. The last owner deletes the int"),
             narr="Here are two owners, a and b. Both point at the same int. A counter next to the int says two. "
                  "When b dies, the counter becomes one. When a dies, it becomes zero, and the int is deleted."),
    B=dict(file="weak.cpp", label="A weak pointer", on="weak_ptr looks without owning",
           src='''
#include <iostream>
#include <memory>
using namespace std;

int main() {
    weak_ptr<int> w;
    {
        shared_ptr<int> s = make_shared<int>(7);
        w = s;
        cout << w.expired() << endl;
        if (auto locked = w.lock()) {
            cout << *locked << endl;
        }
    }
    cout << w.expired() << endl;
    return 0;
}
''',
           narr="[HL: weak_ptr<int> w] W is a weak pointer. It owns nothing. [HL: shared_ptr<int> s] S owns an int with the value seven. [HL: w = s] W now watches the same object. [HL: w.expired()] Expired asks if the object is gone. Not yet, so zero. "
                "[HL: w.lock()] Lock gives a shared pointer, if the object is alive. [HL: cout << *locked] It reads seven. [HL: cout << w.expired()] After the block, s is dead. The object is deleted, and expired is one."),
    term="The program prints zero, seven, and then one.",
    recap=["Many shared pointers can own one object.", "A counter tracks the owners, and the last owner deletes the object.",
           "A weak pointer watches without owning.", "Lock turns a weak pointer into a shared pointer, or an empty one."],
    bug=dict(title="A raw pointer into a shared_ptr", file="shared.cpp", kind="compile", wrong_note="a raw new result is assigned with an equals sign",
             wrong='''
#include <iostream>
#include <memory>
using namespace std;

int main() {
    shared_ptr<int> a = new int(5);
    cout << *a << endl;
    return 0;
}
''', fixed_note="make_shared builds the object",
             fixed='''
#include <iostream>
#include <memory>
using namespace std;

int main() {
    shared_ptr<int> a = make_shared<int>(5);
    cout << *a << endl;
    return 0;
}
''',
             why="The shared pointer constructor from a raw pointer is explicit, so an equals sign does not work. Make shared is also faster and safer.",
             narr="Bug of the Day. We assign a raw new result to a shared pointer. The compiler says it cannot convert int star to shared pointer. "
                  "Use make shared instead. It builds the object and the counter in one safe step."),
    pun="Shared pointers are polite. The last one out always turns off the light.",
    task="share a heap int between two owners", challenge="Make a shared pointer to an int. Copy it into a second shared pointer. Print use count.",
    answer="Use make shared for the first. Write the second as a copy of the first. Use count prints two.",
))
