```python
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

# Define the base model
Base = declarative_base()

class StudentCourse(Base):
    __tablename__ = 'student_courses'

    student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
    course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)

    # Establish relationships to the Student and Course models
    student = relationship('Student', back_populates='courses')
    course = relationship('Course', back_populates='students')

# Update Student model to define relationship with courses
from src.models.student import Student
Student.courses = relationship('StudentCourse', back_populates='student', cascade='all, delete, delete-orphan')

# Update Course model to define relationship with students
from src.models.course import Course
Course.students = relationship('StudentCourse', back_populates='course', cascade='all, delete, delete-orphan')

def migrate_student_course_table():
    """Function to execute the migration for student-course relationships."""
    # Step to create the student_courses table if it doesn't exist
    Base.metadata.create_all(bind=engine)

# Set up migration execution
if __name__ == "__main__":
    migrate_student_course_table()
```