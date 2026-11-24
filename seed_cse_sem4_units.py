
import sqlite3

DB_PATH = "database/ideathon2k26.db"
BRANCH_CODE = "CSE-AIML"
ACADEMIC_YEAR = "2024-25"

# Main syllabus sections only.
# No laboratory subjects and no individual topics.

syllabus = {
    "CSE-401": [
        "Introduction",
        "Operating System Structures",
        "Processes and Threads",
        "CPU Scheduling",
        "Process Synchronization",
        "Deadlocks",
        "Memory Management",
        "File System",
        "I/O Systems",
    ],

    "CSE-402": [
        "Modelling with Linear Programming",
        "Integer Linear Programming",
        "Network Model",
        "Heuristic and Meta Heuristic Programming",
        "Simulation Modelling",
    ],

    "CSE-403": [
        "Unit 1",
        "Unit 2",
        "Unit 3",
    ],

    "CSE-404": [
        "Introduction",
        "Data Link Layer",
        "Network Layer",
        "Transport Layer",
        "Application Layer",
    ],

    "CSE-405": [
        "Unit 1",
        "Unit 2",
        "Unit 3",
    ],
}

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

added = 0
skipped = 0

for course_code, unit_titles in syllabus.items():

    cursor.execute("""
        SELECT s.id
        FROM subjects s
        JOIN semesters sem ON s.semester_id = sem.id
        JOIN curricula c ON sem.curriculum_id = c.id
        JOIN branches b ON c.branch_id = b.id
        WHERE s.course_code = ?
          AND sem.semester_number = 4
          AND b.branch_code = ?
          AND c.academic_year = ?
    """, (course_code, BRANCH_CODE, ACADEMIC_YEAR))

    subject = cursor.fetchone()

    if subject is None:
        print(f"Subject not found: {course_code}")
        continue

    subject_id = subject[0]

    for unit_number, unit_title in enumerate(unit_titles, start=1):

        cursor.execute("""
            SELECT id
            FROM syllabus_units
            WHERE subject_id = ?
              AND unit_number = ?
        """, (subject_id, unit_number))

        if cursor.fetchone():
            skipped += 1
            continue

        cursor.execute("""
            INSERT INTO syllabus_units
            (subject_id, unit_number, unit_title)
            VALUES (?, ?, ?)
        """, (subject_id, unit_number, unit_title))

        added += 1

conn.commit()
conn.close()

print("\nCSE SEMESTER 4 IMPORT COMPLETED!")
print("Units added:", added)
print("Existing units skipped:", skipped)
print("Theory subjects processed:", len(syllabus))
print("Individual topics imported: 0")
