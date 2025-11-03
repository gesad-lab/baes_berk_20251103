```python
from typing import List, Optional
from flask import jsonify, request
from marshmallow import Schema, fields, ValidationError

# Data model for Student
class Student:
    def __init__(self, student_id: int, name: str):
        self.student_id = student_id
        self.name = name

# This will serve as a simple in-memory storage for students
students_db = {}
next_id = 1

class StudentSchema(Schema):
    name = fields.String(required=True)

class StudentService:
    """
    Service for handling business logic related to students.
    """

    @staticmethod
    def register_student(name: str) -> Student:
        """
        Register a new student with the given name.

        :param name: The name of the student to register.
        :return: The newly created Student object.
        """
        global next_id
        student = Student(student_id=next_id, name=name)
        students_db[next_id] = student
        next_id += 1
        return student

    @staticmethod
    def fetch_all_students() -> List[Student]:
        """
        Fetch all registered students.

        :return: A list of all Student objects.
        """
        return list(students_db.values())

    @staticmethod
    def fetch_student(student_id: int) -> Optional[Student]:
        """
        Fetch a specific student by their ID.

        :param student_id: The ID of the student to retrieve.
        :return: The Student object if found, None otherwise.
        """
        return students_db.get(student_id)

    @staticmethod
    def delete_student(student_id: int) -> bool:
        """
        Delete a student by their ID.

        :param student_id: The ID of the student to delete.
        :return: True if deletion was successful, False otherwise.
        """
        if student_id in students_db:
            del students_db[student_id]
            return True
        return False

# Flask routes would typically invoke methods from this service.
```
