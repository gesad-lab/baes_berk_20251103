import os
import subprocess
import sys

def setup_virtual_environment():
    """Set up a virtual environment for the Flask application."""
    
    # Define the virtual environment directory
    venv_dir = "venv"
    
    # Check if virtual environment already exists
    if not os.path.exists(venv_dir):
        print(f"Creating virtual environment in: {venv_dir}")
        try:
            # Create virtual environment
            subprocess.run([sys.executable, "-m", "venv", venv_dir], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Failed to create virtual environment: {e}")
            return

    print("Activating virtual environment...")
    
    # Activate the virtual environment and install dependencies
    activate_script = os.path.join(venv_dir, "Scripts" if os.name == "nt" else "bin", "activate")
    
    # Check if activate script exists
    if not os.path.exists(activate_script):
        print("Activation script not found. Please check your virtual environment setup.")
        return

    # Install dependencies
    try:
        print("Installing dependencies...")
        subprocess.run([os.path.join(venv_dir, "Scripts" if os.name == "nt" else "bin", "pip"), "install", "Flask", "marshmallow", "sqlalchemy", "pytest"], check=True)
        print("Dependencies installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to install dependencies: {e}")

if __name__ == "__main__":
    setup_virtual_environment()