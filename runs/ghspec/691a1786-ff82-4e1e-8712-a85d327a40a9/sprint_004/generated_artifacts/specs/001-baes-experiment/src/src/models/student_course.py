from sqlalchemy import Column, Integer, ForeignKey
from db.database import Base

class StudentCourse(Base):
    """
    This class represents the association between Students and Courses.

    Attributes:
        student_id (int): The ID of the student, which is a foreign key referencing the Student table.
        course_id (int): The ID of the course, which is a foreign key referencing the Course table.
    """
    __tablename__ = 'student_course'

    student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
    course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)

    def __repr__(self):
        return f"<StudentCourse(student_id={self.student_id}, course_id={self.course_id})>"