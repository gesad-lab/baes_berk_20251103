# Implementation Plan: Create Teacher Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Add Course Relationship to Student Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Create Course Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Student Management Web Application

**Version**: 1.1.0  
**Purpose**: Implement the ability to create Teacher entities within the Student Management system to enhance educational management capabilities.

---

## I. Architecture Overview

### 1.1 Architectural Style
- **Microservice architecture**: Continuing with this design for modularity and independent deployment, focusing on the management of Teacher entities alongside existing Student and Course entities.

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
│   ├── models.py           # Database models (Add Teacher entity)
│   ├── schemas.py          # Marshmallow schemas for serialization (Add Teacher schema)
│   ├── routes.py           # API routes for handling requests (Add teacher routes)
│   ├── config.py           # Configuration management
│   └── db.py               # Database initialization and schema handling
├── tests/
│   ├── test_routes.py      # Tests for API routes (Add teacher tests)
│   └── test_validation.py   # Tests for input validation (Add teacher validation tests)
├── .env.example             # Example environment configuration
└── README.md                # Project documentation
```

### 2.2 Responsibilities
- **app.py**: No modifications required.
- **models.py**: Add a `Teacher` model to represent Teacher entities.
- **schemas.py**: Add a Marshmallow schema for the `Teacher` entity to manage serialization and validation.
- **routes.py**: Implement API endpoints for creating and retrieving Teachers.
- **config.py**: No modifications required.
- **db.py**: Update SQLite database schema to include the `teachers` table.

## III. Data Models and API Contracts

### 3.1 Data Model
#### New Model
```python
class Teacher(db.Model):
    __tablename__ = 'teachers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
```

### 3.2 API Endpoints
#### Create Teacher
- **Endpoint**: `POST /teachers`
- **Request Body**:
    ```json
    {
      "name": "John Doe",
      "email": "john.doe@example.com"
    }
    ```
- **Response** (Success):
    ```json
    {
      "id": 1,
      "name": "John Doe",
      "email": "john.doe@example.com"
    }
    ```
- **Response** (Error - Invalid Email):
    ```json
    {
      "error": {
        "code": "E001",
        "message": "Invalid email format."
      }
    }
    ```

#### Retrieve Teacher
- **Endpoint**: `GET /teachers/{teacher_id}`
- **Response** (Success):
    ```json
    {
      "id": 1,
      "name": "John Doe",
      "email": "john.doe@example.com"
    }
    ```
- **Response** (Error - Not Found):
    ```json
    {
      "error": {
        "code": "E002",
        "message": "Teacher not found."
      }
    }
    ```

## IV. Implementation Steps

### 4.1 Development Setup
1. **Environment Setup**:
   - Ensure Python 3.11+ is installed.
   - Update virtual environment and install necessary dependencies:
     ```bash
     source venv/bin/activate
     pip install -U Flask Marshmallow python-dotenv pytest
     ```

### 4.2 Core Functionality
1. **Update Data Model in `models.py`**
   - Add the `Teacher` class to represent Teacher entities.
   ```python
   class Teacher(db.Model):
       ...
   ```

2. **Set Up Marshmallow Schemas in `schemas.py`**
   - Create a new schema for `Teacher` for serialization.
   ```python
   class TeacherSchema(Schema):
       id = fields.Int(dump_only=True)
       name = fields.String(required=True)
       email = fields.Email(required=True)
   ```

3. **Create API Endpoints in `routes.py`**
   - Implement:
     - `POST /teachers` to create a new Teacher.
     - `GET /teachers/{teacher_id}` to retrieve a Teacher by ID.

4. **Update Database Schema in `db.py`**
   - Create a migration script for the SQLite database to add the `teachers` table.
   ```sql
   CREATE TABLE teachers (
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       name TEXT NOT NULL,
       email TEXT NOT NULL UNIQUE
   );
   ```

### 4.3 Validation and Error Handling
- Ensure that the email format is validated, and that the unique constraint for emails is enforced. Use appropriate error messages to inform the user of input issues.

### 4.4 Testing
1. **Unit Tests for Validation and Logic**:
   - Extend `test_validation.py` with tests for the new Teacher creation validation.

2. **Integration Tests for API Endpoints**:
   - Add tests in `test_routes.py` to validate the new Teacher creation and retrieval endpoints.

## V. Documentation and Deployment

### 5.1 Documentation
- Update the `README.md` to include new API functionality for Teacher entities, along with example responses and usage.

### 5.2 Deployment Considerations
- Test the migration process thoroughly on a staging environment before promoting changes to the production environment to ensure no disruption to existing data integrity.

## VI. Success Criteria
1. The application can successfully create a Teacher when valid name and email are provided.
2. Correct retrieval of a Teacher's details based on the Teacher ID in JSON format.
3. Appropriate handling of invalid data during the Teacher creation process.

## VII. Trade-offs and Considerations
- **Database Migration**: Ensuring the new `teachers` table does not disrupt existing schema or data.
- **Input Validations**: Balancing thorough validation against usability to provide a smooth user experience.

## Final Notes
This detailed plan will facilitate the integration of Teacher entity management into the Student Management system, enhancing data organization and communication capabilities within the educational context. Through adherence to the outlined implementation steps, we will uphold existing system functionality and ensure a seamless user experience.

Existing Code Files Adjustments:
File: `tests/test_routes.py`
```python
...

def test_create_teacher_with_valid_data(client):
    """Test creation of a teacher with valid data."""
    response = client.post('/teachers', data=json.dumps({
        'name': 'John Doe',
        'email': 'john.doe@example.com'
    }), content_type='application/json')
    
    assert response.status_code == 201  # Verify success status
    assert response.get_json()['name'] == 'John Doe'  # Verify returned name

def test_retrieve_teacher(client):
    """Test retrieving a teacher's information."""
    response = client.get('/teachers/1')  # Assuming a teacher with id=1 exists
    assert response.status_code == 200
    ...

def test_create_teacher_with_invalid_email(client):
    """Test creation of a teacher with invalid email format."""
    response = client.post('/teachers', data=json.dumps({
        'name': 'Jane Doe',
        'email': 'not-an-email'
    }), content_type='application/json')
    
    assert response.status_code == 400  # Verify error status
    assert response.get_json()['error']['code'] == 'E001'  # Error is due to email
```

File: `tests/test_validation.py`
```python
...

def test_teacher_creation_validation(client):
    """Test validation for Teacher entity."""
    valid_data = {
        'name': 'Jane Doe',
        'email': 'jane.doe@example.com'
    }
    invalid_data_empty_email = {
        'name': 'Jane Doe',
        'email': ''
    }
    invalid_data_invalid_email = {
        'name': 'Jane Doe',
        'email': 'invalid-email'
    }
    
    # Validate valid data
    response = client.post('/teachers', data=json.dumps(valid_data), content_type='application/json')
    assert response.status_code == 201

    # Validate empty email
    response = client.post('/teachers', data=json.dumps(invalid_data_empty_email), content_type='application/json')
    assert response.status_code == 400
    assert response.get_json()['error']['code'] == 'E001'

    # Validate invalid email format
    response = client.post('/teachers', data=json.dumps(invalid_data_invalid_email), content_type='application/json')
    assert response.status_code == 400
    assert response.get_json()['error']['code'] == 'E001'
```

This plan ensures that necessary functionalities for managing Teacher entities are properly integrated while maintaining system integrity and user experience at the forefront.