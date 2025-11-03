```python
from sqlalchemy import Column, Integer, String
from src.database import Base  # Import the base class for the ORM

class Course(Base):
    """Represents a Course entity in the database."""
    
    __tablename__ = 'courses'  # Table name in the database

    id = Column(Integer, primary_key=True, autoincrement=True)  # Unique ID for each course
    name = Column(String, nullable=False)  # Course name, cannot be null
    level = Column(String, nullable=False)  # Course level, cannot be null

    def __repr__(self):
        """Return a string representation of the course."""
        return f'<Course(name={self.name}, level={self.level})>'
```