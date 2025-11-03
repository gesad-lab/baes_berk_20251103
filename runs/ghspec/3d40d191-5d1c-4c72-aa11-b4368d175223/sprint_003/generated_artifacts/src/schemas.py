```python
from pydantic import BaseModel, Field

class CourseCreate(BaseModel):
    """Pydantic schema for creating a new course."""
    name: str = Field(..., description="The name of the course, required.")
    level: str = Field(..., description="The level of the course, required.")

    class Config:
        schema_extra = {
            "example": {
                "name": "Introduction to Programming",
                "level": "Beginner"
            }
        }
```