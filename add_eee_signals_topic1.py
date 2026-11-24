
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "database" / "ideathon2k26.db"

connection = sqlite3.connect(DB_PATH)

subject = "Signals and Systems"
branch_code = "EEE"
semester = 3
topic = "Introduction to Signals and Systems"

questions = [
    (
        "What is a signal?",
        "A physical component",
        "A function that conveys information about a phenomenon",
        "A type of electrical machine",
        "A programming language",
        "B",
        "A signal is a function that represents or conveys information about a physical phenomenon.",
        "Beginner"
    ),
    (
        "Which of the following is an example of an electrical signal?",
        "Temperature only",
        "Voltage varying with time",
        "Mechanical gear",
        "Insulating material",
        "B",
        "Voltage varying with time is an electrical signal.",
        "Beginner"
    ),
    (
        "A system is generally defined as:",
        "A device or process that transforms an input signal into an output signal",
        "A type of resistor",
        "A constant voltage source only",
        "A mathematical number",
        "A",
        "A system processes an input signal and produces an output signal.",
        "Beginner"
    ),
    (
        "Which mathematical variable is commonly used to represent continuous time?",
        "n",
        "k",
        "t",
        "m",
        "C",
        "The variable t is commonly used to represent continuous time.",
        "Beginner"
    ),
    (
        "Which variable is commonly used to represent discrete-time samples?",
        "t",
        "n",
        "x",
        "V",
        "B",
        "The integer variable n commonly represents the discrete-time index.",
        "Beginner"
    ),
    (
        "If an input signal is x(t) = 2t, what is its value at t = 3?",
        "3",
        "5",
        "6",
        "9",
        "C",
        "Substituting t = 3 gives x(3) = 2 × 3 = 6.",
        "Intermediate"
    ),
    (
        "A system has input x(t) and output y(t) = 3x(t). What is the output when x(t) = 4?",
        "7",
        "12",
        "16",
        "3",
        "B",
        "The output is y(t) = 3 × 4 = 12.",
        "Intermediate"
    ),
    (
        "Which of the following best describes a discrete-time signal?",
        "A signal defined only at discrete time instants",
        "A signal defined at every real-valued time instant",
        "A signal that is always constant",
        "A signal that cannot carry information",
        "A",
        "A discrete-time signal is defined at separate time instants, commonly represented by integer indices.",
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

    print("EEE Signals and Systems Topic 1 added successfully!")
    print("Subject:", subject)
    print("Topic:", topic)
    print("New questions added:", inserted)
    print("Existing questions skipped:", skipped)

except Exception as error:
    connection.rollback()
    print("Error:", error)

finally:
    connection.close()
