'''
Defines Pydantic schemas for request and response validation.
'''
from pydantic import BaseModel
class StudentCreate(BaseModel):
    name: str
    email: str
class StudentResponse(BaseModel):
    id: int
    name: str
    email: str
    class Config:
        orm_mode = True
class CourseCreate(BaseModel):
    name: str
    level: str
class CourseResponse(BaseModel):
    id: int
    name: str
    level: str
    class Config:
        orm_mode = True