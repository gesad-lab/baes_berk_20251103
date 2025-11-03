```python
# src/services/student_service.py

from typing import List
from src.models.student import Student
from src.repositories.student_repository import StudentRepository


class StudentService:
    """
    Service layer for managing student operations.

    This class contains methods for adding and retrieving students from the repository.
    """

    def __init__(self, student_repository: StudentRepository):
        """
        Initializes the StudentService with a student repository.

        Parameters:
        - student_repository: An instance of StudentRepository to interact with data store.
        """
        self.student_repository = student_repository

    def add_student(self, name: str) -> Student:
        """
        Adds a new student to the repository.
        
        Parameters:
        - name: The name of the student to add.

        Returns:
        - The created Student object.
        """
        new_student = Student(name=name)  # Create a new Student instance
        created_student = self.student_repository.create(new_student)  # Save to DB
        return created_student

    def get_students(self) -> List[Student]:
        """
        Retrieves all students from the repository.

        Returns:
        - A list of Student objects.
        """
        students = self.student_repository.get_all()  # Fetch all students
        return students
```