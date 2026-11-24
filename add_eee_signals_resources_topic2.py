
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "database" / "ideathon2k26.db"

connection = sqlite3.connect(DB_PATH)
cursor = connection.cursor()

subject = "Signals and Systems"
topic = "Classification of Signals"

resources = [
    (
        subject,
        topic,
        "Beginner",
        "Article",
        "Classification of Signals - Study Notes",
        "",
        """CLASSIFICATION OF SIGNALS

Signals can be classified according to their properties.

1. Continuous-Time and Discrete-Time Signals

Continuous-Time Signal:
Defined for every instant of time t.
Represented by x(t).

Discrete-Time Signal:
Defined only at discrete time instants.
Represented by x[n].

2. Analog and Digital Signals

Analog Signal:
Has continuous amplitude values.

Digital Signal:
Has discrete amplitude levels and is represented
using discrete samples.

3. Periodic and Aperiodic Signals

Periodic Signal:
Repeats after a fixed interval.

Continuous-time condition:
x(t) = x(t + T)

Discrete-time condition:
x[n] = x[n + N]

Aperiodic Signal:
Does not repeat at a fixed interval.

4. Even and Odd Signals

Even Signal:
A signal is even if:
x(-t) = x(t)

Example:
x(t) = cos(t)

Odd Signal:
A signal is odd if:
x(-t) = -x(t)

Example:
x(t) = sin(t)

Any signal can be expressed as the sum of its even
and odd components.

5. Energy and Power Signals

Energy Signal:
Has finite total energy and zero average power.

Power Signal:
Has finite, non-zero average power and infinite total energy.

Energy of a continuous-time signal:
E = integral of |x(t)|² over all time.

Average power:
P = limit as T approaches infinity of
(1 / 2T) integral from -T to T of |x(t)|² dt.

6. Deterministic and Random Signals

Deterministic Signal:
Can be described exactly using a mathematical expression.

Random Signal:
Cannot be predicted exactly at every instant and is
described using statistical properties.

7. Causal and Non-Causal Signals

Causal Signal:
A continuous-time signal is causal if it is zero for t < 0.

Non-Causal Signal:
Has non-zero values before t = 0.

8. Real and Complex Signals

Real Signal:
Contains only real-valued samples.

Complex Signal:
Contains real and imaginary components.

Example:
x(t) = 3 + j4

Remember:
Even -> x(-t) = x(t).
Odd -> x(-t) = -x(t).
Periodic -> Repeats.
Aperiodic -> Does not repeat.
Energy and power classifications depend on their
total energy and long-term average power."""
    ),
    (
        subject,
        topic,
        "Intermediate",
        "Documentation",
        "Signals and Systems Learning Resource",
        "https://nptel.ac.in/courses/108104100",
        "Additional university-level learning resource for "
        "signal properties, signal representation and "
        "mathematical classification."
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

    print("Signals and Systems - Topic 2 resources processed!")
    print("Inserted:", inserted)
    print("Skipped:", skipped)

except Exception as error:
    connection.rollback()
    print("Error:", error)

finally:
    connection.close()
