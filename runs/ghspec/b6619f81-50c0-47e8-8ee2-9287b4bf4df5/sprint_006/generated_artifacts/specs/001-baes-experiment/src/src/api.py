```python
from flask import Flask, jsonify, request, abort
from models import Course, Teacher  # Assuming models.py contains Course and Teacher definitions
from repositories import CourseRepository, TeacherRepository  # Assuming these exist for database interactions

app = Flask(__name__)

@app.route('/courses/<int:course_id>', methods=['GET'])
def get_course(course_id):
    """
    Retrieve course information including the assigned teacher.

    Parameters:
    course_id (int): The ID of the course to retrieve information for.

    Returns:
    JSON response containing course details and assigned teacher information.
    """
    # Retrieve course from the repository
    course = CourseRepository.get_course_by_id(course_id)
    
    # If the course does not exist, return a 404 error
    if course is None:
        abort(404, description="Course not found")

    # Prepare the response data
    response = {
        "course_id": course.id,
        "name": course.name,
        "level": course.level,
        "teacher": None
    }

    # If the course has an assigned teacher, include their information
    if course.teacher_id is not None:
        teacher = TeacherRepository.get_teacher_by_id(course.teacher_id)
        if teacher:
            response["teacher"] = {
                "teacher_id": teacher.id,
                "name": teacher.name,
                "email": teacher.email
            }

    return jsonify(response), 200
```