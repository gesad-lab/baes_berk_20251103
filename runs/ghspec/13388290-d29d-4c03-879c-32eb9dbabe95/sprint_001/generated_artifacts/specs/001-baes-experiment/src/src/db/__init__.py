```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
db = SQLAlchemy(app)

class Student(db.Model):
    """SQLAlchemy model for the Student entity."""
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)

# Schema for validation and serialization
class StudentSchema(Schema):
    """Schema for validating student input."""
    name = fields.Str(required=True)

# Create the database tables on startup
@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/students', methods=['POST'])
def create_student():
    """Endpoint to create a new student record."""
    json_data = request.get_json()

    # Validate input
    try:
        data = StudentSchema().load(json_data)
    except ValidationError as err:
        return jsonify({"error": {"code": "E001", "message": "Invalid input data", "details": err.messages}}), 400

    # Create a new Student object
    new_student = Student(name=data['name'])

    # Add to the database
    db.session.add(new_student)
    db.session.commit()

    return jsonify({"id": new_student.id, "name": new_student.name}), 201

@app.route('/students/<int:id>', methods=['GET'])
def get_student(id):
    """Endpoint to retrieve a student record by ID."""
    student = Student.query.get(id)
    if student is None:
        return jsonify({"error": {"code": "E002", "message": "Student not found"}}), 404
    
    return jsonify({"id": student.id, "name": student.name})

if __name__ == '__main__':
    app.run(debug=True)
```