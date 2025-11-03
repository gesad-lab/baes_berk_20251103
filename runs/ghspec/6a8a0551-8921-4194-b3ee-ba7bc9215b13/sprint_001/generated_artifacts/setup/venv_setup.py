import os
import subprocess
import sys

def create_virtual_environment():
    """Creates a Python virtual environment in the current directory."""
    try:
        # Define the name for the virtual environment directory
        venv_dir = "venv"

        # Check if the virtual environment directory already exists
        if os.path.exists(venv_dir):
            print(f"Virtual environment '{venv_dir}' already exists.")
            return

        # Create the virtual environment
        subprocess.check_call([sys.executable, "-m", "venv", venv_dir])
        print(f"Virtual environment '{venv_dir}' created successfully.")

        # Activate the virtual environment
        activate_script = os.path.join(venv_dir, "Scripts", "activate") if os.name == "nt" else os.path.join(venv_dir, "bin", "activate")
        print(f"To activate the virtual environment, run:\nsource {activate_script}")

        # Install required packages
        install_required_packages(venv_dir)

    except Exception as e:
        print(f"Error while creating virtual environment: {str(e)}")
        
def install_required_packages(venv_dir):
    """Installs required packages in the virtual environment."""
    try:
        # Depending on the platform, adjust the path to the Python executable in the virtual environment
        pip_executable = os.path.join(venv_dir, "Scripts", "pip") if os.name == "nt" else os.path.join(venv_dir, "bin", "pip")
        
        # List of required packages
        required_packages = ["Flask", "marshmallow", "sqlite3"]

        # Install each required package
        for package in required_packages:
            subprocess.check_call([pip_executable, "install", package])
            print(f"Package '{package}' installed successfully.")
            
    except Exception as e:
        print(f"Error while installing packages: {str(e)}")

if __name__ == "__main__":
    create_virtual_environment()