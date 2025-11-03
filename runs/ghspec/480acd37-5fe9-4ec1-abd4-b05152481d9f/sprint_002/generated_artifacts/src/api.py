from fastapi import FastAPI, HTTPException
from typing import List
from models import Student  # Assuming Student model is defined in models.py
from pydantic import BaseModel, EmailStr

app = FastAPI()

# Schema for student response
class StudentResponse(BaseModel):
    id: int
    name: str
    email: EmailStr

# Schema for creating or updating student
class StudentCreateUpdate(BaseModel):
    name: str
    email: EmailStr

@app.post("/students", response_model=StudentResponse, status_code=201)
async def create_student(student: StudentCreateUpdate):
    """
    Create a new student record with email.

    Parameters:
    - student: The data structure containing the name and email of the new student.

    Returns:
    - The created student record.
    """
    new_student = Student(name=student.name, email=student.email)  # Assuming an ORM is being used
    await new_student.save()  # Ensure to save the student in the database
    return new_student

@app.get("/students", response_model=List[StudentResponse], status_code=200)
async def get_students():
    """
    Retrieve all student records with email.

    Returns:
    - A list of student records, including ID, name, and email.
    """
    students = await Student.query.gino.all()  # Retrieving all students from the database
    return students

@app.put("/students/{student_id}", response_model=StudentResponse, status_code=200)
async def update_student(student_id: int, student: StudentCreateUpdate):
    """
    Update an existing student's name and email.

    Parameters:
    - student_id: The ID of the student to update.
    - student: The data structure containing the new name and email.

    Returns:
    - The updated student record.
    """
    existing_student = await Student.get(student_id)
    if not existing_student:
        raise HTTPException(status_code=404, detail="Student not found")

    # Update the student's data
    existing_student.name = student.name
    existing_student.email = student.email
    await existing_student.update()  # Save changes to the database
    return existing_student

# Note: Remember to handle exceptions and add validation for email formatting in the Student model or with Pydantic.