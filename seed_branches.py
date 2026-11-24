
import sqlite3

DB_PATH = "database/ideathon2k26.db"

branches = [
    ("CSE-AIML", "Computer Science and Engineering (AI & ML)"),
    ("EEE", "Electrical and Electronics Engineering")
]

connection = sqlite3.connect(DB_PATH)
cursor = connection.cursor()

for code, name in branches:
    cursor.execute("""
        INSERT OR IGNORE INTO branches (branch_code, branch_name)
        VALUES (?, ?)
    """, (code, name))

connection.commit()

print("\n===== REGISTERED BRANCHES =====")

cursor.execute("""
    SELECT id, branch_code, branch_name
    FROM branches
""")

for row in cursor.fetchall():
    print(row)

connection.close()

print("\nBranches added successfully!")
