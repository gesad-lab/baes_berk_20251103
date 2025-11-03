```python
from marshmallow import Schema, fields, validate
from api.models import Student, Course  # Ensure these models exist in your models.py

class CourseSchema(Schema):
    """Schema to serialize course information."""
    id = fields.Int(required=True)
    name = fields.Str(required=True)

class StudentSchema(Schema):
    """Schema to serialize student information including enrolled courses."""
    id = fields.Int(required=True)
    name = fields.Str(required=True)
    enrolled_courses = fields.List(fields.Nested(CourseSchema), required=False)

def get_student_with_courses(student_id):
    """Retrieve student info along with their enrolled courses.

    Args:
        student_id (int): The ID of the student to retrieve.
    
    Returns:
        dict: A dictionary containing student info and their enrolled courses.
    
    Raises:
        ValueError: If the student does not exist.
    """
    student = Student.query.get(student_id)
    if not student:
        raise ValueError(f"Student with ID {student_id} does not exist.")

    # Load the courses associated with the student
    courses = student.courses  # Assuming 'courses' is the relationship defined in the Student model
    return {
        "id": student.id,
        "name": student.name,
        "enrolled_courses": [{"id": course.id, "name": course.name} for course in courses]
    }

# Add this snippet to the existing routes where you define API behaviors
@app.route('/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    """Get student information with enrolled courses.

    Args:
        student_id (int): The ID of the student to retrieve.
    
    Returns:
        Response: JSON response containing student info and their courses.
    """
    try:
        student_data = get_student_with_courses(student_id)
        return jsonify(student_data), 200
    except ValueError as e:
        return jsonify({"error": {"code": "E404", "message": str(e)}}), 404
```
