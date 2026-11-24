
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "database" / "ideathon2k26.db"

connection = sqlite3.connect(DB_PATH)
cursor = connection.cursor()

subject = "Network Theory"
topic = "Transient Analysis"

resources = [
    (
        subject,
        topic,
        "Beginner",
        "Article",
        "Transient Analysis - Study Notes",
        "",
        """TRANSIENT ANALYSIS - STUDY NOTES

1. Introduction

Transient analysis studies how voltage and current change
with time immediately after a switching operation or
a sudden change in circuit conditions.

The temporary response before reaching steady state
is called the transient response.

2. RC Circuit

An RC circuit contains a resistor and capacitor.

Time constant:
τ = RC

Where:
R = Resistance in ohms
C = Capacitance in farads
τ = Time constant in seconds

Capacitor charging:
Vc(t) = V(1 - e^(-t/RC))

Capacitor discharging:
Vc(t) = V0 e^(-t/RC)

After one time constant, a charging capacitor reaches
approximately 63.2% of its final voltage.

3. RL Circuit

An RL circuit contains a resistor and inductor.

Time constant:
τ = L/R

Where:
L = Inductance in henrys
R = Resistance in ohms

Inductor current growth:
i(t) = (V/R)(1 - e^(-tR/L))

The inductor opposes sudden changes in current.

4. RLC Circuit

An RLC circuit contains a resistor, inductor and capacitor.

Its transient response depends on resistance,
inductance and capacitance.

Three types of response:

- Overdamped: Two distinct real roots; no oscillation.
- Critically damped: Fastest non-oscillatory response.
- Underdamped: Oscillatory response with decreasing amplitude.

5. Important Points

- Capacitor voltage cannot change instantaneously.
- Inductor current cannot change instantaneously.
- At DC steady state, an ideal capacitor behaves as
  an open circuit.
- At DC steady state, an ideal inductor behaves as
  a short circuit.

6. Applications

- Switching circuit analysis.
- Power supply design.
- Electronic circuit response.
- Control and signal systems.

Remember:
RC time constant = RC
RL time constant = L/R
Transient response describes temporary circuit behaviour."""
    ),
    (
        subject,
        topic,
        "Intermediate",
        "Video",
        "Network Analysis - NPTEL IIT Kharagpur",
        "https://nptel.ac.in/courses/108105159",
        "NPTEL Network Analysis course covering first-order and "
        "second-order circuit responses, RC and RL transients, "
        "and RLC circuit behaviour."
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

    print("Network Theory - Topic 4 resources processed!")
    print("Inserted:", inserted)
    print("Skipped:", skipped)

except Exception as error:
    connection.rollback()
    print("Error:", error)

finally:
    connection.close()
