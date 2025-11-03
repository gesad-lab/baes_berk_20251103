from setuptools import setup, find_packages

setup(
    name="your_project_name",
    version="0.1.0",
    description="A FastAPI Project for managing Student records.",
    author="Your Name",
    author_email="your_email@example.com",
    packages=find_packages(),
    install_requires=[
        "fastapi[all]",  # FastAPI with all recommended features
        "SQLAlchemy",     # ORM for database operations
        "pytest",         # Testing framework
        "pytest-asyncio", # For testing async code
        "pydantic",       # Data validation and settings management
    ],
    entry_points={
        "console_scripts": [
            "start-api=your_project_name.main:run",  # Assuming there's a 'main' module to run the FastAPI app
        ],
    },
    python_requires=">=3.7",
)