'''
Data schemas for API requests and responses.
'''
from pydantic import BaseModel
class StudentCreate(BaseModel):
    name: str
    email: str  # Added email field
class StudentResponse(BaseModel):
    id: int
    name: str
    email: str  # Added email field
    class Config:
        orm_mode = True