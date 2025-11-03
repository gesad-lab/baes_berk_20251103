from pydantic import BaseModel, EmailStr, constr

class TeacherCreate(BaseModel):
    """Schema for creating a new Teacher entity."""
    name: constr(min_length=1, max_length=100)  # Field for Teacher's name with constraints
    email: EmailStr  # Field for Teacher's email, must be a valid email format

class TeacherResponse(BaseModel):
    """Schema for returning Teacher entity details."""
    id: int  # Teacher's unique identifier (assumed to be an integer)
    name: str  # Teacher's name
    email: str  # Teacher's email

    class Config:
        orm_mode = True  # Enable ORM mode for compatibility with SQLAlchemy models

class TeacherUpdate(BaseModel):
    """Schema for updating an existing Teacher entity."""
    name: constr(min_length=1, max_length=100) = None  # Optional field for Teacher's name
    email: EmailStr = None  # Optional field for Teacher's email

    class Config:
        orm_mode = True  # Enable ORM mode for compatibility with SQLAlchemy models