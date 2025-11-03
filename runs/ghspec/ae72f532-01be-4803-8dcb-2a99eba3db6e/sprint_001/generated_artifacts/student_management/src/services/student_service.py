```python
"""student_service.py

Provides services for managing student data, including creating and retrieving
students through the data access layer.
"""

from src.dal.student_dal import create_student_record, retrieve_all_students
from src.models.student import Student
from flask import jsonify, abort

def create_student(student_data):
    """Create a new student record.

    Args:
        student_data (dict): A dictionary containing the student information.

    Returns:
        Response: A JSON response with status code 201 upon successful creation or an error message.
    """
    name = student_data.get('name')
    if not name:
        # If the 'name' field is missing, abort with a 400 error
        abort(400, description='E001: Name is required.')

    # Create the student record in the database
    student_id = create_student_record(name)
    
    # Return the created student information
    return jsonify({'id': student_id, 'name': name}), 201

def get_students():
    """Retrieve all student records.

    Returns:
        Response: A JSON array containing all student records.
    """
    students = retrieve_all_students()
    return jsonify([student.serialize() for student in students])
```