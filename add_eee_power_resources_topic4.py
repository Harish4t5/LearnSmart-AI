
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "database" / "ideathon2k26.db"

connection = sqlite3.connect(DB_PATH)
cursor = connection.cursor()

subject = "Power Systems I"
topic = "Transmission Line Parameters"

resources = [
    (
        subject,
        topic,
        "Beginner",
        "Article",
        "Transmission Line Parameters - Study Notes",
        "",
        """A transmission line has four important electrical parameters:

1. Resistance (R):
- Opposes the flow of electric current.
- Depends on conductor material, length and cross-sectional area.
- Causes power loss in the form of heat.
- Formula: R = rho * L / A

2. Inductance (L):
- Arises due to the magnetic field produced by current.
- Opposes changes in current.
- Depends on conductor arrangement and spacing.

3. Capacitance (C):
- Exists between conductors and between conductors and earth.
- Arises due to the electric field and charge separation.
- Affects charging current and voltage behaviour.

4. Conductance (G):
- Represents leakage current through the insulation between
  conductors or between a conductor and earth.
- Depends on insulation properties and environmental conditions.

Important terms:
- GMR: Geometric Mean Radius, used in inductance calculations.
- GMD: Geometric Mean Distance, used to represent conductor spacing.
- Skin Effect: AC current tends to concentrate near the conductor surface.
- Transposition: Periodic interchange of conductor positions
  to balance line parameters.

Remember:
R and L are series parameters.
C and G are shunt parameters.

All four parameters influence transmission-line performance."""
    ),
    (
        subject,
        topic,
        "Intermediate",
        "Video",
        "Power System Analysis - NPTEL IIT Kharagpur",
        "https://nptel.ac.in/courses/108105067",
        "NPTEL course by Prof. A. K. Sinha, IIT Kharagpur. "
        "Covers transmission-line resistance, inductance, "
        "three-phase inductance calculations, capacitance, "
        "line modelling and steady-state operation."
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
    print("Power Systems I - Topic 4 resources processed!")
    print("Inserted:", inserted)
    print("Skipped:", skipped)

except Exception as error:
    connection.rollback()
    print("Error:", error)

finally:
    connection.close()
