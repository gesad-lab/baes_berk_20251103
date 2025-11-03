'''
Pydantic schemas for request and response validation.
'''
from pydantic import BaseModel
class StudentCreate(BaseModel):
    name: str
    email: str  # Added email field
class StudentResponse(BaseModel):
    id: int
    name: str
    email: str  # Added email field
class CourseCreate(BaseModel):
    name: str
    level: str
    teacher_id: int  # Added teacher_id field
class CourseResponse(BaseModel):
    id: int
    name: str
    level: str
    teacher_id: int  # Added teacher_id field
class TeacherCreate(BaseModel):
    name: str
    email: str
class TeacherResponse(BaseModel):
    id: int
    name: str
    email: str