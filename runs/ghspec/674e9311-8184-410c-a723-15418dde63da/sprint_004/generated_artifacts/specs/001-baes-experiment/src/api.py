from flask import Flask, jsonify, request
from sqlalchemy.exc import IntegrityError
from src.models.student_course import StudentCourses  # Import the StudentCourses model
from src.models.student import Student  # Import the Student model for validation
from src.models.course import Course  # Import the Course model for validation
from src import db  # Assuming db is your SQLAlchemy instance


def create_app():
    app = Flask(__name__)

    @app.route('/students/<int:student_id>/enroll', methods=['POST'])
    def enroll_student(student_id):
        """Enroll a student into a course"""
        # Parse the JSON request body
        request_data = request.get_json()
        
        if not request_data or 'course_id' not in request_data:
            return jsonify({"error": {"code": "E001", "message": "Course ID is required."}}), 400
        
        course_id = request_data['course_id']
        
        # Validate student existence
        student = db.session.query(Student).filter_by(id=student_id).first()
        if not student:
            return jsonify({"error": {"code": "E002", "message": "Student not found."}}), 404
        
        # Validate course existence
        course = db.session.query(Course).filter_by(id=course_id).first()
        if not course:
            return jsonify({"error": {"code": "E003", "message": "Course not found."}}), 404
        
        # Create the enrollment
        enrollment = StudentCourses(student_id=student_id, course_id=course_id)
        
        try:
            db.session.add(enrollment)
            db.session.commit()
            return jsonify({"message": "Student successfully enrolled in course."}), 200
        except IntegrityError:
            db.session.rollback()
            return jsonify({"error": {"code": "E004", "message": "Enrollment already exists."}}), 409
            
    @app.route('/students/<int:student_id>/courses', methods=['GET'])
    def get_student_courses(student_id):
        """Retrieve the list of courses a student is enrolled in"""
        student = db.session.query(Student).filter_by(id=student_id).first()
        if not student:
            return jsonify({"error": {"code": "E002", "message": "Student not found."}}), 404
        
        enrolled_courses = db.session.query(Course).join(StudentCourses).filter(StudentCourses.student_id == student_id).all()
        
        courses_response = [{"course_id": course.id, "course_name": course.name, "course_level": course.level} for course in enrolled_courses]
        
        return jsonify(courses_response), 200

    return app