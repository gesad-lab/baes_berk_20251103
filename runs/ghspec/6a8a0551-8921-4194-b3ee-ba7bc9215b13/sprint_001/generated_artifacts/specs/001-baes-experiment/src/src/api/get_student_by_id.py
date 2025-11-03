from flask import Flask, jsonify, abort
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Student model
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

# Create the database schema
@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/students/<int:id>', methods=['GET'])
def get_student_by_id(id):
    """
    Retrieve a specific student by ID.

    Args:
        id (int): The ID of the student to retrieve.
    
    Returns:
        JSON response containing the student data or a 404 error if not found.
    """
    student = Student.query.get(id)
    if student is None:
        # Return a 404 error if the student is not found
        return jsonify({"error": {"code": "E404", "message": "Student not found"}}), 404
    # Return the student data as a JSON response
    return jsonify({"id": student.id, "name": student.name})

if __name__ == '__main__':
    app.run(debug=True)