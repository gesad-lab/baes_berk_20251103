from app import db
from app.models import Student  # Assuming the model is in app/models.py
from typing import List, Dict

class StudentService:
    """
    Service class for managing student operations.
    Responsibilities include creating, retrieving, and listing students.
    """

    @staticmethod
    def create_student(name: str) -> Dict[str, str]:
        """
        Create a new student in the database.

        :param name: The name of the student to be created.
        :return: A dictionary containing the created student's ID and name.
        """
        if not name:
            raise ValueError("Student name cannot be empty.")

        new_student = Student(name=name)
        db.session.add(new_student)
        db.session.commit()  # Persist the new student to the database

        return {"id": new_student.id, "name": new_student.name}

    @staticmethod
    def get_student(student_id: int) -> Dict[str, str]:
        """
        Retrieve a student's details from the database by their ID.

        :param student_id: The ID of the student to be retrieved.
        :return: A dictionary containing the student's ID and name or an error message.
        """
        student = Student.query.get(student_id)
        if not student:
            raise ValueError(f"Student with ID {student_id} not found.")

        return {"id": student.id, "name": student.name}

    @staticmethod
    def list_students() -> List[Dict[str, str]]:
        """
        List all students in the database.

        :return: A list of dictionaries containing IDs and names of all students.
        """
        students = Student.query.all()
        return [{"id": student.id, "name": student.name} for student in students]

    @staticmethod
    def initialize_database() -> None:
        """
        Initialize the database schema for the Student entity if it does not exist.
        This should be called on application startup.
        """
        db.create_all()  # Create all tables in the database if they do not exist

# Ensure that the database is initialized when starting the application:
StudentService.initialize_database()