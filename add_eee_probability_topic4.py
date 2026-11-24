
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "database" / "ideathon2k26.db"

connection = sqlite3.connect(DB_PATH)

subject = "Probability and Statistics"
branch_code = "EEE"
semester = 3
topic = "Random Variables"

questions = [
    (
        "What is a random variable?",
        "A variable that assigns a numerical value to each outcome of a random experiment",
        "A variable that always has a fixed value",
        "A variable used only in electrical circuits",
        "A variable that cannot change",
        "A",
        "A random variable maps outcomes of a random experiment to numerical values.",
        "Beginner"
    ),
    (
        "Which of the following is an example of a discrete random variable?",
        "Height of a student",
        "Weight of a person",
        "Number of heads in three coin tosses",
        "Temperature of a room",
        "C",
        "The number of heads is countable and takes distinct values, so it is discrete.",
        "Beginner"
    ),
    (
        "Which of the following is an example of a continuous random variable?",
        "Number of students in a class",
        "Number of defective bulbs",
        "Number of cars in a parking lot",
        "Time taken to complete an exam",
        "D",
        "Time can take any value within a range and is treated as a continuous random variable.",
        "Beginner"
    ),
    (
        "What is the range of a cumulative distribution function F(x)?",
        "Only negative values",
        "Between 0 and 1, inclusive",
        "Always greater than 1",
        "Between -1 and 1",
        "B",
        "A cumulative distribution function gives probabilities and therefore ranges from 0 to 1.",
        "Beginner"
    ),
    (
        "For a discrete random variable, what is the sum of all probabilities of its possible values?",
        "0",
        "0.5",
        "1",
        "Infinity",
        "C",
        "The probabilities of all possible outcomes of a discrete random variable sum to one.",
        "Beginner"
    ),
    (
        "A fair die is rolled once. Let X be the number obtained. What is P(X = 4)?",
        "1/2",
        "1/3",
        "1/6",
        "1",
        "C",
        "Each of the six outcomes is equally likely, so P(X = 4) = 1/6.",
        "Intermediate"
    ),
    (
        "A random variable X has P(X = 0) = 0.3 and P(X = 1) = 0.7. What is its expected value E(X)?",
        "0.3",
        "0.5",
        "0.7",
        "1.0",
        "C",
        "E(X) = 0 × 0.3 + 1 × 0.7 = 0.7.",
        "Intermediate"
    ),
    (
        "If X is a continuous random variable with probability density function f(x), the total area under its density curve is:",
        "0",
        "0.5",
        "1",
        "2",
        "C",
        "The total integral of a valid probability density function over its entire range equals one.",
        "Intermediate"
    )
]

inserted = 0
skipped = 0

try:
    for q in questions:
        existing = connection.execute("""
            SELECT id FROM quiz_questions
            WHERE subject = ?
              AND branch_code = ?
              AND semester = ?
              AND topic = ?
              AND question = ?
        """, (subject, branch_code, semester, topic, q[0])).fetchone()

        if existing:
            skipped += 1
            continue

        connection.execute("""
            INSERT INTO quiz_questions (
                subject, topic, question,
                option_a, option_b, option_c, option_d,
                correct_answer, explanation, difficulty,
                branch_code, semester
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            subject, topic, q[0],
            q[1], q[2], q[3], q[4],
            q[5], q[6], q[7],
            branch_code, semester
        ))

        inserted += 1

    connection.commit()

    print("EEE Probability and Statistics Topic 4 added successfully!")
    print("Subject:", subject)
    print("Topic:", topic)
    print("New questions added:", inserted)
    print("Existing questions skipped:", skipped)

except Exception as error:
    connection.rollback()
    print("Error:", error)

finally:
    connection.close()
