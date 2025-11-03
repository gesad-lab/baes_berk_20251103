```python
# api.py

from fastapi import FastAPI, HTTPException, Request, status
from pydantic import BaseModel, EmailStr
import logging

app = FastAPI()

# Setup logging for debugging and error tracking
logging.basicConfig(level=logging.INFO)

# Define the teacher model for request validation
class Teacher(BaseModel):
    name: str
    email: EmailStr

# Exception Handling Middleware
@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    try:
        response = await call_next(request)
        return response
    except HTTPException as exc:
        # Log the error for debugging purposes
        logging.error(f"HTTP error occurred: {exc.detail}")
        raise  # Re-raise the exception after logging
    except Exception as exc:
        # Handle unexpected exceptions
        logging.error(f"Unexpected error: {exc}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="An unexpected error occurred.")

# Sample in-memory store for teachers (replace with database logic in production)
teachers_db = []

@app.post("/teachers", status_code=status.HTTP_201_CREATED)
async def create_teacher(teacher: Teacher):
    # Validate input data
    if not teacher.name or not teacher.email:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Both name and email must be provided.")
    
    # Check if teacher already exists
    if any(t for t in teachers_db if t['email'] == teacher.email):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Teacher with this email already exists.")

    # Create new teacher entry
    teachers_db.append(teacher.dict())
    return {"msg": "Teacher created successfully"}

@app.get("/teachers", status_code=status.HTTP_200_OK)
async def get_teachers():
    return teachers_db
```