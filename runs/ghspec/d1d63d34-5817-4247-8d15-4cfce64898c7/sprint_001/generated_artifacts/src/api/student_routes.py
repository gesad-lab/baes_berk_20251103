from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# Define the Student model
class Student(BaseModel):
    id: int
    name: str

# Placeholder for students data, simulating a database
students_db = []  # This will hold our student records

# Error response model
class ErrorResponse(BaseModel):
    error: dict

# Create a Student
@app.post("/students", response_model=Student, status_code=201)
async def create_student(student: Student):
    # Check if a student with the same name already exists
    if any(s.name == student.name for s in students_db):
        raise HTTPException(
            status_code=400,
            detail={"code": "E001", "message": "Student already exists with this name."}
        )
    
    students_db.append(student)
    return student

# Get a Student by ID
@app.get("/students/{id}", response_model=Student)
async def get_student(id: int):
    student = next((s for s in students_db if s.id == id), None)
    if student is None:
        raise HTTPException(
            status_code=404,
            detail={"code": "E002", "message": "Student not found."}
        )
    return student

# Update a Student by ID
@app.put("/students/{id}", response_model=Student)
async def update_student(id: int, student: Student):
    existing_student = next((s for s in students_db if s.id == id), None)
    if existing_student is None:
        raise HTTPException(
            status_code=404,
            detail={"code": "E002", "message": "Student not found."}
        )
    
    existing_student.name = student.name
    return existing_student

# Delete a Student by ID
@app.delete("/students/{id}", status_code=204)
async def delete_student(id: int):
    global students_db
    students_db = [s for s in students_db if s.id != id]
    return

# List all Students
@app.get("/students", response_model=List[Student])
async def list_students():
    return students_db

# Custom error handler
@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc: HTTPException):
    return ErrorResponse(error={"code": exc.detail.get("code", "E500"), "message": exc.detail.get("message", "An unexpected error occurred.")})