```python
from flask import jsonify, request
from app import app, db
from app.models.student import Student

@app.route('/students', methods=['GET'])
def get_students():
    """Retrieve all students from the database.

    Returns:
        JSON: A list of student objects, each containing the student's ID, name, and email.
    """
    try:
        students = Student.query.all()  # Retrieve all student records from the database
        return jsonify([{"id": student.id, "name": student.name, "email": student.email} for student in students]), 200
    except Exception as e:
        # Log the exception with context (could use logging library instead)
        return jsonify({"error": {"code": "E500", "message": "An unexpected error occurred while retrieving students."}}), 500
```