```python
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base  # Assuming Base is defined in a database module

class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    level = Column(String, nullable=False)
    teacher_id = Column(Integer, ForeignKey('teachers.id'), nullable=True)  # New field

    # Establish relationship with Teacher
    teacher = relationship("Teacher", back_populates="courses")

# Assuming the Teacher model is also defined in the same module or imported appropriately
class Teacher(Base):
    __tablename__ = 'teachers'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)

    # Establish relationship with Course
    courses = relationship("Course", back_populates="teacher")
```