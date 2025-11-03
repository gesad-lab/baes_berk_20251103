import os
import subprocess
import sys

def create_requirements_file():
    """Creates the requirements.txt file with the necessary dependencies."""
    requirements_content = """fastapi
uvicorn
sqlalchemy
pydantic
"""
    with open('requirements.txt', 'w') as file:
        file.write(requirements_content)
    print("requirements.txt has been created.")

def create_virtual_environment():
    """Creates a virtual environment for the project."""
    if os.name == 'nt':  # For Windows
        subprocess.check_call([sys.executable, '-m', 'venv', 'venv'])
        print("Virtual environment created: venv\\Scripts\\activate")
    else:  # For macOS/Linux
        subprocess.check_call([sys.executable, '-m', 'venv', 'venv'])
        print("Virtual environment created: source venv/bin/activate")

def install_dependencies():
    """Installs the project dependencies from requirements.txt."""
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])
        print("Dependencies have been installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred during the installation of dependencies: {str(e)}", file=sys.stderr)

def main():
    """Main function to set up the environment and install dependencies."""
    create_requirements_file()  # Step to create requirements file
    create_virtual_environment()  # Step to create virtual environment
    install_dependencies()  # Step to install dependencies

if __name__ == "__main__":
    main()