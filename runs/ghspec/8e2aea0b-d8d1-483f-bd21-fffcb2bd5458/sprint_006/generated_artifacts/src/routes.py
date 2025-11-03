# Content for src/routes.py

```python
"""
API Route Definitions for Course Management

This module defines the API routes related to course management,
specifically for assigning teachers to courses and retrieving course details.

Newly Implemented Functionality:
1. **Assign Teacher to Course**:
   - **Endpoint**: POST /api/v1/courses/<course_id>/assign-teacher
   - **Description**: This endpoint assigns a teacher to a specified course. The `teacher_id` must be provided in the request body.
   - **Request Body**:
     {
       "teacher_id": "<UUID>"
     }
   - **Response**:
     - Success (200 OK): Returns a confirmation message.
     - Error (400 Bad Request): If the course ID does not exist or the teacher ID is invalid.
     - Error (404 Not Found): If the specified course is not found.

2. **Retrieve Course Details**:
   - **Endpoint**: GET /api/v1/courses/<course_id>
   - **Description**: This endpoint retrieves the details of a specified course, including the assigned teacher.
   - **Response**:
     - Success (200 OK): Returns course details including its teacher if assigned.
     - Error (404 Not Found): If the specified course is not found.

Example Usage:
- To assign a teacher, send a POST request to `/api/v1/courses/<course_id>/assign-teacher` with a JSON body containing the teacher ID.
- To get course details, send a GET request to `/api/v1/courses/<course_id>`.

Note: The user interface design related to course-teacher associations, removal or changing of teachers, advanced features such as scheduling or notifications, and performance optimizations are out of scope for this implementation.
"""

from flask import Blueprint, request, jsonify
from src.models import db, Course
from src.schemas import CourseSchema

api_bp = Blueprint('api', __name__)

# Assign a teacher to a course
@api_bp.route('/api/v1/courses/<uuid:course_id>/assign-teacher', methods=['POST'])
def assign_teacher_to_course(course_id):
    # Validate request data
    data = request.get_json()
    teacher_id = data.get("teacher_id")
    
    if not teacher_id:
        return jsonify({"error": {"code": "E001", "message": "Missing teacher_id."}}), 400

    # Find the course
    course = Course.query.get(course_id)
    if not course:
        return jsonify({"error": {"code": "E002", "message": "Course not found."}}), 404

    # Assign teacher to course
    course.teacher_id = teacher_id
    db.session.commit()

    return jsonify({"message": "Teacher assigned successfully."}), 200

# Retrieve course details
@api_bp.route('/api/v1/courses/<uuid:course_id>', methods=['GET'])
def get_course_details(course_id):
    course = Course.query.get(course_id)
    if not course:
        return jsonify({"error": {"code": "E002", "message": "Course not found."}}), 404

    course_schema = CourseSchema()
    return jsonify(course_schema.dump(course)), 200
```