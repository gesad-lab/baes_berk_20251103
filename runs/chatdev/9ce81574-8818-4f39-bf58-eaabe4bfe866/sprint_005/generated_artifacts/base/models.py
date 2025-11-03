'''
Defines the SQLAlchemy models for the application entities.
'''
from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
# Association table for many-to-many relationship
student_courses = Table(
    'student_courses',
    Base.metadata,
    Column('student_id', Integer, ForeignKey('students.id'), primary_key=True),
    Column('course_id', Integer, ForeignKey('courses.id'), primary_key=True)
)
class Student(Base):
    '''
    SQLAlchemy model for the Student entity.
    Attributes:
    - id: int - The primary key for the student.
    - name: str - The name of the student.
    - email: str - The email of the student.
    - courses: list - The list of courses the student is enrolled in.
    '''
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    courses = relationship("Course", secondary=student_courses, back_populates="students")
class Course(Base):
    '''
    SQLAlchemy model for the Course entity.
    Attributes:
    - id: int - The primary key for the course.
    - name: str - The name of the course.
    - level: str - The level of the course.
    - students: list - The list of students enrolled in the course.
    '''
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    level = Column(String, nullable=False)
    students = relationship("Student", secondary=student_courses, back_populates="courses")