```python
# src/models/teacher.py

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from base import Base  # Assuming there's a base class for models somewhere

class Teacher(Base):
    """Represents a teacher entity in the educational management system."""
    
    __tablename__ = 'teachers'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    subject = Column(String, nullable=False)
    
    # Back-reference to courses taught by the teacher
    courses = relationship("Course", back_populates="teacher")

    def __repr__(self):
        return f"<Teacher(id={self.id}, name={self.name}, subject={self.subject})>"

# Ensure to add the relationship in the Course model, which is done in `models/course.py`
```