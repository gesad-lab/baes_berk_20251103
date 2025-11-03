```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Base class for all models
Base = declarative_base()

class Course(Base):
    """ORM model for Course, representing the courses table in the database."""
    
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, index=True)  # Auto-incremented ID
    name = Column(String, nullable=False)  # Course name must be provided
    level = Column(String, nullable=False)  # Course level must be provided

    def __repr__(self):
        return f"<Course(id={self.id}, name={self.name}, level={self.level})>"
```