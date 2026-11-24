
import sqlite3

DB_PATH = "database/ideathon2k26.db"

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

cursor.execute("""
    SELECT
        s.course_code,
        s.subject_name,
        COUNT(DISTINCT u.id) AS total_units,
        COUNT(DISTINCT t.id) AS total_topics
    FROM subjects s
    JOIN semesters sem ON s.semester_id = sem.id
    JOIN curricula c ON sem.curriculum_id = c.id
    JOIN branches b ON c.branch_id = b.id
    LEFT JOIN syllabus_units u ON u.subject_id = s.id
    LEFT JOIN syllabus_topics t ON t.unit_id = u.id
    WHERE b.branch_code = 'EEE'
      AND sem.semester_number = 4
      AND c.academic_year = '2024-25'
      AND s.subject_type = 'Theory'
    GROUP BY s.id
    ORDER BY s.course_code
""")

rows = cursor.fetchall()

print("\nEEE SEMESTER 4 VERIFICATION\n")

total_units = 0
total_topics = 0

for code, name, units, topics in rows:
    print(f"{code} | {name} | Units: {units} | Topics: {topics}")
    total_units += units
    total_topics += topics

print("\nTotal theory subjects:", len(rows))
print("Total units:", total_units)
print("Total topics:", total_topics)

conn.close()
