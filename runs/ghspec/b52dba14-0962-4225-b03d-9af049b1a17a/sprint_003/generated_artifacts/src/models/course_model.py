```python
# src/models/course_model.py

from typing import Any, Dict

class Course:
    """Represents a course in the Student Management System."""

    def __init__(self, name: str, level: str) -> None:
        """
        Initializes a Course instance.

        Parameters:
            name (str): The name of the course.
            level (str): The educational level of the course.
        """
        self.name = name
        self.level = level

    def to_dict(self) -> Dict[str, Any]:
        """Converts the Course object to a dictionary format."""
        return {
            "name": self.name,
            "level": self.level,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Course':
        """
        Creates a Course instance from a dictionary.

        Parameters:
            data (Dict[str, Any]): Dictionary containing the course details.
        
        Returns:
            Course: A Course instance populated with the data.
        """
        if 'name' not in data or 'level' not in data:
            raise ValueError("Missing required fields: 'name' and 'level'")
        
        return cls(name=data['name'], level=data['level'])
```