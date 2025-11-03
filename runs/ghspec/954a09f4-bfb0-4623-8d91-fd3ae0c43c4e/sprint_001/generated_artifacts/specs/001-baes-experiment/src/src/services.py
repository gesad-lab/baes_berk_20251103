```python
from flask import jsonify, abort
from .repositories import StudentRepository

class StudentService:
    def __init__(self, student_repository: StudentRepository):
        self.student_repository = student_repository

    def get_student_by_id(self, student_id: int):
        """
        Retrieve a student by their ID.

        Parameters:
        student_id (int): The ID of the student to retrieve.

        Returns:
        dict: The student's information if found.

        Raises:
        404: If the student is not found.
        """
        student = self.student_repository.get_by_id(student_id)
        
        if student is None:
            # If the student does not exist, return a 404 error.
            abort(404, description=f"Student with ID {student_id} not found.")

        return jsonify(student)

    def create_student(self, name: str):
        """
        Create a new student with the given name.

        Parameters:
        name (str): The name of the student to create.

        Returns:
        dict: The created student's information.
        """
        if not name:
            # If the name is missing, return a 400 error.
            abort(400, description="Name is required to create a student.")

        student = self.student_repository.create(name)
        return jsonify(student)
```