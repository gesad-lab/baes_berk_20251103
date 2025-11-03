```python
from flask import Flask, request, jsonify
from src.services.student_service import StudentService

app = Flask(__name__)
student_service = StudentService()

@app.route('/students', methods=['POST'])
def create_student():
    """Create a new student with the provided name."""
    data = request.get_json()

    # Validate input data
    if not data or 'name' not in data or not data['name']:
        return jsonify({"error": {"code": "E001", "message": "Name is required"}}), 400

    try:
        student = student_service.add_student(data['name'])
    except Exception as e:
        # Log the exception for debugging
        app.logger.error(f"Error creating student: {e}")
        return jsonify({"error": {"code": "E002", "message": "Failed to create student. Please try again later."}}), 500

    return jsonify(student), 201

@app.route('/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    """Retrieve a student's details by ID."""
    try:
        student = student_service.get_student_by_id(student_id)
    except Exception as e:
        # Log the exception for debugging
        app.logger.error(f"Error retrieving student with ID {student_id}: {e}")
        return jsonify({"error": {"code": "E003", "message": "Failed to retrieve student. Please try again later."}}), 500

    if student is None:
        return jsonify({"error": {"code": "E004", "message": "Student not found"}}), 404

    return jsonify(student), 200

if __name__ == '__main__':
    app.run(debug=True)
```