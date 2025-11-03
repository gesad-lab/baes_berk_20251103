```python
# src/models/course.py

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Define the base class for declarative models
Base = declarative_base()

class Course(Base):
    """Represents a course entity in the database."""
    
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    level = Column(String, nullable=False)

    def __repr__(self):
        """Return a string representation of the Course instance."""
        return f"<Course(id={self.id}, name={self.name}, level={self.level})>"

    def to_dict(self):
        """Convert the Course instance to a dictionary for easy serialization."""
        return {
            "id": self.id,
            "name": self.name,
            "level": self.level
        }
```