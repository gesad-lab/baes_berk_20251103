```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Create a base class for declarative models
Base = declarative_base()

class Student(Base):
    """Student model for the students table."""

    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True, autoincrement=True)  # Unique identifier
    name = Column(String, nullable=False)  # Required name field for the student

    def __repr__(self):
        """String representation of the Student object."""
        return f"<Student(id={self.id}, name={self.name})>"
```