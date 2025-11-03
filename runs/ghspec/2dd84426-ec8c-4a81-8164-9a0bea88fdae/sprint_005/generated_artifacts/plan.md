# Implementation Plan: Create Teacher Entity

---
## INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Add Course Relationship to Student Entity

---
## Version
**Version**: 1.1.0

## Technology Stack
- **Backend Framework**: Flask (Python)
- **Database**: SQLite
- **ORM**: SQLAlchemy
- **API Documentation**: Swagger/OpenAPI
- **Testing Framework**: pytest
- **Environment Management**: venv (Python virtual environments)
- **Serialization**: Marshmallow

## Architecture Overview
This implementation features the addition of a new `Teacher` entity to the existing educational framework, ensuring that it integrates seamlessly with the existing `Student` and `Course` entities. The schema change through migration emphasizes maintaining integrity and performance and minimizes disruption to the current system.

### Module Boundaries
1. **API Module**:
   - Add a new route to handle the creation of `Teacher` entities.
  
2. **Service Module**:
   - Implement logic for creating `Teacher` records.
  
3. **Data Module**:
   - Define the `Teacher` entity model to facilitate ORM interactions.
  
4. **Validation Module**:
   - Implement input validation to confirm the presence and correctness of required fields for creating a `Teacher`.
  
5. **Deployment/Configuration Module**:
   - Implement migration logic for the new `Teacher` table schema.

## Data Models
Define the `Teacher` entity in `src/models/teacher.py`.

```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Teacher(Base):
    __tablename__ = 'teachers'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)

    def __repr__(self):
        return f"<Teacher(name={self.name}, email={self.email})>"
```

### Database Schema
The new `teachers` table will have the following schema:
- **id**: Integer (Primary Key)
- **name**: String (Required)
- **email**: String (Required and Unique)

## API Contracts

### 1. Create a Teacher
- **Endpoint**: `POST /teachers`
- **Request Body**:
    ```json
    {
      "name": "string",  // required
      "email": "string"  // required and must be unique
    }
    ```
- **Responses**:
  - **201 Created**:
    ```json
    {
      "message": "Teacher successfully created."
    }
    ```
  - **400 Bad Request** (Missing name):
    ```json
    {
      "error": {
        "code": "E001",
        "message": "The name field is required."
      }
    }
    ```
  - **400 Bad Request** (Missing email):
    ```json
    {
      "error": {
        "code": "E002",
        "message": "The email field is required."
      }
    }
    ```
  - **400 Bad Request** (Invalid email format):
    ```json
    {
      "error": {
        "code": "E003",
        "message": "Email format is invalid."
      }
    }
    ```

## Implementation Approach

### Step 1: Setup Project Structure
No specific changes needed to the existing project structure; new files will be added for the `Teacher` entity.

### Step 2: Install Dependencies
No new dependencies are required; existing tech stack will remain in use.

### Step 3: Update the Data Module
- Create a new file `src/models/teacher.py` and implement the `Teacher` model as defined above.

### Step 4: Database Migration
- Create a migration script using Flask-Migrate to add the `teachers` table:
```bash
flask db migrate -m "Add Teacher table"
flask db upgrade
```
- Ensure that the migration script does not affect existing `Student` or `Course` data.

### Step 5: Extend the Service Module
- In `src/services/teacher_service.py`, implement the creation logic for a teacher.

```python
from models.teacher import Teacher
from sqlalchemy.exc import IntegrityError

def create_teacher(db_session, name, email):
    new_teacher = Teacher(name=name, email=email)
    db_session.add(new_teacher)
    try:
        db_session.commit()
        return new_teacher
    except IntegrityError:
        db_session.rollback()
        raise ValueError("Email already exists.")
```

### Step 6: Implement the API Module
- Create a new file `src/api/teacher_api.py` and define the endpoint for creating a teacher.

```python
from flask import Blueprint, request, jsonify
from services.teacher_service import create_teacher
from db import get_db_session
from validation.teacher_validation import validate_teacher

teacher_bp = Blueprint('teacher', __name__)

@teacher_bp.route('/teachers', methods=['POST'])
def add_teacher():
    data = request.get_json()
    errors = validate_teacher(data)
    if errors:
        return jsonify({"error": errors}), 400

    teacher = create_teacher(get_db_session(), data['name'], data['email'])
    return jsonify({"message": "Teacher successfully created."}), 201
```

### Step 7: Input Validation
- In `src/validation/teacher_validation.py`, implement validation for required fields.
  
```python
def validate_teacher(data):
    errors = {}
    
    if not data.get('name'):
        errors['name'] = "The name field is required."
        
    if not data.get('email'):
        errors['email'] = "The email field is required."
    elif '@' not in data['email']:
        errors['email'] = "Email format is invalid."
    
    return errors
```

### Step 8: Write Unit Tests
- Create `tests/api/test_teacher_api.py` to include tests for creating teachers, ensuring coverage for both success and error scenarios.

```python
import pytest
from flask import Flask
from src.api.teacher_api import teacher_bp

@pytest.fixture()
def app():
    app = Flask(__name__)
    app.register_blueprint(teacher_bp)
    return app

def test_create_teacher(client):
    response = client.post('/teachers', json={"name": "John Doe", "email": "john@example.com"})
    assert response.status_code == 201
    assert response.json["message"] == "Teacher successfully created."

def test_create_teacher_missing_name(client):
    response = client.post('/teachers', json={"email": "john@example.com"})
    assert response.status_code == 400
    assert response.json["error"]["name"] == "The name field is required."
```

### Step 9: Documentation
- Update API documentation to reflect the new endpoint for teacher creation, including details about request and response formats.

### Step 10: Continuous Integration
- Ensure all tests run successfully in CI/CD pipeline with the inclusion of the newly implemented tests for the `Teacher` feature.

## Summary of Technical Decisions
- Flask and SQLAlchemy are maintained to ensure consistent development practices.
- SQLite continues to serve as the database, with migration strategies in place to add the `teachers` table.
- This implementation prioritizes backward compatibility and respects existing models.

## Next Steps
1. Review this plan with stakeholders for approval.
2. Proceed with the implementation based on the outlined approach.
3. Conduct tests on the new feature focusing on the use cases defined in the specification.

## Modifications Needed to Existing Files
1. **src/models/teacher.py**:
   - Create the new `Teacher` model as detailed above.

2. **src/api/teacher_api.py**:
   - Implement the `/teachers` endpoint for creating teachers.

3. **src/services/teacher_service.py**:
   - Implement the `create_teacher` function for adding teachers.

4. **src/validation/teacher_validation.py**:
   - Implement validation for required fields when creating a teacher.

5. **tests/api/test_teacher_api.py**:
   - Write tests for the teacher creation functionality, covering all success and error scenarios.

6. **db/__init__.py**:
   - If not present, ensure the database session management is correctly set up to enable the creation of the `Teacher` entity.

## Documentation
- Update API documentation to accurately represent the changes for the creation of teachers, ensuring clarity for future reference and usage.

--- 

This implementation plan outlines a comprehensive approach to establish the `Teacher` entity within existing architecture while maintaining operational integrity.