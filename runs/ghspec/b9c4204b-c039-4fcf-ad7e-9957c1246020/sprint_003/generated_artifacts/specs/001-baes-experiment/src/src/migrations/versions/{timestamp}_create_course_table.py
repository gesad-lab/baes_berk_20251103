```python
"""create_course_table.py

This migration file creates the Course table in the database.

The Course table will store course entities with their names and levels.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    level = Column(String, nullable=False)

    def __repr__(self):
        return f"<Course(name='{self.name}', level='{self.level}')>"

# Note: Add any additional migration logic or constraints below if necessary
```