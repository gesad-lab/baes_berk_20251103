```python
from flask import Blueprint, request, jsonify
from src.models import StudentCourse  # Assuming StudentCourse class is defined in models.py
from src.schemas import StudentCourseSchema  # Assuming StudentCourseSchema class is defined in schemas.py
from src import db  # Database instance

routes = Blueprint('routes', __name__)

@student.route('/students/<int:student_id>/courses', methods=['POST'])
def add_course_to_student(student_id):
    """Associate a course with a student."""
    schema = StudentCourseSchema()
    
    # Validate request data
    try:
        data = schema.load(request.json)
    except ValidationError as err:
        return jsonify({"error": {"code": "E001", "message": "Invalid input data", "details": err.messages}}), 400

    # Create a new StudentCourse relationship
    student_course = StudentCourse(student_id=student_id, course_id=data['course_id'])
    
    db.session.add(student_course)
    db.session.commit()
    
    return jsonify({"message": "Course associated with student successfully."}), 201


@student.route('/students/<int:student_id>/courses', methods=['GET'])
def get_student_courses(student_id):
    """Retrieve courses associated with a student."""
    courses = StudentCourse.query.filter_by(student_id=student_id).all()
    course_list = [{"course_id": sc.course_id} for sc in courses]

    return jsonify(course_list), 200


@student.route('/students/<int:student_id>/courses/<int:course_id>', methods=['DELETE'])
def remove_course_from_student(student_id, course_id):
    """Remove a course association from a student."""
    student_course = StudentCourse.query.filter_by(student_id=student_id, course_id=course_id).first()
    
    if not student_course:
        return jsonify({"error": {"code": "E002", "message": "Course association not found."}}), 404

    db.session.delete(student_course)
    db.session.commit()
    
    return jsonify({"message": "Course removed from student successfully."}), 200
```