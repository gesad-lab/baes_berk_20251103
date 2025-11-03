```python
# src/healthchecks/checks.py

from flask import jsonify
from app import db
from src.models.course import Course  # Assuming Course model exists
from src.models.student import Student  # Assuming Student model exists

def health_check_courses():
    """
    Health check for the Courses table to verify its presence and functionality.

    Returns:
        dict: Health check status and details regarding the Courses table.
    """
    try:
        # Check if the Courses table exists and can be queried
        courses_count = db.session.query(Course).count()
        return jsonify({
            "status": "healthy",
            "courses_table_exists": True,
            "courses_count": courses_count
        }), 200
    except Exception as e:
        # Log the error for debugging purposes
        db.session.rollback()
        return jsonify({
            "status": "unhealthy",
            "message": "Courses table is not accessible.",
            "error": str(e)
        }), 500

def health_check_students():
    """
    Health check for the Students table to verify its presence and functionality.

    Returns:
        dict: Health check status and details regarding the Students table.
    """
    try:
        # Check if the Students table exists and can be queried
        students_count = db.session.query(Student).count()
        return jsonify({
            "status": "healthy",
            "students_table_exists": True,
            "students_count": students_count
        }), 200
    except Exception as e:
        # Log the error for debugging purposes
        db.session.rollback()
        return jsonify({
            "status": "unhealthy",
            "message": "Students table is not accessible.",
            "error": str(e)
        }), 500

def run_health_checks():
    """
    Execute all health checks.

    Returns:
        dict: Combined health check results from all relevant tables.
    """
    results = {
        "courses_check": health_check_courses(),
        "students_check": health_check_students()
    }
    return jsonify(results), 200
```