```python
from sqlalchemy import Column, Integer, String
from src.db.database import Base

class Course(Base):
    """Course model represents a course entity in the database."""
    
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    level = Column(String, nullable=False)

    def __repr__(self):
        return f"<Course(id={self.id}, name={self.name}, level={self.level})>"
```