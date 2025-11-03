```python
from pydantic import BaseModel, constr

class CourseCreate(BaseModel):
    """Schema for creating a new course."""
    name: constr(min_length=1)  # Ensure name is a non-empty string
    level: constr(min_length=1)  # Ensure level is a non-empty string

class CourseResponse(BaseModel):
    """Schema for returning course details."""
    id: int
    name: str
    level: str
    
    class Config:
        orm_mode = True  # Enable ORM mode for compatibility with SQLAlchemy models
```