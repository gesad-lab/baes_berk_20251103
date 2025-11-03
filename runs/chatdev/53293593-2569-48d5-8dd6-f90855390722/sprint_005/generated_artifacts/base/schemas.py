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
    class Config:
        orm_mode = True