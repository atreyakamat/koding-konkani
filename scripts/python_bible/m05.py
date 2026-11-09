"""Module 5 — Functions, scope, lambdas, recursion (EP 41-50)."""

MODULE = {"id": 5, "name": "Functions, scope, lambdas, recursion", "range": "41–50", "colours": "Lilac + Tomato"}
EPISODES = []
NEXT_AFTER = ("Next: EP 51 · Reading files", "Module five is done! Next time: reading files from your computer.")

CALL = "A call arrow jumps from the call line up to the def, the body lines light up one by one, then the arrow returns to the line after the call"

EPISODES.append(dict(
    n=41, title="Defining functions", spoken="defining functions",
    yt="Python Functions: def and Calling", thumb="MAKE YOUR OWN TOOL",
    vis="Xecxec at a workbench building a tool labelled def greet()",
    goals=["define a function with def", "call a function by its name and brackets", "call one function from inside another"],
    tags=["python functions", "python def", "call a function python", "python beginner functions"],
    hash=["#functions", "#def"],
    analogy="a recipe card: you write the steps once, then cook the dish whenever you like by naming the card",
    c_title="Your own tools",
    c_pts=["def names a block of code", "The body is indented under the def line", "A call runs the body, as often as you like"],
    intro="Until now every program was one long script. Today we learn to name a block of code, and reuse it.",
    concept="A function is a named block of code. You write it once with def, a name, brackets and a colon. The body is indented below. Nothing runs until you call it, by writing its name with brackets. Think of a recipe card. You write the steps once, then cook the dish whenever you like by naming the card. Functions stop you repeating yourself, and they give your code names that explain what it does.",
    A=dict(file="greet.py", label="Define and call", on="one function, called twice",
           src='''
def greet():
    print("Hello from a function")
greet()
greet()
''',
           narr="[HL 1] The word def, a name, empty brackets, and a colon. This line only makes the function. It does not run it. [HL 2] The body is indented. This is what runs on every call. [HL 3] A call. The name, with brackets. Python jumps up to the body, runs it, and comes back. [HL 4] A second call. The same body runs again. Write once, use many times."),
    c2=dict(label="What a call does", on="Call flow: the call line, the def, the body, and the return to the next line", narr="Here is the journey of a call. Python reaches the call line. It jumps up to the def, and runs the body, line by line. When the body ends, Python returns to the line just after the call, and carries on. Defining a function does nothing by itself. Only a call sends Python on this trip.", anim=CALL),
    B=dict(file="banner.py", label="A function that calls another", on="a banner built from two small functions",
           src='''
def line():
    print("-" * 10)
def title():
    line()
    print("KONKANI")
    line()
title()
''',
           narr="[HL 1] A small function that prints ten dashes. [HL 2] Its body. [HL 3] A second function, called title. [HL 4] Inside it, we call line. [HL 5] Print the word. [HL 6] And call line again. [HL 7] One call to title runs the whole banner. Small functions that do one job, combined, make big programs easy to read."),
    term="A line of dashes, the word KONKANI, and another line of dashes.",
    recap=["def makes a function, and the body is indented below it.", "Nothing runs until the function is called with brackets.", "A function can call other functions.", "Write it once, call it as often as you like."],
    bug=dict(title="defined but never called", kind="output", file="greet.py", wrong='''
def hello():
    print("Hi")
''', fixed='''
def hello():
    print("Hi")
hello()
''', wrong_note="the function is only defined", fixed_note="a call is added",
             why="A def only creates the function; the body runs only when you call it with brackets.",
             narr="Bug of the Day. We define the function hello, and run the program. Nothing happens. No error, and no output. A def only makes the function. It does not run it. Add a call, the name with brackets, and Hi appears. If a function seems to do nothing, check that you actually call it."),
    pun="Why did the function never get tired? It was always called back.",
    task="write a function that prints a welcome", challenge="Write a function called welcome that prints two lines, then call it three times.",
    answer="Define def welcome(): with two print lines inside, then call welcome() three times.",
    shorts=[
        ("What is a function?", "A function is a named block of code. You write it once with def, a name, brackets, and a colon. The body is indented below. Then you can use it as many times as you like by calling its name. Think of a recipe card. Write the steps once, and cook the dish whenever you want. Functions stop you repeating yourself.", "DEF GREET():", "Write once, use often."),
        ("Define versus call", "Here is the most important idea about functions. Defining and calling are two different things. The def line only makes the function. Nothing runs. A call, the name with brackets, runs the body. When Python reaches a call, it jumps up to the body, runs it, and comes back to the next line. Two steps, always.", "DEF = MAKE · CALL = RUN", "Two separate steps."),
        ("Functions calling functions", "A function can call another function. A title function can call a line function, print a word, and call the line function again. One call to title runs all of it. Small functions that do one job each are easy to read, easy to test, and easy to reuse. Build big things from small, named pieces.", "TITLE() → LINE()", "Small pieces, big programs."),
        ("The function that did nothing", "A quiet bug. You write a function, run the program, and nothing happens. No error, no output. You only defined the function, and never called it. A def makes the function, it does not run it. Add the call, the name with brackets, and your function finally does its job. Check for the call first.", "NO CALL, NO OUTPUT", "Did you call it?"),
        ("Pun and challenge", "Why did the function never get tired? It was always called back. Your challenge. Write a function called welcome. Inside, print two lines of greeting. Then call the function three times, one after another. You should see six lines on the screen. Try changing the text inside the function, and see all three calls change together. Share it below.", "WRITE A WELCOME()", "Try your first function."),
    ],
))

EPISODES.append(dict(
    n=42, title="Parameters and return values", spoken="parameters and return values",
    yt="Python Parameters and return Explained", thumb="IN AND OUT",
    vis="Xecxec feeding a number into a machine labelled double() and catching the answer",
    goals=["pass values in with parameters", "send a value back with return", "tell return from print"],
    tags=["python return", "python parameters", "python function arguments", "print vs return"],
    hash=["#functions", "#return"],
    analogy="a fish-weighing machine: you put the fish in, and a number comes out that you can write down",
    c_title="Values in, values out",
    c_pts=["Parameters are names for the values you pass in", "return sends a value back to the caller", "print only shows a value; it does not give it back"],
    intro="A function becomes truly useful when it takes values in, and hands a result back. Today we learn both.",
    concept="Parameters are names in the brackets of the def line. They receive the values you pass when you call. Return sends a value back to the caller, so you can save it or use it. Think of a fish weighing machine. You put the fish in, and a number comes out that you can write down. Print only shows a value on the screen. Return hands the value over to your program.",
    A=dict(file="double.py", label="Parameter and return", on="a function that doubles a number",
           src='''
def double(n):
    return n * 2
answer = double(4)
print(answer)
print(double(10))
''',
           narr="[HL 1] One parameter, n. It is a name for whatever value we pass in. [HL 2] Return sends n times two back. [HL 3] We call double with four. Four is tied to n, the body runs, and the answer eight comes back. We tie it to answer. [HL 4] Print the answer, eight. [HL 5] We can use a call straight inside print. Ten doubled is twenty."),
    mem=dict(label="The returned value gets a name", on="The name answer tied to the int 8, which came back from double(4)", names=["answer"], **{"from": "A"},
             narr="Here is the picture. The name answer is tied to the int eight. That int was made inside the function, and returned. The parameter n is gone now, because it only lived while the function ran. Only the returned value survived, and only because we tied a name to it."),
    B=dict(file="area.py", label="Two parameters", on="a function with width and height",
           src='''
def area(width, height):
    return width * height
print(area(3, 4))
total = area(2, 5) + area(1, 1)
print(total)
''',
           narr="[HL 1] Two parameters, separated by a comma. Values are matched by position. [HL 2] Return the product. [HL 3] Three and four give twelve. [HL 4] A function call is a value, so we can add two calls together. Two times five is ten, and one times one is one. [HL 5] Eleven. Since return gives the value back, we can use it anywhere a value fits."),
    term="Twelve, then eleven.",
    recap=["Parameters are names in the def line that receive the passed values.", "Arguments are matched to parameters by position.", "return sends a value back to the caller.", "print shows a value but does not give it back."],
    bug=dict(title="print instead of return", kind="output", file="double.py", wrong='''
def double(n):
    print(n * 2)
result = double(4)
print(result)
''', fixed='''
def double(n):
    return n * 2
result = double(4)
print(result)
''', wrong_note="print is used inside the function", fixed_note="return hands the value back",
             why="print only shows the value; a function with no return gives back None, so the name result holds None.",
             narr="Bug of the Day. Our function prints eight, which looks right. But the result we saved prints None. The function used print, not return. Print shows the value on the screen, and the function hands back nothing, which Python calls None. Use return, and the value travels back to the caller."),
    pun="Why did the function get a medal? It always returned what it was given.",
    task="write a function that adds two numbers", challenge="Write a function add(a, b) that returns the sum, then print add(7, 8).",
    answer="Use def add(a, b): return a + b, then print(add(7, 8)), which shows 15.",
    shorts=[
        ("Parameters", "Parameters are names in the brackets of the def line. They receive the values you pass in when you call the function. Def double, open bracket, n. When you call double with four, the value four is tied to the name n inside the function. The function can then use n, like any other name. Different calls pass different values.", "DEF DOUBLE(N):", "Names for the inputs."),
        ("Return", "Return sends a value back to whoever called the function. Return n times two. Then you can save the result in a name, print it, or use it in a sum. A function call is itself a value. That is what lets you build big calculations out of small functions. The caller gets the answer, and decides what to do with it.", "RETURN N * 2", "Hand the answer back."),
        ("Positional arguments", "When a function has two parameters, the values you pass are matched by position. Area, three, four. Three goes to width, and four goes to height. The first value goes to the first parameter, the second to the second. Mix up the order, and you may get the wrong answer. For multiplication it does not matter, but for subtraction it does.", "AREA(3, 4)", "Order matters."),
        ("Print versus return", "A very common bug. Your function uses print, and you save the result. Then the result is None. Print only shows a value on the screen. It does not give it back. Only return gives a value back. If you want to use the answer later, return it. Print is for people, and return is for your program.", "PRINT ≠ RETURN", "Show or give?"),
        ("Pun and challenge", "Why did the function get a medal? It always returned what it was given. Your challenge. Write a function called add, with two parameters, a and b. It should return the sum. Then print the result of add, seven, eight. You should see fifteen. Try calling it with bigger numbers, and with decimals. Share your function in the comments.", "WRITE ADD(A, B)", "Try return."),
    ],
))

EPISODES.append(dict(
    n=43, title="Default and keyword arguments", spoken="default and keyword arguments",
    yt="Python Default and Keyword Arguments", thumb="DEFAULTS",
    vis="Xecxec holding a coffee order card with a pre-ticked box labelled default",
    goals=["give a parameter a default value", "pass arguments by keyword", "avoid mutable default arguments"],
    tags=["python default arguments", "python keyword arguments", "mutable default argument", "python function defaults"],
    hash=["#functions", "#defaults"],
    analogy="a tea stall order: tea comes with sugar by default, unless you say 'no sugar'",
    c_title="Optional and named",
    c_pts=["name=value in the def gives a default", "Callers can leave the argument out", "Keyword arguments name the parameter in the call"],
    intro="Some inputs are almost always the same. Today we give parameters default values, and name arguments in calls.",
    concept="A default value goes in the def line. Greeting equals Hello. If the caller leaves that argument out, the default is used. Think of a tea stall. Tea comes with sugar by default, unless you say, no sugar. You can also pass arguments by name. Greeting equals Hi. Then the order does not matter, and the call explains itself. Be careful with one thing. Never use a list as a default.",
    A=dict(file="defaults.py", label="Defaults and keywords", on="a greeting with a default word",
           src='''
def greet(name, greeting="Hello"):
    return greeting + ", " + name
print(greet("Asha"))
print(greet("Ravi", "Namaste"))
print(greet(greeting="Hi", name="Maya"))
''',
           narr="[HL 1] Two parameters. The second has a default, Hello. [HL 2] Join the greeting and the name. [HL 3] Only the name is passed, so the default greeting is used. Hello, Asha. [HL 4] Two values by position. Namaste replaces the default. [HL 5] Keyword arguments. We name each one, so the order does not matter. Hi, Maya."),
    c2=dict(label="Which value wins?", on="Three calls side by side; the default is crossed out when a value is passed", narr="Here is the rule. If the caller gives a value, that value wins. If not, the default is used. Parameters with defaults must come after the ones without. In the call, positional arguments come first, then keyword ones. Keyword arguments make long calls much easier to read, because every value carries its own label.", anim="Three call cards; the default value glows when used and fades when replaced"),
    B=dict(file="power.py", label="Default exponent", on="power defaults to squaring",
           src='''
def power(base, exp=2):
    return base ** exp
print(power(5))
print(power(2, 10))
print(power(exp=3, base=2))
''',
           narr="[HL 1] Exp defaults to two. [HL 2] Return base to the power exp. [HL 3] One value, so exp is two. Five squared is twenty five. [HL 4] Two values. Two to the power ten is one thousand twenty four. [HL 5] By keyword, in any order. Two cubed is eight."),
    term="Twenty five, then one thousand twenty four, then eight.",
    recap=["name=value in the def line sets a default.", "Callers can omit an argument that has a default.", "Keyword arguments carry their own labels.", "Never use a list or dictionary as a default value."],
    bug=dict(title="a list as a default", kind="output", file="defaults.py", wrong='''
def add_item(item, basket=[]):
    basket.append(item)
    return basket
print(add_item("fish"))
print(add_item("rice"))
''', fixed='''
def add_item(item, basket=None):
    if basket is None:
        basket = []
    basket.append(item)
    return basket
print(add_item("fish"))
print(add_item("rice"))
''', wrong_note="the default list is made once", fixed_note="None as the default, a new list inside",
             why="A default value is created once, when the def runs, so every call shares the same list; use None and make a fresh list inside.",
             narr="Bug of the Day. We add fish, then rice, to two separate baskets. But the second basket also holds fish. The default list was made only once, when the def ran. Every call shares it. Use None as the default instead. Inside, if basket is None, make a brand new list, and each call gets its own."),
    pun="Why did the parameter relax? It already had a default plan.",
    task="a greeting with a default", challenge="Write welcome(name, place=\"Goa\") that returns a welcome message, and call it with and without place.",
    answer="Use def welcome(name, place=\"Goa\"): return \"Welcome \" + name + \" to \" + place, then call welcome(\"Asha\") and welcome(\"Ravi\", \"Pune\").",
    shorts=[
        ("Default values", "A default value goes in the def line. Greeting equals Hello. If the caller leaves that argument out, Python uses the default. Think of a tea stall, where tea comes with sugar unless you ask for none. Defaults make functions flexible. They keep simple calls short, and still allow special cases. Parameters with defaults must come after the ones without.", "GREETING=\"HELLO\"", "Optional arguments."),
        ("Keyword arguments", "In a call, you can name each argument. Greet, greeting equals Hi, name equals Maya. Because each value carries its label, the order does not matter. Keyword arguments make long calls much easier to read. Anyone looking at the line can see what each value means, without checking the def. Use them when a call has several values.", "GREET(NAME=\"MAYA\")", "Name your arguments."),
        ("Which value wins", "The rule is simple. If the caller passes a value, that value wins. If not, the default is used. Power of five gives five squared, because the default exponent is two. Power of two, ten, uses the ten instead. One function can serve many cases, and the call shows exactly which one you want.", "POWER(5) · POWER(2, 10)", "Caller first."),
        ("The shared basket", "The most famous Python trap. A list as a default value. The list is made once, when the def runs, so every call shares it. Add fish, then add rice, and the second basket also holds fish. Use None as the default. Inside, if it is None, make a fresh list. Then each call gets its own.", "BASKET=[] IS SHARED", "Use None."),
        ("Pun and challenge", "Why did the parameter relax? It already had a default plan. Your challenge. Write a function called welcome, with a name, and a place that defaults to Goa. It should return a welcome message. Call it once with only a name, and once with a name and a place. Check both messages. Post your function in the comments below.", "WELCOME(NAME, PLACE)", "Try defaults."),
    ],
))

EPISODES.append(dict(
    n=44, title="*args and **kwargs", spoken="args and kwargs",
    yt="Python *args and **kwargs Explained", thumb="ANY NUMBER OF ARGS",
    vis="Xecxec catching a stream of fish into a net labelled *args",
    goals=["accept any number of values with *args", "accept named extras with **kwargs", "unpack a list into a call with *"],
    tags=["python args kwargs", "python variable arguments", "python unpacking arguments", "typeerror missing arguments"],
    hash=["#args", "#kwargs"],
    analogy="a net on a fishing boat: it takes however many fish come, big haul or small",
    c_title="Any number of arguments",
    c_pts=["*numbers collects extra values into a tuple", "**info collects named extras into a dictionary", "* in a call spreads a list into separate values"],
    intro="Sometimes you do not know how many values a function will get. Today we make functions that take any number.",
    concept="A star in front of a parameter collects all the extra values into a tuple. A double star collects named extras into a dictionary. Think of a net on a fishing boat. It takes however many fish come. The names args and kwargs are only a habit, the stars do the work. And in a call, a star spreads a list out into separate values. Remember that star pair, one collects, the other spreads.",
    A=dict(file="varargs.py", label="Collect with a star", on="a total of any number of values",
           src='''
def total(*numbers):
    return sum(numbers)
print(total(1, 2, 3))
print(total(10, 20))
print(total())
''',
           narr="[HL 1] A star before the parameter. Whatever values arrive, Python collects them into a tuple called numbers. [HL 2] Sum adds up the tuple. [HL 3] Three values, total six. [HL 4] Two values, thirty. [HL 5] No values at all. The tuple is empty, and the sum is zero. One function, any number of calls."),
    c2=dict(label="Collect and spread", on="Left: values dropping into a net labelled *args. Right: a list being spread into separate boxes by a star in the call", narr="Here is the pair. In a def line, the star collects. Separate values flow in, and one tuple comes out. In a call, the star spreads. One list goes in, and separate values flow out into the parameters. Collect on the way in, spread on the way out. Two directions of the same star.", anim="Values fall into a net and become one box; a list opens and its items fly into separate parameter slots"),
    B=dict(file="kw.py", label="Collect named extras", on="a function that takes any keyword arguments",
           src='''
def describe(**info):
    for key, value in info.items():
        print(key, "=", value)
describe(name="Asha", city="Panjim")
''',
           narr="[HL 1] Two stars. Every named extra is collected into a dictionary called info. [HL 2] We loop over the pairs. [HL 3] Print each key and value. [HL 4] Two named values, name and city. Python builds the dictionary for us. Name equals Asha. City equals Panjim. This is how many library functions accept flexible options."),
    term="Name equals Asha. City equals Panjim.",
    recap=["*args collects extra positional values into a tuple.", "**kwargs collects extra named values into a dictionary.", "A star in a call spreads a list into separate values.", "args and kwargs are habit names; the stars are what matter."],
    bug=dict(title="passing a list instead of spreading it", file="varargs.py", wrong='''
def add(a, b, c):
    return a + b + c
nums = [1, 2, 3]
print(add(nums))
''', fixed='''
def add(a, b, c):
    return a + b + c
nums = [1, 2, 3]
print(add(*nums))
''', wrong_note="the whole list goes into a", fixed_note="the star spreads the list",
             why="Without the star, the list is passed as one value for a, leaving b and c missing; the star spreads its items into separate arguments.",
             narr="Bug of the Day. We have a list of three numbers, and a function with three parameters. We pass the list as it is. Python says, type error, add is missing two required positional arguments. The whole list went into the first parameter. Put a star in front of the list in the call, and the items spread out."),
    pun="Why did the function love stars? It could take everything the sky sent.",
    task="average of any number of marks", challenge="Write average(*marks) that returns the sum divided by the count, and print average(70, 80, 90).",
    answer="Use def average(*marks): return sum(marks) / len(marks), then print(average(70, 80, 90)), which shows 80.0.",
    shorts=[
        ("Star args", "A star in front of a parameter collects all extra values into a tuple. Def total, star numbers. Call it with one value, or ten, or none. Python gathers them all into the tuple. Then you can loop over it, or sum it. It is how print itself accepts any number of things. Think of a fishing net that takes whatever fish come.", "DEF TOTAL(*NUMBERS):", "Take any number."),
        ("Double star kwargs", "A double star collects named extras into a dictionary. Def describe, double star info. Call it with name equals Asha, city equals Panjim. Python builds a dictionary with those pairs. Then you can loop over it with items. This is how many library functions take flexible options, without needing a parameter for every possible setting.", "DEF F(**INFO):", "Collect named extras."),
        ("Spread with a star", "A star also works in a call. If you have a list, and the function wants separate values, put a star in front of the list. Add, star nums. Python spreads the items into the parameters, one by one. In the def line, the star collects. In the call, the star spreads. Same symbol, opposite directions.", "ADD(*NUMS)", "Spread a list."),
        ("Missing arguments", "Here is the bug. You pass a whole list to a function that wants three values. Python says, type error, add is missing two required positional arguments. The entire list went into the first parameter. The fix is one character. A star before the list in the call, and the three items spread into the three parameters.", "TYPEERROR: MISSING 2 ARGUMENTS", "Add the star."),
        ("Pun and challenge", "Why did the function love stars? It could take everything the sky sent. Your challenge. Write a function called average, with a star marks parameter. It should return the sum of the marks divided by how many there are. Print average of seventy, eighty, ninety. You should see eighty point zero. Share your code in the comments below.", "WRITE AVERAGE(*MARKS)", "Try star args."),
    ],
))

EPISODES.append(dict(
    n=45, title="Scope: local vs global", spoken="scope, local and global",
    yt="Python Scope: Local vs Global Variables", thumb="LOCAL OR GLOBAL?",
    vis="Xecxec standing inside a small room labelled local, looking at a big hall labelled global",
    goals=["tell a local name from a global name", "see that a function can read but not rebind a global", "use global only when needed"],
    tags=["python scope", "python global keyword", "local vs global python", "unboundlocalerror"],
    hash=["#scope", "#global"],
    analogy="a hotel: names inside a room are private, names in the lobby are shared by everyone",
    c_title="Where a name lives",
    c_pts=["A name made inside a function is local to it", "Python looks local first, then global", "global lets a function rebind a global name"],
    intro="A name does not live everywhere. Today we learn where names live, and who can see them.",
    concept="A name made inside a function is local. It exists only while the function runs. A name made outside is global. Python looks for a name locally first, then globally. Think of a hotel. Names inside a room are private. Names in the lobby are shared. A function can read a global name. But if it assigns to that name, Python makes a new local one, unless you say global.",
    A=dict(file="scope.py", label="Two names, one spelling", on="an inner and an outer level",
           src='''
level = "outer"
def show():
    level = "inner"
    print(level)
show()
print(level)
''',
           narr="[HL 1] A global name, level, tied to outer. [HL 2] A function. [HL 3] Inside, we assign level. This makes a brand new local name, which hides the global one. [HL 4] Prints inner. [HL 5] We call the function. [HL 6] Back outside, the global level was never touched. It still says outer. Same spelling, two different names, in two different rooms."),
    mem=dict(label="The global name is untouched", on="After the call, the global level is still tied to the string outer", names=["level"], **{"from": "A"},
             narr="Here is what is left after the run. Only one name exists now, the global level, tied to the string outer. The local level lived inside the function, tied to inner. When the function finished, that local name disappeared. Nothing the function did to its own level changed the global one."),
    B=dict(file="global_demo.py", label="Rebinding a global", on="the global keyword lets a function change a global name",
           src='''
count = 0
def add_one():
    global count
    count = count + 1
add_one()
add_one()
print(count)
''',
           narr="[HL 1] A global counter. [HL 2] A function. [HL 3] The word global says, this name means the global one. [HL 4] Now the assignment changes the global count. [HL 5] First call. [HL 6] Second call. [TRACK count=2] [HL 7] The count is two. Use global sparingly. Passing values in and returning them out is usually cleaner."),
    term="Two.",
    recap=["A name made inside a function is local.", "Python looks local first, then global.", "A function can read a global but must declare global to rebind it.", "Prefer parameters and return over global."],
    bug=dict(title="using a global before assigning it", file="scope.py", wrong='''
count = 0
def add_one():
    count = count + 1
add_one()
''', fixed='''
count = 0
def add_one():
    global count
    count = count + 1
add_one()
print(count)
''', wrong_note="count is assigned, so it is local", fixed_note="global count added",
             why="Assigning to count anywhere in the function makes it local for the whole function, so reading it before the assignment fails.",
             narr="Bug of the Day. We try to add one to the global count. Python says, unbound local error. Cannot access local variable count where it is not associated with a value. Because we assign count in the function, Python treats count as local everywhere in it. The local has no value yet. Declare global count first, and the line works."),
    pun="Why did the local variable feel lonely? Nobody outside the function knew its name.",
    task="a counter with global", challenge="Write a function bump() that adds 10 to a global score. Call it twice and print the score.",
    answer="Use score = 0, then def bump(): global score, score = score + 10, call bump() twice, print(score) which shows 20.",
    shorts=[
        ("Local names", "A name made inside a function is local. It exists only while the function runs, and nothing outside can see it. When the function ends, the name disappears. Think of a hotel room. What happens in the room, stays in the room. Local names keep functions tidy, because they cannot accidentally change names elsewhere in your program.", "LOCAL = INSIDE ONLY", "Private to the function."),
        ("Local first, then global", "When Python looks for a name, it checks the local names first. If it finds it there, it stops. If not, it checks the global names. So a function can read a global name freely. But if you assign to a name inside a function, Python makes a new local one. The global with the same spelling is hidden, not changed.", "LOCAL → GLOBAL", "The lookup order."),
        ("The global keyword", "To change a global name from inside a function, say so first. The word global, then the name. After that, an assignment in the function changes the global one. It works, but use it sparingly. Code that reaches out and changes global names is hard to follow. Passing values in and returning values out is usually cleaner and safer.", "GLOBAL COUNT", "Use with care."),
        ("Unbound local error", "A confusing bug. You write count equals count plus one inside a function. Python says, unbound local error. Because you assign count, Python treats it as local for the whole function, and the local has no value yet. Add the line global count at the top of the function, and it works. Or pass the value in, and return the new one.", "UNBOUNDLOCALERROR", "Declare global."),
        ("Pun and challenge", "Why did the local variable feel lonely? Nobody outside the function knew its name. Your challenge. Make a global name score, equal to zero. Write a function called bump that adds ten to it, using the global keyword. Call it twice, and print the score. You should see twenty. Then try it without the global line. Post what happens.", "A GLOBAL SCORE", "Try global."),
    ],
))

EPISODES.append(dict(
    n=46, title="lambda, map and filter", spoken="lambda, map and filter",
    yt="Python lambda, map and filter", thumb="LAMBDA",
    vis="Xecxec holding a tiny one-line function card labelled lambda n: n * 2",
    goals=["write a one-line function with lambda", "transform items with map and keep some with filter", "use lambda as a sort key"],
    tags=["python lambda", "python map filter", "anonymous function python", "map object python"],
    hash=["#lambda", "#map"],
    analogy="a sticky-note instruction: too small to deserve a name, but handy for one quick job",
    c_title="Tiny functions",
    c_pts=["lambda args: expression makes a nameless function", "map applies a function to every item", "filter keeps the items where the function is True"],
    intro="Sometimes a function is so small, a whole def feels like too much. Today we meet the lambda.",
    concept="A lambda is a tiny function without a name. The word lambda, the parameters, a colon, and one expression. The value of that expression is returned automatically. Think of a sticky note instruction. Too small to deserve a name, but handy for one quick job. Map applies a function to every item. Filter keeps only the items for which the function says True. Both give back a lazy object, which you wrap in list to see.",
    A=dict(file="lam.py", label="lambda, map, filter", on="a doubling lambda, then map and filter on a list",
           src='''
double = lambda n: n * 2
print(double(5))
nums = [1, 2, 3, 4]
print(list(map(lambda n: n * 2, nums)))
print(list(filter(lambda n: n % 2 == 0, nums)))
''',
           narr="[HL 1] A lambda tied to the name double. Parameter n, expression n times two. No return word is needed. [HL 2] Call it like any function. Ten. [HL 3] A list of four numbers. [HL 4] Map applies the lambda to every item. List turns the result into a list we can print. Two, four, six, eight. [HL 5] Filter keeps items where the lambda gives True. Only the even numbers survive."),
    c2=dict(label="Map and filter pipelines", on="Items flow through a map machine that doubles them, and through a filter gate that lets only even numbers pass", narr="Picture two machines. The map machine takes every item, changes it, and sends it on. The count of items stays the same. The filter gate checks each item and lets only some through. The count can shrink. Both are lazy. Nothing happens until you ask for the results, for example with list.", anim="Number tokens move along a belt through a transform box, then through a gate that drops the odd ones"),
    B=dict(file="sortkey.py", label="A lambda as a sort key", on="sort words by their last letter",
           src='''
words = ["banana", "fig", "apple"]
print(sorted(words, key=lambda w: w[-1]))
''',
           narr="[HL 1] Three words. [HL 2] Sorted, with a key that is a lambda. For each word, the key is its last letter. Banana ends in a, apple ends in e, and fig ends in g. So the order is banana, apple, fig. A lambda is perfect here, because the rule is used once, in one place."),
    term="Banana, apple, fig.",
    recap=["lambda args: expression is a one-line function with no name.", "map applies a function to every item.", "filter keeps the items for which the function is True.", "Wrap map and filter in list() to see the results."],
    bug=dict(title="map is not a list", kind="output", file="lam.py", wrong='''
nums = [1, 2, 3]
print(map(lambda n: n * 2, nums))
''', fixed='''
nums = [1, 2, 3]
print(list(map(lambda n: n * 2, nums)))
''', wrong_note="the map object is printed", fixed_note="wrapped in list()",
             why="map returns a lazy iterator, not a list, so printing it shows the object; wrap it in list() to get the values.",
             narr="Bug of the Day. We print the result of map, and get a strange line, map object at a long address. Map does not make a list. It gives a lazy object that makes values only when asked. Wrap the map in list, and you see the real values. Filter works the same way."),
    pun="Why did the lambda go unnamed? It preferred a life without labels.",
    task="square every number with map", challenge="Use map and a lambda to square the numbers in [1, 2, 3, 4], and print the list.",
    answer="Use print(list(map(lambda n: n * n, [1, 2, 3, 4]))), which shows [1, 4, 9, 16].",
    shorts=[
        ("What is a lambda?", "A lambda is a tiny function without a name. The word lambda, the parameters, a colon, and one expression. The value of the expression is returned automatically. Lambda n colon n times two doubles a number. It is perfect when a function is so small that a whole def feels like too much. Think of a sticky note instruction, quick and disposable.", "LAMBDA N: N * 2", "A nameless function."),
        ("Map", "Map applies a function to every item in a list. Map, a lambda that doubles, and the list. Each item goes through the lambda, and the doubled value comes out. The count stays the same. Wrap the result in list to see it. Map is the functional way to write a loop that transforms every item. It is neat for one-liners.", "MAP(F, ITEMS)", "Change every item."),
        ("Filter", "Filter keeps only some items. It takes a function that says True or False, and a list. Every item for which the function says True is kept, and the rest are dropped. A lambda that checks for even numbers keeps only the evens. Like map, filter is lazy, so wrap it in list. Think of a gate that only lets some items through.", "FILTER(F, ITEMS)", "Keep only some."),
        ("Map object", "A bug that surprises everyone. You print the result of map, and Python shows, map object at, and a long address. Map does not build a list. It builds a lazy object that makes values only when asked. Wrap it in list, and you see the real values. The same goes for filter. Always wrap them to print.", "<MAP OBJECT AT 0x...>", "Wrap it in list."),
        ("Pun and challenge", "Why did the lambda go unnamed? It preferred a life without labels. Your challenge. Use map and a lambda to square every number in the list one, two, three, four. Print the result as a list. You should see one, four, nine, sixteen. Then use filter to keep only the squares above five. Share both lines in the comments.", "SQUARES WITH MAP", "Try map."),
    ],
))

EPISODES.append(dict(
    n=47, title="Recursion", spoken="recursion",
    yt="Python Recursion: Functions That Call Themselves", thumb="RECURSION",
    vis="Xecxec looking at a mirror that shows a smaller Xecxec looking at a smaller mirror",
    goals=["write a function that calls itself", "always include a base case", "read a RecursionError"],
    tags=["python recursion", "python factorial", "base case recursion", "recursionerror python"],
    hash=["#recursion", "#functions"],
    analogy="Russian dolls: open one and you find a smaller doll, until the smallest doll that does not open",
    c_title="A function that calls itself",
    c_pts=["The function calls itself on a smaller problem", "The base case stops the calls", "Every call waits for the one it started"],
    intro="Today we meet one of the most beautiful ideas in programming, a function that calls itself.",
    concept="Recursion means a function calls itself, on a smaller version of the problem. Think of Russian dolls. Open one and you find a smaller doll, until you reach the smallest, which does not open. That smallest doll is the base case. It stops the calls. Without a base case, the function calls itself forever, until Python stops it with an error. Every call waits for the smaller call it started.",
    A=dict(file="fact.py", label="Factorial", on="factorial of 5 by recursion",
           src='''
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)
print(factorial(5))
''',
           narr="[HL 1] A function that takes n. [HL 2] The base case. If n is one, the answer is one, and no more calls are made. [HL 3] The recursive case. Five times factorial of four. Python must first find factorial of four, which needs factorial of three, and so on, down to one. [HL 4] Then the answers come back up. One, two, six, twenty four, one hundred twenty. Five factorial is one hundred twenty."),
    c2=dict(label="The call stack", on="Five boxes stacked: factorial(5) at the bottom waiting, up to factorial(1) at the top; then answers flow back down", narr="Here is the stack. Factorial of five calls factorial of four, and waits. That calls factorial of three, and waits. Down to factorial of one, which answers at once, with one. Now the waiting calls finish, one by one, from the top down. Two, six, twenty four, one hundred twenty. Each call keeps its own n.", anim="Boxes stack up with a pop for each call; the top box returns 1 and the boxes pop off one by one, each passing a value down"),
    B=dict(file="countdown.py", label="A countdown", on="count down, then stop at the base case",
           src='''
def countdown(n):
    if n == 0:
        print("Liftoff")
        return
    print(n)
    countdown(n - 1)
countdown(3)
''',
           narr="[HL 1] A function that takes n. [HL 2] The base case. At zero, [HL 3] print Liftoff, [HL 4] and return. [HL 5] Otherwise, print n. [HL 6] And call countdown again with one less. Three, two, one, Liftoff. Each call makes the problem smaller, and the base case guarantees that it ends."),
    term="Three, two, one, Liftoff.",
    recap=["A recursive function calls itself on a smaller problem.", "A base case stops the recursion.", "Each call has its own copy of the parameters.", "Without a base case Python stops with a RecursionError."],
    bug=dict(title="a missing base case", file="countdown.py", trim=1, wrong='''
def countdown(n):
    print(n)
    countdown(n - 1)
countdown(3)
''', fixed='''
def countdown(n):
    if n == 0:
        print("Liftoff")
        return
    print(n)
    countdown(n - 1)
countdown(3)
''', wrong_note="nothing ever stops the calls", fixed_note="a base case at zero",
             why="Without a base case the function keeps calling itself with smaller and smaller numbers, so Python stops it when it reaches its recursion limit.",
             narr="Bug of the Day. Our countdown has no base case. It prints three, two, one, zero, minus one, and keeps going. After about a thousand calls, Python stops it with a recursion error, maximum recursion depth exceeded. Python protects itself from endless calls. Add a base case that returns, and the countdown ends."),
    pun="To understand recursion, you must first understand recursion.",
    task="a recursive sum", challenge="Write a recursive function total(n) that returns 1 + 2 + ... + n, and print total(4).",
    answer="Use def total(n): if n == 1: return 1, then return n + total(n - 1). print(total(4)) shows 10.",
    shorts=[
        ("What is recursion?", "Recursion means a function calls itself. Each call works on a smaller version of the problem. Think of Russian dolls. Open one, and you find a smaller doll, until you reach the smallest, which does not open. That smallest one is the base case, and it stops the whole process. Recursion is natural for problems that contain smaller copies of themselves.", "A FUNCTION CALLS ITSELF", "Dolls inside dolls."),
        ("The base case", "Every recursive function needs a base case. It is the simplest version of the problem, which the function answers directly, without calling itself. For factorial, factorial of one is one. Without it, the function would call itself forever. Always write the base case first, then write the call that makes the problem smaller. Check that it really gets smaller.", "IF N == 1: RETURN 1", "Write it first."),
        ("Calls wait", "Here is how factorial of five works. It calls factorial of four, and waits. That calls factorial of three, and waits. Down to factorial of one, which answers one. Then the waiting calls finish, one by one, multiplying on the way back. Two, six, twenty four, one hundred twenty. Each call keeps its own copy of n.", "5 × 4 × 3 × 2 × 1", "Calls wait for answers."),
        ("Recursion error", "What if you forget the base case? The function keeps calling itself, with smaller and smaller numbers, and never stops. After about a thousand calls, Python protects itself, and raises a recursion error, maximum recursion depth exceeded. The fix is a base case that returns. Whenever you see this error, ask, what stops this function?", "RECURSIONERROR", "Add a base case."),
        ("Pun and challenge", "To understand recursion, you must first understand recursion. Your challenge. Write a recursive function called total, that adds one plus two, up to n. The base case is n equals one, which returns one. Otherwise return n plus total of n minus one. Print total of four. You should see ten. Share your function below.", "RECURSIVE SUM", "Try recursion."),
    ],
))

EPISODES.append(dict(
    n=48, title="Docstrings and type hints", spoken="docstrings and type hints",
    yt="Python Docstrings and Type Hints", thumb="DOCUMENT YOUR CODE",
    vis="Xecxec sticking a label on a function box that says takes float, returns float",
    goals=["describe a function with a docstring", "annotate parameters and results with type hints", "know that hints are notes, not rules"],
    tags=["python docstring", "python type hints", "python annotations", "type hints not enforced"],
    hash=["#typehints", "#docstring"],
    analogy="a label on a spice jar: it tells you what is inside, but it does not stop you putting something else in",
    c_title="Notes for readers",
    c_pts=["A docstring is a string on the first line of the body", "Type hints name the expected types", "Python does not enforce hints"],
    intro="Code is read far more often than it is written. Today we learn two ways to explain a function to its readers.",
    concept="A docstring is a string placed on the first line of a function body. It says what the function does. Type hints show the type of each parameter, after a colon, and the type of the result, after an arrow. Think of a label on a spice jar. It tells you what is inside. But it does not stop you pouring something else in. Python reads hints, but does not enforce them. Tools like editors use them to warn you.",
    A=dict(file="hints.py", label="Hints and a docstring", on="area with typed parameters and a docstring",
           src='''
def area(width: float, height: float) -> float:
    """Return the area of a rectangle."""
    return width * height
print(area(2.5, 4))
print(area.__doc__)
''',
           narr="[HL 1] Each parameter has a colon and a type. The arrow, and float, say the result is a float. [HL 2] The docstring, in triple quotes. It must be the first thing in the body. [HL 3] The code itself. [HL 4] Two and a half times four is ten point zero. [HL 5] Every function keeps its docstring in a special attribute. Printing it shows the text. Editors show this text when you hover over the function."),
    c2=dict(label="What a hint looks like", on="A function signature with callouts for the parameter types, the return type, and the docstring", narr="Look at the signature piece by piece. After each parameter name, a colon and its type. After the brackets, an arrow and the type of the result. Below, the docstring, a short sentence that says what the function does. Together they let a reader use the function without reading its body. That saves time, and it prevents mistakes.", anim="Callout arrows point at each part of the signature and the docstring, one at a time"),
    B=dict(file="doc.py", label="Annotations are stored", on="hints can be read back from the function",
           src='''
def greet(name: str, times: int = 1) -> str:
    """Greet a person, repeated times times."""
    return ("Hi " + name + ". ") * times
print(greet("Asha", 2).strip())
print(greet.__annotations__)
''',
           narr="[HL 1] A string parameter, and an int parameter with a default of one. The result is a string. [HL 2] A one line docstring. [HL 3] Repeat the greeting. [HL 4] Greeting Asha twice, with the spaces trimmed. [HL 5] Python stores the hints in a dictionary on the function. Tools can read it. But Python itself never checks them while the program runs."),
    term="Hi Asha twice, then the dictionary of hints.",
    recap=["A docstring on the first line of the body describes the function.", "name: type marks a parameter and -> type marks the result.", "Hints are stored on the function, and tools can read them.", "Python does not enforce type hints at run time."],
    bug=dict(title="hints do not stop wrong types", kind="output", file="hints.py", wrong='''
def double(n: int) -> int:
    return n * 2
print(double("ab"))
''', fixed='''
def double(n: int) -> int:
    if not isinstance(n, int):
        raise TypeError("n must be an int")
    return n * 2
print(double(4))
''', wrong_note="a string is passed to an int parameter", fixed_note="an explicit check, if you need one",
             why="Type hints are notes for people and tools; Python still runs the code with any type, so add a check yourself if a wrong type must be rejected.",
             narr="Bug of the Day. The hint says n is an int. We pass the string ab. Python does not complain. It repeats the string, and prints abab. Type hints are labels, not locks. If a wrong type must be rejected, check it yourself inside the function. Editors and tools also read the hints, and can warn you before you run."),
    pun="Why did the function carry a label? It was tired of explaining itself.",
    task="add a docstring and hints", challenge="Write add(a: int, b: int) -> int with a docstring, and print add(2, 3).",
    answer="Use def add(a: int, b: int) -> int: with a docstring, return a + b. print(add(2, 3)) shows 5.",
    shorts=[
        ("Docstrings", "A docstring is a string on the first line of a function body. It says what the function does, in one short sentence. Use triple quotes. Python keeps the docstring on the function, and editors show it when you hover. Write one for every function that is not obvious. Your future self, and your teammates, will read it before they read the code.", "\"\"\"RETURN THE AREA.\"\"\"", "Explain your function."),
        ("Type hints", "Type hints show what a function expects. After each parameter, a colon and a type. After the brackets, an arrow and the type of the result. Def area, width colon float, arrow float. A reader sees at once what goes in and what comes out. Editors use hints to warn you about mistakes before you even run the program.", "DEF F(N: INT) -> INT:", "Say what goes in."),
        ("Hints are notes", "Here is the truth about type hints. Python does not enforce them. They are notes for people and tools. You can pass a string to a parameter marked int, and Python will simply try to run the code. If you need a wrong type to be rejected, check it yourself. Hints help you write better code, but they are not a lock.", "HINTS ≠ RULES", "Notes, not locks."),
        ("Abab", "A surprising bug. The hint says n is an int. You pass the string ab. Python does not complain, and prints abab, because a string times two repeats the text. Hints are labels, not locks. Use an editor that reads hints, or check types yourself when it matters. Never assume that a hint stops a wrong value from arriving.", "DOUBLE(\"AB\") → ABAB", "Python does not check."),
        ("Pun and challenge", "Why did the function carry a label? It was tired of explaining itself. Your challenge. Write a function called add, with two int parameters, a and b, and an int result. Add a one line docstring. Return the sum. Print add of two, three. You should see five. Then print the docstring of your function. Share your function below.", "ADD WITH HINTS", "Try hints."),
    ],
))

EPISODES.append(dict(
    n=49, title="Higher-order functions", spoken="higher-order functions",
    yt="Python Higher-Order Functions: Functions as Values", thumb="FUNCTIONS AS VALUES",
    vis="Xecxec passing a function card like a baton to another function",
    goals=["pass a function as an argument", "return a function from a function", "tell passing a function from calling it"],
    tags=["python higher order functions", "python functions as values", "python closures", "pass function as argument"],
    hash=["#higherorder", "#functions"],
    analogy="a chef handing a recipe card to an assistant: the card is passed around, and the cooking happens only when someone follows it",
    c_title="Functions are values",
    c_pts=["A function name is a value you can pass around", "Brackets mean call it now", "A function can return another function"],
    intro="In Python, a function is a value, like a number or a string. Today we use that idea.",
    concept="A function name, without brackets, is a value. You can tie it to another name, put it in a list, or pass it to another function. Brackets mean, call it now. No brackets means, here is the function itself. Think of a chef handing a recipe card to an assistant. The card is passed around, and the cooking happens only when someone follows it. A function that takes or returns functions is called higher order.",
    A=dict(file="hof.py", label="Passing functions", on="apply takes a function and a value",
           src='''
def apply(func, value):
    return func(value)
def double(n):
    return n * 2
def square(n):
    return n * n
print(apply(double, 5))
print(apply(square, 5))
''',
           narr="[HL 1] Apply takes a function and a value. [HL 2] It calls the function on the value. [HL 3] Double. [HL 4] Returns n times two. [HL 5] Square. [HL 6] Returns n times n. [HL 7] We pass double, with no brackets. Python gives it to apply, which calls it with five. Ten. [HL 8] Pass square instead, and the same apply gives twenty five. The behaviour is now a choice we make at the call."),
    c2=dict(label="Passing versus calling", on="Two cards: double (the function itself, handed over) and double(5) (the answer 10)", narr="Here is the distinction. Double, with no brackets, is the function itself, a card you can hand to someone. Double of five, with brackets, is the result of running it, the number ten. Passing and calling are different things. When a function wants a function, hand over the card. Do not run it first.", anim="A function card slides to another box; a second card with brackets turns into a number"),
    B=dict(file="compose.py", label="Returning a function", on="make_adder returns a new function",
           src='''
def make_adder(k):
    def add(x):
        return x + k
    return add
add5 = make_adder(5)
print(add5(10))
print(make_adder(1)(1))
''',
           narr="[HL 1] A function that takes k. [HL 2] Inside, another function, add. [HL 3] It adds x and k. It remembers k from the outer function. [HL 4] We return add itself, with no brackets. [HL 5] Calling make adder with five gives back a new function, tied to add five. [HL 6] Add five of ten is fifteen. [HL 7] Or call twice in one line. Make adder one, then call it with one. Two."),
    term="Fifteen, then two.",
    recap=["A function name without brackets is a value.", "Brackets call the function.", "A function can take another function as an argument.", "A function can return a new function that remembers its values."],
    bug=dict(title="calling instead of passing", file="hof.py", wrong='''
def apply(func, value):
    return func(value)
def double(n):
    return n * 2
print(apply(double(), 5))
''', fixed='''
def apply(func, value):
    return func(value)
def double(n):
    return n * 2
print(apply(double, 5))
''', wrong_note="double is called with no argument", fixed_note="double is passed as a value",
             why="double() calls the function immediately, with no argument, instead of handing the function itself to apply.",
             narr="Bug of the Day. We wrote double with brackets. That calls double right now, with no number. Python says, type error, double is missing one required positional argument, n. We wanted to hand over the function, not run it. Remove the brackets, and apply receives the function itself."),
    pun="Why did the function pass the baton? It believed in teamwork.",
    task="pass a function into another", challenge="Write apply_twice(f, x) that returns f(f(x)), and use it with a function that adds 3 to 10.",
    answer="Use def apply_twice(f, x): return f(f(x)) and def add3(n): return n + 3. print(apply_twice(add3, 10)) shows 16.",
    shorts=[
        ("Functions are values", "In Python, a function is a value, like a number or a string. Write the name without brackets, and you have the function itself. You can tie it to another name, put it in a list, or pass it to another function. This is the idea behind map, filter, and sorted with a key. It makes your code flexible, because behaviour becomes a choice.", "DOUBLE (NO BRACKETS)", "A function is a value."),
        ("Passing versus calling", "Brackets make all the difference. Double, with no brackets, is the function itself, like a recipe card. Double of five, with brackets, runs the recipe, and gives the number ten. When another function wants a function, hand over the card. Do not run it first. Most errors in this topic come from adding brackets where they do not belong.", "DOUBLE vs DOUBLE(5)", "Card or cooked dish?"),
        ("Return a function", "A function can build and return another function. Make adder takes k, and defines a small function add, which uses k. It returns add itself. Make adder of five gives you a function that adds five. The inner function remembers k, even after make adder has finished. That memory is called a closure. It is a neat way to make custom tools.", "MAKE_ADDER(5)", "Build a tool."),
        ("Missing argument", "Here is the bug. You write apply, open bracket, double, empty brackets, comma, five. Those empty brackets call double right now, without a number. Python says, type error, double is missing one required positional argument. You meant to pass the function, not run it. Remove the brackets, and apply gets the function it asked for.", "TYPEERROR: MISSING 'N'", "Drop the brackets."),
        ("Pun and challenge", "Why did the function pass the baton? It believed in teamwork. Your challenge. Write a function called apply twice, that takes a function f and a value x, and returns f of f of x. Then write a function that adds three. Call apply twice with it, and ten. You should see sixteen. Share your solution in the comments below.", "APPLY A FUNCTION TWICE", "Try passing functions."),
    ],
))

EPISODES.append(dict(
    n=50, title="Mini project: Calculator", spoken="the calculator mini project",
    yt="Python Mini Project: Build a Calculator", thumb="BUILD A CALCULATOR",
    vis="Xecxec pressing buttons on a big calculator with claws",
    goals=["structure a program with a function and a loop", "dispatch operations with if/elif or a dictionary", "handle division by zero"],
    tags=["python calculator", "python mini project", "python functions project", "zerodivisionerror"],
    hash=["#project", "#calculator"],
    analogy="a shop counter: the customer says what they want, and the shopkeeper picks the right action",
    c_title="Planning the calculator",
    c_pts=["A calculate function does one job: a op b", "A loop asks for a calculation until q", "Division by zero is checked, not allowed to crash"],
    intro="Time for the project that closes the functions module. Today we build a calculator.",
    concept="Here is the plan. One function, calculate, takes two numbers and an operator, and returns the answer. A loop asks the user for a calculation, until they type q. The input is a single line like six star seven, which we split into three parts. We convert the numbers to floats. And we guard against dividing by zero. Small functions, a loop, and decisions, working together.",
    A=dict(file="calc.py", label="The calculator", on="calculate() plus a loop that reads lines like 6 * 7",
           src='''
def calculate(a, op, b):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        return a / b
    else:
        return None

while True:
    choice = input("a op b (or q): ")
    if choice == "q":
        break
    a, op, b = choice.split()
    print(calculate(float(a), op, float(b)))
''',
           stdin="6 * 7\n9 / 3\nq\n",
           narr="[HL 1] The function takes two numbers and an operator. [HL 2] If the operator is plus, [HL 3] return the sum. [HL 4] Else if minus, [HL 5] the difference. [HL 6] Star, [HL 7] the product. [HL 8] Slash, [HL 9] the quotient. [HL 10] Anything else, [HL 11] returns None. [HL 13] A loop that runs until we break. [HL 14] Ask for a line. [HL 15] If it is q, [HL 16] leave the loop. [HL 17] Split the line into three parts and unpack them. [HL 18] Convert the numbers to floats, call calculate, and print the answer."),
    c2=dict(label="Program structure", on="Boxes: input line, split, calculate(a, op, b), print; an arrow loops back until q", narr="Here is the structure. The loop asks for a line. Split cuts it into three parts. Calculate does the real work. Print shows the answer. Then back to the top, until the user types q. Notice how the pieces are separate. The function knows nothing about input and output. That makes it easy to test, and easy to reuse.", anim=CALL),
    B=dict(file="dispatch.py", label="A dictionary of functions", on="operators mapped to lambdas",
           src='''
ops = {"+": lambda a, b: a + b, "*": lambda a, b: a * b}
print(ops["+"](2, 3))
print(ops["*"](4, 5))
''',
           narr="[HL 1] A dictionary. Each key is an operator, and each value is a lambda that does the job. This replaces the if and elif ladder. [HL 2] Look up the plus key, and call the lambda that comes back, with two and three. Five. [HL 3] The star key, with four and five. Twenty. Adding a new operator now means adding one line to the dictionary."),
    term="Forty two point zero, then three point zero.",
    recap=["Put the real work in a small function.", "A loop with break handles repeated input.", "A dictionary of functions can replace a long if and elif ladder.", "Check for a zero divisor before you divide."],
    bug=dict(title="dividing by zero", file="calc.py", wrong='''
print(10 / 0)
''', fixed='''
b = 0
if b != 0:
    print(10 / b)
else:
    print("Cannot divide by zero")
''', wrong_note="the divisor is zero", fixed_note="check the divisor first",
             why="Division by zero is undefined, so Python raises a ZeroDivisionError; test the divisor before you divide.",
             narr="Bug of the Day. We divide ten by zero. Python says, zero division error, division by zero. Maths has no answer, so Python stops. In the calculator, a user can type any numbers, so we must guard. Check that the divisor is not zero, and print a friendly message otherwise."),
    pun="Why did the calculator go to the beach? It wanted to add some sun.",
    task="add a power operator", challenge="Add an operator ** to the calculator that returns a ** b, and test it with 2 ** 8.",
    answer="Add elif op == \"**\": return a ** b. Typing 2 ** 8 prints 256.0.",
    shorts=[
        ("Calculator plan", "Let us build a calculator. One function, calculate, takes two numbers and an operator, and returns the answer. A loop asks the user for a line like six star seven, until they type q. We split the line, convert the numbers, call the function, and print the result. Small pieces that each do one job, working together.", "BUILD A CALCULATOR", "Our functions project."),
        ("One job per function", "Keep the calculate function pure. It takes values in, and returns a value out. It does not ask for input, and it does not print. That makes it easy to test, and easy to reuse. The loop handles the talking to the user. Calculate only does maths. Separate the jobs, and your programs stay clear as they grow.", "CALCULATE(A, OP, B)", "Keep functions focused."),
        ("A dictionary of functions", "A long if and elif ladder can become a dictionary. Each key is an operator, and each value is a lambda that does the job. Ops, bracket plus, close bracket, open bracket, two, three, close bracket, gives five. Adding a new operator means adding one line. Functions are values, so a dictionary can hold them, like anything else.", "OPS[\"+\"](2, 3)", "Functions in a dictionary."),
        ("Zero division", "Every calculator needs this guard. Ten divided by zero has no answer. Python raises a zero division error, division by zero, and your program stops. The user typed the numbers, so you must expect zero. Check that the divisor is not zero, before you divide. Print a friendly message instead. Defensive code keeps programs running.", "ZERODIVISIONERROR", "Guard the divisor."),
        ("Pun and challenge", "Why did the calculator go to the beach? It wanted to add some sun. Your challenge. Add a new operator to the calculator, double star, which raises the first number to the power of the second. Test it with two double star eight. You should see two fifty six point zero. Remember to add a new branch to the ladder. Share your code below.", "ADD A POWER OPERATOR", "Extend the calculator."),
    ],
))
