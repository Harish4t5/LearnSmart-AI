
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "database" / "ideathon2k26.db"

connection = sqlite3.connect(DB_PATH)

subject = "Signals and Systems"
branch_code = "EEE"
semester = 3
topic = "Classification of Signals"

questions = [
    (
        "A signal whose value can be predicted exactly at any time is called:",
        "Random signal",
        "Deterministic signal",
        "Noise signal",
        "Non-periodic signal",
        "B",
        "A deterministic signal can be described by a mathematical expression or rule.",
        "Beginner"
    ),
    (
        "A signal whose future values cannot be predicted exactly is called:",
        "Periodic signal",
        "Deterministic signal",
        "Random signal",
        "Even signal",
        "C",
        "A random signal has values that cannot be predicted exactly in advance.",
        "Beginner"
    ),
    (
        "A signal that repeats itself after a fixed time interval is called:",
        "Periodic signal",
        "Aperiodic signal",
        "Random signal",
        "Energy signal",
        "A",
        "A periodic signal repeats its waveform after a fixed period.",
        "Beginner"
    ),
    (
        "Which condition describes an even signal?",
        "x(-t) = -x(t)",
        "x(-t) = x(t)",
        "x(t) = 0",
        "x(-t) = 1",
        "B",
        "An even signal is symmetric about the vertical axis and satisfies x(-t) = x(t).",
        "Beginner"
    ),
    (
        "Which condition describes an odd signal?",
        "x(-t) = x(t)",
        "x(-t) = 1",
        "x(-t) = -x(t)",
        "x(t) = 0",
        "C",
        "An odd signal satisfies x(-t) = -x(t) and has symmetry about the origin.",
        "Beginner"
    ),
    (
        "Which of the following is an even signal?",
        "x(t) = sin(t)",
        "x(t) = cos(t)",
        "x(t) = t",
        "x(t) = t³",
        "B",
        "Cosine is an even function because cos(-t) = cos(t).",
        "Intermediate"
    ),
    (
        "Which of the following is an odd signal?",
        "x(t) = cos(t)",
        "x(t) = t²",
        "x(t) = sin(t)",
        "x(t) = 1",
        "C",
        "Sine is an odd function because sin(-t) = -sin(t).",
        "Intermediate"
    ),
    (
        "A signal that has finite total energy and zero average power is classified as:",
        "Power signal",
        "Energy signal",
        "Periodic signal",
        "Random signal",
        "B",
        "An energy signal has finite, non-zero total energy and zero average power.",
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

    print("EEE Signals and Systems Topic 2 added successfully!")
    print("Subject:", subject)
    print("Topic:", topic)
    print("New questions added:", inserted)
    print("Existing questions skipped:", skipped)

except Exception as error:
    connection.rollback()
    print("Error:", error)

finally:
    connection.close()
