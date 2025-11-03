```python
from flask import Blueprint, request, jsonify
from marshmallow import Schema, fields, ValidationError
from models import Student  # Assuming the Student model is in your models.py
from extensions import db  # Assuming you use SQLAlchemy for database interaction

# Create a blueprint for the student API
student_bp = Blueprint('student', __name__)

class StudentSchema(Schema):
    """Schema to validate student data."""
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    email = fields.Str(required=False)  # New email field is optional

    @staticmethod
    def validate_email(email):
        """Validate the email format."""
        if not email:
            return
        if "@" not in email or " " in email:
            raise ValidationError("Invalid email format. Please provide a valid email.")

    @pre_load
    def process_input(self, data, **kwargs):
        """Process input data before loading it into the schema."""
        email = data.get('email')
        self.validate_email(email)
        return data

@student_bp.route('/students', methods=['POST'])
def create_student():
    """
    Create a new student record.

    Request example:
    {
      "name": "John Doe",
      "email": "john.doe@example.com"
    }
    
    Returns:
    - 201 Created with student details on success
    - 400 Bad Request if 'name' or 'email' is missing or invalid
    """
    schema = StudentSchema()
    try:
        # Validate and deserialize the input
        student_data = schema.load(request.json)
        
        # Create a new student instance
        student = Student(name=student_data['name'], email=student_data.get('email'))
        
        # Add the new student to the database
        db.session.add(student)
        db.session.commit()
        
        # Return the created student with status 201
        return jsonify(schema.dump(student)), 201

    except ValidationError as err:
        return jsonify(err.messages), 400
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Database integrity error occurred."}), 400
    except Exception as ex:
        db.session.rollback()
        return jsonify({"error": str(ex)}), 500

@student_bp.route('/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    """
    Retrieve a student by ID.

    Returns:
    - 200 OK with student details if found
    - 404 Not Found if student does not exist
    """
    student = Student.query.get(student_id)
    if not student:
        return jsonify({"error": "Student not found."}), 404

    schema = StudentSchema()
    return jsonify(schema.dump(student)), 200
```