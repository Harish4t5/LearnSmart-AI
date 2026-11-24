
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "database" / "ideathon2k26.db"

connection = sqlite3.connect(DB_PATH)

subject = "Probability and Statistics"
branch_code = "EEE"
semester = 3
topic = "Basics of Probability"

questions = [
    (
        "What is the probability of an impossible event?",
        "0",
        "1",
        "0.5",
        "Infinity",
        "A",
        "An impossible event has probability zero.",
        "Beginner"
    ),
    (
        "What is the probability of a certain event?",
        "0",
        "0.25",
        "1",
        "0.5",
        "C",
        "A certain event always occurs, so its probability is one.",
        "Beginner"
    ),
    (
        "When a fair coin is tossed once, what is the probability of getting a head?",
        "1",
        "1/4",
        "1/2",
        "0",
        "C",
        "There are two equally likely outcomes, and one is a head. Probability = 1/2.",
        "Beginner"
    ),
    (
        "When a fair six-sided die is rolled, how many possible outcomes are there?",
        "2",
        "4",
        "6",
        "8",
        "C",
        "A standard six-sided die has six possible outcomes.",
        "Beginner"
    ),
    (
        "What is the probability of getting an even number when a fair die is rolled?",
        "1/6",
        "1/3",
        "1/2",
        "2/3",
        "C",
        "The even outcomes are 2, 4 and 6. Probability = 3/6 = 1/2.",
        "Beginner"
    ),
    (
        "A bag contains 3 red and 2 blue balls. What is the probability of selecting a red ball?",
        "2/5",
        "3/5",
        "1/5",
        "4/5",
        "B",
        "There are 3 red balls out of 5 total balls. Probability = 3/5.",
        "Intermediate"
    ),
    (
        "Two fair coins are tossed together. What is the probability of getting exactly two heads?",
        "1/4",
        "1/2",
        "3/4",
        "1",
        "A",
        "The possible outcomes are HH, HT, TH and TT. Only HH has two heads, so probability = 1/4.",
        "Intermediate"
    ),
    (
        "If P(A) = 0.35, what is the probability of the complement of A?",
        "0.35",
        "0.65",
        "1.35",
        "0",
        "B",
        "P(A complement) = 1 - P(A) = 1 - 0.35 = 0.65.",
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

    print("EEE Probability and Statistics Topic 1 added successfully!")
    print("Subject:", subject)
    print("Topic:", topic)
    print("New questions added:", inserted)
    print("Existing questions skipped:", skipped)

except Exception as error:
    connection.rollback()
    print("Error:", error)

finally:
    connection.close()
