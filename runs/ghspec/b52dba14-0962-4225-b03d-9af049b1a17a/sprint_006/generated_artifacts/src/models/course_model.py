```python
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from src.database import Base

class Course(Base):
    """ Course model representing a course in the student management system. """
    
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    teacher_id = Column(Integer, ForeignKey('teachers.id'), nullable=True)

    # Relationship to Teacher model
    teacher = relationship("Teacher", back_populates="courses")

    def __repr__(self):
        return f"<Course(id={self.id}, name={self.name}, teacher_id={self.teacher_id})>"


class Teacher(Base):
    """ Teacher model representing a teacher in the student management system. """
    
    __tablename__ = 'teachers'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    courses = relationship("Course", back_populates="teacher")

    def __repr__(self):
        return f"<Teacher(id={self.id}, name={self.name})>"
```