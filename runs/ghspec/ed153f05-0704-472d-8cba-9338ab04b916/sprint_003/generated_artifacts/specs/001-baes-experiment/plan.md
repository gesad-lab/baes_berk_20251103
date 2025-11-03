# Implementation Plan: Create Course Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Add Email Field to Student Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Student Management Web Application

## I. Architecture Overview

### 1.1 Technology Stack
- **Backend Framework**: Flask (Python)
- **Database**: SQLite 
- **Serialization**: Marshmallow for JSON validation and serialization
- **Environment Management**: pipenv for virtual environment and dependency management
- **Testing Framework**: pytest 
- **API Documentation**: OpenAPI (Swagger) for documenting endpoints 

### 1.2 Module Structure
```
student_management/
│
├── src/
│   ├── app.py               # Application entry point
│   ├── models.py            # Database models (add Course model here)
│   ├── schemas.py           # Marshmallow schemas (add Course schema here)
│   ├── routes.py            # API endpoint definitions (add Course routes here)
│   ├── database.py          # Database configuration and initialization
│   └── config.py            # Configuration settings
│
├── tests/
│   ├── test_routes.py       # Unit and integration tests for API endpoints (add Course tests here)
│   └── test_models.py       # Unit tests for database models (add Course tests here)
│
├── .env                     # Environment variables for configuration
├── .env.example             # Example environment variables file
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
```

## II. Database Design

### 2.1 Schema Definition
- **Course Table**:
  - `id`: Integer (Primary Key, Auto-Increment)
  - `name`: String (NOT NULL)
  - `level`: String (NOT NULL)

### 2.2 Initialization
- Implement a migration strategy using Flask-Migrate to add a new `Course` table to the database while preserving existing data.

## III. API Design

### 3.1 Endpoints
- **POST /courses**
  - Request Body: 
    ```json
    {
      "name": "string",
      "level": "string"
    }
    ```
  - Success Response: 
    ```json
    {
      "id": "number",
      "name": "string",
      "level": "string"
    }
    ```
  - Status Code: `201 Created`
  - Error Response (missing fields): 
    ```json
    {
      "error": {
        "code": "E001",
        "message": "Both 'name' and 'level' fields are required."
      }
    }
    ```
  - Status Code: `400 Bad Request`

- **GET /courses/{id}**
  - Success Response: 
    ```json
    {
      "id": "number",
      "name": "string",
      "level": "string"
    }
    ```
  - Status Code: `200 OK`
  - Error Response (course not found): 
    ```json
    {
      "error": {
        "code": "E002",
        "message": "Course not found."
      }
    }
    ```
  - Status Code: `404 Not Found`

- **GET /courses**
  - Success Response (list of all courses): 
    ```json
    [
      {
        "id": "number",
        "name": "string",
        "level": "string"
      },
      ...
    ]
    ```
  - Status Code: `200 OK`

## IV. Implementation Plan

### 4.1 Step-by-step Implementation
1. **Setup Environment**
   - Update the `.env` file for any new configuration settings (if necessary).

2. **Update the Model**
   - Create a new `Course` model in `models.py` to include `name` and `level` attributes.
   ```python
   class Course(db.Model):
       id = db.Column(db.Integer, primary_key=True)
       name = db.Column(db.String, nullable=False)
       level = db.Column(db.String, nullable=False)
   ```

3. **Database Migration**
   - Use Flask-Migrate to create a migration script for adding the `Course` table.
   - Create and apply migration scripts that establish the new schema without affecting existing tables.
   ```bash
   flask db migrate -m "Add Course table"
   flask db upgrade
   ```

4. **Update Marshmallow schemas**
   - Create a new schema in `schemas.py` for the `Course` entity validation.
   ```python
   class CourseSchema(ma.SQLAlchemyAutoSchema):
       class Meta:
           model = Course
           fields = ("id", "name", "level")
   ```

5. **Add API Endpoints**
   - Implement the `POST /courses` endpoint in `routes.py` to create a new course.
   - Implement the `GET /courses/{id}` and `GET /courses` endpoints in `routes.py` to fetch courses.
   ```python
   @app.route('/courses', methods=['POST'])
   def create_course():
       ...
   
   @app.route('/courses/<int:id>', methods=['GET'])
   def get_course(id):
       ...
   
   @app.route('/courses', methods=['GET'])
   def get_all_courses():
       ...
   ```

6. **Implement Validation**
   - Handle validation for required fields (name and level) in the POST request, returning structured error responses when they are missing.

7. **Testing**
   - Write new unit tests for `Course` model and API endpoints in the `tests` folder, including scenarios for successful creations and retrievals.
   - Confirm that success and error cases are thoroughly tested to achieve a target of at least 70% coverage for business logic.

8. **Documentation**
   - Update the README.md file with details regarding the new course feature.
   - Ensure the API documentation reflects the new endpoints for creating and retrieving courses.

## V. Testing Strategy

### 5.1 Types of Tests
- **Unit Tests**: Validate the `Course` model and schema functionality.
- **Integration Tests**: Verify API endpoints for course creation and retrieval.
- **Contract Tests**: Ensure that the API responses conform to defined specifications.

### 5.2 Coverage Requirements
- Minimum coverage target: 70% for all business logic including Course.
- Critical paths (course creation and retrieval) should aim for at least 90% coverage.

## VI. Deployment Considerations

### 6.1 Environment Management
- Update guidelines for environment management to reflect new configurations (if any).

### 6.2 Deployment Steps
- Run migrations to ensure the new database schema is up to date.
- Ensure the application starts successfully without errors related to the Course implementation.

### 6.3 Monitoring & Logging
- Consider implementing tracking for error rates and API performance in future iterations.

## VII. Conclusion

This implementation plan outlines the steps required to introduce a Course entity to the Student Management Web Application. By adhering to the prescribed development workflow, we ensure a maintainable codebase and a seamless user experience with robust validation for our API outputs.

### Modifications to Existing Files:
- **models.py**: Created a new `Course` class to define the Course entity.
- **schemas.py**: Added a new schema to validate and serialize Course data.
- **routes.py**: Implemented the new API endpoints for course creation and retrieval.
- **tests/test_models.py**: Created new tests for the `Course` model and its behaviors.
- **tests/test_routes.py**: Implemented tests for API endpoints dealing with course functionalities.

### Database Migration Strategy:
- Utilize Flask-Migrate to automatically create migration scripts that will add the new `Course` table while preserving all existing data in the system.

Existing Code Files Example:
File: tests/test_routes.py
```python
import pytest
from src.database import get_db, init_db
from src.models import Course

@pytest.fixture(scope='module')
def db():
    """Set up a fresh database for testing."""
    init_db()  # Initialize the database
    yield get_db()  # Provide the database to the test
    # Teardown if applicable...

def test_course_creation(db):
    """Test creating a new course record."""
    new_course = Course(name="Mathematics", level="Intermediate")
    db.session.add(new_course)
    db.session.commit()
    assert new_course.id is not None  # Ensures course is created with an ID
```

File: tests/test_models.py
```python
import pytest
from src.database import get_db, init_db
from src.models import Course

@pytest.fixture(scope='module')
def db():
    """Set up a fresh database for testing."""
    init_db()  # Initialize the database
    yield get_db()  # Provide the database to the test

def test_course_creation_with_required_fields(db):
    """Test creating a course with required fields."""
    course = Course(name="Science", level="Advanced")
    db.session.add(course)
    db.session.commit()
    assert course.name == "Science"
    assert course.level == "Advanced"
```