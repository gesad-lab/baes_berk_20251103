```python
# src/models/course.py

from flask_sqlalchemy import SQLAlchemy

# Initialize the database
db = SQLAlchemy()

class Course(db.Model):
    """Model representing a course in the database."""

    __tablename__ = 'courses'

    id = db.Column(db.Integer, primary_key=True)  # Automatically generated primary key
    name = db.Column(db.String, nullable=False)  # Required field
    level = db.Column(db.String, nullable=False)  # Required field

    def __init__(self, name: str, level: str):
        """Initialize a new Course instance.

        Args:
            name (str): The name of the course.
            level (str): The level of the course.

        Raises:
            ValueError: If the name or level is empty.
        """
        if not name:
            raise ValueError("Course name cannot be empty")
        if not level:
            raise ValueError("Course level cannot be empty")
        self.name = name
        self.level = level

    def __repr__(self):
        """Return a string representation of the Course instance."""
        return f"<Course id={self.id} name={self.name} level={self.level}>"
```