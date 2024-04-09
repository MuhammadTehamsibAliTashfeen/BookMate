from flask import Flask, render_template
import sqlite3

app = Flask(__name__)
db_local = 'library.db'


@app.route('/')
@app.route('/home')
def home_page():
    Users_info = query_users_details()
    return render_template('home.html', Users_info=Users_info)

@app.route('/add')
def add_Book():
    return 'Here we will add Books'


def query_users_details():
    connie = sqlite3.connect(db_local)
    c = connie.cursor()
    c.execute("""sumary_line
    SELECT * FROM Users
    """
    )
    Users_info = c.fetchall()
    return Users_info

if __name__ == '__main__':
    app.run()

