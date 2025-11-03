from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# In-memory storage for demonstration purposes
students_db = {}

class Student(BaseModel):
    id: int
    name: str

class CreateStudentRequest(BaseModel):
    name: str

class UpdateStudentRequest(BaseModel):
    name: str

@app.post("/students/", response_model=Student)
async def create_student(request: CreateStudentRequest):
    student_id = len(students_db) + 1  # Simple ID assignment
    student = Student(id=student_id, name=request.name)
    students_db[student_id] = student
    return student

@app.get("/students/{student_id}", response_model=Student)
async def get_student(student_id: int):
    if student_id not in students_db:
        raise HTTPException(status_code=404, detail="Student not found")
    return students_db[student_id]

@app.put("/students/{student_id}", response_model=Student)
async def update_student(student_id: int, request: UpdateStudentRequest):
    if student_id not in students_db:
        raise HTTPException(status_code=404, detail="Student not found")
    student = students_db[student_id]
    student.name = request.name
    return student

@app.delete("/students/{student_id}")
async def delete_student(student_id: int):
    if student_id not in students_db:
        raise HTTPException(status_code=404, detail="Student not found")
    del students_db[student_id]
    return {"message": "Student deleted successfully"}