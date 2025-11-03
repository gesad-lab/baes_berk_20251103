from pydantic import BaseModel, constr

class StudentCreate(BaseModel):
    """Schema for creating a new student."""
    name: constr(min_length=1, max_length=100)  # Name is required with a length limit

class StudentResponse(BaseModel):
    """Schema for responding with student details."""
    id: int  # Unique identifier for the student
    name: str  # Name of the student

    class Config:
        """Pydantic configuration options."""
        orm_mode = True  # Allows Pydantic to read data from the ORM models

class StudentUpdate(BaseModel):
    """Schema for updating an existing student."""
    name: constr(min_length=1, max_length=100)  # New name is required with a length limit