```python
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from src.database import Base

class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    teacher_id = Column(Integer, ForeignKey('teachers.id'), nullable=True)  # Added foreign key for Teacher

    teacher = relationship("Teacher", back_populates="courses")  # Establishing a relationship with Teacher model

# After changes, make sure to modify the Teacher model as well to establish the inverse relationship
class Teacher(Base):
    __tablename__ = 'teachers'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    courses = relationship("Course", back_populates="teacher")  # Establish relationship with courses
```