"""Longer narration for module 9 (EP 77-84). Each text is added to the end of the matching text in m09.py.

Keys: intro, concept, A, ill, B, term, bug, hint (hint goes into the challenge scene).
Rules: docs/cpp-bible/STE.md. Cues [HL n] point at lines of the code file for that scene.
"""
EXT = {
    77: dict(
        concept="Experienced programmers rarely write a loop for sorting, searching or counting. They call an algorithm. "
                "The code is shorter, and it has fewer bugs.\n"
                "The library algorithms are tuned by experts. Most of the time, they are faster than what you would write yourself. "
                "Learn the names, and you will save hours.",
        A="[HL 8] Sort takes two iterators, the start and the end. After this line, the vector is in order. "
          "[HL 13] Max element gives an iterator, so we put a star in front to read the value. The answer is nine. "
          "[HL 14] Reverse turns the order round. "
          "[HL 15] Now the first item is nine.",
        ill="Notice the common shape of the calls. Each takes a begin and an end. Then it may take a value or a rule. "
            "Once you know one algorithm, the others feel familiar.",
        B="[HL 9] Find looks for the value eight, and it gives an iterator. "
          "[HL 10] Always test the iterator against end, before you read it. "
          "[HL 13] Count tells how many times four appears. It is three. "
          "[HL 14] Accumulate adds all the items, starting from zero. The total is twenty-one.",
        term="Check by hand. Four plus eight plus four plus one plus four is twenty-one.",
        bug="The classic sort needs the start and the end. If you pass only the vector, the compiler cannot match the call. "
            "C plus plus twenty has a ranges version that takes the whole vector. For now, write begin and end.",
        hint="Hint: the min element function works like max element, and it also gives an iterator.",
    ),
    78: dict(
        concept="Many algorithms take a rule as the last argument. The rule says how to compare, or what to count. A lambda is the best way to write the rule.\n"
                "Write the lambda right where you need it. The reader sees the rule next to the call, and does not have to jump to another place.",
        A="[HL 8] The third argument is a lambda that takes two ints. It returns true when a is bigger than b. "
          "This changes sort from smallest first to biggest first. "
          "[HL 13] The variable limit is four. "
          "[HL 14] The capture list holds limit, so the lambda can read it. Count if counts the numbers above four. The answer is three.",
        ill="Notice the two jobs. The lambda in sort decides the order of two items. The lambda in count if answers a yes or no question about one item. "
            "The algorithm calls the lambda again and again.",
        B="[HL 13] This vector holds three students. "
          "[HL 14] The lambda compares the marks, so the students are ordered by their marks, highest first. "
          "[HL 15] For each runs a lambda on every student. It prints the name and the marks.",
        term="Notice the order of the output. Asha has ninety-one, Mia has eighty-five, and Ravi has seventy-eight.",
        bug="A lambda starts with a clean slate. It sees nothing from outside until you capture it. "
            "Write the name in the square brackets to copy it. Add an ampersand to use the original variable, and to change it.",
        hint="Hint: the lambda tests the remainder after dividing by two.",
    ),
    79: dict(
        concept="Ranges in C plus plus twenty make code read like a recipe. Take the numbers, keep the even ones, and square them.\n"
                "Views are lazy. They do no work until you ask for an item. They also copy nothing, so they use almost no memory.",
        A="[HL 10] The pipe sends the vector into a filter. The filter keeps only the even numbers. "
          "[HL 11] The next pipe sends the result into a transform, which squares each item. "
          "[HL 12] The loop asks for the items, and now the work happens. The output is four, sixteen, thirty-six, sixty-four. "
          "[HL 16] The ranges sort takes the whole vector, and the greater function sorts in the other direction.",
        ill="Notice the stations on the conveyor belt. Each item goes through all the stations before the next item starts. "
            "No station keeps a full copy of the data.",
        B="[HL 6] Iota makes numbers that start at one and never end. "
          "It is safe, because the numbers are made only when asked for. "
          "[HL 6] Take stops after five items. The loop prints one to five.",
        term="Notice that an endless range is fine here. The take view cuts it after five items.",
        bug="Ranges need the right header and a modern compiler setting. If the compiler says that views is not a member of std, check two things. "
            "Is the ranges header there, and did you pass the flag for C plus plus twenty?",
        hint="Hint: the filter lambda tests that the remainder after dividing by two equals one.",
    ),
    80: dict(
        concept="Copying a big vector is slow, because every item is copied. If the old vector is about to die anyway, a copy is a waste.\n"
                "A move steals the inside of the old object. It takes only a few steps, whatever the size. "
                "The old object stays valid, but you should not rely on its value.",
        A="[HL 7] The vector a holds three items. "
          "[HL 8] The move function does not move anything by itself. It marks a as a thing that may be emptied. "
          "The new vector b then takes the inside of a. "
          "[HL 9] The size of b is three. [HL 10] The vector a is now empty.",
        ill="Notice that no new data was made. The new vector only took the pointer to the old data. "
            "The old vector got an empty pointer. It is like handing over the keys of a house.",
        B="[HL 11] The move constructor takes an rvalue reference, written with two ampersands. It steals the pointer. "
          "[HL 12] The old object gets a null pointer, so its destructor does no harm. "
          "[HL 16] The copy is switched off, so a Buffer can only be moved. "
          "[HL 28] The new Buffer has size one hundred, and the old one has size zero.",
        term="Notice the output. Made, moved, and then one hundred, zero.",
        bug="A unique pointer has one owner. If you could copy it, there would be two owners, and a double delete. "
            "So copying is not allowed. To give the object to another pointer, use move, and the old pointer becomes empty.",
        hint="Hint: the move function turns the string into something that the vector may take apart.",
    ),
    81: dict(
        concept="Old code used magic values. A function returned minus one for no answer, or a null pointer. The caller had to remember the rule, and many forgot.\n"
                "Optional puts the rule in the type. The compiler reminds you to check before you read.",
        A="[HL 6] The function returns an optional int. It may hold an int, or it may hold nothing. "
          "[HL 9] When it finds the value, it returns the index. "
          "[HL 12] If the loop ends with no match, it returns nullopt. "
          "[HL 18] An optional works as a test. It is true when it holds a value. [HL 22] The value or function gives a fallback.",
        ill="Notice the two states. An optional is either full or empty. "
            "If you read an empty one with the star, you get a bug. So test it first, as you test a pointer.",
        B="[HL 7] The variant holds an int or a string, and now it holds an int. "
          "[HL 8] The get call with a type reads that type. "
          "[HL 9] Now the variant holds a string. "
          "[HL 11] The visit function runs a lambda on whatever the variant holds. It works for both types.",
        term="Notice that the visit call prints the string hello. The same lambda would print an int as well.",
        bug="A variant holds one type at a time. If you ask for the wrong one, get throws an exception. "
            "Test with holds alternative first. Or use visit, which handles each type for you.",
        hint="Hint: return nullopt for a negative input, and a real number for any other input.",
    ),
    82: dict(
        concept="Why use exceptions? Some errors cannot be handled where they happen. A function that divides by zero does not know what the caller wants to do.\n"
                "With an exception, the function reports the problem, and the caller decides. "
                "The code in between does not need an if for each error.",
        A="[HL 6] The function checks for a zero divisor. "
          "[HL 7] Throw makes an error object and sends it up. The function ends at once. "
          "[HL 13] The risky code sits in a try block. [HL 14] The first call works, and it prints four. "
          "[HL 15] The second call throws, so the rest of the block is skipped. "
          "[HL 17] The catch block runs, and it prints the message. [HL 20] After the block, the program carries on.",
        ill="Notice the path of the ball. It leaves the function, and it goes up through each caller. "
            "At each level, the computer asks, is there a catch for this type? If yes, it stops there.",
        B="[HL 8] Stoi cannot read the text abc as a number, so it throws. "
          "[HL 10] The first catch matches the invalid argument type. "
          "[HL 12] The second catch is a safety net for any other standard error. "
          "Put the most specific catch first, and the general catch last.",
        term="Notice that only one catch block runs. The first match wins.",
        bug="An error that nobody handles reaches the top of the program, and the program ends. "
            "On some systems, you see a message like terminate called. Handle the error where you can recover, and wrap main as a last safety net.",
        hint="Hint: the at function throws out of range, so put it inside a try block.",
    ),
    83: dict(
        concept="Variables vanish when the program ends. Files stay. If you want to keep data, you save it in a file.\n"
                "File streams use the same arrows as cout and cin. If you know how to print and read, you already know how to use files.",
        A="[HL 8] This line makes an output stream and opens the file. If the file does not exist, the stream creates it. "
          "[HL 9] The arrows send the text into the file, and the backslash n ends the line. "
          "[HL 11] Close writes the last data to the disk. "
          "[HL 13] An input stream opens the same file. [HL 15] Getline reads one full line at a time, until the file ends.",
        ill="Notice the three steps. Open the stream, use it, and close it. "
            "The stream is like a pipe between your program and the file on the disk.",
        B="[HL 9] All the data sits on one line, with spaces between the items. "
          "[HL 16] The arrows read a word and a number each time. The loop stops when the reading fails. "
          "[HL 17] Each mark is added to the total. Ninety-one plus seventy-eight plus eighty-five makes two hundred and fifty-four.",
        term="Check by hand. Ninety-one plus seventy-eight is one hundred sixty-nine. Add eighty-five, and the total is two hundred fifty-four.",
        bug="A file stream that fails to open does not shout. It stays in a failed state, and every read gives nothing. "
            "So test the stream right after you open it. Check the file name, and the folder where the program runs.",
        hint="Hint: read the file with getline, and add one to a counter for each line.",
    ),
    84: dict(
        concept="In a big program, many people write code at the same time. Two of them may choose the same name for different things. Namespaces prevent a clash.\n"
                "The standard library puts everything in the std namespace for this reason. Your own code can do the same.",
        A="[HL 4] The namespace circle opens a drawer. [HL 6] The area function inside takes a radius. "
          "[HL 11] The namespace square is another drawer. [HL 12] It has its own area function, with the same name. "
          "[HL 18] The double colon opens the circle drawer, and the answer is twelve point five six. "
          "[HL 19] The same name in the square drawer gives nine.",
        ill="Notice that the two area functions do not clash. Each lives in its own drawer, and the label tells you which one you mean.",
        B="[HL 4] A namespace can hold another namespace. "
          "[HL 10] An alias gives a short name to a long path. "
          "[HL 13] Now we write sr instead of the whole path. The circumference for radius one is six point two eight.",
        term="Notice that the alias saves typing, and the meaning stays clear.",
        bug="The line using namespace opens every drawer at once, and then the names can clash again. "
            "In small programs this is fine. In big programs, write the namespace name in front of each call.",
        hint="Hint: put the function in the namespace, and call it with the namespace name and two colons.",
    ),
}
