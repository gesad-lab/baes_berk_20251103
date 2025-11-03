```python
from pydantic import BaseModel, Field
from typing import Optional

class CourseTeacherAssign(BaseModel):
    teacher_id: int = Field(..., description="The unique identifier for a Teacher associated with the Course")

class CourseResponse(BaseModel):
    course_id: int
    title: str
    description: str
    teacher: Optional[CourseTeacherAssign] = Field(None, description="Details of the Teacher assigned to the Course")

    class Config:
        orm_mode = True
```