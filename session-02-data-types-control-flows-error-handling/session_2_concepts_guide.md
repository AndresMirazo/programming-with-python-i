# Session II: Concepts Guide
## Data Types, Control Flow, and Error Handling

This guide covers the core Python concepts you will apply throughout the Session II exercises. Read through the explanations and study the examples **before** attempting the exercises.

---

## 1. Data Types and Type Conversion

Every value in Python has a **type**. The most common built-in types you'll work with are:

| Type | Example | Description |
|------|---------|-------------|
| `int` | `42` | Whole numbers |
| `float` | `3.14` | Decimal numbers |
| `str` | `"hello"` | Text (strings) |
| `bool` | `True` / `False` | Logical values |
| `NoneType` | `None` | Represents "no value" |

### Primitive vs. Non-Primitive Data Types

Python data types are commonly grouped into two categories.

**Primitive (basic) types** hold a **single, simple value**. They are the basic building blocks of data:

| Type | Example |
|------|---------|
| `int` | `42` |
| `float` | `3.14` |
| `str` | `"hello"` |
| `bool` | `True` |
| `NoneType` | `None` |

**Non-primitive (collection) types** are built from other values and can hold **multiple items** at once:

| Type | Example | Ordered? | Mutable? | Description |
|------|---------|----------|----------|-------------|
| `list` | `[1, 2, 3]` | Yes | Yes | A changeable sequence of items |
| `tuple` | `(1, 2, 3)` | Yes | No | A fixed sequence of items |
| `dict` | `{"name": "Ana", "age": 20}` | Yes (insertion order) | Yes | Key-value pairs |
| `set` | `{1, 2, 3}` | No | Yes | Unique items only, no duplicates |

```python
# Primitive: one value per variable
age = 25
name = "Ana"

# Non-primitive: one variable holds many values
scores = [90, 85, 77]
student = {"name": "Ana", "age": 25}

scores.append(100)        # lists can be changed after creation
student["age"] = 26       # dicts can be changed too
```

**Key differences:**

- **Number of values:** a primitive holds one value; a non-primitive is a container for many.
- **Mutability:** primitives are **immutable**, so any "change" creates a new value. Most non-primitives (`list`, `dict`, `set`) are **mutable** and can be modified in place. The exception is `tuple`, which is immutable.

> **Note:** Python itself doesn't formally use the terms "primitive" and "non-primitive". Unlike languages such as Java, *everything* in Python is an object, including integers. The distinction is a helpful way to think about simple values versus collections of values.

### Collection Types in Detail

#### `list`: ordered, mutable, duplicates allowed

```python
items = [10, "apple", 3.5, True, [1, 2]]   # can mix types, even nest lists
items[0]            # 10 (indexing starts at 0)
items[-1]           # [1, 2] (negative index counts from the end)
items[1:3]          # ["apple", 3.5] (slicing)
items[0] = 99       # OK: lists are mutable
items.append(7)     # add to the end
[1, 1, 1]           # duplicates are fine
```

#### `tuple`: ordered, immutable, duplicates allowed

```python
point = (3, 4)
point[0]            # 3 (indexing and slicing work like lists)
point[0] = 10       # TypeError: 'tuple' object does not support item assignment

single = (5,)       # a one-item tuple NEEDS the trailing comma
not_tuple = (5)     # this is just the int 5 in parentheses
x, y = point        # unpacking: x = 3, y = 4
```

> **Gotcha:** a tuple is immutable, but if it *contains* a mutable item, that item can still change: `t = ([1, 2], 3); t[0].append(9)` works, giving `([1, 2, 9], 3)`. You just can't replace `t[0]` with a different object.

#### `dict`: key-value pairs, mutable, keys are unique

```python
student = {"name": "Ana", "age": 20}
student["name"]             # "Ana" (look up by KEY, not by position)
student["grade"] = "A"      # add a new pair
student["age"] = 21         # keys are unique, so this overwrites the old value
student["email"]            # KeyError: the key doesn't exist
student.get("email")        # None (safe lookup, no error)
```

**Rules for keys.** A key must be **hashable**, which in practice means **immutable**:

| Allowed as a key | Not allowed as a key |
|------------------|----------------------|
| `str`: `{"name": 1}` | `list`: `{[1, 2]: "x"}` |
| `int`: `{1: "one", 2: "two"}` | `dict`: `{{"a": 1}: "x"}` |
| `float`: `{3.14: "pi"}` | `set`: `{{1, 2}: "x"}` |
| `bool`: `{True: "yes"}` | tuple that contains a list: `{([1], 2): "x"}` |
| `None`: `{None: "empty"}` | |
| `tuple` of immutables: `{(1, 2): "point"}` | |

```python
{[1, 2]: "x"}       # TypeError: unhashable type: 'list'
```

Other things to know about keys:

- **Integer keys are valid**, but they are *labels*, not positions. `d = {10: "a"}` then `d[10]` works, while `d[0]` raises `KeyError`.
- **Keys of different types are different keys**: `"1"` (string) and `1` (int) are two separate keys.
- **`1`, `1.0` and `True` count as the same key**, because they are equal and have the same hash: `{1: "a", True: "b"}` becomes `{1: "b"}`.
- **Duplicate keys are silently overwritten**: `{"a": 1, "a": 2}` becomes `{"a": 2}`.
- **Values have no restrictions.** They can be any type, including lists or other dicts.
- Dicts keep **insertion order** (Python 3.7+), but you access items by key, not by index.

#### `set`: unordered, mutable, unique items only

```python
nums = {1, 2, 2, 3, 3}      # {1, 2, 3}: duplicates are removed automatically
nums.add(4)                 # OK: sets are mutable
nums[0]                     # TypeError: sets have no order, so no indexing
{[1, 2], 3}                 # TypeError: unhashable type: 'list'
```

- Like dict keys, set items must be **hashable** (immutable). `{1, "a", (1, 2)}` is valid; `{[1, 2]}` is not.
- **`{}` creates an empty dict, not an empty set.** Use `set()` for an empty set.
- A common use is removing duplicates: `list(set([1, 1, 2, 3]))` gives `[1, 2, 3]` (the order is not guaranteed).

#### Quick comparison

| | `list` | `tuple` | `dict` | `set` |
|---|---|---|---|---|
| Syntax | `[1, 2]` | `(1, 2)` | `{"a": 1}` | `{1, 2}` |
| Access by | index | index | key | no direct access (loop or `in`) |
| Duplicates | allowed | allowed | keys unique | not allowed |
| Mutable | yes | no | yes | yes |
| Can be a dict key / set item? | no | yes (if its items are immutable) | no | no |

### Checking a Type

Use the built-in `type()` function to inspect any value:

```python
print(type(42))        # <class 'int'>
print(type(3.14))      # <class 'float'>
print(type("hello"))   # <class 'str'>
print(type(True))      # <class 'bool'>
print(type(None))      # <class 'NoneType'>
```

### Explicit Type Conversion (Casting)

Python does **not** automatically convert between incompatible types. You must do it yourself:

```python
# String to integer
age_str = "25"
age = int(age_str)      # 25 (int)

# String to float
price_str = "19.99"
price = float(price_str)  # 19.99 (float)

# Number to string
score = 100
message = "Your score is " + str(score)
```

### When Conversion Fails

Not every value can be converted to every type. This is a very common source of errors. Here are the main ones:

#### `ValueError`: The value's format is wrong

Raised when the *format* of the input doesn't match what the function expects:

```python
int("hello")           # ValueError: invalid literal for int() with base 10: 'hello'
int("12.5")            # ValueError: invalid literal for int() with base 10: '12.5'
float("1.2.3")         # ValueError: could not convert string to float: '1.2.3'
bool("false")          # bool("false") returns True! ("false" is a non-empty string)
```

> **Note:** `bool()` is tricky. It converts *any* value to a boolean based on "truthiness":
> - Falsy: `False`, `0`, `0.0`, `""`, `[]`, `{}`, `set()`, `None`
> - Truthy: everything else (including `"false"`, `"0"`, `[0]`)
>
> So `bool("false")` is `True`. Use the string `"True"` or `"False"` with `ast.literal_eval()` if you need to parse a boolean from a string.

#### `TypeError`: The type itself is incompatible

Raised when you try to convert a type that Python can't convert, no matter what:

```python
int(None)              # TypeError: int() argument must be a string, a bytes-like object or a number, not 'NoneType'
float(None)            # TypeError: float() argument must be a string or a number, not 'NoneType'
int([1, 2, 3])         # TypeError: int() argument must be a string, a bytes-like object or a number, not 'list'
int({"a": 1})          # TypeError: int() argument must be a string, a bytes-like object or a number, not 'dict'
str({"a": 1})          # This works, but gives a string representation: "{'a': 1}"
```

#### Tricky cases

```python
int(True)              # 1: booleans are integers
int(False)             # 0
int(3.99)              # 3: truncates (doesn't round) toward zero
float("inf")           # inf: special floating-point value
int(float("inf"))      # OverflowError: cannot convert float infinity to integer
```

#### Summary table

| Conversion | Success | Failure |
|---|---|---|
| `int("123")` | `123` | — |
| `int("12.5")` | — | `ValueError` (no decimals allowed) |
| `int("hello")` | — | `ValueError` (invalid format) |
| `int(None)` | — | `TypeError` (incompatible type) |
| `float("3.14")` | `3.14` | — |
| `float("12x")` | — | `ValueError` |
| `float(None)` | — | `TypeError` |
| `str(100)` | `"100"` | — |
| `str(None)` | `"None"` | — |
| `bool("anything")` | `True` (if non-empty) | — (doesn't fail; uses truthiness) |

>> Go to the **Exercise 1 (Messy Sensor Data Cleaner)**, you will handle exactly this problem: a list containing values that may or may not be convertible to `float`. You'll use `try/except` to catch `ValueError` and `TypeError`.

---

## 2. Conditional Statements (`if / elif / else`)

Conditionals let your program make **decisions** based on whether a condition is `True` or `False`.

### Basic Structure

```python
temperature = 35

if temperature > 30:
    print("It's hot outside!")
elif temperature > 20:
    print("Nice weather.")
else:
    print("It's cold.")
```

### Comparison and Logical Operators

| Operator | Meaning | Example |
|----------|---------|---------|
| `==` | Equal to | `x == 5` |
| `!=` | Not equal to | `x != 5` |
| `>` | Greater than | `x > 5` |
| `<` | Less than | `x < 5` |
| `>=` | Greater than or equal | `x >= 5` |
| `<=` | Less than or equal | `x <= 5` |
| `and` | Both must be True | `x > 0 and x < 10` |
| `or` | At least one must be True | `x < 0 or x > 100` |
| `not` | Inverts the result | `not x == 5` |

### Nested Conditionals

You can place an `if` statement **inside** another `if` statement. This is useful when decisions depend on multiple layers of logic:

```python
user_type = "student"
age = 16

if user_type == "student":
    if age < 18:
        print("Junior student discount: 50% off")
    else:
        print("Student discount: 20% off")
else:
    print("Regular price")
```

>> Go to the **Exercise 2 (Transit Kiosk)**, you will use nested conditionals to apply discounts based on both the selected zone *and* the passenger's age.

---

## 3. Loops

Loops allow you to **repeat** a block of code multiple times.

### `for` Loop — When You Know the Number of Iterations

Use `for` when you want to iterate over a **known sequence** (a list, a string, a range of numbers):

```python
# Iterating over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Iterating over a range of numbers
for i in range(5):      # 0, 1, 2, 3, 4
    print(f"Step {i}")

# Iterating over characters in a string
for char in "Python":
    print(char)
```

### `while` Loop — When You Don't Know How Many Iterations

Use `while` when the loop should keep running **until a condition changes**:

```python
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    answer = input("Guess the number: ")
    if answer == "7":
        print("Correct!")
        break           # Exit the loop immediately
    attempts += 1
    print(f"Wrong. {max_attempts - attempts} attempts left.")
```

### Key Loop Keywords

| Keyword | What It Does |
|---------|-------------|
| `break` | **Exits** the loop immediately |
| `continue` | **Skips** the rest of the current iteration and goes to the next one |

```python
# Example of continue: skip even numbers
for num in range(10):
    if num % 2 == 0:
        continue        # Skip this iteration
    print(num)          # Only prints: 1, 3, 5, 7, 9
```

> Go to the **Exercise 3 (Three-Strike Quiz)**, you will use a `while` loop with a counter and `break`.

---

## 4. Error Handling (`try / except`)

When Python encounters an error during execution, it raises an **exception** and the program crashes. The `try/except` block lets you **catch** these errors and handle them gracefully.

### Basic Structure

```python
try:
    number = int(input("Enter a number: "))
    print(f"You entered: {number}")
except ValueError:
    print("That's not a valid number!")
```

### Catching Multiple Exception Types

You can handle different error types separately:

```python
try:
    result = 10 / int(input("Enter a divisor: "))
    print(f"Result: {result}")
except ValueError:
    print("Error: Please enter a valid integer.")
except ZeroDivisionError:
    print("Error: You cannot divide by zero.")
```

Or catch several at once:

```python
try:
    value = float(some_variable)
except (ValueError, TypeError):
    print("Could not convert the value to a number.")
```

### Common Exception Types in Python I

| Exception | When It Happens | Example |
|-----------|----------------|---------|
| `ValueError` | A function gets the right type but an invalid value | `int("hello")` |
| `TypeError` | An operation is applied to the wrong type | `"hello" + 5` |
| `ZeroDivisionError` | Division by zero | `10 / 0` |
| `FileNotFoundError` | Trying to open a file that doesn't exist | `open("missing.txt")` |
| `KeyError` | Accessing a dictionary key that doesn't exist | `my_dict["missing_key"]` |

### The Full `try / except / else / finally` Pattern

```python
try:
    file = open("data.txt", "r")
except FileNotFoundError:
    print("File not found!")
else:
    # This runs ONLY if no exception occurred
    content = file.read()
    print(content)
finally:
    # This runs NO MATTER WHAT (useful for cleanup)
    print("Operation complete.")
```

> Error handling is the **central theme** of this entire session. You'll use it in every exercise, but especially in the **Exercise 4 (BMI Refactoring)**.

---

## 5. Functions

Functions let you **organize your code** into reusable, named blocks. This is the foundation of writing clean, maintainable programs.

### Defining and Calling a Function

```python
def greet(name):
    """Print a personalized greeting."""
    print(f"Hello, {name}! Welcome to Python I.")

greet("Alice")      # Hello, Alice! Welcome to Python I.
greet("Bob")        # Hello, Bob! Welcome to Python I.
```

### Parameters, Arguments, and Return Values

```python
def calculate_area(width, height):
    """Calculate and return the area of a rectangle."""
    area = width * height
    return area         # Send the result back to the caller

result = calculate_area(5, 3)
print(f"The area is {result}")    # The area is 15
```

### Default Parameter Values

You can provide a default value so the argument becomes optional:

```python
def power(base, exponent=2):
    """Raise base to the given exponent (default: squared)."""
    return base ** exponent

print(power(5))       # 25 (uses default exponent=2)
print(power(5, 3))    # 125
```

### Why Functions Matter: Refactoring

**Before** (repetitive and fragile):

```python
# Calculating tax for 3 products — copy-pasted logic
price1 = 100
tax1 = price1 * 0.21
total1 = price1 + tax1
print(f"Total: {total1}")

price2 = 250
tax2 = price2 * 0.21
total2 = price2 + tax2
print(f"Total: {total2}")
```

**After** (clean and reusable):

```python
def calculate_total(price, tax_rate=0.21):
    """Calculate price + tax."""
    tax = price * tax_rate
    return round(price + tax, 2)

print(f"Total: {calculate_total(100)}")     # 121.0
print(f"Total: {calculate_total(250)}")     # 302.5
```

> Go to the **Exercise 5 (Universal Unit Converter)**, you will design an entire program organized around multiple functions.

---

## 6. String Methods for Defensive Input Handling

User input is **unreliable**. People type extra spaces, mix upper and lowercase, and make typos. Python's built-in string methods help you clean and inspect input safely.

### Cleaning User Input

```python
raw = "   PaRiS   "
clean = raw.strip().lower()    # "paris"
```

| Method | What It Does | Example |
|--------|-------------|---------|
| `.strip()` | Removes leading/trailing whitespace | `"  hi  ".strip()` → `"hi"` |
| `.lower()` | Converts to lowercase | `"HELLO".lower()` → `"hello"` |
| `.upper()` | Converts to uppercase | `"hello".upper()` → `"HELLO"` |
| `.title()` | Capitalizes first letter of each word | `"hello world".title()` → `"Hello World"` |

### Inspecting Characters in a String

These methods return `True` or `False` and are very useful inside `for` loops and conditionals:

```python
char = "A"
print(char.isupper())     # True
print(char.islower())     # False
print(char.isdigit())     # False
print(char.isalpha())     # True (it's a letter)
```

### Practical Pattern: Checking a String Character by Character

```python
password = "Hello123"

has_upper = False
has_digit = False

for char in password:
    if char.isupper():
        has_upper = True
    if char.isdigit():
        has_digit = True

print(f"Has uppercase: {has_upper}")   # True
print(f"Has digit: {has_digit}")       # True
```

> Go to the  **Exercise 6 (Password Validator)**, you'll loop through a string checking each character's properties.

---

## 7. Dictionaries for Structured Data

Dictionaries store data as **key-value pairs**. They are the most practical data structure for organizing real-world data in Python.

### Creating and Accessing

```python
student = {
    "name": "Alice",
    "age": 22,
    "grade": "A"
}

print(student["name"])       # Alice
print(student["age"])        # 22
```

### Adding and Updating Values

```python
student["email"] = "alice@university.edu"   # Add new key
student["grade"] = "A+"                      # Update existing key
```

### Looping Through a Dictionary

```python
prices = {"Zone 1": 2.50, "Zone 2": 4.00, "Zone 3": 6.50}

for zone, price in prices.items():
    print(f"{zone}: ${price:.2f}")
```

### Using a Dictionary as a Lookup Table

Instead of long `if/elif` chains, use a dictionary:

```python
# Long and repetitive
if zone == 1:
    price = 2.50
elif zone == 2:
    price = 4.00
elif zone == 3:
    price = 6.50

# Clean and scalable
prices = {1: 2.50, 2: 4.00, 3: 6.50}
price = prices[zone]
```

### Accumulating Data with Dictionaries

A very common pattern — counting or summing values by category:

```python
expenses = ["Food", "Transport", "Food", "Entertainment", "Food"]

counts = {}
for category in expenses:
    if category in counts:
        counts[category] += 1
    else:
        counts[category] = 1

print(counts)   # {'Food': 3, 'Transport': 1, 'Entertainment': 1}
```

> Go to the  **Exercise 7 (Multi-Round Quiz)**, questions are stored as a list of dictionaries.

---

## 8. Putting It All Together: Defensive Programming Patterns

The exercises in this session combine all of the above concepts into **defensive programs** — programs that never crash, no matter what the user types. Here is the general pattern you'll use repeatedly:

```python
def get_valid_number(prompt):
    """Keep asking until the user enters a valid number."""
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Error: Please enter a positive number.")
                continue
            return value
        except ValueError:
            print("Error: That's not a valid number. Try again.")


def main():
    """Main menu loop."""
    while True:
        print("\n=== MAIN MENU ===")
        print("[1] Option A")
        print("[2] Option B")
        print("[Q] Quit")

        choice = input("Select an option: ").strip().lower()

        if choice == "1":
            amount = get_valid_number("Enter an amount: ")
            print(f"You entered: {amount}")
        elif choice == "2":
            print("Option B selected.")
        elif choice == "q":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

main()
```

This pattern combines:
-  A `while True` loop for the main menu
- `try/except` for safe type conversion
- `.strip().lower()` for clean input handling
- `break` and `continue` for flow control
- Functions to organize logic into reusable pieces
- Conditionals for menu routing and validation

>> Go to the  **Exercise 8 (Expense Tracker)** is the capstone exercise where you will combine all of these patterns into a single, fully functional application.

---

## Quick Reference Cheat Sheet

```
┌──────────────────────────────────────────────────────┐
│  TYPE CONVERSION     int()  float()  str()  bool()   │
│  CONDITIONALS        if / elif / else                 │
│  LOOPS               for ... in    while              │
│  LOOP CONTROL        break   continue                 │
│  ERROR HANDLING      try / except / else / finally    │
│  FUNCTIONS           def name(params): return value   │
│  STRING CLEANING     .strip()  .lower()  .upper()    │
│  STRING CHECKING     .isdigit() .isalpha() .isupper() │
│  DICT ACCESS         d[key]   d.get(key, default)    │
│  DICT ITERATION      for k, v in d.items():          │
│  FORMATTING          f"Value: {x:.2f}"               │
└──────────────────────────────────────────────────────┘
```

---
