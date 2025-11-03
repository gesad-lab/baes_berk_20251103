'''
Defines the Pydantic schemas for request and response validation.
'''
from pydantic import BaseModel, EmailStr
class StudentSchema(BaseModel):
    name: str
    email: EmailStr  # Added email field and marked as required
    class Config:
        orm_mode = True
class CourseSchema(BaseModel):
    name: str
    level: str
    teacher_id: int  # Added teacher_id field to associate with Teacher
    class Config:
        orm_mode = True
class TeacherSchema(BaseModel):
    name: str
    email: EmailStr  # Added email field and marked as required
    class Config:
        orm_mode = True