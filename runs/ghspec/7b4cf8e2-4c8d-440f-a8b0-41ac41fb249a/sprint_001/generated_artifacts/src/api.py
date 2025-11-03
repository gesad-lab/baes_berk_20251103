from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flasgger import Swagger
from marshmallow import Schema, fields, ValidationError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
swagger = Swagger(app)

class Student(db.Model):
    """Model representing a student."""

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

class StudentSchema(Schema):
    """Schema for validating student input data."""
    
    name = fields.Str(required=True)

student_schema = StudentSchema()
students_schema = StudentSchema(many=True)

@app.before_first_request
def create_tables():
    """Create database tables before the first request."""
    db.create_all()

@app.route('/students', methods=['POST'])
def create_student():
    """Create a new student record.

    ---
    parameters:
      - name: student
        in: body
        required: true
        schema:
          id: Student
          properties:
            name:
              type: string
              required: true
              example: 'John Doe'
    responses:
      201:
        description: Student created successfully
        schema:
          id: Student
          properties:
            id:
              type: integer
              example: 1
            name:
              type: string
              example: 'John Doe'
      400:
        description: Bad Request
        schema:
          properties:
            error:
              type: string
              example: 'Name is required'
    """
    json_data = request.get_json()
    
    try:
        data = student_schema.load(json_data)
    except ValidationError as err:
        return jsonify({'error': str(err)}), 400

    new_student = Student(name=data['name'])
    db.session.add(new_student)
    db.session.commit()

    return student_schema.jsonify(new_student), 201

@app.route('/students/<int:id>', methods=['GET'])
def get_student(id):
    """Retrieve details of a specific student by ID.

    ---
    responses:
      200:
        description: Student retrieved successfully
        schema:
          id: Student
          properties:
            id:
              type: integer
              example: 1
            name:
              type: string
              example: 'John Doe'
      404:
        description: Student not found
        schema:
          properties:
            error:
              type: string
              example: 'Student not found'
    """
    student = Student.query.get(id)
    if not student:
        return jsonify({'error': 'Student not found'}), 404

    return student_schema.jsonify(student)

@app.route('/students/<int:id>', methods=['PUT'])
def update_student(id):
    """Update a student's name by ID.

    ---
    parameters:
      - name: student
        in: body
        required: true
        schema:
          id: Student
          properties:
            name:
              type: string
              required: true
              example: 'Jane Doe'
    responses:
      200:
        description: Student updated successfully
        schema:
          id: Student
          properties:
            id:
              type: integer
              example: 1
            name:
              type: string
              example: 'Jane Doe'
      404:
        description: Student not found
        schema:
          properties:
            error:
              type: string
              example: 'Student not found'
      400:
        description: Bad Request
        schema:
          properties:
            error:
              type: string
              example: 'Name is required'
    """
    json_data = request.get_json()
    
    try:
        data = student_schema.load(json_data)
    except ValidationError as err:
        return jsonify({'error': str(err)}), 400

    student = Student.query.get(id)
    if not student:
        return jsonify({'error': 'Student not found'}), 404

    student.name = data['name']
    db.session.commit()

    return student_schema.jsonify(student)

@app.route('/students/<int:id>', methods=['DELETE'])
def delete_student(id):
    """Delete a student record by ID.

    ---
    responses:
      204:
        description: Student deleted successfully
      404:
        description: Student not found
        schema:
          properties:
            error:
              type: string
              example: 'Student not found'
    """
    student = Student.query.get(id)
    if not student:
        return jsonify({'error': 'Student not found'}), 404

    db.session.delete(student)
    db.session.commit()

    return '', 204

if __name__ == '__main__':
    app.run(debug=True)