
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "database" / "ideathon2k26.db"

connection = sqlite3.connect(DB_PATH)

subject = "Probability and Statistics"
branch_code = "EEE"
semester = 3
topic = "Sampling and Statistical Estimation"

questions = [
    (
        "What is sampling in statistics?",
        "Selecting a subset of a population for study",
        "Studying every member of a population",
        "Removing all data",
        "Calculating only the maximum value",
        "A",
        "Sampling involves selecting a representative subset from a population to draw conclusions about it.",
        "Beginner"
    ),
    (
        "What is a population in statistics?",
        "A small selected group only",
        "The entire group of individuals or observations under study",
        "Only the sample mean",
        "A collection of random numbers",
        "B",
        "A population is the complete set of individuals or observations being studied.",
        "Beginner"
    ),
    (
        "What is a sample?",
        "The entire population",
        "A subset of the population",
        "The maximum observation",
        "The population variance",
        "B",
        "A sample is a selected subset of a population.",
        "Beginner"
    ),
    (
        "Which sampling method gives every population member an equal chance of selection?",
        "Convenience sampling",
        "Judgment sampling",
        "Simple random sampling",
        "Quota sampling",
        "C",
        "In simple random sampling, each population member has an equal chance of being selected.",
        "Beginner"
    ),
    (
        "What is the purpose of statistical estimation?",
        "To estimate unknown population parameters using sample data",
        "To remove all observations",
        "To calculate only the sample size",
        "To arrange observations alphabetically",
        "A",
        "Statistical estimation uses sample information to estimate unknown population parameters.",
        "Beginner"
    ),
    (
        "A sample contains the values 2, 4, 6, 8 and 10. What is its sample mean?",
        "4",
        "5",
        "6",
        "8",
        "C",
        "Sample mean = (2 + 4 + 6 + 8 + 10) / 5 = 30 / 5 = 6.",
        "Intermediate"
    ),
    (
        "Which of the following is a measure of the variability of sample observations?",
        "Sample variance",
        "Sample mean",
        "Sample median",
        "Sample mode",
        "A",
        "Sample variance measures how spread out the observations are around the sample mean.",
        "Intermediate"
    ),
    (
        "What does a confidence interval provide?",
        "A range of plausible values for an unknown population parameter",
        "The exact value of every population observation",
        "The maximum value of a sample",
        "The number of population members",
        "A",
        "A confidence interval provides a range of plausible values for an unknown population parameter at a stated confidence level.",
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

    print("EEE Probability and Statistics Topic 8 added successfully!")
    print("Subject:", subject)
    print("Topic:", topic)
    print("New questions added:", inserted)
    print("Existing questions skipped:", skipped)

except Exception as error:
    connection.rollback()
    print("Error:", error)

finally:
    connection.close()

