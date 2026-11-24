
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "database" / "ideathon2k26.db"

connection = sqlite3.connect(DB_PATH)

subject = "Data Structure with Python Program"
branch_code = "EEE"
semester = 3
topic = "Stacks and Queues"

questions = [
    (
        "Which principle does a stack follow?",
        "FIFO",
        "LIFO",
        "FILO only",
        "Random access",
        "B",
        "A stack follows Last In, First Out (LIFO), meaning the most recently inserted element is removed first.",
        "Beginner"
    ),
    (
        "Which principle does a queue follow?",
        "LIFO",
        "Random order",
        "FIFO",
        "FILO",
        "C",
        "A queue follows First In, First Out (FIFO), meaning the first inserted element is removed first.",
        "Beginner"
    ),
    (
        "Which operation inserts an element into a stack?",
        "Pop",
        "Dequeue",
        "Push",
        "Peek",
        "C",
        "Push is the operation used to insert an element into a stack.",
        "Beginner"
    ),
    (
        "Which operation removes an element from the front of a queue?",
        "Push",
        "Pop",
        "Enqueue",
        "Dequeue",
        "D",
        "Dequeue removes an element from the front of a queue.",
        "Beginner"
    ),
    (
        "What is the condition called when an element is removed from an empty stack?",
        "Overflow",
        "Underflow",
        "Collision",
        "Traversal",
        "B",
        "Stack underflow occurs when a removal operation is attempted on an empty stack.",
        "Beginner"
    ),
    (
        "A stack receives the elements 10, 20, and 30 in that order. What is the order of removal?",
        "10, 20, 30",
        "20, 10, 30",
        "30, 20, 10",
        "10, 30, 20",
        "C",
        "A stack follows LIFO, so the last inserted element 30 is removed first.",
        "Intermediate"
    ),
    (
        "A queue receives 5, 10, and 15 in that order. Which element is removed first?",
        "15",
        "10",
        "5",
        "None",
        "C",
        "A queue follows FIFO, so the first inserted element, 5, is removed first.",
        "Intermediate"
    ),
    (
        "What is the time complexity of push and pop operations in a stack implemented using a Python list at the end of the list?",
        "O(1) amortized",
        "O(n) always",
        "O(log n)",
        "O(n log n)",
        "A",
        "Appending and popping at the end of a Python list take O(1) amortized time.",
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

    print("EEE Python Topic 5 added successfully!")
    print("Subject:", subject)
    print("Topic:", topic)
    print("New questions added:", inserted)
    print("Existing questions skipped:", skipped)

except Exception as error:
    connection.rollback()
    print("Error:", error)

finally:
    connection.close()
