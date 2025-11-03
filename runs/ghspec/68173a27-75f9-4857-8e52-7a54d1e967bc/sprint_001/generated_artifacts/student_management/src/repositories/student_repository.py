```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Create a base class for declarative models
Base = declarative_base()

class Student(Base):
    """Representation of a student entity."""

    __tablename__ = 'students'  # Define the table name

    id = Column(Integer, primary_key=True, autoincrement=True)  # Primary key auto-increment
    name = Column(String, nullable=False)  # Name is a required field

    def __repr__(self):
        """Return a string representation of the Student instance."""
        return f"<Student(id={self.id}, name='{self.name}')>"
```