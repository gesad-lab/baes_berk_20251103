```python
from datetime import datetime
from api import db

class Course(db.Model):
    """Model representing a Course."""
    __tablename__ = 'courses'
    
    id = db.Column(db.Integer, primary_key=True)  # Auto-incremented primary key
    title = db.Column(db.String(100), nullable=False)  # Course title
    description = db.Column(db.String(255), nullable=True)  # Optional course description
    students = db.relationship('Enrollment', back_populates='course')  # Relationship to Enrollment

class Enrollment(db.Model):
    """Model representing an Enrollment, linking Students and Courses."""
    __tablename__ = 'enrollments'
    
    id = db.Column(db.Integer, primary_key=True)  # Auto-incremented primary key
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'), nullable=False)  # Foreign key to Student
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'), nullable=False)  # Foreign key to Course
    created_at = db.Column(db.DateTime, default=datetime.utcnow)  # Timestamp of enrollment

    student = db.relationship('Student', back_populates='enrollments')  # Relationship to Student
    course = db.relationship('Course', back_populates='students')  # Relationship to Course

# Update Student model to reflect the new relationship
class Student(db.Model):
    """Model representing a Student."""
    __tablename__ = 'students'
    
    id = db.Column(db.Integer, primary_key=True)  # Auto-incremented primary key
    name = db.Column(db.String(100), nullable=False)  # Required name field
    enrollments = db.relationship('Enrollment', back_populates='student')  # Relationship to Enrollment
    courses = db.relationship('Course', secondary='enrollments', back_populates='students')  # Many-to-many relationship
```