```python
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

# Define a base class for declarative models
Base = declarative_base()

class Course(Base):
    """Course model for managing educational courses."""
    
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)  # Mandatory field for the course name
    level = Column(String, nullable=False)  # Mandatory field for the course level
    
    def __repr__(self):
        return f"<Course(id={self.id}, name={self.name}, level={self.level})>"
```