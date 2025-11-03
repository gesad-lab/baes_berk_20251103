```python
# /src/models/course.py

from sqlalchemy import Column, Integer, String
from src.database import Base  # Adjusted import to match project structure

class Course(Base):
    """Course model for managing course details."""
    
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)  # Required Course name
    level = Column(String, nullable=False)  # Required Course level

    def __repr__(self):
        """String representation of the Course instance."""
        return f"<Course(id={self.id}, name={self.name}, level={self.level})>"
```