
import sqlite3

DB_PATH = "database/ideathon2k26.db"

experiments = [
    "Implement Stack Using Arrays and Evaluate a Given Postfix Expression",
    "Implement Circular Queue Using Arrays",
    "Implement Double Ended Queue (Deque) Using Arrays",
    "Programs Based on Applications of Stacks and Queues",
    "Implement Singly Linked List and Doubly Linked List",
    "Implement Stack and Queue Using Linked Lists",
    "Create a Binary Search Tree and Perform Minimum, Maximum, Search, Predecessor, Deletion and Application Operations",
    "Construct an AVL Tree and Implement Deletion of a Key",
    "Implement Hashing Using Separate Chaining and Open Addressing",
    "Implement Insertion Sort, Merge Sort, Quick Sort, Heap Sort, Radix Sort and Shell Sort",
    "Implement Graph Traversals Using BFS and DFS",
    "Find Minimum Spanning Tree Using Prim's and Kruskal's Algorithms",
    "Implement Dijkstra's Algorithm Using Priority Queue",
    "Find Euler's Path",
    "Find Biconnected Components and Strongly Connected Components",
    "Implement Creation and Insertion Operations of a Treap",
    "Implement Creation, Insertion, Deletion and Printing of a Bd-Tree",
    "Implement Creation, Insertion, Deletion and Printing of Bd+-Tree and B*-Tree",
    "Implement Creation, Insertion, Deletion and Printing of a Trie",
    "Implement Creation, Insertion, Deletion and Printing of a C-Trie",
]

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

try:
    cursor.execute("""
        SELECT s.id
        FROM subjects s
        JOIN semesters sem ON s.semester_id = sem.id
        JOIN curricula c ON sem.curriculum_id = c.id
        JOIN branches b ON c.branch_id = b.id
        WHERE b.branch_code = ?
          AND sem.semester_number = ?
          AND s.course_code = ?
          AND c.academic_year = ?
    """, ("CSE-AIML", 3, "CSE-301P", "2024-25"))

    result = cursor.fetchone()

    if not result:
        raise ValueError("CSE-301P subject not found!")

    subject_id = result[0]

    cursor.execute("""
        SELECT id FROM syllabus_units
        WHERE subject_id = ? AND unit_number = 1
    """, (subject_id,))

    existing_unit = cursor.fetchone()

    if existing_unit:
        unit_id = existing_unit[0]
        units_added = 0
    else:
        cursor.execute("""
            INSERT INTO syllabus_units
            (subject_id, unit_number, unit_title)
            VALUES (?, ?, ?)
        """, (subject_id, 1, "List of Experiments"))

        unit_id = cursor.lastrowid
        units_added = 1

    topics_added = 0

    for order, experiment in enumerate(experiments, start=1):
        cursor.execute("""
            SELECT id FROM syllabus_topics
            WHERE unit_id = ? AND topic_order = ?
        """, (unit_id, order))

        if cursor.fetchone():
            continue

        cursor.execute("""
            INSERT INTO syllabus_topics
            (unit_id, topic_name, topic_order)
            VALUES (?, ?, ?)
        """, (unit_id, experiment, order))

        topics_added += 1

    conn.commit()

    print("CSE Semester 3 - CSE-301P DSA Lab import completed!")
    print("Units added:", units_added)
    print("Experiments added:", topics_added)

except Exception:
    conn.rollback()
    raise

finally:
    conn.close()
