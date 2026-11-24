
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "database" / "ideathon2k26.db"

connection = sqlite3.connect(DB_PATH)
cursor = connection.cursor()

subject = "Signals and Systems"
topic = "Fourier Transform"

resources = [
    (
        subject,
        topic,
        "Beginner",
        "Article",
        "Fourier Transform - Study Notes",
        "",
        """FOURIER TRANSFORM

1. What is Fourier Transform?

Fourier Transform is a mathematical tool that converts
a time-domain signal into its frequency-domain
representation.

It helps us understand the frequency components
present in a signal.

2. Continuous-Time Fourier Transform (CTFT)

For a continuous-time signal x(t):

X(ω) = integral from -infinity to +infinity of
x(t) exp(-jωt) dt

Here:
x(t) = Time-domain signal
X(ω) = Frequency-domain representation
ω = Angular frequency
j = Imaginary unit

3. Inverse Fourier Transform

The inverse Fourier transform converts a frequency-domain
representation back into the time domain.

x(t) = (1/2π) integral from -infinity to +infinity of
X(ω) exp(jωt) dω

4. Fourier Transform of Discrete-Time Signals

The Discrete-Time Fourier Transform (DTFT) is:

X(e^jω) = sum from n=-infinity to +infinity of
x[n] exp(-jωn)

It represents a discrete-time signal in the frequency
domain and is periodic in frequency with period 2π.

5. Important Properties

Linearity:
The transform of a linear combination is the same
linear combination of the individual transforms.

Time Shifting:
A shift in time introduces a frequency-dependent
phase factor.

Frequency Shifting:
Multiplication by a complex exponential in time
shifts the frequency spectrum.

Time Scaling:
Changes the frequency distribution of a signal.

Convolution:
Convolution in the time domain corresponds to
multiplication in the frequency domain.

6. Fourier Series vs Fourier Transform

Fourier Series:
- Used for periodic signals.
- Represents signals using discrete harmonics.

Fourier Transform:
- Used for aperiodic signals and more general signal analysis.
- Represents frequency content over a continuous frequency axis
  for continuous-time signals.

7. Applications

- Digital signal processing.
- Communication systems.
- Audio and image processing.
- Spectrum analysis.
- Filtering and noise removal.
- Biomedical signal analysis.

8. Important Points

- Fourier Transform converts time-domain information
  into frequency-domain information.
- The inverse transform reconstructs the original signal
  under the required mathematical conditions.
- The magnitude spectrum describes frequency strength.
- The phase spectrum describes frequency-dependent phase.

Remember:
Time domain -> Fourier Transform -> Frequency domain.
Frequency domain -> Inverse Fourier Transform -> Time domain."""
    ),
    (
        subject,
        topic,
        "Intermediate",
        "Documentation",
        "NPTEL Signals and Systems Course",
        "https://nptel.ac.in/courses/108104100",
        "Additional university-level resource for Fourier transforms, "
        "frequency-domain analysis and signal representation."
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

    print("Signals and Systems - Topic 8 resources processed!")
    print("Inserted:", inserted)
    print("Skipped:", skipped)

except Exception as error:
    connection.rollback()
    print("Error:", error)

finally:
    connection.close()

