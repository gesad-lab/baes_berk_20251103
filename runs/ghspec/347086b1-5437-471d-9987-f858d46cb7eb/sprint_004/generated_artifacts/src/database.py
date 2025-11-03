```python
# src/database.py

from sqlalchemy import create_engine, Column, Integer, ForeignKey, Table
from sqlalchemy.orm import sessionmaker, relationship
from alembic import command
from alembic.config import Config
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = "sqlite:///./database.db"

# Base class for our models
Base = declarative_base()

# Association table for many-to-many relationship
student_courses = Table(
    'student_courses', Base.metadata,
    Column('student_id', Integer, ForeignKey('students.id'), primary_key=True),
    Column('course_id', Integer, ForeignKey('courses.id'), primary_key=True)
)

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    # Establish relationship with courses
    courses = relationship("Course", secondary=student_courses, back_populates="students")

class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    level = Column(String)

    # Establish relationship with students
    students = relationship("Student", secondary=student_courses, back_populates="courses")

# Set up the database engine and session
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    """Initialize the database and run migrations if available."""
    Base.metadata.create_all(bind=engine)  # Create all tables, including newly added ones
    alembic_cfg = Config("alembic.ini")
    command.upgrade(alembic_cfg, "head")  # Run migrations if available
```