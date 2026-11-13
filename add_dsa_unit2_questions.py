
import sqlite3

DB_PATH = "database/ideathon2k26.db"
SUBJECT = "Data Structures and Algorithms"

questions = [

    # ================= BEGINNER (10) =================

    (
        "Unit 2 - Tree Fundamentals",
        "Which statement best describes a tree data structure?",
        "A linear collection of elements",
        "A hierarchical collection of nodes",
        "A collection of sorted arrays",
        "A collection of unrelated variables",
        "B",
        "A tree is a hierarchical data structure consisting of nodes connected by edges.",
        "Beginner"
    ),
    (
        "Unit 2 - Tree Fundamentals",
        "What is the topmost node of a tree called?",
        "Leaf",
        "Child",
        "Root",
        "Parent",
        "C",
        "The root is the topmost node from which the tree structure begins.",
        "Beginner"
    ),
    (
        "Unit 2 - Tree Fundamentals",
        "A node with no children is called:",
        "Root node",
        "Leaf node",
        "Parent node",
        "Internal node",
        "B",
        "A leaf node is a node that has no children.",
        "Beginner"
    ),
    (
        "Unit 2 - Tree Traversals",
        "Which traversal visits the root before its subtrees?",
        "Inorder",
        "Postorder",
        "Preorder",
        "Level order",
        "C",
        "Preorder traversal follows Root, Left, Right.",
        "Beginner"
    ),
    (
        "Unit 2 - Tree Traversals",
        "Which traversal follows Left, Root, Right?",
        "Inorder",
        "Preorder",
        "Postorder",
        "Level order",
        "A",
        "Inorder traversal visits the left subtree, root, and then right subtree.",
        "Beginner"
    ),
    (
        "Unit 2 - Binary Trees",
        "In a binary tree, a node can have at most how many children?",
        "One",
        "Two",
        "Three",
        "Four",
        "B",
        "A binary tree allows each node to have at most two children.",
        "Beginner"
    ),
    (
        "Unit 2 - Priority Queues",
        "What is the main purpose of a priority queue?",
        "To process elements only alphabetically",
        "To process elements according to priority",
        "To reverse a linked list",
        "To store only duplicate elements",
        "B",
        "A priority queue removes or accesses elements according to their priority.",
        "Beginner"
    ),
    (
        "Unit 2 - Heaps",
        "Which data structure is commonly used to implement a priority queue?",
        "Heap",
        "Stack",
        "Graph",
        "Linked list only",
        "A",
        "A heap supports efficient priority queue operations.",
        "Beginner"
    ),
    (
        "Unit 2 - Maps and Dictionaries",
        "What does a Map ADT store?",
        "Only individual numbers",
        "Key-value pairs",
        "Only characters",
        "Only tree nodes",
        "B",
        "A Map ADT stores associations between keys and values.",
        "Beginner"
    ),
    (
        "Unit 2 - Hash Tables",
        "What is the main purpose of a hash function?",
        "To sort an array",
        "To generate an index from a key",
        "To reverse a tree",
        "To delete all elements",
        "B",
        "A hash function maps a key to an index in a hash table.",
        "Beginner"
    ),

    # ================= INTERMEDIATE (10) =================

    (
        "Unit 2 - Tree Fundamentals",
        "If a tree contains n nodes, how many edges does it have?",
        "n",
        "n + 1",
        "n - 1",
        "2n",
        "C",
        "A tree with n nodes has exactly n - 1 edges.",
        "Intermediate"
    ),
    (
        "Unit 2 - Tree Traversals",
        "Which traversal visits nodes level by level?",
        "Preorder",
        "Inorder",
        "Postorder",
        "Level order",
        "D",
        "Level-order traversal visits nodes one level at a time, generally using a queue.",
        "Intermediate"
    ),
    (
        "Unit 2 - Tree Traversals",
        "Which data structure is generally used for iterative level-order traversal?",
        "Stack",
        "Queue",
        "Hash table",
        "Priority queue",
        "B",
        "A queue processes nodes in FIFO order, which supports level-order traversal.",
        "Intermediate"
    ),
    (
        "Unit 2 - Binary Trees",
        "In an array-based binary tree using 0-based indexing, what is the index of the left child of a node at index i?",
        "2i",
        "2i + 1",
        "2i + 2",
        "i + 1",
        "B",
        "For 0-based indexing, the left child is at 2i + 1 and the right child is at 2i + 2.",
        "Intermediate"
    ),
    (
        "Unit 2 - Binary Trees",
        "In a linked representation of a binary tree, a node typically contains:",
        "Only one data field",
        "Data and two child pointers",
        "Only an array index",
        "Only a parent pointer",
        "B",
        "A linked binary tree node typically stores data, a left pointer, and a right pointer.",
        "Intermediate"
    ),
    (
        "Unit 2 - Priority Queues",
        "In a max-priority queue, which element is removed first?",
        "Element with the smallest priority",
        "Element with the largest priority",
        "The most recently inserted element always",
        "A random element",
        "B",
        "A max-priority queue gives priority to the element with the largest priority value.",
        "Intermediate"
    ),
    (
        "Unit 2 - Heaps",
        "Which property must a max-heap satisfy?",
        "Every parent is smaller than its children",
        "Every parent is greater than or equal to its children",
        "All elements must be equal",
        "The tree must be a binary search tree",
        "B",
        "In a max-heap, each parent has a value greater than or equal to its children.",
        "Intermediate"
    ),
    (
        "Unit 2 - Maps and Dictionaries",
        "Which operation retrieves a value associated with a given key in a Map ADT?",
        "Search by key",
        "Tree traversal",
        "Stack pop",
        "Queue dequeue",
        "A",
        "A Map ADT supports retrieving the value associated with a specified key.",
        "Intermediate"
    ),
    (
        "Unit 2 - Hash Tables",
        "What is a collision in a hash table?",
        "Two keys producing the same hash-table index",
        "Deleting a key",
        "Sorting the table",
        "Finding an empty array",
        "A",
        "A collision occurs when different keys map to the same table index.",
        "Intermediate"
    ),
    (
        "Unit 2 - Skip Lists",
        "What is the main purpose of additional levels in a skip list?",
        "To increase the size of every key",
        "To speed up searching by skipping multiple nodes",
        "To remove all pointers",
        "To convert the list into an array",
        "B",
        "Higher levels provide shortcuts that allow searches to skip over multiple nodes.",
        "Intermediate"
    ),

    # ================= ADVANCED (10) =================

    (
        "Unit 2 - Tree Fundamentals",
        "A full binary tree has 15 internal nodes. How many leaf nodes does it have?",
        "14",
        "15",
        "16",
        "30",
        "C",
        "In a full binary tree, the number of leaves is one more than the number of internal nodes. Therefore, 15 + 1 = 16.",
        "Advanced"
    ),
    (
        "Unit 2 - Tree Traversals",
        "What is the postorder traversal of a binary tree with root A, left child B, and right child C?",
        "A B C",
        "B A C",
        "B C A",
        "C A B",
        "C",
        "Postorder follows Left, Right, Root. Therefore, the sequence is B, C, A.",
        "Advanced"
    ),
    (
        "Unit 2 - Binary Trees",
        "A complete binary tree has 7 nodes. What is its minimum possible height when height is measured in edges?",
        "1",
        "2",
        "3",
        "6",
        "B",
        "A complete binary tree with 7 nodes can have 3 levels. Its height in edges is 3 - 1 = 2.",
        "Advanced"
    ),
    (
        "Unit 2 - Priority Queues",
        "What is the time complexity of inserting an element into a binary heap?",
        "O(1)",
        "O(log n)",
        "O(n)",
        "O(n log n)",
        "B",
        "Insertion may require moving the new element up the heap, taking O(log n) time.",
        "Advanced"
    ),
    (
        "Unit 2 - Heaps",
        "What is the time complexity of removing the maximum element from a max-heap containing n elements?",
        "O(1)",
        "O(log n)",
        "O(n)",
        "O(n log n)",
        "B",
        "Removing the maximum requires restoring the heap property, which takes O(log n) time.",
        "Advanced"
    ),
    (
        "Unit 2 - Heaps",
        "What is the time complexity of building a binary heap from n elements using the bottom-up heap construction method?",
        "O(n)",
        "O(log n)",
        "O(n log n)",
        "O(n²)",
        "A",
        "Bottom-up heap construction takes O(n) time, not O(n log n).",
        "Advanced"
    ),
    (
        "Unit 2 - Maps and Dictionaries",
        "What is the average-case search complexity in a well-implemented hash-based dictionary?",
        "O(1)",
        "O(log n)",
        "O(n)",
        "O(n²)",
        "A",
        "With a suitable hash function and controlled load factor, average search time is O(1).",
        "Advanced"
    ),
    (
        "Unit 2 - Hash Tables",
        "Which collision-resolution method stores colliding elements in a linked list at the same table index?",
        "Linear probing",
        "Quadratic probing",
        "Separate chaining",
        "Binary search",
        "C",
        "Separate chaining stores multiple elements in a bucket, commonly using a linked list.",
        "Advanced"
    ),
    (
        "Unit 2 - Hash Tables",
        "In open addressing, what happens when a collision occurs?",
        "The element is always discarded",
        "Another available table position is searched",
        "A linked list is always created",
        "The entire table is sorted",
        "B",
        "Open addressing resolves collisions by probing for another available position in the table.",
        "Advanced"
    ),
    (
        "Unit 2 - Skip Lists",
        "What is the expected search time complexity of a skip list with properly randomized levels?",
        "O(1)",
        "O(log n)",
        "O(n²)",
        "O(2ⁿ)",
        "B",
        "A randomized skip list provides expected O(log n) search time.",
        "Advanced"
    )
]

connection = sqlite3.connect(DB_PATH)
cursor = connection.cursor()

inserted = 0
skipped = 0

for question in questions:

    topic = question[0]
    question_text = question[1]

    # Prevent duplicate questions
    cursor.execute("""
        SELECT 1
        FROM quiz_questions
        WHERE subject = ?
        AND topic = ?
        AND question = ?
    """, (SUBJECT, topic, question_text))

    if cursor.fetchone():
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
            explanation,
            difficulty
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (SUBJECT,) + question)

    inserted += 1

connection.commit()
connection.close()

print("DSA Unit 2 questions processed successfully!")
print("New questions inserted:", inserted)
print("Duplicate questions skipped:", skipped)
print("Total questions prepared:", len(questions))
