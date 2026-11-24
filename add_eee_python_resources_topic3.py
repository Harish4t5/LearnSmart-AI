
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "database" / "ideathon2k26.db"

connection = sqlite3.connect(DB_PATH)
cursor = connection.cursor()

subject = "Data Structure with Python Program"
topic = "Functions and Recursion"

resources = [
    (
        subject,
        topic,
        "Beginner",
        "Article",
        "Functions and Recursion - Study Notes",
        "",
        """FUNCTIONS AND RECURSION

1. What is a Function?

A function is a reusable block of code designed to
perform a particular task.

A function helps to:
- Reuse code.
- Reduce repetition.
- Improve readability.
- Divide a large program into smaller parts.

2. Defining a Function

Python uses the def keyword to define a function.

Example:
def greet():
    print("Hello!")

Calling the function:
greet()

3. Parameters and Arguments

Parameters are variables listed in a function definition.
Arguments are the actual values passed during a function call.

Example:
def add(a, b):
    print(a + b)

add(10, 20)

Here, a and b are parameters, while 10 and 20 are arguments.

4. Return Statement

The return statement sends a result back to the caller.

Example:
def square(n):
    return n * n

result = square(5)
print(result)

Output: 25

5. Types of Arguments

- Positional arguments: Matched according to position.
- Keyword arguments: Passed using parameter names.
- Default arguments: Use a predefined value when omitted.
- Variable-length arguments: Accept a variable number of values.

Example:
def greet(name="Student"):
    print("Hello", name)

6. Scope of Variables

Local variable:
Created inside a function and normally accessible there.

Global variable:
Defined outside functions and accessible throughout
the module, subject to Python's scope rules.

The global keyword allows a function to reassign a
module-level global variable.

7. What is Recursion?

Recursion occurs when a function calls itself to solve
a smaller version of a problem.

Every correct recursive solution needs:
- Base case: Stops further recursive calls.
- Recursive case: Moves towards the base case.

Example:
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(5))

Output: 120

8. Advantages and Limitations

Advantages:
- Useful for problems with repetitive subproblems.
- Can make some solutions shorter and clearer.
- Useful in tree traversal and divide-and-conquer algorithms.

Limitations:
- Each recursive call uses stack space.
- Excessive recursion can cause RecursionError.
- Some recursive solutions are less efficient than iterative ones.

Remember:
def -> Defines a function.
return -> Sends a result back.
Recursion -> A function calls itself.
Base case -> Stops recursion."""
    ),
    (
        subject,
        topic,
        "Intermediate",
        "Documentation",
        "Python Functions Documentation",
        "https://docs.python.org/3/tutorial/controlflow.html#defining-functions",
        "Official Python tutorial covering function definitions, "
        "parameters, arguments, return values, default values, "
        "keyword arguments and recursion-related concepts."
    )
]

inserted = 0
skipped = 0

try:
    for resource in resources:
        cursor.execute("""
            SELECT id FROM learning_resources
            WHERE subject = ?
            AND topic = ?
            AND level = ?
            AND resource_type = ?
            AND title = ?
        """, (
            resource[0], resource[1], resource[2],
            resource[3], resource[4]
        ))

        if cursor.fetchone():
            skipped += 1
            continue

        cursor.execute("""
            INSERT INTO learning_resources
            (subject, topic, level, resource_type, title, url, description)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, resource)

        inserted += 1

    connection.commit()

    print("Data Structure with Python - Topic 3 resources processed!")
    print("Inserted:", inserted)
    print("Skipped:", skipped)

except Exception as error:
    connection.rollback()
    print("Error:", error)

finally:
    connection.close()
