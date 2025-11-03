from pydantic import BaseModel, Field
from typing import List, Optional

class CourseBase(BaseModel):
    title: str = Field(..., description="The title of the course")
    description: Optional[str] = Field(None, description="A brief description of the course")
    
class CourseCreate(CourseBase):
    pass

class Course(CourseBase):
    id: int = Field(..., description="The unique identifier for the course")

    class Config:
        orm_mode = True
        
class StudentCourseCreate(BaseModel):
    student_id: int = Field(..., description="The ID of the student to be enrolled")
    course_id: int = Field(..., description="The ID of the course to enroll the student in")

class StudentCourseResponse(BaseModel):
    student_id: int = Field(..., description="The ID of the student")
    course_id: int = Field(..., description="The ID of the course")
    
class StudentCoursesResponse(BaseModel):
    student_id: int = Field(..., description="The ID of the student")
    courses: List[Course] = Field(..., description="List of courses associated with the student")