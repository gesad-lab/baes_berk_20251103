'''
Database models for the application.
'''
from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
# Association table for the many-to-many relationship
student_courses = Table(
    'student_courses',
    Base.metadata,
    Column('student_id', Integer, ForeignKey('students.id'), primary_key=True),
    Column('course_id', Integer, ForeignKey('courses.id'), primary_key=True)
)
class Student(Base):
    '''
    Student model representing the students table in the database.
    '''
    __tablename__ = "students"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)  # Updated to be required
    courses = relationship("Course", secondary=student_courses, back_populates="students")
class Course(Base):
    '''
    Course model representing the courses table in the database.
    '''
    __tablename__ = "courses"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    level = Column(String, nullable=False)
    teacher_id = Column(Integer, ForeignKey('teachers.id'), nullable=True)  # Added teacher_id
    students = relationship("Student", secondary=student_courses, back_populates="courses")
    teacher = relationship("Teacher", back_populates="courses")  # Added relationship to Teacher
class Teacher(Base):
    '''
    Teacher model representing the teachers table in the database.
    '''
    __tablename__ = "teachers"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    courses = relationship("Course", back_populates="teacher")  # Added relationship to Course