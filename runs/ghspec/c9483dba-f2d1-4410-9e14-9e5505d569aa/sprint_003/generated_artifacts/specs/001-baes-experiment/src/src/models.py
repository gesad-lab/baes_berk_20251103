```python
# src/models.py

from flask_sqlalchemy import SQLAlchemy

# Initialize the database
db = SQLAlchemy()

class Student(db.Model):
    """Model representing a student in the system."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

class Course(db.Model):
    """Model representing a course in the system."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)  # Course name, required field
    level = db.Column(db.String(50), nullable=False)  # Course level, required field

    def __repr__(self):
        return f'<Course {self.name} (Level: {self.level})>'
```