# src/schemas/student_course_schemas.py

from pydantic import BaseModel, conint, Field
from typing import List, Optional

class CourseBase(BaseModel):
    """Base schema for a course shared between requests."""
    id: conint(gt=0) = Field(..., description="The unique identifier for the course.")

class StudentBase(BaseModel):
    """Base schema for student details shared between requests."""
    id: conint(gt=0) = Field(..., description="The unique identifier for the student.")
    
class EnrollStudentInCourseRequest(BaseModel):
    """Schema for enrolling a student in a course."""
    student_id: conint(gt=0) = Field(..., description="The ID of the student to enroll.")
    course_id: conint(gt=0) = Field(..., description="The ID of the course to enroll the student in.")

class EnrollStudentInCourseResponse(StudentBase):
    """Response schema for a successful student enrollment."""
    courses: List[CourseBase] = Field(..., description="List of courses the student is enrolled in.")

class RemoveCourseFromStudentRequest(BaseModel):
    """Schema for removing a course from a student."""
    student_id: conint(gt=0) = Field(..., description="The ID of the student.")
    course_id: conint(gt=0) = Field(..., description="The ID of the course to remove.")

class RemoveCourseFromStudentResponse(StudentBase):
    """Response schema for a successful course removal."""
    courses: List[CourseBase] = Field(..., description="List of remaining courses the student is enrolled in.")

class RetrieveStudentCoursesResponse(BaseModel):
    """Response schema for retrieving a student's courses."""
    student_id: conint(gt=0) = Field(..., description="The ID of the student.")
    courses: List[CourseBase] = Field(..., description="List of courses the student is enrolled in.")

class GenericErrorResponse(BaseModel):
    """Schema for generic error responses."""
    error_code: str = Field(..., description="Error code for identifying the error.")
    message: str = Field(..., description="Human-readable error message.")