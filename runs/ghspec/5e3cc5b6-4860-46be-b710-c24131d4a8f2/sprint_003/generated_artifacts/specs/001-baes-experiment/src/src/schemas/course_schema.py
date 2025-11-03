```python
from sqlalchemy import Column, Integer, String
from database.database import Base

class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, index=True)  # Unique identifier for the course
    name = Column(String, nullable=False)  # Name of the course, cannot be null
    level = Column(String, nullable=False)  # Level of the course, cannot be null

    def __repr__(self):
        return f"<Course(name={self.name}, level={self.level})>"
```