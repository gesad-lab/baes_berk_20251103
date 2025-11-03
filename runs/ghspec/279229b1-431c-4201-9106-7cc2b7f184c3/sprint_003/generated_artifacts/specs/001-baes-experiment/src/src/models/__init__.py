```python
# Existing import statements
from .student import Student
from .course import Course  # New Course import

class Course:
    """Represents a course in the educational system."""

    def __init__(self, id: int, name: str, level: str):
        """
        Initializes a new course instance.

        Args:
            id (int): The unique identifier for the course.
            name (str): The name of the course.
            level (str): The level of the course (e.g., beginner, intermediate, advanced).
        """
        self.id = id
        self.name = name
        self.level = level

    def __repr__(self):
        """Return a string representation of the Course instance."""
        return f'<Course id={self.id}, name="{self.name}", level="{self.level}">'
```