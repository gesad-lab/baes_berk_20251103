```python
from flask import Flask, jsonify, request, abort
from src.models import db, Student, Course

app = Flask(__name__)

@app.route('/students/<int:student_id>/courses', methods=['GET'])
def get_student_courses(student_id):
    """
    Retrieve all courses a specific student is enrolled in.
    
    Args:
        student_id (int): The ID of the student whose courses are to be retrieved.

    Returns:
        Response: A JSON list of enrolled courses or a 404 error if the student is not found.
    """
    # Check if the student exists
    student = Student.query.get(student_id)
    if not student:
        abort(404, description=f"Student with ID {student_id} not found.")

    # Retrieve the courses the student is enrolled in
    enrolled_courses = student.enrolled_courses  # Assuming this relationship is established in the Student model
    
    # Prepare the response data
    courses_list = [
        {
            'course_id': course.id,
            'name': course.name,
            'level': course.level
        }
        for course in enrolled_courses
    ]

    return jsonify(courses_list), 200
```