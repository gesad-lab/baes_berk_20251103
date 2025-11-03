from pydantic import BaseModel
from typing import Optional, List

class StudentCreate(BaseModel):
    name: str

class StudentUpdate(BaseModel):
    name: Optional[str]

class StudentResponse(BaseModel):
    id: int
    name: str

class StudentListResponse(BaseModel):
    students: List[StudentResponse]