'''
Defines the Pydantic schemas for request and response validation.
'''
from pydantic import BaseModel
class StudentCreate(BaseModel):
    name: str
class Student(StudentCreate):
    id: int
    class Config:
        orm_mode = True