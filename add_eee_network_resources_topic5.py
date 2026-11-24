
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "database" / "ideathon2k26.db"

connection = sqlite3.connect(DB_PATH)
cursor = connection.cursor()

subject = "Network Theory"
topic = "AC Circuit Analysis"

resources = [
    (
        subject,
        topic,
        "Beginner",
        "Article",
        "AC Circuit Analysis - Study Notes",
        "",
        """AC CIRCUIT ANALYSIS - STUDY NOTES

1. Alternating Current (AC)

AC is an electric current whose magnitude and direction
change periodically with time.

Sinusoidal voltage:
v(t) = Vm sin(ωt + φ)

Where:
Vm = Maximum voltage
ω = Angular frequency (rad/s)
φ = Phase angle
t = Time (s)

Angular frequency:
ω = 2πf

2. RMS Value

RMS means Root Mean Square. It represents the equivalent
DC value that produces the same heating effect in a resistor.

For a sinusoidal voltage:
Vrms = Vm / √2

For a sinusoidal current:
Irms = Im / √2

3. Average Value

The average value of a complete sinusoidal cycle is zero.

The average value over a positive half-cycle is:
Vavg = 2Vm / π

4. Phasor Representation

A phasor represents a sinusoidal quantity using its
magnitude and phase angle.

Phasors simplify AC circuit calculations involving
voltage, current and impedance.

5. Reactance and Impedance

Inductive reactance:
XL = 2πfL

Capacitive reactance:
XC = 1 / (2πfC)

Impedance:
Z = R + jX

For a series RLC circuit:
Z = R + j(XL - XC)

Magnitude:
|Z| = √[R² + (XL - XC)²]

6. AC Power

Active power:
P = VI cosφ (watts)

Reactive power:
Q = VI sinφ (VAR)

Apparent power:
S = VI (VA)

Power factor:
Power factor = cosφ = P/S

For a purely resistive circuit, power factor is 1.

For an inductive circuit, current lags voltage.
For a capacitive circuit, current leads voltage.

Remember:
AC analysis uses RMS values, phasors, impedance
and phase relationships."""
    ),
    (
        subject,
        topic,
        "Intermediate",
        "Video",
        "Network Analysis - NPTEL IIT Kharagpur",
        "https://nptel.ac.in/courses/108105159",
        "NPTEL course covering sinusoidal steady-state analysis, "
        "phasor representation, impedance, AC circuit calculations, "
        "resonance and electrical network behaviour."
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

    print("Network Theory - Topic 5 resources processed!")
    print("Inserted:", inserted)
    print("Skipped:", skipped)

except Exception as error:
    connection.rollback()
    print("Error:", error)

finally:
    connection.close()
