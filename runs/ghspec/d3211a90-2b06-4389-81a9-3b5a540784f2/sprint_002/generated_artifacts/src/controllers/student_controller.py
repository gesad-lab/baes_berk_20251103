```python
from flask import jsonify, request
from validation import validate_student_data  # Assuming a validate_student_data function exists
from src.models.student import Student
from src import db

@app.route('/students', methods=['POST'])
def create_student():
    """
    Create a new Student entity with the provided name and email.
    
    Request body must include:
    - name (string, required)
    - email (string, required, must be in valid format)
    
    Returns:
    - 201 Created with student details on success
    - 400 Bad Request for validation errors
    """
    data = request.get_json()

    # Validate input data
    try:
        validate_student_data(data)  # Validate name and email presence and format
    except ValueError as e:
        return jsonify({
            "error": {
                "code": "E001",
                "message": str(e)
            }
        }), 400

    # Create a new Student
    new_student = Student(name=data['name'], email=data['email'])
    db.session.add(new_student)
    db.session.commit()

    response = {
        "id": new_student.id,
        "name": new_student.name,
        "email": new_student.email
    }
    return jsonify(response), 201

@app.route('/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    """
    Retrieve a Student entity by its ID.
    
    Returns:
    - 200 OK with student details on success
    - 404 Not Found if student does not exist
    """
    student = Student.query.get(student_id)
    if student is None:
        return jsonify({"error": {"code": "E002", "message": "Student not found."}}), 404

    response = {
        "name": student.name,
        "email": student.email
    }
    return jsonify(response), 200
```