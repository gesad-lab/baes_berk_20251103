```python
# File: migrations/001_create_course_table.py

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Course(Base):
    """Course model representing courses in the database."""
    
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)  # Name of the course, required
    level = Column(String, nullable=False)  # Level of the course, required

def create_course_table():
    """Create the courses table in the database if it doesn't exist."""
    
    # Connect to the database (replace with actual database URL)
    engine = create_engine('sqlite:///database.db')
    Base.metadata.create_all(engine)  # Create all tables defined by Base

if __name__ == "__main__":
    create_course_table()
```