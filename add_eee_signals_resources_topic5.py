
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "database" / "ideathon2k26.db"

connection = sqlite3.connect(DB_PATH)
cursor = connection.cursor()

subject = "Signals and Systems"
topic = "Linear Time-Invariant (LTI) Systems"

resources = [
    (
        subject,
        topic,
        "Beginner",
        "Article",
        "Linear Time-Invariant Systems - Study Notes",
        "",
        """LINEAR TIME-INVARIANT (LTI) SYSTEMS

1. What is a Linear System?

A system is linear if it satisfies two properties:

Additivity:
If input x1 produces output y1 and input x2 produces
output y2, then input x1 + x2 produces output y1 + y2.

Homogeneity:
If input x produces output y, then input A*x produces
output A*y for any constant A.

Together, these properties form the superposition principle.

2. What is a Time-Invariant System?

A system is time-invariant if shifting the input by a
time interval produces an identical shift in the output.

If:
x(t) -> y(t)

Then:
x(t - t0) -> y(t - t0)

3. LTI System

An LTI system satisfies both:
- Linearity
- Time invariance

These systems are important because their output can
be determined using convolution.

4. Impulse Response

The impulse response is the output of a system when
the input is a unit impulse.

Continuous time:
h(t)

Discrete time:
h[n]

The impulse response completely characterizes an
LTI system under the usual zero-state assumptions.

5. Convolution

Convolution determines the output of an LTI system
from its input and impulse response.

Continuous-time convolution:

y(t) = integral of x(tau) h(t - tau) over all tau.

Discrete-time convolution:

y[n] = sum of x[k] h[n-k] over all integer k.

6. Important Properties of Convolution

Commutative:
x * h = h * x

Associative:
(x * h) * g = x * (h * g)

Distributive:
x * (h + g) = x * h + x * g

7. Causality of LTI Systems

A continuous-time LTI system is causal if:
h(t) = 0 for t < 0.

A discrete-time LTI system is causal if:
h[n] = 0 for n < 0.

8. Stability of LTI Systems

A continuous-time LTI system is BIBO stable if
the integral of |h(t)| over all time is finite.

A discrete-time LTI system is BIBO stable if
the sum of |h[n]| over all integers is finite.

9. Applications

- Communication systems.
- Digital signal processing.
- Audio filtering.
- Image processing.
- Control systems.

Remember:
LTI = Linear + Time Invariant.
Impulse response = h(t) or h[n].
Convolution determines the output of an LTI system."""
    ),
    (
        subject,
        topic,
        "Intermediate",
        "Documentation",
        "NPTEL Signals and Systems Course",
        "https://nptel.ac.in/courses/108104100",
        "Additional university-level resource for linear systems, "
        "impulse response, convolution, causality and stability."
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

    print("Signals and Systems - Topic 5 resources processed!")
    print("Inserted:", inserted)
    print("Skipped:", skipped)

except Exception as error:
    connection.rollback()
    print("Error:", error)

finally:
    connection.close()
