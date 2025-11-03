from pydantic import BaseModel, EmailStr, Field

class TeacherCreate(BaseModel):
    name: str = Field(..., example="John Doe")
    email: EmailStr = Field(..., example="john.doe@example.com")

class Teacher(BaseModel):
    id: int
    name: str
    email: EmailStr

    class Config:
        orm_mode = True

__tablename__ = 'teachers'  # Define the table name for the Teacher model