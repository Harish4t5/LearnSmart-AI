
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "database" / "ideathon2k26.db"

connection = sqlite3.connect(DB_PATH)
cursor = connection.cursor()

subject = "Power Systems I"
branch_code = "EEE"
semester = 3
topic = "Introduction to Power Systems"

resources = [
    (
        subject,
        topic,
        "Beginner",
        "Article",
        "Introduction to Power Systems - Study Notes",
        "",
        """A power system is an interconnected network used to generate,
transmit, and distribute electrical energy to consumers.

Main stages:
1. Generation: Electricity is produced at power stations.
2. Transmission: High-voltage lines carry electricity over long distances.
3. Distribution: Electricity is supplied to homes, industries, and offices.

Main components:
- Generators: Convert mechanical energy into electrical energy.
- Transformers: Increase or decrease voltage levels.
- Transmission lines: Carry electrical power over distances.
- Substations: Control, protect, and transform electrical power.
- Distribution networks: Deliver electricity to consumers.

Why high voltage transmission?
For the same transmitted power, increasing voltage reduces current.
Lower current reduces I²R power losses in transmission lines.

Remember:
Generation -> Transmission -> Distribution -> Consumers."""
    ),
    (
        subject,
        topic,
        "Intermediate",
        "Video",
        "Power System Generation, Transmission and Distribution - NPTEL",
        "https://nptel.ac.in/courses/108102047",
        "NPTEL course by Prof. D. P. Kothari, IIT Delhi. "
        "Covers the structure of power systems, energy generation, "
        "transmission lines, distribution systems, and related concepts."
    )
]

inserted = 0
skipped = 0

try:
    for resource in resources:
        cursor.execute("""
            SELECT id FROM learning_resources
            WHERE subject = ?
            AND topic = ?
            AND level = ?
            AND resource_type = ?
            AND title = ?
        """, (
            resource[0], resource[1], resource[2],
            resource[3], resource[4]
        ))

        if cursor.fetchone():
            skipped += 1
            continue

        cursor.execute("""
            INSERT INTO learning_resources
            (subject, topic, level, resource_type, title, url, description)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, resource)

        inserted += 1

    connection.commit()

    print("Power Systems I - Topic 1 resources processed!")
    print("Inserted:", inserted)
    print("Skipped (already existing):", skipped)

except Exception as error:
    connection.rollback()
    print("Error:", error)

finally:
    connection.close()
