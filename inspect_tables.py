
import sqlite3

connection = sqlite3.connect("database/ideathon2k26.db")

tables = connection.execute("""
    SELECT name
    FROM sqlite_master
    WHERE type = 'table'
    AND name NOT LIKE 'sqlite_%'
""").fetchall()

for table in tables:
    table_name = table[0]

    print("\nTABLE:", table_name)

    result = connection.execute(
        "SELECT sql FROM sqlite_master WHERE type='table' AND name=?",
        (table_name,)
    ).fetchone()

    print(result[0] if result else "Table not found")

connection.close()
