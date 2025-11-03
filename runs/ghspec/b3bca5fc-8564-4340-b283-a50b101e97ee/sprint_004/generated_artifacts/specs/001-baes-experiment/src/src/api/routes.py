from flask import Flask, request, jsonify
from your_database_module import db  # Import your database session or engine
from your_models import Student, Course, student_courses  # Import your models

app = Flask(__name__)

# API Endpoint to retrieve courses a student is enrolled in
@app.route('/students/<int:student_id>/courses', methods=['GET'])
def get_student_courses(student_id):
    """
    Retrieve all courses the specified student is enrolled in.

    Parameters:
    - student_id (int): The ID of the student.

    Returns:
    - JSON array of course details or error message.
    """
    try:
        # Query the database to get the courses for the given student_id
        student_courses_list = db.session.query(student_courses).filter(student_courses.c.student_id == student_id).all()

        # If no courses found, return an empty array
        if not student_courses_list:
            return jsonify([]), 200

        # Extract course details
        courses = []
        for student_course in student_courses_list:
            course = db.session.query(Course).filter(Course.id == student_course.course_id).first()
            if course:
                courses.append({
                    'id': course.id,
                    'name': course.name,
                    'level': course.level
                })

        return jsonify(courses), 200

    except Exception as e:
        # Log the exception (You should implement logging properly)
        app.logger.error(f"Error retrieving courses for student {student_id}: {str(e)}")
        return jsonify({"error": {"code": "E500", "message": "Internal server error"}}), 500

# Add necessary database setup and migration logic, if required. 