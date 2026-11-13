import sqlite3

DB_PATH = "database/ideathon2k26.db"
SUBJECT = "Object Oriented Programming"


questions = [

    # ================= MODULE 1: OOP FUNDAMENTALS =================

    # BEGINNER (4)
    (
        "Module 1 - OOP Fundamentals",
        "Which programming approach organizes programs around objects?",
        "Procedural programming",
        "Object-oriented programming",
        "Assembly programming",
        "Functional programming",
        "B",
        "Object-oriented programming organizes software around objects containing data and methods.",
        "Beginner"
    ),
    (
        "Module 1 - OOP Fundamentals",
        "Which keyword is used to define a class in Java?",
        "object",
        "define",
        "class",
        "struct",
        "C",
        "The class keyword declares a class in Java.",
        "Beginner"
    ),
    (
        "Module 1 - OOP Fundamentals",
        "An object is an instance of a:",
        "Method",
        "Class",
        "Package",
        "Interface",
        "B",
        "An object is created from a class and represents an instance of that class.",
        "Beginner"
    ),
    (
        "Module 1 - OOP Fundamentals",
        "Which OOP principle combines data and methods into a single unit?",
        "Inheritance",
        "Polymorphism",
        "Encapsulation",
        "Abstraction",
        "C",
        "Encapsulation bundles data and methods together and controls access to internal data.",
        "Beginner"
    ),

    # INTERMEDIATE (3)
    (
        "Module 1 - OOP Fundamentals",
        "Which access modifier makes a Java member accessible only within its declaring class?",
        "public",
        "protected",
        "private",
        "default",
        "C",
        "A private member can be accessed directly only from within its declaring class.",
        "Intermediate"
    ),
    (
        "Module 1 - OOP Fundamentals",
        "What is the main purpose of a constructor in Java?",
        "To destroy an object",
        "To initialize an object",
        "To import a package",
        "To override every method",
        "B",
        "A constructor initializes a newly created object.",
        "Intermediate"
    ),
    (
        "Module 1 - OOP Fundamentals",
        "What happens when a Java class has no explicitly declared constructor?",
        "The compiler supplies a default constructor",
        "The class cannot be instantiated",
        "The class becomes abstract",
        "Every field becomes private",
        "A",
        "If no constructor is declared, Java provides a default no-argument constructor.",
        "Intermediate"
    ),

    # ADVANCED (3)
    (
        "Module 1 - OOP Fundamentals",
        "What is the output of this Java code? int x = 5; System.out.println(x++ + ++x);",
        "11",
        "12",
        "13",
        "Compilation error",
        "B",
        "Post-increment contributes 5 and changes x to 6. Pre-increment changes it to 7 and contributes 7. The sum is 12.",
        "Advanced"
    ),
    (
        "Module 1 - OOP Fundamentals",
        "Which statement about Java objects is correct?",
        "Every object must be created using new",
        "Objects can contain state and behavior",
        "Objects cannot call methods",
        "An object is always a primitive value",
        "B",
        "Objects represent state through fields and behavior through methods. Some objects can also be created without an explicit new expression.",
        "Advanced"
    ),
    (
        "Module 1 - OOP Fundamentals",
        "What is method overloading in Java?",
        "Defining methods with the same name but different parameter lists",
        "Defining methods only in subclasses",
        "Changing a method's access modifier only",
        "Defining two methods with identical signatures",
        "A",
        "Overloaded methods share a name but differ in their parameter lists.",
        "Advanced"
    ),

    # ================= MODULE 2: INHERITANCE AND POLYMORPHISM =================

    # BEGINNER (4)
    (
        "Module 2 - Inheritance and Polymorphism",
        "Which keyword is used for class inheritance in Java?",
        "implements",
        "extends",
        "inherits",
        "super",
        "B",
        "The extends keyword allows a class to inherit from another class.",
        "Beginner"
    ),
    (
        "Module 2 - Inheritance and Polymorphism",
        "Which keyword refers to the current object in Java?",
        "super",
        "this",
        "static",
        "final",
        "B",
        "The this keyword refers to the current object.",
        "Beginner"
    ),
    (
        "Module 2 - Inheritance and Polymorphism",
        "Which keyword refers to the immediate parent-class portion of an object?",
        "this",
        "super",
        "final",
        "new",
        "B",
        "The super keyword is used to access superclass members and constructors.",
        "Beginner"
    ),
    (
        "Module 2 - Inheritance and Polymorphism",
        "Which OOP concept allows one interface or reference to represent different object types?",
        "Encapsulation",
        "Polymorphism",
        "Compilation",
        "Serialization",
        "B",
        "Polymorphism allows a common reference or interface to represent objects of different types.",
        "Beginner"
    ),

    # INTERMEDIATE (3)
    (
        "Module 2 - Inheritance and Polymorphism",
        "Which annotation indicates that a method is intended to override a superclass method?",
        "@Static",
        "@Override",
        "@Inherited",
        "@Super",
        "B",
        "@Override helps the compiler verify that a method correctly overrides an inherited method.",
        "Intermediate"
    ),
    (
        "Module 2 - Inheritance and Polymorphism",
        "Which type of polymorphism is achieved through method overloading?",
        "Runtime polymorphism",
        "Compile-time polymorphism",
        "Dynamic loading",
        "Data abstraction",
        "B",
        "Method overloading is resolved by the compiler using the method name and parameter list.",
        "Intermediate"
    ),
    (
        "Module 2 - Inheritance and Polymorphism",
        "Can a Java class directly extend more than one class?",
        "Yes, without restrictions",
        "Yes, using multiple extends keywords",
        "No, a class can directly extend only one class",
        "Only if both classes are abstract",
        "C",
        "Java does not support multiple inheritance of classes, although a class can implement multiple interfaces.",
        "Intermediate"
    ),

    # ADVANCED (3)
    (
        "Module 2 - Inheritance and Polymorphism",
        "What is printed? class A { void show(){System.out.print(\"A\");} } class B extends A { void show(){System.out.print(\"B\");} } A obj = new B(); obj.show();",
        "A",
        "B",
        "AB",
        "Compilation error",
        "B",
        "The overridden method is selected at runtime based on the actual object type, which is B.",
        "Advanced"
    ),
    (
        "Module 2 - Inheritance and Polymorphism",
        "Which statement about method overriding is correct?",
        "The overriding method must have a different name",
        "The overriding method must have a compatible return type",
        "Private methods are always overridden",
        "Static methods are dynamically overridden",
        "B",
        "An overriding method must have a compatible return type and cannot reduce the visibility of the inherited method.",
        "Advanced"
    ),
    (
        "Module 2 - Inheritance and Polymorphism",
        "What is the result of calling an overridden instance method through a superclass reference?",
        "The superclass version always runs",
        "The subclass version runs when the object is of the subclass",
        "Both versions always run automatically",
        "The program always fails to compile",
        "B",
        "Java uses dynamic method dispatch for overridden instance methods.",
        "Advanced"
    ),

    # ================= MODULE 3: PACKAGES AND EXCEPTIONS =================

    # BEGINNER (4)
    (
        "Module 3 - Packages and Exceptions",
        "Which keyword is used to create a package declaration in Java?",
        "import",
        "package",
        "namespace",
        "include",
        "B",
        "The package keyword declares the package to which a Java class belongs.",
        "Beginner"
    ),
    (
        "Module 3 - Packages and Exceptions",
        "Which block contains code that may generate an exception?",
        "catch",
        "finally",
        "try",
        "throw",
        "C",
        "The try block contains statements that may throw exceptions.",
        "Beginner"
    ),
    (
        "Module 3 - Packages and Exceptions",
        "Which block handles an exception thrown from a try block?",
        "catch",
        "final",
        "throws",
        "package",
        "A",
        "A catch block handles an exception of a matching type.",
        "Beginner"
    ),
    (
        "Module 3 - Packages and Exceptions",
        "Which keyword explicitly throws an exception?",
        "throws",
        "throw",
        "catch",
        "try",
        "B",
        "The throw keyword explicitly throws an exception object.",
        "Beginner"
    ),

    # INTERMEDIATE (3)
    (
        "Module 3 - Packages and Exceptions",
        "Which of these is an unchecked exception in Java?",
        "IOException",
        "SQLException",
        "ArithmeticException",
        "ClassNotFoundException",
        "C",
        "ArithmeticException is a RuntimeException and is therefore unchecked.",
        "Intermediate"
    ),
    (
        "Module 3 - Packages and Exceptions",
        "What is the purpose of the finally block?",
        "It declares a new class",
        "It contains cleanup code that normally executes after try/catch processing",
        "It creates an exception",
        "It replaces the catch block",
        "B",
        "The finally block normally executes after try/catch processing, including when an exception occurs.",
        "Intermediate"
    ),
    (
        "Module 3 - Packages and Exceptions",
        "Which keyword declares exceptions that a method may pass to its caller?",
        "throw",
        "throws",
        "catch",
        "finally",
        "B",
        "The throws clause declares exception types that a method may propagate.",
        "Intermediate"
    ),

    # ADVANCED (3)
    (
        "Module 3 - Packages and Exceptions",
        "What is printed? try { System.out.print(\"A\"); } finally { System.out.print(\"B\"); }",
        "A",
        "B",
        "AB",
        "Nothing",
        "C",
        "The try block prints A, and the finally block then prints B.",
        "Advanced"
    ),
    (
        "Module 3 - Packages and Exceptions",
        "Which exception category must normally be caught or declared when it is not otherwise handled?",
        "Unchecked exceptions",
        "Checked exceptions",
        "Errors only",
        "All RuntimeException subclasses",
        "B",
        "Checked exceptions are subject to Java's catch-or-declare requirement.",
        "Advanced"
    ),
    (
        "Module 3 - Packages and Exceptions",
        "When multiple catch blocks handle related exception types, which should generally appear first?",
        "The most general exception type",
        "The most specific exception type",
        "The Exception type always",
        "The Error type always",
        "B",
        "Specific exception handlers must precede broader handlers, otherwise the broader handler may make later handlers unreachable.",
        "Advanced"
    ),

    # ================= MODULE 4: THREADS, STRINGS AND JAVA I/O =================

    # BEGINNER (4)
    (
        "Module 4 - Multithreading and Java I/O",
        "What is a thread in Java?",
        "A lightweight unit of execution",
        "A database table",
        "A package name",
        "A file format",
        "A",
        "A thread is a lightweight unit of execution within a process.",
        "Beginner"
    ),
    (
        "Module 4 - Multithreading and Java I/O",
        "Which method contains the task performed by a thread when using the Thread class?",
        "start()",
        "run()",
        "stop()",
        "sleep()",
        "B",
        "The run method contains the code executed by a thread.",
        "Beginner"
    ),
    (
        "Module 4 - Multithreading and Java I/O",
        "Which Java class represents an immutable sequence of characters?",
        "String",
        "StringBuilder",
        "File",
        "Scanner",
        "A",
        "String objects are immutable, meaning their contents cannot be changed after creation.",
        "Beginner"
    ),
    (
        "Module 4 - Multithreading and Java I/O",
        "Which stream is primarily used to read bytes from an input source?",
        "OutputStream",
        "InputStream",
        "PrintWriter",
        "StringBuilder",
        "B",
        "InputStream is the base class for reading byte-oriented data.",
        "Beginner"
    ),

    # INTERMEDIATE (3)
    (
        "Module 4 - Multithreading and Java I/O",
        "Which method starts a new thread of execution?",
        "run()",
        "start()",
        "execute()",
        "begin()",
        "B",
        "Calling start() schedules a new thread and causes its run() method to execute.",
        "Intermediate"
    ),
    (
        "Module 4 - Multithreading and Java I/O",
        "Which keyword is commonly used to protect a critical section from simultaneous access by multiple threads?",
        "volatile",
        "synchronized",
        "transient",
        "native",
        "B",
        "The synchronized keyword provides mutual exclusion using an object's or class's monitor lock.",
        "Intermediate"
    ),
    (
        "Module 4 - Multithreading and Java I/O",
        "Which method causes the current thread to wait until another thread finishes?",
        "sleep()",
        "join()",
        "yield()",
        "notify()",
        "B",
        "The join method waits for the specified thread to terminate.",
        "Intermediate"
    ),

    # ADVANCED (3)
    (
        "Module 4 - Multithreading and Java I/O",
        "What happens when start() is called twice on the same Thread object?",
        "The thread starts twice",
        "The thread restarts from the beginning",
        "An IllegalThreadStateException is thrown",
        "The second call is ignored",
        "C",
        "A Java Thread object can be started only once. A subsequent start call throws IllegalThreadStateException.",
        "Advanced"
    ),
    (
        "Module 4 - Multithreading and Java I/O",
        "Which statement about StringBuilder is correct?",
        "It is immutable",
        "It is mutable and not synchronized",
        "It cannot append text",
        "It is always thread-safe",
        "B",
        "StringBuilder is mutable and generally not synchronized, making it suitable for many single-threaded string operations.",
        "Advanced"
    ),
    (
        "Module 4 - Multithreading and Java I/O",
        "Which Java mechanism can convert an object's state into a byte stream?",
        "Inheritance",
        "Serialization",
        "Method overloading",
        "Encapsulation",
        "B",
        "Serialization converts an object's state into a byte stream for storage or transmission.",
        "Advanced"
    ),

    # ================= MODULE 5: JDBC, NETWORKING AND GUI =================

    # BEGINNER (4)
    (
        "Module 5 - JDBC Networking and GUI",
        "What is the full form of JDBC?",
        "Java Database Connectivity",
        "Java Data Binary Connection",
        "Joint Database Class",
        "Java Data Control",
        "A",
        "JDBC stands for Java Database Connectivity and provides APIs for database access.",
        "Beginner"
    ),
    (
        "Module 5 - JDBC Networking and GUI",
        "Which JDBC interface represents a connection to a database?",
        "Statement",
        "Connection",
        "ResultSet",
        "Driver",
        "B",
        "The Connection interface represents a database connection.",
        "Beginner"
    ),
    (
        "Module 5 - JDBC Networking and GUI",
        "Which Java package contains the basic JDBC API?",
        "java.io",
        "java.net",
        "java.sql",
        "java.awt",
        "C",
        "The java.sql package contains core JDBC interfaces and classes.",
        "Beginner"
    ),
    (
        "Module 5 - JDBC Networking and GUI",
        "Which Java package provides classes for basic graphical user interface components?",
        "java.awt",
        "java.sql",
        "java.io",
        "java.lang",
        "A",
        "The java.awt package provides GUI components, graphics and event-handling support.",
        "Beginner"
    ),

    # INTERMEDIATE (3)
    (
        "Module 5 - JDBC Networking and GUI",
        "Which JDBC interface is commonly used to execute parameterized SQL statements?",
        "PreparedStatement",
        "ResultSet",
        "Connection",
        "DatabaseMetaData",
        "A",
        "PreparedStatement supports parameterized SQL and helps prevent SQL injection when parameters are used correctly.",
        "Intermediate"
    ),
    (
        "Module 5 - JDBC Networking and GUI",
        "Which Java class is commonly used to create a TCP server socket?",
        "Socket",
        "ServerSocket",
        "DatagramSocket",
        "URL",
        "B",
        "ServerSocket listens for incoming TCP connection requests.",
        "Intermediate"
    ),
    (
        "Module 5 - JDBC Networking and GUI",
        "Which layout manager arranges components in five regions: North, South, East, West and Center?",
        "FlowLayout",
        "GridLayout",
        "BorderLayout",
        "CardLayout",
        "C",
        "BorderLayout divides a container into five regions.",
        "Intermediate"
    ),

    # ADVANCED (3)
    (
        "Module 5 - JDBC Networking and GUI",
        "Which JDBC method is commonly used to execute a SELECT query and obtain rows?",
        "executeUpdate()",
        "executeQuery()",
        "commit()",
        "close()",
        "B",
        "executeQuery() executes a query that returns a ResultSet, commonly a SELECT statement.",
        "Advanced"
    ),
    (
        "Module 5 - JDBC Networking and GUI",
        "Which statement about TCP sockets in Java is correct?",
        "ServerSocket is normally used by a server to accept connections",
        "ServerSocket is used only for UDP communication",
        "Socket cannot communicate over a network",
        "TCP does not provide a connection-oriented service",
        "A",
        "A server uses ServerSocket to listen for and accept TCP connections, while Socket represents an endpoint of a connection.",
        "Advanced"
    ),
    (
        "Module 5 - JDBC Networking and GUI",
        "In Java event handling, which object typically receives and responds to an event?",
        "Event listener",
        "Layout manager",
        "Database driver",
        "Thread scheduler",
        "A",
        "An event listener receives notifications and performs the appropriate response to an event.",
        "Advanced"
    )
]

connection = sqlite3.connect(DB_PATH)
cursor = connection.cursor()

inserted = 0
skipped = 0

for question in questions:
    topic = question[0]
    question_text = question[1]

    cursor.execute("""
        SELECT 1
        FROM quiz_questions
        WHERE subject = ?
        AND topic = ?
        AND question = ?
    """, (SUBJECT, topic, question_text))

    if cursor.fetchone():
        skipped += 1
        continue

    cursor.execute("""
        INSERT INTO quiz_questions (
            subject,
            topic,
            question,
            option_a,
            option_b,
            option_c,
            option_d,
            correct_answer,
            explanation,
            difficulty
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (SUBJECT,) + question)

    inserted += 1

connection.commit()
connection.close()

print("OOP questions processed successfully!")
print("New questions inserted:", inserted)
print("Duplicate questions skipped:", skipped)
print("Total questions prepared:", len(questions))
