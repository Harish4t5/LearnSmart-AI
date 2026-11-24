
import sqlite3

DB_PATH = "database/ideathon2k26.db"

def main():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    try:
        cursor.execute("""
            SELECT s.id
            FROM subjects s
            JOIN semesters sem ON s.semester_id = sem.id
            JOIN curricula c ON sem.curriculum_id = c.id
            JOIN branches b ON c.branch_id = b.id
            WHERE b.branch_code = ?
              AND sem.semester_number = ?
              AND s.course_code = ?
        """, ("CSE-AIML", 3, "CSE-302"))

        result = cursor.fetchone()

        if not result:
            raise ValueError("CSE-302 subject was not found.")

        subject_id = result[0]

        syllabus = {
            1: {
                "title": "Introduction to Logic Circuits",
                "topics": [
                    "Variables and Functions",
                    "Inversion",
                    "Truth Tables",
                    "Logic Gates and Networks",
                    "Boolean Algebra",
                    "Synthesis using Gates",
                    "Design Examples",
                    "Optimized Implementation of Logic Functions",
                    "Karnaugh Map",
                    "Strategy for Minimization",
                    "Minimization of Product of Sums Forms",
                    "Incompletely Specified Functions",
                    "Multiple Output Circuits",
                    "Tabular Method for Minimization",
                    "Number Representation and Arithmetic Circuits",
                    "Addition of Unsigned Numbers",
                    "Signed Numbers",
                    "Fast Adders"
                ]
            },
            2: {
                "title": "Combinational Circuit Building Blocks",
                "topics": [
                    "Multiplexers",
                    "Decoders",
                    "Encoders",
                    "Code Converters",
                    "Arithmetic Comparison Circuits",
                    "Basic Latch",
                    "Gated SR Latch",
                    "Gated D Latch",
                    "Master Slave Flip-Flops",
                    "Edge Triggered D Flip-Flops",
                    "T Flip-Flop",
                    "JK Flip-Flop",
                    "Registers",
                    "Counters",
                    "Reset Synchronization",
                    "Other Types of Counters"
                ]
            },
            3: {
                "title": "Synchronous Sequential Circuits",
                "topics": [
                    "Basic Design Steps",
                    "State Assignment Problem",
                    "Mealy State Model",
                    "Serial Adders",
                    "State Minimization",
                    "Introduction to Asynchronous Sequential Circuits",
                    "Introduction to CMOS Logic"
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

        print("CSE Semester 3 - CSE-302 import completed!")
        print("Units added:", units_added)
        print("Topics added:", topics_added)

    except Exception:
        conn.rollback()
        raise

    finally:
        conn.close()


if __name__ == "__main__":
    main()
