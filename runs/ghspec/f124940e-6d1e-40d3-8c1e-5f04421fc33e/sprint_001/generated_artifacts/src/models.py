```python
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

# Define the FastAPI application
app = FastAPI()

# In-memory storage for student records (would be replaced by database integration)
students_db = {}

# Model for Student entity
class Student(BaseModel):
    id: int
    name: str

# Example auto-increment ID
next_id = 1

@app.post("/students/", response_model=Student)
async def create_student(student: Student):
    global next_id
    student.id = next_id
    students_db[next_id] = student
    next_id += 1
    return student

@app.get("/students/", response_model=List[Student])
async def get_students():
    return list(students_db.values())

@app.put("/students/{student_id}", response_model=Student)
async def update_student(student_id: int, student: Student):
    if student_id not in students_db:
        return {"error": {"code": "E404", "message": "Student not found"}}
    student.id = student_id
    students_db[student_id] = student
    return student

@app.delete("/students/{student_id}")
async def delete_student(student_id: int):
    if student_id in students_db:
        del students_db[student_id]
        return {"message": "Student deleted successfully"}
    return {"error": {"code": "E404", "message": "Student not found"}}

# Entry point for running the application
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
```