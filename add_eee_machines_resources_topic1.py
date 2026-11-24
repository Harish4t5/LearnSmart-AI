
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "database" / "ideathon2k26.db"

connection = sqlite3.connect(DB_PATH)
cursor = connection.cursor()

subject = "Electrical Machines I"
topic = "Introduction to Electrical Machines"

resources = [
    (
        subject,
        topic,
        "Beginner",
        "Article",
        "Introduction to Electrical Machines - Study Notes",
        "",
        """INTRODUCTION TO ELECTRICAL MACHINES

1. What is an Electrical Machine?

An electrical machine is a device that converts energy
from one form to another using electromagnetic principles.

2. Main Types of Electrical Machines

A. Generator:
Converts mechanical energy into electrical energy.

B. Motor:
Converts electrical energy into mechanical energy.

C. Transformer:
Transfers electrical energy between circuits through
electromagnetic induction, generally changing voltage
and current levels without changing frequency.

3. Basic Working Principle

Electrical machines operate using electromagnetic
induction and the interaction between magnetic fields
and electric currents.

Faraday's Law:
An EMF is induced when the magnetic flux linking a
circuit changes.

4. Classification

Electrical machines can be classified as:

- DC machines
- AC machines
- Transformers
- Synchronous machines
- Induction machines

5. Important Components

- Stator: Stationary part of a machine.
- Rotor: Rotating part of a machine.
- Winding: Conductors used to carry current.
- Magnetic core: Provides a path for magnetic flux.
- Shaft: Transfers mechanical rotation.
- Bearings: Support the rotating shaft.

6. Energy Conversion

Generator:
Mechanical energy -> Electrical energy

Motor:
Electrical energy -> Mechanical energy

Transformer:
Electrical energy -> Electrical energy at a
different voltage/current level.

7. Applications

- Electric power generation.
- Industrial drives.
- Pumps and fans.
- Electric vehicles.
- Domestic appliances.
- Power transmission and distribution.

8. Important Differences

Motor:
Takes electrical input and produces mechanical output.

Generator:
Takes mechanical input and produces electrical output.

Transformer:
Transfers electrical energy between circuits using
mutual electromagnetic induction.

9. Important Points to Remember

- Motors and generators are electromechanical devices.
- A transformer operates on electromagnetic induction.
- The stator is stationary.
- The rotor is the rotating part.
- Electrical machines are essential in power systems
  and industrial applications."""
    ),
    (
        subject,
        topic,
        "Intermediate",
        "Documentation",
        "NPTEL Electrical Machines Course",
        "https://nptel.ac.in/courses/108105017",
        "Additional university-level learning resource covering "
        "electrical machine fundamentals and electromagnetic principles."
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

    print("Electrical Machines I - Topic 1 resources processed!")
    print("Inserted:", inserted)
    print("Skipped:", skipped)

except Exception as error:
    connection.rollback()
    print("Error:", error)

finally:
    connection.close()
