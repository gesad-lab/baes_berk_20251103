import subprocess
import os

def initialize_poetry_project(project_name: str) -> None:
    """Initializes a new Python project with Poetry.

    Args:
        project_name (str): The name of the project.

    Raises:
        RuntimeError: If the Poetry initialization command fails.
    """
    try:
        # Create a new directory for the project
        os.makedirs(project_name, exist_ok=True)
        os.chdir(project_name)

        # Run the Poetry command to initialize a new project
        subprocess.run(["poetry", "init", "--no-interaction"], check=True)

        # Add required dependencies
        dependencies = ["fastapi", "uvicorn", "sqlalchemy", "pytest"]
        subprocess.run(["poetry", "add"] + dependencies, check=True)

        # Create a .env file for configuration
        with open(".env", "w") as env_file:
            env_file.write("DATABASE_URL=sqlite:///./test.db\n")

        print(f"Successfully initialized the project '{project_name}' with Poetry.")

    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"Failed to initialize the project: {e}") from e
    except Exception as e:
        raise RuntimeError(f"An unexpected error occurred: {e}") from e

if __name__ == "__main__":
    # Initialize the project with a specified name (change 'student_management' as needed)
    initialize_poetry_project("student_management")