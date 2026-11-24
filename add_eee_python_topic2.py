
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "database" / "ideathon2k26.db"

connection = sqlite3.connect(DB_PATH)

subject = "Data Structure with Python Program"
branch_code = "EEE"
semester = 3
topic = "Conditional Statements and Loops"

questions = [
    (
        "Which statement is used to execute code when a condition is true?",
        "if",
        "for",
        "while",
        "break",
        "A",
        "The if statement executes its block when the given condition is true.",
        "Beginner"
    ),
    (
        "Which keyword is used to check another condition after an if statement?",
        "else",
        "elif",
        "continue",
        "pass",
        "B",
        "The elif keyword checks another condition when the previous if or elif condition is false.",
        "Beginner"
    ),
    (
        "Which loop is commonly used to iterate over a sequence?",
        "if",
        "for",
        "switch",
        "try",
        "B",
        "A for loop iterates over items in a sequence such as a list or string.",
        "Beginner"
    ),
    (
        "Which keyword immediately terminates a loop?",
        "skip",
        "stop",
        "break",
        "continue",
        "C",
        "The break statement immediately exits the nearest enclosing loop.",
        "Beginner"
    ),
    (
        "What does the continue statement do inside a loop?",
        "Terminates the program",
        "Exits the loop completely",
        "Skips the current iteration",
        "Restarts the computer",
        "C",
        "The continue statement skips the remaining statements in the current iteration and moves to the next iteration.",
        "Beginner"
    ),
    (
        "What is the output of this code? for i in range(2, 6): print(i, end=' ')",
        "2 3 4 5 6",
        "2 3 4 5",
        "1 2 3 4 5",
        "3 4 5 6",
        "B",
        "range(2, 6) generates numbers from 2 up to, but not including, 6.",
        "Intermediate"
    ),
    (
        "How many times will the loop execute? i = 1; while i < 5: i += 1",
        "3",
        "4",
        "5",
        "Infinite times",
        "B",
        "The loop runs for i = 1, 2, 3, and 4. When i becomes 5, the condition becomes false.",
        "Intermediate"
    ),
    (
        "What is the output of this code? for i in range(5): if i == 3: break; print(i, end=' ')",
        "0 1 2",
        "0 1 2 3",
        "1 2 3",
        "0 1 2 3 4",
        "A",
        "The loop prints 0, 1, and 2. When i becomes 3, break terminates the loop before printing it.",
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

    print("EEE Python Topic 2 added successfully!")
    print("Subject:", subject)
    print("Topic:", topic)
    print("New questions added:", inserted)
    print("Existing questions skipped:", skipped)

except Exception as error:
    connection.rollback()
    print("Error:", error)

finally:
    connection.close()
