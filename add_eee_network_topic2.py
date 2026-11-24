
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "database" / "ideathon2k26.db"

connection = sqlite3.connect(DB_PATH)

subject = "Network Theory"
branch_code = "EEE"
semester = 3
topic = "Kirchhoff's Laws"

questions = [
    (
        "What does Kirchhoff's Current Law (KCL) state?",
        "Sum of currents entering a junction equals sum of currents leaving it",
        "Voltage is always zero",
        "Resistance is constant",
        "Power is always zero",
        "A",
        "KCL is based on conservation of electric charge at a junction.",
        "Beginner"
    ),
    (
        "Kirchhoff's Voltage Law (KVL) is based on which principle?",
        "Conservation of charge",
        "Conservation of energy",
        "Conservation of mass",
        "Conservation of momentum",
        "B",
        "KVL follows conservation of energy around a closed electrical loop.",
        "Beginner"
    ),
    (
        "According to KCL, the algebraic sum of currents at a node is:",
        "One",
        "Infinite",
        "Zero",
        "Equal to resistance",
        "C",
        "The algebraic sum of currents entering and leaving a node is zero.",
        "Beginner"
    ),
    (
        "What is the algebraic sum of voltages around a closed loop according to KVL?",
        "Zero",
        "One",
        "Infinite",
        "Equal to current",
        "A",
        "The sum of voltage rises and drops around a closed loop is zero.",
        "Beginner"
    ),
    (
        "If 5 A and 3 A enter a junction and 6 A leaves it, what is the other outgoing current?",
        "1 A",
        "2 A",
        "3 A",
        "4 A",
        "B",
        "By KCL, total incoming current is 8 A. Therefore, the other outgoing current is 8 - 6 = 2 A.",
        "Beginner"
    ),
    (
        "A closed loop has a 12 V source and two voltage drops of 5 V and V. Find V using KVL.",
        "5 V",
        "6 V",
        "7 V",
        "12 V",
        "C",
        "Applying KVL: 12 - 5 - V = 0, so V = 7 V.",
        "Intermediate"
    ),
    (
        "At a node, 10 A enters while 4 A and 2 A leave. What is the remaining outgoing current?",
        "2 A",
        "3 A",
        "4 A",
        "6 A",
        "C",
        "By KCL: 10 = 4 + 2 + I, so I = 4 A.",
        "Intermediate"
    ),
    (
        "A loop contains a 20 V source and series voltage drops of 8 V, 7 V and V. Find V.",
        "3 V",
        "4 V",
        "5 V",
        "6 V",
        "C",
        "Using KVL: 20 - 8 - 7 - V = 0, giving V = 5 V.",
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

    print("EEE Network Theory Topic 2 added successfully!")
    print("Subject:", subject)
    print("Topic:", topic)
    print("New questions added:", inserted)
    print("Existing questions skipped:", skipped)

except Exception as error:
    connection.rollback()
    print("Error:", error)

finally:
    connection.close()
