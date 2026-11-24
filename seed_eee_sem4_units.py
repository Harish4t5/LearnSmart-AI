
import sqlite3

DB_PATH = "database/ideathon2k26.db"
BRANCH_CODE = "EEE"
ACADEMIC_YEAR = "2024-25"

syllabus = {
    "EEE-401": [
        "Electromechanical Energy Conversion Principles",
        "DC Machines",
        "Speed Control of DC Motors",
        "Testing of DC Motors",
        "Single-Phase Two Winding Transformers",
        "Auto transformer",
        "Three-Phase Transformers",
    ],

    "EEE-402": [
        "Per Unit Representation of Power Systems",
        "Symmetrical Components",
        "Fault Calculations",
        "Load Flow Analysis",
        "Power system Stability",
        "Economic Operation of Power Systems",
        "Load Frequency Control",
        "Voltage Control",
    ],

    "EEE-403": [
        "Unit-1 Number system and codes",
        "Unit-2 Boolean Algebra and Minimization Techniques",
        "Unit-3 Combinational Circuits",
        "Unit-4 Sequential Circuits",
        "Unit-5 Basics of Memory and Data Conversion Circuits",
    ],

    "EEE-404": [
        "Introduction",
        "Modelling of Physical Systems",
        "Techniques to Develop Transfer Function of Systems",
        "Time Domain Analysis of Control Systems",
        "Root Locus Techniques",
        "Frequency Domain Analysis of Control Systems",
        "State-Space Representation of Dynamic Systems",
    ],
}

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

added = 0
skipped = 0
missing = []

for course_code, unit_titles in syllabus.items():

    cursor.execute("""
        SELECT s.id, s.subject_name
        FROM subjects s
        JOIN semesters sem ON s.semester_id = sem.id
        JOIN curricula c ON sem.curriculum_id = c.id
        JOIN branches b ON c.branch_id = b.id
        WHERE s.course_code = ?
          AND sem.semester_number = 4
          AND b.branch_code = ?
          AND c.academic_year = ?
          AND s.subject_type = 'Theory'
    """, (course_code, BRANCH_CODE, ACADEMIC_YEAR))

    subject = cursor.fetchone()

    if subject is None:
        missing.append(course_code)
        print(f"Subject not found: {course_code}")
        continue

    subject_id, subject_name = subject

    for unit_number, unit_title in enumerate(unit_titles, start=1):

        cursor.execute("""
            SELECT id FROM syllabus_units
            WHERE subject_id = ? AND unit_number = ?
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

print("\nEEE SEMESTER 4 IMPORT COMPLETED!")
print("Units added:", added)
print("Existing units skipped:", skipped)
print("Theory subjects processed:", len(syllabus) - len(missing))
print("Missing subjects:", missing)
print("Individual topics imported: 0")
