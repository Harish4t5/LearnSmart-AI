
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "database" / "ideathon2k26.db"

connection = sqlite3.connect(DB_PATH)
cursor = connection.cursor()

subject = "Data Structure with Python Program"
topic = "Linked Lists"

resources = [
    (
        subject,
        topic,
        "Beginner",
        "Article",
        "Linked Lists - Study Notes",
        "",
        """LINKED LISTS

1. What is a Linked List?

A linked list is a linear data structure made up of nodes.
Each node stores data and a reference to another node.

Unlike arrays, linked-list nodes do not need to occupy
continuous memory locations.

2. Structure of a Node

A node generally contains:
- Data: Stores the actual value.
- Next: Stores a reference to the next node.

The first node is called the head.
The last node usually points to None.

3. Types of Linked Lists

Singly Linked List:
Each node points to the next node.

Doubly Linked List:
Each node contains references to both the previous
and next nodes.

Circular Linked List:
The last node points back to the first node.

4. Basic Operations

Traversal:
Visit nodes one by one.

Insertion:
Add a new node at the beginning, end or a given position.

Deletion:
Remove a node from the list.

Searching:
Find a node containing a particular value.

5. Simple Linked List in Python

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

first = Node(10)
second = Node(20)
third = Node(30)

first.next = second
second.next = third

current = first

while current is not None:
    print(current.data)
    current = current.next

Output:
10
20
30

6. Time Complexity

For a singly linked list:

Access by index: O(n)
Search: O(n)
Insert at head: O(1)
Delete at head: O(1)

Insertion or deletion at a known node can be O(1),
provided the required references are already available.

7. Advantages

- Dynamic size.
- Efficient insertion and deletion at the head.
- Does not require contiguous memory allocation.

8. Limitations

- No direct random access by index.
- Extra memory is required for references.
- Traversal is generally sequential.

9. Applications

- Implementing stacks and queues.
- Graph adjacency lists.
- Memory management concepts.
- Playlists and navigation systems.

Remember:
Node -> Data + Reference.
Head -> First node.
None -> Marks the end of a normal singly linked list."""
    ),
    (
        subject,
        topic,
        "Intermediate",
        "Documentation",
        "Python Classes Documentation",
        "https://docs.python.org/3/tutorial/classes.html",
        "Official Python tutorial covering classes, objects, "
        "instance attributes and methods used to implement "
        "node-based data structures."
    )
]

inserted = 0
skipped = 0

try:
    for resource in resources:
        cursor.execute("""
            SELECT id FROM learning_resources
            WHERE subject = ?
            AND topic = ?
            AND level = ?
            AND resource_type = ?
            AND title = ?
        """, (
            resource[0], resource[1], resource[2],
            resource[3], resource[4]
        ))

        if cursor.fetchone():
            skipped += 1
            continue

        cursor.execute("""
            INSERT INTO learning_resources
            (subject, topic, level, resource_type, title, url, description)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, resource)

        inserted += 1

    connection.commit()

    print("Data Structure with Python - Topic 7 resources processed!")
    print("Inserted:", inserted)
    print("Skipped:", skipped)

except Exception as error:
    connection.rollback()
    print("Error:", error)

finally:
    connection.close()
