"""Longer narration for module 8 (EP 69-76). Each text is added to the end of the matching text in m08.py.

Keys: intro, concept, A, ill, B, term, bug, hint (hint goes into the challenge scene).
Rules: docs/cpp-bible/STE.md. Cues [HL n] point at lines of the code file for that scene.
"""
EXT = {
    69: dict(
        concept="Imagine that you need a biggest function for ints, for doubles and for strings. Without templates, you copy the code three times. "
                "With a template, you write it once.\n"
                "The template itself makes no code. Only when you call it, the compiler writes a real function. "
                "If you never call it, no code appears.",
        A="[HL 4] The word template and the angle brackets start the recipe. T is a placeholder for a type. "
          "[HL 5] T appears as the return type and as both parameter types. "
          "[HL 6] The question mark line picks the bigger of the two. "
          "[HL 10] With ints, the compiler makes a version where T is int. [HL 11] With doubles, it makes another version.",
        ill="Notice that two real functions exist after the build. One works with ints, and one works with doubles. "
            "The compiler wrote both from the same recipe. You write less, and the result is as fast.",
        B="[HL 10] The angle brackets after the name tell the compiler what T is. "
          "The int three is then converted to a double. "
          "[HL 11] With strings, the greater one is the one that comes later in the alphabet. Pear comes after apple.",
        term="Notice that the first answer is four point five, and the second is pear.",
        bug="The compiler needs one clear answer for T. When one argument is an int and the other is a double, it has two answers, and it gives up. "
            "You have two fixes. Write the type in angle brackets, or make both arguments the same type.",
        hint="Hint: copy the biggest template, and change the comparison sign to less than.",
    ),
    70: dict(
        concept="A class template works like a function template, but for a whole class. You write the class once, and it holds any type.\n"
                "This is how vector, map and unique pointer are written. You are about to build a small one yourself.",
        A="[HL 5] The template line comes before the class. "
          "[HL 7] The member value has the type T. "
          "[HL 10] The constructor takes a T. [HL 11] The getter returns a T. "
          "[HL 15] Box of int holds a seven. [HL 16] Box of string holds a word. The same class works for both.",
        ill="Notice that Box of int and Box of string are two different types. They share a recipe, but they are not the same class. "
            "You cannot put one into the other.",
        B="[HL 7] A vector inside does the storage. "
          "[HL 10] Push adds an item at the end. "
          "[HL 11] Pop takes the last item out, and returns it. "
          "[HL 25] The items come back in reverse order. This is the stack rule, last in, first out.",
        term="Notice that the output is three, two, one. The last item pushed is the first item popped.",
        bug="For a function, the compiler learns T from the arguments. For a class with no constructor argument, it has nothing to learn from. "
            "Write the type in angle brackets, and the object can be built. Since C plus plus seventeen, a constructor argument is often enough.",
        hint="Hint: the member function compares the two members, and returns the bigger one as a T.",
    ),
    71: dict(
        concept="Sometimes a function needs to return two things. A pair is the quick answer. You do not need to define a new struct.\n"
                "For more than two things, or for things that need clear names, a struct is better. "
                "A tuple is handy for short, local code.",
        A="[HL 5] The function returns a pair of ints, the smaller one first. "
          "[HL 6] Make pair builds a pair from two values. "
          "[HL 11] The members first and second give the parts. The output is four, then nine. "
          "[HL 12] The square brackets unpack the pair into two new names. This is a structured binding.",
        ill="Notice how the names help. The pair gives only first and second, which say little. "
            "The structured binding gives you good names for the same two values, and the code reads better.",
        B="[HL 7] The tuple holds a string, an int and a bool. "
          "[HL 8] The function get with a number picks one part. The number must be known when you compile. "
          "[HL 9] A structured binding gives each part its own name. "
          "[HL 10] Now the output is easy to read.",
        term="Notice that the bool prints as true because of boolalpha.",
        bug="A pair has exactly two members, and the names are fixed. A third member does not exist. "
            "For more values, use a tuple. For values that need real names, such as name and marks, write a small struct.",
        hint="Hint: the quotient uses the divide sign, and the remainder uses the percent sign.",
    ),
    72: dict(
        concept="A map is a good tool for look-ups. Words and their meanings, names and marks, and product codes and prices all fit.\n"
                "The map keeps its keys in order, so printing the whole map gives a sorted list. "
                "Finding a key takes only a few steps, even for a large map.",
        A="[HL 7] The first type is the key, and the second type is the value. "
          "[HL 8] Square brackets create the key Asha, and they store the value. "
          "[HL 10] The same key is used again, so the old value is replaced. "
          "[HL 11] The answer is ninety-five. [HL 12] The map holds two keys, not three.",
        ill="Notice that a map is a collection of pairs. Each pair has a key and a value. "
            "The pairs stay sorted by key, so Asha comes before Ravi.",
        B="[HL 7] The braces start the map with three pairs. They are not in order. "
          "[HL 8] The loop shows the pairs in key order. Asha first, then Meera, then Ravi. "
          "[HL 11] The find function looks for a key, and it gives an iterator. "
          "[HL 12] If the iterator equals end, the key was not found.",
        term="Notice the order of the first three lines. The loop sorted them by name, not by the order that we wrote.",
        bug="Square brackets are friendly, but they can surprise you. If the key does not exist, the map adds it with a default value. "
            "A look-up then grows the map. To check without a change, use find or count.",
        hint="Hint: loop over the map, and remember the name with the biggest mark.",
    ),
    73: dict(
        concept="How does a hash table work? A function turns each key into a number. The number tells which slot to look in. "
                "So the computer goes straight to the slot, with no search.\n"
                "Two keys can land in the same slot, and the table handles that. Because the slots are scattered, the order of the keys looks random.",
        A="[HL 8] The map has strings as keys and ints as values. "
          "[HL 9] A string stream lets us read words from a text, as if from a keyboard. "
          "[HL 11] The loop reads one word at a time. "
          "[HL 12] Plus plus adds one to the count of that word. A new word starts at zero, so it becomes one. "
          "[HL 14] The word sun appears three times.",
        ill="Notice that the counting needed no if statement. The square brackets make a new key with zero, and the plus plus does the rest. "
            "This is a short way to count words.",
        B="[HL 8] The count function answers one if the key exists, and zero if it does not. "
          "[HL 9] It never changes the map. "
          "[HL 10] The find function gives an iterator to the pair. "
          "[HL 11] The arrow with second reaches the value. The price of rice is forty-five.",
        term="Notice the three numbers. One for fish, zero for tea, and forty-five for rice.",
        bug="The at function is the strict version of square brackets. It does not create anything. "
            "If the key is missing, it throws an exception. Test with count first, or wrap the call in try and catch.",
        hint="Hint: loop over the letters of the word, and add one to the count of each letter.",
    ),
    74: dict(
        concept="A set answers one question well. Is this value in the collection? It also removes duplicates for free.\n"
                "Use a set when you need each value once. Use a vector when order and repeats matter.",
        A="[HL 7] The vector holds six numbers, with repeats. "
          "[HL 8] The set is built from the whole range. Each value is added once, and the repeats are dropped. "
          "[HL 9] The loop prints the values in sorted order. "
          "[HL 13] The set holds four values, because there are four different numbers.",
        ill="Notice how the repeats vanish. Five appeared twice and three appeared twice, and each now appears once. "
            "A sorted set is built as a tree, so the values stay in order.",
        B="[HL 7] The first insert adds four, and the second part of the answer is true. "
          "[HL 8] The second insert finds four already there. Nothing changes, and the second part is false. "
          "[HL 10] The count function tells if a value is inside. Four gives one. Seven gives zero.",
        term="Notice the output. The first line says true and false. The second says one and zero.",
        bug="A set cares about different values, not about the number of items. If you add one hundred copies of seven, the size is one. "
            "If you need the total count, keep the data in a vector, or in a map from value to count.",
        hint="Hint: build a set from the vector, and print the set with a range-based loop.",
    ),
    75: dict(
        concept="Stack and queue are adaptors. They wrap another container, usually a deque, and they show only a small set of functions.\n"
                "The small set is the point. A stack allows only the top. A queue allows only the two ends. "
                "The rules protect you from messy code.",
        A="[HL 7] Push one on the stack. [HL 8] Push two. [HL 9] Push three. "
          "[HL 10] Top shows the newest item, which is three. "
          "[HL 11] Pop removes it. [HL 12] Now the top is two. "
          "[HL 13] The size is two.",
        ill="Notice the picture of the plates. You can only take the plate on top. If you want the bottom plate, you must lift all the others first. "
            "That is the stack rule.",
        B="[HL 8] Asha joins the line first. [HL 9] Ravi joins second. [HL 10] Meera joins last. "
          "[HL 11] The front is Asha, who came first. "
          "[HL 12] Pop removes Asha. [HL 13] Now the front is Ravi, and the back is Meera.",
        term="Notice that the queue is fair. The first person to join is the first person to leave.",
        bug="Pop only removes. It does not return anything, so you cannot write x equals pop. "
            "Read the value with top or front first, and then pop. This design keeps the container safe if something goes wrong in the middle.",
        hint="Hint: push the letters in order, and then pop them all while you print the top.",
    ),
    76: dict(
        concept="Why do iterators matter? Algorithms like sort and find use them, so one algorithm works with many containers.\n"
                "An iterator is the glue between containers and algorithms. Learn its four main actions. Begin, end, plus plus, and star.",
        A="[HL 6] The vector holds three numbers. "
          "[HL 7] The loop starts at begin, and it stops when the iterator reaches end. "
          "[HL 8] The star reads the item. "
          "[HL 11] Rbegin and rend walk backwards. The second line prints thirty, twenty, ten.",
        ill="Notice the one past the end rule. End does not point to an item. It points right after the last item. "
            "That is why the loop test says not equal, and not less than.",
        B="[HL 7] A list has no square brackets, so you cannot say items of two. "
          "[HL 8] The next function moves a copy of the iterator two steps forward. "
          "[HL 9] The star reads the item, which is fifteen. "
          "[HL 10] The distance function counts the steps from begin, and gives two.",
        term="Notice that the same iterator code would work with a vector, a set or a list.",
        bug="Erase gives back an iterator to the next item. If you also move on with plus plus, you jump over one item. "
            "Write the loop so that you move on only when you did not erase. Then no item is skipped.",
        hint="Hint: use rbegin and rend, and add plus plus to the iterator as usual.",
    ),
}
