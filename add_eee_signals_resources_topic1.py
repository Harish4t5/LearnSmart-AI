
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "database" / "ideathon2k26.db"

connection = sqlite3.connect(DB_PATH)
cursor = connection.cursor()

subject = "Signals and Systems"
topic = "Introduction to Signals and Systems"

resources = [
    (
        subject,
        topic,
        "Beginner",
        "Article",
        "Introduction to Signals and Systems - Study Notes",
        "",
        """INTRODUCTION TO SIGNALS AND SYSTEMS

1. What is a Signal?

A signal is a function that carries information about
a physical phenomenon or a system.

Examples:
- Speech signal
- Temperature variation
- Electrical voltage
- ECG signal

Mathematically, a continuous-time signal is represented
as x(t), while a discrete-time signal is represented as x[n].

2. What is a System?

A system is a process or device that operates on an input
signal and produces an output signal.

Representation:

Input Signal -> SYSTEM -> Output Signal

Mathematically:
y(t) = T{x(t)}

Here:
x(t) = Input signal
y(t) = Output signal
T = System operation

3. Types of Signals

Continuous-Time Signal:
Defined for every value of continuous time t.

Discrete-Time Signal:
Defined only at discrete time instants, represented by n.

Analog Signal:
A continuous-valued signal that varies continuously
with time.

Digital Signal:
A signal represented using discrete-time samples
and quantized amplitude levels.

4. Basic Signal Parameters

Amplitude:
The magnitude or strength of a signal.

Time Period (T):
Time required to complete one cycle of a periodic signal.

Frequency (f):
Number of cycles completed per second.

Relationship:
f = 1/T

Angular Frequency:
ω = 2πf

5. Periodic and Aperiodic Signals

Periodic Signal:
A signal that repeats after a fixed time period.

For continuous time:
x(t) = x(t + T)

For discrete time:
x[n] = x[n + N]

Aperiodic Signal:
A signal that does not repeat at regular intervals.

6. Common Elementary Signals

Unit Step Signal:
Turns on at a specified time.

Unit Impulse Signal:
An idealized impulse used in signal analysis.

Ramp Signal:
Increases linearly with time after its starting point.

Exponential Signal:
Has an exponential variation with time.

Sinusoidal Signal:
A signal represented by a sine or cosine function.

7. Applications

- Communication systems
- Audio and speech processing
- Control systems
- Biomedical signal processing
- Radar and navigation
- Electrical power systems

Remember:
Signal -> Carries information.
System -> Processes a signal.
Continuous time -> x(t).
Discrete time -> x[n].
Frequency -> Cycles per second."""
    ),
    (
        subject,
        topic,
        "Intermediate",
        "Documentation",
        "NPTEL Signals and Systems Course",
        "https://nptel.ac.in/courses/108104100",
        "Additional university-level learning resource for "
        "signals and systems concepts, mathematical analysis "
        "and applications."
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

    print("Signals and Systems - Topic 1 resources processed!")
    print("Inserted:", inserted)
    print("Skipped:", skipped)

except Exception as error:
    connection.rollback()
    print("Error:", error)

finally:
    connection.close()
