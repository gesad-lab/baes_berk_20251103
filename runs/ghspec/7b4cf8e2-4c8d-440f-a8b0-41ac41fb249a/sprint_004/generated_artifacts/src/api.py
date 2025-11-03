from flask import Flask, jsonify, request
from flasgger import Swagger, swag_from
from models import db, Student, Course, StudentCourse  # Assuming models are defined in models.py

app = Flask(__name__)
swagger = Swagger(app)

@app.route('/students/<int:student_id>/courses', methods=['POST'])
@swag_from({
    'responses': {
        201: {
            'description': 'Successfully enrolled student in the course',
            'examples': {
                'application/json': {
                    'message': 'Student successfully enrolled in course',
                    'student_id': student_id,
                    'course_id': 'course_id'
                }
            }
        },
        400: {
            'description': 'Invalid course ID'
        },
        404: {
            'description': 'Student or course not found'
        }
    }
})
def enroll_student_in_course(student_id):
    """Enroll a student in a course

    ---
    parameters:
      - name: student_id
        in: path
        type: integer
        required: true
        description: The ID of the student to enroll
      - name: course_id
        in: body
        required: true
        schema:
          type: object
          properties:
            course_id:
              type: integer
              description: The ID of the course to enroll in
    """
    course_data = request.json
    course_id = course_data.get('course_id')

    student = Student.query.get(student_id)
    course = Course.query.get(course_id)

    if not student or not course:
        return jsonify({'message': 'Invalid student or course ID'}), 404

    enrollment = StudentCourse(student_id=student_id, course_id=course_id)
    db.session.add(enrollment)
    db.session.commit()
    
    return jsonify({'message': 'Student successfully enrolled in course', 'student_id': student_id, 'course_id': course_id}), 201


@app.route('/students/<int:student_id>/courses', methods=['GET'])
@swag_from({
    'responses': {
        200: {
            'description': 'List of courses the student is enrolled in',
            'schema': {
                'type': 'array',
                'items': {
                    'type': 'object',
                    'properties': {
                        'course_id': {
                            'type': 'integer',
                            'description': 'ID of the course'
                        },
                        'course_name': {
                            'type': 'string',
                            'description': 'Name of the course'
                        }
                    }
                }
            }
        },
        404: {
            'description': 'Student not found'
        }
    }
})
def get_student_courses(student_id):
    """Retrieve a list of courses a student is enrolled in

    ---
    parameters:
      - name: student_id
        in: path
        type: integer
        required: true
        description: The ID of the student to retrieve courses for
    """
    student = Student.query.get(student_id)

    if not student:
        return jsonify({'message': 'Student not found'}), 404

    courses = (db.session.query(Course)
               .join(StudentCourse)
               .filter(StudentCourse.student_id == student_id)
               .all())

    return jsonify([{'course_id': course.id, 'course_name': course.name} for course in courses])


@app.route('/students/<int:student_id>/courses/<int:course_id>', methods=['DELETE'])
@swag_from({
    'responses': {
        204: {
            'description': 'Successfully removed the course from the student',
        },
        404: {
            'description': 'Student or course not found'
        }
    }
})
def remove_course_from_student(student_id, course_id):
    """Remove a course from the student's enrollment

    ---
    parameters:
      - name: student_id
        in: path
        type: integer
        required: true
        description: The ID of the student
      - name: course_id
        in: path
        type: integer
        required: true
        description: The ID of the course to remove
    """
    enrollment = StudentCourse.query.filter_by(student_id=student_id, course_id=course_id).first()

    if not enrollment:
        return jsonify({'message': 'Student or course not found'}), 404

    db.session.delete(enrollment)
    db.session.commit()

    return '', 204

if __name__ == '__main__':
    app.run(debug=True)