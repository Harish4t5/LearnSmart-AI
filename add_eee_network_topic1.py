
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "database" / "ideathon2k26.db"

connection = sqlite3.connect(DB_PATH)

subject = "Network Theory"
branch_code = "EEE"
semester = 3
topic = "Basic Electrical Network Concepts"

questions = [
    (
        "What is an electrical network?",
        "A collection of interconnected electrical elements",
        "A mechanical system",
        "A type of battery only",
        "A magnetic material",
        "A",
        "An electrical network consists of interconnected electrical elements such as resistors, capacitors and sources.",
        "Beginner"
    ),
    (
        "Which component opposes the flow of electric current?",
        "Capacitor",
        "Resistor",
        "Inductor",
        "Generator",
        "B",
        "A resistor opposes the flow of electric current.",
        "Beginner"
    ),
    (
        "What is the SI unit of electric current?",
        "Volt",
        "Ohm",
        "Ampere",
        "Watt",
        "C",
        "Electric current is measured in amperes.",
        "Beginner"
    ),
    (
        "Which electrical element stores energy in an electric field?",
        "Resistor",
        "Inductor",
        "Capacitor",
        "Fuse",
        "C",
        "A capacitor stores energy in the electric field between its plates.",
        "Beginner"
    ),
    (
        "An ideal voltage source maintains which quantity constant?",
        "Current",
        "Voltage",
        "Resistance",
        "Power",
        "B",
        "An ideal voltage source maintains a constant terminal voltage regardless of the load current.",
        "Beginner"
    ),
    (
        "What is the reciprocal of electrical resistance?",
        "Reactance",
        "Conductance",
        "Inductance",
        "Capacitance",
        "B",
        "Conductance is the reciprocal of resistance and is measured in siemens.",
        "Intermediate"
    ),
    (
        "Which of the following is an active electrical element?",
        "Resistor",
        "Capacitor",
        "Independent voltage source",
        "Inductor",
        "C",
        "An independent voltage source can supply energy to an electrical network.",
        "Intermediate"
    ),
    (
        "In a series circuit, which quantity remains the same through all components?",
        "Voltage",
        "Current",
        "Resistance",
        "Power",
        "B",
        "The same current flows through every element connected in series.",
        "Intermediate"
    )
]

inserted = 0
skipped = 0

try:
    for q in questions:
        existing = connection.execute("""
            SELECT id FROM quiz_questions
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

    print("EEE Network Theory Topic 1 added successfully!")
    print("Subject:", subject)
    print("Topic:", topic)
    print("New questions added:", inserted)
    print("Existing questions skipped:", skipped)

except Exception as error:
    connection.rollback()
    print("Error:", error)

finally:
    connection.close()
