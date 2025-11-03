```python
from src.models.student import Student  # Importing the Student model
from sqlalchemy.orm import Session
from fastapi import HTTPException, Depends
from typing import List
from src.schemas.student import StudentCreate, StudentResponse

# Business logic for managing students.
class StudentService:
    def __init__(self, db: Session):
        self.db = db

    def create_student(self, student: StudentCreate) -> StudentResponse:
        """
        Create a new student in the database.

        Parameters:
        - student: A StudentCreate object containing name and email.

        Returns:
        - A StudentResponse object containing the created student's information.

        Raises:
        - HTTPException: If the student cannot be created.
        """
        db_student = Student(name=student.name, email=student.email)
        self.db.add(db_student)
        self.db.commit()
        self.db.refresh(db_student)
        
        return StudentResponse(id=db_student.id, name=db_student.name, email=db_student.email)

    def get_student(self, student_id: int) -> StudentResponse:
        """
        Retrieve a student by their ID.

        Parameters:
        - student_id: The ID of the student to retrieve.

        Returns:
        - A StudentResponse object containing the student's information.

        Raises:
        - HTTPException: If the student is not found.
        """
        student = self.db.query(Student).filter(Student.id == student_id).first()
        if student is None:
            raise HTTPException(status_code=404, detail="Student not found")
        
        return StudentResponse(id=student.id, name=student.name, email=student.email)

    def get_all_students(self) -> List[StudentResponse]:
        """
        Retrieve all students from the database.

        Returns:
        - A list of StudentResponse objects containing information of all students.
        """
        students = self.db.query(Student).all()
        return [StudentResponse(id=student.id, name=student.name, email=student.email) for student in students]
```