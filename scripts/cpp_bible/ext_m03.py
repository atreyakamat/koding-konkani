"""Longer narration for module 3 (EP 21-30). Each text is added to the end of the matching text in m03.py.

Keys: intro, concept, A, ill, B, term, bug, hint (hint goes into the challenge scene).
Rules: docs/cpp-bible/STE.md. Cues [HL n] point at lines of the code file for that scene.
"""
EXT = {
    21: dict(
        concept="Why do programmers write functions? A long program becomes hard to read. Functions cut it into small parts, and each part has a name. "
                "When you need the same job again, you call the name, and you do not copy the code.\n"
                "Every program you have written has one function already. It is main. Now you learn to write your own.",
        A="[HL 4] Read the first line as a label. It says the type that comes back, the name, and the inputs. "
          "[HL 5] Everything between the braces is the body, and it runs only when someone calls the function. "
          "[HL 9] A call is the name with round brackets. Do not forget the brackets, or the compiler reads the name as a plain word. "
          "If you change the message in the body, both calls change together.",
        ill="Notice the jump. The program leaves main, runs the body, and comes back to the exact place where it left. "
            "It is like a bookmark. The computer remembers where to return, so you do not have to.",
        B="[HL 4] A declaration is only a promise. It names the function, the inputs and the type, but it has no body. "
          "Large programs keep declarations at the top, or in a header file. "
          "[HL 11] The body can sit anywhere below, in the same file or in another file.",
        term="Notice that the declaration prints nothing. Only the call in main makes the output.",
        bug="The compiler reads the file once, from the top. It has no memory of the lines below. "
            "So any name must appear before it is used. You have two easy fixes. Move the function up, or write a short declaration above main.",
        hint="Hint: write the function above main, so you need no declaration.",
    ),
    22: dict(
        concept="Parameters and arguments are easy to mix up. Parameters are the names in the function line. Arguments are the real values in the call.\n"
                "A function can return only one value. If you need more, you will learn other tools later. "
                "A good function does one job, and its name says what the job is.",
        A="[HL 4] The two parameters are like empty boxes. They get their values when the function is called. "
          "[HL 5] The return statement ends the function at once. Any line after it does not run. "
          "[HL 9] The order of the arguments matters. The first argument goes to the first parameter. "
          "[HL 10] The variable total holds a copy of the answer, and we print it.",
        ill="Notice that the function never knows where its numbers come from. It only sees a and b. "
            "That is a big strength. You can call the same function with numbers from the keyboard, from a file or from a loop.",
        B="[HL 5] This is an early return. The function stops as soon as it knows the answer. "
          "[HL 8] If the first test fails, the code reaches this line. Every path through the function must end with a return. "
          "[HL 12] Now we can use the call right inside the cout line.",
        term="Check the two numbers by eye. The bigger one of seven and twelve is twelve, and of thirty and five is thirty.",
        bug="The compiler cannot always tell what you meant, but it can see a missing return. "
            "A function that says int must give back an int on every path. Read the warning, and look at the last line of the function.",
        hint="Hint: use an if inside the function, and return one of the two numbers.",
    ),
    23: dict(
        concept="Why does C plus plus copy the value? It is safe. The function cannot spoil your variable by accident.\n"
                "But copies cost time for big values, and they cannot send results back through the parameter. "
                "So you must know when to use a copy, and when to use another tool.",
        A="[HL 4] The parameter n is a new box. It is a different box from number, even though it holds the same value. "
          "[HL 5] This line changes only the new box. "
          "[HL 6] So inside the function, we see twenty. "
          "[HL 12] But back in main, the original box still holds ten. The change did not travel back.",
        ill="Notice that the two boxes have different addresses. When the function ends, its box is thrown away, and the doubled value is gone. "
            "If you want to keep it, return it.",
        B="[HL 6] The function swaps a and b, but they are copies. "
          "When the function ends, the copies vanish, and nothing in main has changed. "
          "[HL 13] The output proves it. The order is still one, then two.",
        term="This result is surprising at first, but it is the normal rule of copies.",
        bug="This bug is common, so do not feel bad if you make it. The fix has two parts. "
            "The function returns the new price, and the caller stores that value. "
            "Write price equals add tax of price, and the original variable changes.",
        hint="Hint: the function returns the new value, and main stores it back in the same variable.",
    ),
    24: dict(
        concept="With a reference, the function and the caller share one box. There is no copy at all. "
                "You tie a reference to a variable when you make it. It can never point to a different variable later.\n"
                "Use a reference when a function must change the caller variable. You can also use it to return more than one result.",
        A="[HL 4] The ampersand is part of the type, not of the name. Read the type as int reference. "
          "[HL 5] When the function writes to n, it writes into the box of number. "
          "[HL 10] The call looks the same as before. You write number, with no ampersand. "
          "The only change is in the function line, and the compiler does the rest.",
        ill="Notice how the picture differs from the last episode. Last time, we had two boxes. Now we have one box with two labels. "
            "Any change through one label shows through the other.",
        B="[HL 4] Because both parameters are references, a and b are other names for x and y. "
          "[HL 7] Every line works on the real values. "
          "A swap is a classic use of references. It needs to change two caller variables at once.",
        term="Compare this with the last episode. The code is nearly the same, but the result is different.",
        bug="A reference needs a real box. A plain number is only a value, and it has no place in memory. "
            "So the compiler refuses. Put the five in a variable first, and pass the variable.",
        hint="Hint: write an ampersand after int in both parameters.",
    ),
    25: dict(
        concept="Here is the rule of thumb. For small types like int and char, pass by value. For big types like string, pass by const reference. "
                "If the function must change the value, use a plain reference.\n"
                "This rule is used in nearly all C plus plus code, so learn it well.",
        A="[HL 5] Read the type from right to left. Text is a reference, to a string, that is const. "
          "[HL 6] If you try to write to text here, the compiler stops you. "
          "[HL 11] The call looks normal. Main does not need to know that the function is careful. "
          "This protects your data, and it keeps the program fast.",
        ill="Notice the three cases in the table. A copy is safe, but slow for big values. A plain reference is fast, but it can change the original. "
            "A const reference has both good points, because it is fast and safe.",
        B="[HL 6] The size function gives the number of letters. We only read the strings, so const is right. "
          "[HL 13] A quoted text is not a string yet. The compiler makes a short-lived string for the call. "
          "A const reference may hold such a short-lived value, but a plain reference may not.",
        term="Notice the word false. Panjim and Mapusa have the same size, so one is not longer than the other.",
        bug="This error is useful. It says that you tried to change a value that you promised only to read. "
            "You have two choices. If the function should change the value, remove const and use a plain reference. If not, delete the line that changes it.",
        hint="Hint: a const reference to a string is the right choice here.",
    ),
    26: dict(
        concept="Defaults make a function easy to use. The common case needs fewer arguments, and the special case can still use more.\n"
                "A default value goes in the function line, and only the last parameters can have defaults. "
                "Overloading makes the code read well, because one name fits one idea, like area.",
        A="[HL 4] The equals sign here is not an assignment. It sets the default for a missing argument. "
          "[HL 7] The loop multiplies the result by base again and again. With exp equal to two, it runs two times. "
          "[HL 13] Five times five is twenty-five. "
          "[HL 14] Two times itself ten times gives one thousand and twenty-four.",
        ill="Notice how the compiler decides. First it counts the arguments. Then it compares the types. "
            "If one function fits best, the compiler picks it. If two fit equally well, you get an error.",
        B="[HL 4] A function name can mean three different functions. "
          "The compiler picks the right one from the number and the type of the arguments. "
          "Note that the return type alone can never tell two functions apart.",
        term="Check the middle line by hand. Four times six is twenty-four.",
        bug="An int can become a long, and it can also become a double. Both changes cost the same, so the compiler cannot choose. "
            "Make the call exact. Write the number with the letter L for a long, or add a function that takes an int.",
        hint="Hint: both functions have the same name, but one takes an int and the other takes a string.",
    ),
    27: dict(
        concept="Think of scope as the walls of a room. A name made inside a pair of braces can be used only inside those braces.\n"
                "Global variables are visible everywhere, and that is a danger. Any function can change them, so bugs are hard to trace. "
                "Prefer local variables, and pass values with parameters.",
        A="[HL 4] This variable is outside every function. All functions in the file can use it. "
          "[HL 7] This variable is born each time the function starts, and it dies when the function ends. "
          "[HL 8] Because visits is global, the count survives between calls. "
          "[HL 9] Compare the two numbers on the output. One grows, and the other stays the same.",
        ill="Notice where each variable lives. The stack is busy and changes with every call. The static region stays the same for the whole run. "
            "Your choice of scope decides where the data goes.",
        B="[HL 5] The word static does not change who can see the name. Only the function can see ticket. "
          "It changes how long the variable lives. "
          "[HL 7] Because the value stays, the next call continues where the last call stopped.",
        term="Think of a ticket machine at a station. Each press gives the next number.",
        bug="A name is valid only between its braces. Here, total lives inside the loop, and the loop ends before the print. "
            "Move the line that makes total above the loop. Then the variable lives through the whole function.",
        hint="Hint: a static local variable keeps its value, so add one to it each time.",
    ),
    28: dict(
        concept="Recursion looks like magic, but it follows two simple rules. First, solve the smallest problem directly. That is the base case. "
                "Second, solve a bigger problem by using the answer of a smaller one.\n"
                "If you forget the base case, the calls never stop. The stack fills up, and the program crashes.",
        A="[HL 4] The factorial of five means five times four times three times two times one. "
          "[HL 5] Check the base case first. It stops the chain of calls. "
          "[HL 8] The function calls itself with a smaller number. The number goes down by one each time. "
          "Each call waits for the answer of the next call, and then multiplies.",
        ill="Notice that the frames pile up on the way down, and they leave on the way back. "
            "The answers are built on the way back. The deepest call answers first, and that answer grows with each return.",
        B="[HL 5] Write the base case first, always. It is the safe ending. "
          "[HL 8] Sum to four is four plus three plus two plus one, and then the sum to zero gives zero. "
          "A loop can do this job too, and it uses less memory. But recursion fits trees and puzzles well.",
        term="Check by hand. Four plus three plus two plus one is ten.",
        bug="The base case is the answer for the smallest problem. For a product, doing nothing means multiplying by one. "
            "For a sum, doing nothing means adding zero. Choose the base value that does not change the result.",
        hint="Hint: print the number first, and then call the function with a number that is one smaller.",
    ),
    29: dict(
        concept="Why do we need lambdas? Sometimes you need a tiny function for a few lines only. Writing a full function with a name is too much.\n"
                "Later, you will pass lambdas to library tools, such as sort. There they are a great help. "
                "For now, learn the four parts and how to call one.",
        A="[HL 5] The square brackets come first. They are the capture list, and here it is empty. "
          "[HL 6] The body is ordinary code. Return gives back the square of x. "
          "[HL 7] A semicolon follows the closing brace, because the whole lambda is one statement that makes a variable. "
          "[HL 9] You can call the lambda as many times as you like.",
        ill="Notice the order of the parts. Brackets, then round brackets, then braces. If you keep this order in mind, you can read any lambda.",
        B="[HL 6] A lambda by default keeps a copy of the captured value. "
          "The copy is made when the lambda is made. If offset changes later, the lambda still holds the old value. "
          "[HL 7] Inside the body, you use the name like any other variable.",
        term="Five plus one hundred is one hundred and five, as expected.",
        bug="A lambda is like a sealed room. It sees only what you let in through the square brackets. "
            "Name the variable in the list, and the error goes away. If you capture everything with an equals sign, the lambda takes copies of all.",
        hint="Hint: the capture list stays empty, because the lambda needs only its parameter.",
    ),
    30: dict(
        concept="A calculator is a good first project, because it uses most of what you learned. It uses input, decisions, functions and output.\n"
                "Plan first, and then write. Decide the inputs, the steps and the output. Then write one function for each step, and test them one at a time.",
        A="[HL 4] The function has three inputs, two numbers and one sign. It gives back one number. "
          "[HL 5] A switch is the right tool for one char with many choices. "
          "[HL 9] The question mark line is a short if. If b is not zero, it divides. If not, it returns zero. We never divide by zero. "
          "[HL 10] The default case catches signs that we do not know.",
        ill="Notice the clear steps. Each step has one owner. Cin reads, calc decides, and cout shows. "
            "If the output is wrong, you know where to look first. That is the strength of small functions.",
        B="[HL 4] Each function has one clear job and one clear name. "
          "A reader sees the name and knows what it does, without reading the body. "
          "[HL 5] The formula for Fahrenheit multiplies by nine, divides by five, and adds thirty-two.",
        term="Check the second number. Thirty times nine is two hundred seventy, divided by five is fifty-four, plus thirty-two is eighty-six.",
        bug="Think about all the paths. A switch has many branches, and each one must return a value. "
            "If one path has no return, the function ends with no value, and the answer is garbage. Add a default case, and return something safe.",
        hint="Hint: the pow function lives in the cmath header, so include it at the top.",
    ),
}
