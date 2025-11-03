# Implementation Plan: Create Teacher Entity

---

## INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Add Course Relationship to Student Entity

---
## INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Create Course Entity

---
## INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Add Email Field to Student Entity

---
## INCREMENTAL DEVELOPMENT CONTEXT

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
│   ├── models.py            # Database models (add Teacher model here)
│   ├── schemas.py           # Marshmallow schemas (add Teacher schema here)
│   ├── routes.py            # API endpoint definitions (add Teacher routes here)
│   ├── database.py          # Database configuration and initialization
│   └── config.py            # Configuration settings
│
├── tests/
│   ├── test_routes.py       # Unit and integration tests for API endpoints (add Teacher tests here)
│   └── test_models.py       # Unit tests for database models (add Teacher tests here)
│
├── .env                     # Environment variables for configuration
├── .env.example             # Example environment variables file
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
```

## II. Database Design

### 2.1 Schema Definition
- **Teacher Table** (`teachers`):
  - `id`: Integer (Primary Key)
  - `name`: String (not null)
  - `email`: String (not null, unique)

### 2.2 Initialization
- Implement a migration strategy using Flask-Migrate to create the `teachers` table while preserving existing `Student` and `Course` data.

## III. API Design

### 3.1 Endpoints
- **POST /teachers**
  - Request Body: 
    ```json
    {
      "name": "string",
      "email": "string"
    }
    ```
  - Success Response: 
    ```json
    {
      "message": "Teacher created successfully."
    }
    ```
  - Status Code: `201 Created`
  - Error Response (missing name): 
    ```json
    {
      "error": {
        "code": "E001",
        "message": "Name is required."
      }
    }
    ```
  - Status Code: `400 Bad Request`
  - Error Response (missing email): 
    ```json
    {
      "error": {
        "code": "E002",
        "message": "Email is required."
      }
    }
    ```
  - Status Code: `400 Bad Request`

## IV. Implementation Plan

### 4.1 Step-by-step Implementation
1. **Setup Environment**
   - Ensure the `.env` file is updated with any necessary configuration settings.

2. **Update the Model**
   - Create a new `Teacher` model in `models.py`.
   ```python
   class Teacher(db.Model):
       __tablename__ = 'teachers'
       id = db.Column(db.Integer, primary_key=True)
       name = db.Column(db.String, nullable=False)
       email = db.Column(db.String, nullable=False, unique=True)
   ```

3. **Database Migration**
   - Use Flask-Migrate to create a migration script for adding the `teachers` table:
   ```bash
   flask db migrate -m "Create teachers table"
   flask db upgrade
   ```

4. **Update Marshmallow schemas**
   - Create a new schema in `schemas.py` for the `Teacher` model.
   ```python
   class TeacherSchema(ma.SQLAlchemyAutoSchema):
       class Meta:
           model = Teacher
           fields = ("id", "name", "email")
   ```

5. **Add API Endpoint**
   - Implement the `POST /teachers` endpoint in `routes.py` to create a teacher.
   ```python
   @app.route('/teachers', methods=['POST'])
   def create_teacher():
       data = request.get_json()
       # validation for name and email
       if not data.get('name'):
           return {"error": {"code": "E001", "message": "Name is required."}}, 400
       if not data.get('email'):
           return {"error": {"code": "E002", "message": "Email is required."}}, 400

       new_teacher = Teacher(name=data['name'], email=data['email'])
       db.session.add(new_teacher)
       db.session.commit()
       
       return {"message": "Teacher created successfully."}, 201
   ```

6. **Implement Error Handling and Validation**
   - In the `create_teacher` function, implement checks and return structured error responses if name or email is missing.

7. **Testing**
   - Write new unit tests for the `Teacher` model and API endpoint in the `tests` folder.
   - Ensure tests cover successful creation and validation failure scenarios.
   - Aim for a minimum of 70% coverage on the new business logic.

8. **Documentation**
   - Update the README.md file to include details regarding how to create a teacher through the API.
   - Ensure the API documentation reflects changes for the new endpoint.

## V. Testing Strategy

### 5.1 Types of Tests
- **Unit Tests**: Validate the `Teacher` model and its schema functionality.
- **Integration Tests**: Verify the API endpoint for creating teachers.
- **Contract Tests**: Ensure that the API responses meet defined specifications.

### 5.2 Coverage Requirements
- Minimum coverage target: 70% for all new business logic, with critical paths targeting 90%.

## VI. Deployment Considerations

### 6.1 Environment Management
- Confirm that any new environment configuration required for the teacher entity is documented.

### 6.2 Deployment Steps
- Run migrations to ensure the `teachers` table is properly created without risking existing data integrity.
- Verify that the application starts without errors post-deployment.

### 6.3 Monitoring & Logging
- Implement monitoring mechanisms for API performance and error rates post-deployment.

## VII. Conclusion

This implementation plan outlines the steps required to create a `Teacher` entity within our application. By adhering to this structured plan, we will ensure a maintainable codebase and robust API capabilities for teacher management.

### Modifications to Existing Files:
- **models.py**: Added a new `Teacher` class to handle teacher data.
- **schemas.py**: Included a schema for `Teacher` to validate input data.
- **routes.py**: Implemented the `POST /teachers` endpoint for teacher creation.
- **tests/test_routes.py**: Created tests for the new `POST /teachers` endpoint.
- **tests/test_models.py**: Created tests for the `Teacher` model and its functionalities.

### Database Migration Strategy:
- Use Flask-Migrate to automatically generate a migration script that will introduce the `teachers` table while ensuring the integrity of existing data models.

Existing Code Files Example:
File: tests/test_routes.py
```python
import pytest
from src.database import get_db, init_db
from src.models import Teacher
from flask import json

@pytest.fixture()
def db():
    """Set up a test database environment."""
    init_db()
    yield get_db()  

def test_create_teacher_success(db):
    """Test creating a new teacher with valid data."""
    response = app.test_client().post('/teachers', json={"name": "John Smith", "email": "john.smith@example.com"})
    assert response.status_code == 201
    assert response.json['message'] == "Teacher created successfully."

def test_create_teacher_missing_name(db):
    """Test creating a teacher without a name."""
    response = app.test_client().post('/teachers', json={"email": "john.smith@example.com"})
    assert response.status_code == 400
    assert response.json['error']['code'] == "E001"
    assert response.json['error']['message'] == "Name is required."

def test_create_teacher_missing_email(db):
    """Test creating a teacher without an email."""
    response = app.test_client().post('/teachers', json={"name": "John Smith"})
    assert response.status_code == 400
    assert response.json['error']['code'] == "E002"
    assert response.json['error']['message'] == "Email is required."
```

File: tests/test_models.py
```python
import pytest
from src.database import get_db, init_db
from src.models import Teacher

@pytest.fixture()
def db():
    """Set up a test database environment."""
    init_db()
    yield get_db()  

def test_create_teacher(db):
    """Test creating a new teacher."""
    teacher = Teacher(name="Jane Doe", email="jane.doe@example.com")
    db.session.add(teacher)
    db.session.commit()
    assert teacher.id is not None

def test_teacher_email_uniqueness(db):
    """Test that teacher emails must be unique."""
    teacher1 = Teacher(name="John Doe", email="john.doe@example.com")
    teacher2 = Teacher(name="Jane Roe", email="john.doe@example.com")
    db.session.add(teacher1)
    db.session.commit()
    
    with pytest.raises(Exception):
        db.session.add(teacher2)
        db.session.commit()
``` 

This implementation plan provides a detailed guide for the creation of the `Teacher` entity while ensuring that the existing functionality and data integrity of the application are maintained.