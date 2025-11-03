```python
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from src.database import Base

class StudentCourse(Base):
    """Mapping table to represent the many-to-many relationship between Student and Course."""

    __tablename__ = 'student_courses'

    student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
    course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)

    student = relationship("Student", back_populates="courses")
    course = relationship("Course", back_populates="students")
```

```python
# migrations/2023xxxx_create_student_courses_table.py

from sqlalchemy import create_engine, Column, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class StudentCourse(Base):
    """Mapping table to represent the many-to-many relationship between Student and Course."""
    __tablename__ = 'student_courses'

    student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
    course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)

def run_migration():
    """Run the migration to create the student_courses table."""
    engine = create_engine('your_database_url')  # Replace with your actual database URL
    Base.metadata.create_all(engine)

if __name__ == "__main__":
    run_migration()
```