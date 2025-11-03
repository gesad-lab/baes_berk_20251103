```python
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from src.database import Base

class Course(Base):
    """Represents a course in the student management system."""
    
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    
    # Add the teacher_id foreign key
    teacher_id = Column(Integer, ForeignKey('teachers.id'), nullable=True)  # Allowing nullable for existing courses
    
    # Establish relationship with Teacher model
    teacher = relationship("Teacher", back_populates="courses")
    
    def __repr__(self):
        return f"<Course(id={self.id}, name={self.name}, teacher_id={self.teacher_id})>"
```