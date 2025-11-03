```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Course(Base):
    """Course model representing a course in the educational system."""

    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)  # The name of the course
    level = Column(String, nullable=False)  # The level of the course (e.g., beginner, intermediate, advanced)

    def __repr__(self):
        return f"<Course(id={self.id}, name={self.name}, level={self.level})>"
```