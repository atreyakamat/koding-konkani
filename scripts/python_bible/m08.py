"""Module 8 — Iterators, generators, decorators, typing, testing (EP 73-80)."""

MODULE = {"id": 8, "name": "Iterators, generators, decorators", "range": "73–80", "colours": "Lilac + DarkBlue"}
EPISODES = []
NEXT_AFTER = ("Next: EP 81 · Dates and times", "Module eight is done! Next time: dates and times, and the standard library.")

EPISODES.append(dict(
    n=73, title="Iterators", spoken="iterators",
    yt="Python Iterators: How a for Loop Really Works", thumb="ITERATORS",
    vis="Xecxec pulling beach balls one by one out of a tube",
    goals=["explain what iter() and next() do", "see how a for loop uses an iterator", "write a class with __iter__ and __next__"],
    tags=["python iterators", "python iter next", "python stopiteration", "how for loop works python"],
    hash=["#python", "#iterators"],
    analogy="a ticket machine: each press gives you the next ticket, until the roll is empty",
    c_title="One at a time",
    c_pts=["iter(x) gives an iterator", "next(it) gives the next item", "StopIteration means: no more"],
    intro="Every for loop you have written secretly uses an iterator. Today we open the box.",
    concept="An iterable is anything you can loop over, such as a list or a string. The iter function turns it into an iterator, which hands out items one at a time. Each call to next gives the next item. When there are no more, Python raises a StopIteration, and the for loop quietly stops. Think of a ticket machine. Each press gives you the next ticket, until the roll is empty. And once the roll is empty, it stays empty.",
    A=dict(file="manual.py", label="A for loop by hand", on="iter and next, one step at a time",
           src='''
nums = [10, 20, 30]
it = iter(nums)
print(next(it))
print(next(it))
print(next(it))
try:
    print(next(it))
except StopIteration:
    print("no more")
''',
           narr="[HL 1] A list of three numbers. [HL 2] The iter function gives us an iterator, tied to it. [HL 3] Next gives the first item. Ten. [HL 4] The second. Twenty. [HL 5] The third. Thirty. [HL 6] Now the roll is empty. [HL 7] Next raises a StopIteration. [HL 8] We catch it, and print, no more. A for loop does exactly this, and catches the StopIteration for you."),
    mem=dict(label="The list and its iterator", on="The name nums tied to a list; the name it tied to a separate list iterator that remembers its place", names=["nums", "it"], **{"from": "A"},
             narr="Here is the picture. The name nums is tied to the list. The name it is tied to a different object, a list iterator. The iterator does not copy the list. It points at it, and remembers how far it has walked. The list stays the same. Only the iterator moves forward."),
    B=dict(file="countdown.py", label="Our own iterator", on="a class with __iter__ and __next__",
           src='''
class Countdown:
    def __init__(self, start):
        self.n = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.n <= 0:
            raise StopIteration
        value = self.n
        self.n -= 1
        return value

for i in Countdown(3):
    print(i)
print(list(Countdown(5)))
''',
           narr="[HL 1] A Countdown class. [HL 2] Init remembers where to start. [HL 5] Dunder iter returns the iterator. Here, the object itself. [HL 8] Dunder next hands out the next value. [HL 9] When we reach zero, [HL 10] raise StopIteration. [HL 11] Otherwise, keep the current value. [HL 12] Count down by one. [HL 13] And return it. [HL 15] A for loop uses the class like a list. [HL 16] Three, two, one. [HL 17] List can also consume an iterator. Five, four, three, two, one."),
    term="10, 20, 30, no more. Then 3, 2, 1, and the list 5 to 1.",
    recap=["iter(x) gives an iterator; next(it) gives the next item.", "StopIteration means there is nothing left.", "A for loop calls iter once, then next again and again.", "Your own class needs __iter__ and __next__."],
    bug=dict(title="an iterator is used up after one loop", kind="output", file="once.py", wrong='''
it = iter([1, 2, 3])
print(sum(it))
print(sum(it))
''', fixed='''
nums = [1, 2, 3]
print(sum(nums))
print(sum(nums))
''', wrong_note="the second sum gets an empty iterator", fixed_note="a list can be looped again and again",
             why="An iterator walks forward once and never rewinds. After the first loop it is empty. A list creates a fresh iterator every time you loop over it.",
             narr="Bug of the Day. We sum the iterator twice. The first sum gives six. The second gives zero, with no error. The iterator was used up by the first sum. It never rewinds. Keep the data in a list, and every loop gets a fresh iterator. Or call iter again."),
    pun="Why did the iterator go home early? It had nothing next to do.",
    task="walk a string", challenge="Use iter and next on the string \"abc\", and print each letter. Catch the StopIteration after the third.",
    answer="it = iter(\"abc\"); print(next(it)) three times; then try: next(it) except StopIteration: print(\"done\").",
    shorts=[
        ("iter and next", "Every for loop secretly uses an iterator. Call iter on a list to get one. Each call to next gives the next item. Ten, twenty, thirty. A ticket machine, pressing once for each ticket.", "next(it) -> next item", "Iterators give one at a time."),
        ("StopIteration", "When an iterator has nothing left, next raises StopIteration. A for loop catches it quietly, and ends. That is how a for loop knows when to stop. You can catch it yourself with try and except.", "StopIteration = no more", "That is how loops end."),
        ("Your own iterator", "To build your own iterator, write a class with two methods. Dunder iter returns the iterator, usually self. Dunder next returns the next value, or raises StopIteration. Now your object works in a for loop, like a list.", "__iter__ and __next__", "Two methods make an iterator."),
        ("Used up", "A sneaky bug. You sum an iterator twice. The first sum is six. The second is zero, with no error. An iterator walks forward once, and never rewinds. Keep a list, and each loop starts fresh.", "second sum = 0", "Iterators never rewind."),
        ("Pun and challenge", "Why did the iterator go home early? It had nothing next to do. Your challenge. Use iter and next on the string abc. Print each letter, then catch the StopIteration after the third. Which three letters do you see?", "Challenge: walk a string", "Use iter and next."),
    ],
))

EPISODES.append(dict(
    n=74, title="Generators", spoken="generators",
    yt="Python Generators and yield Explained", thumb="YIELD",
    vis="Xecxec handing out one cookie at a time from a never-ending conveyor belt",
    goals=["write a generator function with yield", "see that a generator runs lazily", "know that a generator can be used only once"],
    tags=["python generators", "python yield", "python generator function", "generator vs list python"],
    hash=["#python", "#generators"],
    analogy="a conveyor belt that makes the next cookie only when you reach for it",
    c_title="Pause and resume",
    c_pts=["yield hands out a value and pauses", "The function resumes where it stopped", "Values are made one at a time"],
    intro="Writing a whole iterator class is long. A generator does the same job in a few lines.",
    concept="A generator is a function that uses yield instead of return. Calling it does not run the body. It gives back a generator object. Each time you ask for the next value, the function runs to the next yield. It hands the value out, and pauses. The next request resumes right after the yield. Nothing is stored in a big list, so a generator can even be endless. Think of a conveyor belt that makes the next cookie only when you reach for it.",
    A=dict(file="gen.py", label="A generator function", on="yield pauses the function",
           src='''
def countdown(n):
    print("start")
    while n > 0:
        yield n
        n -= 1
    print("done")

g = countdown(3)
print("made it")
print(next(g))
print(next(g))
for x in g:
    print(x)
''',
           narr="[HL 1] A function with yield. [HL 2] This print only runs when we first ask. [HL 3] Loop while n is above zero. [HL 4] Yield hands out n, and pauses here. [HL 5] When resumed, count down. [HL 6] After the loop, print done. [HL 8] Calling countdown runs nothing yet. We only get a generator object. [HL 9] Made it. Nothing has started. [HL 10] The first next runs the body. Start. Then yield three. [HL 11] The second next resumes after the yield. Two. [HL 12] A for loop takes the rest. [HL 13] One. Then done, and the loop ends."),
    c2=dict(label="Pause and resume", on="A function box with a bookmark at the yield line; each next moves the bookmark forward", narr="Here is the picture. A generator keeps a bookmark at the yield line. Each next call resumes from the bookmark. It runs to the next yield, hands out a value, and places the bookmark again. All local variables stay alive between calls. When the function ends, the bookmark is gone, and the generator raises StopIteration.", anim="A function box with a bookmark at the yield line; each next call hops the bookmark one step and ejects a value ticket"),
    B=dict(file="squares.py", label="Lazy and endless", on="a generator that never ends, and a take-three loop",
           src='''
def naturals():
    n = 1
    while True:
        yield n
        n += 1

def squares(limit):
    for n in naturals():
        if n > limit:
            return
        yield n * n

print(list(squares(5)))
print(sum(squares(10)))
''',
           narr="[HL 1] A generator that never ends. [HL 2] Start at one. [HL 3] Forever. [HL 4] Yield the number. [HL 5] Then add one. [HL 7] A second generator, built on the first. [HL 8] It pulls numbers one at a time. [HL 9] Past the limit, [HL 10] return, and the generator ends. [HL 11] Otherwise yield the square. [HL 13] The squares up to five. One, four, nine, sixteen, twenty five. [HL 14] The sum of squares up to ten. Three eighty five. The endless generator never filled memory, because values were made only when asked."),
    term="Made it, start, 3, 2, then 1, done. Then the five squares, then 385.",
    recap=["A function with yield returns a generator.", "Each next runs the function up to the next yield.", "Values are made one at a time, so memory stays small.", "A generator can be used only once."],
    bug=dict(title="a generator is used up after one loop", kind="output", file="once.py", wrong='''
def evens():
    for n in range(0, 6, 2):
        yield n

g = evens()
print(list(g))
print(list(g))
''', fixed='''
def evens():
    for n in range(0, 6, 2):
        yield n

print(list(evens()))
print(list(evens()))
''', wrong_note="the second list gets an exhausted generator", fixed_note="call evens() again for a fresh generator",
             why="A generator runs once. When it finishes, it stays empty. Call the generator function again to get a fresh one.",
             narr="Bug of the Day. We turn the same generator into a list twice. The first list is zero, two, four. The second list is empty, with no error. The generator was used up. To loop again, call evens again, and get a fresh generator."),
    pun="Why did the generator get tired? It kept giving without getting anything back.",
    task="generate evens", challenge="Write a generator evens(limit). It yields the even numbers from 0 up to limit. It includes limit if limit is even.",
    answer="def evens(limit): for n in range(0, limit + 1, 2): yield n.",
    shorts=[
        ("What is yield", "Yield works like return, but the function pauses instead of ending. It hands out one value, and waits. The next request resumes right after the yield. A function with yield is called a generator.", "yield = give and pause", "Yield pauses the function."),
        ("Lazy values", "A generator makes values only when you ask. A list of a million numbers fills memory. A generator of a million numbers holds just one at a time. It is a conveyor belt that makes the next cookie on demand.", "one value at a time", "Generators are lazy."),
        ("Endless generator", "A generator can even be endless. A while True loop with a yield gives you one, two, three, forever. It never fills memory, because nothing is stored. You just stop asking when you have enough.", "while True: yield n", "Endless, yet tiny."),
        ("Used up", "A classic bug. You make a list from the same generator twice. The first list is full. The second is empty, and no error appears. A generator runs once. To go again, call the generator function again.", "second list = []", "Generators run once."),
        ("Pun and challenge", "Why did the generator get tired? It kept giving without getting anything back. Your challenge. Write a generator called evens. It takes a limit, and yields every even number from zero up to the limit. Print the list for limit ten.", "Challenge: evens(limit)", "Write an evens generator."),
    ],
))

EPISODES.append(dict(
    n=75, title="Generator expressions", spoken="generator expressions",
    yt="Python Generator Expressions Explained", thumb="GENEXPR",
    vis="Xecxec with a tiny conveyor belt built from round brackets",
    goals=["write a generator expression", "use it with sum, any and all", "tell round brackets from square brackets"],
    tags=["python generator expression", "python genexpr", "python sum generator", "list comprehension vs generator"],
    hash=["#python", "#generators"],
    analogy="a list comprehension with its coat swapped: same recipe, but cooked one dish at a time",
    c_title="Brackets decide",
    c_pts=["[x for ...] builds a whole list", "(x for ...) makes values on demand", "sum, any, all, max accept generators"],
    intro="A list comprehension builds everything at once. Swap the square brackets for round ones, and it becomes lazy.",
    concept="A generator expression looks like a list comprehension, but with round brackets. Instead of building the whole list, it makes values one at a time, as they are needed. Functions that read a sequence once, such as sum, max, any and all, work perfectly with it. When it is the only argument, you can even drop the extra brackets. Think of a list comprehension with its coat swapped. Same recipe, but cooked one dish at a time.",
    A=dict(file="genexpr.py", label="Round brackets", on="the same recipe, list versus generator",
           src='''
nums = [1, 2, 3, 4, 5]
squares_list = [n * n for n in nums]
squares_gen = (n * n for n in nums)
print(squares_list)
print(sum(squares_gen))
print(sum(n * n for n in nums if n % 2 == 1))
print(max(len(w) for w in ["sun", "beach", "sea"]))
''',
           narr="[HL 1] A list of five numbers. [HL 2] Square brackets build the whole list at once. [HL 3] Round brackets build nothing yet. We get a generator. [HL 4] The list prints one, four, nine, sixteen, twenty five. [HL 5] Sum pulls values from the generator, one at a time. Fifty five. [HL 6] As the only argument, we can drop the extra brackets. Only the odd numbers, squared and added. Thirty five. [HL 7] The longest word length. Five."),
    c2=dict(label="List versus generator", on="A full shelf of boxes next to a single box passing along a belt", narr="Here is the difference. A list comprehension fills a whole shelf with finished results, and holds them all in memory. A generator expression keeps a single box on a belt, and makes the next result only when you ask. For small data, either works. For a big or endless source, the generator saves memory, and can start working at once.", anim="A shelf of five filled boxes beside a belt where one box is made at a time and passed to a sum meter"),
    B=dict(file="anyall.py", label="Early stopping", on="any and all stop as soon as the answer is known",
           src='''
words = ["sun", "beach", "sea", "crab"]
print(any(w.startswith("c") for w in words))
print(all(len(w) > 3 for w in words))
first = next((w for w in words if len(w) == 5), None)
print(first)
total = sum(len(w) for w in words)
print(total)
''',
           narr="[HL 1] Four words. [HL 2] Any asks, does at least one word start with c? Crab does. True, and it stops looking there. [HL 3] All asks, is every word longer than three? Sun is not. False, and it stops at once. [HL 4] Next with a generator finds the first match, and gives None if there is none. [HL 5] The first word of length five. Beach. [HL 6] Sum adds the lengths. [HL 7] Fifteen."),
    term="The list of squares, then 55, 35, 5. Then True, False, beach, 15.",
    recap=["Round brackets make a generator expression.", "It produces values one at a time, on demand.", "sum, max, any and all accept it directly.", "Square brackets build the whole list at once."],
    bug=dict(title="printing the generator object", kind="output", file="show.py", wrong='''
squares = (n * n for n in range(4))
print(squares)
''', fixed='''
squares = (n * n for n in range(4))
print(list(squares))
''', wrong_note="print shows the generator, not its values", fixed_note="list() asks for all the values",
             why="A generator holds a recipe, not the values. To see them, loop over it, or pass it to list, sum, or another function that reads it.",
             narr="Bug of the Day. We print the generator, and see generator object genexpr at a memory address. It holds the recipe, not the values. To see the values, ask for them. Wrap it in list, or loop over it. Remember, doing that uses it up."),
    pun="Why did the list comprehension envy the generator expression? It was so much lighter.",
    task="total with a genexpr", challenge="Use a generator expression with sum to add the squares of the even numbers from 1 to 10.",
    answer="sum(n * n for n in range(1, 11) if n % 2 == 0), which is 220.",
    shorts=[
        ("Round brackets", "Take a list comprehension, and swap the square brackets for round ones. You get a generator expression. It builds nothing up front. It makes each value only when something asks for it. Same recipe, cooked one dish at a time.", "(n * n for n in nums)", "Round brackets are lazy."),
        ("Sum a generator", "Sum, max, min, any and all can read a generator directly. Write sum of n times n for n in nums. When it is the only argument, you can skip the extra brackets. No list is ever built in memory.", "sum(n * n for n in nums)", "No list needed."),
        ("any and all", "Any is True as soon as one item matches. All is False as soon as one item fails. With a generator, they stop looking right there. For a million words, that saves much time.", "any(...) stops early", "Stop as soon as you know."),
        ("Printing a generator", "Print a generator, and you see generator object genexpr at an address. That is not a bug in Python. A generator holds a recipe, not the values. Wrap it in list to see the values, or loop over it.", "<generator object ...>", "Use list to see values."),
        ("Pun and challenge", "Why did the list comprehension envy the generator expression? It was so much lighter. Your challenge. Use a generator expression with sum to add the squares of all the even numbers from one to ten. What total do you get?", "Challenge: sum of even squares", "Use sum and a genexpr."),
    ],
))

EPISODES.append(dict(
    n=76, title="Decorators", spoken="decorators",
    yt="Python Decorators Explained Simply", thumb="@DECORATORS",
    vis="Xecxec wrapping a gift function in shiny paper",
    goals=["write a simple decorator", "use the @ syntax", "keep the function's name with functools.wraps"],
    tags=["python decorators", "python @ decorator", "python functools wraps", "python wrapper function"],
    hash=["#python", "#decorators"],
    analogy="gift wrap: the gift is the same, but the wrapper adds something before and after",
    c_title="Wrap a function",
    c_pts=["A decorator takes a function and returns a new one", "@name above def applies it", "functools.wraps keeps the original name"],
    intro="Want to add logging to ten functions without touching their code? Wrap them.",
    concept="A decorator is a function that takes a function, and returns a new function that wraps it. The wrapper can do something before, call the original, and do something after. The at sign is a shortcut. Writing at shout above a def means, after defining the function, replace it with shout of that function. Think of gift wrap. The gift is the same, but the wrapper adds something before and after. Use functools dot wraps to keep the original name.",
    A=dict(file="shout.py", label="A first decorator", on="a decorator that wraps a function",
           src='''
def shout(func):
    def wrapper():
        print("before")
        func()
        print("after")
    return wrapper

@shout
def hello():
    print("Hello")

hello()
''',
           narr="[HL 1] A decorator takes a function, called func. [HL 2] Inside, a new function, the wrapper. [HL 3] First it prints before. [HL 4] Then it calls the original. [HL 5] Then it prints after. [HL 6] The decorator returns the wrapper, not the result. [HL 8] The at sign applies shout to the function below. [HL 9] This is hello. [HL 10] It prints Hello. [HL 12] Calling hello now really calls the wrapper. Before, Hello, after."),
    c2=dict(label="Gift wrap", on="The name hello tied first to the original function; after the decorator, tied to the wrapper that holds the original", narr="Here is what the at sign does. First, Python defines hello normally. Then it calls shout with that function, and ties the name hello to whatever comes back. That is the wrapper. The original function is still alive, kept inside the wrapper, and called from there. So hello is no longer the original. It is the gift wrap, with the gift inside.", anim="A function box labelled hello is placed inside a wrapper box, and the label hello jumps to the outer box"),
    B=dict(file="timer.py", label="Arguments and wraps", on="a decorator that accepts any arguments and keeps the name",
           src='''
import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(func.__name__, args, "->", result)
        return result
    return wrapper

@log
def add(a, b):
    return a + b

print(add(2, 3))
print(add.__name__)
''',
           narr="[HL 1] We need functools. [HL 3] A decorator named log. [HL 4] Wraps copies the original name and notes onto the wrapper. [HL 5] The wrapper accepts any arguments. [HL 6] Call the original, and keep the result. [HL 7] Print the name, the arguments, and the result. [HL 8] And return the result, so callers still get it. [HL 9] Return the wrapper. [HL 11] Apply log to add. [HL 12] A plain add function. [HL 15] Add two and three. The log prints, add, two three, arrow, five. Then print shows five. [HL 16] And the name is still add, thanks to wraps."),
    term="Before, Hello, after. Then the log line, 5, and add.",
    recap=["A decorator takes a function and returns a new one.", "@name above def means: f = name(f).", "The wrapper uses *args and **kwargs to accept anything.", "functools.wraps keeps the original name."],
    bug=dict(title="the wrapper loses the function name", kind="output", file="names.py", wrong='''
def shout(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@shout
def hello():
    "Say hello"

print(hello.__name__)
print(hello.__doc__)
''', fixed='''
import functools

def shout(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@shout
def hello():
    "Say hello"

print(hello.__name__)
print(hello.__doc__)
''', wrong_note="hello is now called wrapper", fixed_note="wraps copies the name and doc",
             why="The decorated name points at the wrapper, so it reports the wrapper's name and no docstring. functools.wraps copies those details across.",
             narr="Bug of the Day. After decoration, the name hello points at the wrapper. So dunder name says wrapper, and the doc string is gone. Tools and error messages show the wrong name. Add functools dot wraps above the wrapper, and the original name and notes are copied across."),
    pun="Why was the function so well dressed? It had a great decorator.",
    task="count the calls", challenge="Write a decorator count_calls. It counts how many times a function is called. It stores the count in wrapper.calls.",
    answer="Define wrapper(*args, **kwargs): wrapper.calls += 1; return func(*args, **kwargs). Set wrapper.calls = 0 before returning wrapper.",
    shorts=[
        ("What is a decorator", "A decorator is a function that takes a function, and returns a new one that wraps it. The wrapper can act before and after the original. Think of gift wrap. The gift is the same, with something added around it.", "func in, wrapper out", "Decorators wrap functions."),
        ("The at sign", "The at sign is a shortcut. Writing at shout above def hello means, after defining hello, replace it with shout of hello. The name hello now points at the wrapper. The original is kept safe inside it.", "@shout = hello = shout(hello)", "At means wrap it."),
        ("Any arguments", "A good wrapper accepts any arguments. Use star args and star star kwargs, and pass them on to the original. Return the original's result too. Now the same decorator works on functions of any shape.", "wrapper(*args, **kwargs)", "Accept anything."),
        ("Lost name", "A sneaky bug. After decoration, hello dot name says wrapper, and the doc string is gone. The name points at the wrapper. Add functools dot wraps above the wrapper, and the original name and notes are copied across.", "hello.__name__ == 'wrapper'", "Use functools.wraps."),
        ("Pun and challenge", "Why was the function so well dressed? It had a great decorator. Your challenge. Write a decorator called count calls. It counts how many times a function was called, and stores the count on the wrapper. Call the function three times.", "Challenge: count_calls", "Count the calls."),
    ],
))

EPISODES.append(dict(
    n=77, title="Decorators with arguments", spoken="decorators with arguments",
    yt="Python Decorators with Arguments Explained", thumb="@REPEAT(3)",
    vis="Xecxec turning a dial on a gift-wrap machine: wrap three times",
    goals=["write a decorator that takes its own arguments", "understand the three levels of nesting", "use functools.wraps in a decorator factory"],
    tags=["python decorator arguments", "python decorator factory", "python nested functions decorator", "python @repeat"],
    hash=["#python", "#decorators"],
    analogy="a wrapping machine with a dial: first you set the dial, then it takes a gift, then it wraps",
    c_title="Three levels",
    c_pts=["Outer function takes the decorator's settings", "Middle function takes the function to wrap", "Inner function is the wrapper that runs"],
    intro="What if the decorator needs a setting, such as how many times to repeat? We add one more level.",
    concept="A decorator with arguments is a function that returns a decorator. So there are three levels. The outer function takes the settings, such as times. It returns the middle function, which is the real decorator, and takes the function to wrap. That returns the inner wrapper, which runs each time. When you write at repeat of three, Python first calls repeat with three, gets the decorator, and applies it. Think of a wrapping machine with a dial. First you set the dial. Then you hand over the gift.",
    A=dict(file="repeat.py", label="A decorator that takes a number", on="repeat a function a chosen number of times",
           src='''
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def hello(name):
    print("Hello", name)

hello("Asha")
''',
           narr="[HL 1] The outer function takes the setting, times. [HL 2] The middle function is the real decorator. It takes the function. [HL 3] The inner wrapper accepts any arguments. [HL 4] It loops times times. [HL 5] And calls the original each time. [HL 6] The middle function returns the wrapper. [HL 7] The outer function returns the decorator. [HL 9] At repeat of three. Python calls repeat with three first, and then applies the result to hello. [HL 10] The function. [HL 11] It prints hello and a name. [HL 13] One call, and we see Hello Asha three times."),
    c2=dict(label="Dial first, gift second", on="A machine with a dial set to 3, then a gift function inserted, then the wrapped gift comes out", narr="Here is the order of events. First, repeat is called with three. That sets the dial, and returns the decorator. Second, that decorator is called with the function hello. That returns the wrapper. Finally, the name hello is tied to the wrapper. Three levels, three steps, always in that order. If you ever lose track, count the brackets in the at line.", anim="A machine with a dial turned to 3; a function enters on a belt, passes through, and leaves wrapped, with the label hello jumping onto it"),
    B=dict(file="require.py", label="A decorator with a password", on="allow only one role to call a function",
           src='''
import functools

def require(role):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(user, *args, **kwargs):
            if user != role:
                return "denied"
            return func(user, *args, **kwargs)
        return wrapper
    return decorator

@require("admin")
def delete_all(user):
    return "deleted"

print(delete_all("admin"))
print(delete_all("guest"))
print(delete_all.__name__)
''',
           narr="[HL 3] The outer function takes the required role. [HL 4] The middle function takes the function. [HL 5] Wraps keeps the original name. [HL 6] The wrapper takes the user first. [HL 7] If the user is not the required role, [HL 8] return denied, and never call the function. [HL 9] Otherwise call it. [HL 10] Return the wrapper. [HL 11] And return the decorator. [HL 13] Require the admin role. [HL 14] The protected function. [HL 15] It returns deleted. [HL 17] The admin gets deleted. [HL 18] The guest gets denied. [HL 19] And the name is still delete all."),
    term="Hello Asha three times. Then deleted, denied, delete_all.",
    recap=["A decorator with arguments has three levels of functions.", "Outer takes the settings and returns the decorator.", "The decorator takes the function and returns the wrapper.", "@repeat(3) first calls repeat(3), then applies the result."],
    bug=dict(title="one level of nesting is missing", file="repeat.py", wrong='''
def repeat(times):
    def wrapper(*args, **kwargs):
        for _ in range(times):
            func(*args, **kwargs)
    return wrapper

@repeat(3)
def hello():
    print("Hello")
''', fixed='''
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def hello():
    print("Hello")

hello()
''', wrong_note="repeat returns the wrapper, not a decorator", fixed_note="the decorator level is added",
             why="At repeat of three calls repeat, and then calls the result with the function. If repeat returns the wrapper directly, the wrapper runs at once, and has no func to call.",
             narr="Bug of the Day. Repeat returns the wrapper directly. But at repeat of three means, call repeat, then call the result with hello. So the wrapper runs immediately, with hello as an argument, and looks for func. Name error, name func is not defined. Add the middle level, a decorator function that takes func."),
    pun="Why did the decorator need three levels? It was a big fan of nesting.",
    task="shout n times", challenge="Write a decorator shout(n) that prints the function's result in capital letters n times.",
    answer="def shout(n): def decorator(func): def wrapper(*a, **k): for _ in range(n): print(func(*a, **k).upper()); return wrapper; return decorator.",
    shorts=[
        ("Why three levels", "A decorator with arguments has three levels. The outer function takes the setting. It returns the decorator. The decorator takes the function, and returns the wrapper. Setting first, function second, wrapper last.", "outer -> decorator -> wrapper", "Three levels, in order."),
        ("What the at line does", "When you write at repeat of three, Python first calls repeat with three. That returns a decorator. Then Python calls that decorator with your function. So the brackets in the at line tell you there is an extra level.", "@repeat(3) = repeat(3)(func)", "Brackets mean an extra level."),
        ("Keep the name", "Do not forget functools dot wraps. Put it above the inner wrapper, even in a decorator with arguments. Then the decorated function keeps its name and its doc string. Tools and error messages then show the right name.", "@functools.wraps(func)", "Always use wraps."),
        ("Missing level", "A bug that confuses everyone. Repeat returns the wrapper directly. At repeat of three then calls the wrapper with hello, and Python says, name error, name func is not defined. Add the middle level that takes func.", "NameError: name 'func'", "Add the middle level."),
        ("Pun and challenge", "Why did the decorator need three levels? It was a big fan of nesting. Your challenge. Write a decorator called shout that takes a number n. It prints the function's result in capital letters, n times. Try it with a greeting function.", "Challenge: @shout(2)", "Write @shout(n)."),
    ],
))

EPISODES.append(dict(
    n=78, title="Context managers", spoken="context managers",
    yt="Python Context Managers and the with Statement", thumb="WITH + ENTER/EXIT",
    vis="Xecxec opening and closing a door around a tiny room, with a bell at each end",
    goals=["explain what with really does", "write __enter__ and __exit__", "use contextlib.contextmanager"],
    tags=["python context manager", "python with statement", "python __enter__ __exit__", "python contextlib"],
    hash=["#python", "#with"],
    analogy="a hotel room: the key card opens the door on the way in, and the room is cleaned on the way out, whatever happened inside",
    c_title="Set up and tidy up",
    c_pts=["__enter__ runs when the with block starts", "__exit__ runs when the block ends, even on error", "@contextmanager makes one from a generator"],
    intro="You have used with for files. Today we learn what happens behind it, and build our own.",
    concept="A with statement guarantees a cleanup. Behind it, Python calls two special methods. Dunder enter runs at the start, and its return value is tied to the name after as. Dunder exit runs at the end, even if an error happened inside. If exit returns True, the error is swallowed. If it returns False, the error continues. The contextlib module offers a shortcut, with a generator and one yield. Think of a hotel room. The key card opens the door on the way in, and the room is cleaned on the way out.",
    A=dict(file="section.py", label="Enter and exit", on="a class that prints when it starts and ends",
           src='''
class Section:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print("enter", self.name)
        return self

    def __exit__(self, exc_type, exc, tb):
        print("exit", self.name)
        return False

with Section("A") as s:
    print("inside", s.name)
print("after")
''',
           narr="[HL 1] A Section class. [HL 2] Init stores a name. [HL 5] Dunder enter runs when the with block starts. [HL 6] It prints enter. [HL 7] And returns self, which is tied to the name after as. [HL 9] Dunder exit runs when the block ends. The three extra values describe any error. [HL 10] It prints exit. [HL 11] False means, do not hide any error. [HL 13] The with statement. Enter runs first. [HL 14] Then the block, inside A. Then exit runs. [HL 15] And the program goes on. After."),
    c2=dict(label="Door in, door out", on="A room with an entry door that rings a bell and an exit door that cleans the room, even when a red error arrow appears inside", narr="Here is the picture. The with statement walks through the entry door, which calls enter. Your block runs inside the room. When the block ends, normal or with an error, Python always walks through the exit door, and calls exit. That is why with is trusted for files. Even if the code inside crashes, the file is closed on the way out.", anim="A room with two doors; a bell rings at the entry door, a cleaner at the exit door; a red lightning arrow inside still ends at the exit door"),
    B=dict(file="tag.py", label="The contextmanager shortcut", on="a generator with one yield does the same job",
           src='''
from contextlib import contextmanager

@contextmanager
def tag(name):
    print("<" + name + ">")
    try:
        yield
    finally:
        print("</" + name + ">")

with tag("b"):
    print("bold text")
try:
    with tag("i"):
        raise ValueError("oops")
except ValueError as e:
    print("caught", e)
''',
           narr="[HL 1] Import the shortcut. [HL 3] The decorator turns a generator into a context manager. [HL 4] A function named tag. [HL 5] Everything before the yield is the enter part. [HL 6] Try. [HL 7] The yield marks the block of the with statement. [HL 8] Finally, [HL 9] runs on the way out, even after an error. [HL 11] The first with. [HL 12] The bold text, between the tags. [HL 13] Now a block that fails. [HL 14] The tags still open. [HL 15] The error is raised inside. [HL 16] The closing tag still prints, and the error continues. [HL 17] Where we catch it. Caught oops."),
    term="Enter A, inside A, exit A, after. Then the bold tags, then the italic tags, and caught oops.",
    recap=["with calls __enter__ at the start and __exit__ at the end.", "__exit__ runs even when the block raises an error.", "Returning True from __exit__ swallows the error.", "@contextmanager builds one from a generator with one yield."],
    bug=dict(title="__exit__ swallows the error", kind="output", file="quiet.py", wrong='''
class Quiet:
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        return True

with Quiet():
    1 / 0
print("finished")
''', fixed='''
class Quiet:
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        return False

try:
    with Quiet():
        1 / 0
except ZeroDivisionError:
    print("error visible")
print("finished")
''', wrong_note="the ZeroDivisionError vanished", fixed_note="exit returns False; the caller sees the error",
             why="If exit returns True, Python treats the error as handled and hides it. Return False, or return nothing, so errors are never swallowed by accident.",
             narr="Bug of the Day. The block divides by zero. But our exit returns True. That tells Python, I handled it. The error vanishes, and the program prints finished. A real bug is now invisible. Return False, or nothing at all, and the error continues up to where you can catch it."),
    pun="Why did the context manager never forget anything? It always cleaned up after itself.",
    task="time a block", challenge="Write a context manager class Banner that prints a line of dashes on enter, and another on exit.",
    answer="def __enter__(self): print(\"-----\"); return self. def __exit__(self, *a): print(\"-----\"); return False.",
    shorts=[
        ("What with does", "The with statement guarantees a cleanup. Python calls dunder enter when the block starts. It calls dunder exit when the block ends, even if an error happened inside. That is why with is the safe way to open files.", "__enter__ / __exit__", "With always cleans up."),
        ("Write your own", "To write your own context manager, make a class with two methods. Enter does the setup. It returns the value that the name after as gets. Exit does the cleanup. Now with your class gives the same safety as with open.", "class with __enter__ and __exit__", "Make your own."),
        ("The shortcut", "The contextlib module has a shortcut. Write a generator with one yield, and add at contextmanager. Everything before the yield is the setup. Everything after it, in a finally block, is the cleanup. Short and tidy.", "@contextmanager + yield", "A shortcut with yield."),
        ("Swallowed error", "A dangerous bug. Dunder exit returns True. Python takes that to mean, I handled the error. Your divide by zero disappears, and the program says finished. Return False, or nothing, so errors are never swallowed by accident.", "return True hides errors", "Never swallow errors."),
        ("Pun and challenge", "Why did the context manager never forget anything? It always cleaned up after itself. Your challenge. Write a class called Banner. On enter, it prints a line of dashes. On exit, it prints another. Use it with a with statement.", "Challenge: Banner", "Write a Banner."),
    ],
))

EPISODES.append(dict(
    n=79, title="Type hints and dataclasses", spoken="type hints and dataclasses",
    yt="Python Type Hints and Dataclasses Explained", thumb="@DATACLASS",
    vis="Xecxec writing labels on boxes, then a machine that builds the class for him",
    goals=["add type hints to functions", "know that hints are not enforced at runtime", "write a dataclass and use default_factory"],
    tags=["python type hints", "python dataclass", "python default_factory", "python typing beginners"],
    hash=["#python", "#dataclass"],
    analogy="labels on jars: they tell everyone what belongs inside, but they do not stop you from putting something else in",
    c_title="Labels and shortcuts",
    c_pts=["name: type is a hint, not a rule", "@dataclass writes init, repr and eq for you", "Use field(default_factory=list) for lists"],
    intro="Hints make code easier to read. Dataclasses make small classes much shorter.",
    concept="A type hint is a label. Write a colon and a type after a parameter, and an arrow and a type for the return value. Hints help readers and editors, but Python does not enforce them when the program runs. Think of labels on jars. They tell everyone what belongs inside, but do not stop you putting something else in. A dataclass uses the same labels to write init, repr and eq for you. For a list field, you must use field with default factory, so every object gets its own list.",
    A=dict(file="hints.py", label="Hints are labels", on="type hints, and what happens with the wrong type",
           src='''
def area(width: float, height: float) -> float:
    return width * height

def greet(name: str, times: int = 1) -> str:
    return "-".join(["Hello " + name] * times)

print(area(3, 4.5))
print(greet("Asha", 2))
print(area("a", 3))
''',
           narr="[HL 1] Hints after each parameter, and an arrow with the return type. [HL 2] The body is the same as before. [HL 4] A string, an integer with a default, and a string back. [HL 5] The body builds the greeting. [HL 7] Three times four point five. Thirteen point five. [HL 8] Hello Asha, twice, joined with a dash. [HL 9] But what if we pass text? The hint says float, but Python does not check. The letter a, three times. The hints are labels, not locks. A tool called mypy can check them, before you run the program."),
    c2=dict(label="Labels, not locks", on="Jars with labels: a jar labelled int still accepts a string without complaint, but a checker tool flags it", narr="Here is the picture. Each parameter is a jar with a label. The label says what is supposed to go inside. At run time, Python does not read the labels. A string can go into a jar marked float, and the program carries on. Separate tools, such as mypy, and your editor, read the labels before the program runs, and warn you. That is the value of hints.", anim="Three jars labelled int, str, float; a string drops into the float jar without a sound; a magnifier tool marked mypy flags it in red"),
    B=dict(file="dc.py", label="A dataclass", on="the class writes itself from the labels",
           src='''
from dataclasses import dataclass, field

@dataclass
class Student:
    name: str
    marks: int = 0
    tags: list = field(default_factory=list)

a = Student("Asha", 91)
b = Student("Ravi")
a.tags.append("top")
print(a)
print(b)
print(a == Student("Asha", 91, ["top"]))
''',
           narr="[HL 1] Import dataclass and field. [HL 3] The dataclass decorator writes init, repr and eq for us. [HL 4] A normal looking class. [HL 5] A field with a type, and no default. [HL 6] A field with a default. [HL 7] A list field. Default factory builds a fresh list for every object. [HL 9] A student with a name and marks. [HL 10] A student with only a name. [HL 11] Add a tag to the first. [HL 12] Print shows all fields, with no repr written by us. [HL 13] Ravi has zero marks, and an empty list. [HL 14] And eq compares every field. True."),
    term="13.5, Hello Asha-Hello Asha, aaa. Then the two Student lines, and True.",
    recap=["Type hints are labels: name: str, and -> int.", "Python does not enforce hints; tools like mypy do.", "@dataclass writes init, repr and eq from the fields.", "Use field(default_factory=list) for a list field."],
    bug=dict(title="a mutable default in a dataclass", trim=1, file="team.py", wrong='''
from dataclasses import dataclass

@dataclass
class Team:
    members: list = []
''', fixed='''
from dataclasses import dataclass, field

@dataclass
class Team:
    members: list = field(default_factory=list)

print(Team())
''', wrong_note="a list as a plain default", fixed_note="default_factory builds a new list each time",
             why="A default list would be shared by every object, so a dataclass refuses it. default_factory calls list for each new object.",
             narr="Bug of the Day. We give the members field a list as its default. A dataclass stops us at once. Value error, mutable default list for field members is not allowed, use default factory. A shared list is the bug from episode sixty five. Use field with default factory equals list, and every team gets its own list."),
    pun="Why did the dataclass go to the gym? It wanted to cut some boilerplate.",
    task="a Book dataclass", challenge="Write a dataclass Book with a title, an author, and a price that defaults to 0. Print one book.",
    answer="@dataclass class Book: title: str; author: str; price: float = 0. print(Book(\"Python 101\", \"Rao\")).",
    shorts=[
        ("Type hints", "A type hint is a label. Write a colon and a type after a parameter, and an arrow and a type for the answer. Hints make code easier to read, and your editor can warn you about mistakes before you run anything.", "def area(w: float) -> float", "Hints are labels."),
        ("Not enforced", "Here is a surprise. Python does not enforce type hints when the program runs. Pass text to a function that says float, and Python carries on. Tools such as mypy read the hints, and warn you before you run the program.", "hints are not locks", "Python does not check hints."),
        ("Dataclass", "At dataclass above a class writes init, repr and eq for you, from the labelled fields. Five lines give you a class that builds, prints and compares itself. No boilerplate, and fewer typing mistakes.", "@dataclass", "Less boilerplate."),
        ("Mutable default", "Give a dataclass field a list as its default. Python says, value error, mutable default list is not allowed, use default factory. It protects you from the shared list bug. Write field with default factory equals list.", "field(default_factory=list)", "Use default_factory."),
        ("Pun and challenge", "Why did the dataclass go to the gym? It wanted to cut some boilerplate. Your challenge. Write a dataclass called Book. It has a title, an author, and a price that defaults to zero. Make one book, and print it.", "Challenge: Book dataclass", "Write a Book dataclass."),
    ],
))

EPISODES.append(dict(
    n=80, title="Testing your code (assert, unittest, pytest)", spoken="testing your code, assert, unittest and pytest",
    yt="Python Testing: assert, unittest and pytest for Beginners", thumb="TEST YOUR CODE",
    vis="Xecxec holding a green tick stamp and a red cross stamp over a row of functions",
    goals=["check code with assert", "write a small unittest test case", "know what a pytest test looks like"],
    tags=["python testing", "python unittest", "python assert", "python pytest beginners"],
    hash=["#python", "#testing"],
    analogy="a quality stamp on every function: tick if it behaves, cross if it does not, before it reaches the customer",
    c_title="Check before you ship",
    c_pts=["assert stops the program if a claim is false", "unittest groups checks into test methods", "pytest needs only plain functions and assert"],
    intro="How do you know your function still works after you change it? You test it, automatically.",
    concept="A test is code that checks your code. The simplest tool is assert. Write assert, then a claim. If the claim is False, Python raises an AssertionError. The unittest module in the standard library groups checks into a class, with methods whose names start with test. Another tool, pytest, needs only plain functions and assert, and is very popular. Think of a quality stamp on every function. Tick if it behaves, cross if it does not.",
    A=dict(file="asserts.py", label="assert", on="claims that must be true",
           src='''
def is_even(n):
    return n % 2 == 0

assert is_even(4)
assert not is_even(7)
print("all good")
try:
    assert is_even(3), "3 should be even?"
except AssertionError as e:
    print("failed:", e)
''',
           narr="[HL 1] A small function. [HL 2] True when the number is even. [HL 4] Assert that four is even. It is, so nothing happens. [HL 5] Assert that seven is not even. Also fine. [HL 6] All good. [HL 7] Now a claim that is false. [HL 8] Assert, a claim, and an optional message. Three is not even, so this raises. [HL 9] We catch the assertion error. [HL 10] And print the message. Failed, three should be even question mark. Normally you do not catch it. The program stops, and shows you where."),
    c2=dict(label="Green tick, red cross", on="A row of test cards; passing ones get a green tick, a failing one gets a red cross and a message", narr="Here is the idea of a test run. Each test is a small card with a claim. The runner flips every card. If the claim is true, it gets a green tick. If not, a red cross, and the message. After every change to your code, you run all the cards again, in a second. If something that worked yesterday breaks today, you see a red cross at once, before your users do.", anim="Test cards flip one by one; green ticks pop on most, one red cross with a message bubble appears"),
    B=dict(file="test_add.py", label="unittest", on="a test case with three test methods",
           src='''
import io
import unittest

def add(a, b):
    return a + b

class TestAdd(unittest.TestCase):
    def test_small(self):
        self.assertEqual(add(2, 3), 5)

    def test_negative(self):
        self.assertEqual(add(-1, 1), 0)

    def test_text(self):
        self.assertEqual(add("a", "b"), "ab")

suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestAdd)
result = unittest.TextTestRunner(stream=io.StringIO()).run(suite)
print(result.testsRun, result.wasSuccessful())
''',
           ref=[("pytest version, for reference", "# test_add.py\ndef add(a, b):\n    return a + b\n\ndef test_small():\n    assert add(2, 3) == 5\n\n# in the terminal\npython -m pytest")],
           narr="[HL 1] We need io. [HL 2] And unittest. [HL 4] The function under test. [HL 7] A test case class, built on unittest dot TestCase. [HL 8] Every test method name starts with test. [HL 9] Assert equal compares the two values. Two plus three is five. [HL 11] A second test. [HL 12] Minus one plus one is zero. [HL 14] A third test. [HL 15] It even works on text. [HL 17] Load every test in the class. [HL 18] Run them, with the report sent to a string, to keep this screen tidy. [HL 19] Three tests ran, and all passed. True. The pytest version, shown on screen, is even shorter. A plain function, and a plain assert."),
    term="all good, failed: 3 should be even?. Then 3 True.",
    recap=["assert claim raises AssertionError if the claim is False.", "unittest groups tests in a TestCase class; names start with test.", "pytest uses plain functions and assert.", "Run tests after every change."],
    bug=dict(title="assert on floats", file="floats.py", wrong='''
assert 0.1 + 0.2 == 0.3
''', fixed='''
import math

assert math.isclose(0.1 + 0.2, 0.3)
print("ok")
''', wrong_note="0.1 + 0.2 is 0.30000000000000004", fixed_note="math.isclose allows a tiny difference",
             why="Computers store most decimals as tiny approximations, so equal-looking numbers may differ in the last digits. Compare floats with math.isclose, not with equals.",
             narr="Bug of the Day. We assert that point one plus point two equals point three. It fails. Assertion error, with no message. Computers store decimals as tiny approximations, and the sum is point three, followed by a long tail ending in four. Compare floats with math dot is close instead. It allows a tiny difference."),
    pun="Why did the test pass the interview? It always checked its assertions.",
    task="test your own function", challenge="Write a function double(n) and an assert for double(4) that proves it returns 8. Then write a unittest version.",
    answer="assert double(4) == 8. For unittest, a TestCase with self.assertEqual(double(4), 8) inside a test method.",
    shorts=[
        ("What is a test", "A test is code that checks your code. After every change, you run your tests, and see at once if something broke. The simplest tool is assert. Write assert and a claim. If the claim is false, Python stops with an assertion error.", "assert claim", "Tests check your code."),
        ("unittest", "The unittest module is built into Python. Write a class that extends TestCase. Each method that starts with test is one test. Use assert equal to compare an answer with what you expect. Run them all in one go.", "class TestAdd(unittest.TestCase)", "unittest is built in."),
        ("pytest", "Pytest is a popular tool you install with pip. A test is a plain function, with a plain assert. No class needed. Name your file starting with test, and run pytest in the terminal. It finds every test and shows green or red.", "def test_add(): assert ...", "Pytest keeps it short."),
        ("Float trap", "Here is a trap. Assert point one plus point two equals point three, and it fails. Decimals are stored as tiny approximations. The sum has a long tail. Use math dot is close, which allows a tiny difference.", "assert math.isclose(...)", "Never compare floats with equals."),
        ("Pun and challenge", "Why did the test pass the interview? It always checked its assertions. Your challenge. Write a function called double. Then write an assert that proves double of four is eight. Bonus, write the same check as a unittest test.", "Challenge: test double()", "Write your own test."),
    ],
))
