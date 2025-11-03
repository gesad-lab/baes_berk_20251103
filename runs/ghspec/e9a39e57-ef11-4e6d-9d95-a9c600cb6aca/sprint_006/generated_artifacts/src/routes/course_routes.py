```python
from flask import jsonify, request
from src.models.course import Course  # Assuming the Course model exists
from src.models.teacher import Teacher  # Importing the Teacher model
from src import db  # Assuming db is initialized in the src module

# Endpoint to assign a teacher to a course
@app.route('/courses/<int:course_id>/assign_teacher', methods=['POST'])
def assign_teacher(course_id):
    data = request.json
    teacher_id = data.get('teacher_id')

    if not isinstance(teacher_id, int):
        return jsonify({"error": {"code": "E001", "message": "Invalid teacher ID format. It should be an integer."}}), 400

    # Fetch the course and teacher from the database
    course = Course.query.get(course_id)
    teacher = Teacher.query.get(teacher_id)

    # Check if the course exists
    if course is None:
        return jsonify({"error": {"code": "E002", "message": "Course not found."}}), 404

    # Check if the teacher exists
    if teacher is None:
        return jsonify({"error": {"code": "E003", "message": "Teacher not found."}}), 404

    # Assign the teacher to the course
    course.teacher_id = teacher_id
    db.session.commit()

    return jsonify({"message": "Teacher assigned successfully.", "course": course.to_dict()}), 200

# Endpoint to retrieve course information including assigned teacher details
@app.route('/courses/<int:course_id>', methods=['GET'])
def get_course_info(course_id):
    course = Course.query.get(course_id)

    # Check if the course exists
    if course is None:
        return jsonify({"error": {"code": "E002", "message": "Course not found."}}), 404

    # Convert course details to a response format
    course_details = {
        "id": course.id,
        "name": course.name,
        "level": course.level,
        "teacher_id": course.teacher_id,
        "teacher_name": course.teacher.name if course.teacher else None,
        "teacher_email": course.teacher.email if course.teacher else None,
    }
    return jsonify(course_details), 200

# Migration setup instructions:
# Use Alembic to run migrations. Below is the expected command:
# alembic revision --autogenerate -m "Add teacher_id to Course"
# alembic upgrade head
```