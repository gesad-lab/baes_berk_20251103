from setuptools import setup, find_packages

setup(
    name='student_management',
    version='1.0.0',
    description='A simple web application for managing student entities',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'Flask>=2.0',
        'Flask-SQLAlchemy>=2.5',
        'marshmallow>=3.0',
        'python-dotenv>=0.19',
    ],
    entry_points={
        'console_scripts': [
            'create_env=setup:create_virtual_env',
        ],
    },
)

import subprocess
import sys

def create_virtual_env():
    """Create a virtual environment and install dependencies using pipenv."""
    try:
        # Create virtual environment using pipenv
        subprocess.check_call([sys.executable, '-m', 'pipenv', 'install'])
        print("Virtual environment created and dependencies installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error creating virtual environment: {e}")
        sys.exit(1)

# Ensure this function runs when executing the script directly
if __name__ == '__main__':
    create_virtual_env()