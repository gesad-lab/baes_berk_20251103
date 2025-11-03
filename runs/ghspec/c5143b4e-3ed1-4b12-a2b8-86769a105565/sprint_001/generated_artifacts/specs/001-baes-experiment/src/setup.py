from setuptools import setup, find_packages

setup(
    name="student_api",
    version="1.0.0",
    description="A simple web application for managing Student entities using FastAPI and SQLite.",
    author="Your Name",
    author_email="your_email@example.com",
    packages=find_packages(where='src'),
    package_dir={"": "src"},
    install_requires=[
        "fastapi==0.78.0",  # FastAPI framework
        "uvicorn==0.18.2",  # ASGI server for serving the app
        "SQLAlchemy==1.4.27",  # ORM for database interactions
        "databases==0.5.2",  # Async database layer for SQLAlchemy with SQLite
        "pydantic==1.9.0"  # Data validation and settings management
    ],
    python_requires='>=3.11',
    classifiers=[
        "Programming Language :: Python :: 3.11",
        "Framework :: FastAPI",
        "License :: OSI Approved :: MIT License",
    ],
)