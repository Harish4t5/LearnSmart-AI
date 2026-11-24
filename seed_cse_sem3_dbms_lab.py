
import sqlite3

DB_PATH = "database/ideathon2k26.db"

units = [
    (
        "Oracle RDBMS and SQL Fundamentals",
        [
            "Familiarization with Oracle RDBMS",
            "SQL*Plus",
            "Oracle Developer",
            "SQL Query Structure",
        ],
    ),
    (
        "SQL Commands and Operations",
        [
            "DDL: CREATE, ALTER, DROP, RENAME and TRUNCATE",
            "DML: SELECT, INSERT, UPDATE, DELETE and LOCK",
            "Set Operations: UNION, INTERSECTION and EXCEPT",
            "Joins",
            "Aggregate Operations",
            "GROUP BY and HAVING",
            "Nested Subqueries",
            "Views",
            "DCL: GRANT and REVOKE",
            "TCL: COMMIT, SAVEPOINT, ROLLBACK and SET TRANSACTION",
        ],
    ),
    (
        "PL/SQL Fundamentals",
        [
            "PL/SQL Environment",
            "PL/SQL Block Structure",
            "Variables and Operators",
            "Data Types",
            "Control Structures",
            "Implicit Cursors",
            "Explicit Cursors",
            "Bulk Collect INTO",
            "FORALL Statements",
            "Compilation and Runtime Exception Handling",
            "User-defined Exceptions",
        ],
    ),
    (
        "Stored Procedures, Functions and Packages",
        [
            "Stored Procedure Creation Options",
            "Pass-by-value in Procedures",
            "Functions and Pass-by-value",
            "Package Specification",
            "Package Body",
            "Package Creation and Usage",
        ],
    ),
    (
        "Triggers and Large Objects",
        [
            "Data Definition Language Triggers",
            "Data Manipulation Language Triggers",
            "Compound Triggers",
            "Trigger Restrictions",
            "CLOB",
            "NCLOB",
            "BLOB",
            "BFILE",
        ],
    ),
    (
        "GUI Applications and Group Project",
        [
            "Implementation of Applications Using GUI",
            "Group Project",
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
    """, ("CSE-AIML", 3, "CSE-304P", "2024-25"))

    result = cursor.fetchone()

    if not result:
        raise ValueError("CSE-304P subject not found!")

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

    print("CSE Semester 3 - CSE-304P DBMS Lab import completed!")
    print("Units added:", units_added)
    print("Topics added:", topics_added)

except Exception:
    conn.rollback()
    raise

finally:
    conn.close()
