
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "database" / "ideathon2k26.db"

connection = sqlite3.connect(DB_PATH)

subject = "Signals and Systems"
branch_code = "EEE"
semester = 3
topic = "Basic Operations on Signals"

questions = [
    (
        "Which operation shifts a signal along the time axis?",
        "Time shifting",
        "Time scaling",
        "Amplitude scaling",
        "Differentiation",
        "A",
        "Time shifting moves a signal to the left or right along the time axis.",
        "Beginner"
    ),
    (
        "What happens to x(t) when it is replaced by x(t - 2)?",
        "It shifts left by 2 units",
        "It shifts right by 2 units",
        "Its amplitude doubles",
        "It becomes zero",
        "B",
        "Replacing t with t - 2 delays the signal by 2 time units, shifting it to the right.",
        "Beginner"
    ),
    (
        "What does amplitude scaling of a signal mean?",
        "Changing its time period",
        "Multiplying its amplitude by a constant",
        "Reversing its time axis",
        "Changing continuous time into discrete time",
        "B",
        "Amplitude scaling multiplies the signal values by a constant factor.",
        "Beginner"
    ),
    (
        "What operation is represented by x(-t)?",
        "Time shifting",
        "Time reversal",
        "Amplitude scaling",
        "Addition",
        "B",
        "Replacing t with -t reflects the signal about the vertical axis.",
        "Beginner"
    ),
    (
        "If two signals x(t) and h(t) are added, the resulting signal is:",
        "x(t) - h(t)",
        "x(t)h(t)",
        "x(t) + h(t)",
        "x(t) / h(t)",
        "C",
        "Signal addition is performed by adding their corresponding values at each time instant.",
        "Beginner"
    ),
    (
        "If x(t) = t, what is the value of x(t - 3) at t = 5?",
        "2",
        "3",
        "5",
        "8",
        "A",
        "Substitute t = 5: x(5 - 3) = x(2) = 2.",
        "Intermediate"
    ),
    (
        "If x(t) = 2t, what is the output of y(t) = x(2t)?",
        "2t",
        "4t",
        "t",
        "8t",
        "B",
        "Substituting 2t into x(t) = 2t gives x(2t) = 2(2t) = 4t.",
        "Intermediate"
    ),
    (
        "If x(t) = t + 1, what is the result of time reversal x(-t)?",
        "t + 1",
        "-t + 1",
        "-t - 1",
        "t - 1",
        "B",
        "Replace t with -t: x(-t) = -t + 1.",
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

    print("EEE Signals and Systems Topic 3 added successfully!")
    print("Subject:", subject)
    print("Topic:", topic)
    print("New questions added:", inserted)
    print("Existing questions skipped:", skipped)

except Exception as error:
    connection.rollback()
    print("Error:", error)

finally:
    connection.close()
