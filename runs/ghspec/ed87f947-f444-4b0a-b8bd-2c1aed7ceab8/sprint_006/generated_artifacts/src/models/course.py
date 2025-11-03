```python
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base  # Assuming there is a base model defined for SQLAlchemy

class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    
    # New field added to associate a teacher with the course
    teacher_id = Column(Integer, ForeignKey('teachers.id'), nullable=True)

    # Define relationship to Teacher model
    teacher = relationship("Teacher", back_populates="courses")

# Assuming the Teacher model has already been defined with courses relationship
```