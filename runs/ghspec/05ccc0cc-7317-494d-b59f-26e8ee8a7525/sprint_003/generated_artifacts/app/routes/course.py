```python
# app/schemas.py

from pydantic import BaseModel, Field

class CourseBase(BaseModel):
    """
    Base model for Course containing common attributes.
    """
    name: str = Field(..., description="The name of the course")
    level: str = Field(..., description="The level of the course")

class CourseCreate(CourseBase):
    """
    Model for creating a new Course.
    This includes the attributes necessary for course creation.
    """
    pass

class CourseRetrieve(CourseBase):
    """
    Model for retrieving a Course.
    This will be used to define the structure of the course data returned from the API.
    """
    id: int = Field(..., description="The unique identifier of the course")

    class Config:
        orm_mode = True  # Enables ORM mode to work with SQLAlchemy models
```