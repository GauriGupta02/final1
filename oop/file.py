import sqlite3
import os

print("Database path:", os.path.abspath("medicine.db"))

conn = sqlite3.connect("medicine.db")
cursor = conn.cursor()

# Show all tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print("Tables:", cursor.fetchall())

try:
    cursor.execute("SELECT * FROM reminders")
    rows = cursor.fetchall()
    print(f"Total rows found: {len(rows)}")
    for row in rows:
        print(row)
except Exception as e:
    print("Error during query:", e)

conn.close()

