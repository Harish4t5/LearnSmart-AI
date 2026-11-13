
import sqlite3

DB_PATH = "database/ideathon2k26.db"

resources = [
    # Abstract Data Types
    ("Unit 1 - Abstract Data Types", "Beginner", "Article",
     "Introduction to Abstract Data Types",
     "https://www.geeksforgeeks.org/abstract-data-types/",
     "Understand ADTs, their operations and examples."),

    ("Unit 1 - Abstract Data Types", "Intermediate", "Practice",
     "Data Structures Practice",
     "https://www.hackerrank.com/domains/data-structures",
     "Practice implementing common data structures."),

    ("Unit 1 - Abstract Data Types", "Advanced", "Documentation",
     "Open Data Structures",
     "https://opendatastructures.org/",
     "Study data structure implementations and analysis."),

    # Arrays and Linked Lists
    ("Unit 1 - Arrays and Linked Lists", "Beginner", "Article",
     "Arrays in Data Structures",
     "https://www.geeksforgeeks.org/array-data-structure/",
     "Learn array operations and memory representation."),

    ("Unit 1 - Arrays and Linked Lists", "Intermediate", "Practice",
     "Array and Linked List Problems",
     "https://leetcode.com/problem-list/linked-list/",
     "Solve array and linked list coding problems."),

    ("Unit 1 - Arrays and Linked Lists", "Advanced", "Documentation",
     "Linked Lists",
     "https://www.programiz.com/dsa/linked-list",
     "Study linked list operations and implementations."),

    # Asymptotic Analysis
    ("Unit 1 - Asymptotic Analysis", "Beginner", "Article",
     "Asymptotic Analysis",
     "https://www.geeksforgeeks.org/analysis-of-algorithms-set-1-asymptotic-analysis/",
     "Understand Big O, Omega and Theta notations."),

    ("Unit 1 - Asymptotic Analysis", "Intermediate", "Practice",
     "Big O Practice",
     "https://www.hackerrank.com/domains/algorithms",
     "Practice algorithm analysis and problem solving."),

    ("Unit 1 - Asymptotic Analysis", "Advanced", "Documentation",
     "Introduction to Algorithms",
     "https://mitpress.mit.edu/9780262046305/introduction-to-algorithms/",
     "Explore advanced algorithm analysis concepts."),

    # Complexity Analysis
    ("Unit 1 - Complexity Analysis", "Beginner", "Article",
     "Time and Space Complexity",
     "https://www.geeksforgeeks.org/understanding-time-complexity-simple-examples/",
     "Learn time and space complexity with examples."),

    ("Unit 1 - Complexity Analysis", "Intermediate", "Practice",
     "Algorithm Complexity Problems",
     "https://leetcode.com/problemset/",
     "Analyze the efficiency of coding solutions."),

    ("Unit 1 - Complexity Analysis", "Advanced", "Documentation",
     "MIT Introduction to Algorithms",
     "https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/",
     "Study advanced algorithm design and analysis."),

    # Stacks
    ("Unit 1 - Stacks", "Beginner", "Article",
     "Stack Data Structure",
     "https://www.geeksforgeeks.org/stack-data-structure/",
     "Learn push, pop and peek operations."),

    ("Unit 1 - Stacks", "Intermediate", "Practice",
     "Stack Coding Problems",
     "https://leetcode.com/problem-list/stack/",
     "Practice stack-based programming problems."),

    ("Unit 1 - Stacks", "Advanced", "Documentation",
     "Stack Data Structure Tutorial",
     "https://www.programiz.com/dsa/stack",
     "Explore stack implementation and applications."),

    # Queues
    ("Unit 1 - Queues", "Beginner", "Article",
     "Queue Data Structure",
     "https://www.geeksforgeeks.org/queue-data-structure/",
     "Understand FIFO and queue operations."),

    ("Unit 1 - Queues", "Intermediate", "Practice",
     "Queue Coding Problems",
     "https://leetcode.com/problem-list/queue/",
     "Solve queue and deque problems."),

    ("Unit 1 - Queues", "Advanced", "Documentation",
     "Queue Data Structure Tutorial",
     "https://www.programiz.com/dsa/queue",
     "Study circular queues and queue applications."),

    # Recursion
    ("Unit 1 - Recursion", "Beginner", "Article",
     "Introduction to Recursion",
     "https://www.geeksforgeeks.org/introduction-to-recursion-2/",
     "Understand recursive functions and base cases."),

    ("Unit 1 - Recursion", "Intermediate", "Practice",
     "Recursion Practice Problems",
     "https://leetcode.com/problem-list/recursion/",
     "Practice recursion-based coding problems."),

    ("Unit 1 - Recursion", "Advanced", "Documentation",
     "MIT Introduction to Algorithms",
     "https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/",
     "Explore recursion trees and recursive algorithms."),

    # Sorting
    ("Unit 1 - Sorting", "Beginner", "Article",
     "Sorting Algorithms",
     "https://www.geeksforgeeks.org/sorting-algorithms/",
     "Learn basic sorting algorithms and their working."),

    ("Unit 1 - Sorting", "Intermediate", "Practice",
     "Sorting Algorithm Practice",
     "https://www.hackerrank.com/domains/algorithms",
     "Practice sorting and selection problems."),

    ("Unit 1 - Sorting", "Advanced", "Documentation",
     "Sorting Algorithms Explained",
     "https://www.programiz.com/dsa/sorting-algorithm",
     "Study advanced sorting algorithms and complexity."),

    # UNIT 2 - Tree Fundamentals
    ("Unit 2 - Tree Fundamentals", "Beginner", "Article",
     "Introduction to Trees",
     "https://www.geeksforgeeks.org/introduction-to-tree-data-structure/",
     "Learn tree terminology, properties and basic concepts."),

    ("Unit 2 - Tree Fundamentals", "Intermediate", "Article",
     "Tree Data Structure Tutorial",
     "https://www.programiz.com/dsa/trees",
     "Understand tree structures and their applications."),

    ("Unit 2 - Tree Fundamentals", "Advanced", "Practice",
     "Tree Problems",
     "https://leetcode.com/tag/tree/",
     "Solve advanced tree-based programming problems."),

    # UNIT 2 - Tree Traversals
    ("Unit 2 - Tree Traversals", "Beginner", "Article",
     "Tree Traversal",
     "https://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder/",
     "Learn inorder, preorder and postorder traversal."),

    ("Unit 2 - Tree Traversals", "Intermediate", "Practice",
     "Binary Tree Traversal Problems",
     "https://leetcode.com/tag/tree/",
     "Practice different tree traversal techniques."),

    ("Unit 2 - Tree Traversals", "Advanced", "Practice",
     "Advanced Tree Problems",
     "https://leetcode.com/tag/binary-tree/",
     "Solve challenging binary tree traversal problems."),

    # UNIT 2 - Binary Trees
    ("Unit 2 - Binary Trees", "Beginner", "Article",
     "Binary Tree Introduction",
     "https://www.geeksforgeeks.org/binary-tree-data-structure/",
     "Understand binary tree structure and properties."),

    ("Unit 2 - Binary Trees", "Intermediate", "Article",
     "Binary Tree Implementation",
     "https://www.programiz.com/dsa/binary-tree",
     "Study binary tree representation and implementation."),

    ("Unit 2 - Binary Trees", "Advanced", "Practice",
     "Binary Tree Coding Problems",
     "https://leetcode.com/tag/binary-tree/",
     "Practice advanced binary tree problems."),

    # UNIT 2 - Priority Queues
    ("Unit 2 - Priority Queues", "Beginner", "Article",
     "Priority Queue Introduction",
     "https://www.geeksforgeeks.org/priority-queue-in-cpp-stl/",
     "Learn priority queue operations and applications."),

    ("Unit 2 - Priority Queues", "Intermediate", "Practice",
     "Priority Queue Problems",
     "https://www.geeksforgeeks.org/problems/",
     "Practice priority queue and scheduling problems."),

    ("Unit 2 - Priority Queues", "Advanced", "Documentation",
     "C++ Priority Queue Reference",
     "https://en.cppreference.com/w/cpp/container/priority_queue",
     "Explore priority queue operations and complexity in C++."),

    # UNIT 2 - Heaps
    ("Unit 2 - Heaps", "Beginner", "Article",
     "Introduction to Heap",
     "https://www.geeksforgeeks.org/heap-data-structure/",
     "Understand min heap, max heap and heap properties."),

    ("Unit 2 - Heaps", "Intermediate", "Article",
     "Heap Data Structure",
     "https://www.programiz.com/dsa/heap-data-structure",
     "Learn heap insertion, deletion and implementation."),

    ("Unit 2 - Heaps", "Advanced", "Practice",
     "Heap Coding Problems",
     "https://leetcode.com/tag/heap-priority-queue/",
     "Solve advanced heap and priority queue problems."),

    # UNIT 2 - Maps and Dictionaries
    ("Unit 2 - Maps and Dictionaries", "Beginner", "Article",
     "Map Data Structure",
     "https://www.geeksforgeeks.org/map-in-cpp-stl/",
     "Understand key-value pairs and map operations."),

    ("Unit 2 - Maps and Dictionaries", "Intermediate", "Documentation",
     "C++ Map Reference",
     "https://en.cppreference.com/w/cpp/container/map",
     "Study map operations, ordering and complexity."),

    ("Unit 2 - Maps and Dictionaries", "Advanced", "Practice",
     "Hash Map Problems",
     "https://leetcode.com/tag/hash-table/",
     "Solve advanced map and dictionary problems."),

    # UNIT 2 - Hash Tables
    ("Unit 2 - Hash Tables", "Beginner", "Article",
     "Introduction to Hashing",
     "https://www.geeksforgeeks.org/hashing-data-structure/",
     "Learn hash functions, hash tables and collisions."),

    ("Unit 2 - Hash Tables", "Intermediate", "Article",
     "Hash Table Implementation",
     "https://www.programiz.com/dsa/hash-table",
     "Understand insertion, searching and deletion."),

    ("Unit 2 - Hash Tables", "Advanced", "Practice",
     "Hash Table Coding Problems",
     "https://leetcode.com/tag/hash-table/",
     "Practice advanced hashing problems."),

    # UNIT 2 - Skip Lists
    ("Unit 2 - Skip Lists", "Beginner", "Article",
     "Introduction to Skip Lists",
     "https://www.geeksforgeeks.org/skip-list/",
     "Understand skip list structure and basic operations."),

    ("Unit 2 - Skip Lists", "Intermediate", "Article",
     "Skip List Data Structure",
     "https://en.wikipedia.org/wiki/Skip_list",
     "Study searching, insertion and deletion in skip lists."),

    ("Unit 2 - Skip Lists", "Advanced", "Documentation",
     "Skip List Research Paper",
     "https://www.cs.umd.edu/~meesh/351/mount/lectures/lect14-skiplist.pdf",
     "Explore skip list design and expected complexity.")

]

connection = sqlite3.connect(DB_PATH)

try:
    cursor = connection.cursor()

    inserted = 0
    skipped = 0

    for topic, level, resource_type, title, url, description in resources:

        cursor.execute("""
            INSERT OR IGNORE INTO learning_resources
            (subject, topic, level, resource_type, title, url, description)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            "Data Structures and Algorithms",
            topic,
            level,
            resource_type,
            title,
            url,
            description
        ))

        if cursor.rowcount == 1:
            inserted += 1
        else:
            skipped += 1

    connection.commit()

    print("DSA learning resources processed successfully!")
    print("New resources inserted:", inserted)
    print("Existing resources skipped:", skipped)

finally:
    connection.close()
