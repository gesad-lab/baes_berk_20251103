```python
from flask import Blueprint, request, jsonify
from marshmallow import Schema, fields, validate, ValidationError
from src.models import Course
from src.database import db

api = Blueprint('api', __name__)

class CourseSchema(Schema):
    name = fields.String(required=True, validate=validate.Length(min=1))
    level = fields.String(required=True, validate=validate.Length(min=1))

course_schema = CourseSchema()

@api.route('/courses', methods=['POST'])
def create_course():
    """
    Create a new Course.

    Request Body:
    - name: str, required, non-empty
    - level: str, required, non-empty

    Returns:
    JSON representation of the created Course with HTTP 201 status.
    """
    try:
        # Validate input data against the Course schema
        data = request.get_json()
        course_data = course_schema.load(data)

        # Create and save the new Course instance
        new_course = Course(**course_data)
        db.session.add(new_course)
        db.session.commit()

        return jsonify(course_schema.dump(new_course)), 201
    except ValidationError as err:
        return jsonify({"error": {"code": "E001", "message": "Invalid input", "details": err.messages}}), 400
    except Exception as e:
        # Handle any unexpected exceptions
        return jsonify({"error": {"code": "E002", "message": "Internal server error", "details": str(e)}}), 500

@api.route('/courses/<int:id>', methods=['GET'])
def get_course(id):
    """
    Retrieve details of a specific Course by ID.

    Returns:
    JSON representation of the specified Course with HTTP 200 status.
    """
    course = Course.query.get_or_404(id)
    return jsonify(course_schema.dump(course))
```