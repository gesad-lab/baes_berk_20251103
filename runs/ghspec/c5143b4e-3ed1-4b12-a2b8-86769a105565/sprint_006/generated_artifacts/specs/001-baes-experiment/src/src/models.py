```python
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Course(Base):
    __tablename__ = 'courses'

    id = Column(String, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, nullable=True)
    teacher_id = Column(String, ForeignKey('teachers.id'), nullable=True)

    # Relationship to the Teacher model
    teacher = relationship("Teacher", back_populates="courses")

# NOTE: Make sure to update the Teacher model to include a back reference to Courses as well.
```