```python
# models.py

"""
models.py

This module defines the SQLAlchemy models used in the application, including the Student model.
It also provides setup instructions for the development environment.

## Setup Instructions

To set up the development environment for this application, follow the steps below:

1. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

2. **Install the required dependencies**:
   Make sure you have `pip` installed, then run:
   ```bash
   pip install fastapi[all] sqlalchemy sqlite
   ```

3. **Verify your installation**:
   You can check if FastAPI, SQLAlchemy, and SQLite are installed correctly by running:
   ```bash
   python -m pip show fastapi sqlalchemy sqlite
   ```

The application uses FastAPI to create a RESTful API, SQLAlchemy as the ORM for database interactions, and SQLite as the database backend.

"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Student(Base):
    """Represents a student in the database."""
    
    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)

    def __repr__(self):
        return f"<Student(name={self.name}, email={self.email})>"
```