
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "database" / "ideathon2k26.db"

connection = sqlite3.connect(DB_PATH)

subject = "Probability and Statistics"
branch_code = "EEE"
semester = 3
topic = "Probability Distributions"

questions = [
    (
        "What does a probability distribution describe?",
        "Possible values of a random variable and their probabilities",
        "Only the average of a dataset",
        "Only the maximum value of a dataset",
        "The physical dimensions of a circuit",
        "A",
        "A probability distribution describes the possible values of a random variable and the probabilities associated with them.",
        "Beginner"
    ),
    (
        "Which distribution is commonly used to model the number of successes in a fixed number of independent trials?",
        "Normal distribution",
        "Binomial distribution",
        "Exponential distribution",
        "Uniform distribution",
        "B",
        "The binomial distribution models the number of successes in a fixed number of independent Bernoulli trials.",
        "Beginner"
    ),
    (
        "Which distribution has a bell-shaped curve?",
        "Binomial distribution",
        "Poisson distribution",
        "Normal distribution",
        "Geometric distribution",
        "C",
        "The normal distribution is commonly represented by a symmetric bell-shaped curve.",
        "Beginner"
    ),
    (
        "Which distribution is often used to model the number of events occurring in a fixed interval at a constant average rate?",
        "Poisson distribution",
        "Normal distribution",
        "Uniform distribution",
        "Continuous uniform distribution",
        "A",
        "The Poisson distribution models event counts over a fixed interval under suitable assumptions.",
        "Beginner"
    ),
    (
        "In a binomial distribution, what does n represent?",
        "Number of trials",
        "Probability of failure",
        "Number of successes only",
        "Mean of the distribution",
        "A",
        "The parameter n represents the fixed number of independent trials.",
        "Beginner"
    ),
    (
        "A fair coin is tossed 3 times. What is the probability of getting exactly 2 heads?",
        "1/8",
        "3/8",
        "1/2",
        "5/8",
        "B",
        "Using the binomial formula: P(X=2) = C(3,2)(1/2)^2(1/2)^1 = 3/8.",
        "Intermediate"
    ),
    (
        "For a Poisson distribution with parameter lambda = 2, what is P(X = 0)?",
        "1",
        "e^(-2)",
        "2e^(-2)",
        "1 - e^(-2)",
        "B",
        "The Poisson formula is P(X=x) = e^(-lambda) lambda^x / x!. For x=0 and lambda=2, the answer is e^(-2).",
        "Intermediate"
    ),
    (
        "For a normal distribution, which two parameters determine its shape and location?",
        "Mean and variance",
        "Median and mode only",
        "Maximum and minimum",
        "Range and sample size",
        "A",
        "A normal distribution is determined by its mean and variance (or equivalently, standard deviation).",
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

    print("EEE Probability and Statistics Topic 5 added successfully!")
    print("Subject:", subject)
    print("Topic:", topic)
    print("New questions added:", inserted)
    print("Existing questions skipped:", skipped)

except Exception as error:
    connection.rollback()
    print("Error:", error)

finally:
    connection.close()
