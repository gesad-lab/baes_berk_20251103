```python
# File: src/models.py

from sqlalchemy import Column, Integer, String
from database import Base  # Importing the Base from the database setup


class Course(Base):
    """SQLAlchemy model representing a Course entity."""
    
    __tablename__ = 'courses'  # Table name in the database

    id = Column(Integer, primary_key=True, index=True)  # Auto-incrementing primary key
    name = Column(String, nullable=False)  # Course name, cannot be null
    level = Column(String, nullable=False)  # Course level, cannot be null

    def __repr__(self):
        """Return a string representation of the Course instance."""
        return f"<Course(id={self.id}, name='{self.name}', level='{self.level}')>"
```