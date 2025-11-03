```python
from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel, constr

router = APIRouter()

# Define a Pydantic model for a Student
class Student(BaseModel):
    name: constr(min_length=1, max_length=100)  # Validate name length

# In-memory storage for students (replace with database in production)
students_db = {}

@router.post("/students")
async def create_student(student: Student):
    """
    Create a new student in the database.

    :param student: A Student object containing the student's name.
    :return: A success message along with the student's ID.
    :raises HTTPException: If the student name is not valid.
    """
    # Check if student name already exists (optional)
    if any(s.name == student.name for s in students_db.values()):
        raise HTTPException(status_code=400, detail="Student name already exists")

    # Generate a new student ID (simple incremental)
    student_id = len(students_db) + 1
    students_db[student_id] = student  # Store student in the database

    return {"message": "Student created successfully", "student_id": student_id}

@router.get("/students/{student_id}")
async def get_student(student_id: int):
    """
    Retrieve a student by their ID.

    :param student_id: The ID of the student to retrieve.
    :return: The details of the student.
    :raises HTTPException: If the student ID does not exist.
    """
    if student_id not in students_db:
        raise HTTPException(status_code=404, detail="Student not found")

    return students_db[student_id]
```