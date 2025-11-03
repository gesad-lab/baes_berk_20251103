from flask import Flask, request, jsonify
from your_application import db
from your_application.models import Teacher  # Assuming Teacher model will be created in models.py
from your_application.validators import validate_teacher_creation  # Assuming validation logic will be in validators.py

app = Flask(__name__)

@app.route('/teachers', methods=['POST'])
def create_teacher():
    """
    Create a new Teacher.

    Request Body:
    - JSON containing 'name' and 'email' fields.

    Returns:
    - JSON confirmation message on success, or an error message if required fields are missing.
    """
    data = request.get_json()

    # Validate input data
    validation_error = validate_teacher_creation(data)
    if validation_error:
        return jsonify({'error': validation_error}), 400

    # Create a new Teacher instance
    new_teacher = Teacher(name=data['name'], email=data['email'])
    db.session.add(new_teacher)
    db.session.commit()

    return jsonify({'message': 'Teacher created successfully', 'teacher_id': new_teacher.id}), 201

@app.route('/teachers/<int:teacher_id>', methods=['GET'])
def get_teacher(teacher_id):
    """
    Retrieve the information of a Teacher.

    Args:
    - teacher_id: The unique identifier of the Teacher.

    Returns:
    - JSON object containing the details of the requested Teacher or an error message if not found.
    """
    teacher = Teacher.query.get(teacher_id)

    if not teacher:
        return jsonify({'error': {'code': 'E404', 'message': 'Teacher not found'}}), 404

    # Return the teacher information
    return jsonify({
        'id': teacher.id,
        'name': teacher.name,
        'email': teacher.email
    }), 200

# Ensure the app is actually running the routes when executed
if __name__ == "__main__":
    app.run(debug=True)