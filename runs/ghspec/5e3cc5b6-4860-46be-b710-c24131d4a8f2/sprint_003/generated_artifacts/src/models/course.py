```python
"""
Course model definition for the application.

This module defines the Course entity, which includes fields for
course name and level. It leverages SQLAlchemy to interact
with the underlying database.

"""

from sqlalchemy import Column, String
from database.database import Base

class Course(Base):
    __tablename__ = 'courses'
    
    # Defining the `name` column for the course
    name = Column(String, nullable=False)  # String field, required
    # Defining the `level` column for the course
    level = Column(String, nullable=False)  # String field, required

    def __repr__(self):
        """Representation of the Course entity."""
        return f"<Course(name={self.name}, level={self.level})>"
```