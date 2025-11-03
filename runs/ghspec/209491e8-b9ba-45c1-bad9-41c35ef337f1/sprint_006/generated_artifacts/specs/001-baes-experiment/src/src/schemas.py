from pydantic import BaseModel
from typing import Optional

class CourseResponse(BaseModel):
    id: int
    name: str
    description: str
    teacher_id: Optional[int]  # Add the teacher_id field to the response schema
    teacher_name: Optional[str]  # Field for the associated teacher's name

    class Config:
        orm_mode = True

class AssignTeacherResponse(BaseModel):
    message: str  # Confirmation message after assigning a teacher

# Additional schemas can be added as needed for other responses related to courses.