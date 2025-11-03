```python
# migrations/versions/create_student_courses_table.py

from pydantic import BaseModel

class EnrollmentCreate(BaseModel):
    """Pydantic model for creating an enrollment relationship between a student and a course."""
    
    student_id: int  # Unique identifier for the student
    course_id: int   # Unique identifier for the course

# The rest of the migration logic follows...
```