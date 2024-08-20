import sqlite3
from datetime import datetime, timedelta

# יצירת חיבור למסד הנתונים
conn = sqlite3.connect('library.db')
cursor = conn.cursor()

# יצירת טבלת users
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL
    )
''')

# הכנסה של משתמשים לדוגמה
cursor.execute('''
    INSERT INTO users (username, email, password) VALUES (?, ?, ?)
''', ('testuser', 'test@example.com', 'password'))

# סגירת החיבור
conn.commit()
conn.close()

print("User table created and sample user inserted.")
