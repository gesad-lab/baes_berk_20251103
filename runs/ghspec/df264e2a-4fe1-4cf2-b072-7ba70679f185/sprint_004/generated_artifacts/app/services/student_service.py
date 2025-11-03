```python
# app/services/student_service.py

from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Session
from fastapi import HTTPException

Base = declarative_base()

# Define the Student model (Assumed already exists)
class Student(Base):
    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    courses = relationship("Course", secondary="student_courses", back_populates="students")

# Define the Course model (Assumed already exists)
class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    level = Column(String, nullable=False)
    students = relationship("Student", secondary="student_courses", back_populates="courses")

# Define the association table for the many-to-many relationship
class StudentCourses(Base):
    __tablename__ = 'student_courses'
    
    student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
    course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)

    def __init__(self, student_id: int, course_id: int):
        self.student_id = student_id
        self.course_id = course_id

# Function to assign a student to a course
def assign_course_to_student(db: Session, student_id: int, course_id: int):
    # Check if student exists
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    
    # Check if course exists
    course = db.query(Course).filter(Course.id == course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")

    # Associate student with course
    student.courses.append(course)
    db.commit()
    return {"message": "Course assigned successfully"}

# Function to retrieve a student with their courses
def get_student_with_courses(db: Session, student_id: int):
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student
```