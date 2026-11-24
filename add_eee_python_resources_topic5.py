
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "database" / "ideathon2k26.db"

connection = sqlite3.connect(DB_PATH)
cursor = connection.cursor()

subject = "Data Structure with Python Program"
topic = "Stacks and Queues"

resources = [
    (
        subject,
        topic,
        "Beginner",
        "Article",
        "Stacks and Queues - Study Notes",
        "",
        """STACKS AND QUEUES

1. What is a Data Structure?

A data structure is a way of organizing and storing data
so that it can be accessed and modified efficiently.

2. Stack

A stack is a linear data structure that follows LIFO:
Last In, First Out.

The element inserted last is removed first.

Main operations:
- push(): Inserts an element.
- pop(): Removes the top element.
- peek(): Returns the top element without removing it.
- is_empty(): Checks whether the stack is empty.

Example:
stack = []
stack.append(10)
stack.append(20)
stack.append(30)

print(stack.pop())

Output: 30

3. Stack Applications

- Function calls and recursion.
- Undo and redo operations.
- Expression evaluation.
- Parentheses matching.
- Backtracking.

4. Queue

A queue is a linear data structure that follows FIFO:
First In, First Out.

The element inserted first is removed first.

Main operations:
- enqueue(): Inserts an element at the rear.
- dequeue(): Removes an element from the front.
- front(): Returns the first element.
- is_empty(): Checks whether the queue is empty.

5. Queue Example in Python

from collections import deque

queue = deque()

queue.append(10)
queue.append(20)
queue.append(30)

print(queue.popleft())

Output: 10

6. Types of Queues

Simple Queue:
Insertion at the rear and deletion at the front.

Circular Queue:
The last position connects back to the first position.

Priority Queue:
Elements are removed according to priority.

Deque:
Allows insertion and deletion at both ends.

7. Stack vs Queue

Stack:
- Follows LIFO.
- Insertion and deletion happen at the top.

Queue:
- Follows FIFO.
- Insertion happens at the rear.
- Deletion happens at the front.

8. Overflow and Underflow

Overflow:
Attempting to insert into a full fixed-capacity structure.

Underflow:
Attempting to remove an element from an empty structure.

Remember:
Stack -> LIFO.
Queue -> FIFO.
Python list can implement a simple stack.
collections.deque is useful for efficient queue operations."""
    ),
    (
        subject,
        topic,
        "Intermediate",
        "Documentation",
        "Python Collections Documentation",
        "https://docs.python.org/3/library/collections.html#collections.deque",
        "Official Python documentation for collections.deque, "
        "including append, appendleft, pop and popleft operations."
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

    print("Data Structure with Python - Topic 5 resources processed!")
    print("Inserted:", inserted)
    print("Skipped:", skipped)

except Exception as error:
    connection.rollback()
    print("Error:", error)

finally:
    connection.close()
