```python
from pydantic import BaseModel

class CourseCreate(BaseModel):
    """
    Schema for creating a new course.

    Attributes:
        name (str): The name of the course.
        level (str): The level of the course.
    """
    name: str
    level: str

class CourseResponse(BaseModel):
    """
    Schema for representing a course response.

    Attributes:
        id (int): The unique identifier for the course.
        name (str): The name of the course.
        level (str): The level of the course.
    """
    id: int
    name: str
    level: str
```