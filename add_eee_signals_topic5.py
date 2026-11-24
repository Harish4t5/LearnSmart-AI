
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "database" / "ideathon2k26.db"

connection = sqlite3.connect(DB_PATH)

subject = "Signals and Systems"
branch_code = "EEE"
semester = 3
topic = "Linear Time-Invariant (LTI) Systems"

questions = [
    (
        "What does LTI stand for in Signals and Systems?",
        "Linear Time Integration",
        "Linear Time-Invariant",
        "Logical Time Interval",
        "Linear Transfer Input",
        "B",
        "LTI stands for Linear Time-Invariant.",
        "Beginner"
    ),
    (
        "A system is linear if it satisfies which property?",
        "Superposition",
        "Time reversal only",
        "Frequency shifting only",
        "Randomness",
        "A",
        "A linear system satisfies the principle of superposition, which includes additivity and homogeneity.",
        "Beginner"
    ),
    (
        "Which property means that a system's behavior does not change with a shift in time?",
        "Linearity",
        "Time invariance",
        "Causality",
        "Stability",
        "B",
        "A time-invariant system responds consistently regardless of when the input is applied.",
        "Beginner"
    ),
    (
        "If a system is linear, what should happen when the input is multiplied by a constant a?",
        "Output remains unchanged",
        "Output is multiplied by a",
        "Output becomes zero",
        "Output is reversed",
        "B",
        "The homogeneity property states that scaling the input by a constant scales the output by the same constant.",
        "Beginner"
    ),
    (
        "Which of the following is a basic requirement for an LTI system?",
        "Linearity only",
        "Time invariance only",
        "Both linearity and time invariance",
        "Random input",
        "C",
        "An LTI system must satisfy both linearity and time-invariance properties.",
        "Beginner"
    ),
    (
        "A system is described by y(t) = 2x(t). Is it linear?",
        "Yes",
        "No",
        "Only for negative inputs",
        "Cannot be determined",
        "A",
        "The system satisfies additivity and homogeneity, so it is linear.",
        "Intermediate"
    ),
    (
        "A system is described by y(t) = x(t) + 5. Is it linear?",
        "Yes, always",
        "No, because of the constant addition",
        "Yes, only for positive inputs",
        "No, because it is time-varying",
        "B",
        "For zero input, the output is 5 rather than zero. Therefore, the system is not linear.",
        "Intermediate"
    ),
    (
        "For a time-invariant system, if input x(t) produces output y(t), what output is produced by input x(t - t0)?",
        "y(t + t0)",
        "y(t)",
        "y(t - t0)",
        "Zero",
        "C",
        "Time invariance means delaying the input by t0 delays the output by the same amount, producing y(t - t0).",
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

    print("EEE Signals and Systems Topic 5 added successfully!")
    print("Subject:", subject)
    print("Topic:", topic)
    print("New questions added:", inserted)
    print("Existing questions skipped:", skipped)

except Exception as error:
    connection.rollback()
    print("Error:", error)

finally:
    connection.close()
