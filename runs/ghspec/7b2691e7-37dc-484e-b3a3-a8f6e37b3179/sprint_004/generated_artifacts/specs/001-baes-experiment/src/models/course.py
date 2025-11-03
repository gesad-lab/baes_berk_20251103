from extensions import db  # Assuming you use SQLAlchemy for database interaction
from sqlalchemy import Column, Integer, String

class Course(db.Model):
    """Course model to represent a course entity in the system."""
    
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True)  # Unique identifier for the course
    name = Column(String(100), nullable=False)  # Name of the course
    level = Column(String(50), nullable=False)  # Level of the course (e.g., beginner, intermediate)

    # Establish a many-to-many relationship with the Student model through StudentCourses
    students = db.relationship('Student', secondary='student_courses', back_populates='courses')


# Define a junction table for the many-to-many relationship
class StudentCourses(db.Model):
    """Junction table to represent the many-to-many relationship between students and courses."""
    
    __tablename__ = 'student_courses'
    
    student_id = Column(Integer, db.ForeignKey('students.id'), primary_key=True)  # Link to Student
    course_id = Column(Integer, db.ForeignKey('courses.id'), primary_key=True)    # Link to Course

    # Optional: If you want to track additional information about the enrollment, add fields here
    # Example: enrollment_date = Column(DateTime, default=datetime.utcnow)
