from fastapi import HTTPException
from pydantic import BaseModel, EmailStr
from typing import List
from src.repositories.student_repository import StudentRepository
from src.models.student import Student

class CreateStudentRequest(BaseModel):
    name: str
    email: EmailStr

class StudentService:
    def __init__(self, student_repository: StudentRepository):
        self.student_repository = student_repository

    def create_student(self, student_data: CreateStudentRequest) -> Student:
        # Validate input data
        if not student_data.name or not student_data.email:
            raise HTTPException(
                status_code=400,
                detail={"error": {"code": "E001", "message": "Missing name or email field."}}
            )
        
        # Create a new student using validated data
        new_student = Student(name=student_data.name, email=student_data.email)
        return self.student_repository.save(new_student)

    def get_all_students(self) -> List[Student]:
        # Retrieve all students from the repository
        return self.student_repository.get_all()

    def validate_email(self, email: str) -> bool:
        # Utilizing EmailStr from Pydantic to validate email format
        try:
            EmailStr.validate(email)
            return True
        except ValueError:
            return False

# Note: The routing and request handling will need to be updated in `main.py` to handle
# the new request body and call the appropriate service methods. Make sure to handle
# the case where an invalid email is provided as well.