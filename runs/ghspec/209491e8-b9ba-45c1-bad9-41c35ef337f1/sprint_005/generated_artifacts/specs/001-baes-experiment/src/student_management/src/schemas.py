from pydantic import BaseModel, EmailStr

class TeacherCreate(BaseModel):
    """Schema for creating a new teacher."""
    name: str  # The name of the teacher
    email: EmailStr  # The email address of the teacher


class TeacherResponse(BaseModel):
    """Schema for the response returned when retrieving teacher information."""
    id: int  # Unique identifier for the teacher
    name: str  # The name of the teacher
    email: EmailStr  # The email address of the teacher

    class Config:
        """Configuration for Pydantic model to use ORM mode."""
        orm_mode = True