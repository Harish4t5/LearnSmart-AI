
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "database" / "ideathon2k26.db"

connection = sqlite3.connect(DB_PATH)

subject = "Data Structure with Python Program"
branch_code = "EEE"
semester = 3
topic = "Functions and Recursion"

questions = [
    (
        "Which keyword is used to define a function in Python?",
        "function",
        "def",
        "return",
        "lambda",
        "B",
        "The def keyword is used to define a user-defined function in Python.",
        "Beginner"
    ),
    (
        "Which keyword is used to send a value back from a function?",
        "print",
        "break",
        "return",
        "continue",
        "C",
        "The return statement sends a result back to the function caller.",
        "Beginner"
    ),
    (
        "What is a parameter in a Python function?",
        "A value returned by a function",
        "A variable listed in a function definition",
        "A loop inside a function",
        "A Python module",
        "B",
        "A parameter is a variable specified in the function definition that receives an argument.",
        "Beginner"
    ),
    (
        "What is the term for a function calling itself?",
        "Iteration",
        "Inheritance",
        "Recursion",
        "Encapsulation",
        "C",
        "Recursion occurs when a function calls itself.",
        "Beginner"
    ),
    (
        "Which type of argument uses a parameter name while calling a function?",
        "Positional argument",
        "Keyword argument",
        "Default argument",
        "Variable argument",
        "B",
        "A keyword argument is passed using the parameter name, such as greet(name='Amit').",
        "Beginner"
    ),
    (
        "What is the output? def add(a, b=5): return a + b; print(add(3))",
        "3",
        "5",
        "8",
        "Error",
        "C",
        "Since b has a default value of 5, add(3) returns 3 + 5 = 8.",
        "Intermediate"
    ),
    (
        "What is the output of this recursive function? def fact(n): return 1 if n == 0 else n * fact(n-1); print(fact(4))",
        "10",
        "16",
        "24",
        "120",
        "C",
        "The function calculates 4 × 3 × 2 × 1 = 24 using recursion.",
        "Intermediate"
    ),
    (
        "What is the main purpose of a base case in recursion?",
        "To repeat the function forever",
        "To stop recursive calls",
        "To define a global variable",
        "To import a module",
        "B",
        "A base case provides a stopping condition that prevents infinite recursive calls.",
        "Intermediate"
    )
]

inserted = 0
skipped = 0

try:
    for q in questions:
        existing = connection.execute("""
            SELECT id FROM quiz_questions
            WHERE subject = ?
              AND branch_code = ?
              AND semester = ?
              AND topic = ?
              AND question = ?
        """, (subject, branch_code, semester, topic, q[0])).fetchone()

        if existing:
            skipped += 1
            continue

        connection.execute("""
            INSERT INTO quiz_questions (
                subject, topic, question,
                option_a, option_b, option_c, option_d,
                correct_answer, explanation, difficulty,
                branch_code, semester
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            subject, topic, q[0],
            q[1], q[2], q[3], q[4],
            q[5], q[6], q[7],
            branch_code, semester
        ))

        inserted += 1

    connection.commit()

    print("EEE Python Topic 3 added successfully!")
    print("Subject:", subject)
    print("Topic:", topic)
    print("New questions added:", inserted)
    print("Existing questions skipped:", skipped)

except Exception as error:
    connection.rollback()
    print("Error:", error)

finally:
    connection.close()
