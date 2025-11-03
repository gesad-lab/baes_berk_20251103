```python
# src/models.py

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Student(db.Model):
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    courses = db.relationship('Course', secondary='student_courses', lazy='dynamic')

class Course(db.Model):
    __tablename__ = 'courses'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

class StudentCourses(db.Model):
    """
    Association table for many-to-many relationship between Student and Course.
    It establishes the link between students and the courses they are enrolled in.
    """
    __tablename__ = 'student_courses'
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'), primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'), primary_key=True)

    # Define relationships for easy access if needed
    student = db.relationship('Student', back_populates='courses')
    course = db.relationship('Course')

# Functionality to create database tables
def create_tables():
    db.create_all()
```
