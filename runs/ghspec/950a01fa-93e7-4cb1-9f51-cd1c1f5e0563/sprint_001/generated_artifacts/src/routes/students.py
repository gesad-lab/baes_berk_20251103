from flask import Blueprint, request, jsonify
from werkzeug.exceptions import BadRequest
from .models import db, Student

students_blueprint = Blueprint('students', __name__)

@students_blueprint.route('/students', methods=['POST'])
def create_student():
    """
    Create a new Student entry.
    Expects a JSON body with a required 'name' field.
    
    Returns:
        JSON response with the created Student object or an error message.
    """
    data = request.get_json()
    
    # Validate input data
    if not data or 'name' not in data:
        raise BadRequest('E001: Name is required to create a Student.')

    # Create a new Student instance
    new_student = Student(name=data['name'])
    
    # Save to the database
    db.session.add(new_student)
    db.session.commit()

    return jsonify({
        'id': new_student.id,
        'name': new_student.name
    }), 201


@students_blueprint.route('/students', methods=['GET'])
def get_students():
    """
    Retrieve a list of all Student entries.
    
    Returns:
        JSON response containing an array of Student objects.
    """
    students = Student.query.all()
    students_list = [{'id': student.id, 'name': student.name} for student in students]
    
    return jsonify(students_list), 200


# Error handling for BadRequest and other exceptions
@students_blueprint.errorhandler(BadRequest)
def handle_bad_request(error):
    """Handle 400 Bad Request errors."""
    response = jsonify({
        'error': {
            'code': error.description.split(':')[0],
            'message': error.description
        }
    })
    response.status_code = 400
    return response

@students_blueprint.errorhandler(Exception)
def handle_exception(error):
    """Handle unexpected exceptions."""
    response = jsonify({
        'error': {
            'code': 'E500',
            'message': 'An unexpected error occurred. Please try again later.'
        }
    })
    response.status_code = 500
    return response