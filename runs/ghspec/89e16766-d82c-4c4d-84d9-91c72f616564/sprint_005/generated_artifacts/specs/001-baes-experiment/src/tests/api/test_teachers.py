from flask import jsonify, request
from app import app, db
from app.models import Teacher
import re

@app.route('/teachers', methods=['POST'])
def create_teacher():
    data = request.get_json()

    # Input validation logic
    name = data.get('name')
    email = data.get('email')

    if not name or not isinstance(name, str) or len(name.strip()) == 0:
        return jsonify({"error": {"code": "E001", "message": "Invalid input: Name is required and must be a non-empty string."}}), 400

    if not email or not isinstance(email, str) or not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return jsonify({"error": {"code": "E002", "message": "Invalid input: Email is required and must be a valid email format."}}), 400

    # Create the teacher if validation passes
    teacher = Teacher(name=name.strip(), email=email.strip())
    db.session.add(teacher)
    db.session.commit()

    return jsonify({"message": "Teacher created successfully.", "teacher": {"id": teacher.id, "name": teacher.name, "email": teacher.email}}), 201

@app.route('/teachers/<int:teacher_id>', methods=['GET'])
def get_teacher(teacher_id):
    teacher = Teacher.query.get_or_404(teacher_id)
    return jsonify({"id": teacher.id, "name": teacher.name, "email": teacher.email})