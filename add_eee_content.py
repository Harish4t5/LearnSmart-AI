
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "database" / "ideathon2k26.db"

connection = sqlite3.connect(DB_PATH)

subject = "Power Systems I"
branch_code = "EEE"
semester = 3
topic = "Introduction to Power Systems"

questions = [
    (
        "What is the main purpose of an electrical power system?",
        "To generate, transmit and distribute electrical energy",
        "To store mechanical energy",
        "To convert electrical energy into fuel",
        "To produce only direct current",
        "A",
        "An electrical power system delivers electrical energy from generating stations to consumers.",
        "Beginner"
    ),
    (
        "Which of the following is a conventional source of electrical energy?",
        "Solar energy",
        "Wind energy",
        "Coal",
        "Tidal energy",
        "C",
        "Coal is a conventional energy source commonly used in thermal power plants.",
        "Beginner"
    ),
    (
        "Which component is primarily responsible for stepping up voltage at a generating station?",
        "Current transformer",
        "Power transformer",
        "Circuit breaker",
        "Isolator",
        "B",
        "A step-up transformer increases voltage to reduce current and transmission losses.",
        "Beginner"
    ),
    (
        "Why is electrical power transmitted at high voltage?",
        "To increase transmission current",
        "To reduce transmission losses",
        "To increase conductor resistance",
        "To reduce frequency",
        "B",
        "For a given power, higher voltage means lower current, reducing I²R losses.",
        "Intermediate"
    ),
    (
        "Which part of a power system delivers electricity directly to consumers?",
        "Generating station",
        "Transmission network",
        "Distribution network",
        "Turbine",
        "C",
        "The distribution network supplies electrical energy to domestic, commercial and industrial consumers.",
        "Beginner"
    ),
    (
        "Which of the following is generally used to interrupt fault current?",
        "Circuit breaker",
        "Insulator",
        "Busbar",
        "Lightning arrester",
        "A",
        "A circuit breaker can open a circuit and interrupt fault current under specified conditions.",
        "Intermediate"
    ),
    (
        "What is the standard frequency of AC power supply in India?",
        "25 Hz",
        "50 Hz",
        "60 Hz",
        "100 Hz",
        "B",
        "The standard AC supply frequency in India is 50 Hz.",
        "Beginner"
    ),
    (
        "Which sequence correctly represents the basic stages of an electrical power system?",
        "Distribution → Generation → Transmission",
        "Transmission → Generation → Distribution",
        "Generation → Transmission → Distribution",
        "Generation → Distribution → Transmission",
        "C",
        "Electrical energy is generated, transmitted over long distances and then distributed to consumers.",
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
        """, (
            subject,
            branch_code,
            semester,
            topic,
            q[0]
        )).fetchone()

        if existing:
            skipped += 1
            continue

        connection.execute("""
            INSERT INTO quiz_questions
            (
                subject,
                topic,
                question,
                option_a,
                option_b,
                option_c,
                option_d,
                correct_answer,
                explanation,
                difficulty,
                branch_code,
                semester
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            subject,
            topic,
            q[0],
            q[1],
            q[2],
            q[3],
            q[4],
            q[5],
            q[6],
            q[7],
            branch_code,
            semester
        ))

        inserted += 1

    connection.commit()

    print("EEE content added successfully!")
    print("Subject:", subject)
    print("Topic:", topic)
    print("New questions added:", inserted)
    print("Existing questions skipped:", skipped)

except Exception as error:
    connection.rollback()
    print("Error:", error)

finally:
    connection.close()
