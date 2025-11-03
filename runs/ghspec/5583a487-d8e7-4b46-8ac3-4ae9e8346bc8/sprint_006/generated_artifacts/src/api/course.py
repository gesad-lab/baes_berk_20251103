```python
from flask import jsonify, request, abort
from app import app, db
from app.models import Course, Teacher  # Import Course and Teacher models

@app.route('/courses', methods=['POST'])
def create_course():
    """Create a new Course record.

    Request body must contain `name` (string) and `teacher_id` (integer).
    Returns a confirmation message with status code 201 for success,
    or descriptive error messages with status code 400 for validation failures.
    """
    data = request.get_json()

    # Validate input
    name = data.get('name')
    teacher_id = data.get('teacher_id')

    if not name or not isinstance(name, str):
        abort(400, description="E001: Course name is required and must be a string")
    
    if not teacher_id or not isinstance(teacher_id, int):
        abort(400, description="E002: Valid teacher_id is required and must be an integer")

    # Check if the teacher exists
    teacher = Teacher.query.get(teacher_id)
    if teacher is None:
        abort(400, description=f"E003: Teacher with id {teacher_id} does not exist")

    # Create new course
    new_course = Course(name=name, teacher_id=teacher_id)
    db.session.add(new_course)
    db.session.commit()

    return jsonify({"message": "Course created successfully", "course_id": new_course.id}), 201

@app.route('/courses/<int:id>', methods=['GET'])
def get_course(id):
    """Retrieve a Course record by its ID.

    Returns the Course details in JSON format along with associated Teacher information.
    """
    course = Course.query.get_or_404(id)  # Get course or return 404

    course_data = {
        "id": course.id,
        "name": course.name,
        "teacher": {
            "id": course.teacher.id,
            "name": course.teacher.name
        }
    }

    return jsonify(course_data), 200
```