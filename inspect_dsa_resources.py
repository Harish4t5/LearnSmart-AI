
import sqlite3

connection = sqlite3.connect("database/ideathon2k26.db")

query = """
SELECT topic, level, resource_type, title
FROM learning_resources
WHERE subject = ?
ORDER BY topic, level
"""

rows = connection.execute(
    query,
    ("Data Structures and Algorithms",)
).fetchall()

print("\nDSA LEARNING RESOURCES:")
for row in rows:
    print(row)

connection.close()
