```python
from sqlalchemy import Column, Integer, String
from src.database import Base

class Course(Base):
    """Course model representing the course structure within the application."""
    
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)  # Course name
    level = Column(String, nullable=False)  # Course level

    def __repr__(self):
        return f"<Course(id={self.id}, name={self.name}, level={self.level})>"
```