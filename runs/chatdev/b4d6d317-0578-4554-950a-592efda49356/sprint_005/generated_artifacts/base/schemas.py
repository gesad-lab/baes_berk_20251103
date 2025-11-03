'''
Defines the Pydantic models for request validation of the Student and Course entities.
'''
from pydantic import BaseModel
class StudentCreate(BaseModel):
    '''
    Model for creating a new student.
    '''
    name: str
    email: str
class CourseCreate(BaseModel):
    '''
    Model for creating a new course.
    '''
    name: str
    level: str