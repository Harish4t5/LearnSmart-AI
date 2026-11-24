
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "database" / "ideathon2k26.db"

connection = sqlite3.connect(DB_PATH)
cursor = connection.cursor()

subject = "Signals and Systems"
topic = "Basic Operations on Signals"

resources = [
    (
        subject,
        topic,
        "Beginner",
        "Article",
        "Basic Operations on Signals - Study Notes",
        "",
        """BASIC OPERATIONS ON SIGNALS

Signal operations modify the amplitude or time
characteristics of a signal.

1. Amplitude Scaling

Multiplying a signal by a constant changes its amplitude.

y(t) = A x(t)

If A > 1, amplitude increases.
If 0 < A < 1, amplitude decreases.
If A < 0, amplitude is also inverted.

2. Addition of Signals

Two signals can be added point by point.

y(t) = x1(t) + x2(t)

This operation is called signal addition.

3. Multiplication of Signals

Two signals can be multiplied point by point.

y(t) = x1(t) x2(t)

4. Time Shifting

Time shifting moves a signal along the time axis.

Delay:
y(t) = x(t - t0)

The signal shifts to the right by t0.

Advance:
y(t) = x(t + t0)

The signal shifts to the left by t0.

5. Time Reversal

Time reversal reflects a signal around the vertical axis.

y(t) = x(-t)

For example, a signal originally defined at positive
time values is reflected to corresponding negative
time values.

6. Time Scaling

Time scaling compresses or expands a signal.

y(t) = x(at)

If |a| > 1:
The signal is compressed in time.

If 0 < |a| < 1:
The signal is expanded in time.

If a < 0:
Time reversal also occurs.

7. Operations on Discrete-Time Signals

Discrete-time signals use integer indices.

Amplitude scaling:
y[n] = A x[n]

Time shifting:
y[n] = x[n - n0]

Time reversal:
y[n] = x[-n]

8. Important Points

- Amplitude scaling changes signal magnitude.
- Time shifting changes signal position.
- Time reversal reflects the signal.
- Time scaling changes its time duration.
- Addition and multiplication combine signal values
  at corresponding time instants.

Remember:
x(t - t0) -> Delay.
x(t + t0) -> Advance.
x(-t) -> Time reversal.
x(at), |a| > 1 -> Time compression.
x(at), 0 < |a| < 1 -> Time expansion."""
    ),
    (
        subject,
        topic,
        "Intermediate",
        "Documentation",
        "Signals and Systems Learning Resource",
        "https://nptel.ac.in/courses/108104100",
        "Additional university-level resource for mathematical "
        "signal representation and time-domain operations."
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

    print("Signals and Systems - Topic 3 resources processed!")
    print("Inserted:", inserted)
    print("Skipped:", skipped)

except Exception as error:
    connection.rollback()
    print("Error:", error)

finally:
    connection.close()
