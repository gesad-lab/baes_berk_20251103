```python
# src/models/course.py

class Course:
    """
    Course model representing the Course entity.

    Attributes:
        id (int): Primary key, auto-incremented for each course.
        name (str): Name of the course; a required field.
        level (str): Academic level of the course; a required field.
    """

    def __init__(self, id: int, name: str, level: str):
        """
        Initializes a new Course instance.

        :param id: Unique identifier for the course.
        :param name: The name of the course.
        :param level: The academic level of the course.
        """
        self.id = id  # Primary key
        self.name = name  # Required field
        self.level = level  # Required field

    def to_dict(self) -> dict:
        """
        Converts the Course instance to a dictionary format.

        :return: Dictionary representation of the Course.
        """
        return {
            "id": self.id,
            "name": self.name,
            "level": self.level
        }

    @classmethod
    def from_dict(cls, data: dict):
        """
        Creates a Course instance from a dictionary.

        :param data: Dictionary containing course data.
        :return: Course instance.
        """
        return cls(
            id=data.get("id"),
            name=data.get("name"),
            level=data.get("level")
        )
```