
import sqlite3

connection = sqlite3.connect("database/ideathon2k26.db")

query = """
SELECT topic, difficulty, COUNT(*)
FROM quiz_questions
WHERE subject = ?
GROUP BY topic, difficulty
ORDER BY topic, difficulty
"""

rows = connection.execute(
    query,
    ("Data Structures and Algorithms",)
).fetchall()

print("\nDSA QUESTION BANK:")
for row in rows:
    print(row)

connection.close()
