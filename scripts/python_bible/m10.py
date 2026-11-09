"""Module 10 — Capstone and what's next (EP 87-90)."""

MODULE = {"id": 10, "name": "Capstone and what's next", "range": "87–90", "colours": "Mint + Tomato"}
EPISODES = []
NEXT_AFTER = ("That is the course! Keep building.", "That is the whole Python course. Pick a small project of your own, and start building today. See you in the next course.")

EPISODES.append(dict(
    n=87, title="Capstone 1: Expense tracker design", spoken="capstone one, expense tracker design",
    yt="Python Capstone: Design an Expense Tracker", thumb="EXPENSE TRACKER",
    vis="Xecxec drawing boxes and arrows on a whiteboard next to a piggy bank",
    goals=["break a project into data and actions", "model one expense with a dataclass", "validate input before it enters the data"],
    tags=["python capstone project", "python expense tracker", "python project design", "python dataclass project"],
    hash=["#python", "#project"],
    analogy="a blueprint before building a house: walls, doors and wiring decided on paper first",
    c_title="Plan before you type",
    c_pts=["List what the program must do", "Decide what one expense looks like", "Reject bad input at the door"],
    intro="Time for a real project. Over three episodes we build an expense tracker, starting with the plan.",
    concept="Before writing code, write the plan. Our expense tracker must add an expense, list the expenses, show totals by category, and save everything in a file. First decide what one expense looks like. It has a day, a category, an amount and an optional note. A dataclass is perfect for that. Then decide the actions, each as a small function. Finally, decide the rules. For example, an amount must be positive. Think of a blueprint before building a house. Walls, doors and wiring are decided on paper first.",
    A=dict(file="design.py", label="The data model", on="one Expense, and a function that adds it",
           src='''
from dataclasses import dataclass

@dataclass
class Expense:
    day: str
    category: str
    amount: float
    note: str = ""

expenses = []

def add_expense(day, category, amount, note=""):
    expenses.append(Expense(day, category, amount, note))

add_expense("2025-03-01", "food", 120.5, "lunch")
add_expense("2025-03-02", "travel", 60, "bus pass")
add_expense("2025-03-03", "food", 80)
print(len(expenses))
print(expenses[0])
''',
           narr="[HL 1] We use a dataclass. [HL 3] One Expense is a small bundle. [HL 4] The class. [HL 5] A day, written as text. [HL 6] A category, such as food. [HL 7] An amount. For now, a plain number. We improve money in the next episode. [HL 8] An optional note. [HL 10] All expenses live in one list. [HL 12] Add expense builds an Expense, [HL 13] and appends it to the list. [HL 15] Lunch. [HL 16] A bus pass. [HL 17] And another food expense. [HL 18] Three expenses. [HL 19] And the first one prints itself, thanks to the dataclass."),
    c2=dict(label="The whole plan on one page", on="Four boxes in a row: add, list, summary, save, each pointing to one shared list of Expense cards", narr="Here is the plan on one page. In the middle sits one list of Expense cards. Around it, four actions. Add puts a new card in the list. List shows the cards. Summary adds the amounts by category. Save writes the cards to a file, and loads them back at the start. Each action is a small function. If every function does one job, the project stays easy to change.", anim="A central list of expense cards with four arrows labelled add, list, summary and save, each pointing to a function box"),
    B=dict(file="totals.py", label="Totals by category", on="group the amounts with a dictionary",
           src='''
expenses = [
    ("food", 120.5),
    ("travel", 60.0),
    ("food", 80.0),
]
totals = {}
for category, amount in expenses:
    totals[category] = totals.get(category, 0) + amount
for category in sorted(totals):
    print(category, totals[category])
print(sum(totals.values()))
''',
           narr="[HL 1] A few expenses, as pairs. [HL 2] Food. [HL 3] Travel. [HL 4] More food. [HL 6] An empty dictionary for the totals. [HL 7] Loop over the pairs. [HL 8] Get the total so far for this category, or zero, and add the amount. [HL 9] Sort the categories, so the order is steady. [HL 10] Print each total. Food two hundred point five, travel sixty. [HL 11] And the grand total. Two sixty point five."),
    term="3 and the first Expense line. Then food 200.5, travel 60.0, 260.5.",
    recap=["Plan first: what the program must do.", "Model one thing with a dataclass.", "Each action is one small function.", "Check the rules before data enters the list."],
    bug=dict(title="negative amounts are accepted", kind="output", file="rules.py", wrong='''
expenses = []

def add_expense(category, amount):
    expenses.append((category, amount))

add_expense("food", 100)
add_expense("travel", -500)
print(sum(a for _, a in expenses))
''', fixed='''
expenses = []

def add_expense(category, amount):
    if amount <= 0:
        raise ValueError("amount must be positive")
    expenses.append((category, amount))

add_expense("food", 100)
try:
    add_expense("travel", -500)
except ValueError as e:
    print("rejected:", e)
print(sum(a for _, a in expenses))
''', wrong_note="a negative expense reduces the total", fixed_note="bad amounts are rejected at the door",
             why="Nothing stopped a negative amount, so the total silently became wrong. Validate input in one place, before it enters your data.",
             narr="Bug of the Day. We add a travel expense of minus five hundred. Nothing stops it, and the total becomes minus four hundred. No error, just a wrong answer. Validate at the door. If the amount is zero or less, raise a value error, and let the caller decide what to do."),
    pun="Why did the expense tracker go to design school? It wanted a better balance sheet.",
    task="one more rule", challenge="Add a rule that the category must not be empty, and test it with a try and except.",
    answer="if not category: raise ValueError(\"category is required\"), placed inside add_expense before the append.",
    shorts=[
        ("Plan first", "Before you type, plan. Our expense tracker must add, list, summarise and save. Write those four actions down, each as one small function. A plan on paper takes five minutes, and saves hours of rewriting later.", "add, list, summary, save", "Plan before you type."),
        ("One expense", "What does one expense look like? A day, a category, an amount, and a note. That is a perfect dataclass. Three lines of fields, and Python writes init, repr and eq for you. One small class, the heart of the project.", "@dataclass class Expense", "Model one thing."),
        ("Totals", "To total by category, use a dictionary. Loop over the expenses. For each one, get the total so far, or zero, and add the amount. Sort the keys when printing, so the order is steady every time.", "totals.get(category, 0) + amount", "Group with a dict."),
        ("Validate", "A bug hides in many projects. Nothing stops a negative amount, and the total silently goes wrong. Check at the door. If the amount is zero or less, raise a value error. One check, in one place, protects everything.", "if amount <= 0: raise ValueError", "Validate at the door."),
        ("Pun and challenge", "Why did the expense tracker go to design school? It wanted a better balance sheet. Your challenge. Add one more rule. The category must not be empty. Raise a value error if it is, and test your rule with try and except.", "Challenge: category required", "Add one more rule."),
    ],
))

EPISODES.append(dict(
    n=88, title="Capstone 2: Expense tracker build", spoken="capstone two, expense tracker build",
    yt="Python Capstone: Build the Expense Tracker (Money, JSON, Files)", thumb="BUILD IT",
    vis="Xecxec stacking coins into neat columns beside a JSON file folder",
    goals=["store money as whole cents", "format cents back into text", "save and load the data as JSON"],
    tags=["python capstone build", "python money decimal", "python save json file", "python float rounding money"],
    hash=["#python", "#project"],
    analogy="counting coins instead of weighing money: whole pieces never come out as 28.999",
    c_title="Money in cents",
    c_pts=["Floats cannot store most decimals exactly", "Keep money as whole cents", "Save the list as JSON, load it back at the start"],
    intro="Today we build the real thing. First, the one thing computers get wrong: money.",
    concept="Floats store most decimals as tiny approximations. For money, that leads to errors in the last digit. The safe way is to keep money as whole cents, in an integer. To read text such as one twenty point five zero, use the Decimal type, which is exact, and multiply by one hundred. To show it, divide by one hundred with floor division, and the remainder with two digits. Then save the list to a JSON file, and load it when the program starts. Think of counting coins instead of weighing money.",
    A=dict(file="money.py", label="Cents and Decimal", on="convert text to cents and back; dataclass to JSON",
           src='''
from dataclasses import dataclass, asdict
import json
from decimal import Decimal

@dataclass
class Expense:
    day: str
    category: str
    cents: int
    note: str = ""

def to_cents(text):
    value = Decimal(text)
    if value <= 0:
        raise ValueError("amount must be positive")
    return int(value * 100)

def money(cents):
    return f"{cents // 100}.{cents % 100:02d}"

e = Expense("2025-03-01", "food", to_cents("120.50"), "lunch")
print(e)
print(money(e.cents))
print(json.dumps(asdict(e)))
''',
           narr="[HL 1] Dataclass and asdict. [HL 2] Json. [HL 3] Decimal, the exact number type. [HL 5] The dataclass decorator. [HL 6] The same Expense, but now with cents, a whole number. [HL 7] A day. [HL 8] A category. [HL 9] Cents, an integer. [HL 10] And the note. [HL 12] To cents turns text into whole cents. [HL 13] Decimal reads the text exactly. [HL 14] The rule from last time. Positive only. [HL 15] The error. [HL 16] Multiply by one hundred, and make it an integer. [HL 18] Money turns cents back into text. [HL 19] Whole units, a dot, and the remainder, with two digits. [HL 21] An expense of one twenty point five zero. [HL 22] It prints with cents twelve thousand fifty. [HL 23] Money shows one twenty point five zero. [HL 24] And as dict, with json dumps, turns the dataclass into JSON text, ready for a file."),
    c2=dict(label="Coins, not weights", on="A scale showing 28.999999 next to a tray of 29 whole coins", narr="Here is the problem. A float stores point two nine as a tiny approximation, slightly under. Multiply by one hundred, and it is twenty eight point nine nine nine. Cut off the end, and we get twenty eight, one cent lost. Decimal stores the number exactly, like counting coins. Whole cents in an integer never drift. Convert once, at the door, and every calculation after that is exact.", anim="A balance showing 28.999 on one side and a tray of 29 coins on the other"),
    B=dict(file="store.py", label="Save and load", on="load the list from a file, add one, save it back",
           src='''
import json
from pathlib import Path

FILE = Path("expenses.json")

def load():
    if not FILE.exists():
        return []
    return json.loads(FILE.read_text())

def save(items):
    FILE.write_text(json.dumps(items))

items = load()
print(len(items))
items.append({"category": "food", "cents": 12050})
save(items)
print(len(load()))
''',
           narr="[HL 1] Json. [HL 2] And Path. [HL 4] The file name, as a Path. [HL 6] Load. [HL 7] On the first run, the file does not exist, [HL 8] so we start with an empty list. [HL 9] Otherwise, read the text, and load the list. [HL 11] Save. [HL 12] Write the list as JSON text. [HL 14] Load at the start. [HL 15] Zero on the first run. [HL 16] Add an expense. [HL 17] Save it. [HL 18] Load again, and now there is one. On the next run of the program, the data is already there."),
    term="The Expense line, 120.50, the JSON text. Then 0 and 1.",
    recap=["Keep money as whole cents in an integer.", "Decimal reads text exactly; floats do not.", "Convert once at the door, show with money().", "Save the list as JSON, load it at the start."],
    bug=dict(title="money as a float rounds wrongly", kind="output", file="cents.py", wrong='''
print(int(0.29 * 100))
''', fixed='''
from decimal import Decimal

print(int(Decimal("0.29") * 100))
''', wrong_note="0.29 * 100 is 28.999999999999996", fixed_note="Decimal is exact",
             why="Floats store point two nine as an approximation just below it, so multiplying and cutting off the end loses a cent. Decimal reads the text exactly.",
             narr="Bug of the Day. Point two nine times one hundred should be twenty nine. Python prints twenty eight. The float is a hair below point two nine, and int cuts off the end. A cent vanishes, and no error appears. Read money as text with Decimal instead, and the answer is exactly twenty nine."),
    pun="Why did the programmer count in cents? Every penny counts.",
    task="show a total", challenge="Write a function total_cents(items) that adds the cents of a list of dictionaries, and print the total with money().",
    answer="def total_cents(items): return sum(i[\"cents\"] for i in items). Then print(money(total_cents(items))).",
    shorts=[
        ("Float trouble", "Here is the money trap. Point two nine times one hundred is not twenty nine. Python prints twenty eight, after you cut off the end. The float is a tiny bit below point two nine. Never use floats for money.", "int(0.29 * 100) = 28", "Floats lose cents."),
        ("Whole cents", "The safe way is to keep money as whole cents, in an integer. One twenty point five zero becomes twelve thousand fifty. Add, subtract and compare whole numbers, and nothing ever drifts. Convert once, when the amount comes in.", "120.50 -> 12050", "Count in cents."),
        ("Decimal", "To read money from text, use Decimal. It stores the number exactly. Decimal of the text, times one hundred, and make it an integer. Printing back is easy. Floor divide by one hundred, then the remainder with two digits.", "Decimal(\"120.50\") * 100", "Decimal is exact."),
        ("Save as JSON", "Saving is short. Write the list as JSON text with json dumps, into a file. Loading reads the text, and json loads gives the list back. On the first run, the file does not exist, so check first, and start with an empty list.", "json.dumps / json.loads", "Save and load JSON."),
        ("Pun and challenge", "Why did the programmer count in cents? Every penny counts. Your challenge. Write a function called total cents. It adds the cents of a list of dictionaries. Then print the total, in the money format, with a dot and two digits.", "Challenge: total_cents()", "Total the cents."),
    ],
))

EPISODES.append(dict(
    n=89, title="Capstone 3: Tests and polish", spoken="capstone three, tests and polish",
    yt="Python Capstone: Tests and Polish for Your Project", thumb="TEST + POLISH",
    vis="Xecxec polishing a coin with a cloth beside a row of green ticks",
    goals=["test the money functions with unittest", "check that a function raises the right error", "print a tidy report with f-string alignment"],
    tags=["python capstone tests", "python unittest assertraises", "python f-string alignment", "python project polish"],
    hash=["#python", "#testing"],
    analogy="a final inspection before the shop opens: everything checked, then polished",
    c_title="Check, then shine",
    c_pts=["Tests keep money code honest", "assertRaises checks that bad input is rejected", "f-string alignment makes a neat report"],
    intro="Our tracker works. Now we make sure it keeps working, and make its report look good.",
    concept="Money code deserves tests. We write a test case with a few checks. Assert equal for exact answers. Assert raises, as a context manager, to check that bad input raises the right error. Run the tests after every change. Then polish the report. Inside an f string, a colon, a less than sign and a number left aligns text in a column. A greater than sign right aligns, and dot two f shows two decimals. Think of a final inspection before the shop opens. Everything is checked, then polished.",
    A=dict(file="test_money.py", label="Testing the money functions", on="three tests, including one for bad input",
           src='''
import io
import unittest
from decimal import Decimal

def to_cents(text):
    value = Decimal(text)
    if value <= 0:
        raise ValueError("amount must be positive")
    return int(value * 100)

def money(cents):
    return f"{cents // 100}.{cents % 100:02d}"

class TestMoney(unittest.TestCase):
    def test_exact(self):
        self.assertEqual(to_cents("0.29"), 29)

    def test_format(self):
        self.assertEqual(money(12050), "120.50")

    def test_rejects_negative(self):
        with self.assertRaises(ValueError):
            to_cents("-5")

suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestMoney)
result = unittest.TextTestRunner(stream=io.StringIO()).run(suite)
print(result.testsRun, result.wasSuccessful())
''',
           narr="[HL 1] We need io. [HL 2] And unittest. [HL 3] And Decimal. [HL 5] The same to cents function. [HL 11] And the money function. [HL 14] A test case. [HL 15] The first test. [HL 16] Point two nine must become exactly twenty nine. This is the very bug from last time. [HL 18] The second test. [HL 19] Twelve thousand fifty cents must read one twenty point five zero. [HL 21] The third test. [HL 22] Assert raises, as a with block, passes only if the code inside raises a value error. [HL 23] Minus five must be rejected. [HL 25] Load the tests. [HL 26] Run them, quietly. [HL 27] Three tests, all passing."),
    c2=dict(label="Tests as a safety net", on="A tightrope walker with a net labelled tests; a change causes a red cross and the net catches it", narr="Here is why we test. Imagine you change the money function next month. Without tests, you hope nothing broke. With tests, you run them, and in a second you see a green tick, or a red cross with the name of the test that failed. The net catches the fall before your users see it. Good tests are small, fast, and each checks one thing, with a name that says what.", anim="A walker on a rope steps, wobbles, and a net labelled tests catches a falling red cross card"),
    B=dict(file="report.py", label="A tidy report", on="align columns with f-string format specs",
           src='''
expenses = [("food", 12050), ("travel", 6000), ("food", 8000)]
totals = {}
for category, cents in expenses:
    totals[category] = totals.get(category, 0) + cents
print(f"{'Category':<10}{'Total':>10}")
for category in sorted(totals):
    print(f"{category:<10}{totals[category] / 100:>10.2f}")
print("-" * 20)
print(f"{'All':<10}{sum(totals.values()) / 100:>10.2f}")
''',
           narr="[HL 1] Expenses in cents. [HL 2] Totals by category. [HL 3] Loop over the expenses. [HL 4] Add the cents. [HL 5] A header. Less than ten, left aligns in ten columns. Greater than ten right aligns the total. [HL 6] For each category, in order. [HL 7] The name, left aligned. The total, divided by one hundred, right aligned, with two decimals. [HL 8] A line of twenty dashes. [HL 9] The grand total, in the same columns. The columns line up, and the report looks professional."),
    term="3 True. Then the aligned table, food 200.50, travel 60.00, and All 260.50.",
    recap=["Test the money code with unittest.", "assertRaises checks that bad input is rejected.", "f-string formats such as <10 and >10.2f align columns.", "Run the tests after every change."],
    bug=dict(title="a test that always passes", kind="output", file="weak.py", wrong='''
def to_cents(text):
    return int(float(text) * 100)

def test_cents():
    result = to_cents("0.29")
    assert result == to_cents("0.29")

test_cents()
print("test passed")
''', fixed='''
def to_cents(text):
    return int(float(text) * 100)

def test_cents():
    result = to_cents("0.29")
    assert result == 29

try:
    test_cents()
    print("test passed")
except AssertionError:
    print("test failed: caught the bug")
''', wrong_note="the test compares the result with itself", fixed_note="the test compares with the known right answer",
             why="A test must compare against an independent, known answer. Comparing a result with the same function's result can never fail, so it proves nothing.",
             narr="Bug of the Day. The test passes, and the function is wrong. It turns point two nine into twenty eight. The test compares the result with the same function called again, so it can never fail. A test needs a known answer, written by you. Compare with twenty nine, and the bug is caught at once."),
    pun="Why did the test never fail? It was always comparing itself with itself.",
    task="test the report", challenge="Write one test that checks money(5) returns \"0.05\", and run it.",
    answer="self.assertEqual(money(5), \"0.05\"). Cents 5 gives 0 whole, and 05 as the remainder.",
    shorts=[
        ("Test money code", "Money code deserves tests. Write a test case with unittest. Assert equal checks exact answers. Point two nine must become twenty nine cents. Run the tests after every change, and bugs will not sneak back in.", "assertEqual(to_cents(\"0.29\"), 29)", "Test your money code."),
        ("assertRaises", "To test that bad input is rejected, use assert raises, as a with block. If the code inside raises a value error, the test passes. If it does not raise, the test fails. It checks the error, not just the answer.", "with self.assertRaises(ValueError)", "Test the errors too."),
        ("Align columns", "Make reports tidy with f string formats. Colon, less than, ten, left aligns in ten columns. Greater than aligns right. And dot two f shows two decimals. Together, the columns line up like a real table.", "f\"{name:<10}{total:>10.2f}\"", "Line up the columns."),
        ("Useless test", "A test that always passes is worse than no test. Comparing a result with the same function's result can never fail. A real test compares with a known answer you wrote yourself. Then a wrong function fails the test.", "assert result == 29", "Compare with a known answer."),
        ("Pun and challenge", "Why did the test never fail? It was always comparing itself with itself. Your challenge. Write one test that checks money of five returns zero point zero five. Make sure you compare with a string you typed yourself.", "Challenge: test money(5)", "Write one test."),
    ],
))

EPISODES.append(dict(
    n=90, title="What's next", spoken="what's next",
    yt="Python: What to Learn Next After This Course", thumb="WHAT'S NEXT?",
    vis="Xecxec standing at a crossroads with signs for web, data, games and automation",
    goals=["review the big ideas of the course", "spot a classic bug in a quiz", "choose your next project"],
    tags=["python what to learn next", "python roadmap", "python after beginner", "python project ideas"],
    hash=["#python", "#roadmap"],
    analogy="a map with several roads: you have learned to drive, now choose where to go",
    c_title="You can code now",
    c_pts=["You know variables, loops, functions, classes and files", "You can read errors and fix them", "The best next step is a project of your own"],
    intro="You made it to the end. Here is what you can do now, and where to go next.",
    concept="Look at how far you have come. You can store data in variables, lists, dictionaries and sets. You can make decisions and repeat work with loops. You can write functions, classes, and generators, read and write files, handle errors, test your code, and use the standard library. Most of all, you can read an error message, and fix the problem. That is the real skill. The best next step is a project of your own. Pick something small that you would use yourself. Think of a map with several roads. You have learned to drive. Now choose where to go.",
    A=dict(file="review.py", label="A taste of everything", on="a small program that mixes several ideas from the course",
           src='''
from collections import Counter

def top(words, n=1):
    return Counter(words).most_common(n)

menu = {"tea": 10, "chai": 15, "coffee": 25}
orders = ["tea", "chai", "tea", "coffee", "tea"]
bill = sum(menu[o] for o in orders)
print(top(orders))
print(f"Bill: {bill}")
print(sorted(o for o in set(orders) if menu[o] > 12))
''',
           narr="[HL 1] A tool from the standard library. [HL 3] A function, with a default argument. [HL 4] It uses Counter, and returns the top items. [HL 6] A dictionary for prices. [HL 7] A list of orders. [HL 8] A generator expression adds the prices. [HL 9] The most common order. Tea, three times. [HL 10] An f string for the bill. Seventy. [HL 11] A set removes duplicates, a condition filters, and sorted makes the order steady. Chai and coffee. Dictionaries, lists, sets, functions, f strings, generators and a standard library module, all in eleven lines. You learned every one of them."),
    c2=dict(label="Roads to choose from", on="A crossroads with signs: web with Flask, data with pandas, games with pygame, automation, and testing with pytest", narr="Here are the roads. For websites, look at Flask or Django. For data and charts, try pandas and matplotlib. For games, there is pygame. For automation, write scripts that rename files, send reports or tidy your folders. For testing, learn pytest. You do not have to choose forever. Pick one road, build a small project, and see if you enjoy it. If not, try another.", anim="A crossroads with five signposts, each lighting up in turn with a small icon"),
    B=dict(file="roadmap.py", label="Your next steps", on="a numbered list of next steps",
           src='''
topics = [
    "web: Flask",
    "data: pandas",
    "games: pygame",
    "automation: your own scripts",
    "testing: pytest",
]
for i, topic in enumerate(topics, start=1):
    print(i, topic)
print("Pick one, and build something small this week.")
''',
           narr="[HL 1] A list of next steps. [HL 2] Web, with Flask. [HL 3] Data, with pandas. [HL 4] Games, with pygame. [HL 5] Automation, with scripts of your own. [HL 6] Testing, with pytest. [HL 8] Enumerate numbers the topics from one. [HL 9] Print each. [HL 10] And one last line. Pick one, and build something small this week. A small finished project teaches more than ten unfinished big ones."),
    term="[('tea', 3)], Bill: 70, ['chai', 'coffee']. Then the five numbered topics and the final line.",
    recap=["You can write and read Python programs.", "You can use lists, dictionaries, functions, classes and files.", "You can read errors, test your code, and fix bugs.", "Next: build one small project of your own."],
    bug=dict(title="quiz: spot the bug", kind="output", file="quiz.py", wrong='''
nums = [2, 4, 6, 8]
for n in nums:
    if n % 2 == 0:
        nums.remove(n)
print(nums)
''', fixed='''
nums = [2, 4, 6, 8]
nums = [n for n in nums if n % 2 != 0]
print(nums)
''', wrong_note="the list changes while the loop walks it", fixed_note="build a new list instead",
             why="Removing items from a list while looping over it shifts the remaining items, so the loop skips some. Build a new list with a comprehension instead.",
             narr="Final quiz. Spot the bug. We remove every even number from the list, and print. We expect an empty list. We get four and eight. The loop walks the list by position. When we remove an item, the next one slides into its place, and the loop jumps over it. Never change a list while looping over it. Build a new list with a comprehension instead."),
    pun="Why did the student finish the course with a smile? Because they finally got the last laugh, and the last loop.",
    task="start your project", challenge="Write down one small project you would use yourself, and write its first three functions as empty def lines with pass.",
    answer="Any small idea works: a habit tracker, a quiz, a budget. List three functions, such as add_item, show_items and save, each with pass.",
    shorts=[
        ("Look how far you came", "Look how far you have come. Variables, loops, functions, classes, files, errors, tests and the standard library. You can read an error message, and fix the problem. That is the real skill of a programmer. Well done.", "You can code now", "You came a long way."),
        ("Choose a road", "Where next? For websites, try Flask. For data, pandas. For games, pygame. For automation, write scripts that tidy your folders. For testing, pytest. Pick one road, build something small, and see if you enjoy it.", "web, data, games, automation", "Pick one road."),
        ("Build something small", "The best way to learn is to build. Pick a small project you would really use. A habit tracker, a quiz, a budget. Write its first three functions as empty def lines. Then fill them in, one at a time.", "small project, finished", "Finish something small."),
        ("Spot the bug", "A final quiz. We remove every even number from a list while looping over it. We expect an empty list. We get four and eight. The loop skipped items, because the list shifted. Build a new list instead.", "remove while looping = skips", "Never edit while looping."),
        ("Thank you", "Thank you for learning Python with me. Every expert was once a beginner who kept going. Pick one small project this week, and build it. Your challenge. Write down your idea, and its first three functions. Show me what you build.", "Challenge: your own project", "Keep building."),
    ],
))
