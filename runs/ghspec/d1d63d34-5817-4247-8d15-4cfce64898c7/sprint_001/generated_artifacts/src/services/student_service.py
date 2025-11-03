```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, constr
from typing import List, Optional

app = FastAPI()

# Database simulation
students_db = {}

class Student(BaseModel):
    id: int
    name: constr(min_length=1)  # Validating name as a non-empty string

@app.post("/students/", response_model=Student, status_code=201)
def create_student(student: Student):
    # Check if the student with the same ID already exists
    if student.id in students_db:
        raise HTTPException(status_code=400, detail="Student ID already exists.")
    
    # Add student to the simulated database
    students_db[student.id] = student
    return student

@app.get("/students/{student_id}", response_model=Student, status_code=200)
def get_student(student_id: int):
    # Retrieve student from the simulated database
    student = students_db.get(student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found.")
    return student

@app.put("/students/{student_id}", response_model=Student, status_code=200)
def update_student(student_id: int, student: Student):
    if student_id not in students_db:
        raise HTTPException(status_code=404, detail="Student not found.")
    
    # Update student's name
    students_db[student_id].name = student.name
    return students_db[student_id]

@app.delete("/students/{student_id}", status_code=204)
def delete_student(student_id: int):
    if student_id not in students_db:
        raise HTTPException(status_code=404, detail="Student not found.")
    
    # Remove student from the simulated database
    del students_db[student_id]
    return

@app.get("/students/", response_model=List[Student], status_code=200)
def list_students():
    return list(students_db.values())
```