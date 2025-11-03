import os

def create_project_structure():
    # Define the desired directory structure
    directory_structure = {
        "student_api": {
            "src": ["main.py", "models.py", "crud.py", "schemas.py", "database.py"],
            "tests": ["test_main.py"],
            ".env.example": "",
            "requirements.txt": "",
            "README.md": ""
        }
    }
    
    # Create the directory structure
    for main_dir, sub_dirs in directory_structure.items():
        # Create main directory
        os.makedirs(main_dir, exist_ok=True)
        for sub_dir, files in sub_dirs.items():
            # Create subdirectories
            os.makedirs(os.path.join(main_dir, sub_dir), exist_ok=True)
            for file in files:
                # Create empty files
                open(os.path.join(main_dir, sub_dir, file), 'a').close()
    
    print("Project directory structure created successfully.")

if __name__ == "__main__":
    create_project_structure()