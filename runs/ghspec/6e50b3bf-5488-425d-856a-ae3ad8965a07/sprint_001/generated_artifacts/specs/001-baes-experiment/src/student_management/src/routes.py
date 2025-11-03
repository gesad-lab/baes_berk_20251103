from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Student(db.Model):
    __tablename__ = 'students'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)

db.create_all()  # Automatically create the database schema at startup

@app.route('/students', methods=['POST'])
def create_student():
    """
    Create a new student record.

    Request body should contain the student's name.
    Returns a 201 status with the created student's details on success.
    Returns 400 status if the name is empty.
    """
    data = request.get_json()

    if not data or 'name' not in data or not data['name']:
        # Bad Request: name field is required and cannot be empty
        return jsonify({"error": {"code": "E001", "message": "Name is required."}}), 400

    new_student = Student(name=data['name'])
    db.session.add(new_student)
    db.session.commit()

    return jsonify({"id": new_student.id, "name": new_student.name}), 201

@app.route('/students/<int:id>', methods=['GET'])
def retrieve_student(id):
    """
    Retrieve a student record by ID.

    Returns a 200 status with the student's details if found.
    Returns 404 status if no student is found with the given ID.
    """
    student = Student.query.get(id)
    
    if not student:
        # Not Found: student does not exist
        return jsonify({"error": {"code": "E002", "message": "Student not found."}}), 404

    return jsonify({"id": student.id, "name": student.name}), 200

if __name__ == '__main__':
    app.run(debug=True)