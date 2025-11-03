```python
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from src.database import Base

class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    
    # New teacher_id column as a foreign key reference
    teacher_id = Column(Integer, ForeignKey('teachers.id'), nullable=True)

    # Relationship to Teacher model. This allows access to the Teacher data from the Course instance.
    teacher = relationship("Teacher", back_populates="courses")

# Assuming Teacher model has the following structure
class Teacher(Base):
    __tablename__ = 'teachers'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    # Define a relationship to access courses assigned to this teacher
    courses = relationship("Course", back_populates="teacher")
```