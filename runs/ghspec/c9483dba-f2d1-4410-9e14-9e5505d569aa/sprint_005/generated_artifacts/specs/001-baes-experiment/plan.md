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
# Implementation Plan: Add Email Field to Student Entity

## Version
1.1.0

## Overview
This implementation plan outlines the architecture, technology stack, data models, API contracts, and implementation approach required for introducing a new `Teacher` entity within the existing student management application. This feature aims to enhance the management of educational structures by allowing for the management of teacher information.

## Architecture

### 1.1 Application Architecture
- **Type**: RESTful web application
- **Design Pattern**: MVC (Model-View-Controller) for separation of concerns
- **Framework**: Flask (Python) for the backend
- **Database**: SQLite for local development and testing, with migration support for schema updates.

### 1.2 Module Structure
1. **Models**:
   - Introduce a new `Teacher` model.

2. **Controllers**:
   - Create handlers for creating and retrieving teacher details.

3. **Routes**:
   - Define API endpoints that handle requests for creating and retrieving teachers.

4. **Database Management**:
   - Logic for creating the `Teacher` table and handling migrations.

## Technology Stack
- **Backend Framework**: Flask
- **Database**: SQLite
- **ORM**: SQLAlchemy for database interactions
- **Request Validation**: Marshmallow for input validation and serialization
- **Testing Framework**: pytest for testing the application
- **Environment Management**: Python 3 and virtual environments

## Data Models

### 2.1 New Teacher Model
```python
from sqlalchemy import Column, Integer, String
from your_app.database import Base  # Adjust import based on actual structure

class Teacher(Base):
    __tablename__ = 'teachers'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)

    def __repr__(self):
        return f'<Teacher {self.id}: {self.name}, Email: {self.email}>'
```

### 2.2 Database Schema
The SQLite database will now include the following structure for the `Teacher` entity:
- **teachers**
  - `id`: Integer (Primary Key, Auto-increment)
  - `name`: String (Non-nullable)
  - `email`: String (Non-nullable)

## API Contracts

### 3.1 Endpoints
1. **Create Teacher**
   - **Endpoint**: `POST /teachers`
   - **Request Body**:
     ```json
     {
       "name": "John Doe",
       "email": "john.doe@example.com"
     }
     ```
   - **Responses**:
     - **201 Created**:
       ```json
       {
         "id": 1,
         "name": "John Doe",
         "email": "john.doe@example.com"
       }
       ```
     - **400 Bad Request** (if `name` or `email` is missing):
       ```json
       {
         "error": {
           "code": "E001",
           "message": "Name and Email are required"
         }
       }
       ```

2. **Retrieve Teacher**
   - **Endpoint**: `GET /teachers/{id}`
   - **Responses**:
     - **200 OK**:
       ```json
       {
         "id": 1,
         "name": "John Doe",
         "email": "john.doe@example.com"
       }
       ```
     - **404 Not Found** (if the teacher does not exist):
       ```json
       {
         "error": {
           "code": "E002",
           "message": "Teacher not found"
         }
       }
       ```

## Implementation Approach

### 4.1 Steps to Implement
1. **Modify Project Structure**:
   ```bash
   student_management/
       ├── src/
       │   ├── app.py
       │   ├── models.py       # Add Teacher model
       │   ├── controllers/
       │   │   ├── teacher_controller.py # New controller for Teacher entity
       │   └── database.py
       ├── migrations/         # Create migration scripts for Teacher table
       ├── tests/
       │   ├── test_teacher.py # Create tests for Teacher functionality
       └── README.md
   ```

2. **Database Migration**:
   - Utilize Flask-Migrate (using Alembic) for database migrations.
   - Create a migration script to add the `teachers` table:
     ```bash
     flask db migrate -m "Add Teacher table"
     flask db upgrade
     ```

3. **Route Definitions**:
   - Define new `POST /teachers` and `GET /teachers/<id>` routes in `app.py`:
     ```python
     from controllers.teacher_controller import create_teacher, get_teacher

     @app.route('/teachers', methods=['POST'])
     @app.route('/teachers/<int:id>', methods=['GET'])
     ```

4. **Controller Logic**:
   - Implement logic in `teacher_controller.py` to handle create and retrieve functionality, ensuring input validations:
     ```python
     from flask import request, jsonify
     from models import Teacher, db  # Import necessary components

     @app.route('/teachers', methods=['POST'])
     def create_teacher():
         data = request.get_json()
         name = data.get('name')
         email = data.get('email')

         if not name or not email:
             return jsonify({"error": {"code": "E001", "message": "Name and Email are required"}}), 400

         new_teacher = Teacher(name=name, email=email)
         db.session.add(new_teacher)
         db.session.commit()

         return jsonify({"id": new_teacher.id, "name": new_teacher.name, "email": new_teacher.email}), 201

     @app.route('/teachers/<int:id>', methods=['GET'])
     def get_teacher(id):
         teacher = Teacher.query.get(id)
         if not teacher:
             return jsonify({"error": {"code": "E002", "message": "Teacher not found"}}), 404

         return jsonify({"id": teacher.id, "name": teacher.name, "email": teacher.email}), 200
     ```

5. **Validation and Error Handling**:
   - Ensure validation logic for the required fields, `name` and `email`.
   - By structuring error responses consistently to match existing API standards.

6. **Testing**:
   - Create unit tests in `test_teacher.py` for both creating and retrieving functionality.
   - Ensure a minimum of 70% coverage for this new functionality.

## Security Considerations
- Validate teacher inputs to avoid SQL injection and other vulnerabilities.
- Sanitize inputs to prevent injection risks.

## Scalability Considerations
- While starting with SQLite, the design should allow future transitions to a more robust database system (e.g., PostgreSQL) as the student management application scales.

## Conclusion
This implementation plan provides a comprehensive approach for integrating the `Teacher` entity into the student management system. Following this plan will ensure that the addition of the teacher functionality aligns with existing application protocols and maintains the integrity of current data management processes.

### Existing Code Files:
File: `src/models.py`
```python
# Add the new Teacher model
from sqlalchemy import Column, Integer, String
from your_app.database import Base  # Adjust import based on actual structure

class Teacher(Base):
    __tablename__ = 'teachers'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)

    def __repr__(self):
        return f'<Teacher {self.id}: {self.name}, Email: {self.email}>'
```

File: `src/controllers/teacher_controller.py`
```python
from flask import request, jsonify
from models import Teacher, db

@app.route('/teachers', methods=['POST'])
def create_teacher():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')

    if not name or not email:
        return jsonify({"error": {"code": "E001", "message": "Name and Email are required"}}), 400

    new_teacher = Teacher(name=name, email=email)
    db.session.add(new_teacher)
    db.session.commit()

    return jsonify({"id": new_teacher.id, "name": new_teacher.name, "email": new_teacher.email}), 201

@app.route('/teachers/<int:id>', methods=['GET'])
def get_teacher(id):
    teacher = Teacher.query.get(id)
    if not teacher:
        return jsonify({"error": {"code": "E002", "message": "Teacher not found"}}), 404

    return jsonify({"id": teacher.id, "name": teacher.name, "email": teacher.email}), 200
```

File: `tests/test_teacher.py`
```python
import pytest
from app import app  # Assuming 'app' is the Flask app instance
from models import Teacher, db  # Assuming Teacher model is defined in 'models.py'

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_create_teacher_success(client):
    """Test creating a new teacher with valid data."""
    response = client.post('/teachers', json={"name": "John Doe", "email": "john.doe@example.com"})
    assert response.status_code == 201
    assert response.json['name'] == "John Doe"

def test_create_teacher_missing_fields(client):
    """Test creating a teacher without required fields."""
    response = client.post('/teachers', json={"name": "John Doe"})
    assert response.status_code == 400
    assert response.json['error']['code'] == 'E001'

def test_get_teacher_success(client):
    """Test retrieving a teacher by ID."""
    new_teacher = Teacher(name="Jane Doe", email="jane.doe@example.com")
    db.session.add(new_teacher)
    db.session.commit()

    response = client.get(f'/teachers/{new_teacher.id}')
    assert response.status_code == 200
    assert response.json['name'] == "Jane Doe"

def test_get_teacher_not_found(client):
    """Test retrieving a teacher that does not exist."""
    response = client.get('/teachers/999')
    assert response.status_code == 404
    assert response.json['error']['code'] == 'E002'
```

This plan covers the requirements necessary to implement the `Teacher` entity while ensuring integration with existing modules and maintaining backward compatibility with established database models.