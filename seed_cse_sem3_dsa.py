
import sqlite3

DB_PATH = "database/ideathon2k26.db"

def main():
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
        """, ("CSE-AIML", 3, "CSE-301"))

        result = cursor.fetchone()

        if not result:
            raise ValueError("CSE-301 subject was not found.")

        subject_id = result[0]

        syllabus = {
            1: {
                "title": "Refresher of Data Structures",
                "topics": [
                    "Abstract Data Types and Data Structures",
                    "Principles and Patterns of Data Structures",
                    "Basic Complexity Analysis",
                    "Best, Worst and Average Cases",
                    "Asymptotic Analysis",
                    "Analyzing Programs",
                    "Space Bounds",
                    "Linear, Binary and Multiple Recursions",
                    "Sorting and Selection",
                    "Linear Sorting",
                    "Divide and Conquer Based Sorting",
                    "Analysis using Recurrence Tree Method",
                    "Merge Sort",
                    "Quick Sort",
                    "Studying Sorting through an Algorithmic Lens",
                    "Arrays",
                    "Lists",
                    "Array Based List Implementation",
                    "Linked Lists",
                    "Linked List ADT",
                    "Singly Linked List",
                    "Doubly Linked List",
                    "Circular Linked List",
                    "Stack ADT",
                    "Array Based Stacks",
                    "Linked Stacks",
                    "Implementing Recursion using Stacks",
                    "Stack Applications",
                    "Queue ADT",
                    "Array Based Queue",
                    "Linked Queue",
                    "Double-ended Queue",
                    "Circular Queue",
                    "Queue Applications"
                ]
            },

            2: {
                "title": "Trees",
                "topics": [
                    "Tree Definition and Properties",
                    "Tree ADT",
                    "Basic Tree Traversals",
                    "Binary Tree",
                    "Data Structure for Representing Trees",
                    "Linked Structure for Binary Tree",
                    "Array Based Implementation of Binary Tree",
                    "Priority Queue ADT",
                    "Implementing Priority Queue using List",
                    "Heaps",
                    "Map ADT",
                    "List Based Map Implementation",
                    "Hash Tables",
                    "Dictionary ADT",
                    "Skip Lists",
                    "Skip List Implementation",
                    "Skip List Complexity"
                ]
            },

            3: {
                "title": "Search Trees",
                "topics": [
                    "Binary Search Tree",
                    "AVL Tree",
                    "Segment Trees",
                    "B-Trees",
                    "Implementation of Search Trees",
                    "External Memory Sorting",
                    "External Memory Searching",
                    "Graph ADT",
                    "Data Structures for Graphs",
                    "Graph Traversal",
                    "Transitive Closure",
                    "Directed Acyclic Graphs",
                    "Weighted Graphs",
                    "Shortest Paths",
                    "Minimum Spanning Tree",
                    "Greedy Methods for Minimum Spanning Tree"
                ]
            }
        }

        units_added = 0
        topics_added = 0

        for unit_number, unit_data in syllabus.items():

            cursor.execute("""
                SELECT id FROM syllabus_units
                WHERE subject_id = ? AND unit_number = ?
            """, (subject_id, unit_number))

            existing_unit = cursor.fetchone()

            if existing_unit:
                unit_id = existing_unit[0]
            else:
                cursor.execute("""
                    INSERT INTO syllabus_units
                    (subject_id, unit_number, unit_title)
                    VALUES (?, ?, ?)
                """, (subject_id, unit_number, unit_data["title"]))

                unit_id = cursor.lastrowid
                units_added += 1

            for order, topic in enumerate(unit_data["topics"], start=1):

                cursor.execute("""
                    SELECT id FROM syllabus_topics
                    WHERE unit_id = ? AND topic_name = ?
                """, (unit_id, topic))

                if cursor.fetchone():
                    continue

                cursor.execute("""
                    INSERT INTO syllabus_topics
                    (unit_id, topic_name, topic_order)
                    VALUES (?, ?, ?)
                """, (unit_id, topic, order))

                topics_added += 1

        conn.commit()

        print("CSE Semester 3 - CSE-301 import completed!")
        print("Units added:", units_added)
        print("Topics added:", topics_added)

    except Exception:
        conn.rollback()
        raise

    finally:
        conn.close()


if __name__ == "__main__":
    main()
