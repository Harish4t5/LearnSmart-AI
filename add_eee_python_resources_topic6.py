
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "database" / "ideathon2k26.db"

connection = sqlite3.connect(DB_PATH)
cursor = connection.cursor()

subject = "Data Structure with Python Program"
topic = "Searching and Sorting"

resources = [
    (
        subject,
        topic,
        "Beginner",
        "Article",
        "Searching and Sorting - Study Notes",
        "",
        """SEARCHING AND SORTING

1. Searching

Searching is the process of finding a particular element
in a collection of data.

2. Linear Search

Linear search checks elements one by one until the target
is found or the collection ends.

Example:
numbers = [10, 20, 30, 40]
target = 30

for i in range(len(numbers)):
    if numbers[i] == target:
        print("Found at index:", i)
        break

Time Complexity:
Best case: O(1)
Average case: O(n)
Worst case: O(n)

Advantages:
- Simple to implement.
- Works on sorted and unsorted data.

3. Binary Search

Binary search repeatedly divides the search interval
into two halves.

Important:
The input data must be sorted.

Example:
numbers = [10, 20, 30, 40, 50]
target = 40

left = 0
right = len(numbers) - 1

while left <= right:
    mid = (left + right) // 2

    if numbers[mid] == target:
        print("Found at index:", mid)
        break
    elif numbers[mid] < target:
        left = mid + 1
    else:
        right = mid - 1

Time Complexity:
Best case: O(1)
Average case: O(log n)
Worst case: O(log n)

4. Sorting

Sorting arranges data in a particular order,
usually ascending or descending.

5. Bubble Sort

Repeatedly compares adjacent elements and swaps them
when they are in the wrong order.

Time Complexity:
Average and worst case: O(n^2)
Best case with an optimized implementation: O(n)

6. Selection Sort

Finds the smallest element from the unsorted portion
and places it at the correct position.

Time Complexity:
Best, average and worst case: O(n^2)

7. Insertion Sort

Builds a sorted portion by inserting each new element
into its correct position.

Time Complexity:
Best case: O(n)
Average and worst case: O(n^2)

8. Python Sorting Functions

sort():
Sorts a list in place.

Example:
numbers = [4, 2, 1, 3]
numbers.sort()

sorted():
Returns a new sorted list.

Example:
numbers = [4, 2, 1, 3]
result = sorted(numbers)

Remember:
Linear Search -> O(n) worst case.
Binary Search -> O(log n) worst case.
Binary Search requires sorted data.
Bubble, Selection and Insertion Sort -> O(n^2) average case."""
    ),
    (
        subject,
        topic,
        "Intermediate",
        "Documentation",
        "Python Sorting Techniques Documentation",
        "https://docs.python.org/3/howto/sorting.html",
        "Official Python guide explaining sorted(), list.sort(), "
        "sorting keys, reverse ordering and stable sorting."
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

    print("Data Structure with Python - Topic 6 resources processed!")
    print("Inserted:", inserted)
    print("Skipped:", skipped)

except Exception as error:
    connection.rollback()
    print("Error:", error)

finally:
    connection.close()
