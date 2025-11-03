from flask import Flask, request, jsonify
from marshmallow import Schema, fields, ValidationError
from models import db, Student

app = Flask(__name__)

# Schema for validating incoming student data
class StudentSchema(Schema):
    name = fields.String(required=True)
    email = fields.Email(required=True)  # Validate that email is in the correct format

student_schema = StudentSchema()

@app.route('/students', methods=['POST'])
def create_student():
    """
    Create a new Student record with name and email.
    Returns the created Student's ID, name, and email.
    """
    try:
        # Validate input data using Marshmallow schema
        student_data = student_schema.load(request.json)

        # Create a new Student instance
        new_student = Student(name=student_data['name'], email=student_data['email'])

        # Add the new student to the session and commit
        db.session.add(new_student)
        db.session.commit()

        # Prepare response
        response = {
            'id': new_student.id,
            'name': new_student.name,
            'email': new_student.email
        }
        return jsonify(response), 201  # Return 201 Created status
    
    except ValidationError as err:
        # Return validation errors
        return jsonify({"error": {"code": "E001", "message": "Invalid input", "details": err.messages}}), 400
    except Exception as e:
        # Log the exception for debugging purposes (excludes sensitive information)
        app.logger.error(f"Error creating student: {str(e)}")
        return jsonify({"error": {"code": "E002", "message": "Could not create student"}}), 500

@app.route('/students/<int:id>', methods=['GET'])
def get_student(id):
    """
    Retrieve a Student record by ID.
    Returns the Student's details including id, name, and email.
    """
    student = Student.query.get(id)
    if not student:
        return jsonify({"error": {"code": "E003", "message": "Student not found"}}), 404

    response = {
        'id': student.id,
        'name': student.name,
        'email': student.email
    }
    return jsonify(response), 200  # Return 200 OK status

# Other existing routes...

if __name__ == '__main__':
    app.run(debug=True)  # Only for development, remove in production