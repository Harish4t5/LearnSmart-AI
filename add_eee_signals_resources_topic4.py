
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "database" / "ideathon2k26.db"

connection = sqlite3.connect(DB_PATH)
cursor = connection.cursor()

subject = "Signals and Systems"
topic = "Continuous-Time and Discrete-Time Systems"

resources = [
    (
        subject,
        topic,
        "Beginner",
        "Article",
        "Continuous-Time and Discrete-Time Systems - Study Notes",
        "",
        """CONTINUOUS-TIME AND DISCRETE-TIME SYSTEMS

1. What is a System?

A system processes an input signal and produces an output.

Mathematically:
y(t) = T{x(t)}

For discrete-time systems:
y[n] = T{x[n]}

2. Continuous-Time System

A continuous-time system operates on continuous-time
signals represented by x(t).

Example:
y(t) = 2x(t)

Here, the output is twice the input at every instant.

3. Discrete-Time System

A discrete-time system operates on discrete-time
signals represented by x[n].

Example:
y[n] = x[n] + x[n-1]

The output depends on the present and previous input samples.

4. Memoryless and Dynamic Systems

Memoryless System:
The output at a given instant depends only on the input
at that same instant.

Example:
y(t) = 3x(t)

Dynamic System:
The output depends on input values at other time instants
or on stored internal states.

Example:
y[n] = x[n] + x[n-1]

5. Causal and Non-Causal Systems

Causal System:
The output at a given time depends only on present
and past input values.

Non-Causal System:
The output depends on future input values.

Example:
y[n] = x[n+1] is non-causal.

6. Stable and Unstable Systems

BIBO Stable System:
A system is BIBO stable if every bounded input produces
a bounded output.

Unstable System:
At least one bounded input can produce an unbounded output.

7. Invertible and Non-Invertible Systems

Invertible System:
Different inputs can be uniquely recovered from the output.

Non-Invertible System:
The input cannot be uniquely recovered from the output.

8. Static and Dynamic Examples

Static:
y(t) = 5x(t)

Dynamic:
y(t) = x(t) + x(t-1)

9. Important Differences

Continuous-Time:
- Input is represented by x(t).
- Defined over continuous time.

Discrete-Time:
- Input is represented by x[n].
- Defined at discrete time indices.

Remember:
Memoryless -> Depends only on present input.
Causal -> No dependence on future input.
BIBO stable -> Bounded input gives bounded output.
Dynamic -> Has memory."""
    ),
    (
        subject,
        topic,
        "Intermediate",
        "Documentation",
        "NPTEL Signals and Systems Course",
        "https://nptel.ac.in/courses/108104100",
        "Additional university-level resource for understanding "
        "continuous-time and discrete-time systems and their "
        "mathematical properties."
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

    print("Signals and Systems - Topic 4 resources processed!")
    print("Inserted:", inserted)
    print("Skipped:", skipped)

except Exception as error:
    connection.rollback()
    print("Error:", error)

finally:
    connection.close()
