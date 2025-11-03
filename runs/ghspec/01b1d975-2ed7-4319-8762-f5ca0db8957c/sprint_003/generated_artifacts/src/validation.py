# src/validation.py

import re
from flask import jsonify

def validate_student_data(name: str, email: str) -> dict:
    """Validate student name and email.

    Args:
        name (str): The name of the student.
        email (str): The email address of the student.

    Returns:
        dict: Validation results, containing 'is_valid' status and 'errors' list.
    """
    errors = []
    
    # Validate name (assuming name must be non-empty)
    if not name or not isinstance(name, str):
        errors.append("E001: Name is required and must be a string.")

    # Validate email (basic format check)
    if not email or not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        errors.append("E002: A valid email address is required.")
        
    return {
        'is_valid': len(errors) == 0,
        'errors': errors
    }

def validate_course_data(name: str, level: str) -> dict:
    """Validate course name and level.

    Args:
        name (str): The name of the course.
        level (str): The level of the course.

    Returns:
        dict: Validation results, containing 'is_valid' status and 'errors' list.
    """
    errors = []
    
    # Validate course name
    if not name or not isinstance(name, str):
        errors.append("E003: Course name is required and must be a string.")

    # Validate course level
    if not level or not isinstance(level, str):
        errors.append("E004: Course level is required and must be a string.")
    
    return {
        'is_valid': len(errors) == 0,
        'errors': errors
    }