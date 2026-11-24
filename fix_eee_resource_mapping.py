
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "database" / "ideathon2k26.db"

connection = sqlite3.connect(DB_PATH)
cursor = connection.cursor()

try:
    # EEE Semester 3 subjects
    semester_3_subjects = [
        "Power Systems I",
        "Network Theory",
        "Data Structure with Python Program",
        "Signals and Systems",
        "Probability and Statistics"
    ]

    for subject in semester_3_subjects:
        cursor.execute("""
            UPDATE learning_resources
            SET branch_code = ?, semester = ?
            WHERE subject = ?
        """, ("EEE", 3, subject))

    # Only one EEE Semester 4 subject
    cursor.execute("""
        UPDATE learning_resources
        SET branch_code = ?, semester = ?
        WHERE subject = ?
    """, ("EEE", 4, "Electrical Machines I"))

    connection.commit()

    print("EEE study material mapping completed!")

    cursor.execute("""
        SELECT subject, semester, COUNT(*)
        FROM learning_resources
        WHERE branch_code = 'EEE'
        GROUP BY subject, semester
        ORDER BY semester, subject
    """)

    print("\nEEE resource summary:")
    for row in cursor.fetchall():
        print(f"{row[0]} | Semester {row[1]} | {row[2]} resources")

except Exception as error:
    connection.rollback()
    print("Error:", error)

finally:
    connection.close()
