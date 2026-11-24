
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "database" / "ideathon2k26.db"

connection = sqlite3.connect(DB_PATH)

subject = "Data Structure with Python Program"
branch_code = "EEE"
semester = 3
topic = "Python Fundamentals and Data Types"

questions = [
    (
        "Which keyword is used to define a function in Python?",
        "function",
        "def",
        "define",
        "fun",
        "B",
        "The def keyword is used to define a function in Python.",
        "Beginner"
    ),
    (
        "Which of the following is a valid Python variable name?",
        "2value",
        "my-value",
        "my_value",
        "class",
        "C",
        "Variable names can contain underscores but cannot start with a digit or use reserved keywords.",
        "Beginner"
    ),
    (
        "Which data type is used to store True or False values?",
        "int",
        "str",
        "bool",
        "float",
        "C",
        "The bool data type represents Boolean values True and False.",
        "Beginner"
    ),
    (
        "What is the output of type(10) in Python?",
        "float",
        "str",
        "int",
        "bool",
        "C",
        "The value 10 is an integer, so its type is int.",
        "Beginner"
    ),
    (
        "Which function is used to display output in Python?",
        "input()",
        "print()",
        "display()",
        "show()",
        "B",
        "The print() function displays output on the screen.",
        "Beginner"
    ),
    (
        "What is the output of the expression 10 // 3?",
        "3.33",
        "3",
        "1",
        "4",
        "B",
        "The // operator performs floor division. Therefore, 10 // 3 gives 3.",
        "Intermediate"
    ),
    (
        "What is the output of bool(0) in Python?",
        "True",
        "False",
        "0",
        "None",
        "B",
        "Zero is a falsy value in Python, so bool(0) returns False.",
        "Intermediate"
    ),
    (
        "What is the output of the following expression: 2 ** 3 ** 2?",
        "64",
        "512",
        "256",
        "36",
        "B",
        "Exponentiation is right-associative: 2 ** (3 ** 2) = 2 ** 9 = 512.",
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

    print("EEE Python Topic 1 added successfully!")
    print("Subject:", subject)
    print("Topic:", topic)
    print("New questions added:", inserted)
    print("Existing questions skipped:", skipped)

except Exception as error:
    connection.rollback()
    print("Error:", error)

finally:
    connection.close()
