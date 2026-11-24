
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "database" / "ideathon2k26.db"

connection = sqlite3.connect(DB_PATH)

subject = "Network Theory"
branch_code = "EEE"
semester = 3
topic = "Resonance and Coupled Circuits"

questions = [
    (
        "What is resonance in a series RLC circuit?",
        "When resistance becomes zero",
        "When inductive reactance equals capacitive reactance",
        "When current becomes zero",
        "When frequency becomes zero",
        "B",
        "Series resonance occurs when XL = XC, making the circuit impedance purely resistive.",
        "Beginner"
    ),
    (
        "At series resonance, the power factor of an ideal RLC circuit is:",
        "Zero",
        "0.5",
        "Unity",
        "Leading",
        "C",
        "At series resonance, voltage and current are in phase and the power factor is unity.",
        "Beginner"
    ),
    (
        "What is the unit of mutual inductance?",
        "Ohm",
        "Farad",
        "Henry",
        "Watt",
        "C",
        "Mutual inductance is measured in henry (H).",
        "Beginner"
    ),
    (
        "What is the coefficient of coupling between two coils?",
        "Always greater than one",
        "Always negative",
        "A value between zero and one",
        "Always equal to zero",
        "C",
        "The coefficient of coupling k lies between 0 and 1 for ordinary coupled coils.",
        "Beginner"
    ),
    (
        "At series resonance, the impedance of an ideal series RLC circuit is:",
        "Maximum",
        "Minimum and equal to resistance",
        "Infinite",
        "Equal to capacitive reactance",
        "B",
        "At resonance, XL and XC cancel each other, leaving only resistance.",
        "Beginner"
    ),
    (
        "A series RLC circuit has L = 0.1 H and C = 100 μF. What is its resonant frequency approximately?",
        "25.3 Hz",
        "50.3 Hz",
        "100.3 Hz",
        "159.2 Hz",
        "B",
        "fr = 1/(2π√LC). Substituting L = 0.1 H and C = 100 × 10^-6 F gives approximately 50.3 Hz.",
        "Intermediate"
    ),
    (
        "If the resonant frequency is 1000 Hz and the bandwidth is 100 Hz, what is the quality factor?",
        "5",
        "10",
        "20",
        "100",
        "B",
        "For a resonant circuit, Q = resonant frequency / bandwidth = 1000/100 = 10.",
        "Intermediate"
    ),
    (
        "Two magnetically coupled coils have self-inductances of 4 H and 9 H, with coefficient of coupling k = 0.5. Find their mutual inductance.",
        "1 H",
        "2 H",
        "3 H",
        "6 H",
        "B",
        "M = k√(L1L2) = 0.5 × √(4 × 9) = 0.5 × 6 = 3 H.",
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

    print("EEE Network Theory Topic 6 added successfully!")
    print("Subject:", subject)
    print("Topic:", topic)
    print("New questions added:", inserted)
    print("Existing questions skipped:", skipped)

except Exception as error:
    connection.rollback()
    print("Error:", error)

finally:
    connection.close()
