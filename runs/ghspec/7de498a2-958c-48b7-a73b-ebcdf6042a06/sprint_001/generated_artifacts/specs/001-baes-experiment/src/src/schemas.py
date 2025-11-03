from pydantic import BaseModel, Field

class StudentCreate(BaseModel):
    """Model for creating a new student."""
    name: str = Field(..., title="Student Name", description="The name of the student, required field.")

class StudentUpdate(BaseModel):
    """Model for updating an existing student's information."""
    name: str = Field(..., title="Updated Student Name", description="The updated name of the student, required field.")

class StudentResponse(BaseModel):
    """Model for the student response representation."""
    id: int
    name: str

    class Config:
        # Configure the model to use ORM mode so we can work with ORM instances
        orm_mode = True