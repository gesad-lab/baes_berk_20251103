import os
import sys
import subprocess
import platform

def create_virtual_environment():
    """Create and activate a Python virtual environment."""
    
    # Determine the current working directory
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Define the virtual environment directory
    venv_dir = os.path.join(base_dir, "venv")
    
    # Command to create a virtual environment
    try:
        print(f"Creating virtual environment in: {venv_dir}")
        subprocess.check_call([sys.executable, "-m", "venv", venv_dir])
    except subprocess.CalledProcessError as e:
        print(f"Failed to create virtual environment: {e}")
        return False

    # Command to determine the activation command based on the OS
    if platform.system() == "Windows":
        activate_command = os.path.join(venv_dir, "Scripts", "activate")
    else:
        activate_command = os.path.join(venv_dir, "bin", "activate")
    
    # Provide the activation command to the user
    print(f"Virtual environment created successfully.")
    print(f"To activate the virtual environment, run the following command:")
    print(f"source {activate_command}" if platform.system() != "Windows" else f"{activate_command}")
    
    return True

if __name__ == "__main__":
    create_virtual_environment()