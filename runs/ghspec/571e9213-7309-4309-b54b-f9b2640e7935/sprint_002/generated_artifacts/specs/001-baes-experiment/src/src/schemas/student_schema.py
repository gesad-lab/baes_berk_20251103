from pydantic import BaseModel, EmailStr

class StudentSchema(BaseModel):
    id: int
    name: str
    email: EmailStr  # New Email Field to validate email format

    class Config:
        orm_mode = True  # Enable ORM mode to work with SQLAlchemy models