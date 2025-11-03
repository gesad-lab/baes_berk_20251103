```python
# routes.py
from flask import request, jsonify
from .models import db, Course, Teacher

@app.route('/api/v1/courses/<int:course_id>/assign_teacher', methods=['POST'])
def assign_teacher_to_course(course_id):
    """Assign a teacher to a specific course."""
    data = request.json
    
    # Validate that teacher_id is provided and it corresponds to an existing Teacher
    teacher_id = data.get('teacher_id')
    if not isinstance(teacher_id, int) or teacher_id <= 0 or not Teacher.query.get(teacher_id):
        return jsonify({'error': {'code': 'E001', 'message': 'Valid teacher ID must be provided.'}}), 400
    
    # Check if the course exists
    course = Course.query.get(course_id)
    if not course:
        return jsonify({'error': {'code': 'E002', 'message': 'Course not found.'}}), 404

    # Assign the teacher to the course
    course.teacher_id = teacher_id
    db.session.commit()

    return jsonify({'message': 'Teacher assigned successfully to course.'}), 200

@app.route('/api/v1/courses/<int:course_id>', methods=['GET'])
def get_course_details(course_id):
    """Retrieve detailed information of a specific course, including teacher details."""
    # Fetch the course details
    course = Course.query.get(course_id)
    if not course:
        return jsonify({'error': {'code': 'E002', 'message': 'Course not found.'}}), 404
    
    # Retrieve teacher info if assigned
    teacher = Teacher.query.get(course.teacher_id)
    teacher_info = {"name": teacher.name, "email": teacher.email} if teacher else None

    return jsonify({
        'id': course.id,
        'title': course.title,
        'description': course.description,
        'teacher': teacher_info
    }), 200
```