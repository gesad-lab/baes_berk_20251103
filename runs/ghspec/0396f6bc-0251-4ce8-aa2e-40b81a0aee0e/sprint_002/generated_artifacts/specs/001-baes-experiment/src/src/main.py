from fastapi import FastAPI, HTTPException, Body
from pydantic import BaseModel, EmailStr
from typing import Optional, Dict

app = FastAPI()

# Simulating a database with a dictionary for demonstration purposes
students_db: Dict[int, dict] = {}
student_id_counter = 1

# Request and response models
class StudentCreateRequest(BaseModel):
    name: str
    email: EmailStr  # Ensure proper email format

class StudentResponse(BaseModel):
    id: int
    name: str
    email: str

@app.post("/students", response_model=StudentResponse)
async def create_student(student: StudentCreateRequest):
    global student_id_counter

    # Check for existing student with the same email
    for existing_student in students_db.values():
        if existing_student['email'] == student.email:
            raise HTTPException(status_code=400, detail="Email already exists.")

    # Create new student entry
    new_student = {
        "id": student_id_counter,
        "name": student.name,
        "email": student.email,
    }
    students_db[student_id_counter] = new_student
    student_id_counter += 1
    
    return new_student

@app.get("/students/{student_id}", response_model=StudentResponse)
async def get_student(student_id: int):
    if student_id not in students_db:
        raise HTTPException(status_code=404, detail={"error": {"code": "E404", "message": "Student not found."}})
    
    return students_db[student_id]