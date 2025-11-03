```python
from flask import Blueprint, request, jsonify
from models.student import Student  # Assuming the Student model is in models/student.py
from models.course import Course  # Assuming the Course model is in models/course.py
from database import session  # Assuming the database session is managed in database.py
from models.student_course import student_courses  # Junction table model for Student-Course associations

students_bp = Blueprint('students', __name__)

@students_bp.route('/students/<int:student_id>/courses', methods=['POST'])
def associate_courses_with_student(student_id):
    data = request.json

    # Validate the incoming data for course IDs
    if 'course_ids' not in data or not isinstance(data['course_ids'], list):
        return jsonify({"error": {"code": "E003", "message": "Invalid course_ids format. Must be an array."}}), 400
    
    student = session.query(Student).filter_by(id=student_id).first()
    if not student:
        return jsonify({"error": {"code": "E002", "message": "Student does not exist."}}), 404

    for course_id in data['course_ids']:
        # Assuming you handle duplicate associations at this point
        association = student_courses.insert().values(student_id=student_id, course_id=course_id)
        session.execute(association)

    session.commit()

    return jsonify({"message": "Courses associated successfully."}), 200

@students_bp.route('/students/<int:student_id>', methods=['GET'])
def get_student_with_courses(student_id):
    student = session.query(Student).filter_by(id=student_id).first()
    if not student:
        return jsonify({"error": {"code": "E002", "message": "Student does not exist."}}), 404

    # Fetch associated course IDs for the student
    course_ids = session.query(student_courses.c.course_id).filter_by(student_id=student_id).all()
    course_ids = [course_id for (course_id,) in course_ids]  # Flatten the list to get a simple list of course IDs

    # Return student details along with associated courses
    return jsonify({
        "id": student.id,
        "name": student.name,
        "email": student.email,
        "courses": course_ids  # List of associated course IDs
    }), 200

@students_bp.route('/students/<int:student_id>/courses/<int:course_id>', methods=['DELETE'])
def remove_course_from_student(student_id, course_id):
    # Function to remove a specific course association from a student
    pass  # Implementation for course removal will go here
```