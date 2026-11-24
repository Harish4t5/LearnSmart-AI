
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
        """, ("CSE-AIML", 3, "CSE-302P"))

        result = cursor.fetchone()

        if not result:
            raise ValueError("CSE-302P subject was not found.")

        subject_id = result[0]

        experiments = [
            "Study of Logic Gate ICs",
            "Realization of Boolean Functions using Logic Gate ICs",
            "Truth Table Based Design and Implementation of Simple Real-Life Problems",
            "Implementation of Digital Systems using MSI Building Blocks such as Adders, Multiplexers and Decoders",
            "Breadboard Realization of Synchronous Sequential Circuits",
            "Digital System Design and Implementation for a Real-Life Problem"
        ]

        cursor.execute("""
            SELECT id FROM syllabus_units
            WHERE subject_id = ? AND unit_number = 1
        """, (subject_id,))

        existing_unit = cursor.fetchone()

        if existing_unit:
            unit_id = existing_unit[0]
        else:
            cursor.execute("""
                INSERT INTO syllabus_units
                (subject_id, unit_number, unit_title)
                VALUES (?, ?, ?)
            """, (subject_id, 1, "List of Experiments"))

            unit_id = cursor.lastrowid

        topics_added = 0

        for order, experiment in enumerate(experiments, start=1):
            cursor.execute("""
                SELECT id FROM syllabus_topics
                WHERE unit_id = ? AND topic_name = ?
            """, (unit_id, experiment))

            if cursor.fetchone():
                continue

            cursor.execute("""
                INSERT INTO syllabus_topics
                (unit_id, topic_name, topic_order)
                VALUES (?, ?, ?)
            """, (unit_id, experiment, order))

            topics_added += 1

        conn.commit()

        print("CSE Semester 3 - CSE-302P import completed!")
        print("Units added:", 0 if existing_unit else 1)
        print("Experiments added:", topics_added)

    except Exception:
        conn.rollback()
        raise

    finally:
        conn.close()


if __name__ == "__main__":
    main()
