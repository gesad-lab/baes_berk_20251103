import os
import subprocess
import sys

def install_python_and_setup_virtualenv():
    """
    Install Python 3.11+ and set up a virtual environment. 
    Then install the required dependencies for the application.
    """
    # Check if Python 3.11 or higher is installed
    try:
        python_version = subprocess.check_output(["python3", "--version"]).decode().strip()
        print(f"Detected Python version: {python_version}")
    except subprocess.CalledProcessError:
        print("Python is not installed or not found in the system PATH.")
        sys.exit(1)

    major_version = int(python_version.split()[1].split('.')[0])
    minor_version = int(python_version.split()[1].split('.')[1])

    if major_version < 3 or (major_version == 3 and minor_version < 11):
        print("Python 3.11+ is required. Please install the correct version.")
        sys.exit(1)

    # Create a virtual environment
    try:
        subprocess.check_call(["python3", "-m", "venv", "venv"])
        print("Virtual environment created: venv")
    except subprocess.CalledProcessError:
        print("Failed to create a virtual environment.")
        sys.exit(1)

    # Activate the virtual environment and install dependencies
    try:
        if os.name == "nt":
            activate_script = ".\\venv\\Scripts\\activate"
        else:
            activate_script = "./venv/bin/activate"

        # Install required packages
        install_command = "pip install fastapi sqlalchemy uvicorn[standard] pytest"
        subprocess.check_call(f"{activate_script} && {install_command}", shell=True)
        print("Required packages installed.")
    except subprocess.CalledProcessError:
        print("Failed to install required packages.")
        sys.exit(1)

if __name__ == "__main__":
    install_python_and_setup_virtualenv()