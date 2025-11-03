from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Course(Base):
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    # ... other fields ...
    teacher_id = Column(Integer, ForeignKey('teachers.id'), nullable=True)

    # Establishing a relationship with Teacher model
    teacher = relationship("Teacher", back_populates="courses") 

# Assuming the Teacher model is defined in the same project
class Teacher(Base):
    __tablename__ = 'teachers'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    # ... other fields ...
    
    # Back relationship to access courses for a teacher
    courses = relationship("Course", back_populates="teacher") 

# This allows for querying and accessing teacher assignments for courses
# and ensures referential integrity through proper foreign key constraints
