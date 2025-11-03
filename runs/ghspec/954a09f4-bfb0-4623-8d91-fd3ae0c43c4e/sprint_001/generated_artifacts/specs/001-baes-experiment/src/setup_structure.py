import os

def create_directory_structure(base_path: str):
    """
    Create the application directory structure for the Student Management application.
    
    :param base_path: The base path where the application structure will be created.
    """
    # Define the structure as a nested list
    structure = [
        "src",
        "tests",
        "requirements.txt",
        ".env.example",
        "README.md"
    ]
    
    src_files = [
        "app.py",
        "models.py",
        "services.py",
        "repositories.py",
        "database.py"
    ]
    
    # Create base directories and files
    for item in structure:
        item_path = os.path.join(base_path, item)
        if item == "src":
            # Create the 'src' directory
            os.makedirs(item_path, exist_ok=True)
            # Create the files inside 'src'
            for file in src_files:
                open(os.path.join(item_path, file), 'a').close()  # Create empty files
        else:
            # Create other files
            open(item_path, 'a').close()  # Create empty file

if __name__ == "__main__":
    # Set the base path for the application structure
    BASE_PATH = os.getcwd()  # Use current working directory
    create_directory_structure(BASE_PATH)  # Call the function to create directories
    print("Application directory structure created successfully.")