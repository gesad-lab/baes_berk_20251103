```python
from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from .base import Base  # Assuming Base is defined in a separate base.py module

class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)  # Required Field
    level = Column(String, nullable=False)  # Required Field
    teacher_id = Column(Integer, ForeignKey('teachers.id'), nullable=True)  # Nullable to allow courses without assigned teachers

    teacher = relationship("Teacher", back_populates="courses")  # Relationship to Teacher

    def __repr__(self):
        return f"<Course(id={self.id}, name={self.name}, level={self.level}, teacher_id={self.teacher_id})>"
```