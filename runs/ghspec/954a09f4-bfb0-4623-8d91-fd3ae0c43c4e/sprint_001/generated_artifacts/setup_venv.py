import os
import subprocess
import sys

def create_virtual_environment(venv_dir: str) -> None:
    """Creates a virtual environment in the specified directory."""
    try:
        # Create the virtual environment
        subprocess.check_call([sys.executable, '-m', 'venv', venv_dir])
        print(f"Virtual environment created at {venv_dir}")
    except subprocess.CalledProcessError as e:
        print(f"Error creating virtual environment: {e}")
        sys.exit(1)

def install_dependencies(venv_dir: str) -> None:
    """Installs necessary dependencies in the virtual environment."""
    requirements = ['Flask', 'SQLAlchemy']
    try:
        # Activate the virtual environment and install dependencies
        if os.name == 'nt':  # Windows
            subprocess.check_call([os.path.join(venv_dir, 'Scripts', 'pip'), 'install'] + requirements)
        else:  # Unix-based
            subprocess.check_call([os.path.join(venv_dir, 'bin', 'pip'), 'install'] + requirements)
        print("Dependencies installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error installing dependencies: {e}")
        sys.exit(1)

def main() -> None:
    """Main function to setup the virtual environment and install dependencies."""
    venv_directory = './venv'  # Define the directory for the virtual environment
    create_virtual_environment(venv_directory)  # Create the virtual environment
    install_dependencies(venv_directory)  # Install dependencies

if __name__ == '__main__':
    main()