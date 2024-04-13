from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Users(db.Model):
    __tablename__ = 'Users'
    UserID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(100), nullable=False)
    Email = db.Column(db.String(100), unique=True, nullable=False)
    Password = db.Column(db.String(100), nullable=False)
    UserType = db.Column(db.String(50), nullable=False)

class Books(db.Model):
    __tablename__ = 'Books'
    BookID = db.Column(db.Integer, primary_key=True)
    Title = db.Column(db.String(100), nullable=False)
    Author = db.Column(db.String(100), nullable=False)
    Genre = db.Column(db.String(50), nullable=False)
    ISBN = db.Column(db.String(50), unique=True, nullable=False)
    Status = db.Column(db.String(50), nullable=False)

class Borrowing(db.Model):
    __tablename__ = 'Borrowing'
    BorrowID = db.Column(db.Integer, primary_key=True)
    UserID = db.Column(db.Integer, db.ForeignKey('Users.UserID'), nullable=False)
    BookID = db.Column(db.Integer, db.ForeignKey('Books.BookID'), nullable=False)
    BorrowDate = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    ReturnDate = db.Column(db.DateTime, nullable=True)

class Events(db.Model):
    __tablename__ = 'Events'
    EventID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(100), nullable=False)
    Description = db.Column(db.String(255), nullable=False)
    Date = db.Column(db.DateTime, nullable=False)

@app.route('/users/create', methods=['GET', 'POST'])
def create_user():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']  # In a real app, make sure to hash passwords before storing them
        user_type = request.form['user_type']
        
        new_user = Users(Name=name, Email=email, Password=password, UserType=user_type)
        db.session.add(new_user)
        db.session.commit()
        
        return redirect(url_for('list_users'))
    return render_template('create_user.html')

@app.route('/users')
def list_users():
    users = Users.query.all()
    return render_template('list_users.html', users=users)


with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
