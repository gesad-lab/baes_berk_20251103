```python
from sqlalchemy import Column, Integer, ForeignKey, Table
from sqlalchemy.orm import relationship
from src.database import Base

# Association Table for Enrollment between Student and Course
enrollment_table = Table('enrollment', Base.metadata,
    Column('student_id', Integer, ForeignKey('students.id'), primary_key=True),
    Column('course_id', Integer, ForeignKey('courses.id'), primary_key=True)
)

class Enrollment(Base):
    """Enrollment model representing the relationship between Students and Courses."""
    
    __tablename__ = 'enrollment'

    # No additional columns are needed as this is a many-to-many relation
    student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
    course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)

    # Relationships
    student = relationship("Student", back_populates="enrollments")
    course = relationship("Course", back_populates="enrollments")

# In the Student model, we would add the following:
# enrollments = relationship("Enrollment", back_populates="student")

# In the Course model, we would add the following:
# enrollments = relationship("Enrollment", back_populates="course")

```