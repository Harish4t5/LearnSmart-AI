
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "database" / "ideathon2k26.db"

connection = sqlite3.connect(DB_PATH)

subject = "Power Systems I"
branch_code = "EEE"
semester = 3
topic = "Insulators and Cables"

questions = [
    (
        "What is the main function of an insulator in an overhead transmission line?",
        "To increase current",
        "To support conductors and prevent leakage of current to earth",
        "To generate electricity",
        "To reduce frequency",
        "B",
        "Insulators mechanically support conductors and electrically isolate them from supporting structures.",
        "Beginner"
    ),
    (
        "Which material is commonly used for overhead line insulators?",
        "Copper",
        "Aluminium",
        "Porcelain",
        "Cast iron",
        "C",
        "Porcelain is widely used because of its good insulating and mechanical properties.",
        "Beginner"
    ),
    (
        "Which type of insulator is commonly used on low-voltage overhead distribution lines?",
        "Pin-type insulator",
        "Suspension-type insulator",
        "Strain-type insulator",
        "Shackle-type insulator only for all voltages",
        "A",
        "Pin-type insulators are commonly used on distribution lines at lower voltage levels.",
        "Beginner"
    ),
    (
        "Which type of insulator is generally used for high-voltage transmission lines?",
        "Pin-type",
        "Suspension-type",
        "Shackle-type",
        "Stay insulator",
        "B",
        "Suspension insulators use a string of disc units and are commonly used for high-voltage transmission.",
        "Beginner"
    ),
    (
        "What is the primary purpose of an underground power cable?",
        "To transmit power through buried conductors",
        "To increase power generation",
        "To convert AC into DC",
        "To store electrical energy",
        "A",
        "Underground cables carry electrical power through insulated conductors installed below ground.",
        "Beginner"
    ),
    (
        "Why are multiple disc units connected in series in a suspension insulator string?",
        "To increase conductor resistance",
        "To obtain the required insulation level for higher voltages",
        "To increase supply frequency",
        "To reduce mechanical strength",
        "B",
        "A string of disc insulators provides the insulation required for high-voltage lines, and the number of units can be increased with voltage.",
        "Intermediate"
    ),
    (
        "Which layer in a power cable provides electrical insulation around the conductor?",
        "Armouring",
        "Outer serving",
        "Insulation layer",
        "Protective bedding",
        "C",
        "The insulation layer electrically separates the conductor from other cable components and the surroundings.",
        "Intermediate"
    ),
    (
        "What is the main purpose of armouring in an underground power cable?",
        "To increase electrical frequency",
        "To provide mechanical protection",
        "To generate magnetic flux",
        "To reduce conductor length",
        "B",
        "Armouring protects underground cables against mechanical damage during installation and service.",
        "Intermediate"
    )
]

inserted = 0
skipped = 0

try:
    for q in questions:
        existing = connection.execute("""
            SELECT id
            FROM quiz_questions
            WHERE subject = ?
              AND branch_code = ?
              AND semester = ?
              AND topic = ?
              AND question = ?
        """, (subject, branch_code, semester, topic, q[0])).fetchone()

        if existing:
            skipped += 1
            continue

        connection.execute("""
            INSERT INTO quiz_questions (
                subject, topic, question,
                option_a, option_b, option_c, option_d,
                correct_answer, explanation, difficulty,
                branch_code, semester
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            subject, topic, q[0],
            q[1], q[2], q[3], q[4],
            q[5], q[6], q[7],
            branch_code, semester
        ))

        inserted += 1

    connection.commit()

    print("EEE Topic 5 added successfully!")
    print("Subject:", subject)
    print("Topic:", topic)
    print("New questions added:", inserted)
    print("Existing questions skipped:", skipped)

except Exception as error:
    connection.rollback()
    print("Error:", error)

finally:
    connection.close()

