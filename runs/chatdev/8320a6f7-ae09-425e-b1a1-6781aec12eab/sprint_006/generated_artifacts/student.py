'''
Defines the SQLAlchemy model for the Student entity.
'''
from sqlalchemy import create_engine, Column, Integer, String, Table, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
DATABASE_URL = "sqlite:///./students.db"
engine = create_engine(DATABASE_URL)
Base = declarative_base()
# Association table for the many-to-many relationship
student_course_association = Table(
    'student_course', Base.metadata,
    Column('student_id', Integer, ForeignKey('students.id')),
    Column('course_id', Integer, ForeignKey('courses.id'))
)
class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    courses = relationship("Course", secondary=student_course_association, back_populates="students")
class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    level = Column(String, nullable=False)
    teacher_id = Column(Integer, ForeignKey('teachers.id'))  # Added foreign key reference to Teacher
    students = relationship("Student", secondary=student_course_association, back_populates="courses")
    teacher = relationship("Teacher", back_populates="courses")  # Added relationship to Teacher