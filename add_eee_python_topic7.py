
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "database" / "ideathon2k26.db"

connection = sqlite3.connect(DB_PATH)

subject = "Data Structure with Python Program"
branch_code = "EEE"
semester = 3
topic = "Linked Lists"

questions = [
    (
        "What is a linked list?",
        "A collection of elements stored only in an array",
        "A collection of nodes connected using links",
        "A type of sorting algorithm",
        "A programming language",
        "B",
        "A linked list is a linear data structure consisting of nodes connected through references.",
        "Beginner"
    ),
    (
        "What are the two main parts of a basic singly linked list node?",
        "Index and value",
        "Data and next pointer",
        "Key and array",
        "Front and rear",
        "B",
        "A singly linked list node contains data and a reference to the next node.",
        "Beginner"
    ),
    (
        "What does the next pointer of the last node in a singly linked list contain?",
        "Address of the first node",
        "Zero always",
        "None",
        "Address of the previous node",
        "C",
        "The next reference of the last node is None, indicating the end of the list.",
        "Beginner"
    ),
    (
        "Which linked list allows traversal in both forward and backward directions?",
        "Singly linked list",
        "Doubly linked list",
        "Linear array",
        "Stack",
        "B",
        "A doubly linked list contains references to both the previous and next nodes.",
        "Beginner"
    ),
    (
        "Which linked list has its last node connected back to the first node?",
        "Singly linked list",
        "Doubly linked list",
        "Circular linked list",
        "Static linked list",
        "C",
        "In a circular linked list, the last node points back to the first node.",
        "Beginner"
    ),
    (
        "What is the time complexity of accessing the element at position n in a singly linked list?",
        "O(1)",
        "O(log n)",
        "O(n)",
        "O(n log n)",
        "C",
        "A linked list must be traversed node by node to reach a particular position, so access takes O(n) time.",
        "Intermediate"
    ),
    (
        "What is the time complexity of inserting a node at the beginning of a singly linked list when the head pointer is available?",
        "O(1)",
        "O(n)",
        "O(log n)",
        "O(n²)",
        "A",
        "Insertion at the beginning only requires updating the new node's next reference and the head pointer.",
        "Intermediate"
    ),
    (
        "Which data structure is generally more suitable when frequent insertions and deletions are required at known positions?",
        "Linked list",
        "Fixed-size array",
        "String",
        "Integer",
        "A",
        "A linked list can insert or delete a node at a known position by changing references without shifting other elements.",
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

    print("EEE Python Topic 7 added successfully!")
    print("Subject:", subject)
    print("Topic:", topic)
    print("New questions added:", inserted)
    print("Existing questions skipped:", skipped)

except Exception as error:
    connection.rollback()
    print("Error:", error)

finally:
    connection.close()
