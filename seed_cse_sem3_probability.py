
import sqlite3

DB_PATH = "database/ideathon2k26.db"

def main():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    try:
        # Find the Probability & Statistics subject
        cursor.execute("""
            SELECT s.id
            FROM subjects s
            JOIN semesters sem ON s.semester_id = sem.id
            JOIN curricula c ON sem.curriculum_id = c.id
            JOIN branches b ON c.branch_id = b.id
            WHERE b.branch_code = ?
              AND sem.semester_number = ?
              AND s.course_code = ?
        """, ("CSE-AIML", 3, "BSC-302"))

        result = cursor.fetchone()

        if not result:
            raise ValueError("BSC-302 subject was not found.")

        subject_id = result[0]

        syllabus = {
            1: {
                "title": "Random variables and their distributions",
                "topics": [
                    "Introduction to Probability",
                    "Random variables (discrete and continuous)",
                    "Probability functions",
                    "Density and distribution functions",
                    "Mean and variance",
                    "Binomial distribution",
                    "Hypergeometric distribution",
                    "Poisson distribution",
                    "Uniform distribution",
                    "Exponential distribution",
                    "Normal distribution",
                    "Chebyshev's inequality",
                    "Parameter and statistic",
                    "Maximum Likelihood Estimation"
                ]
            },
            2: {
                "title": "Testing of Hypothesis",
                "topics": [
                    "Null and alternative hypothesis",
                    "Level of significance",
                    "One-tailed and two-tailed tests",
                    "Large sample tests",
                    "Tests for single mean and difference of means",
                    "Tests for single proportion and difference of proportions",
                    "Small sample tests",
                    "t-test for single mean and difference of means",
                    "F-test for comparison of variances",
                    "Chi-square test for goodness of fit",
                    "Analysis of variance (ANOVA)",
                    "Karl Pearson coefficient of correlation",
                    "Lines of regression"
                ]
            },
            3: {
                "title": "Queuing theory",
                "topics": [
                    "Concepts and applicability of queuing theory",
                    "Classification of queuing models",
                    "Birth and death process",
                    "Poisson queues",
                    "Characteristics of queuing models",
                    "Single server model with finite and infinite capacities",
                    "Multiple server model with infinite capacity"
                ]
            }
        }

        units_added = 0
        topics_added = 0

        for unit_number, unit_data in syllabus.items():
            cursor.execute("""
                SELECT id FROM syllabus_units
                WHERE subject_id = ? AND unit_number = ?
            """, (subject_id, unit_number))

            existing_unit = cursor.fetchone()

            if existing_unit:
                unit_id = existing_unit[0]
            else:
                cursor.execute("""
                    INSERT INTO syllabus_units
                    (subject_id, unit_number, unit_title)
                    VALUES (?, ?, ?)
                """, (subject_id, unit_number, unit_data["title"]))

                unit_id = cursor.lastrowid
                units_added += 1

            for order, topic in enumerate(unit_data["topics"], start=1):
                cursor.execute("""
                    SELECT id FROM syllabus_topics
                    WHERE unit_id = ? AND topic_name = ?
                """, (unit_id, topic))

                if cursor.fetchone():
                    continue

                cursor.execute("""
                    INSERT INTO syllabus_topics
                    (unit_id, topic_name, topic_order)
                    VALUES (?, ?, ?)
                """, (unit_id, topic, order))

                topics_added += 1

        conn.commit()

        print("CSE Semester 3 - BSC-302 import completed!")
        print("Units added:", units_added)
        print("Topics added:", topics_added)

    except Exception:
        conn.rollback()
        raise

    finally:
        conn.close()


if __name__ == "__main__":
    main()
