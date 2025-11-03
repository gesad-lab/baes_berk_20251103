```python
# src/database/database.py

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Create a base class for declarative models
Base = declarative_base()

# Existing Student model
class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    # Relationship to associate courses
    courses = relationship('StudentCourse', back_populates='student')

# Existing Course model
class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    # Relationship to associate students
    students = relationship('StudentCourse', back_populates='course')

# New StudentCourse model for Many-to-Many relationship
class StudentCourse(Base):
    __tablename__ = 'student_courses'

    student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
    course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)

    # Relationships to Student and Course
    student = relationship('Student', back_populates='courses')
    course = relationship('Course', back_populates='students')

# Database engine setup (update your connection string accordingly)
DATABASE_URL = "sqlite:///./test.db"  # Adjust for your actual database
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Create tables if they don't exist
def init_db():
    Base.metadata.create_all(bind=engine)

# Create a session for database operations
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Initialize database
if __name__ == "__main__":
    init_db()
```