
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "database" / "ideathon2k26.db"

connection = sqlite3.connect(DB_PATH)
cursor = connection.cursor()

subject = "Network Theory"
topic = "Resonance and Coupled Circuits"

resources = [
    (
        subject,
        topic,
        "Beginner",
        "Article",
        "Resonance and Coupled Circuits - Study Notes",
        "",
        """RESONANCE AND COUPLED CIRCUITS - STUDY NOTES

1. Electrical Resonance

Resonance occurs in an AC circuit when inductive
reactance equals capacitive reactance.

At resonance:
XL = XC

2. Series RLC Resonance

For a series RLC circuit:

Resonant frequency:
f0 = 1 / (2π√LC)

At resonance:
- Inductive and capacitive reactances cancel.
- Impedance becomes equal to resistance (Z = R).
- Circuit current becomes maximum.
- Power factor becomes unity.
- Voltage and current are in phase.

3. Parallel Resonance

In an ideal parallel RLC circuit, resonance occurs
when the inductive and capacitive susceptances cancel.

At resonance:
- Input impedance is maximum.
- Supply current is minimum.
- Power factor is unity for the ideal circuit.

4. Quality Factor (Q)

Quality factor indicates the sharpness of resonance.

For a series RLC circuit:
Q = (1/R)√(L/C)

A higher Q indicates a sharper resonance.

5. Bandwidth

Bandwidth is the difference between the upper and
lower half-power frequencies.

BW = f2 - f1

For a series RLC circuit:
Q = f0 / BW

6. Coupled Circuits

Two coils are magnetically coupled when a change
in current in one coil produces a changing magnetic
flux that links the other coil.

Mutual inductance:
M = k√(L1 × L2)

Where:
M = Mutual inductance in henrys
L1, L2 = Self-inductances in henrys
k = Coefficient of coupling

The coefficient of coupling satisfies:
0 ≤ k ≤ 1

7. Dot Convention

Dots indicate the relative polarity of mutually
induced voltages in magnetically coupled coils.

The dot convention helps determine whether
mutual voltage terms are added or subtracted.

8. Applications

- Radio and communication tuning circuits.
- Frequency-selective circuits.
- Inductive power transfer.
- Transformers and coupled inductors.
- Resonant converters.

Remember:
Series resonance -> Minimum impedance and maximum current.
Ideal parallel resonance -> Maximum impedance and minimum supply current.
Mutual inductance -> M = k√(L1 × L2)."""
    ),
    (
        subject,
        topic,
        "Intermediate",
        "Video",
        "Network Analysis - NPTEL IIT Kharagpur",
        "https://nptel.ac.in/courses/108105159",
        "NPTEL Network Analysis course by IIT Kharagpur. "
        "Use the course lectures to study AC network behaviour, "
        "resonance, coupled circuits and mutual inductance."
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

    print("Network Theory - Topic 6 resources processed!")
    print("Inserted:", inserted)
    print("Skipped:", skipped)

except Exception as error:
    connection.rollback()
    print("Error:", error)

finally:
    connection.close()
