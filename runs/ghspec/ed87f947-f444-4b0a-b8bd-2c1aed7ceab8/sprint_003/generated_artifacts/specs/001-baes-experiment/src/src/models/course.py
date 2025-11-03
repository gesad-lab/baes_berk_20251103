```python
# src/models/course.py

from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declaration import declarative_base

# Define the base class for the SQLAlchemy models
Base = declarative_base()

class Course(Base):
    """Model representing a course in the educational system."""
    
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)  # Name of the course
    level = Column(String, nullable=False)  # Difficulty level of the course

    def __repr__(self):
        """Return a string representation of the Course object."""
        return f"<Course(id={self.id}, name='{self.name}', level='{self.level}')>"
    
    def validate(self):
        """Validate Course instance attributes for required fields."""
        if not self.name:
            raise ValueError("Course name is required.")
        if not self.level:
            raise ValueError("Course level is required.")
```