
import sqlite3

connection = sqlite3.connect("database/ideathon2k26.db")
cursor = connection.cursor()

print("OOP TOTAL QUESTIONS:")

cursor.execute("""
    SELECT COUNT(*)
    FROM quiz_questions
    WHERE subject = 'Object Oriented Programming'
""")

print(cursor.fetchone()[0])

print("\nDIFFICULTY DISTRIBUTION:")

cursor.execute("""
    SELECT difficulty, COUNT(*)
    FROM quiz_questions
    WHERE subject = 'Object Oriented Programming'
    GROUP BY difficulty
    ORDER BY difficulty
""")

for row in cursor.fetchall():
    print(row)

print("\nMODULE DISTRIBUTION:")

cursor.execute("""
    SELECT topic, COUNT(*)
    FROM quiz_questions
    WHERE subject = 'Object Oriented Programming'
    GROUP BY topic
    ORDER BY topic
""")

for row in cursor.fetchall():
    print(row)

connection.close()
