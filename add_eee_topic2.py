
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "database" / "ideathon2k26.db"

connection = sqlite3.connect(DB_PATH)

subject = "Power Systems I"
branch_code = "EEE"
semester = 3
topic = "Electrical Power Generation"

questions = [
    (
        "Which of the following is a conventional source of electrical energy?",
        "Solar energy",
        "Wind energy",
        "Coal",
        "Tidal energy",
        "C",
        "Coal is a conventional energy source commonly used in thermal power stations.",
        "Beginner"
    ),
    (
        "Which energy conversion takes place in a hydroelectric power station?",
        "Electrical to chemical",
        "Potential energy of water to electrical energy",
        "Solar to electrical",
        "Chemical to nuclear",
        "B",
        "Water stored at a height drives turbines connected to electrical generators.",
        "Beginner"
    ),
    (
        "Which component converts mechanical energy into electrical energy in a power station?",
        "Transformer",
        "Generator",
        "Circuit breaker",
        "Insulator",
        "B",
        "An electrical generator converts mechanical energy into electrical energy.",
        "Beginner"
    ),
    (
        "Which fuel is commonly used in nuclear power stations?",
        "Coal",
        "Uranium",
        "Diesel",
        "Natural gas",
        "B",
        "Uranium is commonly used as nuclear fuel.",
        "Beginner"
    ),
    (
        "Which of these is a renewable source of energy?",
        "Coal",
        "Petroleum",
        "Natural gas",
        "Wind",
        "D",
        "Wind is naturally replenished and is a renewable energy source.",
        "Beginner"
    ),
    (
        "In a thermal power station, what is the primary function of a boiler?",
        "To generate steam using heat",
        "To increase transmission voltage",
        "To store electrical energy",
        "To cool the generator",
        "A",
        "The boiler uses heat from fuel combustion to convert water into high-pressure steam.",
        "Intermediate"
    ),
    (
        "Why is a turbine used in a hydroelectric power station?",
        "To increase water temperature",
        "To convert water energy into mechanical energy",
        "To convert AC into DC",
        "To reduce transmission losses",
        "B",
        "Moving water rotates the turbine, converting hydraulic energy into mechanical energy.",
        "Intermediate"
    ),
    (
        "Which energy conversion sequence is correct in a thermal power station?",
        "Chemical → Thermal → Mechanical → Electrical",
        "Electrical → Thermal → Chemical → Mechanical",
        "Mechanical → Chemical → Electrical → Thermal",
        "Thermal → Electrical → Chemical → Mechanical",
        "A",
        "Fuel chemical energy produces heat, steam drives a turbine, and the generator produces electricity.",
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
            INSERT INTO quiz_questions
            (
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

    print("EEE Topic 2 added successfully!")
    print("Subject:", subject)
    print("Topic:", topic)
    print("New questions added:", inserted)
    print("Existing questions skipped:", skipped)

except Exception as error:
    connection.rollback()
    print("Error:", error)

finally:
    connection.close()
