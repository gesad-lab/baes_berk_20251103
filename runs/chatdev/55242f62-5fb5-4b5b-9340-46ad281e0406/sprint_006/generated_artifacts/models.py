'''
Database models for the application.
'''
from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
# Association table for the many-to-many relationship
student_courses = Table(
    'student_courses',
    Base.metadata,
    Column('student_id', Integer, ForeignKey('students.id'), primary_key=True),
    Column('course_id', Integer, ForeignKey('courses.id'), primary_key=True)
)
class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)  # Added email field
    courses = relationship("Course", secondary=student_courses, back_populates="students")
class Course(Base):
    __tablename__ = "courses"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)  # Course name
    level = Column(String, nullable=False)  # Course level
    teacher_id = Column(Integer, ForeignKey('teachers.id'), nullable=True)  # Make teacher_id nullable
    teacher = relationship("Teacher", back_populates="courses")  # Establish relationship
class Teacher(Base):
    __tablename__ = "teachers"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)  # Teacher name
    email = Column(String, nullable=False)  # Teacher email
    courses = relationship("Course", back_populates="teacher")  # Establish relationship