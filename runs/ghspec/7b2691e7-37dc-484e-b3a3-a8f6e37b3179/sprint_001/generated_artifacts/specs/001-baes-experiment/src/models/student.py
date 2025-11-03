```python
import os
import subprocess
import sys

def setup_environment():
    """Sets up the development environment by creating a virtual environment 
    and installing necessary packages.
    
    Raises:
        RuntimeError: If the virtual environment creation or package installation fails.
    """
    # Define the project directory and virtual environment name
    project_dir = os.path.dirname(os.path.abspath(__file__))
    venv_dir = os.path.join(project_dir, 'venv')

    # Create a virtual environment
    try:
        subprocess.check_call([sys.executable, '-m', 'venv', venv_dir])
        print(f'Virtual environment created at {venv_dir}')
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f'Failed to create virtual environment: {str(e)}')

    # Activate the virtual environment and install packages
    try:
        # Path to pip within the virtual environment
        pip_path = os.path.join(venv_dir, 'bin', 'pip') if os.name != 'nt' else os.path.join(venv_dir, 'Scripts', 'pip')
        
        # Install required packages
        subprocess.check_call([pip_path, 'install', 'Flask', 'Flask-SQLAlchemy', 'Marshmallow', 'pytest'])
        print('Required packages installed successfully.')
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f'Failed to install packages: {str(e)}')

if __name__ == "__main__":
    setup_environment()
```