
import sqlite3

connection = sqlite3.connect("database/ideathon2k26.db")
cursor = connection.cursor()

subject = "Data Structures and Algorithms"

print("\n--- UNIT 2 DIFFICULTY SUMMARY ---")

cursor.execute("""
    SELECT difficulty, COUNT(*)
    FROM quiz_questions
    WHERE subject = ?
      AND topic LIKE 'Unit 2 - %'
    GROUP BY difficulty
    ORDER BY difficulty
""", (subject,))

for difficulty, count in cursor.fetchall():
    print(f"{difficulty}: {count} questions")

print("\n--- UNIT 2 TOPIC SUMMARY ---")

cursor.execute("""
    SELECT topic, COUNT(*)
    FROM quiz_questions
    WHERE subject = ?
      AND topic LIKE 'Unit 2 - %'
    GROUP BY topic
    ORDER BY topic
""", (subject,))

for topic, count in cursor.fetchall():
    print(f"{topic}: {count}")

connection.close()
