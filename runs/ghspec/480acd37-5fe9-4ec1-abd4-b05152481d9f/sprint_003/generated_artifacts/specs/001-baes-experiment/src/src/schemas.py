```python
from pydantic import BaseModel, Field, constr


class CourseCreate(BaseModel):
    """Schema for creating a new course."""
    name: constr(min_length=1, max_length=255) = Field(..., description="The name of the course.")
    level: constr(min_length=1, max_length=50) = Field(..., description="The level of the course.")


class CourseUpdate(BaseModel):
    """Schema for updating an existing course."""
    name: constr(min_length=1, max_length=255) = Field(None, description="The name of the course.")
    level: constr(min_length=1, max_length=50) = Field(None, description="The level of the course.")


class CourseOut(BaseModel):
    """Schema for returning course data after creation or retrieval."""
    id: int
    name: str
    level: str

    class Config:
        orm_mode = True  # Enable ORM mode for compatibility with SQLAlchemy models
```