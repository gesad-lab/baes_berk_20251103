```python
from flask import request, jsonify
from src.models.course import Course
from src.models.teacher import Teacher
from src.app import db
from src.migrations import migrate  # Importing the migration function

def create_app(config=None):
    app = Flask(__name__)
    app.config.from_object(config or 'src.config.default')

    # Integrate migration setup at startup
    with app.app_context():
        migrate()  # Ensure migrations are applied during startup

    return app

@app.route('/courses/<int:course_id>/assign-teacher', methods=['PUT'])
def assign_teacher(course_id):
    course = Course.query.get(course_id)
    if not course:
        return jsonify({"error": {"code": "E001", "message": "Invalid course ID."}}), 400

    data = request.json
    teacher_id = data.get('teacher_id')

    if not Teacher.query.get(teacher_id):
        return jsonify({"error": {"code": "E001", "message": "Invalid teacher ID."}}), 400

    course.teacher_id = teacher_id
    db.session.commit()

    return jsonify({
        "message": "Teacher assigned successfully.",
        "course": {
            "id": course.id,
            "name": course.name,
            "level": course.level,
            "teacher_id": course.teacher_id
        }
    }), 200

@app.route('/courses/<int:course_id>', methods=['GET'])
def get_course(course_id):
    course = Course.query.get(course_id)
    if not course:
        return jsonify({"error": {"code": "E002", "message": "Course not found."}}), 404

    teacher = Teacher.query.get(course.teacher_id) if course.teacher_id else None

    response = {
        "id": course.id,
        "name": course.name,
        "level": course.level
    }

    if teacher:
        response["teacher"] = {
            "id": teacher.id,
            "name": teacher.name,
            "email": teacher.email
        }

    return jsonify(response), 200
```