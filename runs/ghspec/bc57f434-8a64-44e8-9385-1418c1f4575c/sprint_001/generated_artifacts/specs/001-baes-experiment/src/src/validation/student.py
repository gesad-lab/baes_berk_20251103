from pydantic import BaseModel, Field

class StudentCreate(BaseModel):
    """Pydantic model for creating a new student."""
    name: str = Field(..., min_length=1, description="The name of the student, must not be empty.")

class StudentUpdate(BaseModel):
    """Pydantic model for updating an existing student's information."""
    name: str = Field(..., min_length=1, description="The updated name of the student, must not be empty.")

class StudentResponse(BaseModel):
    """Pydantic model for returning student details."""
    id: int
    name: str

    class Config:
        """Configuration for the Pydantic models."""
        orm_mode = True  # Enables compatibility with SQLAlchemy models for ORM use.