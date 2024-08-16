import sqlite3
from datetime import datetime, timedelta

# יצירת חיבור למסד הנתונים
conn = sqlite3.connect('library.db')
cursor = conn.cursor()

# יצירת טבלת members
cursor.execute('''
    CREATE TABLE IF NOT EXISTS members (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        phone TEXT,
        address TEXT,
        join_date DATE NOT NULL
    )
''')

# יצירת טבלת books
cursor.execute('''
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        author TEXT NOT NULL,
        isbn TEXT NOT NULL UNIQUE,
        published_year INTEGER,
        category TEXT,
        available_copies INTEGER NOT NULL
    )
''')

# יצירת טבלת loans
cursor.execute('''
    CREATE TABLE IF NOT EXISTS loans (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        book_id INTEGER NOT NULL,
        member_id INTEGER NOT NULL,
        loan_date DATE NOT NULL,
        due_date DATE NOT NULL,
        return_date DATE,
        FOREIGN KEY (book_id) REFERENCES books(id),
        FOREIGN KEY (member_id) REFERENCES members(id)
    )
''')

# הכנסת נתונים לדוגמה לטבלת members
cursor.executemany('''
    INSERT INTO members (name, email, phone, address, join_date) 
    VALUES (?, ?, ?, ?, ?)
''', [
    ('John Doe', 'john.doe@example.com', '555-1234', '123 Elm St', '2024-08-01'),
    ('Jane Smith', 'jane.smith@example.com', '555-5678', '456 Oak St', '2024-08-05'),
    ('Alice Johnson', 'alice.j@example.com', '555-8765', '789 Maple St', '2024-08-10')
])

# הכנסת נתונים לדוגמה לטבלת books
cursor.executemany('''
    INSERT INTO books (title, author, isbn, published_year, category, available_copies)
    VALUES (?, ?, ?, ?, ?, ?)
''', [
    ('The Great Gatsby', 'F. Scott Fitzgerald', '9780743273565', 1925, 'Fiction', 3),
    ('1984', 'George Orwell', '9780451524935', 1949, 'Dystopian', 2),
    ('To Kill a Mockingbird', 'Harper Lee', '9780060935467', 1960, 'Fiction', 4)
])

# הכנסת נתונים לדוגמה לטבלת loans
loan_date = datetime.now()
due_date = loan_date + timedelta(days=10)

cursor.executemany('''
    INSERT INTO loans (book_id, member_id, loan_date, due_date, return_date)
    VALUES (?, ?, ?, ?, ?)
''', [
    (1, 1, loan_date.date(), due_date.date(), None),  # השאלה של ספר 1 על ידי משתמש 1
    (2, 2, loan_date.date(), due_date.date(), None),  # השאלה של ספר 2 על ידי משתמש 2
    (3, 1, loan_date.date(), due_date.date(), None)   # השאלה של ספר 3 על ידי משתמש 1
])

# שמירת השינויים וסגירת החיבור
conn.commit()
conn.close()

print("Database created and sample data inserted successfully.")
