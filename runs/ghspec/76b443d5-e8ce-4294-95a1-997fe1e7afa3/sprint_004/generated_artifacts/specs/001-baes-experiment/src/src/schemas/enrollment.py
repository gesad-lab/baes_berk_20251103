```python
from pydantic import BaseModel, Field

class EnrollmentRequestModel(BaseModel):
    """Model for handling enrollment requests for students."""
    
    courseId: str = Field(..., description="The unique identifier for the course to enroll in.")
    
    class Config:
        """Pydantic configuration options."""
        
        schema_extra = {
            "example": {
                "courseId": "some_course_id"
            }
        }
```