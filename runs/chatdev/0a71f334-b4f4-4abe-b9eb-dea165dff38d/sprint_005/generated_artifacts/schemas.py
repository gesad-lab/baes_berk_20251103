'''
Pydantic schemas for request and response validation.
'''
from pydantic import BaseModel
class StudentCreate(BaseModel):
    name: str
    email: str
class CourseCreate(BaseModel):
    name: str
    level: str
class CourseResponse(BaseModel):
    id: int
    name: str
    level: str
class StudentResponse(BaseModel):
    id: int
    name: str
    email: str
    courses: list[CourseResponse] = []  # Add this line to include courses
    class Config:
        orm_mode = True
class TeacherCreate(BaseModel):
    name: str
    email: str
class TeacherResponse(BaseModel):
    id: int
    name: str
    email: str
    class Config:
        orm_mode = True