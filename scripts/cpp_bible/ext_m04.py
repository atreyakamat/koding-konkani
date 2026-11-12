"""Longer narration for module 4 (EP 31-40). Each text is added to the end of the matching text in m04.py.

Keys: intro, concept, A, ill, B, term, bug, hint (hint goes into the challenge scene).
Rules: docs/cpp-bible/STE.md. Cues [HL n] point at lines of the code file for that scene.
"""
EXT = {
    31: dict(
        concept="Why use an array? Imagine five marks in five separate variables. You would write five names, and a loop could not reach them. "
                "With an array, one name holds all five, and a loop can visit each one.\n"
                "Arrays are everywhere. A list of prices, the pixels of a photo and the scores of a game all live in arrays.",
        A="[HL 5] Read the line in parts. The type is int, and the name is marks. The number five in square brackets is the size. "
          "The curly braces hold the starting values, in order. "
          "[HL 6] The first item has index zero, so marks of zero is seventy-two. "
          "[HL 7] The last item has index four, one less than the size. "
          "[HL 8] You can change an item with an equals sign, like a plain variable.",
        ill="Notice that the items sit side by side. Each int takes four bytes, so each address is four more than the one before. "
            "That is why the computer finds any item at once. It starts at the first address and adds the index times four.",
        B="[HL 6] The sum starts at zero before the loop. "
          "[HL 7] The loop counts from zero up to four. The test says less than five, so the index five is never used. "
          "[HL 8] Each round adds one mark to the sum. This is the standard way to walk through an array.",
        term="Check the sum by hand. Seventy-two plus eighty-five is one hundred fifty-seven. Add sixty-four, ninety and fifty-eight to reach three hundred sixty-nine.",
        bug="The size of an array is fixed, and the compiler counts your starting values. "
            "If you give more values than boxes, the compiler stops. If you give fewer, the rest become zero. "
            "You can also leave out the size, and the compiler counts for you.",
        hint="Hint: the last index is the size minus one, so use index four for five items.",
    ),
    32: dict(
        concept="There are two ways to walk through an array. Use the index loop when you need the position, or when you must change items. "
                "Use the range-based loop when you only read the values. The second way is shorter and safer.\n"
                "Finding the biggest item is a classic task. The same pattern also finds the smallest, the first match, and the total.",
        A="[HL 6] We start with the first item as the best so far. This is a safe start, because the array has at least one item. "
          "[HL 7] The loop visits every mark in turn. "
          "[HL 8] If the new mark beats the best, we remember it. [HL 9] The best box gets the new value. "
          "At the end, best holds the largest mark, which is ninety.",
        ill="Notice how best changes during the loop. It starts at seventy-two, then it grows to eighty-five, and then to ninety. "
            "It never goes down. Each step keeps the best value seen so far.",
        B="[HL 6] To go backwards, start at the last index and count down. "
          "The test says i is at least zero, so index zero is still included. "
          "[HL 7] Each round prints one mark with a space after it. The output is the array in reverse order.",
        term="Notice that the first mark prints last. The loop visits the items in the opposite order.",
        bug="Think about the data, not only the code. If all values are below zero, no value beats a best of zero. "
            "So best never changes, and the answer is wrong. Start with the first real item, and the loop works for any data.",
        hint="Hint: start the smallest at the first item, and change the comparison to less than.",
    ),
    33: dict(
        concept="Two-dimensional arrays are for tables. A school timetable, a chess board and a game map all have rows and columns.\n"
                "Think of the first index as the row, and the second index as the seat in that row. "
                "Both indexes start at zero, so the first seat of the first row is grid zero zero.",
        A="[HL 5] The first number in the type is the rows, and the second is the columns. "
          "The inner braces show each row. The first row holds one, two and three. "
          "[HL 6] Row zero, column two is the last item of the first row. That is three. "
          "[HL 7] Row one, column zero is the first item of the second row. That is four.",
        ill="Notice the memory. The computer stores the second row right after the first row, as one long line. "
            "The two indexes are only a way to find the right place in that line.",
        B="[HL 6] The outer loop picks a row. "
          "[HL 7] The sum starts at zero for every row. If we put it outside the loop, the rows would add up together. "
          "[HL 8] The inner loop walks along the columns. "
          "[HL 11] After the inner loop, we print the row sum.",
        term="Check by hand. One plus two plus three is six. Four plus five plus six is fifteen.",
        bug="To find a seat, the compiler must know how long each row is. It can guess the number of rows from your list, but not the columns. "
            "So always write the column size. You may leave out only the first size.",
        hint="Hint: the diagonal uses the same number for the row and the column.",
    ),
    34: dict(
        concept="A plain array is fast, but it is careless. It does not know its own size, and it does not check the index. "
                "The std array fixes both problems and costs nothing extra.\n"
                "The size is part of the type. So array of int, three, and array of int, four, are different types.",
        A="[HL 6] The two parts inside the angle brackets are the item type and the size. "
          "[HL 7] The size function tells us the size. No need to count by hand. "
          "[HL 8] The at function checks the index, and it stops the program with an error if the index is too big. "
          "[HL 9] The fill function sets every item to one value, here zero.",
        ill="Notice the difference in the table. Square brackets are fast but trust you. The at function costs a tiny check, and it protects you. "
            "While you learn, use at, and you will find your mistakes sooner.",
        B="[HL 7] A std array can be copied with a plain equals sign. A plain array cannot. "
          "The copy has its own items, so a change to b leaves a alone. "
          "[HL 9] You can also compare two arrays with the double equals sign. Here, they differ, so the answer is false.",
        term="Notice that a keeps its first item. The copy changed, but the original did not.",
        bug="Indexes run from zero to size minus one. The index nine is far outside a row of three. "
            "A plain array would read some random memory and say nothing. The at function stops the program, and the message tells you what went wrong.",
        hint="Hint: the fill function sets every item to one value, so call it once.",
    ),
    35: dict(
        concept="Vector is the most used container in C plus plus. When you do not know how many items you need, use a vector.\n"
                "Inside, a vector keeps a plain array. When the array is full, it makes a bigger one, copies the items, and drops the old one. "
                "You never see this work, but it is why adding at the end is fast.",
        A="[HL 6] The type in angle brackets says what the vector holds. A new vector starts empty. "
          "[HL 7] Push back adds one item at the end. [HL 8] The next item goes after it. [HL 9] And the next. "
          "[HL 10] The size is now three. "
          "[HL 11] You read an item with square brackets, as with an array. Index one is twenty.",
        ill="Notice the difference from an array. The array has a fixed size. The vector has a size and a capacity. "
            "The capacity is how many items fit before the next growth. It is usually bigger than the size.",
        B="[HL 6] You can start a vector with a list of values. "
          "[HL 7] Push back adds sixteen at the end. "
          "[HL 12] The back function gives the last item. [HL 13] Pop back removes it. [HL 14] The size is then three again.",
        term="Notice the numbers. The loop prints four, eight, fifteen and sixteen. Then the back call prints sixteen. After the pop, the size is three.",
        bug="The vector type lives in its own header. Without the include line, the compiler does not know the word vector. "
            "The error says that vector is not declared. Add the include line at the top, and the error goes away.",
        hint="Hint: add the numbers to the sum in a loop, after you fill the vector.",
    ),
    36: dict(
        concept="Iterators are like arrows that point at an item. The begin function points at the first item, and the end function points after the last item. "
                "You can add a number to an iterator to move it along.\n"
                "Many library tools work with a pair of iterators, the start and the end. Sort and find are two of them.",
        A="[HL 6] The vector holds ten, twenty and thirty. "
          "[HL 7] Begin plus one points at the second item. Insert puts ninety-nine in front of it. "
          "The vector is now ten, ninety-nine, twenty and thirty. "
          "[HL 8] Erase removes the first item. Now we have ninety-nine, twenty and thirty.",
        ill="Notice that insert and erase move all the items after the spot. For a big vector, this takes time. "
            "So add and remove at the end when you can.",
        B="[HL 8] Sort needs two iterators, the start and the end. After the call, the numbers are in order. "
          "[HL 13] Find gives back an iterator. If it finds the value, it points at that item. "
          "[HL 14] Subtract begin to get the index. The value thirty sits at index two.",
        term="The sorted vector is ten, twenty, thirty, forty. Thirty has index two.",
        bug="An index is a plain number, but erase needs an iterator. The compiler cannot turn one into the other. "
            "So write begin plus the index. This makes a point in the vector that erase can use.",
        hint="Hint: after sort, the smallest item is first, and the biggest is last.",
    ),
    37: dict(
        concept="Text is everywhere in programs. Names, messages and file paths are all strings. A good programmer knows the common tools.\n"
                "Most tools use an index and a count. Replace and erase both say, start here, and take this many letters.",
        A="[HL 6] The string is Goa is sunny. The word sunny starts at index seven. "
          "[HL 7] Replace takes the start, the length, and the new text. Five letters from index seven become warm. "
          "[HL 9] Erase takes a start and a length too. We remove three letters from index three. "
          "The result is shorter, and the space moves.",
        ill="Notice that each tool changes the string itself. It does not make a new one. "
            "If you need the old text later, make a copy before you edit.",
        B="[HL 7] Stoi turns the text forty-two into the number forty-two. Now we can use it in maths. "
          "[HL 8] Forty-two plus one is forty-three. "
          "[HL 9] To string goes the other way. It turns a number into text, so we can join it with other text.",
        term="Notice that the answer is a string, so we can add more text to it.",
        bug="Text like abc has no number in it. Stoi cannot guess one, so it throws an exception. "
            "A try block runs the risky line, and a catch block handles the problem. We study this in detail later in the course.",
        hint="Hint: call stoi on each text, add the two ints, and give the sum to to string.",
    ),
    38: dict(
        concept="C strings come from the C language, and C plus plus keeps them for old code. You will meet them in many libraries.\n"
                "The null character is the key. Every function in the cstring header stops when it finds it. "
                "If you forget it, the functions run on into other memory.",
        A="[HL 6] The compiler counts the letters, and it adds the null character for us. "
          "[HL 7] Strlen counts the letters until it finds the null. It gives three. "
          "[HL 8] Sizeof gives the size of the whole array. That is four, because the null takes one place. "
          "[HL 9] Cout also stops at the null character.",
        ill="Notice the picture. The word Goa has three letters, and the array has four boxes. The last box holds the null. "
            "That one extra box is the most common reason for a mistake with sizes.",
        B="[HL 6] Both arrays hold the same word, but they sit at different places in memory. "
          "[HL 8] Strcmp compares the letters. It gives zero when the two strings are equal. "
          "That is why we test the answer against zero.",
        term="Notice that the answer prints as one, because true prints as one.",
        bug="An array name stands for an address. Two arrays have two addresses, so a test with equals is always false. "
            "That is rarely what you want. Use strcmp for C strings, or use std string, where the double equals sign compares the letters.",
        hint="Hint: the loop runs while the char is not the null character, which is backslash zero.",
    ),
    39: dict(
        concept="Searching is one of the oldest jobs in computing. Every time you look for a contact in your phone, a search runs.\n"
                "Linear search is simple and works on any list. Binary search is much faster, but the list must be sorted first. "
                "For a million items, binary search needs only about twenty steps.",
        A="[HL 5] The loop visits each index in turn. "
          "[HL 6] If the item equals the target, we return the index at once. "
          "[HL 10] If the loop ends with no match, we return minus one. Minus one is a good signal, because no index is negative. "
          "[HL 15] The first call finds the number three at index three. [HL 16] The second call gives minus one.",
        ill="Notice how the work grows. For ten items, linear search may take ten steps. For a million, it may take a million. "
            "Binary search halves the range each step, so it grows slowly.",
        B="[HL 5] Low and high mark the part of the array we still search. "
          "[HL 7] The middle is the average of the two ends. "
          "[HL 10] If the middle item is too small, the target must be on the right. So we move low up. "
          "[HL 13] If the middle item is too big, we move high down. Each step throws away half of the items.",
        term="Check by hand. The middle of seven items is index three, which is seven. Five is smaller, so we go left, and we find five at index two.",
        bug="Binary search trusts that the data is sorted. If it is not, the program may throw away the half that holds the target. "
            "The program does not warn you. So sort the data first, or use linear search.",
        hint="Hint: return the index when the item matches, and return minus one when the loop ends.",
    ),
    40: dict(
        concept="Why learn sorting by hand? The library has a sort tool. But sorting teaches you loops, swaps and how to count steps.\n"
                "Both methods in this episode are simple. They are slow for big data. For real work, use the library sort. "
                "For learning, these two are perfect.",
        A="[HL 7] Each pass of the outer loop puts the biggest remaining number at its final place. "
          "[HL 8] The inner loop compares neighbours. It stops earlier on every pass, because the end is already sorted. "
          "[HL 9] If the left one is bigger, we swap. "
          "[HL 10] The swap needs a helper box, because two lines of plain assignment lose one value.",
        ill="Notice how the big numbers bubble up to the right. After the first pass, eight is at the end. After the second pass, five is next to it. "
            "That is why the method has its name.",
        B="[HL 7] The outer loop picks the place that we fill next. "
          "[HL 8] Variable m remembers the index of the smallest item seen so far. "
          "[HL 9] The inner loop looks at the rest of the array. [HL 11] If it finds a smaller item, it remembers the index. "
          "[HL 14] After the search, one swap puts the smallest item in place.",
        term="Both programs print the same answer, one, three, four, five, eight. The paths differ, but the result is the same.",
        bug="Follow the lines by hand. If you copy a j plus one into a j first, the old value of a j is gone. "
            "Then both boxes hold the same number. Save the old value in a helper box first, then copy, then restore.",
        hint="Hint: add one to the counter inside the if, right next to the swap.",
    ),
}
