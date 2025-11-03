```python
# migrations/versions/{timestamp}_add_course_relationship.py

from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.services.course_service import Course
from app.services.student_service import Student
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Additional Migration to add a foreign key relationship from Student to Course
class StudentCourse(Base):
    __tablename__ = 'student_courses'
    
    student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
    course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)

    student = relationship("Student", back_populates="courses")
    course = relationship("Course", back_populates="students")

# Update Student model to include a relationship to courses
class Student(Base):
    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)

    courses = relationship("StudentCourse", back_populates="student")

# Update Course model to include a relationship to students
class Course(Base):
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    level = Column(String, nullable=False)

    students = relationship("StudentCourse", back_populates="course")

# Function to execute migration logic
def upgrade():
    # Execute the necessary SQL commands to add relationships
    pass  # Implement migration logic here

def downgrade():
    # Logic to reverse the migration if necessary
    pass  # Implement migration roll-back logic here
```