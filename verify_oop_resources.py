import sqlite3

connection = sqlite3.connect("database/ideathon2k26.db")
cursor = connection.cursor()

cursor.execute("""
    SELECT topic, level, COUNT(*)
    FROM learning_resources
    WHERE subject = 'Object Oriented Programming'
    GROUP BY topic, level
    ORDER BY topic, level
""")

print("OOP LEARNING RESOURCES:")
for row in cursor.fetchall():
    print(row)

cursor.execute("""
    SELECT COUNT(*)
    FROM learning_resources
    WHERE subject = 'Object Oriented Programming'
""")

print("\nTOTAL OOP RESOURCES:", cursor.fetchone()[0])

connection.close()