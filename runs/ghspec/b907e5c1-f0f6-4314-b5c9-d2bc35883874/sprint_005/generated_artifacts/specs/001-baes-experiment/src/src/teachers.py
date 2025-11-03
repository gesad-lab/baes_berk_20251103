```python
# src/teachers.py

from flask import Flask, request, jsonify
from datetime import datetime
from models import Teacher  # Assuming Teacher model is defined in models.py
from database import db_session  # Assume db_session for database interactions

app = Flask(__name__)

@app.route('/teachers', methods=['POST'])
def create_teacher():
    start_time = datetime.now()  # Start time for measuring response
    
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')

    # Validate inputs
    if not name or not email:
        return jsonify({"error": {"code": "E001", "message": "Name and email are required."}}), 400
    
    # Basic email format validation
    if "@" not in email or "." not in email.split("@")[-1]:
        return jsonify({"error": {"code": "E002", "message": "Invalid email format."}}), 400

    # Create a new Teacher instance
    teacher = Teacher(name=name, email=email)
    
    # Add the teacher to the database
    db_session.add(teacher)
    db_session.commit()

    response_time = (datetime.now() - start_time).total_seconds() * 1000  # Convert to milliseconds
    
    # Check response time requirement
    if response_time >= 200:
        app.logger.warning(f"Response time exceeded: {response_time}ms")

    # Return the created teacher's data
    return jsonify({"id": teacher.id, "name": teacher.name, "email": teacher.email}), 201

@app.route('/teachers/<int:teacher_id>', methods=['GET'])
def get_teacher(teacher_id):
    start_time = datetime.now()  # Start time for measuring response
    
    teacher = Teacher.query.get(teacher_id)

    if not teacher:
        return jsonify({"error": {"code": "E003", "message": "Teacher not found."}}), 404

    response_time = (datetime.now() - start_time).total_seconds() * 1000  # Convert to milliseconds
    
    # Check response time requirement
    if response_time >= 200:
        app.logger.warning(f"Response time exceeded: {response_time}ms")

    # Return the teacher's data
    return jsonify({"id": teacher.id, "name": teacher.name, "email": teacher.email}), 200

@app.route('/teachers', methods=['GET'])
def list_teachers():
    start_time = datetime.now()  # Start time for measuring response
    
    teachers = Teacher.query.all()
    response_time = (datetime.now() - start_time).total_seconds() * 1000  # Convert to milliseconds
    
    # Check response time requirement
    if response_time >= 200:
        app.logger.warning(f"Response time exceeded: {response_time}ms")

    # Return a list of teachers
    return jsonify([{"id": teacher.id, "name": teacher.name, "email": teacher.email} for teacher in teachers]), 200

if __name__ == '__main__':
    app.run()
```