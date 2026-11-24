
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "database" / "ideathon2k26.db"

connection = sqlite3.connect(DB_PATH)

subject = "Data Structure with Python Program"
branch_code = "EEE"
semester = 3
topic = "Searching and Sorting"

questions = [
    (
        "Which searching algorithm checks elements one by one?",
        "Binary Search",
        "Linear Search",
        "Merge Sort",
        "Quick Sort",
        "B",
        "Linear search checks each element sequentially until the target is found or the list ends.",
        "Beginner"
    ),
    (
        "Which searching algorithm requires the data to be sorted?",
        "Linear Search",
        "Binary Search",
        "Sequential Search",
        "None of these",
        "B",
        "Binary search works on sorted data because it repeatedly divides the search range into halves.",
        "Beginner"
    ),
    (
        "Which sorting algorithm repeatedly compares adjacent elements and swaps them if necessary?",
        "Merge Sort",
        "Bubble Sort",
        "Binary Search",
        "Linear Search",
        "B",
        "Bubble sort compares adjacent elements and swaps them when they are in the wrong order.",
        "Beginner"
    ),
    (
        "What is the main purpose of a sorting algorithm?",
        "To arrange data in a particular order",
        "To delete all elements",
        "To search only strings",
        "To reverse a program",
        "A",
        "Sorting arranges elements in a specified order, such as ascending or descending.",
        "Beginner"
    ),
    (
        "Which Python function returns a new sorted list?",
        "sort()",
        "sorted()",
        "order()",
        "arrange()",
        "B",
        "The sorted() function returns a new sorted list without modifying the original iterable.",
        "Beginner"
    ),
    (
        "What is the time complexity of binary search in the average case?",
        "O(n)",
        "O(n²)",
        "O(log n)",
        "O(1)",
        "C",
        "Binary search halves the search space at each step, resulting in O(log n) time complexity.",
        "Intermediate"
    ),
    (
        "What is the worst-case time complexity of linear search?",
        "O(1)",
        "O(log n)",
        "O(n)",
        "O(n log n)",
        "C",
        "In the worst case, linear search checks all n elements, giving O(n) time complexity.",
        "Intermediate"
    ),
    (
        "What is the output of sorted([4, 1, 3, 2])?",
        "[4, 3, 2, 1]",
        "[1, 2, 3, 4]",
        "[2, 1, 4, 3]",
        "[4, 1, 3, 2]",
        "B",
        "The sorted() function arranges the elements in ascending order by default.",
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

    print("EEE Python Topic 6 added successfully!")
    print("Subject:", subject)
    print("Topic:", topic)
    print("New questions added:", inserted)
    print("Existing questions skipped:", skipped)

except Exception as error:
    connection.rollback()
    print("Error:", error)

finally:
    connection.close()
