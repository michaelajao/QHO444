# Corrections spotted in the SOL pages (weeks 1–11)

These are already fixed in the hub, where the page shows a "Note" box. SOL itself has not been changed. Check each one before you edit SOL.

## Week 1

- The module code appears as **QHO426** and **COM411** in places (repo name, welcome message, Modules page). It should be **QHO444**.
- Version Control, Activity 4: in `.gitignore` the line `*.idea` should be `.idea/`.
- Version Control: the mention of **REPL** is out of date. Point students to PyCharm on Learning on Demand instead.
- Profession page: Oxford Living Dictionaries (Lexico) no longer exists. Replace it with a link to Oxford Learner's Dictionaries.

## Week 2

- Multiple Conditions: the page says "*In the case of the not operator only one of the expressions must evaluate to True*". This is wrong. `not` flips a **single** condition. In the same paragraph, "on other side" should be "on **either** side".
- Decisions: the example output ends with "!" in some places and "." in others ("Finished reading book!" vs "."; "smallest!" vs "smallest."). Pick one so students' output matches exactly.
- Dark forest: the expected output's punctuation doesn't match the task text.

## Week 3

- While Loops, Activity 2: the prompt says "must I avoid" but the example says "should I avoid". The message also ends in "!" in the task and "." in the example.
- For Loops, Activity 4: the example output says `index 4: 0` (zero). It should be `index 4: o`.
- For Loops, Activity 3: "asterix" should be "asterisk".
- For Loops, Activity 6: the prompt is "What phrase do you want to print?" but the example shows "What phrase do you see?".
- Nested Loops: under the single-loop example the text says "*the line of digits is repeat 3 times*". That describes the nested version, not this one.

## Week 4

- Built-in Functions, Activity 1: "should start by displaying" appears twice. The prompt says "standard character" but the example says "letter".
- Built-in Functions, Activity 2: the example says "*ASCII code 155 is: m*". It should be **109**. "Otherwise, if the number is within the range" should be "is **not** within the range".
- User Defined Functions, Activity 4: "we must keep going!" vs "We must keep going!" (capital W in the example).
- User Defined Functions, Activity 3: "call-by-object-reference" is heavy for Year 1. Consider "Python passes the value into the parameter".
- Modules: `while(True):` doesn't need the parentheses. PEP 8 style is `while True:`.

## Week 5

- Ordered Data Structures: **`cmp()` doesn't exist in Python 3.** Remove it from both tables.
- `list.pop(el)` is described as "removes the last occurrence of el". In fact `pop(i)` removes and returns the item at **index** i.
- "`list.sort(key = lambda x)` sorts using a lambda function named x" is misleading. Lambdas come later.
- Lists, Activities 1 and 4: the expected output shows `["Move Forward", ...]` with double quotes, but Python prints `['Move Forward', ...]`. Students may think their code is wrong.
- Lists, Activity 3: the task says "Please select a direction:" but the example says "Please enter a direction:".
- Lists, Activity 4: "Call the function menu" should be `menu_and_input`. Also "start be displaying" should be "start by displaying".
- Tuples: `min(temperature)` / `max(temperature)` are missing the **s**, so they raise NameError.

## Week 6

- Data Files: **.docx and .xls are binary files**, not "text files with formatting".
- Data Files: `data/staff/prins.txt` is described as an absolute path. It's relative. The absolute version is `/data/staff/prins.txt`.
- Data Files: "attedance.csv" is a typo.
- Data Files: `requests` is third-party, so students need `pip install requests`.
- Text Files: the example path says `com411/week6`. Activity 3's output has stray full stops.
- CSV Files, Activity 1: "call the function read" should be `read_csv`. Activity 2's message doesn't match its example output.

## Week 7

- Unordered Data Structures: `s.issubeset(t)` should be `s.issubset(t)`.
- Dictionaries, Activity 1: "create an empty list and add elements later" should say an empty **dictionary**.
- Dictionary example outputs are missing the space after each colon. Python prints `{'Short Sequence': 3, ...}`.
- JSON, Activity 1: the example output ("Population:", strength/speed sentences) doesn't match the task's required format.
- JSON, Activity 2: "call the function read" should be `read_task2`. The intro says `dump` takes "the file path", but it takes an open **file object**.

## Week 8

- Data Visualisation: "Napolean" should be "Napoleon" (three times). Also "help bring an end" should be "helped bring an end".
- `plt.bar` is described as creating a **histogram**. It's a bar chart. Histograms use `plt.hist`.
- Plots, Activity 2: the squares task asks for "pentagon markers" (format character `p`) but never says which character to use. The sample image shows `x` markers, not pentagons.
- Plots, Activity 3: the values from `input()` must go through `int()`/`float()`, or matplotlib plots them as text categories. Worth adding as a hint.
- Plots, Activity 4: `random.sample` needs a population, e.g. `random.sample(range(0, 20), 5)`. Students will get stuck without an example.

## Week 9

- Objects and Classes: class methods are described as "require an instance of the class". They don't. They receive the class (`cls`) and can be called as `Robot.assemble()`.
- `if (__name__ == "__main__"):` doesn't need the parentheses.
- "one class per file, named in lowercase" is a convention, not a Python rule. Worth saying so.
- Pre-reading: "We know that it is a method as it has the keyword self" is misleading. `self` is a naming convention, not a keyword.

## Week 10

- Activity 4: the example `class Tech:` is missing `(ABC)`, and `def activate():` is missing `self`. As written, Tech can still be instantiated, and calling the method raises TypeError.
- Activity 2's commit message is copied from week 9 ("Updated classes human and robot with instance methods").
- The class diagram is an image only. Students who use screen readers need a text version of the classes and their relationships.

## Week 11

- Titanic, Activity 6: two separate `if`s ("below 18", "below 65") count every child as an adult too. It has to be `if/elif/else` to get 113 / 590 / 11. Ages can also be decimals (0.42), so use `float()`, not `int()`.
- Titanic: "You have selection option" is a typo. The expected output in Activity 3 shows the lines in the wrong order.
- Olympics: the second function heading reads `def display_medal_tally(team_tally)` but should be `display_team_medal_tally`. "the medals the team has one" should be "won".
- Olympics: the padding note says `{msg:10}` pads the start of the message. For strings it pads the end (left-aligns). Only numbers right-align by default.
- The Process Module page was cut off when it was pasted here, after "Expected Output". Check that its ending is complete on SOL.

## Supplementary PDFs (from a read-through)

- **Python Short Notes**: p34 `return Fahrenheit` raises NameError. On p50 the break/continue examples are wrong. On p63 the tuple name doesn't match. p89 `try: open(...) as file:` is invalid. On p90 the mode `'b'` is invalid, and PyPDF2 is deprecated.
- **Python Handbook**: p71 `range(04)` is a SyntaxError. The comments on p56 are wrong. p110 `def eat():` is missing `self`.
- **Python Programs Example**: uses `sum` as a variable name, camelCase methods, and in program 56 a variable named `even_numbers` that holds odd numbers.
- **Python Interview Questions**: the answer to Q45 (p124) should be `sum(kwargs.values())`. Q44, Q47 and Q72 are ambiguous or wrong. Q86 and Q88 are duplicates.
- **Gaps:** none of the PDFs covers Git, matplotlib or `abc` abstract classes. JSON is barely covered.
