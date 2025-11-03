from pydantic import BaseModel, Field

class EnrollStudent(BaseModel):
    """Schema for enrolling a student in a course."""
    
    course_id: int = Field(..., description="The ID of the course to enroll the student in.")
    
    class Config:
        schema_extra = {
            "example": {
                "course_id": 1
            }
        }