```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Course(Base):
    """Course model defines the structure for the courses in the database."""
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)  # Course name, required
    level = Column(String, nullable=False)  # Course level (e.g., Beginner, Intermediate), required

    def __repr__(self):
        """String representation of the Course model for debugging purposes."""
        return f"<Course(id={self.id}, name={self.name}, level={self.level})>"
```