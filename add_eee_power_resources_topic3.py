
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "database" / "ideathon2k26.db"

connection = sqlite3.connect(DB_PATH)
cursor = connection.cursor()

subject = "Power Systems I"
topic = "Transmission and Distribution"

resources = [
    (
        subject,
        topic,
        "Beginner",
        "Article",
        "Transmission and Distribution - Study Notes",
        "",
        """Electrical power transmission and distribution deliver
electricity from generating stations to consumers.

1. Transmission System:
- Carries bulk electrical power over long distances.
- Uses high voltage to reduce current and I²R losses.
- Includes transmission lines, towers and substations.

2. Distribution System:
- Supplies electrical energy to local consumers.
- Receives power from transmission substations.
- Uses feeders, distributors and service mains.

Important components:

Feeder:
Carries power from a substation towards distribution areas.
Its current-carrying capacity is an important design factor.

Distributor:
A conductor from which consumer connections are tapped.
Its current varies along its length.

Service Mains:
Connect the distributor to individual consumer premises.

Common voltage transformation:
Step-up transformer -> increases voltage for transmission.
Step-down transformer -> reduces voltage for distribution.

Power flow:
Generating Station -> Step-up Transformer ->
Transmission Line -> Receiving Substation ->
Distribution Network -> Consumers.

Advantages of high-voltage transmission:
For a given power and power factor, higher voltage means
lower current, reducing resistive power losses."""
    ),
    (
        subject,
        topic,
        "Intermediate",
        "Video",
        "Power System Generation, Transmission and Distribution - NPTEL",
        "https://nptel.ac.in/courses/108102047",
        "NPTEL course by Prof. D. P. Kothari, IIT Delhi. "
        "Study transmission line parameters, performance, voltage "
        "control, underground cables and distribution systems."
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
    print("Power Systems I - Topic 3 resources processed!")
    print("Inserted:", inserted)
    print("Skipped:", skipped)

except Exception as error:
    connection.rollback()
    print("Error:", error)

finally:
    connection.close()
