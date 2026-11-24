
import sqlite3

DB_PATH = "database/ideathon2k26.db"

connection = sqlite3.connect(DB_PATH)
cursor = connection.cursor()

# Get registered branches
cursor.execute("""
    SELECT id, branch_code
    FROM branches
""")
branches = cursor.fetchall()

for branch_id, branch_code in branches:

    # Create curriculum for JUT 2024-25
    cursor.execute("""
        INSERT OR IGNORE INTO curricula
        (branch_id, academic_year, regulation, source_url)
        VALUES (?, ?, ?, ?)
    """, (
        branch_id,
        "2024-25",
        "JUT 2024-25",
        None
    ))

    # Get curriculum ID
    cursor.execute("""
        SELECT id FROM curricula
        WHERE branch_id = ?
        AND academic_year = ?
        AND regulation = ?
    """, (branch_id, "2024-25", "JUT 2024-25"))

    curriculum_id = cursor.fetchone()[0]

    # Create semesters 1 to 4
    for semester_number in range(1, 5):
        cursor.execute("""
            INSERT OR IGNORE INTO semesters
            (curriculum_id, semester_number)
            VALUES (?, ?)
        """, (curriculum_id, semester_number))

connection.commit()

print("\n===== CURRICULUM AND SEMESTER STATUS =====")

cursor.execute("""
    SELECT b.branch_code, c.academic_year,
           s.semester_number
    FROM branches b
    JOIN curricula c ON b.id = c.branch_id
    JOIN semesters s ON c.id = s.curriculum_id
    ORDER BY b.branch_code, s.semester_number
""")

for row in cursor.fetchall():
    print(row)

connection.close()

print("\nCurricula and semesters created successfully!")
