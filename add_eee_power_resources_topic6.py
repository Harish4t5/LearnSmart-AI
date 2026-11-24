
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "database" / "ideathon2k26.db"

connection = sqlite3.connect(DB_PATH)
cursor = connection.cursor()

subject = "Power Systems I"
topic = "Substations"

resources = [
    (
        subject,
        topic,
        "Beginner",
        "Article",
        "Electrical Substations - Study Notes",
        "",
        """ELECTRICAL SUBSTATIONS - STUDY NOTES

1. Introduction

A substation is an important part of an electrical power
system. It receives, transforms, controls and distributes
electrical power.

2. Main Functions

- Step up or step down voltage.
- Switch transmission and distribution circuits.
- Protect equipment during electrical faults.
- Control and monitor power flow.
- Improve reliability of power supply.

3. Types of Substations

Based on function:

A. Step-up Substation:
Increases generator voltage for long-distance transmission.

B. Step-down Substation:
Reduces transmission voltage for distribution.

C. Distribution Substation:
Reduces voltage to levels suitable for local consumers.

Based on construction:

- Indoor Substation: Equipment is installed inside a building.
- Outdoor Substation: Equipment is installed in an open switchyard.
- Gas-Insulated Substation (GIS): Uses gas-insulated
  enclosures for compact equipment arrangements.

4. Important Substation Equipment

- Power Transformer: Changes voltage levels.
- Busbar: Common electrical connection for incoming
  and outgoing circuits.
- Circuit Breaker: Makes or interrupts current,
  including fault current within its rated capability.
- Isolator: Provides isolation after the circuit
  has been safely de-energized.
- Current Transformer (CT): Provides a reduced
  current signal for metering and protection.
- Potential Transformer (PT): Provides a reduced
  voltage signal for metering and protection.
- Lightning Arrester: Protects equipment against
  lightning and switching surges.
- Protective Relay: Detects abnormal conditions
  and initiates circuit-breaker tripping.

5. Busbar Arrangements

Common arrangements include:
- Single Busbar
- Double Busbar
- Main and Transfer Busbar
- Ring Busbar

The arrangement affects reliability, flexibility,
maintenance and cost.

6. Importance of Earthing

Earthing provides a safe path for fault current
and helps limit dangerous touch voltages.

Remember:
A substation is a major connection point between
generation, transmission and distribution systems."""
    ),
    (
        subject,
        topic,
        "Intermediate",
        "Video",
        "Electrical Distribution System Analysis - NPTEL IIT Roorkee",
        "https://nptel.ac.in/courses/108107112",
        "NPTEL course by Prof. N. P. Padhy and Late Prof. G. B. Kumbhar, "
        "IIT Roorkee. Covers distribution-system components, "
        "substation and busbar layouts, feeders, transformers, "
        "voltage regulation and distribution-system analysis."
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

    print("Power Systems I - Topic 6 resources processed!")
    print("Inserted:", inserted)
    print("Skipped:", skipped)

except Exception as error:
    connection.rollback()
    print("Error:", error)

finally:
    connection.close()
