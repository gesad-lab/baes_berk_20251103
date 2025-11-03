from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Database model for Student
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

# Function to initialize the database and create the schema
def init_db():
    """Initialize the database and create the schema if it doesn't exist."""
    with app.app_context():
        db.create_all()  # Create database tables for all models

if __name__ == '__main__':
    init_db()  # Call the initialize function on startup
    app.run(debug=True)