```python
# src/models/course.py

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from src.database.database import Base

class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    teacher_id = Column(Integer, ForeignKey('teachers.id'), nullable=True)  # Add teacher_id field

    # Establish relationship with Teacher
    teacher = relationship("Teacher", back_populates="courses")

    def __repr__(self):
        return f"<Course(id={self.id}, name={self.name}, teacher_id={self.teacher_id})>"
```

In this modification:
- We've added the `teacher_id` field to the `Course` model to establish a foreign key relationship with the `Teacher` entity.
- The `teacher` relationship is defined to allow access to the associated teacher object when working with a course. 
- The `nullable=True` for the `teacher_id` field means that a course may exist without a teacher assigned, which aligns with potential initial states of courses before teachers are assigned.