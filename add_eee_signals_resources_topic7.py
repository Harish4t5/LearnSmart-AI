
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "database" / "ideathon2k26.db"

connection = sqlite3.connect(DB_PATH)
cursor = connection.cursor()

subject = "Signals and Systems"
topic = "Fourier Series"

resources = [
    (
        subject,
        topic,
        "Beginner",
        "Article",
        "Fourier Series - Study Notes",
        "",
        """FOURIER SERIES

1. What is a Fourier Series?

A Fourier series represents a periodic signal as a sum
of sinusoidal components: sines, cosines and a possible
constant component.

It is widely used to analyze periodic signals.

2. Trigonometric Fourier Series

For a periodic signal with fundamental period T:

x(t) = a0/2 + sum from n=1 to infinity of
[an cos(nω0t) + bn sin(nω0t)]

Here:
T = Fundamental time period
f0 = Fundamental frequency
ω0 = Fundamental angular frequency
an and bn = Fourier coefficients

3. Fundamental Frequency

f0 = 1/T

ω0 = 2π/T = 2πf0

4. Fourier Coefficients

For one period, taken over any interval of length T:

a0 = (2/T) integral x(t) dt

an = (2/T) integral x(t) cos(nω0t) dt

bn = (2/T) integral x(t) sin(nω0t) dt

The integrals are evaluated over one complete period.

5. Harmonics

The fundamental frequency is the first harmonic.

The integer multiples of the fundamental frequency
are called harmonics.

Second harmonic = 2f0
Third harmonic = 3f0
Fourth harmonic = 4f0

6. Even and Odd Signals

For an even periodic signal:
bn = 0 for all n.

For an odd periodic signal:
a0 = 0 and an = 0 for all n.

These properties can simplify Fourier coefficient
calculations.

7. Exponential Fourier Series

A periodic signal can also be represented as:

x(t) = sum from n=-infinity to +infinity of
Cn exp(jnω0t)

Here Cn are complex Fourier coefficients.

8. Applications

- Harmonic analysis in power systems.
- Communication engineering.
- Signal reconstruction.
- Audio processing.
- Electrical circuit analysis.

Remember:
Fourier Series -> Periodic signals.
Fundamental frequency -> 1/T.
Harmonics -> Integer multiples of fundamental frequency.
Even signal -> Sine coefficients vanish.
Odd signal -> Cosine and constant coefficients vanish."""
    ),
    (
        subject,
        topic,
        "Intermediate",
        "Documentation",
        "NPTEL Signals and Systems Course",
        "https://nptel.ac.in/courses/108104100",
        "Additional university-level resource for Fourier series, "
        "periodic signal representation and frequency-domain analysis."
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

    print("Signals and Systems - Topic 7 resources processed!")
    print("Inserted:", inserted)
    print("Skipped:", skipped)

except Exception as error:
    connection.rollback()
    print("Error:", error)

finally:
    connection.close()
