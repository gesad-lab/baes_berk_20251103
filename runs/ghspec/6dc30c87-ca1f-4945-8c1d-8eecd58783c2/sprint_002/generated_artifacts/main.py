```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
from myapp.database import create_student, get_student_by_id

app = FastAPI()

class Student(BaseModel):
    name: str
    email: EmailStr  # Using Pydantic's built-in email validation

@app.post("/students", status_code=201)
async def create_student_endpoint(student: Student):
    """Create a new student with a valid name and email."""
    # Attempt to create the student in the database
    try:
        created_student = create_student(student.name, student.email)
        return created_student
    except ValueError as e:
        # Handling specific database errors during student creation
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/students/{id}")
async def retrieve_student(id: int):
    """Retrieve a student's details by their ID."""
    student = get_student_by_id(id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student
```