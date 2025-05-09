import sqlite3

DATABASE = 'reminders.db'

def init_db():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS reminders (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                dateTime TEXT NOT NULL,
                message TEXT NOT NULL,
                reminder_type TEXT CHECK(reminder_type IN ('sms', 'email')) NOT NULL
            )
        ''')
    conn.commit()

def save_reminder(dateTime, message, reminder_type):
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO reminders (dateTime, message, reminder_type)
            VALUES (?, ?, ?)
        ''', (dateTime, message, reminder_type))
        conn.commit()

def get_reminders():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM reminders')
        reminders = cursor.fetchall()
        return reminders