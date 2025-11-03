'''
Defines the Pydantic models for the Student and Course entities.
'''
from pydantic import BaseModel
class StudentBase(BaseModel):
    name: str
    email: str  # Add email field
class StudentCreate(StudentBase):
    pass
class StudentResponse(StudentBase):
    id: int
    class Config:
        orm_mode = True
class CourseBase(BaseModel):
    name: str
    level: str
class CourseCreate(CourseBase):
    pass
class CourseResponse(CourseBase):
    id: int
    class Config:
        orm_mode = True