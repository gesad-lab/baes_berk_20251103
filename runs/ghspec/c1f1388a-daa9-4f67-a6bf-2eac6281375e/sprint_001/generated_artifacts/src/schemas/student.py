from pydantic import BaseModel, Field

class StudentOutputSchema(BaseModel):
    """Schema for Student output data."""
    
    id: int = Field(..., description="The unique identifier for the student")
    name: str = Field(..., description="The name of the student")

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "name": "John Doe"
            }
        }