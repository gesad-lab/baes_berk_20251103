```python
# migrations/add_courses_table.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import sys

# Initialize Flask application
app = Flask(__name__)

# Set configuration for SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students_management.db'
db = SQLAlchemy(app)

# Course model definition
class Course(db.Model):
    __tablename__ = 'courses'
    id = db.Column(db.Integer, primary_key=True)  # Auto-incremented primary key
    name = db.Column(db.String, nullable=False)    # Required name field
    level = db.Column(db.String, nullable=False)    # Required level field

def create_courses_table():
    """Create the courses table in the database if it doesn't exist."""
    with app.app_context():
        db.create_all()  # Create all tables
        print("Courses table created successfully.")

def main():
    """Ensure virtual environment is active and required libraries are installed."""
    try:
        # Import required libraries
        import flask
        import marshmallow
        import sqlite3
    except ImportError as e:
        print(f"Error: Required library is not installed. {e}")
        print("Please ensure that Flask, Marshmallow, and SQLite are installed in your virtual environment.")
        sys.exit(1)

    create_courses_table()

if __name__ == "__main__":
    main()
```