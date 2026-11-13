
import sqlite3
from pathlib import Path

# Find the main project directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Database file location
DB_PATH = BASE_DIR / "database" / "ideathon2k26.db"


def create_database():
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    connection = sqlite3.connect(DB_PATH)

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            full_name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            password_hash TEXT NOT NULL,
            college_name TEXT NOT NULL,
            branch TEXT NOT NULL,
            semester INTEGER NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    # Create quiz questions table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS quiz_questions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            subject TEXT NOT NULL,
            topic TEXT NOT NULL,
            question TEXT NOT NULL,
            option_a TEXT NOT NULL,
            option_b TEXT NOT NULL,
            option_c TEXT NOT NULL,
            option_d TEXT NOT NULL,
            correct_answer TEXT NOT NULL
    CHECK (correct_answer IN ('A', 'B', 'C', 'D')),
explanation TEXT,
difficulty TEXT
    CHECK (difficulty IN ('Beginner', 'Intermediate', 'Advanced'))
        )
    """)
        # Add difficulty column to existing databases if missing
    cursor.execute("PRAGMA table_info(quiz_questions)")
    columns = [column[1] for column in cursor.fetchall()]

    if "difficulty" not in columns:
        cursor.execute("""
            ALTER TABLE quiz_questions
            ADD COLUMN difficulty TEXT
            CHECK (difficulty IN ('Beginner', 'Intermediate', 'Advanced'))
        """)

    # Create quiz attempts table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS quiz_attempts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER NOT NULL,
            subject TEXT NOT NULL,
            total_questions INTEGER NOT NULL,
            correct_answers INTEGER NOT NULL,
            score_percentage REAL NOT NULL,
            attempted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

            FOREIGN KEY (student_id)
                REFERENCES students(id)
                ON DELETE CASCADE
        )
    """)


    cursor.execute("""
        CREATE TABLE IF NOT EXISTS academic_marks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER NOT NULL,
            subject TEXT NOT NULL,
            assessment_type TEXT NOT NULL
                CHECK (assessment_type IN (
                    'Internal',
                    'Mid-Semester',
                    'End-Semester',
                    'Total'
                )),
            obtained_marks REAL NOT NULL
                CHECK (obtained_marks >= 0),
            maximum_marks REAL NOT NULL
                CHECK (maximum_marks > 0),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

            FOREIGN KEY (student_id)
                REFERENCES students(id)
                ON DELETE CASCADE,

            CHECK (obtained_marks <= maximum_marks)
        )
    """)


    sample_questions = [
    (
        "Python", "Basics",
        "Which symbol is used for comments in Python?",
        "//", "#", "/* */", "--",
        "B",
        "The # symbol is used for single-line comments."
    ),
    (
        "Python", "Basics",
        "Which data type stores True or False?",
        "int", "str", "bool", "float",
        "C",
        "The bool data type stores True or False."
    ),
    (
        "Python", "Basics",
        "What is the output of print(2 ** 3)?",
        "6", "8", "9", "5",
        "B",
        "The ** operator performs exponentiation."
    ),
    (
        "Python", "Loops",
        "Which loop is commonly used to iterate over a sequence?",
        "if", "for", "def", "class",
        "B",
        "A for loop iterates over sequence elements."
    ),
    (
        "Python", "Loops",
        "What does the break statement do?",
        "Skips one iteration",
        "Stops the loop",
        "Restarts the loop",
        "Defines a function",
        "B",
        "The break statement terminates the loop."
    ),
    (
        "Python", "Functions",
        "Which keyword is used to define a function?",
        "function", "def", "fun", "define",
        "B",
        "The def keyword defines a function."
    ),
    (
        "Python", "Functions",
        "What does the return statement do?",
        "Repeats a loop",
        "Defines a variable",
        "Sends a value back from a function",
        "Prints text automatically",
        "C",
        "The return statement sends a value back."
    )
]


        # Create topic performance table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS topic_performance (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER NOT NULL,
            quiz_attempt_id INTEGER NOT NULL,
            subject TEXT NOT NULL,
            topic TEXT NOT NULL,
            total_questions INTEGER NOT NULL,
            correct_answers INTEGER NOT NULL,
            performance_percentage REAL NOT NULL,

            FOREIGN KEY (student_id)
                REFERENCES students(id)
                ON DELETE CASCADE,

            FOREIGN KEY (quiz_attempt_id)
                REFERENCES quiz_attempts(id)
                ON DELETE CASCADE
        )
    """)

    # Create personalized learning resources table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS learning_resources (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            subject TEXT NOT NULL,
            topic TEXT NOT NULL,
            level TEXT NOT NULL
                CHECK (level IN (
                    'Beginner',
                    'Intermediate',
                    'Advanced'
                )),
            resource_type TEXT NOT NULL
                CHECK (resource_type IN (
                    'Video',
                    'Practice',
                    'Article',
                    'Documentation'
                )),
            title TEXT NOT NULL,
            url TEXT NOT NULL,
            description TEXT,

            UNIQUE(subject, topic, level, resource_type, title)
        )
    """)

    # Add curated Python learning resources
    resource_data = [
        (
            "Python", "Basics", "Beginner",
            "Article", "Python Basics for Beginners",
            "https://www.programiz.com/python-programming/first-program",
            "Learn Python fundamentals with simple examples."
        ),
        (
            "Python", "Basics", "Intermediate",
            "Practice", "Python Programming Practice",
            "https://www.hackerrank.com/domains/python",
            "Practice Python programming problems."
        ),
        (
            "Python", "Basics", "Advanced",
            "Documentation", "Python Standard Library",
            "https://docs.python.org/3/library/",
            "Explore Python's standard library."
        ),
        (
            "Python", "Loops", "Beginner",
            "Article", "Python For Loop Tutorial",
            "https://www.programiz.com/python-programming/for-loop",
            "Understand loops with beginner-friendly examples."
        ),
        (
            "Python", "Loops", "Intermediate",
            "Practice", "Python Practice Challenges",
            "https://www.hackerrank.com/domains/python",
            "Improve your loop-solving skills."
        ),
        (
            "Python", "Loops", "Advanced",
            "Documentation", "Python Control Flow",
            "https://docs.python.org/3/tutorial/controlflow.html",
            "Study advanced control flow concepts."
        ),
        (
            "Python", "Functions", "Beginner",
            "Article", "Python Functions Tutorial",
            "https://www.programiz.com/python-programming/function",
            "Learn how to define and call functions."
        ),
        (
            "Python", "Functions", "Intermediate",
            "Practice", "Python Coding Challenges",
            "https://www.hackerrank.com/domains/python",
            "Practice writing and using Python functions."
        ),
        (
            "Python", "Functions", "Advanced",
            "Documentation", "Python Function Definitions",
            "https://docs.python.org/3/tutorial/controlflow.html#defining-functions",
            "Explore function definitions in detail."
        )
    ]

    cursor.executemany("""
        INSERT OR IGNORE INTO learning_resources
        (
            subject, topic, level, resource_type,
            title, url, description
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, resource_data)


    # Check whether Python questions already exist
    existing_questions = cursor.execute("""
        SELECT COUNT(*)
        FROM quiz_questions
        WHERE subject = ?
    """, ("Python",)).fetchone()[0]

    # Insert sample questions only if none exist
    if existing_questions == 0:
        cursor.executemany("""
            INSERT INTO quiz_questions
            (
                subject, topic, question,
                option_a, option_b, option_c, option_d,
                correct_answer, explanation
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, sample_questions)

    connection.commit()
    connection.close()

    print("Database and students table created successfully!")


if __name__ == "__main__":
    create_database()
