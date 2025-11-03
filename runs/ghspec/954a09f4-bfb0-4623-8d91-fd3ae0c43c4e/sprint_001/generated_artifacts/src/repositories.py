from typing import Optional, Dict, Any
from flask_sqlalchemy import SQLAlchemy

# Initialize the SQLAlchemy object
db = SQLAlchemy()

class Student(db.Model):
    """Model representing a student entity."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f"<Student {self.name}>"

class StudentRepository:
    """Repository for managing Student entities in the database."""

    @staticmethod
    def create_student(name: str) -> Student:
        """
        Create a new student record in the database.

        Parameters:
        - name (str): The name of the student, which is required.

        Returns:
        - Student: The created student object.
        
        Raises:
        - ValueError: If the name is not provided or is empty.
        """
        if not name:
            raise ValueError("Name is required.")
        
        student = Student(name=name)
        db.session.add(student)
        db.session.commit()  # Commit the transaction
        return student

    @staticmethod
    def get_student(student_id: int) -> Optional[Student]:
        """
        Retrieve a student by their ID.

        Parameters:
        - student_id (int): The ID of the student to retrieve.

        Returns:
        - Optional[Student]: The student object if found, else None.
        """
        return Student.query.get(student_id)  # Retrieve by primary key