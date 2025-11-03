```python
from flask import Blueprint, request, jsonify
from marshmallow import Schema, fields, ValidationError
from models import Student, Course, db  # Importing Course model
from sqlalchemy.exc import IntegrityError

students_bp = Blueprint('students', __name__)

class StudentSchema(Schema):
    """Schema to validate student data, including a valid email format."""
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    email = fields.Str(required=True)

class CourseSchema(Schema):
    """Schema to validate course data."""
    id = fields.Int(required=True)

# Endpoint to associate a course with a student
@students_bp.route('/students/<int:student_id>/courses', methods=['POST'])
def associate_courses(student_id):
    """Associates specified courses with a student."""
    try:
        data = request.get_json()
        course_ids = data.get('course_ids', [])
        
        # Validate that student exists
        student = Student.query.get_or_404(student_id)

        # Validate that courses exist
        courses = Course.query.filter(Course.id.in_(course_ids)).all()
        if len(courses) != len(course_ids):
            return jsonify({'error': {'code': 'E001', 'message': 'One or more course IDs do not exist.'}}), 400

        # Create associations in the junction table
        for course in courses:
            student.courses.append(course)  # Assuming relationship exists in Student model
            
        db.session.commit()
        
        return jsonify({'message': 'Courses associated successfully.'}), 200

    except IntegrityError:
        return jsonify({'error': {'code': 'E002', 'message': 'Failed to associate courses, please check integrity constraints.'}}), 500
    except ValidationError as ve:
        return jsonify({'error': {'code': 'E003', 'message': str(ve.messages)}}), 400
    except Exception as e:
        return jsonify({'error': {'code': 'E004', 'message': 'An unexpected error occurred.', 'details': str(e)}}), 500

# Endpoint to retrieve courses associated with a student
@students_bp.route('/students/<int:student_id>/courses', methods=['GET'])
def get_student_courses(student_id):
    """Retrieves a list of courses associated with a specified student."""
    student = Student.query.get_or_404(student_id)
    course_list = [{'id': course.id, 'name': course.name} for course in student.courses]
    
    return jsonify(course_list), 200

# Ensure that the Course model relationship is set up correctly in the Student model as well
# For example, add in models/student.py
# courses = db.relationship('Course', secondary='student_courses', backref='students')

```