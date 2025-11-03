from flask import Blueprint, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# Initialize the API blueprint
api = Blueprint('api', __name__)
# Initialize database
db = SQLAlchemy()
# Initialize marshmallow
ma = Marshmallow()

# Student model
class Student(db.Model):
    __tablename__ = 'students'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)

# Student schema for serialization
class StudentSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Student

# Create a new student
@api.route('/students', methods=['POST'])
def create_student():
    """Create a new student with a JSON body containing the name."""
    data = request.get_json()
    
    # Validate input
    if not data or 'name' not in data:
        return jsonify({"error": {"code": "E001", "message": "Name is required."}}), 400
    
    new_student = Student(name=data['name'])
    
    try:
        db.session.add(new_student)
        db.session.commit()
        
        # Return a success response
        student_schema = StudentSchema()
        return student_schema.jsonify(new_student), 201
    except Exception as e:
        # Log exception details for debugging
        db.session.rollback()
        return jsonify({"error": {"code": "E002", "message": "Could not create student.", "details": str(e)}}), 500

@api.route('/students', methods=['GET'])
def get_students():
    """Retrieve a list of all students."""
    students = Student.query.all()
    student_schema = StudentSchema(many=True)
    return student_schema.jsonify(students), 200