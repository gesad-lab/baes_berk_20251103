```python
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base  # Assuming there's a base model for SQLAlchemy

class Course(Base):
    """Model representing a Course with an optional associated Teacher."""
    
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    description = Column(String)
    teacher_id = Column(Integer, ForeignKey('teachers.id'), nullable=True)  # Foreign key to Teacher

    # Relationship to the Teacher entity
    teacher = relationship("Teacher", back_populates="courses")

# Assuming there's a Teacher model defined somewhere
class Teacher(Base):
    """Model representing a Teacher with associated courses."""
    
    __tablename__ = 'teachers'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)

    # Relationship to associate courses with this teacher
    courses = relationship("Course", back_populates="teacher")
```