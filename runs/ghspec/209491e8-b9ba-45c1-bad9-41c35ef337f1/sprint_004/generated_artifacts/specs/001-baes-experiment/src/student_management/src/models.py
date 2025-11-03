from sqlalchemy import Column, Integer, ForeignKey, Table
from sqlalchemy.orm import relationship
from database import Base

# Association table for the many-to-many relationship between Student and Course
student_courses = Table(
    'student_courses',
    Base.metadata,
    Column('student_id', Integer, ForeignKey('students.id'), primary_key=True),
    Column('course_id', Integer, ForeignKey('courses.id'), primary_key=True)
)

class Student(Base):
    __tablename__ = 'students'

    # Existing fields
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    # Relationships
    courses = relationship('Course', secondary=student_courses, back_populates='students')

class Course(Base):
    __tablename__ = 'courses'

    # Existing fields
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    # Relationships
    students = relationship('Student', secondary=student_courses, back_populates='courses')