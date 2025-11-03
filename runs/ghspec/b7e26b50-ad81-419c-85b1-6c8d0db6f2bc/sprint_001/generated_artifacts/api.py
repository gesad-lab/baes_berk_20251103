```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for Student
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

# Schema for student validation and serialization
class StudentSchema(Schema):
    id = fields.Int()
    name = fields.Str(required=True)

# Initialize the database schema
with app.app_context():
    db.create_all()

@app.route('/students', methods=['POST'])
def create_student():
    """ Create a new student entry. 
    Expects a JSON body with a 'name' key. 
    Returns a JSON confirmation message.
    """
    data = request.get_json()
    
    if not data or 'name' not in data:
        return jsonify({"error": {"code": "E001", "message": "Name is required."}}), 400
    
    # Create a new Student instance
    new_student = Student(name=data['name'])
    db.session.add(new_student)
    db.session.commit()

    return jsonify({"message": "Student created successfully."}), 201

@app.route('/students', methods=['GET'])
def retrieve_students():
    """ Retrieve a list of all students. 
    Returns a JSON array of students.
    """
    students = Student.query.all()
    student_schema = StudentSchema(many=True)
    return jsonify(student_schema.dump(students)), 200

if __name__ == '__main__':
    app.run(debug=True)
```