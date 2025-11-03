from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Pydantic model for student creation
class StudentCreate(BaseModel):
    name: str

# In-memory storage for example purposes (replace with database later)
students = []

@app.post("/students", response_model=StudentCreate)
async def create_student(student: StudentCreate):
    # Validate that the name is provided
    if not student.name:
        # Raise HTTPException for invalid input with a descriptive error message
        raise HTTPException(status_code=400, detail={
            "error": {
                "code": "E001",
                "message": "Invalid input",
                "details": {"name": "The name field is required."}
            }
        })
    
    # Add the new student to the list (in a real scenario, this would involve a database operation)
    students.append(student)
    
    return student

@app.get("/students", response_model=List[StudentCreate])
async def get_students():
    return students