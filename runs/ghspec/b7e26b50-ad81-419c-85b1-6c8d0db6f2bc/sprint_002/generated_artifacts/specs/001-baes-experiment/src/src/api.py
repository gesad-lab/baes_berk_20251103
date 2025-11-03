from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from marshmallow import Schema, fields, ValidationError

# Initialize Flask and SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
db = SQLAlchemy(app)


# Define the Student model
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)


# Schema for validating student input
class StudentSchema(Schema):
    name = fields.Str(required=True)
    email = fields.Email(required=True)


# Create a new student with email
@app.route('/students', methods=['POST'])
def create_student():
    """Create a new student with name and email."""
    try:
        # Validate input data
        data = StudentSchema().load(request.json)
        student = Student(name=data['name'], email=data['email'])
        db.session.add(student)
        db.session.commit()
        return jsonify({"message": "Student created", "id": student.id, "email": student.email}), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": {"code": "E001", "message": "Email already exists."}}), 400
    except Exception as e:
        return jsonify({"error": {"code": "E002", "message": str(e)}}), 500


# Update existing student's email
@app.route('/students/<int:id>', methods=['PUT'])
def update_student(id):
    """Update an existing student's email."""
    try:
        # Validate input data
        data = request.json
        if 'email' not in data:
            return jsonify({"error": {"code": "E003", "message": "Email is required."}}), 400

        student = Student.query.get_or_404(id)
        student.email = data['email']
        db.session.commit()
        return jsonify({"message": "Student email updated successfully."}), 200
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": {"code": "E001", "message": "Email already exists."}}), 400
    except Exception as e:
        return jsonify({"error": {"code": "E002", "message": str(e)}}), 500


# Run the application
if __name__ == '__main__':
    db.create_all()  # Create the database tables
    app.run(debug=True)