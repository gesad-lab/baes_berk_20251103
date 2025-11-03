from typing import List, Optional
from sqlalchemy.orm import Session
from models import Student  # Assumes the Student model is defined in models.py
from schemas import StudentCreate, StudentResponse  # Assumes these schemas are defined in schemas.py

class StudentService:
    """Service class for handling student-related business logic."""

    def __init__(self, db: Session):
        self.db = db

    def create_student(self, student_data: StudentCreate) -> StudentResponse:
        """Create a new student record in the database.

        Args:
            student_data (StudentCreate): The data of the student to be created.

        Returns:
            StudentResponse: The created student object.
        """
        # Validate email format here if necessary (could also be handled in the schema)
        
        # Create new student instance
        new_student = Student(
            name=student_data.name,
            email=student_data.email  # New email field
        )
        
        self.db.add(new_student)  # Add new student to the session
        self.db.commit()  # Commit the transaction
        self.db.refresh(new_student)  # Refresh to get the new student's data
        
        return StudentResponse.from_orm(new_student)  # Convert to response schema format

    def get_students(self) -> List[StudentResponse]:
        """Retrieve all students from the database.

        Returns:
            List[StudentResponse]: A list of students.
        """
        students = self.db.query(Student).all()  # Query all students
        return [StudentResponse.from_orm(student) for student in students]  # Convert to response schema format

    def get_student_by_id(self, student_id: int) -> Optional[StudentResponse]:
        """Retrieve a single student by their ID.

        Args:
            student_id (int): The ID of the student.

        Returns:
            Optional[StudentResponse]: The student object if found, otherwise None.
        """
        student = self.db.query(Student).filter(Student.id == student_id).first()  # Query by ID
        if student:
            return StudentResponse.from_orm(student)  # Convert to response schema format
        return None  # Return None if no student was found

    # Additional methods can be added as needed for managing students
