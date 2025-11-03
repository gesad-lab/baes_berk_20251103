from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from typing import List, Optional

# Import the Student model from your data access layer (assuming it is defined elsewhere)
from src.models.student import Student


class StudentService:
    """Service for managing Student records."""

    def __init__(self, db: Session):
        """Initialize the StudentService with the database session.

        Args:
            db (Session): SQLAlchemy database session.
        """
        self.db = db

    def create_student(self, name: str) -> Student:
        """Create a new student record.

        Args:
            name (str): The name of the student.

        Returns:
            Student: The created Student object.
        
        Raises:
            ValueError: If name is empty or None.
            SQLAlchemyError: If there is an error during the database operation.
        """
        if not name:
            raise ValueError("Student name cannot be empty.")

        new_student = Student(name=name)
        try:
            self.db.add(new_student)
            self.db.commit()
            self.db.refresh(new_student)
            return new_student
        except SQLAlchemyError as e:
            self.db.rollback()  # Rollback the transaction on error
            raise SQLAlchemyError(f"Error creating student: {str(e)}")

    def get_student(self, student_id: int) -> Optional[Student]:
        """Retrieve a student record by ID.

        Args:
            student_id (int): The ID of the student to retrieve.

        Returns:
            Optional[Student]: The Student object if found, else None.
        
        Raises:
            SQLAlchemyError: If there is an error during the database operation.
        """
        try:
            return self.db.query(Student).filter(Student.id == student_id).first()
        except SQLAlchemyError as e:
            raise SQLAlchemyError(f"Error retrieving student: {str(e)}")

    def update_student(self, student_id: int, name: str) -> Optional[Student]:
        """Update an existing student record.

        Args:
            student_id (int): The ID of the student to update.
            name (str): The new name of the student.

        Returns:
            Optional[Student]: The updated Student object if found, else None.
        
        Raises:
            ValueError: If name is empty or None.
            SQLAlchemyError: If there is an error during the database operation.
        """
        if not name:
            raise ValueError("Student name cannot be empty.")

        try:
            student = self.get_student(student_id)
            if student is None:
                return None

            student.name = name
            self.db.commit()
            return student
        except SQLAlchemyError as e:
            self.db.rollback()  # Rollback the transaction on error
            raise SQLAlchemyError(f"Error updating student: {str(e)}")

    def delete_student(self, student_id: int) -> bool:
        """Delete a student record by ID.

        Args:
            student_id (int): The ID of the student to delete.

        Returns:
            bool: True if the student was deleted, False if not found.
        
        Raises:
            SQLAlchemyError: If there is an error during the database operation.
        """
        try:
            student = self.get_student(student_id)
            if not student:
                return False

            self.db.delete(student)
            self.db.commit()
            return True
        except SQLAlchemyError as e:
            self.db.rollback()  # Rollback the transaction on error
            raise SQLAlchemyError(f"Error deleting student: {str(e)}")

    def list_students(self) -> List[Student]:
        """Retrieve all students.

        Returns:
            List[Student]: A list of Student objects.
        
        Raises:
            SQLAlchemyError: If there is an error during the database operation.
        """
        try:
            return self.db.query(Student).all()
        except SQLAlchemyError as e:
            raise SQLAlchemyError(f"Error retrieving students: {str(e)}")