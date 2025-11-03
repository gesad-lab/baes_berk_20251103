```python
from app import db

class Teacher(db.Model):
    """Model representing a Teacher in the system."""
    __tablename__ = 'teachers'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    
    # Establish a relationship with the Course model
    courses = db.relationship("Course", back_populates="teacher")

class Course(db.Model):
    """Model representing a Course in the system, now includes teacher assignment."""
    __tablename__ = 'courses'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    teacher_id = db.Column(db.Integer, db.ForeignKey('teachers.id'), nullable=False)

    # Relationship to connect Course with Teacher
    teacher = db.relationship("Teacher", back_populates="courses")
```