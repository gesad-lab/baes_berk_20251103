```python
# src/api/teacher_api.py

from flask import Blueprint, request, jsonify
from services.teacher_service import create_teacher
from db import get_db_session
from validation.teacher_validation import validate_teacher
from sqlalchemy.exc import IntegrityError

teacher_bp = Blueprint('teacher', __name__)

@teacher_bp.route('/teachers', methods=['POST'])
def add_teacher():
    data = request.get_json()
    errors = validate_teacher(data)
    if errors:
        return jsonify({"error": errors}), 400

    try:
        teacher = create_teacher(get_db_session(), data['name'], data['email'])
        return jsonify({"message": "Teacher successfully created."}), 201
    except IntegrityError as e:
        # Handle integrity error related to duplicate email addresses
        return jsonify({"error": {"code": "E001", "message": "Email address already exists."}}), 400
```