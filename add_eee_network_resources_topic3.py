
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "database" / "ideathon2k26.db"

connection = sqlite3.connect(DB_PATH)
cursor = connection.cursor()

subject = "Network Theory"
topic = "Network Theorems"

resources = [
    (
        subject,
        topic,
        "Beginner",
        "Article",
        "Electrical Network Theorems - Study Notes",
        "",
        """NETWORK THEOREMS - STUDY NOTES

Network theorems simplify the analysis of complex linear
electrical circuits.

1. Thevenin's Theorem

Statement:
Any linear bilateral two-terminal network can be replaced
by an equivalent voltage source (Vth) in series with
an equivalent resistance (Rth).

Steps:
- Remove the load resistor.
- Calculate the open-circuit voltage across the terminals.
- Deactivate independent sources to calculate equivalent
  resistance: short ideal voltage sources and open ideal
  current sources.
- Connect Vth in series with Rth and reconnect the load.

2. Norton's Theorem

Statement:
A linear bilateral two-terminal network can be replaced
by an equivalent current source (In) in parallel with
an equivalent resistance (Rn).

Steps:
- Remove the load resistor.
- Calculate short-circuit current across the terminals.
- Calculate equivalent resistance using deactivated
  independent sources.
- Connect In in parallel with Rn and reconnect the load.

Relationship:
Rn = Rth
Vth = In × Rth

3. Superposition Theorem

Statement:
In a linear circuit containing multiple independent
sources, the response in any element equals the algebraic
sum of responses produced by each independent source
acting separately.

Rules:
- Keep one independent source active at a time.
- Replace other ideal voltage sources with short circuits.
- Replace other ideal current sources with open circuits.
- Keep dependent sources active.
- Add individual responses algebraically.

4. Maximum Power Transfer Theorem

For a DC resistive network, maximum power is transferred
to the load when:

RL = Rth

where:
RL = Load resistance
Rth = Thevenin equivalent resistance

Maximum power:
Pmax = Vth² / (4 × Rth)

For AC networks, maximum average power transfer occurs
when the load impedance is the complex conjugate of
the Thevenin impedance.

5. Applications

- Simplifying complicated electrical networks.
- Finding load current and voltage.
- Circuit design and analysis.
- Impedance matching.
- Power transfer optimisation.

Remember:
Thevenin -> Voltage source in series with resistance.
Norton -> Current source in parallel with resistance.
Superposition -> One independent source at a time.
Maximum Power Transfer -> Match load to source resistance
for a DC resistive network."""
    ),
    (
        subject,
        topic,
        "Intermediate",
        "Video",
        "Network Analysis - NPTEL IIT Kharagpur",
        "https://nptel.ac.in/courses/108105159",
        "NPTEL course by IIT Kharagpur covering Thevenin's theorem, "
        "Norton's theorem, superposition, maximum power transfer "
        "and other methods of linear network analysis."
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

    print("Network Theory - Topic 3 resources processed!")
    print("Inserted:", inserted)
    print("Skipped:", skipped)

except Exception as error:
    connection.rollback()
    print("Error:", error)

finally:
    connection.close()
