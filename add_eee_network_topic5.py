
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "database" / "ideathon2k26.db"

connection = sqlite3.connect(DB_PATH)

subject = "Network Theory"
branch_code = "EEE"
semester = 3
topic = "AC Circuit Analysis"

questions = [
    (
        "What does AC stand for?",
        "Alternating Current",
        "Automatic Current",
        "Applied Charge",
        "Average Current",
        "A",
        "Alternating current periodically changes its magnitude and direction.",
        "Beginner"
    ),
    (
        "What is the standard power supply frequency in India?",
        "25 Hz",
        "50 Hz",
        "60 Hz",
        "100 Hz",
        "B",
        "The standard electricity supply frequency in India is 50 Hz.",
        "Beginner"
    ),
    (
        "What is the RMS value of a sinusoidal voltage with maximum value Vm?",
        "Vm",
        "Vm/2",
        "Vm/√2",
        "√2Vm",
        "C",
        "The RMS value of a sinusoidal voltage is approximately 0.707 times its maximum value.",
        "Beginner"
    ),
    (
        "What is the time period of a 50 Hz AC supply?",
        "0.01 seconds",
        "0.02 seconds",
        "0.05 seconds",
        "0.1 seconds",
        "B",
        "Time period T = 1/f = 1/50 = 0.02 seconds.",
        "Beginner"
    ),
    (
        "In a purely resistive AC circuit, voltage and current are:",
        "90 degrees out of phase",
        "180 degrees out of phase",
        "In phase",
        "Always opposite",
        "C",
        "In a purely resistive circuit, voltage and current reach their corresponding zero and maximum values together.",
        "Beginner"
    ),
    (
        "What is the inductive reactance of a circuit with L = 0.1 H at 50 Hz? (Use π = 3.14)",
        "15.7 ohms",
        "31.4 ohms",
        "50 ohms",
        "62.8 ohms",
        "B",
        "XL = 2πfL = 2 × 3.14 × 50 × 0.1 = 31.4 ohms.",
        "Intermediate"
    ),
    (
        "A sinusoidal current has a maximum value of 10 A. What is its RMS value approximately?",
        "5 A",
        "7.07 A",
        "10 A",
        "14.14 A",
        "B",
        "Irms = Im/√2 = 10/1.414 ≈ 7.07 A.",
        "Intermediate"
    ),
    (
        "In a purely inductive AC circuit, the current:",
        "Leads voltage by 90 degrees",
        "Lags voltage by 90 degrees",
        "Is in phase with voltage",
        "Lags voltage by 180 degrees",
        "B",
        "In a purely inductive circuit, current lags the applied voltage by 90 degrees.",
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

    print("EEE Network Theory Topic 5 added successfully!")
    print("Subject:", subject)
    print("Topic:", topic)
    print("New questions added:", inserted)
    print("Existing questions skipped:", skipped)

except Exception as error:
    connection.rollback()
    print("Error:", error)

finally:
    connection.close()
