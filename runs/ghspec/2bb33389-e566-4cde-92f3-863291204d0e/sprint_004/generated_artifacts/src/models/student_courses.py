```python
from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship
from src.database import Base  # Assuming Base is defined in the database module

class StudentCourses(Base):
    """
    Represents the association between students and courses in a many-to-many relationship.
    
    Attributes:
        student_id (int): Foreign key referencing the id of the Student.
        course_id (int): Foreign key referencing the id of the Course.
    """
    
    __tablename__ = 'student_courses'
    
    student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)  # Link to Student
    course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)    # Link to Course

    # Relationship back to the Student model
    student = relationship("Student", back_populates="courses")  # A student can have multiple courses
    # Relationship back to the Course model
    course = relationship("Course", back_populates="students")   # A course can have multiple students
```