import os

def create_directories():
    # Define the directory structure
    project_structure = [
        "src/api",
        "src/models",
        "src/database",
        "tests",
    ]
    
    # Create the directories
    for directory in project_structure:
        try:
            os.makedirs(directory, exist_ok=True)  # Create directory if it does not exist
            print(f"Directory '{directory}' created successfully.")
        except Exception as e:
            print(f"Error creating directory '{directory}': {e}")

if __name__ == "__main__":
    create_directories()