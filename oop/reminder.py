import sqlite3

class MedicineReminder:
    def __init__(self, db_name='medicine.db'):
        self.conn = sqlite3.connect(db_name, check_same_thread=False)
        self.create_table()

    def create_table(self):
        with self.conn:
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS reminders (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    time TEXT NOT NULL,
                    email TEXT NOT NULL
                )
            ''')

    def add_reminder(self, name, time, email):
        with self.conn:
            self.conn.execute(
                'INSERT INTO reminders (name, time, email) VALUES (?, ?, ?)',
                (name, time.strip(), email.strip())
            )
        print(f"✅ Reminder saved: {name} at {time} for {email}")

    def get_all_reminders(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT name, time, email FROM reminders')
        return cursor.fetchall()
