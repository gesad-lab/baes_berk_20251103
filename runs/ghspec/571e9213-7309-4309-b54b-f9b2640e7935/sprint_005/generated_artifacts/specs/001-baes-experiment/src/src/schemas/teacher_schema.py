from pydantic import BaseModel, EmailStr

class TeacherSchema(BaseModel):
    id: int
    name: str
    email: EmailStr

class CreateTeacherRequestSchema(BaseModel):
    name: str
    email: EmailStr