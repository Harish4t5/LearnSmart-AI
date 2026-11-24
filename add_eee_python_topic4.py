
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "database" / "ideathon2k26.db"

connection = sqlite3.connect(DB_PATH)

subject = "Data Structure with Python Program"
branch_code = "EEE"
semester = 3
topic = "Lists, Tuples and Strings"

questions = [
    (
        "Which symbol is used to create a list in Python?",
        "()",
        "[]",
        "{}",
        "<>",
        "B",
        "Square brackets [] are used to create a list in Python.",
        "Beginner"
    ),
    (
        "Which of the following data structures is immutable?",
        "List",
        "Dictionary",
        "Tuple",
        "Set",
        "C",
        "A tuple is immutable, which means its elements cannot be changed after creation.",
        "Beginner"
    ),
    (
        "Which method adds an element to the end of a list?",
        "insert()",
        "append()",
        "remove()",
        "pop()",
        "B",
        "The append() method adds a single element to the end of a list.",
        "Beginner"
    ),
    (
        "What is the index of the first element in a Python list?",
        "1",
        "-1",
        "0",
        "2",
        "C",
        "Python uses zero-based indexing, so the first element has index 0.",
        "Beginner"
    ),
    (
        "Which operator is used to join two strings?",
        "&",
        "+",
        "*",
        "%",
        "B",
        "The + operator concatenates two strings.",
        "Beginner"
    ),
    (
        "What is the output of len([10, 20, 30, 40])?",
        "3",
        "4",
        "5",
        "40",
        "B",
        "The len() function returns the number of elements. This list contains four elements.",
        "Intermediate"
    ),
    (
        "What is the output of [1, 2, 3][1]?",
        "1",
        "2",
        "3",
        "Error",
        "B",
        "List indexing starts at 0. Therefore, index 1 refers to the second element, which is 2.",
        "Intermediate"
    ),
    (
        "What is the output of 'PYTHON'[1:4]?",
        "PYT",
        "YTH",
        "THO",
        "YTHO",
        "B",
        "String slicing includes the starting index but excludes the ending index, giving characters at positions 1, 2 and 3.",
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

    print("EEE Python Topic 4 added successfully!")
    print("Subject:", subject)
    print("Topic:", topic)
    print("New questions added:", inserted)
    print("Existing questions skipped:", skipped)

except Exception as error:
    connection.rollback()
    print("Error:", error)

finally:
    connection.close()
