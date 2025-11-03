```python
from flask import Blueprint, jsonify, request
from src.models import Teacher
from src.database import get_db_session

routes = Blueprint('routes', __name__)

@routes.route('/teachers/<int:teacher_id>', methods=['GET'])
def retrieve_teacher(teacher_id):
    """Retrieve teacher details by teacher_id.
    
    Args:
        teacher_id (int): The ID of the teacher to retrieve.
    
    Returns:
        JSON response with teacher details if found, else returns 404 Not Found.
    """
    db_session = get_db_session()
    
    # Attempt to retrieve the teacher using the provided ID
    teacher = db_session.query(Teacher).filter(Teacher.teacher_id == teacher_id).first()
    
    if teacher is None:
        # Teacher not found, return a 404 error
        return jsonify({"error": {"code": "E404", "message": "Teacher not found"}}, 404
    
    # Teacher found, return the details
    response_data = {
        "teacher_id": teacher.teacher_id,
        "name": teacher.name,
        "email": teacher.email
    }
    return jsonify(response_data), 200
```