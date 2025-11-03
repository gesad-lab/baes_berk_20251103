from flask import jsonify, request
from app import app, db
from app.models import Teacher
from sqlalchemy.exc import IntegrityError

@app.route('/teachers', methods=['POST'])
def create_teacher():
    data = request.get_json()
    
    # Extract name and email from the request data
    name = data.get('name')
    email = data.get('email')
    
    # Validate input data
    if not name:
        return jsonify({"error": {"code": "E001", "message": "Name is required."}}), 400
    if not email:
        return jsonify({"error": {"code": "E002", "message": "Email is required."}}), 400

    # Create a new Teacher object
    teacher = Teacher(name=name, email=email)
    
    # Attempt to add the new teacher to the database
    try:
        db.session.add(teacher)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": {"code": "E003", "message": "Email already exists."}}), 400
    
    # Return success response with created teacher details
    return jsonify({"message": "Teacher created successfully.", "teacher": {"id": teacher.id, "name": teacher.name, "email": teacher.email}}), 201

@app.route('/teachers/<int:teacher_id>', methods=['GET'])
def get_teacher(teacher_id):
    # Retrieve the teacher by ID, or return 404 if not found
    teacher = Teacher.query.get_or_404(teacher_id)
    return jsonify({"id": teacher.id, "name": teacher.name, "email": teacher.email})