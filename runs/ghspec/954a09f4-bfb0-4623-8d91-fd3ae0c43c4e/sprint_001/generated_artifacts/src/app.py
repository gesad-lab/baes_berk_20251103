from flask import Flask, jsonify, request
from models import db, Student

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db.init_app(app)

@app.before_first_request
def create_tables():
    """Create database tables on the first request."""
    db.create_all()

@app.route('/students/<int:id>', methods=['GET'])
def get_student(id):
    """
    Retrieve a student by their ID.
    
    :param id: The ID of the student to retrieve.
    :return: JSON representation of the student or an error response if not found.
    """
    # Find the student in the database by ID
    student = Student.query.get(id)
    
    if student is None:
        # If student not found, return a 404 error response
        return jsonify({
            "error": {
                "code": "E002",
                "message": "Student not found."
            }
        }), 404
    
    # Return the student's details in JSON format
    return jsonify({
        "id": student.id,
        "name": student.name
    }), 200

if __name__ == '__main__':
    app.run(debug=True)