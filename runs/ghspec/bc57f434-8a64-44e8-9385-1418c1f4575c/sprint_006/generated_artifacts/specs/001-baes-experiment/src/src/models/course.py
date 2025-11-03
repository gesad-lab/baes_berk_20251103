from pydantic import BaseModel, Field
from typing import Optional

class CourseUpdateRequest(BaseModel):
    teacher_id: Optional[int] = Field(None, title="Teacher ID", description="The ID of the teacher to associate with the course.")

class CourseResponse(BaseModel):
    id: int
    name: str
    description: Optional[str]
    teacher_id: Optional[int] = Field(None, title="Teacher ID", description="The ID of the teacher assigned to this course.")
    teacher_name: Optional[str] = Field(None, title="Teacher Name", description="The name of the teacher assigned to this course.")
    teacher_email: Optional[str] = Field(None, title="Teacher Email", description="The email of the teacher assigned to this course.")