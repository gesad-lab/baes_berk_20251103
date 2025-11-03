```python
from pydantic import BaseModel, Field
from typing import List, Optional

class CourseCreate(BaseModel):
    """Schema for creating a new Course."""
    name: str = Field(..., title="Course Name", description="The name of the course.")
    level: str = Field(..., title="Course Level", description="The level of the course (e.g., Beginner, Intermediate).")

class CourseResponse(BaseModel):
    """Schema for representing a Course response."""
    id: int
    name: str
    level: str

    class Config:
        orm_mode = True  # Enables Pydantic to read data from SQLAlchemy models
```