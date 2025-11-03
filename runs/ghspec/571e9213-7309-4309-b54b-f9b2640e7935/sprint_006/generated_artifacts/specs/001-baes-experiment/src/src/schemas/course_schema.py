```python
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from models.base import Base  # Assuming your Base is defined here
from models.teacher import Teacher  # Importing the Teacher model

class Course(Base):
    __tablename__ = 'courses'
    
    # Existing columns here...
    
    teacher_id = Column(Integer, ForeignKey('teachers.id'), nullable=True)  # Adding teacher_id as a foreign key

    # Establishing a relationship with the Teacher model
    teacher = relationship("Teacher", back_populates="courses")  # Assuming back_populates is defined in the Teacher model

# In the Teacher model, you would typically include:
class Teacher(Base):
    __tablename__ = 'teachers'
    
    # Existing columns here...
    
    courses = relationship("Course", back_populates="teacher")  # Establishing inverse relationship if needed
```