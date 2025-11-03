```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Create a base class for declarative class definitions
Base = declarative_base()

class Course(Base):
    """
    Represents a course in the academic catalog.

    Attributes:
        id (int): The primary key for the course.
        name (str): The name of the course.
        level (str): The educational level of the course.
    """
    
    __tablename__ = 'courses'  # Table name in the database

    # Define the columns in the courses table
    id = Column(Integer, primary_key=True, autoincrement=True)  # Auto-incrementing ID column
    name = Column(String, nullable=False)  # Required name field
    level = Column(String, nullable=False)  # Required level field
```