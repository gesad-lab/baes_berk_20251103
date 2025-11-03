```python
from pydantic import BaseModel

class AssignTeacherRequest(BaseModel):
    teacher_id: int  # Required field for assigning a teacher to a course

class CourseDetailsResponse(BaseModel):
    id: int
    teacher_id: int = None  # Assigned teacher's ID; None if unassigned
    # additional course fields can be added here
```