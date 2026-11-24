
import sqlite3

DB_PATH = "database/ideathon2k26.db"

# Only subjects whose codes and names are available in the
# uploaded JUT 2024-25 syllabus PDFs are included.
subjects = {
    ("CSE-AIML", 3): [
        ("BSC-302", "Probability & Statistics", "Theory"),
        ("CSE-301", "Data Structures and Algorithms", "Theory"),
        ("CSE-302", "Digital Electronics and Systems", "Theory"),
        ("CSE-303", "Object Oriented Programming", "Theory"),
        ("CSE-304", "Database Management Systems", "Theory"),
        ("CSE-301P", "Data Structures Lab", "Lab"),
        ("CSE-302P", "Digital Electronics and Systems Lab", "Lab"),
        ("CSE-303P", "Object Oriented Programming Lab", "Lab"),
        ("CSE-304P", "Database Management Systems Lab", "Lab"),
    ],

    ("CSE-AIML", 4): [
        ("CSE-401", "Operating Systems", "Theory"),
        ("CSE-402", "Modelling and Optimization Techniques", "Theory"),
        ("CSE-403", "Design and Analysis of Algorithms", "Theory"),
        ("CSE-404", "Computer Networks", "Theory"),
        ("CSE-405", "Advanced Programming Practice", "Theory"),
        ("CSE-403P", "Design and Analysis of Algorithm Lab", "Lab"),
        ("CSE-401P", "Operating Systems Lab", "Lab"),
        ("CSE-405P", "Advanced Programming Laboratory", "Lab"),
    ],

    ("EEE", 3): [
        ("BSC-302", "Probability & Statistics", "Theory"),
        ("EEE-301", "Power Systems - I", "Theory"),
        ("EEE-304", "Signals & Systems", "Theory"),
        ("EEE-302", "Network Theory", "Theory"),
        ("EEE-303", "Data Structure with Python Program", "Theory"),
        ("EEE-301P", "Power Systems I Lab", "Lab"),
        ("EEE-302P", "Network Theory Lab", "Lab"),
        ("EEE-303P", "Data Structure with Python Program Lab", "Lab"),
    ],

    ("EEE", 4): [
        ("EEE-401", "Electrical Machines - I", "Theory"),
        ("EEE-402", "Power Systems - II", "Theory"),
        ("EEE-403", "Digital Electronics", "Theory"),
        ("EEE-404", "Control Systems", "Theory"),
        ("EEE-401P", "Electrical Machines - I Lab", "Lab"),
        ("EEE-404P", "Control Systems Lab", "Lab"),
        ("EEE-403P", "Digital Electronics Lab", "Lab"),
    ],
}


def main():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    added = 0
    skipped = 0

    try:
        for (branch_code, semester_number), course_list in subjects.items():

            cursor.execute("""
                SELECT s.id
                FROM semesters s
                JOIN curricula c ON s.curriculum_id = c.id
                JOIN branches b ON c.branch_id = b.id
                WHERE b.branch_code = ?
                  AND c.academic_year = ?
                  AND s.semester_number = ?
            """, (branch_code, "2024-25", semester_number))

            semester = cursor.fetchone()

            if semester is None:
                print(
                    f"Semester not found: {branch_code}, "
                    f"Semester {semester_number}"
                )
                continue

            semester_id = semester[0]

            for course_code, subject_name, subject_type in course_list:

                cursor.execute("""
                    SELECT id FROM subjects
                    WHERE semester_id = ? AND course_code = ?
                """, (semester_id, course_code))

                if cursor.fetchone():
                    skipped += 1
                    continue

                cursor.execute("""
                    INSERT INTO subjects
                    (semester_id, course_code, subject_name,
                     subject_type, credits)
                    VALUES (?, ?, ?, ?, ?)
                """, (
                    semester_id,
                    course_code,
                    subject_name,
                    subject_type,
                    None
                ))

                added += 1

        conn.commit()

        print("\n===== SUBJECT IMPORT SUMMARY =====")
        print("Subjects added:", added)
        print("Already existing subjects skipped:", skipped)

        print("\n===== SUBJECTS BY BRANCH AND SEMESTER =====")

        cursor.execute("""
            SELECT b.branch_code, s.semester_number,
                   sub.course_code, sub.subject_name, sub.subject_type
            FROM subjects sub
            JOIN semesters s ON sub.semester_id = s.id
            JOIN curricula c ON s.curriculum_id = c.id
            JOIN branches b ON c.branch_id = b.id
            ORDER BY b.branch_code, s.semester_number, sub.course_code
        """)

        for row in cursor.fetchall():
            print(row)

    except Exception:
        conn.rollback()
        raise

    finally:
        conn.close()


if __name__ == "__main__":
    main()
