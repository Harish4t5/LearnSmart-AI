
import sqlite3

conn = sqlite3.connect("database/ideathon2k26.db")
cursor = conn.cursor()

cursor.execute("""
    SELECT
        s.course_code,
        s.subject_name,
        COUNT(DISTINCT u.id) AS total_units,
        COUNT(t.id) AS total_topics
    FROM subjects s
    JOIN semesters sem ON s.semester_id = sem.id
    JOIN curricula c ON sem.curriculum_id = c.id
    JOIN branches b ON c.branch_id = b.id
    LEFT JOIN syllabus_units u ON u.subject_id = s.id
    LEFT JOIN syllabus_topics t ON t.unit_id = u.id
    WHERE b.branch_code = 'CSE-AIML'
      AND sem.semester_number = 3
      AND c.academic_year = '2024-25'
    GROUP BY s.id, s.course_code, s.subject_name
    ORDER BY s.course_code
""")

rows = cursor.fetchall()

print("\nCSE SEMESTER 3 DATABASE VERIFICATION")
print("-" * 65)

total_units = 0
total_topics = 0

for code, name, units, topics in rows:
    print(f"{code} | {name} | Units: {units} | Topics: {topics}")
    total_units += units
    total_topics += topics

print("-" * 65)
print("Total subjects:", len(rows))
print("Total units:", total_units)
print("Total topics:", total_topics)

conn.close()
