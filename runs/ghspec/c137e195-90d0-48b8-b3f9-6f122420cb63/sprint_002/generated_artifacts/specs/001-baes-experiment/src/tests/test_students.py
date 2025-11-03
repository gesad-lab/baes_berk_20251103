```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
from database.db import init_db
from api.students import router as student_router

app = FastAPI()

class ErrorResponse(BaseModel):
    error: dict

@app.on_event("startup")
def startup():
    """Initialize the database on application startup."""
    init_db()

app.include_router(student_router)

# Error handling functions
def handle_missing_email():
    """Raises an HTTP exception for missing email."""
    raise HTTPException(
        status_code=400, 
        detail={"message": "Email is required", "code": "E001"}
    )

def handle_invalid_email_format():
    """Raises an HTTP exception for invalid email format."""
    raise HTTPException(
        status_code=400, 
        detail={"message": "Invalid email format", "code": "E002"}
    )

# Example of usage in creating a student
@router.post("/students")
def create_student(student: StudentCreate):
    if not student.name:
        raise HTTPException(status_code=400, detail="Name is required")
    
    if not student.email:
        handle_missing_email()

    # Assuming EmailStr validation from Pydantic handles format validation
    try:
        email = EmailStr(student.email)
    except ValueError:
        handle_invalid_email_format()

    # Logic for creating student goes here...
```