
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "database" / "ideathon2k26.db"

connection = sqlite3.connect(DB_PATH)

subject = "Probability and Statistics"
branch_code = "EEE"
semester = 3
topic = "Conditional Probability"

questions = [
    (
        "What does conditional probability mean?",
        "Probability of an event when another event is known to have occurred",
        "Probability of an impossible event",
        "Probability of two independent events only",
        "Probability of a certain event",
        "A",
        "Conditional probability measures the probability of an event under the condition that another event has occurred.",
        "Beginner"
    ),
    (
        "Which symbol is commonly used to represent the conditional probability of A given B?",
        "P(A + B)",
        "P(A | B)",
        "P(A - B)",
        "P(A × B)",
        "B",
        "P(A | B) represents the probability of event A occurring given that event B has occurred.",
        "Beginner"
    ),
    (
        "What is the formula for P(A | B), provided P(B) is greater than zero?",
        "P(A) / P(B)",
        "P(A ∩ B) / P(B)",
        "P(A ∪ B) / P(A)",
        "P(B) / P(A)",
        "B",
        "Conditional probability is P(A | B) = P(A ∩ B) / P(B).",
        "Beginner"
    ),
    (
        "If two events A and B are independent, then P(A | B) is equal to:",
        "P(B)",
        "P(A)",
        "Zero",
        "One",
        "B",
        "For independent events, the occurrence of B does not change the probability of A.",
        "Beginner"
    ),
    (
        "If P(A ∩ B) = 0, the events A and B are:",
        "Independent always",
        "Mutually exclusive",
        "Certain events",
        "Identical events",
        "B",
        "If the intersection has zero probability, the events are mutually exclusive (disjoint).",
        "Beginner"
    ),
    (
        "If P(A ∩ B) = 0.2 and P(B) = 0.5, find P(A | B).",
        "0.2",
        "0.4",
        "0.5",
        "0.7",
        "B",
        "P(A | B) = P(A ∩ B) / P(B) = 0.2 / 0.5 = 0.4.",
        "Intermediate"
    ),
    (
        "A card is selected from a standard deck. Given that the selected card is a face card, what is the probability that it is a king?",
        "1/3",
        "1/4",
        "1/2",
        "1/13",
        "B",
        "There are 12 face cards and 4 kings. The required probability is 4/12 = 1/3.",
        "Intermediate"
    ),
    (
        "If P(A) = 0.6, P(B) = 0.5 and A and B are independent, find P(A ∩ B).",
        "0.1",
        "0.3",
        "0.5",
        "1.1",
        "B",
        "For independent events, P(A ∩ B) = P(A) × P(B) = 0.6 × 0.5 = 0.3.",
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

    print("EEE Probability and Statistics Topic 2 added successfully!")
    print("Subject:", subject)
    print("Topic:", topic)
    print("New questions added:", inserted)
    print("Existing questions skipped:", skipped)

except Exception as error:
    connection.rollback()
    print("Error:", error)

finally:
    connection.close()
