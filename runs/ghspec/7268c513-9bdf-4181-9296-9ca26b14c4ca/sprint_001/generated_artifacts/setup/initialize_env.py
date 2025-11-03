import os
import subprocess
import sys

def create_virtual_environment(env_name: str) -> None:
    """Create a Python virtual environment."""
    try:
        # Check if the virtual environment already exists
        if os.path.exists(env_name):
            print(f"Virtual environment '{env_name}' already exists. Skipping creation.")
            return
        
        # Create virtual environment
        subprocess.check_call([sys.executable, '-m', 'venv', env_name])
        print(f"Virtual environment '{env_name}' created successfully.")

    except subprocess.CalledProcessError as error:
        print(f"Error creating virtual environment: {error}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def install_packages(env_name: str) -> None:
    """Install necessary packages in the virtual environment."""
    try:
        # Install packages using pip from the created virtual environment
        subprocess.check_call([os.path.join(env_name, 'bin', 'pip'), 'install', 'Flask', 'SQLAlchemy', 'pytest'])
        print("Required packages installed successfully.")

    except subprocess.CalledProcessError as error:
        print(f"Error installing packages: {error}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    env_name = "venv"  # Name of the virtual environment
    create_virtual_environment(env_name)
    install_packages(env_name)