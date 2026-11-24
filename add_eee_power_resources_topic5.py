
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "database" / "ideathon2k26.db"

connection = sqlite3.connect(DB_PATH)
cursor = connection.cursor()

subject = "Power Systems I"
topic = "Insulators and Cables"

resources = [
    (
        subject,
        topic,
        "Beginner",
        "Article",
        "Insulators and Underground Cables - Study Notes",
        "",
        """INSULATORS AND CABLES - STUDY NOTES

1. Electrical Insulators

An insulator prevents unwanted flow of electric current
between a live conductor and its support or earth.

Main functions:
- Support overhead conductors mechanically.
- Provide electrical insulation.
- Prevent leakage current to supporting structures.

Types of overhead line insulators:

A. Pin Insulator:
Mounted on a pin attached to the cross-arm.
Commonly used for lower-voltage distribution lines.

B. Suspension Insulator:
Consists of a string of disc units.
Used for high-voltage transmission lines.

C. Strain Insulator:
Designed to withstand high mechanical tension.
Used at dead ends and sharp line turns.

D. Shackle Insulator:
Commonly used in low-voltage distribution systems.

Important terms:
- Flashover: Discharge over the surface of an insulator.
- Puncture: Electrical breakdown through the insulator material.
- String Efficiency: Indicates how uniformly voltage is
  distributed across a suspension-insulator string.

2. Underground Cables

Underground cables transmit electrical power below ground.

Main parts:
- Conductor: Carries electric current.
- Insulation: Prevents current leakage.
- Metallic sheath: Protects against moisture and provides
  a barrier around the insulation.
- Bedding: Provides protection to the sheath.
- Armouring: Provides mechanical protection.
- Outer serving: Protects the cable from external damage.

Types based on voltage:
- Low-voltage cables
- Medium-voltage cables
- High-voltage cables

Advantages:
- Less affected by weather.
- Better appearance in urban areas.
- Lower exposure to external physical damage.

Limitations:
- Higher installation cost.
- Fault location and repair can be difficult.

Remember:
Insulators support and isolate overhead conductors.
Cables provide insulated paths for underground power transmission."""
    ),
    (
        subject,
        topic,
        "Intermediate",
        "Video",
        "Power System Engineering - Insulators and Cables (NPTEL)",
        "https://nptel.ac.in/courses/108105104",
        "NPTEL lectures covering overhead-line insulators, "
        "underground cable construction, cable characteristics, "
        "transient overvoltages and insulation coordination."
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
    print("Power Systems I - Topic 5 resources processed!")
    print("Inserted:", inserted)
    print("Skipped:", skipped)

except Exception as error:
    connection.rollback()
    print("Error:", error)

finally:
    connection.close()
