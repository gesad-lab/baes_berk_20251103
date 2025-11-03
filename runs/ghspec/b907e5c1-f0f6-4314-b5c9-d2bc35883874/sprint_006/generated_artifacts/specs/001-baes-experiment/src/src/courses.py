```python
from flask import Flask, jsonify, request, abort
from models import Course, Teacher
from database import db_session

app = Flask(__name__)

@app.route('/courses/<int:course_id>/assign-teacher', methods=['PUT'])
def assign_teacher_to_course(course_id):
    """Assign a teacher to a course by course_id."""
    data = request.get_json()
    teacher_id = data.get('teacher_id')

    if not teacher_id:
        abort(400, {"error": {"code": "E001", "message": "teacher_id must be provided."}})

    course = db_session.query(Course).filter(Course.id == course_id).first()
    if not course:
        abort(404, {"error": {"code": "E002", "message": "Course not found."}})

    # Validate if the teacher exists
    teacher = db_session.query(Teacher).filter(Teacher.id == teacher_id).first()
    if not teacher:
        abort(404, {"error": {"code": "E003", "message": "Teacher not found."}})

    # Assign the teacher to the course
    course.teacher_id = teacher_id
    db_session.commit()

    return jsonify({
        "id": course.id,
        "name": course.name,
        "description": course.description,
        "teacher_id": course.teacher_id
    }), 200

@app.route('/courses/<int:course_id>', methods=['GET'])
def get_course_details(course_id):
    """Retrieve details of a specific course, including assigned teacher information."""
    course = db_session.query(Course).filter(Course.id == course_id).first()
    if not course:
        abort(404, {"error": {"code": "E002", "message": "Course not found."}})

    teacher = db_session.query(Teacher).filter(Teacher.id == course.teacher_id).first()
    teacher_info = {
        "id": teacher.id,
        "name": teacher.name
    } if teacher else None

    return jsonify({
        "id": course.id,
        "name": course.name,
        "description": course.description,
        "teacher": teacher_info
    }), 200

@app.route('/courses', methods=['GET'])
def list_courses():
    """Retrieve a list of all courses with teacher information."""
    courses = db_session.query(Course).all()
    results = []
    
    for course in courses:
        teacher = db_session.query(Teacher).filter(Teacher.id == course.teacher_id).first()
        teacher_info = {
            "id": teacher.id,
            "name": teacher.name
        } if teacher else None
        
        results.append({
            "id": course.id,
            "name": course.name,
            "description": course.description,
            "teacher": teacher_info
        })

    return jsonify(results), 200

if __name__ == '__main__':
    app.run()
```