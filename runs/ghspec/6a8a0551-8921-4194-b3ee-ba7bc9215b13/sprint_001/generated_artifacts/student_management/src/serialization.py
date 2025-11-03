def validate_student_input(data):
    """
    Validate student input data to ensure required fields are present.

    Args:
        data (dict): The input data to validate.

    Raises:
        ValueError: If the 'name' field is missing or empty.

    Returns:
        None: If validation is successful.
    """
    # Check if 'name' is present in the input data
    if 'name' not in data or not data['name']:
        # Raise an error if 'name' is missing or empty
        raise ValueError("E001: The 'name' field is required and cannot be empty.")