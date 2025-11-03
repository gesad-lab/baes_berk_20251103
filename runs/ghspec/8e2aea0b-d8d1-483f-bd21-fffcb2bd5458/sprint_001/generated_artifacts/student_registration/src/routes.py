```python
from flask import Flask, request, jsonify
from marshmallow import Schema, fields, ValidationError
from models import db, Student

app = Flask(__name__)

# Marshmallow schema for student validation
class StudentSchema(Schema):
    name = fields.String(required=True)

# Initialize schema
student_schema = StudentSchema()
students_schema = StudentSchema(many=True)

@app.route('/students', methods=['POST'])
def register_student():
    """Register a new student."""
    try:
        # Validate and deserialize input
        data = student_schema.load(request.json)

        # Create and save the new student in the database
        student = Student(name=data['name'])
        db.session.add(student)
        db.session.commit()

        # Return the created student as JSON with 201 status
        return student_schema.dump(student), 201

    except ValidationError as err:
        # Handle validation error: return an error response
        return jsonify({
            "error": {
                "code": "E001",
                "message": str(err)
            }
        }), 400
    except Exception as e:
        # Log unexpected errors with detailed context
        # Here it's important to log the error, but for this implementation,
        # we're returning a generic error message.
        app.logger.error(f"Unexpected error: {str(e)}")
        return jsonify({
            "error": {
                "code": "E002",
                "message": "An unexpected error occurred."
            }
        }), 500

@app.route('/students', methods=['GET'])
def get_students():
    """Retrieve the list of all registered students."""
    students = Student.query.all()
    return students_schema.dump(students), 200

# Function to create the database schema
def init_db():
    """Initialize the database and create students table if not exists."""
    db.create_all()

if __name__ == '__main__':
    init_db()  # Call the database initialization
    app.run(debug=True)
```