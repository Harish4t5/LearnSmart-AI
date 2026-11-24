
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "database" / "ideathon2k26.db"

connection = sqlite3.connect(DB_PATH)
cursor = connection.cursor()

subject = "Power Systems I"
topic = "Electrical Power Generation"

resources = [
    (
        subject,
        topic,
        "Beginner",
        "Article",
        "Electrical Power Generation - Study Notes",
        "",
        """Electrical power generation is the process of converting
different forms of energy into electrical energy.

Major methods of generation:

1. Thermal Power Plant:
Uses heat from burning coal or other fuels to produce steam.
Steam rotates a turbine connected to an alternator.

2. Hydroelectric Power Plant:
Uses the potential energy of stored water to rotate a turbine.
The turbine drives an electrical generator.

3. Nuclear Power Plant:
Uses heat released by nuclear fission to produce steam
and generate electricity through a turbine-generator.

4. Solar Power Plant:
Solar photovoltaic cells convert sunlight directly into
electrical energy.

5. Wind Power Plant:
Wind rotates turbine blades connected to a generator.

Important terms:
- Prime mover: Drives the generator.
- Alternator: Converts mechanical energy into AC electrical energy.
- Renewable sources: Solar, wind and hydropower.
- Non-renewable sources: Coal, petroleum and natural gas.

Remember:
Energy source -> Prime mover (where applicable) ->
Generator -> Electrical energy."""
    ),
    (
        subject,
        topic,
        "Intermediate",
        "Video",
        "Power System Generation, Transmission and Distribution - NPTEL",
        "https://nptel.ac.in/courses/108102047",
        "NPTEL course by Prof. D. P. Kothari, IIT Delhi. "
        "Includes conventional power generation, hydroelectric "
        "generation, non-conventional energy sources, renewable "
        "energy and energy storage."
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
    print("Power Systems I - Topic 2 resources processed!")
    print("Inserted:", inserted)
    print("Skipped:", skipped)

except Exception as error:
    connection.rollback()
    print("Error:", error)

finally:
    connection.close()
