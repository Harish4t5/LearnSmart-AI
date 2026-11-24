
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "database" / "ideathon2k26.db"

connection = sqlite3.connect(DB_PATH)

subject = "Power Systems I"
branch_code = "EEE"
semester = 3
topic = "Substations"

questions = [
    (
        "What is the main function of an electrical substation?",
        "To manufacture electrical equipment",
        "To change voltage levels and control power flow",
        "To generate coal",
        "To store mechanical energy",
        "B",
        "Substations help transform voltage levels, switch circuits and control electrical power flow.",
        "Beginner"
    ),
    (
        "Which type of substation increases voltage for long-distance transmission?",
        "Distribution substation",
        "Step-down substation",
        "Step-up substation",
        "Switching substation",
        "C",
        "A step-up substation increases generated voltage to a suitable transmission level.",
        "Beginner"
    ),
    (
        "Which equipment is used to change voltage levels in a substation?",
        "Transformer",
        "Insulator",
        "Relay",
        "Fuse wire",
        "A",
        "Power transformers increase or decrease voltage levels in substations.",
        "Beginner"
    ),
    (
        "What is the function of a busbar in a substation?",
        "To generate electricity",
        "To collect and distribute electrical power to circuits",
        "To measure temperature",
        "To provide mechanical support to towers",
        "B",
        "A busbar is a common conducting arrangement used to connect incoming and outgoing circuits.",
        "Beginner"
    ),
    (
        "Which device is used to interrupt fault current?",
        "Isolator",
        "Circuit breaker",
        "Busbar",
        "Lightning arrester",
        "B",
        "A circuit breaker can make, carry and interrupt current under specified normal and fault conditions.",
        "Beginner"
    ),
    (
        "Why is an isolator generally operated only after the circuit breaker has opened?",
        "Because an isolator is not designed to interrupt load or fault current",
        "Because it increases the voltage",
        "Because it generates electrical power",
        "Because it controls frequency",
        "A",
        "An isolator provides visible isolation and is normally operated under no-load conditions.",
        "Intermediate"
    ),
    (
        "Which protective device helps protect substation equipment against lightning surges?",
        "Current transformer",
        "Lightning arrester",
        "Isolator",
        "Bus coupler",
        "B",
        "A lightning arrester limits transient overvoltages and diverts surge current to earth.",
        "Intermediate"
    ),
    (
        "What is the main purpose of a current transformer (CT) in a substation?",
        "To increase transmission frequency",
        "To reduce high current to a measurable value for metering and protection",
        "To generate electrical energy",
        "To replace the power transformer",
        "B",
        "A CT provides a reduced proportional current for measuring instruments and protective relays.",
        "Intermediate"
    )
]

inserted = 0
skipped = 0

try:
    for q in questions:
        existing = connection.execute("""
            SELECT id
            FROM quiz_questions
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

    print("EEE Topic 6 added successfully!")
    print("Subject:", subject)
    print("Topic:", topic)
    print("New questions added:", inserted)
    print("Existing questions skipped:", skipped)

except Exception as error:
    connection.rollback()
    print("Error:", error)

finally:
    connection.close()
