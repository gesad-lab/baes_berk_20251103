from setuptools import setup, find_packages

setup(
    name="student_management",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A Flask application for managing student records.",
    packages=find_packages(),  # Automatically find packages in the project
    include_package_data=True,  # Include any package data specified in MANIFEST.in
    install_requires=[
        "Flask>=2.0.0",                    # Flask framework
        "Flask-RESTful>=0.3.9",            # Flask extension for building RESTful APIs
        "SQLAlchemy>=1.4.0",                # ORM for database interactions
        "pytest>=6.0.0",                    # Testing framework
        "marshmallow>=3.0.0",               # For input validation
        "Flask-Cors>=3.0.9",                # Handle Cross-Origin Resource Sharing (CORS)
        "gunicorn>=20.0.4",                 # WSGI server for running the application
    ],
    entry_points={
        "console_scripts": [
            "run=app:main",  # Entry point for running the application (assuming the main app function resides in app.py)
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Framework :: Flask",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires='>=3.6',  # Specify Python version the project requires
)