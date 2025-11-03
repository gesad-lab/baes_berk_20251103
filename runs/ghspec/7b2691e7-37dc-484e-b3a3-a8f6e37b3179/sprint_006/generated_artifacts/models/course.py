```python
from extensions import db  # Assuming you use SQLAlchemy for database interaction
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

class Course(db.Model):
    """Course model representing courses in the educational management system."""
    
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, autoincrement=True)  # Unique identifier for the course
    teacher_id = Column(Integer, ForeignKey('teachers.id'), nullable=True)  # Foreign key to Teacher

    teacher = relationship("Teacher", back_populates="courses")  # Establish a relationship to Teacher

    # Include any additional fields and methods here as needed
```