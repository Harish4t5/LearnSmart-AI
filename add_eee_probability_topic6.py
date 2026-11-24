
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "database" / "ideathon2k26.db"

connection = sqlite3.connect(DB_PATH)

subject = "Probability and Statistics"
branch_code = "EEE"
semester = 3
topic = "Mathematical Expectation and Variance"

questions = [
    (
        "What does the mathematical expectation of a random variable represent?",
        "Its expected or average value",
        "Its maximum value",
        "Its minimum value",
        "Its range only",
        "A",
        "Mathematical expectation represents the probability-weighted average value of a random variable.",
        "Beginner"
    ),
    (
        "What is the formula for the expectation of a discrete random variable X?",
        "E(X) = sum of x times P(X=x)",
        "E(X) = sum of P(X=x) only",
        "E(X) = x squared",
        "E(X) = 1/P(X)",
        "A",
        "For a discrete random variable, E(X) = Σ x P(X=x).",
        "Beginner"
    ),
    (
        "What does variance measure?",
        "The spread of values around the mean",
        "Only the highest value",
        "The total number of observations",
        "The probability of an impossible event",
        "A",
        "Variance measures how widely the values of a random variable are spread around its mean.",
        "Beginner"
    ),
    (
        "What is the relationship between variance and standard deviation?",
        "Variance is the square of standard deviation",
        "Variance is the square root of standard deviation",
        "They are always equal",
        "Variance is always zero",
        "A",
        "Standard deviation is the square root of variance, so variance is its square.",
        "Beginner"
    ),
    (
        "What is the variance of a constant random variable?",
        "1",
        "0",
        "Infinity",
        "Cannot be determined",
        "B",
        "A constant random variable has no spread, so its variance is zero.",
        "Beginner"
    ),
    (
        "A random variable X takes values 1 and 3 with probabilities 0.5 and 0.5 respectively. Find E(X).",
        "1",
        "2",
        "2.5",
        "3",
        "B",
        "E(X) = 1(0.5) + 3(0.5) = 0.5 + 1.5 = 2.",
        "Intermediate"
    ),
    (
        "If E(X) = 4 and E(X squared) = 20, find Var(X).",
        "4",
        "8",
        "12",
        "16",
        "B",
        "Var(X) = E(X²) - [E(X)]² = 20 - 16 = 4. Therefore the correct answer is A.",
        "Intermediate"
    ),
    (
        "If the variance of a random variable is 25, what is its standard deviation?",
        "3",
        "4",
        "5",
        "25",
        "C",
        "Standard deviation = √Variance = √25 = 5.",
        "Intermediate"
    )
]

# Correct the answer for Question 7:
# Var(X) = 20 - (4)^2 = 4, so option A is correct.
questions[6] = (
    questions[6][0],
    questions[6][1],
    questions[6][2],
    questions[6][3],
    questions[6][4],
    "A",
    "Var(X) = E(X²) - [E(X)]² = 20 - 16 = 4.",
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

    print("EEE Probability and Statistics Topic 6 added successfully!")
    print("Subject:", subject)
    print("Topic:", topic)
    print("New questions added:", inserted)
    print("Existing questions skipped:", skipped)

except Exception as error:
    connection.rollback()
    print("Error:", error)

finally:
    connection.close()
