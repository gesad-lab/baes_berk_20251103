```python
from pydantic import BaseModel, Field

class AssignTeacher(BaseModel):
    """Schema for assigning a teacher to a course."""
    
    teacher_id: str = Field(..., description="The ID of the teacher to be assigned to the course.")
```