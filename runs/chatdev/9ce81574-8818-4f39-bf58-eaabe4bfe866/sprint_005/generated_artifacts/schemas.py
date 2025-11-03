'''
Defines the Pydantic models for request validation and response serialization.
'''
from pydantic import BaseModel, EmailStr
class StudentCreate(BaseModel):
    '''
    Schema for creating a new student.
    Attributes:
    - name: str - The name of the student.
    - email: EmailStr - The email of the student (must be a valid email format).
    '''
    name: str
    email: EmailStr
class CourseCreate(BaseModel):
    '''
    Schema for creating a new course.
    Attributes:
    - name: str - The name of the course.
    - level: str - The level of the course.
    '''
    name: str
    level: str
class TeacherCreate(BaseModel):
    '''
    Schema for creating a new teacher.
    Attributes:
    - name: str - The name of the teacher.
    - email: EmailStr - The email of the teacher (must be a valid email format).
    '''
    name: str
    email: EmailStr