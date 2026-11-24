
import sqlite3

DB_PATH = "database/ideathon2k26.db"

connection = sqlite3.connect(DB_PATH)
cursor = connection.cursor()

cursor.execute("""
    SELECT name
    FROM sqlite_master
    WHERE type = 'table'
    ORDER BY name
""")

tables = cursor.fetchall()

print("\n===== LEARNSMART AI DATABASE =====")

for (table_name,) in tables:
    print(f"\nTABLE: {table_name}")

    cursor.execute(f"PRAGMA table_info('{table_name}')")

    columns = cursor.fetchall()

    for column in columns:
        print("Column:", column[1], "| Type:", column[2])

connection.close()

print("\nDatabase inspection completed!")
