"""Module 10 — Data structures and projects (EP 85-90)."""
from lib import flow, table, mem, graph

MODULE = {"id": 10, "name": "Data structures and projects", "range": "85–90", "colours": "Mint + Tomato", "bg": "mint"}
NEXT_AFTER = ("The end of the course", "That is the end of the course. Thank you for coding with us.")
EPISODES = []

EPISODES.append(dict(
    n=85, title="Linked list", spoken="linked list", yt="C++ Linked List from Scratch",
    thumb="LINKED LIST", vis="train cars joined by arrows",
    goals=["build a linked list with nodes", "walk along a list", "free every node"],
    tags=["c++ linked list", "node pointer", "data structures", "dynamic memory"],
    analogy="train cars: each car knows only the next car",
    c_pts=["A node holds a value and a pointer", "The head points to the first node", "Free every node when you finish"],
    hook="Build a train of nodes with pointers.",
    intro="Today we build our first data structure. A linked list is a chain of nodes, and each node points to the next one.",
    concept="A node holds a value and a pointer to the next node. The last node points to null. A pointer called head points to the first node.\n"
            "Think of train cars. Each car knows only the next car. To reach the last car, you walk along the train.",
    A=dict(file="list.cpp", label="Build, walk and free", on="three nodes are linked, printed, and freed",
           src='''
#include <iostream>
using namespace std;

struct Node {
    int value;
    Node* next;
};

int main() {
    Node* head = new Node{10, nullptr};
    head->next = new Node{20, nullptr};
    head->next->next = new Node{30, nullptr};
    for (Node* cur = head; cur != nullptr; cur = cur->next) {
        cout << cur->value << " ";
    }
    cout << endl;
    while (head != nullptr) {
        Node* next = head->next;
        delete head;
        head = next;
    }
    return 0;
}
''',
           narr="[HL: struct Node] A node has a value and a pointer to the next node. [HL: Node* head = new Node] New makes the first node on the heap. The head pointer keeps its address. "
                "[HL: head->next = new Node] The next pointer of the first node points to a second node. [HL: head->next->next] The same step adds a third node. [HL: for (Node* cur = head] The walker cur starts at the head. "
                "[HL: cur = cur->next] Each step moves cur to the next node. The loop stops at null. The output is ten twenty thirty. [HL: Node* next = head->next] To free the list, first save the next pointer. [HL: delete head] Then delete the node. "
                "[HL: head = next] Then move on. If you delete first, you lose the way forward."),
    ill=dict(label="Three nodes on the heap", on="memory boxes: head and three nodes joined by next pointers",
             data=mem([("head", "Node*", None, "stack"), ("n1.value", "int", "10", "heap"), ("n1.next", "Node*", None, "heap"), ("n2.value", "int", "20", "heap"), ("n2.next", "Node*", None, "heap"),
                       ("n3.value", "int", "30", "heap"), ("n3.next", "Node*", "nullptr", "heap")],
                      arrows=[("head", "n1.value", "head"), ("n1.next", "n2.value", "next"), ("n2.next", "n3.value", "next")],
                      caption="Each next pointer holds the address of the following node"),
             narr="The head pointer lives on the stack. The three nodes live on the heap. Each next pointer holds the address of the next node. "
                  "The last pointer is null, so the walk stops there."),
    B=dict(file="push.cpp", label="Add at the front", on="a function adds a node at the front of the list",
           src='''
#include <iostream>
using namespace std;

struct Node {
    int value;
    Node* next;
};

Node* push_front(Node* head, int value) {
    return new Node{value, head};
}

void print_list(const Node* head) {
    for (const Node* cur = head; cur != nullptr; cur = cur->next) {
        cout << cur->value << " ";
    }
    cout << endl;
}

void free_list(Node* head) {
    while (head != nullptr) {
        Node* next = head->next;
        delete head;
        head = next;
    }
}

int main() {
    Node* head = nullptr;
    for (int i = 1; i <= 3; ++i) {
        head = push_front(head, i);
    }
    print_list(head);
    free_list(head);
    return 0;
}
''',
           narr="[HL: Node* push_front] This function makes a new node, and its next pointer is the old head. The new node is now the first one. [HL: Node* head = nullptr] An empty list has a null head. "
                "[HL: head = push_front(head, i)] Each call returns the new head, so we store it. [HL: print_list(head)] We add one, then two, then three, each at the front. The list prints three two one. "
                "[HL: free_list(head)] Free list deletes every node."),
    term="The program prints ten twenty thirty, and then three two one.",
    recap=["A node holds a value and a next pointer.", "The head points to the first node.", "Walk the list until the pointer is null.", "Save the next pointer before you delete a node."],
    bug=dict(title="The walk stops one node early", file="early.cpp", kind="output", wrong_note="the loop tests cur->next instead of cur",
             wrong='''
#include <iostream>
using namespace std;

struct Node {
    int value;
    Node* next;
};

int main() {
    Node* head = new Node{1, new Node{2, new Node{3, nullptr}}};
    for (Node* cur = head; cur->next != nullptr; cur = cur->next) {
        cout << cur->value << " ";
    }
    cout << endl;
    while (head != nullptr) {
        Node* next = head->next;
        delete head;
        head = next;
    }
    return 0;
}
''', fixed_note="the loop tests cur",
             fixed='''
#include <iostream>
using namespace std;

struct Node {
    int value;
    Node* next;
};

int main() {
    Node* head = new Node{1, new Node{2, new Node{3, nullptr}}};
    for (Node* cur = head; cur != nullptr; cur = cur->next) {
        cout << cur->value << " ";
    }
    cout << endl;
    while (head != nullptr) {
        Node* next = head->next;
        delete head;
        head = next;
    }
    return 0;
}
''',
             why="The test cur next not null stops at the last node, before it prints. Test cur itself. It is null only after the last node.",
             narr="Bug of the Day. The list holds one, two and three, but the output shows only one and two. The loop tests the next pointer. "
                  "It stops on the last node, before it prints. Test cur itself."),
    pun="Why did the node feel lonely? It only ever knew the next one.",
    task="count the nodes", challenge="Write a function that counts the nodes in a linked list. An empty list has zero nodes.",
    answer="Set a counter to zero. Walk with a pointer from the head until null. Add one on each step.",
))

EPISODES.append(dict(
    n=86, title="Binary tree", spoken="binary tree", yt="C++ Binary Search Tree: Insert, Search, Traverse",
    thumb="BINARY TREE", vis="an upside down tree with numbers on its branches",
    goals=["insert into a binary search tree", "print a tree in sorted order", "search a tree and find its height"],
    tags=["c++ binary tree", "binary search tree", "recursion", "inorder traversal", "data structures"],
    analogy="a family tree where small numbers go left and big numbers go right",
    c_pts=["Each node has a left and a right child", "Smaller keys go left", "Inorder traversal prints sorted keys"],
    hook="Print numbers in sorted order with no sort call.",
    intro="Today we build a tree. Each node has two children. Small numbers go left, and big numbers go right.",
    concept="A binary search tree keeps its keys in order. For each node, every key in the left side is smaller, and every key in the right side is bigger.\n"
            "Recursion fits trees well. To insert, compare the key, then go left or right, and repeat.",
    A=dict(file="tree.cpp", label="Insert and print in order", on="five keys are inserted and printed in sorted order",
           src='''
#include <iostream>
using namespace std;

struct Node {
    int key;
    Node* left;
    Node* right;
};

Node* insert(Node* root, int key) {
    if (root == nullptr) {
        return new Node{key, nullptr, nullptr};
    }
    if (key < root->key) {
        root->left = insert(root->left, key);
    } else {
        root->right = insert(root->right, key);
    }
    return root;
}

void inorder(const Node* node) {
    if (node == nullptr) {
        return;
    }
    inorder(node->left);
    cout << node->key << " ";
    inorder(node->right);
}

void destroy(Node* node) {
    if (node == nullptr) {
        return;
    }
    destroy(node->left);
    destroy(node->right);
    delete node;
}

int main() {
    Node* root = nullptr;
    for (int k : {5, 3, 8, 1, 4}) {
        root = insert(root, k);
    }
    inorder(root);
    cout << endl;
    destroy(root);
    return 0;
}
''',
           narr="[HL: Node* insert] Insert returns the root of the tree after the change. [HL: if (root == nullptr)] An empty spot is the base case. We make a new node there. "
                "[HL: if (key < root->key)] A smaller key goes into the left side. [HL: else {] A bigger key goes into the right side. [HL: for (int k : {5, 3, 8, 1, 4})] We insert five, three, eight, one and four. "
                "[HL: inorder(node->left)] Inorder visits the left side first. [HL: cout << node->key] Then it prints the node. [HL: inorder(node->right)] Then it visits the right side. The output is one three four five eight. "
                "[HL: destroy(node->left)] Destroy deletes the children first, and then the node."),
    ill=dict(label="The tree", on="a tree with five, three, eight, one and four",
             data=graph([("n5", "5", "root"), ("n3", "3", "left of 5"), ("n8", "8", "right of 5"), ("n1", "1", "left of 3"), ("n4", "4", "right of 3")],
                        [("n5", "n3", "left"), ("n5", "n8", "right"), ("n3", "n1", "left"), ("n3", "n4", "right")], layout="tree"),
             narr="Five is the root. Three is smaller, so it goes left. Eight is bigger, so it goes right. "
                  "One goes left of three, and four goes right of three."),
    B=dict(file="search.cpp", label="Search and height", on="the tree is searched, and its height is measured",
           src='''
#include <algorithm>
#include <iostream>
using namespace std;

struct Node {
    int key;
    Node* left;
    Node* right;
};

Node* insert(Node* root, int key) {
    if (root == nullptr) {
        return new Node{key, nullptr, nullptr};
    }
    if (key < root->key) {
        root->left = insert(root->left, key);
    } else {
        root->right = insert(root->right, key);
    }
    return root;
}

bool contains(const Node* node, int key) {
    if (node == nullptr) {
        return false;
    }
    if (key == node->key) {
        return true;
    }
    return key < node->key ? contains(node->left, key) : contains(node->right, key);
}

int height(const Node* node) {
    if (node == nullptr) {
        return 0;
    }
    return 1 + max(height(node->left), height(node->right));
}

void destroy(Node* node) {
    if (node == nullptr) {
        return;
    }
    destroy(node->left);
    destroy(node->right);
    delete node;
}

int main() {
    Node* root = nullptr;
    for (int k : {5, 3, 8, 1, 4}) {
        root = insert(root, k);
    }
    cout << boolalpha << contains(root, 4) << endl;
    cout << contains(root, 7) << endl;
    cout << height(root) << endl;
    destroy(root);
    return 0;
}
''',
           narr="[HL: bool contains] Contains follows one path only. [HL: return false] An empty spot means the key is not in the tree. [HL: if (key == node->key)] A match means the key is in the tree. "
                "[HL: return key < node->key ?] Otherwise it goes left or right, as insert did. Four is in the tree, so we get true. Seven is not, so we get false. [HL: int height] Height is one plus the height of the taller child. "
                "[HL: max(height(node->left)] Max picks the taller side. This tree has height three."),
    term="The program prints one three four five eight, then true, false, and three.",
    recap=["A binary search tree keeps keys in order.", "Smaller keys go left, and bigger keys go right.", "Inorder traversal prints the keys in sorted order.", "Recursion fits trees well."],
    bug=dict(title="Printing before the left side", file="preorder.cpp", kind="output", wrong_note="the node prints before the left side",
             wrong='''
#include <iostream>
using namespace std;

struct Node {
    int key;
    Node* left;
    Node* right;
};

void show(const Node* node) {
    if (node == nullptr) {
        return;
    }
    cout << node->key << " ";
    show(node->left);
    show(node->right);
}

int main() {
    Node a{1, nullptr, nullptr};
    Node c{4, nullptr, nullptr};
    Node b{3, &a, &c};
    Node root{5, &b, nullptr};
    show(&root);
    cout << endl;
    return 0;
}
''', fixed_note="the node prints between the two sides",
             fixed='''
#include <iostream>
using namespace std;

struct Node {
    int key;
    Node* left;
    Node* right;
};

void show(const Node* node) {
    if (node == nullptr) {
        return;
    }
    show(node->left);
    cout << node->key << " ";
    show(node->right);
}

int main() {
    Node a{1, nullptr, nullptr};
    Node c{4, nullptr, nullptr};
    Node b{3, &a, &c};
    Node root{5, &b, nullptr};
    show(&root);
    cout << endl;
    return 0;
}
''',
             why="The order of the three lines decides the traversal. Left, node, right gives sorted order. Node first gives preorder, which is not sorted.",
             narr="Bug of the Day. The keys come out as five three one four, which is not sorted. The code prints the node before the left side. "
                  "Visit left first, then print, then visit right."),
    pun="Why did the tree win the race? It had strong roots, and it never lost its balance.",
    task="find the smallest key", challenge="Write a function that returns the smallest key in a binary search tree. Hint: keep going left.",
    answer="Start at the root. While the left child is not null, move to the left child. Return that key.",
))

EPISODES.append(dict(
    n=87, title="Threads and mutex", spoken="threads and mutex", yt="C++ Threads and Mutex: Concurrency Basics",
    thumb="THREADS", vis="two crabs working on one pile, with a lock on the door",
    goals=["start a thread and join it", "share data between threads", "protect shared data with a mutex"],
    tags=["c++ thread", "std::mutex", "lock_guard", "concurrency", "join"],
    analogy="two cooks in one kitchen, and a key to the pantry",
    c_pts=["A thread runs code at the same time", "Join waits for a thread to finish", "A mutex lets one thread in at a time"],
    hook="Run two jobs at the same time.",
    intro="Today we run code on two threads at once. We also learn the lock that keeps shared data safe.",
    concept="A thread is a second path of execution. Two threads can run at the same time. You must join each thread before it goes out of scope.\n"
            "When two threads change the same data, they can clash. A mutex is a key. Only the thread that holds the key may enter. Think of two cooks and one pantry.",
    A=dict(file="thread.cpp", label="Start and join a thread", on="a thread adds numbers, and main joins it",
           src='''
#include <iostream>
#include <thread>
using namespace std;

int main() {
    int result = 0;
    thread t([&result]() {
        for (int i = 1; i <= 100; ++i) {
            result += i;
        }
    });
    t.join();
    cout << result << endl;
    return 0;
}
''',
           narr="[HL: thread t(] This line starts a new thread. The thread runs the lambda at once. [HL: [&result]] The lambda captures result by reference, so it can change the variable of main. "
                "[HL: result += i] It adds the numbers from one to one hundred. [HL: t.join()] Join makes main wait until the thread is done. [HL: cout << result] Now it is safe to read result. The sum is five thousand and fifty."),
    ill=dict(label="Start, work, join", on="a flow: main starts a thread, both run, main joins",
             data=flow([("start", "main makes thread t"), ("work", "t adds the numbers"), ("join", "main waits at join"), ("read", "main prints the result")]),
             narr="Main starts the thread. The thread does the work. Main waits at join. "
                  "Only after the join does main read the result."),
    B=dict(file="mutex.cpp", label="Two threads, one counter", on="two threads add to one counter, guarded by a mutex",
           src='''
#include <iostream>
#include <mutex>
#include <thread>
using namespace std;

int main() {
    int counter = 0;
    mutex m;
    auto work = [&]() {
        for (int i = 0; i < 1000; ++i) {
            lock_guard<mutex> lock(m);
            ++counter;
        }
    };
    thread a(work);
    thread b(work);
    a.join();
    b.join();
    cout << counter << endl;
    return 0;
}
''',
           narr="[HL: mutex m] The mutex is the key to the pantry. [HL: auto work] Both threads run this same lambda. Each one adds one to the counter, one thousand times. [HL: lock_guard<mutex> lock(m)] Lock guard takes the key. It gives the key back at the end of each pass. "
                "While one thread holds the key, the other thread waits. [HL: ++counter] So the two threads never change the counter together. [HL: a.join()] Main joins both threads. The counter is two thousand every time."),
    term="The program prints five thousand and fifty, and then two thousand.",
    recap=["A thread runs code at the same time as main.", "Join waits for a thread to finish.", "Two threads that change the same data need a mutex.", "Lock guard gives the key back for you."],
    bug=dict(title="A thread that is never joined", file="nojoin.cpp", kind="runtime", wrong_note="the thread goes out of scope without a join",
             wrong='''
#include <iostream>
#include <thread>
using namespace std;

int main() {
    thread t([]() { cout << "hello" << endl; });
    return 0;
}
''', fixed_note="main joins the thread",
             fixed='''
#include <iostream>
#include <thread>
using namespace std;

int main() {
    thread t([]() { cout << "hello" << endl; });
    t.join();
    return 0;
}
''',
             why="A thread that goes out of scope while it is still joinable ends the program. Always join the thread, or detach it on purpose.",
             narr="Bug of the Day. We start a thread and never join it. The program stops with terminate called without an active exception. "
                  "Join every thread before main ends."),
    pun="Why did two threads share one door? They took turns, because one had the key.",
    task="sum two halves", challenge="Start two threads. Each thread adds half of a vector into its own variable. Join both, and print the total.",
    answer="Make two result variables. Each thread adds its own half into its own variable. After both joins, add the two results.",
))

EPISODES.append(dict(
    n=88, title="Project: student records", spoken="project, student records", yt="C++ Project: Student Records Program",
    thumb="PROJECT", vis="a crab with a clipboard and a stack of report cards",
    goals=["design a small class", "combine a vector, a lambda and algorithms", "write a const correct class"],
    tags=["c++ project", "student records", "class design", "const correctness", "beginner project"],
    analogy="a teacher with a register: add a student, ask for the average",
    c_pts=["One class owns the data", "Methods that only read are const", "Use library algorithms inside the class"],
    hook="Build a real program from the parts you know.",
    intro="Today we build a small project. A roster class holds student marks. It can add a student, print a ranking, and find the best student.",
    concept="A good class owns its data and hides it. It offers a few clear methods. Methods that only read the data are marked const.\n"
            "We use a vector to store students, a lambda to sort them, and an optional for the best student.",
    A=dict(file="roster.cpp", label="The Roster class", on="a roster adds students, ranks them and computes the average",
           src='''
#include <algorithm>
#include <iomanip>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

struct Student {
    string name;
    int marks;
};

class Roster {
public:
    void add(const string& name, int marks) {
        students_.push_back({name, marks});
    }

    double average() const {
        double total = 0;
        for (const Student& s : students_) {
            total += s.marks;
        }
        return students_.empty() ? 0 : total / students_.size();
    }

    void print_ranking() const {
        vector<Student> copy = students_;
        sort(copy.begin(), copy.end(), [](const Student& a, const Student& b) { return a.marks > b.marks; });
        for (const Student& s : copy) {
            cout << s.name << " " << s.marks << endl;
        }
    }

private:
    vector<Student> students_;
};

int main() {
    Roster r;
    r.add("Ravi", 78);
    r.add("Asha", 91);
    r.add("Mia", 85);
    r.print_ranking();
    cout << fixed << setprecision(1) << r.average() << endl;
    return 0;
}
''',
           narr="[HL: void add] Add stores one student at the back of the vector. [HL: double average() const] Average only reads the data, so it is const. [HL: return students_.empty()] If the roster is empty, we return zero, and we never divide by zero. "
                "[HL: vector<Student> copy = students_] Print ranking works on a copy, so the original order does not change. [HL: sort(copy.begin()] The lambda puts the highest marks first. [HL: private:] The vector is private. Only the class can change it. "
                "[HL: r.add(\"Ravi\", 78)] Main adds three students. [HL: r.print_ranking()] The ranking is Asha ninety-one, Mia eighty-five, Ravi seventy-eight. [HL: setprecision(1)] The average is eighty-four point seven."),
    ill=dict(label="Class design", on="a table of the members of Roster",
             data=table(["Member", "Kind", "Const", "Job"], [["students_", "data, private", "no", "holds every Student"], ["add", "method", "no", "stores one student"], ["average", "method", "yes", "returns the mean mark"], ["print_ranking", "method", "yes", "prints highest marks first"]]),
             narr="The data is private. The add method changes the roster, so it is not const. "
                  "Average and print ranking only read the data, so both are const."),
    B=dict(file="best.cpp", label="The best student", on="best returns an optional student",
           src='''
#include <algorithm>
#include <iostream>
#include <optional>
#include <string>
#include <vector>
using namespace std;

struct Student {
    string name;
    int marks;
};

class Roster {
public:
    void add(const string& name, int marks) {
        students_.push_back({name, marks});
    }

    optional<Student> best() const {
        if (students_.empty()) {
            return nullopt;
        }
        return *max_element(students_.begin(), students_.end(),
                            [](const Student& a, const Student& b) { return a.marks < b.marks; });
    }

private:
    vector<Student> students_;
};

int main() {
    Roster r;
    auto none = r.best();
    cout << none.has_value() << endl;
    r.add("Ravi", 78);
    r.add("Asha", 91);
    auto top = r.best();
    if (top) {
        cout << top->name << " " << top->marks << endl;
    }
    return 0;
}
''',
           narr="[HL: optional<Student> best() const] Best returns an optional, because an empty roster has no best student. [HL: return nullopt] For an empty roster, it returns nullopt. "
                "[HL: max_element(students_.begin()] Max element finds the student with the highest marks. [HL: a.marks < b.marks] The lambda says that a is smaller than b when a has fewer marks. "
                "[HL: none.has_value()] The first call is on an empty roster, so it prints zero. [HL: if (top)] After two adds, the optional holds a value. The output is Asha ninety-one."),
    term="The program prints the ranking and the average, then zero, and then Asha ninety-one.",
    recap=["A class owns its data and keeps it private.", "Mark read only methods const.", "A lambda gives sort its rule.", "Optional says that a result may not exist."],
    bug=dict(title="A const object calls a non const method", file="constbug.cpp", kind="compile", wrong_note="average is not marked const, but show gets a const reference",
             wrong='''
#include <iostream>
#include <vector>
using namespace std;

class Roster {
public:
    void add(int marks) { marks_.push_back(marks); }
    double average() {
        double total = 0;
        for (int m : marks_) {
            total += m;
        }
        return marks_.empty() ? 0 : total / marks_.size();
    }

private:
    vector<int> marks_;
};

void show(const Roster& r) {
    cout << r.average() << endl;
}

int main() {
    Roster r;
    r.add(80);
    show(r);
    return 0;
}
''', fixed_note="average is marked const",
             fixed='''
#include <iostream>
#include <vector>
using namespace std;

class Roster {
public:
    void add(int marks) { marks_.push_back(marks); }
    double average() const {
        double total = 0;
        for (int m : marks_) {
            total += m;
        }
        return marks_.empty() ? 0 : total / marks_.size();
    }

private:
    vector<int> marks_;
};

void show(const Roster& r) {
    cout << r.average() << endl;
}

int main() {
    Roster r;
    r.add(80);
    show(r);
    return 0;
}
''',
             why="A const reference may call only const methods. Add const after the parameter list of every method that does not change the object.",
             narr="Bug of the Day. The function gets a const reference, and calls average. The compiler says this discards qualifiers. "
                  "Average does not change the object, so mark it const."),
    pun="Why did the roster stay calm? Everything inside it was in order.",
    task="add a method to find a student", challenge="Add a method that takes a name and returns the marks of that student as an optional.",
    answer="Loop over the students. If the name matches, return the marks. After the loop, return nullopt.",
))

EPISODES.append(dict(
    n=89, title="Common mistakes and exam questions", spoken="common mistakes and exam questions", yt="C++ Common Mistakes and Exam Questions",
    thumb="EXAM TRAPS", vis="a crab avoiding banana peels on an exam paper",
    goals=["spot six classic traps", "explain integer division and wraparound", "compare floating point numbers safely"],
    tags=["c++ common mistakes", "c++ exam questions", "integer division", "floating point compare", "interview questions"],
    analogy="banana peels on the road: easy to see once you know them",
    c_pts=["Integer division drops the decimals", "Small types wrap around", "Never compare doubles with equals"],
    hook="Six traps that fail exams.",
    intro="Today is a safety walk through the traps. Exams and interviews love them, and now you can avoid every one.",
    concept="Most wrong answers come from a few old traps. Integer division drops the decimals. A small type wraps around when it is too small. A double is not exact, so equals can fail.\n"
            "Also, never return a reference to a local variable. Never use a moved object. Never forget to free what you made with new.",
    A=dict(file="traps.cpp", label="Division and wraparound", on="integer division and a char that wraps around",
           src='''
#include <iostream>
using namespace std;

int main() {
    cout << 7 / 2 << endl;
    unsigned char c = 250;
    c += 10;
    cout << static_cast<int>(c) << endl;
    return 0;
}
''',
           narr="[HL: 7 / 2] Both numbers are ints, so the answer is an int. The decimals are cut, and the answer is three. [HL: unsigned char c = 250] An unsigned char holds values from zero to two hundred and fifty-five. "
                "[HL: c += 10] Adding ten goes past the top, and the value wraps around to zero. [HL: static_cast<int>(c)] The cast to int prints the number, not a letter. The answer is four. "
                "Exam tip. Always ask what the type can hold."),
    ill=dict(label="Six classic traps", on="a table of six mistakes, the symptom and the fix",
             data=table(["Trap", "Symptom", "Fix"], [["integer division", "7 / 2 gives 3", "make one side a double"], ["wraparound", "250 + 10 gives 4 in an unsigned char", "use a bigger type"],
                                                    ["double equals", "0.1 + 0.2 == 0.3 is false", "compare with a small epsilon"], ["dangling reference", "returns a reference to a local", "return by value"],
                                                    ["use after move", "reads a moved-from object", "do not use it again"], ["leak", "new without delete", "use a smart pointer"]]),
             narr="Here are the six traps. Each one has a symptom and a fix. Learn the symptom, and the fix follows."),
    B=dict(file="floats.cpp", label="Comparing doubles", on="equals fails for doubles, and an epsilon test works",
           src='''
#include <cmath>
#include <iostream>
using namespace std;

int main() {
    double a = 0.1 + 0.2;
    cout << boolalpha << (a == 0.3) << endl;
    cout << (fabs(a - 0.3) < 1e-9) << endl;
    return 0;
}
''',
           narr="[HL: double a = 0.1 + 0.2] A double stores a close value, and not the exact value. [HL: (a == 0.3)] So the test with equals is false. [HL: fabs(a - 0.3) < 1e-9] Instead, take the difference. "
                "If its size is smaller than a tiny epsilon, the numbers are equal for our purpose. This test is true."),
    term="The program prints three, then four, then false, and then true.",
    recap=["Integer division drops the decimals.", "A small type wraps around.", "Never compare doubles with equals.", "Never return a reference to a local variable."],
    bug=dict(title="A reference to a local variable", file="dangling.cpp", kind="warn", wrong_note="biggest returns a reference to a local variable",
             wrong='''
#include <iostream>
using namespace std;

const int& biggest(int a, int b) {
    int result = a > b ? a : b;
    return result;
}

int main() {
    cout << biggest(3, 8) << endl;
    return 0;
}
''', fixed_note="biggest returns by value",
             fixed='''
#include <iostream>
using namespace std;

int biggest(int a, int b) {
    return a > b ? a : b;
}

int main() {
    cout << biggest(3, 8) << endl;
    return 0;
}
''',
             why="The local variable dies when the function ends, so the reference points to nothing. Return small values by value.",
             narr="Bug of the Day. The function returns a reference to a local variable. The compiler warns that it returns a reference to a local variable. "
                  "The variable dies at the end of the function. Return by value."),
    pun="Why did the exam trap fail? We saw it coming.",
    task="fix three traps", challenge="Fix this: a program prints the average of seven and two as three. Make it print three point five.",
    answer="Make one of the two numbers a double, or use a cast. Then the division keeps the decimals.",
))

EPISODES.append(dict(
    n=90, title="Finale: what you can build", spoken="finale, what you can build", yt="C++ Course Finale: What You Can Build Now",
    thumb="YOU DID IT", vis="a crab on a podium holding a trophy of code",
    goals=["read a modern C++ program", "see the whole course map", "choose a project to build next"],
    tags=["c++ course finale", "c++ roadmap", "learn c++", "what to build", "c++ projects"],
    analogy="a map of everything you have climbed",
    c_pts=["You can read modern C plus plus", "You know the whole core language", "The next step is to build something"],
    hook="You can now read modern C plus plus.",
    intro="This is the last episode. We read one modern program together, look at the road you walked, and pick what to build next.",
    concept="You started with a first program. Now you know types, control flow, functions, memory, classes, inheritance, templates, the library, and threads.\n"
            "Reading is the first skill. Let us read a small modern program, line by line, and see how much you already know.",
    A=dict(file="library.cpp", label="A small modern program", on="books are searched, sorted and printed",
           src='''
#include <algorithm>
#include <iostream>
#include <optional>
#include <string>
#include <vector>
using namespace std;

struct Book {
    string title;
    int pages;
};

optional<Book> longest(const vector<Book>& books) {
    if (books.empty()) {
        return nullopt;
    }
    return *max_element(books.begin(), books.end(),
                        [](const Book& a, const Book& b) { return a.pages < b.pages; });
}

int main() {
    vector<Book> books = {{"Basics", 120}, {"Pointers", 200}, {"Templates", 150}};
    if (auto top = longest(books)) {
        cout << top->title << " " << top->pages << endl;
    }
    sort(books.begin(), books.end(), [](const Book& a, const Book& b) { return a.title < b.title; });
    for (const Book& b : books) {
        cout << b.title << endl;
    }
    return 0;
}
''',
           narr="[HL: struct Book] A struct groups a title and a page count. [HL: optional<Book> longest] The function may have no answer, so it returns an optional. [HL: max_element] It uses a library algorithm with a lambda. "
                "[HL: if (auto top = longest(books))] The if statement makes the optional and tests it in one step. [HL: top->title] The longest book is Pointers, with two hundred pages. [HL: sort(books.begin()] Then we sort by title. "
                "[HL: for (const Book& b : books)] A range for loop prints the titles in order. You learned every part of this program."),
    ill=dict(label="Your road", on="a flow of the six stages of the course",
             data=flow([("Start", "first program and basics"), ("Core", "types, decisions, loops, functions"), ("Memory", "pointers, arrays, strings"), ("Objects", "classes, inheritance, polymorphism"),
                        ("Library", "templates, containers, algorithms"), ("Next", "your own projects")]),
             narr="Here is your road. You began with a first program. Then came the core language, and then memory. "
                  "After that came objects, templates and the library. The next stage is yours."),
    B=dict(file="grades.cpp", label="Maps and structured bindings", on="a map is printed with structured bindings",
           src='''
#include <iostream>
#include <map>
#include <string>
using namespace std;

int main() {
    map<string, int> marks = {{"Asha", 91}, {"Mia", 85}};
    for (const auto& [name, mark] : marks) {
        cout << name << " " << mark << endl;
    }
    return 0;
}
''',
           narr="[HL: map<string, int> marks] A map joins names to marks. [HL: const auto& [name, mark]] A structured binding names the key and the value. [HL: cout << name] The loop prints Asha ninety-one, and then Mia eighty-five. "
                "This is modern C plus plus. It is short, and you can read it."),
    term="The program prints Pointers two hundred, then the sorted titles, then the two students from the map.",
    recap=["You can read modern C plus plus.", "You know the core language, memory, objects and the library.", "The next step is to build a project.", "Pick one idea, and build it small."],
    bug=dict(title="The last classic: a missing semicolon", file="semicolon.cpp", kind="compile", wrong_note="the struct has no semicolon after the closing brace",
             wrong='''
#include <iostream>
using namespace std;

struct Point {
    int x;
    int y;
}

int main() {
    Point p{1, 2};
    cout << p.x << endl;
    return 0;
}
''', fixed_note="the struct ends with a semicolon",
             fixed='''
#include <iostream>
using namespace std;

struct Point {
    int x;
    int y;
};

int main() {
    Point p{1, 2};
    cout << p.x << endl;
    return 0;
}
''',
             why="A struct or a class definition ends with a semicolon. The compiler often reports the error on the next line, so read one line up.",
             narr="Bug of the Day, the last one. The struct has no semicolon after the closing brace. The compiler says expected semicolon after struct definition. "
                  "Read the error, and look one line up."),
    pun="Why did the programmer love this course? Every bug had a fix, and every fix had a pun.",
    task="build your own project", challenge="Pick one small idea. A quiz, a contact book, or a to do list. Build it, and share it in the comments.",
    answer="Start with one struct and one vector. Add one feature at a time, and compile after each step.",
))
