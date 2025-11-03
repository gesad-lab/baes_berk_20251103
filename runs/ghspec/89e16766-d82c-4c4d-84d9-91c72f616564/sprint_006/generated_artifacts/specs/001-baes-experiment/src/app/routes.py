```python
from flask import jsonify, request
from app import app, db
from app.models import Course, Teacher

@app.route('/courses/<int:course_id>/teachers', methods=['POST'])
def associate_teacher_with_course(course_id):
    """
    Associate a teacher with a course.
    
    Parameters:
    - course_id: ID of the course to associate the teacher with.
    
    Request Body:
    - teacher_id: ID of the teacher to associate with the course.
    
    Returns:
    - JSON response with success message and updated course details
    or an error message if the teacher does not exist.
    """
    data = request.get_json()
    teacher_id = data.get('teacher_id')

    # Check if teacher exists
    if not Teacher.query.get(teacher_id):
        return jsonify({"error": {"code": "E002", "message": "The specified teacher does not exist."}}), 404

    course = Course.query.get_or_404(course_id)
    course.teacher_id = teacher_id
    db.session.commit()

    return jsonify({
        "message": "Teacher associated with course successfully.", 
        "course": {
            "id": course.id, 
            "teacher_id": course.teacher_id
        }
    }), 200

@app.route('/courses/<int:course_id>', methods=['GET'])
def get_course_with_teacher(course_id):
    """
    Retrieve course details including the associated teacher's info.
    
    Parameters:
    - course_id: ID of the course to retrieve.
    
    Returns:
    - JSON response with course details and teacher's name and email
    or an appropriate error if the course is not found.
    """
    course = Course.query.get_or_404(course_id)

    # Get teacher info if associated
    if course.teacher_id:
        teacher = Teacher.query.get(course.teacher_id)
        teacher_info = {"name": teacher.name, "email": teacher.email}
    else:
        teacher_info = None

    return jsonify({
        "id": course.id, 
        "teacher": teacher_info
    }), 200
```