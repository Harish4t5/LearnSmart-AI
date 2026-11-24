
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "database" / "ideathon2k26.db"

connection = sqlite3.connect(DB_PATH)

subject = "Signals and Systems"
branch_code = "EEE"
semester = 3
topic = "Convolution"

questions = [
    (
        "What is convolution mainly used for in Signals and Systems?",
        "Finding the output of an LTI system",
        "Measuring resistance",
        "Calculating electrical power only",
        "Generating random signals",
        "A",
        "Convolution is used to determine the output of an LTI system from its input and impulse response.",
        "Beginner"
    ),
    (
        "Which symbol is commonly used to represent convolution?",
        "+",
        "-",
        "*",
        "/",
        "C",
        "The asterisk symbol is commonly used to represent convolution.",
        "Beginner"
    ),
    (
        "What is the impulse response of a system?",
        "The output when the input is a unit impulse",
        "The output when the input is zero",
        "The maximum input voltage",
        "The average power of a signal",
        "A",
        "The impulse response is the output of a system when its input is a unit impulse.",
        "Beginner"
    ),
    (
        "Which mathematical operation is used in continuous-time convolution?",
        "Differentiation only",
        "Integration",
        "Matrix multiplication only",
        "Division",
        "B",
        "Continuous-time convolution is defined using an integral.",
        "Beginner"
    ),
    (
        "Which mathematical operation is used in discrete-time convolution?",
        "Summation",
        "Integration",
        "Differentiation",
        "Subtraction only",
        "A",
        "Discrete-time convolution is calculated using a summation over the sample index.",
        "Beginner"
    ),
    (
        "For an LTI system, if x(t) is the input and h(t) is the impulse response, the output y(t) is:",
        "x(t) + h(t)",
        "x(t) - h(t)",
        "x(t) * h(t)",
        "x(t) / h(t)",
        "C",
        "The output of a continuous-time LTI system is the convolution of its input and impulse response.",
        "Intermediate"
    ),
    (
        "What is the convolution of x[n] = delta[n] and any discrete-time signal h[n]?",
        "Zero",
        "h[n]",
        "1",
        "delta[n] only",
        "B",
        "Convolution with the unit impulse leaves the other signal unchanged.",
        "Intermediate"
    ),
    (
        "If x(t) = delta(t) and h(t) is the impulse response, what is the output of the LTI system?",
        "Zero",
        "delta(t)",
        "h(t)",
        "1",
        "C",
        "Convolving a signal with the unit impulse reproduces that signal: delta(t) * h(t) = h(t).",
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

    print("EEE Signals and Systems Topic 6 added successfully!")
    print("Subject:", subject)
    print("Topic:", topic)
    print("New questions added:", inserted)
    print("Existing questions skipped:", skipped)

except Exception as error:
    connection.rollback()
    print("Error:", error)

finally:
    connection.close()
