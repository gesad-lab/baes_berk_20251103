def validate_student_name(name: str) -> None:
    """Validate the student's name for registration.

    Args:
        name (str): The name of the student to validate.

    Raises:
        ValueError: If the name is empty or not a string.
    """
    if not isinstance(name, str):
        raise ValueError("E001: Name must be a string.")
    if not name.strip():
        raise ValueError("E002: Name cannot be empty or whitespace only.")

def validate_student_data(student_data: dict) -> None:
    """Validate the student data for registration.

    Args:
        student_data (dict): A dictionary containing student details.

    Raises:
        ValueError: If the validation checks fail.
    """
    if 'name' not in student_data:
        raise ValueError("E003: Name field is required.")
    
    validate_student_name(student_data['name'])