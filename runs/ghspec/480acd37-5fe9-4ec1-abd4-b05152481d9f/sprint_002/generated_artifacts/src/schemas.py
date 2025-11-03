from pydantic import BaseModel, EmailStr, Field
from typing import List, Optional

class StudentBase(BaseModel):
    name: str = Field(..., min_length=1)
    email: EmailStr  # Validate email format

class StudentCreate(StudentBase):
    pass

class StudentUpdate(StudentBase):
    name: Optional[str] = Field(None, min_length=1)
    email: Optional[EmailStr]  # Optional field for updates

class StudentResponse(StudentBase):
    id: int  # ID included in the response

class StudentListResponse(BaseModel):
    students: List[StudentResponse]  # For listing multiple students

    class Config:
        orm_mode = True  # Allows Pydantic to work with SQLAlchemy models
