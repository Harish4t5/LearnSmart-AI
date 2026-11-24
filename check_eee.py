
import sqlite3

connection = sqlite3.connect("database/ideathon2k26.db")

result = connection.execute("""
    SELECT subject, topic, branch_code, semester, COUNT(*)
    FROM quiz_questions
    WHERE subject = ?
    GROUP BY subject, topic, branch_code, semester
""", ("Power Systems I",)).fetchall()

print("EEE quiz content:")
print(result)

connection.close()
