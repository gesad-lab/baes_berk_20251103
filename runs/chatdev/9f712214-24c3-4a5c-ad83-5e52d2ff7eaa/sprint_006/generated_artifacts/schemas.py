'''
Defines the Pydantic models for request validation.
'''
from pydantic import BaseModel, EmailStr
class StudentCreate(BaseModel):
    '''
    Pydantic model for creating a student.
    '''
    name: str
    email: EmailStr
class CourseCreate(BaseModel):
    '''
    Pydantic model for creating a course.
    '''
    name: str
    level: str
    teacher_id: int = None  # Added field for teacher ID
class TeacherCreate(BaseModel):
    '''
    Pydantic model for creating a teacher.
    '''
    name: str
    email: EmailStr