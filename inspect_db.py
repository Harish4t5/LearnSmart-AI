
import sqlite3

connection = sqlite3.connect("database/ideathon2k26.db")
cursor = connection.cursor()

cursor.execute("""
    SELECT name
    FROM sqlite_master
    WHERE type = 'table'
    AND name NOT LIKE 'sqlite_%'
""")

tables = cursor.fetchall()

print("\nDATABASE TABLES:")

for table in tables:
    table_name = table[0]
    print(f"\nTable: {table_name}")

    cursor.execute(f"PRAGMA table_info({table_name})")

    for column in cursor.fetchall():
        print(column)
# Display existing quiz questions
print("\n\nEXISTING QUIZ QUESTIONS:")

cursor.execute("""
    SELECT
        id,
        subject,
        topic,
        question,
        option_a,
        option_b,
        option_c,
        option_d,
        correct_answer,
        explanation
    FROM quiz_questions
""")

questions = cursor.fetchall()

for question in questions:
    print("\n-----------------------------")
    print("ID:", question[0])
    print("Subject:", question[1])
    print("Topic:", question[2])
    print("Question:", question[3])
    print("A:", question[4])
    print("B:", question[5])
    print("C:", question[6])
    print("D:", question[7])
    print("Correct Answer:", question[8])
    print("Explanation:", question[9])

print("\nTotal Questions:", len(questions))
connection.close()
