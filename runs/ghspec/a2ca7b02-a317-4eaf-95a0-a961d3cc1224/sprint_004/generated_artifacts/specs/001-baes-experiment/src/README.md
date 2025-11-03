# README.md

# README for Student-Course Enrollment System

## Overview
This project exposes RESTful APIs for managing students and their course enrollments. It utilizes FastAPI for the API framework and SQLAlchemy for database interactions, providing efficient handling of student enrollment data.

## Getting Started

### Prerequisites
- Python 3.8+
- FastAPI
- SQLAlchemy
- Pytest for testing
- SQLite (in-memory for testing)

### Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```
2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application
To run the FastAPI application:
```bash
uvicorn api.student:router --reload
```

### API Endpoints
- `POST /students/{student_id}/courses`: Enroll a student in a course.
- `GET /students/{student_id}`: Retrieve a student's details including their enrolled courses.

### Testing
To run tests, ensure that all dependencies are installed, then execute:
```bash
pytest tests/
```

## Unit Tests for Service Methods and API Endpoints
To ensure the reliability of the services and endpoints, we have implemented unit tests located in `tests/test_student.py`. These tests cover scenarios including:

- Successful enrollment in a course
- Attempt to enroll in a non-existent course
- Retrieving a student's information including enrolled courses

### Example of Test Implementation
```python
import pytest
from services.student_service import StudentService
from db.database import Database
from models.student import Student 
from models.course import Course
  
@pytest.fixture
def setup_database():
    # Setup an in-memory SQLite database for testing
    db = Database('sqlite:///:memory:')
    db.create_schema()  # Create necessary tables
    yield db
    db.close()

def test_enroll_student_in_course_valid(setup_database):
    # Arrange
    student = Student(name="John Doe")
    course = Course(name="Introduction to Programming", level="Beginner")
    setup_database.add(student)
    setup_database.add(course)

    # Act
    result = StudentService.enroll_student_in_course(student.id, course.id)

    # Assert
    assert result is True
    assert student.courses == [course]  # Assuming a relationship attribute on Student

def test_enroll_student_in_nonexistent_course(setup_database):
    # Arrange
    student = Student(name="Jane Doe")
    setup_database.add(student)

    # Act & Assert
    with pytest.raises(ValueError) as excinfo:
        StudentService.enroll_student_in_course(student.id, 999)  # Nonexistent course
    assert str(excinfo.value) == "Course not found"
```

This structure allows for comprehensive testing of the core business logic, ensuring that enrollments are processed correctly and invalid operations are appropriately handled.

## Conclusion
This project framework, along with its well-defined testing structure, ensures that the system is robust, maintainable, and easy to extend in the future.