from pydantic import BaseModel, Field
from typing import List, Optional

class CourseBase(BaseModel):
    course_id: int = Field(..., example=101)
    course_name: str = Field(..., example="Introduction to Programming")

class EnrollStudentRequest(BaseModel):
    course_id: int = Field(..., example=101)

class StudentCoursesResponse(BaseModel):
    student_id: int = Field(..., example=1)
    courses: List[CourseBase] = []

class ErrorResponse(BaseModel):
    error_code: str
    message: str
    details: Optional[dict] = None

# Example of how error response can be used
# class ValidationErrorResponse(ErrorResponse):
#     error_code: str = "E001"
#     message: str = "Invalid course ID provided"
#     details: dict = {"expected": "A valid course ID", "received": "abcd"}