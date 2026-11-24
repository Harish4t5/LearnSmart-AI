
import sqlite3

DB_PATH = "database/ideathon2k26.db"

units = [
    (
        "Object Oriented Thinking and Java Fundamentals",
        [
            "Object Oriented Thinking",
            "A Way of Viewing the World",
            "Computation as Simulation",
            "Messages and Methods",
            "History of Object Oriented Programming",
            "History of Java",
            "The Java White Paper",
            "OOP Concepts",
        ],
    ),
    (
        "Inheritance and Object Class",
        [
            "Understanding Inheritance",
            "Base Class Object",
            "Subclass, Subtype and Substitutability",
            "Forms of Inheritance",
            "Modifiers and Inheritance",
            "Benefits of Inheritance",
            "Final Keyword",
            "this Keyword",
            "Using super to Call Superclass Constructor",
            "Method Overriding",
            "Dynamic Method Dispatch",
            "Abstract Classes",
        ],
    ),
    (
        "Packages, Interfaces and Exception Handling",
        [
            "Packages",
            "Access Protection",
            "Importing Packages",
            "Interfaces",
            "Implementing Interfaces",
            "Variables in Interfaces",
            "Extending Interfaces",
            "Checked and Unchecked Exceptions",
            "Try and Catch",
            "Multiple Catch",
            "Throw and Throws",
            "Finally Block",
            "Built-in Exceptions",
            "User-defined Exceptions",
        ],
    ),
    (
        "Multithreading, Strings, Java I/O, JDBC and Networking",
        [
            "Java Thread Model",
            "Thread Priorities",
            "Synchronization",
            "Creating a Thread",
            "Creating Multiple Threads",
            "isAlive() and join()",
            "wait() and notify()",
            "String Constructors and Length",
            "Character Extraction and String Comparison",
            "Modifying a String",
            "Java I/O Classes and Interfaces",
            "Stream Classes",
            "Byte Streams and Character Streams",
            "Serialization",
            "JDBC Fundamentals",
            "Type I, II, III and IV JDBC Drivers",
            "Networking Basics and Socket Overview",
            "Networking Classes and Interfaces",
            "TCP/IP Client and Server Sockets",
            "Whois, URL and URLConnection",
        ],
    ),
    (
        "Polymorphism and AWT",
        [
            "Varieties of Polymorphism",
            "Polymorphic Variables",
            "Method Overloading",
            "Method Overriding",
            "Abstract Methods",
            "Pure Polymorphism",
            "AWT Class Hierarchy",
            "Layout Managers",
            "User Interface Components",
            "Panels and Dialogs",
            "Menu Bar",
            "Input and Output Streams",
            "Streams versus Readers and Writers",
            "Input Streams and Stream Tokenizer",
            "Output Streams",
            "Object Serialization",
            "Piped Input and Output",
        ],
    ),
    (
        "Applets and Event Handling",
        [
            "Applet Basics and Architecture",
            "Applet Skeleton",
            "HTML APPLET Tag",
            "Passing Parameters to Applets",
            "Applet Context and showDocument()",
            "Delegation Event Model",
            "Event Classes",
            "Event Listener Interfaces",
            "Adapter Classes",
            "AWT Window Fundamentals",
            "Component and Container",
            "Panel, Window, Frame and Canvas",
            "Creating a Frame Window in an Applet",
            "Working with Graphics",
            "Control Fundamentals",
            "Handling Events by Extending AWT Components",
        ],
    ),
    (
        "Core Java API, Swing and Advanced Concepts",
        [
            "Core Java API Packages",
            "Reflection",
            "Swing Applet",
            "Icons and Labels",
            "Text Fields and Buttons",
            "Combo Boxes",
            "Tabbed Panes and Scroll Panes",
            "Trees and Tables",
            "Simple Type Wrappers",
            "Runtime Memory Management",
            "Object Cloning",
            "Cloneable Interface",
            "Thread and Thread Group",
            "Runnable Interface",
        ],
    ),
]

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
          AND c.academic_year = ?
    """, ("CSE-AIML", 3, "CSE-303", "2024-25"))

    result = cursor.fetchone()

    if not result:
        raise ValueError("CSE-303 subject not found!")

    subject_id = result[0]
    units_added = 0
    topics_added = 0

    for unit_number, (unit_title, topics) in enumerate(units, start=1):
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
            """, (subject_id, unit_number, unit_title))

            unit_id = cursor.lastrowid
            units_added += 1

        for topic_order, topic_name in enumerate(topics, start=1):
            cursor.execute("""
                SELECT id FROM syllabus_topics
                WHERE unit_id = ? AND topic_order = ?
            """, (unit_id, topic_order))

            if cursor.fetchone():
                continue

            cursor.execute("""
                INSERT INTO syllabus_topics
                (unit_id, topic_name, topic_order)
                VALUES (?, ?, ?)
            """, (unit_id, topic_name, topic_order))

            topics_added += 1

    conn.commit()

    print("CSE Semester 3 - CSE-303 OOP import completed!")
    print("Units added:", units_added)
    print("Topics added:", topics_added)

except Exception:
    conn.rollback()
    raise

finally:
    conn.close()
