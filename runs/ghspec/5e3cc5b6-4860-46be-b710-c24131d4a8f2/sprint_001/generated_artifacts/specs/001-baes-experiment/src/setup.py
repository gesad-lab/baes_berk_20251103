```python
from setuptools import setup, find_packages

setup(
    name="student_management_app",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.11",
    install_requires=[
        "fastapi",
        "uvicorn",
        "sqlalchemy",
        "pydantic",
        "python-dotenv"  # For managing environment variables
    ],
    entry_points={
        "console_scripts": [
            "start-app=main:run"  # Assumes a run function in main.py starts the FastAPI app
        ]
    },
)
```