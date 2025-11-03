```python
from flask import request, jsonify
from sqlalchemy.exc import IntegrityError
from src.models import Course, Teacher
from src import db

@app.route('/courses', methods=['POST'])
def create_course():
    """Create a new course with an optional teacher assignment."""
    data = request.get_json()
    
    # Validate input
    if not data.get('course_name'):
        return {"error": {"code": "E001", "message": "Course name is required."}}, 400

    # Create new course instance
    new_course = Course(course_name=data['course_name'], teacher_id=data.get('teacher_id'))
    
    try:
        db.session.add(new_course)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return {"error": {"code": "E002", "message": "Failed to create course with the provided data."}}, 400

    return {"message": "Course created successfully."}, 201


@app.route('/courses/<int:id>', methods=['PUT'])
def update_course(id):
    """Update an existing course to assign a teacher."""
    data = request.get_json()
    teacher_id = data.get('teacher_id')
    
    # Fetch the course by ID
    course = Course.query.get(id)
    if course is None:
        return {"error": {"code": "E404", "message": "Course not found."}}, 404
    
    # Check if teacher ID is provided and exists
    if teacher_id is not None:
        teacher = Teacher.query.get(teacher_id)
        if teacher is None:
            return {"error": {"code": "E003", "message": "Teacher does not exist."}}, 400
        course.teacher_id = teacher_id

    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return {"error": {"code": "E002", "message": "Failed to update course."}}, 400

    return {"message": "Course updated successfully."}, 200
```