```python
# Course and Teacher models
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from src.database import Base  # Assuming your base declarative class is in src/database.py

class Course(Base):
    """Represents a course in the educational system, linked to a specific teacher."""
    
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    description = Column(String(255), nullable=True)
    teacher_id = Column(Integer, ForeignKey('teachers.id'), nullable=True)

    teacher = relationship('Teacher', backref='courses')

    def __repr__(self):
        # String representation of the Course instance
        return f'<Course {self.name}>'
```