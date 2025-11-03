from pydantic import BaseModel, Field
from typing import Optional

class CourseUpdateRequest(BaseModel):
    """Model for updating a course with a teacher association."""
    teacher_id: int = Field(..., example=1)

class CourseResponse(BaseModel):
    """Model for the response containing course details."""
    id: int
    name: str
    level: str
    teacher_id: Optional[int] = Field(None, example=1)  # Optional field for teacher ID

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "name": "Mathematics",
                "level": "Intermediate",
                "teacher_id": 1
            }
        }