
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "database" / "ideathon2k26.db"

connection = sqlite3.connect(DB_PATH)
cursor = connection.cursor()

subject = "Data Structure with Python Program"
topic = "Python Fundamentals and Data Types"

resources = [
    (
        subject,
        topic,
        "Beginner",
        "Article",
        "Python Fundamentals and Data Types - Study Notes",
        "",
        """PYTHON FUNDAMENTALS AND DATA TYPES

1. Introduction to Python

Python is a high-level, interpreted programming language.
It is known for readable syntax and a large collection
of libraries.

2. Variables

Variables store values in a program.

Example:
name = "Harish"
age = 18
marks = 85.5

Python determines the variable type at runtime.

3. Basic Data Types

int:
Stores integer values.
Example: 10, -5

float:
Stores decimal values.
Example: 10.5, 3.14

str:
Stores text.
Example: "Hello Python"

bool:
Stores True or False.

complex:
Stores complex numbers.
Example: 3 + 4j

4. Collection Data Types

list:
Ordered and mutable collection.
Example: [10, 20, 30]

tuple:
Ordered and immutable collection.
Example: (10, 20, 30)

set:
Unordered collection of unique elements.
Example: {10, 20, 30}

dictionary:
Stores key-value pairs.
Example: {"name": "Harish", "age": 18}

5. Type Conversion

Converting one data type into another is called
type conversion.

Examples:
int("25")       -> 25
float("5")      -> 5.0
str(100)        -> "100"

6. Operators

Arithmetic: +, -, *, /, //, %, **
Comparison: ==, !=, >, <, >=, <=
Logical: and, or, not
Assignment: =, +=, -=

7. Input and Output

input() accepts user input.
print() displays output.

Example:
name = input("Enter your name: ")
print("Hello", name)

8. Important Points

- Python is case-sensitive.
- Variable names cannot begin with a digit.
- Lists are mutable, while tuples are immutable.
- Dictionaries store key-value pairs.
- The type() function identifies an object's type.

Remember:
Understand variables, data types and collections
before starting data structures and algorithms."""
    ),
    (
        subject,
        topic,
        "Intermediate",
        "Documentation",
        "Python Official Tutorial",
        "https://docs.python.org/3/tutorial/",
        "Official Python documentation covering variables, "
        "numbers, strings, lists, tuples, sets, dictionaries, "
        "control flow and basic programming concepts."
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

    print("Data Structure with Python - Topic 1 resources processed!")
    print("Inserted:", inserted)
    print("Skipped:", skipped)

except Exception as error:
    connection.rollback()
    print("Error:", error)

finally:
    connection.close()
