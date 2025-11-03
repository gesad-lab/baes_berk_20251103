```python
# src/services.py

from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Course(Base):
    """Model representing an educational course in the system."""

    __tablename__ = 'courses'

    # Defining the columns for the Course model
    id = Column(Integer, primary_key=True, index=True)  # Primary key for the course
    name = Column(String, nullable=False)  # Course name (required)
    level = Column(String, nullable=False)  # Course level (required)

    def __repr__(self):
        """Provide a string representation of the Course object."""
        return f"<Course(name={self.name}, level={self.level})>"
```