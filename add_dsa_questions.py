
import sqlite3

connection = sqlite3.connect("database/ideathon2k26.db")
cursor = connection.cursor()

questions = [

    # Topic 1: Abstract Data Types
    (
        "Data Structures and Algorithms",
        "Unit 1 - Abstract Data Types",
        "What does an Abstract Data Type (ADT) primarily define?",
        "How data is physically stored",
        "What operations are supported and their behavior",
        "The programming language used",
        "The memory address of each element",
        "B",
        "An ADT defines the operations and behavior of a data type without specifying its internal implementation."
    ),

    (
        "Data Structures and Algorithms",
        "Unit 1 - Abstract Data Types",
        "Which of the following is an example of an ADT?",
        "Stack",
        "Integer variable",
        "CPU register",
        "Memory address",
        "A",
        "A stack is an ADT that follows the Last In, First Out (LIFO) principle."
    ),

    # Topic 2: Complexity Analysis
    (
        "Data Structures and Algorithms",
        "Unit 1 - Complexity Analysis",
        "What does the worst-case time complexity represent?",
        "Minimum time taken by an algorithm",
        "Maximum time taken for inputs of a given size",
        "Average memory used",
        "Time taken for the smallest input",
        "B",
        "Worst-case complexity describes the maximum time an algorithm may require for an input of a particular size."
    ),

    (
        "Data Structures and Algorithms",
        "Unit 1 - Complexity Analysis",
        "What is the time complexity of accessing an array element using its index?",
        "O(n)",
        "O(log n)",
        "O(1)",
        "O(n²)",
        "C",
        "Array elements can be accessed directly using their index, so access takes constant time."
    ),

    # Topic 3: Asymptotic Analysis
    (
        "Data Structures and Algorithms",
        "Unit 1 - Asymptotic Analysis",
        "Which notation represents an asymptotic upper bound?",
        "Big O",
        "Big Omega",
        "Big Theta",
        "Little Omega",
        "A",
        "Big O notation describes an asymptotic upper bound on the growth of a function."
    ),

    # Topic 4: Recursion
    (
        "Data Structures and Algorithms",
        "Unit 1 - Recursion",
        "What is essential to prevent infinite recursion?",
        "A global variable",
        "A base case",
        "A sorting operation",
        "A linked list",
        "B",
        "A base case provides the stopping condition for recursive function calls."
    ),

    # Topic 5: Arrays and Linked Lists
    (
        "Data Structures and Algorithms",
        "Unit 1 - Arrays and Linked Lists",
        "Which statement about an array is correct?",
        "Elements are always stored at random memory locations",
        "Elements are stored in contiguous memory locations",
        "Array elements cannot be accessed using an index",
        "Array size always changes automatically",
        "B",
        "Array elements are stored in contiguous memory locations, allowing direct indexed access."
    ),

    (
        "Data Structures and Algorithms",
        "Unit 1 - Arrays and Linked Lists",
        "Which linked list node generally contains data and a pointer to the next node?",
        "Doubly linked list node",
        "Singly linked list node",
        "Tree node",
        "Graph node",
        "B",
        "A singly linked list node contains data and a link to the next node."
    ),

    # Topic 6: Stacks
    (
        "Data Structures and Algorithms",
        "Unit 1 - Stacks",
        "Which principle does a stack follow?",
        "FIFO",
        "LIFO",
        "Random access",
        "Priority based access",
        "B",
        "A stack follows Last In, First Out. The last inserted element is removed first."
    ),

    # Topic 7: Queues
    (
        "Data Structures and Algorithms",
        "Unit 1 - Queues",
        "Which principle does a standard queue follow?",
        "LIFO",
        "FIFO",
        "Random access",
        "Last come, first served",
        "B",
        "A standard queue follows First In, First Out. The first inserted element is removed first."
    ),

    # Topic 8: Sorting
    (
        "Data Structures and Algorithms",
        "Unit 1 - Sorting",
        "Which sorting algorithm uses the divide-and-conquer technique?",
        "Linear Search",
        "Merge Sort",
        "Bubble Sort",
        "Selection Sort",
        "B",
        "Merge Sort divides the array into smaller parts, sorts them and merges the sorted parts."
    ),

    (
        "Data Structures and Algorithms",
        "Unit 1 - Sorting",
        "What is the average-case time complexity of Quick Sort?",
        "O(n)",
        "O(log n)",
        "O(n log n)",
        "O(n²)",
        "C",
        "Quick Sort has average-case time complexity O(n log n), although its worst case is O(n²)."
    )
]

inserted = 0
skipped = 0

try:
    for question in questions:

        existing = cursor.execute("""
            SELECT id
            FROM quiz_questions
            WHERE subject = ?
            AND topic = ?
            AND question = ?
            LIMIT 1
        """, (question[0], question[1], question[2])).fetchone()

        if existing:
            skipped += 1
            continue

        cursor.execute("""
            INSERT INTO quiz_questions (
                subject,
                topic,
                question,
                option_a,
                option_b,
                option_c,
                option_d,
                correct_answer,
                explanation
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, question)

        inserted += 1

    connection.commit()

    print("DSA question bank updated successfully!")
    print("New questions inserted:", inserted)
    print("Duplicate questions skipped:", skipped)

    total = cursor.execute("""
        SELECT COUNT(*)
        FROM quiz_questions
        WHERE subject = ?
    """, ("Data Structures and Algorithms",)).fetchone()[0]

    print("Total DSA questions:", total)

except Exception as error:
    connection.rollback()
    print("Error:", error)

finally:
    connection.close()
