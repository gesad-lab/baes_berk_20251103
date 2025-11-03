```python
from pydantic import BaseModel, Field
from typing import Optional

class CourseBase(BaseModel):
    name: str = Field(..., example="Mathematics 101")
    level: str = Field(..., example="Beginner")

class CourseCreate(CourseBase):
    pass

class CourseUpdate(CourseBase):
    teacher_id: Optional[int] = Field(None, example=1)  # Optional teacher ID for course updates

class CourseInDB(CourseBase):
    id: int
    teacher_id: Optional[int] = None  # Include teacher_id in the database response

    class Config:
        orm_mode = True  # Allow the model to work with ORM objects
```