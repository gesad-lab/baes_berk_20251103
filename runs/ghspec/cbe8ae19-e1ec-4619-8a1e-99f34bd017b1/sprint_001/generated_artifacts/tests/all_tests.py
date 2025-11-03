```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
db = SQLAlchemy(app)

# Define the Student model
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

# Define the Student schema for validation
class StudentSchema(Schema):
    name = fields.String(required=True)

student_schema = StudentSchema()
students_schema = StudentSchema(many=True)

@app.route('/students', methods=['POST'])
def add_student():
    """
    Add a new student to the database.
    
    Request Body:
        {
            "name": "string"
        }
    
    Return Value:
        JSON object of the created student or an error message.
    """
    try:
        # Validate input data
        data = request.get_json()
        if not data:
            return jsonify({"error": {"code": "E001", "message": "Missing input data."}}), 400
        
        student_data = student_schema.load(data)

        # Create a new Student instance
        new_student = Student(name=student_data['name'])

        # Add to database
        db.session.add(new_student)
        db.session.commit()

        return student_schema.dump(new_student), 201

    except ValidationError as err:
        # Handle validation errors
        return jsonify({"error": {"code": "E002", "message": "Invalid input.", "details": err.messages}}), 400
    except Exception as e:
        # Log error for debugging without exposing sensitive information
        app.logger.error(f"Error occurred while adding a student: {str(e)}")
        return jsonify({"error": {"code": "E003", "message": "An error occurred while processing the request."}}), 500

@app.route('/students', methods=['GET'])
def get_students():
    """
    Retrieve all students from the database.
    
    Return Value:
        JSON array of students.
    """
    try:
        all_students = Student.query.all()
        return students_schema.dump(all_students), 200
    except Exception as e:
        app.logger.error(f"Error occurred while retrieving students: {str(e)}")
        return jsonify({"error": {"code": "E004", "message": "An error occurred while retrieving students."}}), 500

if __name__ == '__main__':
    # Run the app in debug mode for development
    app.run(debug=True)
```