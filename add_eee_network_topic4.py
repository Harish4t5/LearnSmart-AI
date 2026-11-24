
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "database" / "ideathon2k26.db"

connection = sqlite3.connect(DB_PATH)

subject = "Network Theory"
branch_code = "EEE"
semester = 3
topic = "Transient Analysis"

questions = [
    (
        "What is a transient response in an electrical circuit?",
        "The response after a sudden change in circuit conditions",
        "The steady-state response only",
        "The response at zero frequency",
        "The permanent failure of a circuit",
        "A",
        "Transient response describes the temporary behavior of a circuit immediately after switching or another sudden change.",
        "Beginner"
    ),
    (
        "What is the time constant of a series RC circuit?",
        "R/C",
        "RC",
        "C/R",
        "1/RC",
        "B",
        "The time constant of a series RC circuit is the product of resistance and capacitance.",
        "Beginner"
    ),
    (
        "What is the time constant of a series RL circuit?",
        "RL",
        "R/L",
        "L/R",
        "1/RL",
        "C",
        "The time constant of a series RL circuit is L divided by R.",
        "Beginner"
    ),
    (
        "What happens to the voltage across an ideal capacitor at the instant of switching?",
        "It changes instantaneously",
        "It cannot change instantaneously",
        "It always becomes infinite",
        "It always becomes zero",
        "B",
        "Capacitor voltage cannot change instantaneously because that would require an infinite current.",
        "Beginner"
    ),
    (
        "What happens to the current through an ideal inductor at the instant of switching?",
        "It changes instantaneously",
        "It cannot change instantaneously",
        "It always becomes zero",
        "It becomes infinite",
        "B",
        "Inductor current cannot change instantaneously because that would require an infinite voltage.",
        "Beginner"
    ),
    (
        "A series RC circuit has R = 10 kΩ and C = 100 μF. What is its time constant?",
        "0.1 seconds",
        "1 second",
        "10 seconds",
        "100 seconds",
        "B",
        "Tau = RC = 10000 × 100 × 10^-6 = 1 second.",
        "Intermediate"
    ),
    (
        "A series RL circuit has L = 2 H and R = 4 Ω. Find its time constant.",
        "0.25 seconds",
        "0.5 seconds",
        "2 seconds",
        "8 seconds",
        "B",
        "Tau = L/R = 2/4 = 0.5 seconds.",
        "Intermediate"
    ),
    (
        "Approximately what percentage of its final value does a charging capacitor reach after one time constant?",
        "36.8%",
        "50%",
        "63.2%",
        "100%",
        "C",
        "For a charging RC circuit, capacitor voltage reaches approximately 63.2% of its final value after one time constant.",
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

    print("EEE Network Theory Topic 4 added successfully!")
    print("Subject:", subject)
    print("Topic:", topic)
    print("New questions added:", inserted)
    print("Existing questions skipped:", skipped)

except Exception as error:
    connection.rollback()
    print("Error:", error)

finally:
    connection.close()
