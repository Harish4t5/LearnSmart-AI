
import sqlite3

DB_PATH = "database/ideathon2k26.db"

connection = sqlite3.connect(DB_PATH)
cursor = connection.cursor()

# Enable foreign key support
cursor.execute("PRAGMA foreign_keys = ON")

# 1. Branches
cursor.execute("""
CREATE TABLE IF NOT EXISTS branches (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    branch_code TEXT UNIQUE NOT NULL,
    branch_name TEXT NOT NULL
)
""")

# 2. Curricula
cursor.execute("""
CREATE TABLE IF NOT EXISTS curricula (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    branch_id INTEGER NOT NULL,
    academic_year TEXT NOT NULL,
    regulation TEXT,
    source_url TEXT,
    FOREIGN KEY (branch_id) REFERENCES branches(id),
    UNIQUE(branch_id, academic_year, regulation)
)
""")

# 3. Semesters
cursor.execute("""
CREATE TABLE IF NOT EXISTS semesters (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    curriculum_id INTEGER NOT NULL,
    semester_number INTEGER NOT NULL,
    FOREIGN KEY (curriculum_id) REFERENCES curricula(id),
    UNIQUE(curriculum_id, semester_number)
)
""")

# 4. Subjects
cursor.execute("""
CREATE TABLE IF NOT EXISTS subjects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    semester_id INTEGER NOT NULL,
    course_code TEXT,
    subject_name TEXT NOT NULL,
    subject_type TEXT,
    credits REAL,
    FOREIGN KEY (semester_id) REFERENCES semesters(id)
)
""")

# 5. Syllabus Units
cursor.execute("""
CREATE TABLE IF NOT EXISTS syllabus_units (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    subject_id INTEGER NOT NULL,
    unit_number INTEGER NOT NULL,
    unit_title TEXT NOT NULL,
    FOREIGN KEY (subject_id) REFERENCES subjects(id)
)
""")

# 6. Syllabus Topics
cursor.execute("""
CREATE TABLE IF NOT EXISTS syllabus_topics (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    unit_id INTEGER NOT NULL,
    topic_name TEXT NOT NULL,
    topic_order INTEGER DEFAULT 1,
    FOREIGN KEY (unit_id) REFERENCES syllabus_units(id)
)
""")

connection.commit()
connection.close()

print("================================")
print("Syllabus database migration done!")
print("Six new tables created successfully.")
print("Existing tables preserved.")
print("================================")
