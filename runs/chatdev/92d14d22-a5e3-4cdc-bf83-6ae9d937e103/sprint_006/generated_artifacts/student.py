'''
Migration script to add Teacher table to the database.
'''
from sqlalchemy import create_engine, Column, String, Integer, Table, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
DATABASE_URL = "sqlite:///./students.db"
engine = create_engine(DATABASE_URL)
Base = declarative_base()
# Association table for the many-to-many relationship
student_courses = Table(
    'student_courses',
    Base.metadata,
    Column('student_id', Integer, ForeignKey('students.id'), primary_key=True),
    Column('course_id', Integer, ForeignKey('courses.id'), primary_key=True)
)
# Create the Course table
class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    level = Column(String, nullable=False)
    teacher_id = Column(Integer, ForeignKey('teachers.id'), nullable=True)  # Add this line
    students = relationship("Student", secondary=student_courses, back_populates="courses")
    teacher = relationship("Teacher", back_populates="courses")  # Add this line to establish the relationship
# Create the Teacher table
class Teacher(Base):
    __tablename__ = 'teachers'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    courses = relationship("Course", back_populates="teacher")  # Add this line
# Note: Do not call Base.metadata.create_all(bind=engine) here