
import sqlite3

DB_PATH = "database/ideathon2k26.db"

# Existing questions that need difficulty classification
dsa_unit1_ids = list(range(18, 30))
python_ids = list(range(11, 18))

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

try:
    # Update DSA Unit 1 questions
    cursor.executemany(
        """
        UPDATE quiz_questions
        SET difficulty = 'Beginner'
        WHERE id = ? AND subject = 'Data Structures and Algorithms'
        AND difficulty IS NULL
        """,
        [(qid,) for qid in dsa_unit1_ids]
    )

    # Update Python questions
    cursor.executemany(
        """
        UPDATE quiz_questions
        SET difficulty = 'Beginner'
        WHERE id = ? AND subject = 'Python'
        AND difficulty IS NULL
        """,
        [(qid,) for qid in python_ids]
    )

    conn.commit()

    # Verify updated records
    cursor.execute("""
        SELECT subject, difficulty, COUNT(*)
        FROM quiz_questions
        GROUP BY subject, difficulty
        ORDER BY subject, difficulty
    """)

    print("Difficulty update completed!")
    print("\nUpdated difficulty distribution:")

    for row in cursor.fetchall():
        print(row)

    cursor.execute("""
        SELECT COUNT(*)
        FROM quiz_questions
        WHERE difficulty IS NULL
    """)

    print("\nQuestions still missing difficulty:", cursor.fetchone()[0])

except Exception:
    conn.rollback()
    raise

finally:
    conn.close()
