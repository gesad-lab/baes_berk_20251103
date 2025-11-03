# Implementation Plan: Create Course Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Student Management Web Application

**Version**: 1.1.0  
**Purpose**: Introduce a new Course entity to enhance academic course management within the Student Management system.

---

## I. Architecture Overview

### 1.1 Architectural Style
- **Microservice architecture**: Continuing the microservice approach to allow independent updates and scalability of the service responsible for course management.

### 1.2 Technology Stack
- **Backend Framework**: Flask (Python)
- **Database**: SQLite
- **Data Serialization**: Marshmallow (for JSON serialization)
- **Environment Configuration**: python-dotenv (for managing configuration)
- **Testing Framework**: pytest

## II. Module Boundaries and Responsibilities

### 2.1 Application Structure
```
student_management/
├── src/
│   ├── app.py              # Main application entry point
│   ├── models.py           # Database models (add new Course model)
│   ├── schemas.py          # Marshmallow schemas for serialization (add Course schema)
│   ├── routes.py           # API routes for handling requests (add Course routes)
│   ├── config.py           # Configuration management
│   └── db.py               # Database initialization and schema handling
├── tests/
│   ├── test_routes.py      # Tests for API routes (add Course tests)
│   └── test_validation.py   # Tests for input validation (add Course validation tests)
├── .env.example             # Example environment configuration
└── README.md                # Project documentation
```

### 2.2 Responsibilities
- **app.py**: No modifications required.
- **models.py**: Create a new `Course` model to represent the Course entity.
- **schemas.py**: Add Marshmallow schema for Course serialization and validation.
- **routes.py**: Implement API endpoints for creating and retrieving Course entities.
- **config.py**: No modifications required.
- **db.py**: Update SQLite database schema to include the new Course table.

## III. Data Models and API Contracts

### 3.1 Data Model
#### Course
```python
class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    level = db.Column(db.String(50), nullable=False)
```

### 3.2 API Endpoints
#### Create Course
- **Endpoint**: `POST /courses`
- **Request Body**:
    ```json
    {
      "name": "Introduction to Programming",
      "level": "Beginner"
    }
    ```
- **Response** (Success):
    ```json
    {
      "message": "Course created successfully",
      "course": {
        "id": 1,
        "name": "Introduction to Programming",
        "level": "Beginner"
      }
    }
    ```
- **Response** (Error - Missing Fields):
    ```json
    {
      "error": {
        "code": "E001",
        "message": "Name and level are required"
      }
    }
    ```
- **Response** (Error - Invalid Input):
    ```json
    {
      "error": {
        "code": "E002",
        "message": "Invalid input format"
      }
    }
    ```

#### Retrieve Course
- **Endpoint**: `GET /courses/{id}`
- **Response** (Success):
    ```json
    {
      "id": 1,
      "name": "Introduction to Programming",
      "level": "Beginner"
    }
    ```
- **Response** (Error - Course Not Found):
    ```json
    {
      "error": {
        "code": "E003",
        "message": "Course not found"
      }
    }
    ```

## IV. Implementation Steps

### 4.1 Development Setup
1. **Environment Setup**:
   - Ensure Python 3.11+ is installed.
   - Update virtual environment and install any new necessary dependencies:
     ```bash
     source venv/bin/activate
     pip install -U Flask Marshmallow python-dotenv pytest
     ```

### 4.2 Core Functionality
1. **Update Data Model in `models.py`**
   - Add the new `Course` class to represent courses in the database.

2. **Set Up Marshmallow Schemas in `schemas.py`**
   - Create a new `CourseSchema` to manage the serialization and validation of course data.
   ```python
   class CourseSchema(Schema):
       id = fields.Int(dump_only=True)
       name = fields.Str(required=True)
       level = fields.Str(required=True)
   ```

3. **Create API Endpoints in `routes.py`**
   - Develop the `POST /courses` endpoint to accept course creation requests and validate the input.
   - Implement the `GET /courses/{id}` endpoint to retrieve course details by ID.

4. **Update Database Schema in `db.py`**
   - Create a migration script for the SQLite database to add the `Course` table with appropriate fields.
   ```sql
   CREATE TABLE courses (
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       name VARCHAR(100) NOT NULL,
       level VARCHAR(50) NOT NULL
   );
   ```

### 4.3 Validation and Error Handling
- Implement input validation checks to ensure both `name` and `level` are provided and are valid strings. Return informative error messages for invalid requests.

### 4.4 Testing
1. **Unit Tests for Validation and Logic**:
   - Extend `test_validation.py` to include tests for the Course entity input validation.
  
2. **Integration Tests for API Endpoints**:
   - Validate the new endpoints in `test_routes.py` focusing on correct creation and retrieval of courses.

## V. Documentation and Deployment

### 5.1 Documentation
- Update the `README.md` to document the new API endpoints for creating and retrieving Course entities. Ensure JSON structure and error codes are detailed.

### 5.2 Deployment Considerations
- Ensure the production environment is properly configured to apply the new database migrations without downtime. Provide clear instructions on implementing migrations.

## VI. Success Criteria
1. Successful creation of a Course entity when valid `name` and `level` values are provided.
2. Correct retrieval of Course details including the `name` and `level`.
3. Proper handling of requests with missing or invalid fields, yielding appropriate error messages.

## VII. Trade-offs and Considerations
- **Database Migration**: Care must be taken to ensure the new `Course` table is created without affecting existing data models. Proper testing will verify this.
  
- **Input Validation Complexity**: Striking a balance on user-friendly error messages while securing against potential misuse of input fields.

## Final Notes
This implementation plan delineates the necessary steps to introduce the Course entity into the Student Management Web Application while preserving the integrity and performance of existing components. Adhering to these detailed guidelines will facilitate efficient development, testing, and deployment of the new functionality.

Existing Code Files:
File: tests/test_routes.py
```python
import pytest
from flask import json
from src.app import app  # Assuming the Flask app is initialized in app.py

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_create_course_with_valid_data(client):
    response = client.post('/courses', data=json.dumps({
        'name': 'Introduction to Programming',
        'level': 'Beginner'
    }), content_type='application/json')
    
    assert response.status_code == 201  # Code indicates that the course was created
    data = response.get_json()
    assert 'course' in data and data['course']['name'] == 'Introduction to Programming'
```

File: tests/test_validation.py
```python
import pytest
from src.schemas import CourseSchema
from marshmallow.exceptions import ValidationError

class TestCourseValidation:
    @pytest.fixture
    def course_schema(self):
        """Fixture to provide a Course schema instance for testing."""
        return CourseSchema()

    def test_valid_course_data(self, course_schema):
        """Test validation for valid course data"""
        valid_data = {
            "name": "Introduction to Programming",
            "level": "Beginner"
        }
        # Validate and assert that it passes
```

This structured approach ensures that the feature development aligns with existing patterns and practices while enhancing overall system capabilities.