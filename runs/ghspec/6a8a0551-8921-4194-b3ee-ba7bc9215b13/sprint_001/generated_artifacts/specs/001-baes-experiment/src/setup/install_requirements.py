import subprocess
import sys

def install_requirements():
    """Install the required libraries for the project."""
    required_libraries = [
        'Flask',
        'Flask-Marshmallow',
        'sqlite3'
    ]
    try:
        # Use subprocess to run pip install command for required libraries
        subprocess.check_call([sys.executable, '-m', 'pip', 'install'] + required_libraries)
        print("Required libraries installed successfully.")
    except subprocess.CalledProcessError as error:
        # Catch any errors during installation and print an appropriate message
        print(f"Error occurred while installing libraries: {error}")
        sys.exit(1)

if __name__ == '__main__':
    install_requirements()