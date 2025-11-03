from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)

class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)

class StudentCourse(Base):
    __tablename__ = 'student_course'

    student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
    course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)

    # Establish relationships
    student = relationship("Student", back_populates="courses")
    course = relationship("Course", back_populates="students")

# Update Student and Course classes to include relationships
Student.courses = relationship("StudentCourse", back_populates="student")
Course.students = relationship("StudentCourse", back_populates="course")

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def setup_database():
    """
    Setup the database and create all necessary tables
    including Student, Course, and StudentCourse.
    """
    Base.metadata.create_all(engine)  # Create all defined tables in the engine

if __name__ == "__main__":
    setup_database()  # Initialize the database when the script is run directly