
import sqlite3

DB_PATH = "database/ideathon2k26.db"

connection = sqlite3.connect(DB_PATH)
cursor = connection.cursor()

# Check whether the difficulty column already exists
cursor.execute("PRAGMA table_info(quiz_questions)")
columns = [column[1] for column in cursor.fetchall()]

if "difficulty" not in columns:
    cursor.execute("""
        ALTER TABLE quiz_questions
        ADD COLUMN difficulty TEXT
        CHECK (difficulty IN ('Beginner', 'Intermediate', 'Advanced'))
    """)
    connection.commit()
    print("Difficulty column added successfully!")
else:
    print("Difficulty column already exists. No changes made.")

connection.close()
