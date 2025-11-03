from flask import request, jsonify
from app import app, db, Course, Teacher

@app.route('/courses/<int:course_id>/assign-teacher', methods=['PATCH'])
def assign_teacher_to_course(course_id):
    data = request.get_json()
    teacher_id = data.get('teacher_id')

    # Validate the provided teacher_id
    if not Teacher.query.get(teacher_id):
        return jsonify({"error": {"code": "E001", "message": "Teacher does not exist."}}), 400

    course = Course.query.get(course_id)
    if not course:
        return jsonify({"error": {"code": "E002", "message": "Course not found."}}), 404

    # Assign the teacher to the course
    course.teacher_id = teacher_id
    db.session.commit()
    
    # Return updated course details
    return jsonify({
        "id": course.id,
        "name": course.name,
        "level": course.level,
        "teacher_id": course.teacher_id
    }), 200

@app.route('/courses/<int:course_id>', methods=['GET'])
def get_course(course_id):
    course = Course.query.get(course_id)
    if not course:
        return jsonify({"error": {"code": "E002", "message": "Course not found."}}), 404

    teacher_info = None
    if course.teacher_id:
        teacher_info = {
            "id": course.teacher.id,
            "name": course.teacher.name,
            "email": course.teacher.email
        }

    return jsonify({
        "id": course.id,
        "name": course.name,
        "level": course.level,
        "teacher": teacher_info
    }), 200