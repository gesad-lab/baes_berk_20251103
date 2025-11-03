```python
# models/course.py

from app import db

class Course(db.Model):
    """
    Course entity model that maps to the courses table in the database.
    
    Attributes:
        id (int): Unique identifier for the course.
        name (str): The name of the course.
        level (str): The educational level of the course.
    """
    __tablename__ = 'courses'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    level = db.Column(db.String, nullable=False)

    def __init__(self, name: str, level: str) -> None:
        """
        Initialize a new Course instance.

        Parameters:
            name (str): The name of the course.
            level (str): The educational level of the course.
        """
        self.name = name
        self.level = level

    def __repr__(self) -> str:
        """Return a string representation of the Course instance."""
        return f'<Course {self.name} - Level: {self.level}>'
```