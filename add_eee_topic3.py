
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "database" / "ideathon2k26.db"

connection = sqlite3.connect(DB_PATH)

subject = "Power Systems I"
branch_code = "EEE"
semester = 3
topic = "Transmission and Distribution"

questions = [
    (
        "What is the main purpose of an electrical transmission system?",
        "To generate electricity",
        "To transfer electrical power over long distances",
        "To consume electrical energy",
        "To store electrical energy",
        "B",
        "Transmission systems carry electrical power from generating stations to substations over long distances.",
        "Beginner"
    ),
    (
        "Which voltage level is generally used for long-distance power transmission?",
        "Low voltage",
        "Medium voltage",
        "High voltage",
        "Zero voltage",
        "C",
        "High voltage transmission reduces current and helps reduce power losses.",
        "Beginner"
    ),
    (
        "Where does electrical power generally go after generation?",
        "Directly to consumers",
        "To a transmission substation or grid",
        "To household appliances",
        "To distribution transformers only",
        "B",
        "Generated electricity is transferred to the transmission network through suitable substations and switchyards.",
        "Beginner"
    ),
    (
        "What is the main function of a distribution transformer?",
        "To increase generation",
        "To reduce voltage for consumer use",
        "To generate mechanical energy",
        "To measure frequency",
        "B",
        "Distribution transformers step down voltage to levels suitable for consumers.",
        "Beginner"
    ),
    (
        "Which component connects the distribution network to an individual consumer?",
        "Service mains",
        "Generator",
        "Turbine",
        "Transmission tower",
        "A",
        "Service mains provide the final connection from the distribution system to the consumer.",
        "Beginner"
    ),
    (
        "Why is electrical power transmitted at high voltage?",
        "To increase current",
        "To reduce line current and I²R losses for a given power transfer",
        "To increase resistance",
        "To eliminate transformers",
        "B",
        "For a given transmitted power, higher voltage means lower current, reducing resistive line losses.",
        "Intermediate"
    ),
    (
        "What is the correct order of the basic power supply system?",
        "Distribution → Generation → Transmission",
        "Transmission → Generation → Distribution",
        "Generation → Transmission → Distribution",
        "Generation → Distribution → Transmission",
        "C",
        "Electrical power is generated, transmitted over long distances, and then distributed to consumers.",
        "Intermediate"
    ),
    (
        "Which statement correctly describes a feeder in a distribution system?",
        "It directly generates electrical power",
        "It carries power from a substation towards distribution areas",
        "It converts AC into DC",
        "It stores electrical energy",
        "B",
        "A feeder carries electrical power from a distribution substation towards distribution points. Its current rating is an important design consideration.",
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
            INSERT INTO quiz_questions (
                subject, topic, question,
                option_a, option_b, option_c, option_d,
                correct_answer, explanation, difficulty,
                branch_code, semester
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

    print("EEE Topic 3 added successfully!")
    print("Subject:", subject)
    print("Topic:", topic)
    print("New questions added:", inserted)
    print("Existing questions skipped:", skipped)

except Exception as error:
    connection.rollback()
    print("Error:", error)

finally:
    connection.close()
