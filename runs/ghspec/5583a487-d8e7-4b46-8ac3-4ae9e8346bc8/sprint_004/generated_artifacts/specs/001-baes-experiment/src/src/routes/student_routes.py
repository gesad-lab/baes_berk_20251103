```python
from flask import jsonify, request
from app import app, db, Student, Course  # Import Student and Course models from the main application
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

# Define the route to retrieve a student by ID along with their associated courses
@app.route('/students/<int:id>', methods=['GET'])
def get_student_with_courses(id):
    student = Student.query.get(id)  # Retrieve student by ID
    if not student:
        return jsonify({"error": {"code": "E001", "message": "Student not found."}}), 404

    # Load associated courses
    courses = [{'course_id': course.id, 'course_name': course.name} for course in student.courses]

    return jsonify({
        'id': student.id,
        'name': student.name,
        'courses': courses
    }), 200

# Define the route to associate courses to a student
@app.route('/students/<int:id>/courses', methods=['PUT'])
def associate_courses(id):
    data = request.get_json()

    if not data or 'course_ids' not in data or not data['course_ids']:
        return jsonify({
            'error': {
                'code': 'E002',
                'message': 'At least one course must be selected.'
            }
        }), 400

    student = Student.query.get(id)  # Retrieve student by ID
    if not student:
        return jsonify({"error": {"code": "E001", "message": "Student not found."}}), 404

    # Clear existing associations
    student.courses.clear()  

    # Validate and associate the selected courses
    for course_id in data['course_ids']:
        course = Course.query.get(course_id)
        if not course:
            return jsonify({
                'error': {
                    'code': 'E003',
                    'message': f'Course ID {course_id} does not exist.'
                }
            }), 400
        student.courses.append(course)  # Append the course to the student's course list

    try:
        db.session.commit()  # Commit the changes to the database
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": {"code": "E004", "message": "Failed to associate courses."}}), 500

    return jsonify({"message": "Courses associated with the student successfully."}), 200
```