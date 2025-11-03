```python
from flask import jsonify, request
from sqlalchemy.exc import IntegrityError
from models import db, Student, Course, StudentCourse  # Assuming these are defined in models.py

class StudentCourseService:
    @staticmethod
    def add_courses_to_student(student_id: int):
        """Adds a list of courses to a student.

        Args:
            student_id (int): The ID of the student to whom courses will be added.

        Returns:
            A tuple containing the response data and the HTTP status code.
        """

        # Parse and validate request body
        data = request.get_json()
        if not data or 'course_ids' not in data:
            return jsonify({
                "error": {
                    "code": "E001",
                    "message": "Course IDs are required."
                }
            }), 400

        course_ids = data['course_ids']

        if not isinstance(course_ids, list) or any(not isinstance(i, int) for i in course_ids):
            return jsonify({
                "error": {
                    "code": "E002",
                    "message": "Invalid course IDs format."
                }
            }), 400

        try:
            student = Student.query.get(student_id)
            if not student:
                return jsonify({
                    "error": {
                        "code": "E002",
                        "message": "Student not found."
                    }
                }), 404
            
            courses = Course.query.filter(Course.id.in_(course_ids)).all()
            if len(courses) != len(course_ids):
                return jsonify({
                    "error": {
                        "code": "E003",
                        "message": "One or more courses not found."
                    }
                }), 404

            # Establish relationship by adding course to student
            for course in courses:
                student_course = StudentCourse(student_id=student.id, course_id=course.id)
                db.session.add(student_course)

            db.session.commit()
            return jsonify({
                "message": "Courses added successfully.",
                "student_id": student.id,
                "courses": [{"id": course.id, "name": course.name, "level": course.level} for course in courses]
            }), 200
        
        except IntegrityError:
            db.session.rollback()  # Rollback in case of failure
            return jsonify({"error": {"code": "E004", "message": "Database error occurred."}}), 500
        except Exception as e:
            db.session.rollback()  # Rollback on any other error
            return jsonify({"error": {"code": "E500", "message": "An unknown error occurred."}}), 500

    @staticmethod
    def get_courses_for_student(student_id: int):
        """Retrieves a list of courses for a student.

        Args:
            student_id (int): The ID of the student whose courses are to be retrieved.

        Returns:
            A tuple containing the response data and the HTTP status code.
        """

        student = Student.query.get(student_id)
        if not student:
            return jsonify({
                "error": {
                    "code": "E002",
                    "message": "Student not found."
                }
            }), 404

        # Fetch related courses
        courses = db.session.query(Course).join(StudentCourse).filter(StudentCourse.student_id == student.id).all()

        return jsonify({
            "student_id": student.id,
            "courses": [{"id": course.id, "name": course.name, "level": course.level} for course in courses]
        }), 200
```