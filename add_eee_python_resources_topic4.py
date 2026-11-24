
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "database" / "ideathon2k26.db"

connection = sqlite3.connect(DB_PATH)
cursor = connection.cursor()

subject = "Data Structure with Python Program"
topic = "Lists, Tuples and Strings"

resources = [
    (
        subject,
        topic,
        "Beginner",
        "Article",
        "Lists, Tuples and Strings - Study Notes",
        "",
        """LISTS, TUPLES AND STRINGS

1. Lists

A list is an ordered, mutable collection of elements.
Lists allow duplicate values and can store different data types.

Example:
numbers = [10, 20, 30, 40]

Accessing elements:
print(numbers[0])  # 10
print(numbers[-1]) # 40

Important list methods:
- append(x): Adds an element at the end.
- insert(i, x): Inserts an element at a position.
- remove(x): Removes the first matching value.
- pop(): Removes and returns an element.
- sort(): Sorts the list.
- reverse(): Reverses the list.

2. Tuples

A tuple is an ordered, immutable collection.

Example:
data = (10, 20, 30)

Accessing elements:
print(data[1])  # 20

Important points:
- Tuples allow duplicate values.
- Elements can be accessed using indexing.
- A tuple cannot be modified after creation.
- A single-element tuple requires a trailing comma.

Example:
single = (10,)

3. Strings

A string is an immutable sequence of characters.

Example:
name = "Python"

Accessing characters:
print(name[0])  # P
print(name[-1]) # n

Important string methods:
- upper(): Converts to uppercase.
- lower(): Converts to lowercase.
- strip(): Removes surrounding whitespace.
- replace(old, new): Replaces a substring.
- split(): Splits a string into a list.
- find(): Finds the position of a substring.

4. Indexing and Slicing

Indexing accesses an individual element.
Slicing extracts a portion of a sequence.

Example:
values = [10, 20, 30, 40, 50]

print(values[1:4])
Output: [20, 30, 40]

5. Mutable and Immutable Objects

Mutable:
Can be changed after creation.
Example: List.

Immutable:
Cannot be changed after creation.
Examples: Tuple and String.

6. List Comprehension

A concise way to create a list.

Example:
squares = [x*x for x in range(1, 5)]

Output: [1, 4, 9, 16]

7. Basic Comparison

List:
- Uses square brackets [].
- Mutable.

Tuple:
- Uses parentheses ().
- Immutable.

String:
- Uses quotes.
- Immutable sequence of characters.

Remember:
Lists are useful for changeable collections.
Tuples are useful for fixed collections.
Strings are used to store text."""
    ),
    (
        subject,
        topic,
        "Intermediate",
        "Documentation",
        "Python Data Structures Documentation",
        "https://docs.python.org/3/tutorial/datastructures.html",
        "Official Python tutorial covering lists, list methods, "
        "tuples, sequences, sets, dictionaries and list comprehensions."
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

    print("Data Structure with Python - Topic 4 resources processed!")
    print("Inserted:", inserted)
    print("Skipped:", skipped)

except Exception as error:
    connection.rollback()
    print("Error:", error)

finally:
    connection.close()

