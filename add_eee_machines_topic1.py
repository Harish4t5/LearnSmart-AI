
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "database" / "ideathon2k26.db"

connection = sqlite3.connect(DB_PATH)

subject = "Electrical Machines I"
branch_code = "EEE"
semester = 4
topic = "Introduction to Electrical Machines"

questions = [
    (
        "What is the main function of an electrical machine?",
        "To convert electrical energy into mechanical energy or vice versa",
        "To store chemical energy",
        "To measure temperature",
        "To generate light only",
        "A",
        "Electrical machines convert energy between electrical and mechanical forms.",
        "Beginner"
    ),
    (
        "Which electrical machine converts mechanical energy into electrical energy?",
        "Motor",
        "Generator",
        "Transformer",
        "Rectifier",
        "B",
        "A generator converts mechanical energy into electrical energy.",
        "Beginner"
    ),
    (
        "Which electrical machine converts electrical energy into mechanical energy?",
        "Generator",
        "Transformer",
        "Motor",
        "Alternator only",
        "C",
        "An electric motor converts electrical energy into mechanical energy.",
        "Beginner"
    ),
    (
        "Which device transfers electrical energy between circuits through electromagnetic induction?",
        "Transformer",
        "Resistor",
        "Capacitor",
        "Fuse",
        "A",
        "A transformer transfers electrical energy between circuits through electromagnetic induction.",
        "Beginner"
    ),
    (
        "Which principle is commonly used in the operation of transformers?",
        "Electrostatic attraction",
        "Mutual induction",
        "Chemical reaction",
        "Thermal expansion",
        "B",
        "Transformers operate on the principle of mutual electromagnetic induction.",
        "Beginner"
    ),
    (
        "Which part of a rotating electrical machine generally carries the armature winding?",
        "Frame only",
        "Armature",
        "Foundation",
        "Terminal box",
        "B",
        "The armature is the part in which the main electromotive force is induced or through which the armature current flows.",
        "Intermediate"
    ),
    (
        "What is the main purpose of the magnetic core in an electrical machine?",
        "To provide a low-reluctance path for magnetic flux",
        "To increase mechanical friction",
        "To store electrical charge",
        "To eliminate all copper losses",
        "A",
        "The magnetic core provides an effective path for magnetic flux and helps reduce magnetic reluctance.",
        "Intermediate"
    ),
    (
        "Which type of electrical machine can operate as both a motor and a generator?",
        "Only a transformer",
        "Only a DC motor",
        "A reversible electrical machine",
        "Only a rectifier",
        "C",
        "Many electrical machines are reversible and can operate as either motors or generators depending on the direction of energy conversion.",
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

    print("EEE Electrical Machines I Topic 1 added successfully!")
    print("Subject:", subject)
    print("Topic:", topic)
    print("New questions added:", inserted)
    print("Existing questions skipped:", skipped)

except Exception as error:
    connection.rollback()
    print("Error:", error)

finally:
    connection.close()
