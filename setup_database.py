
import sqlite3
import subprocess
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "database" / "ideathon2k26.db"

scripts = [
    "database/db.py",
    "add_dsa_questions.py",
    "add_dsa_unit2_questions.py",
    "add_dsa_resources.py",
    "add_oop_questions.py",
    "add_oop_resources.py",
]

for script in scripts:
    print(f"\nRunning {script}...")
    subprocess.run(
        [sys.executable, str(BASE_DIR / script)],
        cwd=BASE_DIR,
        check=True
    )

connection = sqlite3.connect(DB_PATH)

# Set a default difficulty for Python sample questions.
connection.execute("""
    UPDATE quiz_questions
    SET difficulty = 'Beginner'
    WHERE subject = 'Python' AND difficulty IS NULL
""")

# Set a default difficulty for DSA Unit 1 questions.
connection.execute("""
    UPDATE quiz_questions
    SET difficulty = 'Beginner'
    WHERE subject = 'Data Structures and Algorithms'
    AND topic NOT LIKE 'Unit 2%'
    AND difficulty IS NULL
""")

connection.commit()
connection.close()

print("\nLearnSmart AI database setup completed successfully!")
