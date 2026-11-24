
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "database" / "ideathon2k26.db"

connection = sqlite3.connect(DB_PATH)

subject = "Probability and Statistics"
branch_code = "EEE"
semester = 3
topic = "Bayes' Theorem"

questions = [
    (
        "Bayes' Theorem is mainly used to calculate:",
        "Conditional probability",
        "Electrical resistance",
        "Average speed",
        "Signal frequency",
        "A",
        "Bayes' Theorem helps calculate conditional probabilities using known probabilities.",
        "Beginner"
    ),
    (
        "Which formula represents Bayes' Theorem for events A and B, where P(B) is greater than zero?",
        "P(A | B) = P(A)P(B)",
        "P(A | B) = P(B | A)P(A) / P(B)",
        "P(A | B) = P(A) + P(B)",
        "P(A | B) = P(B) / P(A)",
        "B",
        "Bayes' Theorem states P(A | B) = P(B | A)P(A) / P(B).",
        "Beginner"
    ),
    (
        "In Bayes' Theorem, P(A) is commonly called:",
        "Posterior probability",
        "Prior probability",
        "Conditional frequency",
        "Joint probability",
        "B",
        "P(A) is the prior probability before observing the evidence.",
        "Beginner"
    ),
    (
        "In Bayes' Theorem, P(A | B) is called:",
        "Prior probability",
        "Posterior probability",
        "Independent probability",
        "Impossible probability",
        "B",
        "P(A | B) is the posterior probability after observing event B.",
        "Beginner"
    ),
    (
        "What is the purpose of the denominator P(B) in Bayes' Theorem?",
        "To normalize the probability using the evidence",
        "To calculate the mean",
        "To find the variance",
        "To remove the conditional probability",
        "A",
        "P(B) represents the probability of the observed evidence and normalizes the result.",
        "Beginner"
    ),
    (
        "If P(A) = 0.4, P(B | A) = 0.5 and P(B) = 0.2, find P(A | B).",
        "0.2",
        "0.5",
        "0.8",
        "1.0",
        "C",
        "P(A | B) = P(B | A)P(A) / P(B) = (0.5 × 0.4) / 0.2 = 1.0. Therefore the correct answer is D.",
        "Intermediate"
    ),
    (
        "A factory has two machines. Machine A produces 60% of items and Machine B produces 40%. Their defective rates are 2% and 5%, respectively. What is the probability that a randomly selected item is defective?",
        "2.0%",
        "3.2%",
        "4.0%",
        "5.0%",
        "B",
        "P(D) = 0.60 × 0.02 + 0.40 × 0.05 = 0.032 = 3.2%.",
        "Intermediate"
    ),
    (
        "Two events A and B have P(A) = 0.3, P(B | A) = 0.6 and P(B) = 0.4. Find P(A | B).",
        "0.25",
        "0.35",
        "0.45",
        "0.60",
        "C",
        "P(A | B) = (0.6 × 0.3) / 0.4 = 0.45.",
        "Intermediate"
    )
]

# Correct the numerical answer in Question 6:
# (0.5 × 0.4) / 0.2 = 1.0, so option D is correct.
questions[5] = (
    questions[5][0],
    questions[5][1],
    questions[5][2],
    questions[5][3],
    questions[5][4],
    "D",
    "P(A | B) = P(B | A)P(A) / P(B) = (0.5 × 0.4) / 0.2 = 1.0.",
    "Intermediate"
)

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

    print("EEE Probability and Statistics Topic 3 added successfully!")
    print("Subject:", subject)
    print("Topic:", topic)
    print("New questions added:", inserted)
    print("Existing questions skipped:", skipped)

except Exception as error:
    connection.rollback()
    print("Error:", error)

finally:
    connection.close()
