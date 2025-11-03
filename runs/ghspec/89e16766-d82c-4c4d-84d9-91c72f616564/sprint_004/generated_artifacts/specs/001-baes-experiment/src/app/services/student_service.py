```python
from flask import jsonify, request
from app import db
from app.models import Student, Course, StudentCourse

class StudentService:
    
    @staticmethod
    def associate_courses(student_id: int, course_ids: list):
        """
        Associate a list of courses with a student.
        
        :param student_id: The ID of the student to associate courses with
        :param course_ids: A list of course IDs to associate with the student
        :return: A JSON response with success message and updated student record
        """
        # Validate student
        student = Student.query.get(student_id)
        if not student:
            return {"error": {"code": "E001", "message": "Invalid student ID provided."}}, 400
        
        # Validate courses
        valid_courses = Course.query.filter(Course.id.in_(course_ids)).all()
        if len(valid_courses) != len(course_ids):
            return {"error": {"code": "E002", "message": "One or more invalid course IDs provided."}}, 400
        
        # Associate courses
        for course in valid_courses:
            if not StudentCourse.query.filter_by(student_id=student.id, course_id=course.id).first():
                student_course_association = StudentCourse(student_id=student.id, course_id=course.id)
                db.session.add(student_course_association)
        
        db.session.commit()
        
        return jsonify({
            "message": "Student associated with courses successfully.",
            "student": {
                "id": student.id,
                "name": student.name,
                "courses": [{"id": course.id, "name": course.name} for course in valid_courses]
            }
        }), 200

    @staticmethod
    def retrieve_student_with_courses(student_id: int):
        """
        Retrieve a student's record along with associated courses.
        
        :param student_id: The ID of the student to retrieve
        :return: A JSON response with student record and associated courses
        """
        # Validate student
        student = Student.query.get(student_id)
        if not student:
            return {"error": {"code": "E001", "message": "Invalid student ID provided."}}, 400
        
        # Get associated courses
        student_courses = StudentCourse.query.filter_by(student_id=student.id).all()
        courses = [{"id": sc.course.id, "name": sc.course.name} for sc in student_courses]

        return jsonify({
            "id": student.id,
            "name": student.name,
            "courses": courses
        }), 200
```