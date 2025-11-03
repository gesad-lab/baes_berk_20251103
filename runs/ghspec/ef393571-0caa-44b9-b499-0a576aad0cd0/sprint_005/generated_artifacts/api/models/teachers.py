from pydantic import BaseModel, EmailStr, Field

class TeacherCreateRequest(BaseModel):
    """Model for creating a new teacher."""
    name: str = Field(..., min_length=1, example="John Doe")
    email: EmailStr = Field(..., example="john.doe@example.com")

class TeacherResponse(BaseModel):
    """Model for the response containing teacher details."""
    id: int
    name: str
    email: EmailStr

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "name": "John Doe",
                "email": "john.doe@example.com"
            }
        }