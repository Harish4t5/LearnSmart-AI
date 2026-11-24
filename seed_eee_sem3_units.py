
import sqlite3

DB_PATH = "database/ideathon2k26.db"
BRANCH_CODE = "EEE"
ACADEMIC_YEAR = "2024-25"

# Main syllabus headings only.
# No laboratory subjects and no individual topics.

syllabus = {
    "BSC-302": [
        "Random Variables and Their Distributions",
        "Testing of Hypothesis",
        "Queuing Theory",
    ],

    "EEE-301": [
        "Electrical Design of Overhead Line",
        "Performance of Lines",
        "Travelling Waves on Transmission Lines",
        "Compensation in Power Systems",
        "Economics of Generation",
        "AC Distribution",
        "Overhead Line Insulators",
        "Insulated Cables",
        "Transmission Line Sag Calculation",
    ],

    "EEE-304": [
        "Unit 1",
        "Unit 2",
        "Unit 3",
    ],

    "EEE-302": [
        "Module I",
        "Module II",
        "Module III",
        "Module IV",
        "Module V",
        "Module VI",
    ],

    "EEE-303": [
        "Part I - Data Structure",
        "Part II - Python Program",
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
          AND sem.semester_number = 3
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

print("\nEEE SEMESTER 3 IMPORT COMPLETED!")
print("Units added:", added)
print("Existing units skipped:", skipped)
print("Theory subjects processed:", len(syllabus) - len(missing))
print("Missing subjects:", missing)
print("Individual topics imported: 0")
