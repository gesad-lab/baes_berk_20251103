```python
from sqlalchemy import Column, Integer, String
from src.database import Base

class Course(Base):
    """Course model representing a course entity."""

    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)  # The name of the course (required)
    level = Column(String, nullable=False)  # The level of the course (required)
```