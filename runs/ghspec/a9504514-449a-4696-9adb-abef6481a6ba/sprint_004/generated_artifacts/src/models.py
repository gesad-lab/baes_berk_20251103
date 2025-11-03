from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class StudentCourses(Base):
    __tablename__ = 'student_courses'

    student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
    course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)

    student = relationship("Student", back_populates="courses")
    course = relationship("Course", back_populates="students")

# Extend the existing Student and Course models to have relationships
Student.courses = relationship("StudentCourses", back_populates="student")
Course.students = relationship("StudentCourses", back_populates="course")