```python
from flask import request, jsonify
from src.models.student import Student
from src.models.course import Course
from sqlalchemy.exc import SQLAlchemyError

@app.route('/students/<int:student_id>/courses', methods=['POST'])
def assign_courses_to_student(student_id):
    data = request.json
    course_ids = data.get('course_ids', [])

    # Validate that the student exists
    student = Student.query.get(student_id)
    if not student:
        return jsonify({"error": {"code": "E002", "message": "Student not found."}}), 404

    # Validate course IDs
    invalid_courses = [course_id for course_id in course_ids if not Course.query.get(course_id)]
    if invalid_courses:
        return jsonify({"error": {"code": "E001", "message": "One or more course IDs are invalid."}}), 400

    # Assign courses to the student
    try:
        student.course_ids = ",".join(map(str, course_ids))
        db.session.commit()
    except SQLAlchemyError as e:
        # Handle database commit errors
        db.session.rollback()  # Rollback the session to prevent inconsistent state
        return jsonify({"error": {"code": "E003", "message": "Failed to assign courses. Please try again."}}), 500

    # Respond with success message
    return jsonify({
        "message": "Courses assigned successfully.",
        "student": {
            "id": student.id,
            "name": student.name,
            "course_ids": course_ids
        }
    }), 200

@app.route('/students/<int:student_id>', methods=['GET'])
def get_student_info(student_id):
    student = Student.query.get(student_id)
    if not student:
        return jsonify({"error": {"code": "E002", "message": "Student not found."}}), 404

    # Parse course IDs
    course_ids = list(map(int, student.course_ids.split(','))) if student.course_ids else []
    return jsonify({
        "id": student.id,
        "name": student.name,
        "course_ids": course_ids
    }), 200
```