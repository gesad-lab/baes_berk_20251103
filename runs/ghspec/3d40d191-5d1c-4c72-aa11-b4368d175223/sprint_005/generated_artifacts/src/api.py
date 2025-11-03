```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
from typing import Optional

app = FastAPI()

class TeacherCreate(BaseModel):
    """Schema for teacher creation input."""
    name: str
    email: EmailStr

@app.post("/teachers")
def create_teacher(teacher: TeacherCreate):
    """
    Create a new Teacher entity.
    
    Parameters:
    - teacher: TeacherCreate - Object containing the teacher's name and email.
    
    Returns:
    A message indicating successful creation along with the teacher details.
    
    Raises:
    - HTTPException: If the name or email field is missing.
    """
    # Check for missing fields and raise an error if found
    missing_fields = []
    if not teacher.name:
        missing_fields.append("name")
    if not teacher.email:
        missing_fields.append("email")

    if missing_fields:
        raise HTTPException(
            status_code=400,
            detail=f"Missing required field(s): {', '.join(missing_fields)}. Please provide all required fields."
        )

    # Presumably, create the teacher entity via a service call
    return create_teacher_service(teacher)

@app.get("/teachers/{teacher_id}")
def get_teacher(teacher_id: int):
    """
    Retrieve the details of a specific Teacher entity by its unique identifier.
    
    Parameters:
    - teacher_id: int - Unique identifier of the teacher.
    
    Returns:
    A Teacher object with the specified id, including name and email.
    
    Raises:
    - HTTPException: If the teacher with the specified ID is not found.
    """
    teacher = get_teacher_service(teacher_id)
    if not teacher:  # Assuming get_teacher_service returns None if not found
        raise HTTPException(status_code=404, detail="Teacher not found")
        
    return teacher
```