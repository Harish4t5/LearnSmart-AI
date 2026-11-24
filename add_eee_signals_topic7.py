
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "database" / "ideathon2k26.db"

connection = sqlite3.connect(DB_PATH)

subject = "Signals and Systems"
branch_code = "EEE"
semester = 3
topic = "Fourier Series"

questions = [
    (
        "What is the main purpose of Fourier Series?",
        "To represent a periodic signal as a sum of sinusoids",
        "To calculate resistance",
        "To convert AC into DC",
        "To measure frequency only",
        "A",
        "Fourier Series represents a periodic signal using sine and cosine components.",
        "Beginner"
    ),
    (
        "Fourier Series is mainly applicable to which type of signals?",
        "Only random signals",
        "Periodic signals",
        "Only constant signals",
        "Only impulse signals",
        "B",
        "Fourier Series is used to represent periodic signals.",
        "Beginner"
    ),
    (
        "Which two trigonometric functions are commonly used in the trigonometric Fourier Series?",
        "Tangent and cotangent",
        "Secant and cosecant",
        "Sine and cosine",
        "Logarithm and exponential",
        "C",
        "The trigonometric Fourier Series uses sine and cosine functions.",
        "Beginner"
    ),
    (
        "What does the fundamental frequency represent?",
        "The highest frequency in a signal",
        "The lowest non-zero frequency of a periodic signal",
        "The average value of a signal",
        "The signal amplitude",
        "B",
        "The fundamental frequency is the frequency corresponding to the fundamental period.",
        "Beginner"
    ),
    (
        "What is the fundamental period T of a periodic signal with frequency f?",
        "T = f",
        "T = f squared",
        "T = 1/f",
        "T = 2f",
        "C",
        "The fundamental period is the reciprocal of the fundamental frequency.",
        "Beginner"
    ),
    (
        "Which term represents the average or DC component in a trigonometric Fourier Series?",
        "The constant term",
        "The highest harmonic",
        "The sine term only",
        "The cosine term only",
        "A",
        "The constant coefficient represents the average or DC component of the periodic signal.",
        "Intermediate"
    ),
    (
        "A periodic signal has a fundamental frequency of 50 Hz. What is its fundamental period?",
        "0.2 seconds",
        "0.02 seconds",
        "2 seconds",
        "50 seconds",
        "B",
        "T = 1/f = 1/50 = 0.02 seconds.",
        "Intermediate"
    ),
    (
        "In Fourier Series, harmonics are frequencies that are:",
        "Always lower than the fundamental frequency",
        "Unrelated to the fundamental frequency",
        "Integer multiples of the fundamental frequency",
        "Always equal to zero",
        "C",
        "The harmonics of a periodic signal occur at integer multiples of its fundamental frequency.",
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

    print("EEE Signals and Systems Topic 7 added successfully!")
    print("Subject:", subject)
    print("Topic:", topic)
    print("New questions added:", inserted)
    print("Existing questions skipped:", skipped)

except Exception as error:
    connection.rollback()
    print("Error:", error)

finally:
    connection.close()
