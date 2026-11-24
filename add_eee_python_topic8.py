
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "database" / "ideathon2k26.db"

connection = sqlite3.connect(DB_PATH)

subject = "Data Structure with Python Program"
branch_code = "EEE"
semester = 3
topic = "Trees and Graphs"

questions = [
    (
        "Which data structure represents hierarchical relationships?",
        "Queue",
        "Stack",
        "Tree",
        "Array",
        "C",
        "A tree is a hierarchical data structure consisting of nodes connected by edges.",
        "Beginner"
    ),
    (
        "What is the topmost node of a tree called?",
        "Leaf",
        "Root",
        "Child",
        "Sibling",
        "B",
        "The root is the topmost node of a tree.",
        "Beginner"
    ),
    (
        "What is a node with no children called?",
        "Root node",
        "Parent node",
        "Leaf node",
        "Internal node",
        "C",
        "A leaf node is a node that has no children.",
        "Beginner"
    ),
    (
        "In a binary tree, what is the maximum number of children a node can have?",
        "1",
        "2",
        "3",
        "Unlimited",
        "B",
        "A binary tree allows each node to have at most two children.",
        "Beginner"
    ),
    (
        "Which data structure is commonly used to implement Breadth-First Search (BFS)?",
        "Stack",
        "Queue",
        "Array only",
        "Linked list only",
        "B",
        "BFS uses a queue to explore nodes level by level.",
        "Beginner"
    ),
    (
        "Which data structure is commonly used in iterative Depth-First Search (DFS)?",
        "Queue",
        "Stack",
        "Heap only",
        "Hash table",
        "B",
        "Iterative DFS uses a stack to keep track of nodes to visit.",
        "Intermediate"
    ),
    (
        "In a binary search tree, values in the left subtree of a node are generally:",
        "Greater than the node",
        "Equal to all other values",
        "Less than the node",
        "Always zero",
        "C",
        "In a standard binary search tree with distinct keys, values in the left subtree are smaller than the node's value.",
        "Intermediate"
    ),
    (
        "What is the maximum number of nodes at level 2 of a binary tree, when the root is at level 0?",
        "2",
        "3",
        "4",
        "8",
        "C",
        "The maximum number of nodes at level L in a binary tree is 2^L. At level 2, it is 2^2 = 4.",
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

    print("EEE Python Topic 8 added successfully!")
    print("Subject:", subject)
    print("Topic:", topic)
    print("New questions added:", inserted)
    print("Existing questions skipped:", skipped)

except Exception as error:
    connection.rollback()
    print("Error:", error)

finally:
    connection.close()
