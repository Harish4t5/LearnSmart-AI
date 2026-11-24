
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "database" / "ideathon2k26.db"

connection = sqlite3.connect(DB_PATH)
cursor = connection.cursor()

subject = "Signals and Systems"
topic = "Convolution"

resources = [
    (
        subject,
        topic,
        "Beginner",
        "Article",
        "Convolution - Study Notes",
        "",
        """CONVOLUTION

1. What is Convolution?

Convolution is a mathematical operation used to determine
the output of a Linear Time-Invariant (LTI) system from
its input signal and impulse response.

Input signal: x(t)
Impulse response: h(t)
Output signal: y(t)

2. Continuous-Time Convolution

The convolution integral is:

y(t) = integral from -infinity to +infinity of
x(tau) h(t - tau) d(tau).

Here:
x(t) = Input signal
h(t) = Impulse response
y(t) = Output signal
tau = Dummy integration variable

3. Discrete-Time Convolution

The convolution sum is:

y[n] = sum from k = -infinity to +infinity of
x[k] h[n-k].

It is used for discrete-time LTI systems.

4. Graphical Method of Convolution

The main steps are:

Step 1: Fold one signal.
Replace h(t) with h(-tau).

Step 2: Shift the folded signal.
Replace h(-tau) with h(t-tau).

Step 3: Multiply the two signals.
Calculate x(tau) h(t-tau).

Step 4: Integrate the product.
Find the area over the complete time axis.

Repeat these steps for different values of t.

5. Properties of Convolution

Commutative Property:
x(t) * h(t) = h(t) * x(t)

Associative Property:
(x * h) * g = x * (h * g)

Distributive Property:
x * (h + g) = x * h + x * g

Identity Property:
x(t) * delta(t) = x(t)

6. Convolution and LTI Systems

For an LTI system, the output is the convolution
of the input with the system's impulse response.

y(t) = x(t) * h(t)

This relationship also applies to discrete-time
LTI systems using the convolution sum.

7. Applications of Convolution

- Digital signal processing.
- Audio and image filtering.
- Communication systems.
- System response analysis.
- Noise reduction.

8. Important Points

- Convolution combines an input with an impulse response.
- It is used to calculate the output of an LTI system.
- Continuous-time convolution uses integration.
- Discrete-time convolution uses summation.
- The impulse response characterizes an LTI system
  under zero-state conditions.

Remember:
Continuous time -> Convolution integral.
Discrete time -> Convolution sum.
LTI output -> Input convolved with impulse response."""
    ),
    (
        subject,
        topic,
        "Intermediate",
        "Documentation",
        "NPTEL Signals and Systems Course",
        "https://nptel.ac.in/courses/108104100",
        "Additional university-level resource for convolution, "
        "impulse response and analysis of LTI systems."
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

    print("Signals and Systems - Topic 6 resources processed!")
    print("Inserted:", inserted)
    print("Skipped:", skipped)

except Exception as error:
    connection.rollback()
    print("Error:", error)

finally:
    connection.close()
