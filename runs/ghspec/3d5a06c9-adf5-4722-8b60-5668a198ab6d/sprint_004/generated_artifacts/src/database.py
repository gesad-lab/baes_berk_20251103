```python
# src/database.py

from sqlalchemy import create_engine, Column, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

# Creating the base class for the SQLAlchemy models
Base = declarative_base()

# Define the Enrollment model that establishes the many-to-many relationship
class Enrollment(Base):
    __tablename__ = 'enrollments'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    student_id = Column(Integer, ForeignKey('students.id'), nullable=False)
    course_id = Column(Integer, ForeignKey('courses.id'), nullable=False)

    # Relationships to Student and Course
    student = relationship("Student", back_populates="enrollments")
    course = relationship("Course", back_populates="enrollments")

# Existing Student and Course Models should be adapted to include back_populates
class Student(Base):
    # Assuming other columns exist...
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String)  # For example
    
    # Relationship with enrollments
    enrollments = relationship("Enrollment", back_populates="student")

class Course(Base):
    # Assuming other columns exist...
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True)
    name = Column(String)  # For example

    # Relationship with enrollments
    enrollments = relationship("Enrollment", back_populates="course")

# SQLAlchemy database engine
DATABASE_URL = "sqlite:///./test.db"  # Replace with your actual database URL
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create all tables (including the new Enrollment table)
def init_db():
    Base.metadata.create_all(bind=engine)

# Call this function to initialize your database on application startup
init_db()
```