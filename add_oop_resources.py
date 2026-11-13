
import sqlite3

DB_PATH = "database/ideathon2k26.db"

resources = [

    # MODULE 1 - OOP FUNDAMENTALS
    ("Module 1 - OOP Fundamentals", "Beginner", "Article",
     "Introduction to Object-Oriented Programming",
     "https://docs.oracle.com/javase/tutorial/java/concepts/",
     "Learn classes, objects, abstraction, encapsulation and OOP concepts."),

    ("Module 1 - OOP Fundamentals", "Intermediate", "Documentation",
     "Java Classes and Objects",
     "https://docs.oracle.com/javase/tutorial/java/javaOO/index.html",
     "Study constructors, methods, fields, objects and class members."),

    ("Module 1 - OOP Fundamentals", "Advanced", "Documentation",
     "Modern Java Learning Resources",
     "https://dev.java/learn/",
     "Explore Java language concepts and advanced programming features."),

    # MODULE 2 - INHERITANCE AND POLYMORPHISM
    ("Module 2 - Inheritance and Polymorphism", "Beginner", "Article",
     "Java Inheritance and Interfaces",
     "https://docs.oracle.com/javase/tutorial/java/IandI/index.html",
     "Understand inheritance, interfaces and superclass-subclass relationships."),

    ("Module 2 - Inheritance and Polymorphism", "Intermediate", "Practice",
     "Java Programming Practice",
     "https://www.hackerrank.com/domains/java",
     "Practice Java coding questions involving classes and inheritance."),

    ("Module 2 - Inheritance and Polymorphism", "Advanced", "Documentation",
     "Java Language Specification",
     "https://docs.oracle.com/javase/specs/",
     "Explore the formal Java language rules and object-oriented features."),

    # MODULE 3 - PACKAGES AND EXCEPTIONS
    ("Module 3 - Packages and Exceptions", "Beginner", "Article",
     "Java Exceptions Tutorial",
     "https://docs.oracle.com/javase/tutorial/essential/exceptions/",
     "Learn exception types, try, catch, finally, throw and throws."),

    ("Module 3 - Packages and Exceptions", "Intermediate", "Practice",
     "Java Exception Handling Practice",
     "https://www.hackerrank.com/domains/java",
     "Practice Java problems involving exceptions and packages."),

    ("Module 3 - Packages and Exceptions", "Advanced", "Documentation",
     "Java API Documentation",
     "https://docs.oracle.com/en/java/javase/",
     "Explore Java API packages, classes and exception documentation."),

    # MODULE 4 - MULTITHREADING AND JAVA I/O
    ("Module 4 - Multithreading and Java I/O", "Beginner", "Article",
     "Java Concurrency Tutorial",
     "https://docs.oracle.com/javase/tutorial/essential/concurrency/",
     "Understand threads, synchronization and concurrent programming."),

    ("Module 4 - Multithreading and Java I/O", "Intermediate", "Documentation",
     "Java Input and Output Tutorial",
     "https://docs.oracle.com/javase/tutorial/essential/io/",
     "Study byte streams, character streams and file operations."),

    ("Module 4 - Multithreading and Java I/O", "Advanced", "Practice",
     "Java Programming Challenges",
     "https://www.hackerrank.com/domains/java",
     "Practice Java programming with threads, strings and I/O concepts."),

    # MODULE 5 - JDBC NETWORKING AND GUI
    ("Module 5 - JDBC Networking and GUI", "Beginner", "Article",
     "JDBC Basics",
     "https://docs.oracle.com/javase/tutorial/jdbc/basics/",
     "Learn database connectivity, SQL statements and JDBC connections."),

    ("Module 5 - JDBC Networking and GUI", "Intermediate", "Documentation",
     "Java Networking Tutorial",
     "https://docs.oracle.com/javase/tutorial/networking/",
     "Understand URLs, networking concepts and socket programming."),

    ("Module 5 - JDBC Networking and GUI", "Advanced", "Documentation",
     "Java GUI and API Documentation",
     "https://docs.oracle.com/en/java/javase/",
     "Explore Java GUI libraries, AWT components and event handling.")
]

connection = sqlite3.connect(DB_PATH)

try:
    cursor = connection.cursor()

    inserted = 0
    skipped = 0

    for topic, level, resource_type, title, url, description in resources:

        cursor.execute("""
            INSERT OR IGNORE INTO learning_resources
            (subject, topic, level, resource_type, title, url, description)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            "Object Oriented Programming",
            topic,
            level,
            resource_type,
            title,
            url,
            description
        ))

        if cursor.rowcount == 1:
            inserted += 1
        else:
            skipped += 1

    connection.commit()

    print("OOP learning resources processed successfully!")
    print("New resources inserted:", inserted)
    print("Existing resources skipped:", skipped)

finally:
    connection.close()
