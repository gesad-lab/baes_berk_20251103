'''
Defines the Pydantic models for the Student entity.
'''
from pydantic import BaseModel
class StudentBase(BaseModel):
    name: str
class StudentCreate(StudentBase):
    pass
class StudentResponse(StudentBase):
    id: int
    class Config:
        orm_mode = True