import os
import sys
import subprocess
import venv

def create_virtual_environment(venv_dir: str) -> None:
    """Create a virtual environment in the specified directory."""
    try:
        # Create the virtual environment
        venv.create(venv_dir, with_pip=True)
        print(f"Virtual environment created at {venv_dir}")

        # Install required dependencies
        install_dependencies(venv_dir)
    except Exception as e:
        print(f"Error creating virtual environment: {e}")
        sys.exit(1)

def install_dependencies(venv_dir: str) -> None:
    """Install FastAPI and SQLAlchemy in the virtual environment."""
    try:
        # Activate the virtual environment and use pip to install dependencies
        pip_executable = os.path.join(venv_dir, 'bin', 'pip')
        subprocess.check_call([pip_executable, 'install', 'fastapi[all]', 'sqlalchemy'])
        print("Dependencies installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to install dependencies: {e}")
        sys.exit(1)

if __name__ == "__main__":
    venv_directory = './venv'  # Default virtual environment directory
    create_virtual_environment(venv_directory)