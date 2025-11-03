'''
Pydantic schemas for request and response validation.
'''
from pydantic import BaseModel
from typing import List
class CourseBase(BaseModel):
    name: str
    level: str
class CourseCreate(CourseBase):
    pass
class CourseResponse(CourseBase):
    id: int
    class Config:
        orm_mode = True
class StudentBase(BaseModel):
    name: str
    email: str  # Email field is required
class StudentCreate(StudentBase):
    courses: List[CourseCreate] = []  # Allow courses to be added
class StudentResponse(StudentBase):
    id: int
    courses: List[CourseResponse] = []  # Include courses in response
    class Config:
        orm_mode = True
class TeacherBase(BaseModel):
    name: str
    email: str
class TeacherCreate(TeacherBase):
    pass
class TeacherResponse(TeacherBase):
    id: int
    class Config:
        orm_mode = True