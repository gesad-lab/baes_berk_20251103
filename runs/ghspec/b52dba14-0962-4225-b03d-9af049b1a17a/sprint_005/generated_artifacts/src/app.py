```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from src.models.teacher_model import Teacher  # Assuming a teacher_model exists with the Teacher entity

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///path_to_your_db'
db = SQLAlchemy(app)

@app.route('/teachers', methods=['POST'])
def create_teacher():
    """Create a new teacher.

    The request must contain both 'name' and 'email' fields.
    Returns a success message or an error if validation fails.
    """
    data = request.get_json()

    # Validate input
    if 'name' not in data or 'email' not in data:
        return jsonify({'error': {'code': 'E001', 'message': 'Both name and email are required'}}), 400
    
    # Validate email format
    if not isinstance(data['email'], str) or '@' not in data['email']:
        return jsonify({'error': {'code': 'E002', 'message': 'Invalid email format'}}), 400

    # Create and add the teacher to the database
    new_teacher = Teacher(name=data['name'], email=data['email'])
    try:
        db.session.add(new_teacher)
        db.session.commit()
        return jsonify({'message': 'Teacher created successfully'}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': {'code': 'E003', 'message': 'Teacher with this email already exists'}}), 409

@app.route('/teachers/<int:teacher_id>', methods=['GET'])
def get_teacher(teacher_id):
    """Retrieve the information of a teacher by ID.
    
    Returns the teacher's details in JSON format or an error if not found.
    """
    teacher = Teacher.query.get(teacher_id)
    
    if not teacher:
        return jsonify({'error': {'code': 'E004', 'message': 'Teacher not found'}}), 404

    return jsonify({'id': teacher.id, 'name': teacher.name, 'email': teacher.email}), 200

if __name__ == '__main__':
    # Check database migrations and run app
    with app.app_context():
        db.create_all()  # This will execute migrations and create teachers table if it does not exist
    app.run(debug=True)
```