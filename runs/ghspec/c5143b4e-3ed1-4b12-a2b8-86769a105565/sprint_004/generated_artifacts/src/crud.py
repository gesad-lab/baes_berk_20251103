```python
from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Junction table definition for the many-to-many relationship between students and courses
student_courses = Table(
    'student_courses', Base.metadata,
    Column('student_id', ForeignKey('students.id'), primary_key=True, nullable=False),
    Column('course_id', ForeignKey('courses.id'), primary_key=True, nullable=False)
)

class Student(Base):
    __tablename__ = 'students'

    id = Column(String, primary_key=True, index=True)
    name = Column(String, nullable=False)
    # Establishing relationship to courses through the junction table
    courses = relationship(
        'Course',
        secondary=student_courses,
        back_populates='students'
    )

class Course(Base):
    __tablename__ = 'courses'

    id = Column(String, primary_key=True, index=True)
    name = Column(String, nullable=False)
    level = Column(String, nullable=False)
    # Establishing relationship to students through the junction table
    students = relationship(
        'Student',
        secondary=student_courses,
        back_populates='courses'
    )
```