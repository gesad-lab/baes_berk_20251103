from pydantic import BaseModel, Field
from typing import List

class CourseEnrollment(BaseModel):
    """Model for enrolling a student in a course."""
    course_id: int = Field(..., example=101)

class EnrolledCoursesResponse(BaseModel):
    """Model for the response containing a list of courses a student is enrolled in."""
    courses: List[int]  # List of course IDs the student is enrolled in

    class Config:
        schema_extra = {
            "example": {
                "courses": [101, 102, 103]
            }
        }