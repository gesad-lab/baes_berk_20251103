# src/models/course.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base  # Assuming there's a base class for models

class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    level = Column(String, nullable=False)
    teacher_id = Column(Integer, ForeignKey('teachers.id'), nullable=True)  # new field for teacher reference

    # Relationship to the Teacher
    teacher = relationship("Teacher", back_populates="courses")

# Modification in Teacher model to accommodate this relationship
# Ensure that the Teacher model in src/models/teacher.py is updated as follows:
class Teacher(Base):
    __tablename__ = 'teachers'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)

    # Relationship to access courses taught by the teacher
    courses = relationship("Course", back_populates="teacher")  # existing code

    def __repr__(self):
        return f"<Teacher(name={self.name}, email={self.email})>"  # Add a representation for better logging/debugging

# Make sure to maintain existing imports and class definitions so that this modification is seamless.