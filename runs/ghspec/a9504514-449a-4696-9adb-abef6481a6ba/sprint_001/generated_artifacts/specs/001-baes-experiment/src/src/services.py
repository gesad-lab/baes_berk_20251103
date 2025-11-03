```python
from flask import jsonify, request
from models import db, Student

def create_student():
    """
    Create a new student from the incoming request data.

    Returns:
        JSON response with success message and student details or error message.
    """
    data = request.get_json()

    # Input validation: Check if 'name' is provided
    if not data or 'name' not in data or not data['name']:
        return jsonify({
            "error": {
                "code": "E001",
                "message": "Name field is required."
            }
        }), 400  # Return 400 Bad Request

    student_name = data['name']

    # Create a new student instance
    new_student = Student(name=student_name)

    # Add the new student to the session and commit to the database
    db.session.add(new_student)
    db.session.commit()

    return jsonify({
        "success": True,
        "student": {
            "id": new_student.id,
            "name": new_student.name
        }
    }), 201  # Return 201 Created

def retrieve_students():
    """
    Retrieve a list of all students from the database.

    Returns:
        JSON response containing a list of student names.
    """
    students = Student.query.all()
    student_list = [{"id": student.id, "name": student.name} for student in students]

    return jsonify(student_list), 200  # Return 200 OK
```