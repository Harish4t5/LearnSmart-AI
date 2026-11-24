
import sqlite3

DB_PATH = "database/ideathon2k26.db"

connection = sqlite3.connect(DB_PATH)
cursor = connection.cursor()

tables = [
    "branches",
    "curricula",
    "semesters",
    "subjects",
    "syllabus_units",
    "syllabus_topics"
]

print("\n===== SYLLABUS DATABASE STATUS =====")

for table in tables:
    cursor.execute(f"SELECT COUNT(*) FROM {table}")
    count = cursor.fetchone()[0]
    print(f"{table}: {count} records")

print("\n===== REGISTERED BRANCHES =====")

cursor.execute("""
    SELECT id, branch_code, branch_name
    FROM branches
""")

for row in cursor.fetchall():
    print(row)

connection.close()
print("\nDatabase check completed!")
