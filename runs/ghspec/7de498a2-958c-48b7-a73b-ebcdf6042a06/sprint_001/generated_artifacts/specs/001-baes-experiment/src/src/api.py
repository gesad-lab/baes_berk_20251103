from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Model for Student
class Student(BaseModel):
    name: str

# In-memory database simulation
students_db = {}

@app.post("/students/", response_model=Student)
async def create_student(student: Student):
    """
    Create a new Student entry
    :param student: Student object containing the name
    :return: Created Student
    """
    if not student.name:
        raise HTTPException(status_code=400, detail="E001: Name is required to create a student.")

    student_id = len(students_db) + 1  # Simple incremental ID
    students_db[student_id] = student
    return student

@app.get("/students/{student_id}", response_model=Student)
async def get_student(student_id: int):
    """
    Retrieve a Student by ID
    :param student_id: ID of the student to retrieve
    :return: Student details
    """
    student = students_db.get(student_id)
    if not student:
        raise HTTPException(status_code=404, detail="E002: Student not found.")
    return student

@app.put("/students/{student_id}", response_model=Student)
async def update_student(student_id: int, student: Student):
    """
    Update an existing Student's name
    :param student_id: ID of the student to update
    :param student: Updated student data
    :return: Updated Student details
    """
    if not student.name:
        raise HTTPException(status_code=400, detail="E001: Name is required to update a student.")

    if student_id not in students_db:
        raise HTTPException(status_code=404, detail="E002: Student not found.")

    students_db[student_id] = student
    return student

@app.delete("/students/{student_id}")
async def delete_student(student_id: int):
    """
    Delete a Student by ID
    :param student_id: ID of the student to delete
    :return: Success message
    """
    if student_id not in students_db:
        raise HTTPException(status_code=404, detail="E002: Student not found.")

    del students_db[student_id]
    return {"message": "Student deleted successfully."}