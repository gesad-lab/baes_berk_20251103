```python
# File: src/schemas/course.py

from pydantic import BaseModel, Field
from typing import Optional

class CourseBase(BaseModel):
    name: str = Field(..., example="Mathematics 101")

class CourseCreate(CourseBase):
    teacher_id: Optional[int] = Field(None, example=1)

class Course(CourseBase):
    id: int
    teacher_id: Optional[int] = Field(None, example=1)  # Adding the teacher_id field

    class Config:
        orm_mode = True
```