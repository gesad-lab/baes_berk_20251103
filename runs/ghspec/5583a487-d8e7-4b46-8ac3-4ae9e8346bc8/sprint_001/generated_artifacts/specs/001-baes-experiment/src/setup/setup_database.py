import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

# Initialize Flask application
app = Flask(__name__)

# Configure SQLite database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Student model definition
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f'<Student {self.name}>'

def create_database():
    """
    Create the database and tables if they do not exist.
    This function is called at startup to ensure the schema is set up.
    """
    try:
        db.create_all()  # Create the database tables
    except IntegrityError as e:
        print(f"Error creating database: {e}")

if __name__ == '__main__':
    create_database()
    app.run(debug=True)  # Start the Flask application in debug mode