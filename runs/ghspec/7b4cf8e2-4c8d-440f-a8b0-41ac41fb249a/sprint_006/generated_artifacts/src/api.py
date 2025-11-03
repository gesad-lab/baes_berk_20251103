```python
from flask import Flask, jsonify, request, abort
from models import db, Course, Teacher  # Importing necessary models
from sqlalchemy.orm.exc import NoResultFound

app = Flask(__name__)

@app.route('/courses/<int:course_id>/assign-teacher/<int:teacher_id>', methods=['PUT'])
def assign_teacher(course_id, teacher_id):
    """
    Assign a teacher to a specific course by updating the course's teacher_id.

    Parameters:
    - course_id (int): The ID of the course to update.
    - teacher_id (int): The ID of the teacher to assign.

    Returns:
    - JSON response with confirmation message.
    """
    course = Course.query.get(course_id)  # Fetching the course
    if not course:
        abort(404, description="Course not found.")

    teacher = Teacher.query.get(teacher_id)  # Fetching the teacher
    if not teacher:
        abort(404, description="Teacher not found.")

    course.teacher_id = teacher.id  # Assigning the teacher to the course
    db.session.commit()  # Persisting changes to the database

    return jsonify({"message": "Teacher assigned to the course successfully."}), 200

@app.route('/courses/<int:course_id>/unassign-teacher', methods=['DELETE'])
def unassign_teacher(course_id):
    """
    Remove the teacher assignment from a specific course.

    Parameters:
    - course_id (int): The ID of the course to update.

    Returns:
    - JSON response with confirmation message.
    """
    course = Course.query.get(course_id)  # Fetching the course
    if not course:
        abort(404, description="Course not found.")

    course.teacher_id = None  # Removing the teacher assignment
    db.session.commit()  # Persisting changes to the database

    return jsonify({"message": "Teacher unassigned from the course successfully."}), 200

@app.route('/courses/<int:course_id>', methods=['GET'])
def get_course(course_id):
    """
    Retrieve the details of a specific course, including the assigned teacher.

    Parameters:
    - course_id (int): The ID of the course to retrieve.

    Returns:
    - JSON response containing course details.
    """
    course = Course.query.get(course_id)
    if not course:
        abort(404, description="Course not found.")

    course_data = {
        "id": course.id,
        "name": course.name,
        "teacher_id": course.teacher_id,
        "assigned_teacher": None
    }

    if course.teacher_id:
        teacher = Teacher.query.get(course.teacher_id)
        if teacher:
            course_data["assigned_teacher"] = {"id": teacher.id, "name": teacher.name}

    return jsonify(course_data), 200

@app.route('/courses', methods=['GET'])
def list_courses():
    """
    Retrieve a list of all courses, along with their assigned teachers.

    Returns:
    - JSON response containing a list of all courses.
    """
    courses = Course.query.all()  # Fetching all courses
    courses_data = []

    for course in courses:
        course_data = {
            "id": course.id,
            "name": course.name,
            "teacher_id": course.teacher_id,
            "assigned_teacher": None
        }

        if course.teacher_id:
            teacher = Teacher.query.get(course.teacher_id)
            if teacher:
                course_data["assigned_teacher"] = {"id": teacher.id, "name": teacher.name}

        courses_data.append(course_data)

    return jsonify(courses_data), 200
```