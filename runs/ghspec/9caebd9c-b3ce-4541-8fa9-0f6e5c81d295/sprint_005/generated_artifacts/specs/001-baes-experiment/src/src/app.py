```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from your_application.models import Teacher  # Adjust import based on your structure
from your_application.validators import validate_teacher_creation  # Adjust import based on your structure

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'  # Adjust as necessary
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

@app.route('/teachers', methods=['POST'])
def create_teacher():
    """
    Create a new Teacher.
    Request body should contain JSON with 'name' and 'email'.

    Returns JSON confirmation message or error message if validation fails.
    """
    data = request.get_json()

    # Validate input
    validation_error = validate_teacher_creation(data)
    if validation_error:
        return jsonify({"error": validation_error}), 400

    # Create a new Teacher instance
    new_teacher = Teacher(name=data['name'], email=data['email'])

    try:
        db.session.add(new_teacher)
        db.session.commit()
        return jsonify({"message": "Teacher created successfully", "teacher_id": new_teacher.id}), 201
    except Exception as e:
        db.session.rollback()  # Rollback in case of error
        return jsonify({"error": "Could not create teacher", "details": str(e)}), 500

@app.route('/teachers/<int:teacher_id>', methods=['GET'])
def get_teacher(teacher_id):
    """
    Retrieve teacher information by their unique identifier.

    Returns JSON object with teacher details or an error message.
    """
    teacher = Teacher.query.get(teacher_id)

    if teacher is None:
        return jsonify({"error": "Teacher not found"}), 404

    return jsonify({
        "id": teacher.id,
        "name": teacher.name,
        "email": teacher.email
    }), 200

if __name__ == '__main__':
    app.run(debug=True)
```