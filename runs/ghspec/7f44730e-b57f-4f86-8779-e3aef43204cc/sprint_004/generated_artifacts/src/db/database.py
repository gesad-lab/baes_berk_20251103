```python
# src/db/database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.student import Base as StudentBase
from models.course import Base as CourseBase
from models.student_courses import Base as StudentCourseBase

DATABASE_URL = "sqlite:///./students.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    """Initialize the database and create tables if they do not exist."""
    # Create tables if they do not exist
    StudentBase.metadata.create_all(bind=engine)  # Ensure Student table exists
    CourseBase.metadata.create_all(bind=engine)   # Ensure Course table exists
    StudentCourseBase.metadata.create_all(bind=engine)  # Ensure join table exists


# src/models/student_courses.py
from sqlalchemy import Column, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class StudentCourse(Base):
    """Model representing the association between students and courses."""
    
    __tablename__ = 'student_courses'

    student_id = Column(ForeignKey('students.id'), primary_key=True)
    course_id = Column(ForeignKey('courses.id'), primary_key=True)

    def __repr__(self):
        return f"<StudentCourse(student_id={self.student_id}, course_id={self.course_id})>"
```