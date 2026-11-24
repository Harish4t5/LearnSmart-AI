
import sqlite3

DB_PATH = "database/ideathon2k26.db"

units = [
    (
        "Introduction",
        [
            "DBMS Fundamentals",
            "Overview of Relational Databases and Keys",
            "Structure of Relational Databases",
            "Database Schema",
            "Formal Relational Query Languages",
            "Relational Algebra and Relational Operations",
            "Database Design Process",
            "Entity-Relationship (E-R) Models",
            "Constraints",
            "Removing Redundant Attributes in Entity Sets",
            "E-R Diagrams",
            "Reduction to Relational Schemas",
            "Entity Relationship Design Issues",
            "Extended E-R Features",
            "Alternative E-R Notations",
            "Unified Modeling Language (UML)",
        ],
    ),
    (
        "Relational Database Design",
        [
            "Features of Good Relational Designs",
            "Atomic Domains and First Normal Form (1NF)",
            "Functional Dependencies",
            "Second Normal Form (2NF)",
            "Third Normal Form (3NF)",
            "Boyce-Codd Normal Form (BCNF)",
            "Higher Normal Forms",
            "Functional Dependency Theory",
            "Algorithms for Decomposition",
            "Multivalued Dependencies",
            "Fourth Normal Form (4NF)",
            "4NF Decomposition",
            "Database Design Process and Its Issues",
            "Review of SQL",
            "Intermediate SQL",
            "Advanced SQL",
        ],
    ),
    (
        "Transactions",
        [
            "Transaction Concept",
            "A Simple Transaction Model",
            "Storage Structure",
            "Transaction Atomicity and Durability",
            "Transaction Isolation",
            "Serializability",
            "Recoverable Schedules",
            "Cascadeless Schedules",
            "Concurrency Control",
            "Lock-based Protocols",
            "Locks and Granting of Locks",
            "Two-phase Locking Protocol",
            "Implementation of Locking",
            "Graph-based Protocols",
            "Deadlock Prevention",
            "Deadlock Detection and Recovery",
            "High-level Databases: MongoDB",
            "Hadoop and HBase",
            "Redis",
            "IBM Cloudant",
            "DynamoDB",
            "Cassandra",
            "CouchDB",
            "Choosing the Right Database for a Given Problem",
        ],
    ),
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
    """, ("CSE-AIML", 3, "CSE-304", "2024-25"))

    result = cursor.fetchone()

    if not result:
        raise ValueError("CSE-304 subject not found!")

    subject_id = result[0]
    units_added = 0
    topics_added = 0

    for unit_number, (unit_title, topics) in enumerate(units, start=1):
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
            """, (subject_id, unit_number, unit_title))

            unit_id = cursor.lastrowid
            units_added += 1

        for topic_order, topic_name in enumerate(topics, start=1):
            cursor.execute("""
                SELECT id FROM syllabus_topics
                WHERE unit_id = ? AND topic_order = ?
            """, (unit_id, topic_order))

            if cursor.fetchone():
                continue

            cursor.execute("""
                INSERT INTO syllabus_topics
                (unit_id, topic_name, topic_order)
                VALUES (?, ?, ?)
            """, (unit_id, topic_name, topic_order))

            topics_added += 1

    conn.commit()

    print("CSE Semester 3 - CSE-304 DBMS import completed!")
    print("Units added:", units_added)
    print("Topics added:", topics_added)

except Exception:
    conn.rollback()
    raise

finally:
    conn.close()
