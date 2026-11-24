
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "database" / "ideathon2k26.db"

connection = sqlite3.connect(DB_PATH)
cursor = connection.cursor()

subject = "Network Theory"
topic = "Kirchhoff's Laws"

resources = [
    (
        subject,
        topic,
        "Beginner",
        "Article",
        "Kirchhoff's Laws - Study Notes",
        "",
        """KIRCHHOFF'S LAWS - STUDY NOTES

Kirchhoff's laws are fundamental rules used to analyse
electrical circuits.

1. Kirchhoff's Current Law (KCL)

Statement:
The algebraic sum of currents at any junction is zero.

In simple words:
Total current entering a junction equals total current
leaving that junction.

Formula:
Sum of incoming currents = Sum of outgoing currents

Example:
If 5 A enters a junction and 2 A and I leave it:

5 = 2 + I
I = 3 A

KCL is based on the conservation of electric charge.

2. Kirchhoff's Voltage Law (KVL)

Statement:
The algebraic sum of all voltages around any closed loop
of a circuit is zero.

In simple words:
Total voltage rises equal total voltage drops.

Formula:
Sum of voltage rises = Sum of voltage drops

Example:
A 12 V source supplies two series resistors.
Their voltage drops are 5 V and V2.

12 = 5 + V2
V2 = 7 V

KVL is based on the conservation of energy.

3. Important Terms

Junction:
A point where three or more branches meet.

Branch:
A part of a circuit between two nodes.

Loop:
Any closed path in an electrical network.

Mesh:
A loop that contains no other loop inside it.

4. Sign Conventions

For KCL:
Choose entering or leaving currents as positive
and use the opposite sign for the other direction.

For KVL:
- Moving from negative to positive terminal: voltage rise.
- Moving from positive to negative terminal: voltage drop.
- Across a resistor in the direction of current: voltage drop.

5. Applications

- Finding unknown currents.
- Calculating unknown voltages.
- Nodal analysis.
- Mesh analysis.
- Solving complex electrical networks.

Remember:
KCL -> Conservation of charge at a junction.
KVL -> Conservation of energy around a closed loop."""
    ),
    (
        subject,
        topic,
        "Intermediate",
        "Video",
        "Network Analysis - NPTEL IIT Kharagpur",
        "https://nptel.ac.in/courses/108105159",
        "NPTEL course by IIT Kharagpur covering Kirchhoff's "
        "Current Law, Kirchhoff's Voltage Law, nodal analysis, "
        "mesh analysis and systematic electrical network solving."
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

    print("Network Theory - Topic 2 resources processed!")
    print("Inserted:", inserted)
    print("Skipped:", skipped)

except Exception as error:
    connection.rollback()
    print("Error:", error)

finally:
    connection.close()
