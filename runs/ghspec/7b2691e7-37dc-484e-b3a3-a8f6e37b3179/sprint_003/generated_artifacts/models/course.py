```python
from extensions import db  # Assuming you use SQLAlchemy for database interaction
from sqlalchemy import Column, Integer, String

class Course(db.Model):
    """Course model to represent a course entity in the system."""
    
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True)  # Unique identifier for the course
    name = Column(String(100), nullable=False)  # Name of the course
    level = Column(String(50), nullable=False)  # Level of the course (e.g., beginner, intermediate, advanced)

    def __repr__(self):
        """Representation of the Course object."""
        return f"<Course(id={self.id}, name={self.name}, level={self.level})>"
```