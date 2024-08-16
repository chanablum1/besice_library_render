from flask import Flask, render_template

app = Flask(__name__)

# רשימת ספרים לדוגמה
books = [
    {'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald', 'year': 1925},
    {'title': '1984', 'author': 'George Orwell', 'year': 1949},
    {'title': 'To Kill a Mockingbird', 'author': 'Harper Lee', 'year': 1960},
    {'title': 'Moby-Dick', 'author': 'Herman Melville', 'year': 1851},
]

# רשימת משתמשים לדוגמה
members = [
    {'name': 'John Doe', 'email': 'john.doe@example.com', 'join_date': '2024-08-01'},
    {'name': 'Jane Smith', 'email': 'jane.smith@example.com', 'join_date': '2024-08-05'},
    {'name': 'Alice Johnson', 'email': 'alice.j@example.com', 'join_date': '2024-08-10'},
]

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/books')
def book_list():
    return render_template('books.html', books=books)

@app.route('/members')
def member_list():
    return render_template('members.html', members=members)

if __name__ == '__main__':
    app.run(debug=True)
