```python
# src/validation.py

from pydantic import BaseModel, Field

class EnrollmentRequest(BaseModel):
    """
    Pydantic model for validating enrollment requests.

    Attributes:
    - course_id (int): The ID of the course to enroll in. This is a required field.
    - student_id (int): The ID of the student to enroll. This is a required field.
    """
    course_id: int = Field(..., title="Course ID", description="The ID of the course to enroll in.")
    student_id: int = Field(..., title="Student ID", description="The ID of the student to enroll.")
```
