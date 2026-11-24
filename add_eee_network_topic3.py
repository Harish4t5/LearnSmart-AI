
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "database" / "ideathon2k26.db"

connection = sqlite3.connect(DB_PATH)

subject = "Network Theory"
branch_code = "EEE"
semester = 3
topic = "Network Theorems"

questions = [
    (
        "Which theorem is used to analyze a linear bilateral network by considering one independent source at a time?",
        "Thevenin's Theorem",
        "Superposition Theorem",
        "Norton's Theorem",
        "Maximum Power Transfer Theorem",
        "B",
        "The Superposition Theorem considers the effect of one independent source at a time in a linear network.",
        "Beginner"
    ),
    (
        "Thevenin's theorem replaces a linear two-terminal network with:",
        "An ideal current source in parallel with resistance",
        "An ideal voltage source in series with resistance",
        "A capacitor and an inductor",
        "A resistor only",
        "B",
        "Thevenin's equivalent consists of a voltage source in series with an equivalent resistance.",
        "Beginner"
    ),
    (
        "Norton's theorem represents a linear two-terminal network using:",
        "A voltage source in series with resistance",
        "A current source in parallel with resistance",
        "A voltage source in parallel with capacitance",
        "An ideal resistor only",
        "B",
        "Norton's equivalent consists of a current source in parallel with equivalent resistance.",
        "Beginner"
    ),
    (
        "Maximum power is transferred to a resistive load when the load resistance is equal to:",
        "Zero",
        "Twice the source resistance",
        "The Thevenin resistance",
        "Half the Thevenin resistance",
        "C",
        "For a DC resistive network, maximum power transfer occurs when load resistance equals Thevenin resistance.",
        "Beginner"
    ),
    (
        "While applying the Superposition Theorem, an ideal independent voltage source that is switched off is replaced by:",
        "An open circuit",
        "A short circuit",
        "A capacitor",
        "An inductor",
        "B",
        "An ideal voltage source set to zero volts is replaced by a short circuit.",
        "Beginner"
    ),
    (
        "A network has a Thevenin voltage of 12 V and Thevenin resistance of 4 ohms. What is the Norton current?",
        "2 A",
        "3 A",
        "4 A",
        "6 A",
        "B",
        "Norton current equals Thevenin voltage divided by Thevenin resistance: 12/4 = 3 A.",
        "Intermediate"
    ),
    (
        "A Thevenin equivalent has Vth = 20 V and Rth = 5 ohms. What load resistance receives maximum power?",
        "2 ohms",
        "5 ohms",
        "10 ohms",
        "20 ohms",
        "B",
        "Maximum power transfer occurs when RL = Rth. Therefore, RL = 5 ohms.",
        "Intermediate"
    ),
    (
        "A voltage source of 10 V is connected in series with a 2-ohm resistor. What is its equivalent Norton current?",
        "2 A",
        "5 A",
        "10 A",
        "20 A",
        "B",
        "Source transformation gives IN = V/R = 10/2 = 5 A.",
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

    print("EEE Network Theory Topic 3 added successfully!")
    print("Subject:", subject)
    print("Topic:", topic)
    print("New questions added:", inserted)
    print("Existing questions skipped:", skipped)

except Exception as error:
    connection.rollback()
    print("Error:", error)

finally:
    connection.close()
