from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flasgger import Swagger
from models import Student  # Assuming the Student model is in a file named models.py

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
swagger = Swagger(app)

@app.route('/students', methods=['POST'])
def create_student():
    """Create a new student
    ---
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
              example: John Doe
    responses:
      201:
        description: Student created
      400:
        description: Invalid input
    """
    data = request.json
    name = data.get('name')

    if not name:
        return jsonify({'error': {'code': 'E001', 'message': 'Name is required'}}), 400

    new_student = Student(name=name)
    db.session.add(new_student)
    db.session.commit()
    
    return jsonify({'id': new_student.id, 'name': new_student.name}), 201

@app.route('/students', methods=['GET'])
def get_students():
    """Get list of all students
    ---
    responses:
      200:
        description: A list of students
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: integer
                example: 1
              name:
                type: string
                example: John Doe
    """
    students = Student.query.all()
    return jsonify([{'id': student.id, 'name': student.name} for student in students]), 200

@app.route('/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    """Get a single student by ID
    ---
    parameters:
      - name: student_id
        in: path
        required: true
        type: integer
    responses:
      200:
        description: Student found
        schema:
          type: object
          properties:
            id:
              type: integer
              example: 1
            name:
              type: string
              example: John Doe
      404:
        description: Student not found
    """
    student = Student.query.get(student_id)
    if not student:
        return jsonify({'error': {'code': 'E002', 'message': 'Student not found'}}), 404

    return jsonify({'id': student.id, 'name': student.name}), 200

if __name__ == '__main__':
    db.create_all()  # Create the database and tables if they don't exist
    app.run(debug=True)  # Run the Flask app in debug mode