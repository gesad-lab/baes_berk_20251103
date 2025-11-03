```python
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Enrollment(db.Model):
    """Model representing the many-to-many relationship between students and courses."""
    __tablename__ = 'enrollment'

    student_id = db.Column(db.Integer, db.ForeignKey('students.id'), primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'), primary_key=True)

    student = db.relationship('Student', back_populates='enrollments')
    course = db.relationship('Course', back_populates='enrolled_students')

class Student(db.Model):
    """Model representing a student."""
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key=True)
    # Other fields...

    enrollments = db.relationship('Enrollment', back_populates='student')

class Course(db.Model):
    """Model representing a course."""
    __tablename__ = 'courses'
    id = db.Column(db.Integer, primary_key=True)
    # Other fields...

    enrolled_students = db.relationship('Enrollment', back_populates='course')
```