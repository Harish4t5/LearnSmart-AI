import sqlite3

conn = sqlite3.connect("database/ideathon2k26.db")

rows = conn.execute("""
    SELECT u.id, u.unit_number, u.unit_title
    FROM syllabus_units u
    JOIN subjects s ON u.subject_id = s.id
    WHERE s.course_code = ?
""", ("CSE-304",)).fetchall()

for row in rows:
    print(row)

conn.close()