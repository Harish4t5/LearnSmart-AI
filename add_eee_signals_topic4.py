
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "database" / "ideathon2k26.db"

connection = sqlite3.connect(DB_PATH)

subject = "Signals and Systems"
branch_code = "EEE"
semester = 3
topic = "Continuous-Time and Discrete-Time Systems"

questions = [
    (
        "A continuous-time signal is defined at:",
        "Only integer time values",
        "Every instant of time in a given interval",
        "Only even time values",
        "Only zero time",
        "B",
        "A continuous-time signal is defined for every instant of time in its domain.",
        "Beginner"
    ),
    (
        "A discrete-time signal is commonly represented using which notation?",
        "x(t)",
        "x(n)",
        "x(s)",
        "x(f)",
        "B",
        "Discrete-time signals are commonly represented as x[n] or x(n), where n is an integer index.",
        "Beginner"
    ),
    (
        "Which of the following is an example of a discrete-time signal?",
        "Temperature changing continuously",
        "Voltage measured at fixed time intervals",
        "Sound pressure at every instant",
        "Continuous water flow",
        "B",
        "Measurements taken at fixed time intervals form a sequence of discrete-time samples.",
        "Beginner"
    ),
    (
        "What is the process of converting a continuous-time signal into samples called?",
        "Amplification",
        "Sampling",
        "Modulation",
        "Integration",
        "B",
        "Sampling converts a continuous-time signal into a sequence of values at discrete time instants.",
        "Beginner"
    ),
    (
        "Which of the following is generally true about a discrete-time signal?",
        "It is defined only at discrete time instants",
        "It must be continuous",
        "It cannot represent information",
        "It always has a constant value",
        "A",
        "A discrete-time signal is defined at separate time indices rather than at every instant.",
        "Beginner"
    ),
    (
        "A continuous-time signal x(t) = 3t is sampled at t = 2. What is the sample value?",
        "3",
        "5",
        "6",
        "9",
        "C",
        "Substituting t = 2 gives x(2) = 3 × 2 = 6.",
        "Intermediate"
    ),
    (
        "A discrete-time signal is given by x[n] = 2n + 1. What is x[3]?",
        "5",
        "6",
        "7",
        "8",
        "C",
        "Substituting n = 3 gives x[3] = 2(3) + 1 = 7.",
        "Intermediate"
    ),
    (
        "If a continuous-time signal is sampled every 0.01 seconds, what is its sampling frequency?",
        "10 Hz",
        "50 Hz",
        "100 Hz",
        "1000 Hz",
        "C",
        "Sampling frequency is the reciprocal of the sampling interval: fs = 1 / 0.01 = 100 Hz.",
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

    print("EEE Signals and Systems Topic 4 added successfully!")
    print("Subject:", subject)
    print("Topic:", topic)
    print("New questions added:", inserted)
    print("Existing questions skipped:", skipped)

except Exception as error:
    connection.rollback()
    print("Error:", error)

finally:
    connection.close()
