```python
# src/models/course.py

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base  # Assuming this is where the SQLAlchemy Base is defined

class Course(Base):
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, nullable=True)
    teacher_id = Column(Integer, ForeignKey('teachers.id'), nullable=True)  # New foreign key for Teacher

    # Define relationship to Teacher model (assuming it exists)
    teacher = relationship("Teacher", back_populates="courses")  # Assuming courses relationship is defined in Teacher model

    def __repr__(self):
        return f"<Course(id={self.id}, title={self.title}, teacher_id={self.teacher_id})>"
```
