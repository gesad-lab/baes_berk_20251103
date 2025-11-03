# Implementation Plan: Create Teacher Entity

---
## INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Add Course Relationship to Student Entity

---
## Version
1.0.0

## Overview
This implementation plan outlines the steps necessary to create a new Teacher entity within the educational management system. The addition of this entity allows the system to manage teacher information effectively, addressing the need for robust management of educational staff operations.

## Technology Stack
- **Backend Framework**: Flask (Python)
- **Database**: SQLite (for simplicity and initial development)
- **Data Format**: JSON
- **Development Tools**:
  - Flask-SQLAlchemy for ORM (Object Relational Mapping)
  - Marshmallow for serialization
  - pytest for testing
- **Environment Management**: Virtualenv

## Architecture
The existing monolithic architecture will be extended by introducing a new `Teacher` entity, which maintains the relational integrity of existing entities (Students and Courses) while ensuring scalability and maintainability in the future.

1. **API Layer**:
   - New endpoints to create and retrieve Teacher records.

2. **Service Layer**: 
   - Define business logic for the creation and retrieval of Teacher entities.

3. **Data Access Layer**: 
   - Implement database interactions specifically related to Teacher data management.

4. **Database**: 
   - SQLite will be used for data storage, with an updated schema to include the new `Teacher` table.

## Module Responsibilities
### 1. API Module (`api.py`)
- New routes to handle Teacher operations:
  - `POST /api/v1/teachers`: Create a new teacher.
  - `GET /api/v1/teachers`: Retrieve all teachers.

### 2. Service Module (`services/teacher_service.py`)
- Define functions to:
  - Create a new teacher entry, including validation.
  - Retrieve all teacher records.

### 3. Data Model (`models/teacher.py`)
- Define a new entity called `Teacher`:
  ```python
  from sqlalchemy import Column, Integer, String
  from sqlalchemy.ext.declarative import declarative_base

  Base = declarative_base()

  class Teacher(Base):
      """
      Represents a teacher in the system.

      Attributes:
          id (int): Unique identifier for the teacher (Primary Key).
          name (str): The name of the teacher (Required).
          email (str): The email of the teacher (Required, must be unique).
      """
      __tablename__ = 'teachers'

      id = Column(Integer, primary_key=True, autoincrement=True)
      name = Column(String, nullable=False)
      email = Column(String, nullable=False, unique=True)
  ```

### 4. Database Access (`data_access/teacher_repository.py`)
- Define methods for:
  - Creating a teacher record.
  - Fetching all teachers from the database.

## Data Models and API Contracts
### Data Models
```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Teacher(Base):
    """
    Represents a teacher in the system.

    Attributes:
        id (int): Primary key.
        name (str): The name of the teacher.
        email (str): The email of the teacher, must be unique.
    """
    __tablename__ = 'teachers'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
```

### API Contract
#### Create Teacher
- **Endpoint**: `POST /api/v1/teachers`
- **Request Body**:
  ```json
  {
      "name": "John Doe",
      "email": "john.doe@example.com"
  }
  ```
- **Response**:
  - **Status**: 201 Created
  - **Body**:
  ```json
  {
      "message": "Teacher successfully created."
  }
  ```

#### Get All Teachers
- **Endpoint**: `GET /api/v1/teachers`
- **Response**:
  - **Status**: 200 OK
  - **Body**:
  ```json
  [
      {
          "id": 1,
          "name": "John Doe",
          "email": "john.doe@example.com"
      }
  ]
  ```

## Implementation Approach
1. **Project Setup**:
   - Use the existing Git repository for the project. Update the `requirements.txt` as needed.

2. **Define Teacher Data Model**:
   - Create the `Teacher` model in `models/teacher.py`.

3. **Implement Database Migration**:
   - Create a migration script to add the `teachers` table, ensuring it does not affect existing data integrity.
   
   Example Migration Script:
   ```python
   from flask_migrate import Migrate, MigrateCommand
   from flask_script import Manager
   from models import db, Teacher

   # Initialize migration
   migrate = Migrate(app, db)
   manager = Manager(app)
   manager.add_command('db', MigrateCommand)

   # Create teachers table
   def upgrade():
       db.create_all()  # Automatically finds and creates the `teachers` table

   def downgrade():
       db.drop_table('teachers')  # Drop the teachers table if needed
   ```

4. **Create Service Layer**:
   - Implement functions in `services/teacher_service.py` for creating and retrieving teacher data.

5. **Build API Layer**:
   - Update `api.py` with the new endpoints for creating and retrieving teachers.

6. **Testing**:
   - Write unit tests for the teacher creation and retrieval functionalities in `tests/test_teacher_service.py` and test API endpoints in `tests/test_api.py`.

7. **Documentation**:
   - Update `README.md` with details on how to use the new teacher-related endpoints and any other changes made to the API.

8. **Error Handling**:
   - Implement input validation in the API to check for valid name and email formats before processing requests.

## Scalability Considerations
- The architecture allows for horizontal scalability. As operations grow, the application can scale by adding more instances to handle increased loads.
- Future features like teacher assignments can seamlessly integrate with the existing structure.

## Security Considerations
- Input validation to mitigate risks of SQL injection and XSS attacks.
- Ensure that error responses do not expose sensitive information.
  
## Deployment Considerations
- Document environment variables and configuration settings necessary for deployment. Ensure migrations run without downtime.

## Testing Strategy
- **Unit Tests**: Validate the creation of teacher entities and error handling through the service layer.
- **Integration Tests**: Ensure proper API functionality and correct responses from the new teacher endpoints.
- **Contract Tests**: Verify that APIs adhere to defined contracts for APIs.

## Success Metrics
- The application successfully creates teacher entities and returns confirmation using the `POST` endpoint.
- The application retrieves and displays a list of teachers with names and emails in JSON format.
- Input validation functionality correctly provides actionable error messages for invalid input.
- The database schema is updated with the new Teacher table and maintains existing data integrity.

## Conclusion
This implementation plan outlines the approach to ensure the educational management system can effectively manage teacher information, thus enhancing overall organizational capabilities regarding educational staff management.

---

### Existing Code Files Modifications:
1. **New File**: `models/teacher.py` for the Teacher model.
2. **New File**: `services/teacher_service.py` for the business logic of managing teachers.
3. **Modifications to** `api.py` to include new endpoints for creating and retrieving teachers.
4. **New File**: `tests/test_teacher_service.py` to cover tests for the new teacher features.

Existing Code Files:
File: `api.py`
```python
from flask import Flask, jsonify, request
from services.teacher_service import create_teacher, get_all_teachers

app = Flask(__name__)

@app.route('/api/v1/teachers', methods=['POST'])
def add_teacher():
    data = request.json
    response = create_teacher(data)
    return jsonify(response), 201

@app.route('/api/v1/teachers', methods=['GET'])
def list_teachers():
    teachers = get_all_teachers()
    return jsonify(teachers), 200
```

File: `tests/test_api.py`
```python
import pytest
from app import create_app, db
from services.teacher_service import create_teacher, get_all_teachers

@pytest.fixture
def setup_database():
    db.create_all()  # Create the database tables
    yield
    db.session.remove()  # Cleanup the session
    db.drop_all()  # Cleanup the database

def test_create_teacher(setup_database):
    response = create_teacher({"name": "John Doe", "email": "john.doe@example.com"})
    assert response["message"] == "Teacher successfully created."

def test_list_teachers(setup_database):
    create_teacher({"name": "John Doe", "email": "john.doe@example.com"})
    teachers = get_all_teachers()
    assert len(teachers) == 1
```

File: `tests/test_teacher_service.py`
```python
import pytest
from models import db, Teacher
from services.teacher_service import create_teacher, get_all_teachers

@pytest.fixture
def setup_database():
    db.create_all()  # Create the database tables
    yield
    db.session.remove()  # Cleanup the session
    db.drop_all()  # Cleanup the database

def test_create_teacher(setup_database):
    result = create_teacher({"name": "John Doe", "email": "john.doe@example.com"})
    assert result['message'] == "Teacher successfully created."
    assert Teacher.query.count() == 1

def test_get_all_teachers(setup_database):
    create_teacher({"name": "John Doe", "email": "john.doe@example.com"})
    teachers = get_all_teachers()
    assert len(teachers) == 1
    assert teachers[0]['name'] == "John Doe"
```

This implementation plan ensures that new modules integrate seamlessly with existing functionalities while maintaining backward compatibility and ensuring data integrity.