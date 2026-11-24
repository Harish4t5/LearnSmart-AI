
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "database" / "ideathon2k26.db"

connection = sqlite3.connect(DB_PATH)
cursor = connection.cursor()

subject = "Data Structure with Python Program"
topic = "Trees and Graphs"

resources = [
    (
        subject,
        topic,
        "Beginner",
        "Article",
        "Trees and Graphs - Study Notes",
        "",
        """TREES AND GRAPHS

1. What is a Tree?

A tree is a non-linear hierarchical data structure
consisting of nodes connected by edges.

Important terminology:
- Root: The topmost node.
- Parent: A node having child nodes.
- Child: A node connected below a parent.
- Leaf: A node with no children.
- Edge: A connection between two nodes.
- Height: The number of edges on the longest downward
  path from a node to a leaf.

2. Binary Tree

A binary tree is a tree in which each node has at most
two children:
- Left child
- Right child

3. Binary Search Tree (BST)

A BST is a binary tree where:
- Values in the left subtree are smaller than the node.
- Values in the right subtree are greater than the node.

This ordering property applies recursively to every node.

4. Tree Traversal

Traversal means visiting all nodes in a tree.

Inorder:
Left -> Root -> Right

Preorder:
Root -> Left -> Right

Postorder:
Left -> Right -> Root

Level Order:
Visits nodes level by level.

5. What is a Graph?

A graph is a non-linear data structure consisting of:
- Vertices (nodes)
- Edges (connections)

6. Types of Graphs

Undirected Graph:
Edges have no direction.

Directed Graph:
Edges have a direction.

Weighted Graph:
Edges have associated weights or costs.

Unweighted Graph:
Edges do not carry weights.

7. Graph Representation

Adjacency Matrix:
A two-dimensional matrix represents connections.

Adjacency List:
Each vertex stores a list of its neighboring vertices.

8. Graph Traversal

Breadth-First Search (BFS):
Explores neighboring vertices level by level.
It commonly uses a queue.

Depth-First Search (DFS):
Explores one path deeply before backtracking.
It commonly uses recursion or a stack.

9. Applications

Trees:
- File systems.
- Database indexing.
- Hierarchical data.
- Expression trees.

Graphs:
- Computer networks.
- Maps and navigation.
- Social networks.
- Dependency relationships.

Remember:
Tree -> Hierarchical structure.
Graph -> Network of vertices and edges.
BFS -> Queue-based traversal.
DFS -> Stack or recursion-based traversal."""
    ),
    (
        subject,
        topic,
        "Intermediate",
        "Documentation",
        "Python Graph and Tree Implementation Reference",
        "https://docs.python.org/3/tutorial/datastructures.html",
        "Python's official data structures tutorial. Use it for "
        "understanding lists, dictionaries and collections that "
        "can represent tree and graph structures in Python."
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

    print("Data Structure with Python - Topic 8 resources processed!")
    print("Inserted:", inserted)
    print("Skipped:", skipped)

except Exception as error:
    connection.rollback()
    print("Error:", error)

finally:
    connection.close()
