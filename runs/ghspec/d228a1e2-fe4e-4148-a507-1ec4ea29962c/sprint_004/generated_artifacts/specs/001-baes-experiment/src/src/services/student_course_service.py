```python
from flask_sqlalchemy import SQLAlchemy
from flask import jsonify, request, abort

# Initialize SQLAlchemy
db = SQLAlchemy()

# Junction table for the many-to-many relationship between Student and Course
class StudentCourse(db.Model):
    __tablename__ = 'student_courses'
    
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), primary_key=True)

# Service for student-course relationships
class StudentCourseService:
    
    @staticmethod
    def enroll_student(student_id: int, course_id: int):
        """Enroll a student in a specific course."""
        # Check if the student and course exist
        from models import Student, Course  # Assuming models exist
        student = Student.query.get(student_id)
        course = Course.query.get(course_id)
        
        if not student:
            abort(404, jsonify({"error": {"code": "E001", "message": "Student not found."}}))
        if not course:
            abort(404, jsonify({"error": {"code": "E002", "message": "Course not found."}}))
        
        enrollment = StudentCourse(student_id=student_id, course_id=course_id)
        db.session.add(enrollment)
        db.session.commit()
        
        return jsonify({"message": "Student enrolled successfully."}), 201

    @staticmethod
    def remove_student_from_course(student_id: int, course_id: int):
        """Remove a student from a specific course."""
        # Check if the relationship exists
        enrollment = StudentCourse.query.filter_by(student_id=student_id, course_id=course_id).first()
        
        if not enrollment:
            abort(404, jsonify({"error": {"code": "E003", "message": "Enrollment not found."}}))
        
        db.session.delete(enrollment)
        db.session.commit()
        
        return jsonify({"message": "Student removed from course successfully."}), 200

    @staticmethod
    def list_student_courses(student_id: int):
        """List all courses for a specific student."""
        # Retrieve all courses for the student
        from models import Course  # Assuming models exist
        courses = db.session.query(Course).join(StudentCourse).filter(StudentCourse.student_id == student_id).all()
        
        if not courses:
            return jsonify([]), 200  # No courses found
        
        return jsonify([{"id": course.id, "name": course.name, "level": course.level} for course in courses]), 200
```