from flask import Flask, jsonify, request, abort
from models.student import Student  # Assuming there's a Student model in models/student.py
from db.database import db_session  # Assuming an active database session is being managed
from utils.email_validators import is_valid_email  # Importing email validation function

app = Flask(__name__)

@app.route('/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    """
    Retrieve a student by ID.

    Parameters:
    - student_id (int): The ID of the student to retrieve.

    Returns:
    - JSON response containing the student's name and email if found.
    - 404 Not Found response if the student does not exist.
    """
    # Query the database for the student with the given ID
    student = db_session.query(Student).filter(Student.id == student_id).first()
    
    if student is None:
        # Return 404 if student is not found
        abort(404, description="Student not found")
    
    # Return student details in JSON format
    return jsonify({
        'name': student.name,
        'email': student.email
    }), 200

if __name__ == '__main__':
    app.run(debug=True)  # Run the application in debug mode for development purposes