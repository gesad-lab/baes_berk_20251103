```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Course(Base):
    """Represents a Course entity in the educational application.

    Attributes:
        id (int): The unique identifier for the course.
        name (str): The name of the course. This field is required.
        level (str): The educational level of the course. This field is required.
    """
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)  # Course name cannot be null
    level = Column(String, nullable=False)  # Course level cannot be null
```