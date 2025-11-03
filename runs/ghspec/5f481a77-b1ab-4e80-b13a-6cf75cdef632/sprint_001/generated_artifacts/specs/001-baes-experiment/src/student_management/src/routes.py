from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
db = SQLAlchemy(app)

# Database model for Student
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

# Create the database schema on startup
@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/students', methods=['POST'])
def create_student():
    """
    Creates a new Student in the database.
    
    Request body must include:
    - name (string, required): The name of the student.
    
    Returns:
    - JSON response with success message and student details or error message if validation fails.
    """
    data = request.get_json()
    
    # Validate input: Ensure 'name' is provided
    if not data or 'name' not in data or not data['name']:
        return jsonify({
            "error": {
                "code": "E001",
                "message": "Missing required field: 'name'.",
                "details": {}
            }
        }), 400  # 400 Bad Request

    try:
        new_student = Student(name=data['name'])
        db.session.add(new_student)
        db.session.commit()
        
        return jsonify({
            "message": "Student created successfully.",
            "student": {
                "id": new_student.id,
                "name": new_student.name
            }
        }), 201  # 201 Created

    except IntegrityError:
        db.session.rollback()
        return jsonify({
            "error": {
                "code": "E002",
                "message": "Database integrity error occurred.",
                "details": {}
            }
        }), 500  # 500 Internal Server Error

@app.route('/students/<int:id>', methods=['GET'])
def get_student(id):
    """
    Retrieves a Student by ID from the database.
    
    Returns:
    - JSON response with student details or error message if not found.
    """
    student = Student.query.get(id)
    
    if student is None:
        return jsonify({
            "error": {
                "code": "E003",
                "message": "Student not found.",
                "details": {}
            }
        }), 404  # 404 Not Found

    return jsonify({
        "student": {
            "id": student.id,
            "name": student.name
        }
    }), 200  # 200 OK

if __name__ == '__main__':
    app.run(debug=True)