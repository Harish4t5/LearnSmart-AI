
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "database" / "ideathon2k26.db"

connection = sqlite3.connect(DB_PATH)

subject = "Probability and Statistics"
branch_code = "EEE"
semester = 3
topic = "Correlation and Regression"

questions = [
    (
        "What does correlation measure?",
        "The strength and direction of relationship between two variables",
        "The difference between two variables",
        "The sum of all observations",
        "The maximum value of a variable",
        "A",
        "Correlation measures the strength and direction of association between two variables.",
        "Beginner"
    ),
    (
        "What is the range of the correlation coefficient r?",
        "0 to 1",
        "-1 to +1",
        "-10 to +10",
        "0 to infinity",
        "B",
        "The correlation coefficient always lies between -1 and +1.",
        "Beginner"
    ),
    (
        "What does a correlation coefficient of +1 indicate?",
        "Perfect negative correlation",
        "No correlation",
        "Perfect positive correlation",
        "Weak correlation",
        "C",
        "A correlation coefficient of +1 indicates a perfect positive linear relationship.",
        "Beginner"
    ),
    (
        "What does a correlation coefficient of -1 indicate?",
        "Perfect positive correlation",
        "Perfect negative correlation",
        "No correlation",
        "Zero variance",
        "B",
        "A correlation coefficient of -1 indicates a perfect negative linear relationship.",
        "Beginner"
    ),
    (
        "What is the main purpose of regression analysis?",
        "To predict or estimate one variable using another",
        "To calculate only the median",
        "To arrange data alphabetically",
        "To find the highest observation only",
        "A",
        "Regression analysis models the relationship between variables and can be used for prediction.",
        "Beginner"
    ),
    (
        "If the correlation coefficient between X and Y is zero, it indicates:",
        "Perfect positive linear correlation",
        "Perfect negative linear correlation",
        "No linear correlation",
        "That X and Y must be identical",
        "C",
        "A zero correlation coefficient indicates no linear correlation, though a nonlinear relationship may still exist.",
        "Intermediate"
    ),
    (
        "In the regression equation Y = a + bX, what does b represent?",
        "The intercept",
        "The regression coefficient or slope",
        "The dependent variable",
        "The mean of Y",
        "B",
        "The coefficient b represents the slope, indicating the expected change in Y for a one-unit increase in X.",
        "Intermediate"
    ),
    (
        "If the regression equation is Y = 5 + 2X, what is the predicted value of Y when X = 3?",
        "8",
        "10",
        "11",
        "15",
        "C",
        "Substituting X = 3 gives Y = 5 + 2(3) = 11.",
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

    print("EEE Probability and Statistics Topic 7 added successfully!")
    print("Subject:", subject)
    print("Topic:", topic)
    print("New questions added:", inserted)
    print("Existing questions skipped:", skipped)

except Exception as error:
    connection.rollback()
    print("Error:", error)

finally:
    connection.close()
