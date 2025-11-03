from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class StudentCourses(Base):
    __tablename__ = 'student_courses'

    id = Column(Integer, primary_key=True, autoincrement=True)  # Auto-incrementing ID for the association table
    student_id = Column(Integer, ForeignKey('students.id'), nullable=False)  # Foreign key referencing the Student model
    course_id = Column(Integer, ForeignKey('courses.id'), nullable=False)  # Foreign key referencing the Course model

    # Establishing relationships with Student and Course models
    student = relationship('Student', back_populates='courses')  # Link back to the Student model
    course = relationship('Course', back_populates='students')    # Link back to the Course model

# Note that the `Student` and `Course` classes must be defined elsewhere in the codebase with corresponding relationships:
# - Student should have a `courses` relationship
# - Course should have a `students` relationship

# Example placeholder for Student and Course models (these would normally be in models.py as well)
class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True, autoincrement=True)
    # Adding relationship for backref
    courses = relationship('StudentCourses', back_populates='student')

class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True, autoincrement=True)
    # Adding relationship for backref
    students = relationship('StudentCourses', back_populates='course')