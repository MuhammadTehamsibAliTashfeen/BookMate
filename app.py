from flask import Flask
import sqlite3

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home_page():
    return 'Welcome to Book Mate'

@app.route('/add')
def add_Book():
    return 'Here we will add Books'


if __name__ == '__main__':
    app.run()

