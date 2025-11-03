import os

# Create directory structure for the student application
directory_structure = {
    "student_app": {
        "src": {
            "controllers": {},
            "models": {},
            "services": {},
            "database": {},
            "main.py": ""
        },
        "tests": {
            "test_student.py": ""
        },
        "requirements.txt": ""
    }
}

def create_directory_structure(base_path, structure):
    """Recursively create directories and files based on the provided structure."""
    for name, content in structure.items():
        current_path = os.path.join(base_path, name)
        if isinstance(content, dict):
            os.makedirs(current_path, exist_ok=True)
            # Recursively create subdirectories
            create_directory_structure(current_path, content)
        else:  # It's a file
            with open(current_path, 'w') as f:
                f.write(content)  # Create an empty file

# Create the directory structure starting from the current path
create_directory_structure(os.getcwd(), directory_structure)