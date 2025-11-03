```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

# Base class for SQLAlchemy models
Base = declarative_base()

class Course(Base):
    """Course model representing a course in the educational framework.

    Attributes:
        id (int): The unique identifier for the course.
        name (str): The name of the course (required).
        level (str): The level of the course (required).
    """

    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)  # Course name
    level = Column(String, nullable=False)  # Course level

    def __repr__(self):
        return f"<Course(id={self.id}, name={self.name}, level={self.level})>"

# API Endpoints Documentation

"""
API Endpoints for Course Management

1. **Create Course**: 
   - **Endpoint**: POST /courses
   - **Description**: Creates a new course with the provided name and level.
   - **Request Body**:
     - `name` (string, required): The name of the course.
     - `level` (string, required): The level of the course.
   - **Responses**:
     - **200 OK**: Course created successfully, returns course object.
     - **400 Bad Request**: Missing required fields.
   
2. **Retrieve Course**: 
   - **Endpoint**: GET /courses/{id}
   - **Description**: Retrieves the details of an existing course by its ID.
   - **Responses**:
     - **200 OK**: Returns the course's name, level, and ID.
     - **404 Not Found**: Course not found by the provided ID.
"""
```