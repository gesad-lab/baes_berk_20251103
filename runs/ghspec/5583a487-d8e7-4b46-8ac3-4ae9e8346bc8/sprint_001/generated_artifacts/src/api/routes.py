```python
from flask import Blueprint, jsonify, request
from models import db, Student  # Assuming models.py exists with a Student model defined
from sqlalchemy.exc import IntegrityError

# Create a blueprint for API routes
api_bp = Blueprint('api', __name__)

@api_bp.route('/students', methods=['GET'])
def get_students():
    """
    Retrieve all student records from the database.
    
    Returns a JSON response containing a list of student records.
    Each record includes the student's ID and name.
    """
    try:
        students = Student.query.all()  # Retrieve all student records
        # Convert student records to a list of dictionaries
        students_list = [{"id": student.id, "name": student.name} for student in students]
        
        return jsonify(students_list), 200  # Return list of students with HTTP 200 status
    except Exception as e:
        # Log the error (logging assumed to be set up)
        print(f"Error retrieving students: {str(e)}")  # Replace with actual logging
        return jsonify({"error": {"code": "E002", "message": "Unable to retrieve student records."}}), 500
```