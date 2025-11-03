```python
from pydantic import BaseModel, Field
from typing import Optional

class CourseTeacherAssociation(BaseModel):
    course_id: int = Field(..., description="The identifier of the Course")
    teacher_id: int = Field(..., description="The identifier of the Teacher")

class CourseWithTeacherDetails(BaseModel):
    id: int
    name: str
    description: str
    teacher_id: Optional[int] = Field(None, description="The identifier of the assigned Teacher")
    teacher_name: Optional[str] = Field(None, description="The name of the assigned Teacher")

class UpdateTeacherForCourse(BaseModel):
    teacher_id: int = Field(..., description="The new identifier of the Teacher to be assigned to the Course")
```