```python
# models.py

from sqlalchemy import Column, Integer, String
from api import db

class Student(db.Model):
    """Model representing a student."""
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)

class Course(db.Model):
    """Model representing a course."""
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)  # Required field
    level = Column(String, nullable=False)  # Required field

    def __repr__(self):
        return f"<Course id={self.id} name={self.name} level={self.level}>"

# Ensure database migration does not affect existing Student data.
# The new 'Course' model is independently defined and allows migration scripts to
# create the courses table without altering any existing student records.
```