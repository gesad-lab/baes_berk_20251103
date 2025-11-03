```python
from flask import Flask, request, jsonify
from models import db, Course, Teacher  # Assuming these models are defined in models module
from marshmallow import Schema, fields, ValidationError

app = Flask(__name__)


class CourseTeacherAssignmentSchema(Schema):
    """Schema for validating course and teacher assignment inputs."""
    course_id = fields.Int(required=True)
    teacher_id = fields.Int(required=True)


@app.route('/assign_teacher', methods=['POST'])
def assign_teacher_to_course():
    """Assign a teacher to a course and return confirmation."""
    data = request.json
    schema = CourseTeacherAssignmentSchema()

    # Validate input data
    try:
        validated_data = schema.load(data)
    except ValidationError as err:
        return jsonify({"error": {"code": "E002", "message": "Invalid input", "details": err.messages}}), 400

    course_id = validated_data['course_id']
    teacher_id = validated_data['teacher_id']

    # Check if the course exists
    course = Course.query.get(course_id)
    if not course:
        return jsonify({"error": {"code": "E003", "message": "Course not found"}}), 404

    # Check if the teacher exists
    teacher = Teacher.query.get(teacher_id)
    if not teacher:
        return jsonify({"error": {"code": "E004", "message": "Teacher not found"}}), 404

    # Assign the teacher to the course
    course.teacher_id = teacher_id
    db.session.commit()

    return jsonify({"message": "Teacher assigned to course successfully"}), 200


@app.route('/course/<int:course_id>', methods=['GET'])
def get_course_details(course_id):
    """Retrieve course details along with the assigned teacher's name."""
    course = Course.query.get(course_id)
    if not course:
        return jsonify({"error": {"code": "E003", "message": "Course not found"}}), 404

    # Prepare response data
    course_details = {
        "course_id": course.id,
        "course_name": course.name,
        "assigned_teacher": course.teacher.name if course.teacher else None
    }

    return jsonify(course_details), 200


if __name__ == "__main__":
    app.run(debug=True)
```