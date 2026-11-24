
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "database" / "ideathon2k26.db"

connection = sqlite3.connect(DB_PATH)

subject = "Signals and Systems"
branch_code = "EEE"
semester = 3
topic = "Fourier Transform"

questions = [
    (
        "What is the main purpose of the Fourier Transform?",
        "To convert a time-domain signal into its frequency-domain representation",
        "To calculate electrical resistance",
        "To measure temperature",
        "To convert AC into DC",
        "A",
        "The Fourier Transform represents a signal in terms of its frequency components.",
        "Beginner"
    ),
    (
        "Which domain does the Fourier Transform convert a time-domain signal into?",
        "Temperature domain",
        "Frequency domain",
        "Resistance domain",
        "Power domain",
        "B",
        "The Fourier Transform converts a time-domain representation into a frequency-domain representation.",
        "Beginner"
    ),
    (
        "Which mathematical function is used in the continuous-time Fourier Transform kernel?",
        "Exponential function",
        "Logarithmic function",
        "Polynomial function only",
        "Square-root function",
        "A",
        "The continuous-time Fourier Transform uses the complex exponential e^(-jwt) as its kernel.",
        "Beginner"
    ),
    (
        "What does the magnitude spectrum of a signal show?",
        "The phase of each frequency component",
        "The amplitude of frequency components",
        "The temperature of the signal",
        "The duration of the signal only",
        "B",
        "The magnitude spectrum describes the magnitude or amplitude of the signal's frequency components.",
        "Beginner"
    ),
    (
        "What does the phase spectrum represent?",
        "The phase angle of frequency components",
        "The resistance of a circuit",
        "The average power only",
        "The sampling interval only",
        "A",
        "The phase spectrum represents the phase angle associated with each frequency component.",
        "Beginner"
    ),
    (
        "Which Fourier Transform property states that time shifting a signal changes its frequency-domain representation by a phase factor?",
        "Linearity property",
        "Time-shifting property",
        "Convolution property",
        "Scaling property",
        "B",
        "A time shift in the signal introduces a corresponding complex exponential phase factor in its Fourier Transform.",
        "Intermediate"
    ),
    (
        "If x(t) has Fourier Transform X(jw), what is the Fourier Transform of x(t - t0)?",
        "X(jw) + t0",
        "e^(-jwt0) X(jw)",
        "t0 X(jw)",
        "X(jw) / t0",
        "B",
        "The time-shifting property gives F{x(t-t0)} = e^(-jwt0)X(jw).",
        "Intermediate"
    ),
    (
        "Which theorem relates multiplication in the time domain to convolution in the frequency domain?",
        "Time-shifting theorem",
        "Differentiation theorem",
        "Multiplication-convolution duality",
        "Periodicity theorem",
        "C",
        "The Fourier Transform multiplication-convolution property relates multiplication in one domain to convolution in the other, subject to the transform convention.",
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

    print("EEE Signals and Systems Topic 8 added successfully!")
    print("Subject:", subject)
    print("Topic:", topic)
    print("New questions added:", inserted)
    print("Existing questions skipped:", skipped)

except Exception as error:
    connection.rollback()
    print("Error:", error)

finally:
    connection.close()
