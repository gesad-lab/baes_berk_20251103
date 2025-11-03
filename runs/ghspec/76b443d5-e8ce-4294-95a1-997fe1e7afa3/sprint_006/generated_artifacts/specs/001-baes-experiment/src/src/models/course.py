```python
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from src.database import Base

class Course(Base):
    __tablename__ = 'courses'

    # Existing fields...
    
    teacher_id = Column(Integer, ForeignKey('teachers.id'), nullable=True)
    # Relationship to Teacher model
    teacher = relationship("Teacher", back_populates="courses")

    def __repr__(self):
        return f"<Course(id={self.id}, name={self.name}, teacher_id={self.teacher_id})>"

# Note: Ensure that the Teacher model has a corresponding 'courses' relationship defined for bi-directional linkage.
```