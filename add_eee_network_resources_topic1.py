
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "database" / "ideathon2k26.db"

connection = sqlite3.connect(DB_PATH)
cursor = connection.cursor()

subject = "Network Theory"
topic = "Basic Electrical Network Concepts"

resources = [
    (
        subject,
        topic,
        "Beginner",
        "Article",
        "Basic Electrical Network Concepts - Study Notes",
        "",
        """BASIC ELECTRICAL NETWORK CONCEPTS

1. Electrical Network:
An electrical network is an interconnection of electrical
components such as resistors, inductors, capacitors and sources.

2. Electrical Circuit:
A network that contains at least one closed path for current
flow is called an electrical circuit.

3. Basic Circuit Elements:

Resistor (R):
- Opposes the flow of electric current.
- Unit: Ohm (Ω).
- Ohm's law: V = IR.
- Consumes electrical energy.

Inductor (L):
- Stores energy in a magnetic field.
- Opposes changes in current.
- Unit: Henry (H).
- Voltage relation: V = L(di/dt).

Capacitor (C):
- Stores energy in an electric field.
- Opposes changes in voltage.
- Unit: Farad (F).
- Current relation: I = C(dv/dt).

4. Electrical Sources:

Voltage Source:
Maintains a specified voltage across its terminals.

Current Source:
Maintains a specified current through its branch.

Independent Source:
Its value does not depend on another circuit variable.

Dependent Source:
Its value is controlled by another voltage or current
in the circuit.

5. Important Electrical Quantities:

- Voltage: Electrical potential difference, measured in volts.
- Current: Rate of flow of electric charge, measured in amperes.
- Resistance: Opposition to current, measured in ohms.
- Power: Rate of electrical energy transfer, measured in watts.
- Energy: Total work done or energy transferred, measured in joules.

6. Series and Parallel Connections:

Series:
Components share the same current.

Parallel:
Components share the same voltage.

Remember:
Voltage is measured in volts (V), current in amperes (A),
resistance in ohms (Ω), and power in watts (W)."""
    ),
    (
        subject,
        topic,
        "Intermediate",
        "Video",
        "Network Analysis - NPTEL IIT Kharagpur",
        "https://nptel.ac.in/courses/108105159",
        "Official NPTEL course by Prof. Tapas Kumar Bhattacharya, "
        "IIT Kharagpur. Covers circuit elements, voltage and current "
        "sources, KVL, KCL, mesh analysis, nodal analysis and "
        "network theorems."
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

    print("Network Theory - Topic 1 resources processed!")
    print("Inserted:", inserted)
    print("Skipped:", skipped)

except Exception as error:
    connection.rollback()
    print("Error:", error)

finally:
    connection.close()
