
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "database" / "ideathon2k26.db"

connection = sqlite3.connect(DB_PATH)
cursor = connection.cursor()

subject = "Data Structure with Python Program"
topic = "Conditional Statements and Loops"

resources = [
    (
        subject,
        topic,
        "Beginner",
        "Article",
        "Conditional Statements and Loops - Study Notes",
        "",
        """CONDITIONAL STATEMENTS AND LOOPS

1. Conditional Statements

Conditional statements execute code depending on
whether a condition is True or False.

if statement:
Executes a block when the condition is True.

Example:
age = 18
if age >= 18:
    print("Eligible")

if-else statement:
Chooses between two blocks.

Example:
if marks >= 40:
    print("Pass")
else:
    print("Fail")

if-elif-else:
Checks multiple conditions in sequence.

Example:
if marks >= 90:
    print("A")
elif marks >= 75:
    print("B")
else:
    print("C")

2. for Loop

A for loop iterates over items in a sequence or iterable.

Example:
for i in range(1, 6):
    print(i)

Output: 1 2 3 4 5

3. while Loop

A while loop repeats as long as its condition is True.

Example:
i = 1
while i <= 5:
    print(i)
    i += 1

4. Loop Control Statements

break:
Terminates the nearest enclosing loop.

continue:
Skips the remaining statements in the current iteration
and moves to the next iteration.

pass:
Acts as a placeholder and performs no operation.

5. range() Function

range() generates a sequence of integers.

range(5)       -> 0, 1, 2, 3, 4
range(1, 5)    -> 1, 2, 3, 4
range(1, 10, 2)-> 1, 3, 5, 7, 9

6. Nested Loops

A loop placed inside another loop is called a nested loop.

Example:
for i in range(2):
    for j in range(2):
        print(i, j)

7. Important Points

- Indentation defines code blocks in Python.
- A for loop is useful for iterating over sequences.
- A while loop is useful when repetition depends on a condition.
- An infinite loop occurs when its condition never becomes False.
- break exits the nearest enclosing loop.

Remember:
if/elif/else -> Decision making.
for/while -> Repetition.
break/continue -> Loop control."""
    ),
    (
        subject,
        topic,
        "Intermediate",
        "Documentation",
        "Python Control Flow Documentation",
        "https://docs.python.org/3/tutorial/controlflow.html",
        "Official Python tutorial covering if statements, for loops, "
        "range(), break, continue, pass, loop else clauses and "
        "function definitions."
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

    print("Data Structure with Python - Topic 2 resources processed!")
    print("Inserted:", inserted)
    print("Skipped:", skipped)

except Exception as error:
    connection.rollback()
    print("Error:", error)

finally:
    connection.close()
