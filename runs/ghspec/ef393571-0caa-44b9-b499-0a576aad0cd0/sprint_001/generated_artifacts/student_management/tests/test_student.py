```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, constr
from typing import List
from student_management.models.student import Student
from student_management.services.student_service import StudentService

app = FastAPI()
student_service = StudentService()

class StudentCreate(BaseModel):
    name: constr(min_length=1)  # Require names to be at least 1 character long

@app.post("/students", response_model=Student)
async def create_student(student: StudentCreate):
    """
    Create a new student with the provided name.

    :param student: The student information, including the student's name.
    :return: The created student object.
    :raises HTTPException: If the student name is not provided.
    """
    try:
        new_student = await student_service.add_student(student.name)
        return new_student
    except ValueError as e:
        # Catch validation errors, such as when the name is empty or not valid
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        # Log the exception for debugging and raise an internal server error
        # Here you would use logger instead of print in production code
        print(f"Error adding student: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@app.get("/students", response_model=List[Student])
async def get_students():
    """
    Retrieve all students in the database.

    :return: A list of student objects.
    :raises HTTPException: If there is an error retrieving students.
    """
    try:
        students = await student_service.get_all_students()
        return students
    except Exception as e:
        # Log the exception for debugging and raise an internal server error
        print(f"Error retrieving students: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
```