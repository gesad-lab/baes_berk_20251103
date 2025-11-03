```python
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_script import Manager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Initialize migration and manager
migrate = Migrate(app, db)
manager = Manager(app)

# Import existing models after creating the `db` instance
from models import Student, Course  # Assuming models are defined in models.py

# Define the StudentCourse junction table
student_courses = db.Table('student_courses',
    db.Column('student_id', db.Integer, db.ForeignKey('student.id'), primary_key=True),
    db.Column('course_id', db.Integer, db.ForeignKey('course.id'), primary_key=True)
)

# Command to initialize the database
@manager.command
def db_init():
    """Initialize the database, creating tables and applying migrations."""
    db.create_all()  # Creates all tables, including the junction table
    print("Database initialized.")

if __name__ == "__main__":
    manager.run()
```