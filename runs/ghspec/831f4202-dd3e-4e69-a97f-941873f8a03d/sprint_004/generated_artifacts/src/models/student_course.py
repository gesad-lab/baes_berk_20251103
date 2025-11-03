```python
from sqlalchemy import create_engine, Column, ForeignKey, Integer, Table, MetaData
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class StudentCourse(Base):
    """Model representing the many-to-many relationship between students and courses."""

    __tablename__ = 'student_courses'

    student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
    course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)

    def __repr__(self):
        return f"<StudentCourse(student_id={self.student_id}, course_id={self.course_id})>"

def add_student_courses_table():
    """Create the student_courses junction table in the database."""
    engine = create_engine('sqlite:///app.db')
    Base.metadata.create_all(engine)  # Create the junction table
```