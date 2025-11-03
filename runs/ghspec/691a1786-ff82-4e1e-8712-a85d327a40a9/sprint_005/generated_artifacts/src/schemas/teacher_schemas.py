```python
from pydantic import BaseModel, EmailStr, Field

class TeacherCreateSchema(BaseModel):
    """Schema for creating a new Teacher."""
    name: str = Field(..., description="The name of the teacher.")
    email: EmailStr = Field(..., description="The email address of the teacher.")

class TeacherResponseSchema(BaseModel):
    """Schema for returning Teacher details."""
    id: int = Field(..., description="Unique identifier of the teacher.")
    name: str = Field(..., description="The name of the teacher.")
    email: EmailStr = Field(..., description="The email address of the teacher.")

class TeacherUpdateSchema(BaseModel):
    """Schema for updating Teacher information."""
    name: str = Field(None, description="The name of the teacher.")
    email: EmailStr = Field(None, description="The email address of the teacher.")

# Example usage of these schemas:
# - TeacherCreateSchema can be used for input validation when creating a teacher.
# - TeacherResponseSchema can be used to format the response after a teacher is created or retrieved.
# - TeacherUpdateSchema can be used for validating the fields during an update operation.
```