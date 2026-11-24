
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "database" / "ideathon2k26.db"

connection = sqlite3.connect(DB_PATH)

subject = "Power Systems I"
branch_code = "EEE"
semester = 3
topic = "Transmission Line Parameters"

questions = [
    (
        "Which of the following is a primary parameter of a transmission line?",
        "Resistance",
        "Frequency",
        "Power factor",
        "Efficiency",
        "A",
        "Resistance is one of the four primary transmission line parameters.",
        "Beginner"
    ),
    (
        "What is the SI unit of electrical resistance?",
        "Farad",
        "Henry",
        "Ohm",
        "Siemens",
        "C",
        "Electrical resistance is measured in ohms.",
        "Beginner"
    ),
    (
        "Which parameter represents the ability of a transmission line to store energy in a magnetic field?",
        "Resistance",
        "Inductance",
        "Capacitance",
        "Conductance",
        "B",
        "Inductance is associated with the magnetic field produced by current flowing through a conductor.",
        "Beginner"
    ),
    (
        "What is the SI unit of capacitance?",
        "Henry",
        "Ohm",
        "Farad",
        "Watt",
        "C",
        "Capacitance is measured in farads.",
        "Beginner"
    ),
    (
        "Which parameter represents leakage current through the insulation between conductors?",
        "Inductance",
        "Conductance",
        "Resistance",
        "Reactance",
        "B",
        "Conductance represents the leakage path through insulation between conductors.",
        "Beginner"
    ),
    (
        "What is the main cause of power loss in a transmission line under normal operating conditions?",
        "Capacitive charging",
        "I²R loss in conductors",
        "Magnetic energy storage",
        "Voltage transformation",
        "B",
        "Conductor resistance causes real power loss according to the I²R relationship.",
        "Intermediate"
    ),
    (
        "Which relationship describes the capacitive reactance of a transmission line?",
        "Xc = 2πfC",
        "Xc = 1/(2πfC)",
        "Xc = 2πfL",
        "Xc = R/I",
        "B",
        "Capacitive reactance is inversely proportional to frequency and capacitance.",
        "Intermediate"
    ),
    (
        "If the frequency of a transmission line increases while inductance remains constant, what happens to inductive reactance?",
        "It decreases",
        "It becomes zero",
        "It increases",
        "It remains unchanged",
        "C",
        "Inductive reactance is XL = 2πfL, so it increases with frequency when inductance is constant.",
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

    print("EEE Topic 4 added successfully!")
    print("Subject:", subject)
    print("Topic:", topic)
    print("New questions added:", inserted)
    print("Existing questions skipped:", skipped)

except Exception as error:
    connection.rollback()
    print("Error:", error)

finally:
    connection.close()
