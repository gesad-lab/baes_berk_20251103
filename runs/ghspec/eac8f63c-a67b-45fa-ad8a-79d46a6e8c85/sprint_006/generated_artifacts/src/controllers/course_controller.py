```python
# src/models/course.py

from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Course(Base):
    __tablename__ = 'courses'

    id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    
    # New foreign key to associate with the Teacher model
    teacher_id = Column(String, ForeignKey('teachers.id'), nullable=True)
    
    # Establish a relationship with the Teacher model
    teacher = relationship('Teacher', back_populates='courses')

    def __init__(self, id: str, name: str, teacher_id: str = None):
        self.id = id
        self.name = name
        self.teacher_id = teacher_id

    def __repr__(self):
        return f"<Course(id='{self.id}', name='{self.name}', teacher_id='{self.teacher_id}')>"
```
