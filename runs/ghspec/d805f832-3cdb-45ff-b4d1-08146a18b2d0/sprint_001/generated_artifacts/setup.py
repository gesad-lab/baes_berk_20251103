from setuptools import setup, find_packages

setup(
    name="student_management",
    version="1.0.0",
    description="A simple web application for managing Student entities through a RESTful API.",
    author="Your Name",
    author_email="youremail@example.com",
    url="https://github.com/yourusername/student_management",
    packages=find_packages(),
    install_requires=[
        "fastapi[all]",
        "sqlalchemy",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.11',
    entry_points={
        'console_scripts': [
            'run-app=main:app',  # Assuming `main.py` has an instance of FastAPI app named `app`
        ],
    },
)