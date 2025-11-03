from pydantic import BaseModel, EmailStr

class TeacherCreate(BaseModel):
    """Schema for creating a Teacher.

    Attributes:
        name (str): The name of the Teacher. Must be provided.
        email (EmailStr): The email of the Teacher. Must be a valid email format.
    """
    name: str
    email: EmailStr

class TeacherResponse(BaseModel):
    """Schema for responding with Teacher details.

    Attributes:
        id (int): The unique identifier of the Teacher.
        name (str): The name of the Teacher.
        email (EmailStr): The email of the Teacher.
    """
    id: int
    name: str
    email: EmailStr

    class Config:
        orm_mode = True  # Enables compatibility with SQLAlchemy models