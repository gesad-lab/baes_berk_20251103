```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Create a base class for declarative models
Base = declarative_base()

class Course(Base):
    """
    Course model to represent courses in the educational system.

    Attributes:
    - id (int): Unique identifier for the course.
    - name (str): The name of the course.
    - level (str): The educational level of the course (e.g., "beginner", "intermediate", "advanced").
    """
    __tablename__ = 'courses'  # Database table name
    id = Column(Integer, primary_key=True, autoincrement=True)  # Auto-incrementing primary key
    name = Column(String, nullable=False)  # Course name cannot be null
    level = Column(String, nullable=False)  # Course level cannot be null
```