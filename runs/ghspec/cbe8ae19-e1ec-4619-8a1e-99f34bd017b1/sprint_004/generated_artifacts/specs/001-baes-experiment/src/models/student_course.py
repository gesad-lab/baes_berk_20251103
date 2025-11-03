from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

# Base class for SQLAlchemy models
Base = declarative_base()

class StudentCourses(Base):
    """
    Represents the association between students and courses in the database.

    Attributes:
        id (int): The unique identifier for the association (Primary Key).
        student_id (int): The identifier for the student (Foreign Key).
        course_id (int): The identifier for the course (Foreign Key).
    """

    __tablename__ = 'student_courses'  # Rename to fit the naming convention

    id = Column(Integer, primary_key=True)  # Unique ID for the association
    student_id = Column(Integer, ForeignKey('students.id'), nullable=False)  # Reference to students
    course_id = Column(Integer, ForeignKey('courses.id'), nullable=False)    # Reference to courses

    # Define relationships to access associated objects
    student = relationship('Student', back_populates='courses')  # Relationship to Student model
    course = relationship('Course', back_populates='students')    # Relationship to Course model

# Ensure that `Student` and `Course` models are updated with back_populates
# Example for Student model:
# class Student(Base):
#     ...
#     courses = relationship('StudentCourses', back_populates='student')

# Example for Course model:
# class Course(Base):
#     ...
#     students = relationship('StudentCourses', back_populates='course')