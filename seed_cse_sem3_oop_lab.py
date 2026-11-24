
import sqlite3

DB_PATH = "database/ideathon2k26.db"

experiments = [
    "Ball Games",
    "Cannon Game",
    "Pinball Game",
    "Cards Game",
    "User Interface Dialogs Related Programs",
    "I/O Processing Programs",
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
    """, ("CSE-AIML", 3, "CSE-303P", "2024-25"))

    result = cursor.fetchone()

    if not result:
        raise ValueError("CSE-303P subject not found!")

    subject_id = result[0]

    cursor.execute("""
        SELECT id FROM syllabus_units
        WHERE subject_id = ? AND unit_number = 1
    """, (subject_id,))

    existing_unit = cursor.fetchone()

    if existing_unit:
        unit_id = existing_unit[0]
        units_added = 0
    else:
        cursor.execute("""
            INSERT INTO syllabus_units
            (subject_id, unit_number, unit_title)
            VALUES (?, ?, ?)
        """, (subject_id, 1, "List of Experiments"))

        unit_id = cursor.lastrowid
        units_added = 1

    topics_added = 0

    for order, experiment in enumerate(experiments, start=1):
        cursor.execute("""
            SELECT id FROM syllabus_topics
            WHERE unit_id = ? AND topic_order = ?
        """, (unit_id, order))

        if cursor.fetchone():
            continue

        cursor.execute("""
            INSERT INTO syllabus_topics
            (unit_id, topic_name, topic_order)
            VALUES (?, ?, ?)
        """, (unit_id, experiment, order))

        topics_added += 1

    conn.commit()

    print("CSE Semester 3 - CSE-303P OOP Lab import completed!")
    print("Units added:", units_added)
    print("Experiments added:", topics_added)

except Exception:
    conn.rollback()
    raise

finally:
    conn.close()
