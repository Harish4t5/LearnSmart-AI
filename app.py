from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
import math
from pathlib import Path
from recommendations import generate_recommendation
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv
from google import genai

app = Flask(__name__)

# Load environment variables
load_dotenv()

# Secure Flask session key
app.secret_key = os.getenv("FLASK_SECRET_KEY")

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Initialize Gemini client
gemini_client = None

if GEMINI_API_KEY:
    gemini_client = genai.Client(api_key=GEMINI_API_KEY)

# Database location
BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "database" / "ideathon2k26.db"


def get_db_connection():
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    return connection


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        full_name = request.form.get("full_name", "").strip()
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")
        confirm_password = request.form.get("confirm_password", "")
        college_name = request.form.get("college_name", "").strip()
        branch = request.form.get("branch", "").strip()
        semester = request.form.get("semester", "").strip()

        if not all([full_name, email, password, confirm_password,
                    college_name, branch, semester]):
            flash("Please fill in all fields.")
            return redirect(url_for("register"))

        if password != confirm_password:
            flash("Passwords do not match.")
            return redirect(url_for("register"))

        if len(password) < 8:
            flash("Password must contain at least 8 characters.")
            return redirect(url_for("register"))

        try:
            semester = int(semester)
            if semester < 1 or semester > 8:
                raise ValueError
        except ValueError:
            flash("Please select a valid semester.")
            return redirect(url_for("register"))

        password_hash = generate_password_hash(password)

        connection = get_db_connection()

        try:
            connection.execute("""
                INSERT INTO students
                (full_name, email, password_hash, college_name, branch, semester)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (full_name, email, password_hash, college_name, branch, semester))

            connection.commit()
            flash("Registration successful! You can now log in.")

        except sqlite3.IntegrityError:
            flash("This email is already registered.")

        finally:
            connection.close()

        return redirect(url_for("register"))

    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")

        connection = get_db_connection()

        student = connection.execute(
            "SELECT * FROM students WHERE email = ?",
            (email,)
        ).fetchone()

        connection.close()

        if student and check_password_hash(
            student["password_hash"], password
        ):
            session["student_id"] = student["id"]
            session["student_name"] = student["full_name"]

            flash("Login successful! Welcome to LearnSmart AI.")
            return redirect(url_for("dashboard"))

        flash("Invalid email or password. Please try again.")
        return redirect(url_for("login"))

    return render_template("login.html")



@app.route("/dashboard")
def dashboard():

    if "student_id" not in session:
        flash("Please log in first.")
        return redirect(url_for("login"))

    connection = get_db_connection()

    try:
        student = connection.execute("""
            SELECT *
            FROM students
            WHERE id = ?
        """, (session["student_id"],)).fetchone()

        if student is None:
            session.clear()
            flash("Student account not found. Please log in again.")
            return redirect(url_for("login"))

        weak_subjects = connection.execute("""
            SELECT
                subject,
                ROUND(
                    AVG(obtained_marks * 100.0 / maximum_marks),
                    2
                ) AS average_percentage
            FROM academic_marks
            WHERE student_id = ?
            GROUP BY subject
            HAVING AVG(obtained_marks * 100.0 / maximum_marks) < 60
        """, (session["student_id"],)).fetchall()

        topic_performance = connection.execute("""
            SELECT
                topic,
                ROUND(AVG(performance_percentage), 2)
                    AS average_percentage
            FROM topic_performance
            WHERE student_id = ?
            AND subject = ?
            GROUP BY topic
            ORDER BY average_percentage ASC
        """, (
            session["student_id"],
            "Python"
        )).fetchall()

        # Fetch the latest two quiz scores for each topic
        progress_rows = connection.execute("""
            SELECT
                tp.topic,
                tp.performance_percentage
            FROM topic_performance AS tp
            JOIN quiz_attempts AS qa
                ON qa.id = tp.quiz_attempt_id
            WHERE tp.student_id = ?
            AND tp.subject = ?
            ORDER BY
                tp.topic,
                qa.attempted_at DESC,
                qa.id DESC
        """, (
            session["student_id"],
            "Python"
        )).fetchall()

        topic_progress = []
        progress_by_topic = {}

        for row in progress_rows:

            topic = row["topic"]

            if topic not in progress_by_topic:
                progress_by_topic[topic] = []

            if len(progress_by_topic[topic]) < 2:
                progress_by_topic[topic].append(
                    round(row["performance_percentage"], 2)
                )

        for topic, scores in progress_by_topic.items():

            current_score = scores[0]

            if len(scores) >= 2:
                previous_score = scores[1]
                improvement = round(
                    current_score - previous_score, 2
                )
            else:
                previous_score = None
                improvement = None

            topic_progress.append({
                "topic": topic,
                "current_score": current_score,
                "previous_score": previous_score,
                "improvement": improvement
            })

        # Overall Learning Summary
        summary = connection.execute("""
            SELECT
                COUNT(*) AS total_quiz_attempts,
                ROUND(AVG(score_percentage), 2)
                    AS average_quiz_score
            FROM quiz_attempts
            WHERE student_id = ?
        """, (session["student_id"],)).fetchone()

        topics_tracked = connection.execute("""
            SELECT COUNT(DISTINCT topic) AS total_topics
            FROM topic_performance
            WHERE student_id = ?
        """, (session["student_id"],)).fetchone()["total_topics"]

        learning_summary = {
            "total_quiz_attempts": summary["total_quiz_attempts"],
            "average_quiz_score": summary["average_quiz_score"] or 0,
            "topics_tracked": topics_tracked
        }
                # Performance Analytics Chart


        # Existing personalized recommendations
        recommendations = []

        for topic in topic_performance:

            recommendation = generate_recommendation(
                topic["topic"],
                topic["average_percentage"]
            )

            resources = connection.execute("""
                SELECT
                    resource_type,
                    title,
                    url,
                    description
                FROM learning_resources
                WHERE subject = ?
                AND topic = ?
                AND level = ?
                ORDER BY resource_type, title
            """, (
                "Python",
                recommendation["topic"],
                recommendation["level"]
            )).fetchall()

            recommendation["resources"] = resources

            recommendations.append(recommendation)

    finally:
        connection.close()

    return render_template(
        "dashboard.html",
        student=student,
        weak_subjects=weak_subjects,
        topic_performance=topic_performance,
        recommendations=recommendations,
        topic_progress=topic_progress,
        learning_summary=learning_summary
    )


@app.route("/syllabus")
def syllabus():
    if "student_id" not in session:
        return redirect(url_for("login"))

    connection = get_db_connection()

    student = connection.execute(
        "SELECT branch, semester FROM students WHERE id = ?",
        (session["student_id"],)
    ).fetchone()

    if student is None:
        connection.close()
        flash("Student account not found.", "error")
        return redirect(url_for("login"))

    branch_map = {
        "CSE AI/ML": "CSE-AIML",
        "CSE-AIML": "CSE-AIML",
        "EEE": "EEE",
        "EE": "EEE"
    }

    branch_code = branch_map.get(student["branch"])

    # Read selected semester from the URL
    selected_semester = request.args.get(
        "semester",
        default=student["semester"],
        type=int
    )

    if selected_semester not in [1, 2, 3, 4]:
        selected_semester = student["semester"]

    if selected_semester not in [1, 2, 3, 4]:
        selected_semester = 1

    if branch_code is None:
        connection.close()
        return render_template(
            "syllabus.html",
            available=False,
            student=student,
            subjects=[],
            selected_semester=selected_semester
        )

    subjects = connection.execute("""
        SELECT
            subjects.id,
            subjects.course_code,
            subjects.subject_name,
            subjects.credits
        FROM subjects
        JOIN semesters ON subjects.semester_id = semesters.id
        JOIN curricula ON semesters.curriculum_id = curricula.id
        JOIN branches ON curricula.branch_id = branches.id
        WHERE branches.branch_code = ?
          AND semesters.semester_number = ?
          AND subjects.subject_type = 'Theory'
        ORDER BY subjects.course_code
    """, (branch_code, selected_semester)).fetchall()

    syllabus_data = []

    for subject in subjects:
        units = connection.execute("""
            SELECT unit_title
            FROM syllabus_units
            WHERE subject_id = ?
            ORDER BY id
        """, (subject["id"],)).fetchall()

        syllabus_data.append({
            "course_code": subject["course_code"],
            "subject_name": subject["subject_name"],
            "credits": subject["credits"],
            "units": units
        })

    connection.close()

    return render_template(
        "syllabus.html",
        available=True,
        student=student,
        subjects=syllabus_data,
        selected_semester=selected_semester
    )


@app.route("/analytics")
def analytics():

    if "student_id" not in session:
        flash("Please log in first.")
        return redirect(url_for("login"))

    connection = get_db_connection()

    try:
        student = connection.execute("""
            SELECT *
            FROM students
            WHERE id = ?
        """, (session["student_id"],)).fetchone()

        if student is None:
            session.clear()
            flash("Student account not found. Please log in again.")
            return redirect(url_for("login"))

        # Fetch subjects available to this student
        subject_rows = connection.execute("""
            SELECT DISTINCT subject
            FROM quiz_attempts
            WHERE student_id = ?
            ORDER BY subject
        """, (session["student_id"],)).fetchall()

        subjects = [row["subject"] for row in subject_rows]

        # Get selected subject from the URL
        selected_subject = request.args.get(
            "subject", "All Subjects"
        )

        if selected_subject not in subjects:
            selected_subject = "All Subjects"

        # Overall or subject-wise quiz summary
        summary = connection.execute("""
            SELECT
                COUNT(*) AS total_attempts,
                ROUND(AVG(score_percentage), 2) AS average_score
            FROM quiz_attempts
            WHERE student_id = ?
            AND (? = 'All Subjects' OR subject = ?)
        """, (
            session["student_id"],
            selected_subject,
            selected_subject
        )).fetchone()

        # Topic-wise performance
        topic_performance = connection.execute("""
            SELECT
                topic,
                ROUND(AVG(performance_percentage), 2)
                    AS average_percentage
            FROM topic_performance
            WHERE student_id = ?
            AND (? = 'All Subjects' OR subject = ?)
            GROUP BY topic
            ORDER BY average_percentage ASC
        """, (
            session["student_id"],
            selected_subject,
            selected_subject
        )).fetchall()

        # Quiz history
        quiz_history = connection.execute("""
            SELECT
                subject,
                total_questions,
                correct_answers,
                score_percentage,
                attempted_at
            FROM quiz_attempts
            WHERE student_id = ?
            AND (? = 'All Subjects' OR subject = ?)
            ORDER BY id DESC
            LIMIT 20
        """, (
            session["student_id"],
            selected_subject,
            selected_subject
        )).fetchall()
        # Convert UTC timestamps to Indian Standard Time (IST)
        quiz_history = [
    {
        **dict(row),
        "attempted_at": (
            datetime.strptime(
                row["attempted_at"],
                "%Y-%m-%d %H:%M:%S"
            ) + timedelta(hours=5, minutes=30)
        ).strftime("%Y-%m-%d %H:%M:%S")
    }
    for row in quiz_history
]

        # Prepare latest 10 attempts for the chart
        chart_rows = list(reversed(quiz_history[:10]))

        performance_chart = {
            "labels": [
                row["attempted_at"] for row in chart_rows
            ],
            "scores": [
                row["score_percentage"] for row in chart_rows
            ]
        }

        learning_summary = {
            "total_attempts": summary["total_attempts"],
            "average_score": summary["average_score"] or 0
        }

    finally:
        connection.close()

    return render_template(
        "analytics.html",
        student=student,
        subjects=subjects,
        selected_subject=selected_subject,
        learning_summary=learning_summary,
        topic_performance=topic_performance,
        quiz_history=quiz_history,
        performance_chart=performance_chart
    )




def analyse_performance(percentage):

    if percentage >= 75:
        return "Excellent"

    elif percentage >= 60:
        return "Good"

    elif percentage >= 40:
        return "Average"

    else:
        return "Needs Improvement"



@app.route("/study-plan")
def study_plan():

    if "student_id" not in session:
        flash("Please log in first.")
        return redirect(url_for("login"))

    connection = get_db_connection()

    try:
        # Get subjects available for this student
        available_subjects = connection.execute("""
            SELECT DISTINCT subject
            FROM topic_performance
            WHERE student_id = ?
            ORDER BY subject
        """, (session["student_id"],)).fetchall()

        available_subjects = [
            row["subject"] for row in available_subjects
        ]

        # Get selected subject from URL
        selected_subject = request.args.get(
            "subject", "All Subjects"
        )

        # Validate selected subject
        if selected_subject not in available_subjects:
            selected_subject = "All Subjects"

        # Fetch topic performance
        if selected_subject == "All Subjects":
            topic_rows = connection.execute("""
                SELECT
                    subject,
                    topic,
                    ROUND(AVG(performance_percentage), 2)
                        AS average_percentage
                FROM topic_performance
                WHERE student_id = ?
                GROUP BY subject, topic
                ORDER BY average_percentage ASC
            """, (session["student_id"],)).fetchall()

        else:
            topic_rows = connection.execute("""
                SELECT
                    subject,
                    topic,
                    ROUND(AVG(performance_percentage), 2)
                        AS average_percentage
                FROM topic_performance
                WHERE student_id = ?
                AND subject = ?
                GROUP BY subject, topic
                ORDER BY average_percentage ASC
            """, (
                session["student_id"],
                selected_subject
            )).fetchall()

        study_topics = []

        for row in topic_rows:

            # Fetch latest two quiz performances
            recent_attempts = connection.execute("""
                SELECT tp.performance_percentage
                FROM topic_performance tp
                JOIN quiz_attempts qa
                    ON tp.quiz_attempt_id = qa.id
                WHERE tp.student_id = ?
                AND tp.subject = ?
                AND tp.topic = ?
                ORDER BY qa.attempted_at DESC, tp.id DESC
                LIMIT 2
            """, (
                session["student_id"],
                row["subject"],
                row["topic"]
            )).fetchall()

            latest_score = recent_attempts[0]["performance_percentage"]

            previous_score = (
                recent_attempts[1]["performance_percentage"]
                if len(recent_attempts) > 1
                else None
            )

            recommendation = generate_recommendation(
                row["topic"],
                latest_score,
                previous_percentage=previous_score
            )

            # Fetch suitable learning resources
            resources = connection.execute("""
                SELECT
                    resource_type,
                    title,
                    url,
                    description
                FROM learning_resources
                WHERE subject = ?
                AND topic = ?
                AND level = ?
                ORDER BY resource_type, title
            """, (
                row["subject"],
                row["topic"],
                recommendation["level"]
            )).fetchall()

            score = row["average_percentage"]

            if score < 40:
                priority = "High"
            elif score < 60:
                priority = "Medium"
            else:
                priority = "Low"

            study_topics.append({
                "subject": row["subject"],
                "topic": row["topic"],
                "score": score,
                "level": recommendation["level"],
                "priority": priority,
                "message": recommendation["message"],
                "practice": recommendation["practice"],
                "resources": resources,
                "latest_score": latest_score,
                "previous_score": previous_score,
                "progress": recommendation["progress"]
            })

        # Generate personalized 7-day study schedule
        weekly_plan = []

        if study_topics:

            high_priority = [
                topic for topic in study_topics
                if topic["score"] < 40
            ]

            medium_priority = [
                topic for topic in study_topics
                if 40 <= topic["score"] < 60
            ]

            low_priority = [
                topic for topic in study_topics
                if 60 <= topic["score"] < 75
            ]

            advanced_topics = [
                topic for topic in study_topics
                if topic["score"] >= 75
            ]

            priority_topics = (
                high_priority * 2
                + medium_priority * 2
                + low_priority
                + advanced_topics
            )

            selected_topics = []

            priority_groups = [
                high_priority,
                medium_priority,
                low_priority,
                advanced_topics
            ]

            for group in priority_groups:
                if group and len(selected_topics) < 7:
                    selected_topics.append(group[0])

            for topic in priority_topics:
                if len(selected_topics) >= 7:
                    break

                if topic not in selected_topics:
                    selected_topics.append(topic)

            # Build weekly schedule
            for day, selected_topic in enumerate(
                selected_topics, start=1
            ):

                if selected_topic["level"] == "Beginner":
                    task = "Study basic concepts, review examples and solve beginner questions."

                elif selected_topic["level"] == "Intermediate":
                    task = "Strengthen concepts, practise coding problems and solve intermediate questions."

                else:
                    task = "Study advanced concepts and solve challenging problems."

                weekly_plan.append({
                    "day": day,
                    "subject": selected_topic["subject"],
                    "topic": selected_topic["topic"],
                    "task": task
                })

    finally:
        connection.close()

    return render_template(
        "study_plan.html",
        study_topics=study_topics,
        weekly_plan=weekly_plan,
        available_subjects=available_subjects,
        selected_subject=selected_subject
    )

@app.route("/marks", methods=["GET", "POST"])
def marks():

    # Check whether the student is logged in
    if "student_id" not in session:
        flash("Please log in to enter academic marks.")
        return redirect(url_for("login"))

    if request.method == "POST":

        subject = request.form.get("subject", "").strip()
        assessment_type = request.form.get("assessment_type", "")
        obtained_input = request.form.get("obtained_marks", "")
        maximum_input = request.form.get("maximum_marks", "")

        allowed_types = [
            "Internal",
            "Mid-Semester",
            "End-Semester",
            "Total"
        ]

        if not subject or len(subject) > 100:
            flash("Please enter a valid subject name.")
            return redirect(url_for("marks"))

        if assessment_type not in allowed_types:
            flash("Please select a valid assessment type.")
            return redirect(url_for("marks"))

        try:
            obtained = float(obtained_input)
            maximum = float(maximum_input)

            if not math.isfinite(obtained) or not math.isfinite(maximum):
                raise ValueError

            if maximum <= 0 or obtained < 0 or obtained > maximum:
                flash("Please enter valid marks.")
                return redirect(url_for("marks"))

        except ValueError:
            flash("Marks must be valid numbers.")
            return redirect(url_for("marks"))

        connection = get_db_connection()


        try:
            connection.execute("""
                INSERT INTO academic_marks
                (student_id, subject, assessment_type,
                 obtained_marks, maximum_marks)
                VALUES (?, ?, ?, ?, ?)
            """, (
                session["student_id"],
                subject,
                assessment_type,
                obtained,
                maximum
            ))

            connection.commit()
            flash("Academic marks saved successfully!")

        finally:
            connection.close()

        return redirect(url_for("marks"))

    connection = get_db_connection()

    try:
        marks_records = connection.execute("""
        SELECT subject, assessment_type,
               obtained_marks, maximum_marks,
               (obtained_marks * 100.0 / maximum_marks) AS percentage
        FROM academic_marks
        WHERE student_id = ?
        ORDER BY created_at DESC
    """, (session["student_id"],)).fetchall()

    finally:
            connection.close()
    marks_records = [dict(mark) for mark in marks_records]

    for mark in marks_records:
        percentage = mark["percentage"]

        mark["performance"] = analyse_performance(percentage)

        if percentage >= 75:
            mark["recommendation"] = "Continue learning"
        elif percentage >= 60:
            mark["recommendation"] = "Regular practice"
        elif percentage >= 40:
            mark["recommendation"] = "More practice needed"
        else:
            mark["recommendation"] = "Priority learning"

        mark["percentage"] = round(percentage, 2)

    return render_template(
        "marks.html",
        marks_records=marks_records
    )



@app.route("/quiz")
def quiz():

    if "student_id" not in session:
        flash("Please log in to attempt the quiz.")
        return redirect(url_for("login"))

    connection = get_db_connection()

    try:
        # Get the logged-in student's branch and semester
        student = connection.execute("""
            SELECT branch, semester
            FROM students
            WHERE id = ?
        """, (session["student_id"],)).fetchone()

        if student is None:
            flash("Student account not found.")
            return redirect(url_for("login"))

        # Convert registered branch into syllabus branch code
        branch_map = {
            "CSE AI/ML": "CSE-AIML",
            "CSE-AIML": "CSE-AIML",
            "EEE": "EEE",
            "EE": "EEE"
        }

        branch_code = branch_map.get(student["branch"])
        semester = student["semester"]

        # Fetch only subjects assigned to this branch and semester
        subjects = connection.execute("""
            SELECT DISTINCT subject
            FROM quiz_questions
            WHERE branch_code = ?
              AND semester = ?
            ORDER BY subject
        """, (branch_code, semester)).fetchall()

        available_subjects = [
            row["subject"] for row in subjects
        ]

        # Select a valid subject
        selected_subject = request.args.get("subject", "")

        if selected_subject not in available_subjects:
            selected_subject = (
                available_subjects[0]
                if available_subjects else ""
            )

        # Validate difficulty
        selected_difficulty = request.args.get(
            "difficulty", "All Levels"
        )

        valid_difficulties = [
            "All Levels",
            "Beginner",
            "Intermediate",
            "Advanced"
        ]

        if selected_difficulty not in valid_difficulties:
            selected_difficulty = "All Levels"

        # Fetch questions for the selected subject
        if selected_subject:

            if selected_difficulty == "All Levels":
                questions = connection.execute("""
                    SELECT id, subject, topic, question,
                           option_a, option_b, option_c, option_d
                    FROM quiz_questions
                    WHERE branch_code = ?
                      AND semester = ?
                      AND subject = ?
                    ORDER BY id
                """, (
                    branch_code,
                    semester,
                    selected_subject
                )).fetchall()

            else:
                questions = connection.execute("""
                    SELECT id, subject, topic, question,
                           option_a, option_b, option_c, option_d
                    FROM quiz_questions
                    WHERE branch_code = ?
                      AND semester = ?
                      AND subject = ?
                      AND difficulty = ?
                    ORDER BY id
                """, (
                    branch_code,
                    semester,
                    selected_subject,
                    selected_difficulty
                )).fetchall()

        else:
            questions = []

    finally:
        connection.close()

    return render_template(
        "quiz.html",
        questions=questions,
        subjects=available_subjects,
        selected_subject=selected_subject,
        selected_difficulty=selected_difficulty
    )




@app.route("/submit_quiz", methods=["POST"])
def submit_quiz():

    if "student_id" not in session:
        flash("Please log in first.")
        return redirect(url_for("login"))

    selected_subject = request.form.get("subject", "").strip()

    selected_difficulty = request.form.get(
        "difficulty", "All Levels"
    )

    valid_difficulties = [
        "All Levels",
        "Beginner",
        "Intermediate",
        "Advanced"
    ]

    if selected_difficulty not in valid_difficulties:
        flash("Invalid difficulty selection.")
        return redirect(url_for("quiz"))

    connection = get_db_connection()

    try:
        # Get the logged-in student's branch and semester
        student = connection.execute("""
            SELECT branch, semester
            FROM students
            WHERE id = ?
        """, (session["student_id"],)).fetchone()

        if student is None:
            flash("Student account not found.")
            return redirect(url_for("login"))

        # Convert registered branch into syllabus branch code
        branch_map = {
            "CSE AI/ML": "CSE-AIML",
            "CSE-AIML": "CSE-AIML",
            "EEE": "EEE",
            "EE": "EEE"
        }

        branch_code = branch_map.get(student["branch"])
        semester = student["semester"]

        if not branch_code:
            flash("Quiz is not available for your branch yet.")
            return redirect(url_for("dashboard"))

        # Verify that the selected subject belongs to this student
        available_subject = connection.execute("""
            SELECT DISTINCT subject
            FROM quiz_questions
            WHERE branch_code = ?
              AND semester = ?
              AND subject = ?
        """, (
            branch_code,
            semester,
            selected_subject
        )).fetchone()

        if available_subject is None:
            flash("Invalid subject selection.")
            return redirect(url_for("quiz"))

        # Fetch only questions for the student's branch and semester
        if selected_difficulty == "All Levels":

            questions = connection.execute("""
                SELECT id, subject, topic, question,
                       option_a, option_b, option_c, option_d,
                       correct_answer
                FROM quiz_questions
                WHERE branch_code = ?
                  AND semester = ?
                  AND subject = ?
                ORDER BY id
            """, (
                branch_code,
                semester,
                selected_subject
            )).fetchall()

        else:

            questions = connection.execute("""
                SELECT id, subject, topic, question,
                       option_a, option_b, option_c, option_d,
                       correct_answer
                FROM quiz_questions
                WHERE branch_code = ?
                  AND semester = ?
                  AND subject = ?
                  AND difficulty = ?
                ORDER BY id
            """, (
                branch_code,
                semester,
                selected_subject,
                selected_difficulty
            )).fetchall()

        total_questions = len(questions)

        if total_questions == 0:
            flash("No questions are available for this selection.")
            return redirect(url_for(
                "quiz",
                subject=selected_subject,
                difficulty=selected_difficulty
            ))

        correct_answers = 0
        topic_scores = {}

        # Evaluate submitted answers
        for question in questions:

            question_id = question["id"]
            topic = question["topic"]

            selected_answer = request.form.get(
                f"question_{question_id}"
            )

            is_correct = (
                selected_answer == question["correct_answer"]
            )

            if is_correct:
                correct_answers += 1

            if topic not in topic_scores:
                topic_scores[topic] = {
                    "total": 0,
                    "correct": 0
                }

            topic_scores[topic]["total"] += 1

            if is_correct:
                topic_scores[topic]["correct"] += 1

        score_percentage = (
            correct_answers / total_questions
        ) * 100

        # Save overall quiz attempt
        cursor = connection.execute("""
            INSERT INTO quiz_attempts
            (
                student_id,
                subject,
                total_questions,
                correct_answers,
                score_percentage
            )
            VALUES (?, ?, ?, ?, ?)
        """, (
            session["student_id"],
            selected_subject,
            total_questions,
            correct_answers,
            score_percentage
        ))

        attempt_id = cursor.lastrowid

        topic_results = []

        # Save topic-wise performance
        for topic, scores in topic_scores.items():

            percentage = (
                scores["correct"] / scores["total"]
            ) * 100

            connection.execute("""
                INSERT INTO topic_performance
                (
                    student_id,
                    quiz_attempt_id,
                    subject,
                    topic,
                    total_questions,
                    correct_answers,
                    performance_percentage
                )
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (
                session["student_id"],
                attempt_id,
                selected_subject,
                topic,
                scores["total"],
                scores["correct"],
                percentage
            ))

            # Find the previous attempt for this topic
            previous_attempt = connection.execute("""
                SELECT tp.performance_percentage
                FROM topic_performance AS tp
                JOIN quiz_attempts AS qa
                    ON qa.id = tp.quiz_attempt_id
                WHERE tp.student_id = ?
                  AND tp.subject = ?
                  AND tp.topic = ?
                  AND tp.quiz_attempt_id != ?
                ORDER BY qa.attempted_at DESC, qa.id DESC
                LIMIT 1
            """, (
                session["student_id"],
                selected_subject,
                topic,
                attempt_id
            )).fetchone()

            current_percentage = round(percentage, 2)

            if previous_attempt:

                previous_percentage = round(
                    previous_attempt["performance_percentage"], 2
                )

                improvement = round(
                    current_percentage - previous_percentage, 2
                )

            else:
                previous_percentage = None
                improvement = None

            topic_results.append({
                "topic": topic,
                "percentage": current_percentage,
                "previous_percentage": previous_percentage,
                "improvement": improvement
            })

        connection.commit()

    finally:
        connection.close()

    return render_template(
        "quiz_result.html",
        selected_subject=selected_subject,
        selected_difficulty=selected_difficulty,
        total_questions=total_questions,
        correct_answers=correct_answers,
        score_percentage=round(score_percentage, 2),
        topic_results=topic_results
    )

@app.route("/study-materials")
def study_materials():

    if "student_id" not in session:
        flash("Please log in first.")
        return redirect(url_for("login"))

    connection = get_db_connection()

    try:
        # Step 1: Get logged-in student's branch and semester
        student = connection.execute("""
            SELECT branch, semester
            FROM students
            WHERE id = ?
        """, (session["student_id"],)).fetchone()

        if not student:
            flash("Student details not found. Please log in again.")
            return redirect(url_for("login"))

        student_branch = student["branch"]
        student_semester = student["semester"]

        # Step 2: Map registered branch to database branch code
        branch_mapping = {
            "CSE AI/ML": "CSE-AIML",
            "CSE-AIML": "CSE-AIML",
            "EEE": "EEE",
            "EE": "EEE"
        }

        branch_code = branch_mapping.get(student_branch)

        # Step 3: Read selected filters
        selected_subject = request.args.get(
            "subject", "All Subjects"
        )
        selected_topic = request.args.get(
            "topic", "All Topics"
        )
        selected_level = request.args.get(
            "level", "All Levels"
        )

        # Step 4: Fetch subjects for this branch and semester only
        if branch_code:
            subjects = connection.execute("""
                SELECT DISTINCT subject
                FROM learning_resources
                WHERE branch_code = ?
                AND semester = ?
                ORDER BY subject
            """, (branch_code, student_semester)).fetchall()
        else:
            subjects = []

        available_subjects = [
            row["subject"] for row in subjects
        ]

        if selected_subject not in available_subjects:
            selected_subject = "All Subjects"

        # Step 5: Fetch topics for the selected subject
        topic_query = """
            SELECT DISTINCT topic
            FROM learning_resources
            WHERE branch_code = ?
            AND semester = ?
        """

        topic_parameters = [
            branch_code,
            student_semester
        ]

        if selected_subject != "All Subjects":
            topic_query += " AND subject = ?"
            topic_parameters.append(selected_subject)

        topic_query += " ORDER BY topic"

        if branch_code:
            topics = connection.execute(
                topic_query, topic_parameters
            ).fetchall()
        else:
            topics = []

        available_topics = [
            row["topic"] for row in topics
        ]

        if selected_topic not in available_topics:
            selected_topic = "All Topics"

        # Step 6: Fetch learning materials
        query = """
            SELECT subject, topic, level, resource_type,
                   title, url, description
            FROM learning_resources
            WHERE branch_code = ?
            AND semester = ?
        """

        parameters = [
            branch_code,
            student_semester
        ]

        if selected_subject != "All Subjects":
            query += " AND subject = ?"
            parameters.append(selected_subject)

        if selected_topic != "All Topics":
            query += " AND topic = ?"
            parameters.append(selected_topic)

        if selected_level != "All Levels":
            query += " AND level = ?"
            parameters.append(selected_level)

        query += """
            ORDER BY subject, topic,
            CASE level
                WHEN 'Beginner' THEN 1
                WHEN 'Intermediate' THEN 2
                WHEN 'Advanced' THEN 3
            END
        """

        if branch_code:
            resources = connection.execute(
                query, parameters
            ).fetchall()
        else:
            resources = []

    finally:
        connection.close()

    return render_template(
        "study_materials.html",
        available_subjects=available_subjects,
        available_topics=available_topics,
        selected_subject=selected_subject,
        selected_topic=selected_topic,
        selected_level=selected_level,
        resources=resources
    )



@app.route("/ai-chat", methods=["POST"])
def ai_chat():

    # Check whether the student is logged in
    if "student_id" not in session:
        return jsonify({
            "error": "Please log in to use the AI Assistant."
        }), 401

    # Check Gemini configuration
    if gemini_client is None:
        return jsonify({
            "error": "AI Assistant is not configured. Please check the API key."
        }), 503

    # Get the student's message
    data = request.get_json(silent=True) or {}
    user_message = data.get("message", "").strip()

    if not user_message:
        return jsonify({
            "error": "Please enter a message."
        }), 400

    if len(user_message) > 2000:
        return jsonify({
            "error": "Message is too long. Please keep it under 2000 characters."
        }), 400

    
    connection = get_db_connection()

    try:
        student = connection.execute("""
            SELECT full_name, branch, semester
            FROM students
            WHERE id = ?
        """, (session["student_id"],)).fetchone()

        syllabus_subjects = []

        if student is not None:

            branch_map = {
                "CSE AI/ML": "CSE-AIML",
                "CSE-AIML": "CSE-AIML",
                "EEE": "EEE",
                "EE": "EEE"
            }

            branch_code = branch_map.get(student["branch"])

            if branch_code:
                syllabus_subjects = connection.execute("""
                    SELECT
                        subjects.course_code,
                        subjects.subject_name,
                        syllabus_units.unit_title
                    FROM subjects
                    JOIN semesters
                        ON subjects.semester_id = semesters.id
                    JOIN curricula
                        ON semesters.curriculum_id = curricula.id
                    JOIN branches
                        ON curricula.branch_id = branches.id
                    LEFT JOIN syllabus_units
                        ON syllabus_units.subject_id = subjects.id
                    WHERE branches.branch_code = ?
                      AND semesters.semester_number = ?
                      AND subjects.subject_type = 'Theory'
                    ORDER BY subjects.course_code, syllabus_units.id
                """, (
                    branch_code,
                    student["semester"]
                )).fetchall()

    finally:
        connection.close()

    if student is None:
        return jsonify({
            "error": "Student account not found."
        }), 404

    # Convert syllabus database rows into readable text
    syllabus_context = "\n".join(
        f"- {row['course_code']} | {row['subject_name']} | {row['unit_title'] or 'Units not added yet'}"
        for row in syllabus_subjects
    )

    if not syllabus_context:
        syllabus_context = "No syllabus data available for this student's branch and semester."

    # Prepare the AI instruction and student context
    prompt = f"""

    You are LearnSmart AI, a friendly and helpful academic assistant
    for B.Tech students.

    Student information:
    Name: {student['full_name']}
    Branch: {student['branch']}
    Semester: {student['semester']}
        Current semester syllabus:
    {syllabus_context}

    Use this syllabus as reference when answering academic questions.
    Do not invent official course codes, subject names, or unit titles.
    If syllabus information is unavailable, clearly say so.

    Your responsibilities:
    1. Explain Python, DSA, OOP, DBMS and other engineering subjects.
    2. Explain programming concepts in beginner-friendly language.
    3. Help students understand code errors and debugging.
    4. Provide examples and step-by-step explanations when useful.
    5. Help with study planning and exam preparation.
    6. Always use valid Markdown formatting.
    7. Use triple backticks with the correct language identifier,
       such as python, cpp, java or sql.
    8. Never write the word "Copy" after code blocks.
    9. Do not nest code blocks or use mismatched backticks.
    10. Keep code examples separate from explanations.
    11. Never use unrelated code language identifiers.

    Keep answers clear, accurate and easy to understand.
    Use examples when they help the student learn.

    Student's message:
    {user_message}
    """

    try:
        response = gemini_client.models.generate_content(
            model="gemini-3.5-flash-lite",
            contents=prompt
        )

        ai_reply = response.text

        if not ai_reply:
            return jsonify({
                "error": "The AI could not generate a response. Please try again."
            }), 502

        return jsonify({
            "reply": ai_reply
        })

    except Exception as error:
        print("Gemini API Error:", error)

        return jsonify({
            "error": "The AI Assistant is temporarily unavailable. Please try again."
        }), 503


@app.route("/logout")
def logout():
    session.clear()
    flash("You have been logged out.")
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        debug=False
    )
