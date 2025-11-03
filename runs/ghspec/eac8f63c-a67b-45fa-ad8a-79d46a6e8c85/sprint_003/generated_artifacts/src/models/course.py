```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Course(Base):
    """Course model representing the educational offerings."""
    
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True, autoincrement=True)  # Unique identifier
    name = Column(String, nullable=False)  # Course name, required field
    level = Column(String, nullable=False)  # Course level, required field

    def __repr__(self):
        return f"<Course(id={self.id}, name='{self.name}', level='{self.level}')>"
```