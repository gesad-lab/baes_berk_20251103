```python
from pydantic import BaseModel

class CourseCreate(BaseModel):
    """Model for creating a new course."""
    name: str  # Required: The name of the course
    level: str  # Required: The level of the course

class CourseResponse(BaseModel):
    """Model for the course response."""
    id: int  # The unique identifier of the course
    name: str  # The name of the course
    level: str  # The level of the course
```