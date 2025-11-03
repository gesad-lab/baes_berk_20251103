# Implementation Plan: Create Teacher Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Add Email Field to Student Entity

---

## Version
**Version**: 1.1.0

## Purpose
This implementation plan outlines the technical design for enhancing the Student Management Web Application by introducing a Teacher entity. This feature enables the application to manage teacher information effectively, thereby improving educational management capabilities.

## Architecture Overview
- **Architecture Pattern**: RESTful API
- **Technology Stack**:
  - **Programming Language**: Python
  - **Web Framework**: Flask
  - **Database**: SQLite
  - **ORM**: SQLAlchemy
  - **Testing Framework**: pytest

## Module Boundaries and Responsibilities
1. **API Module**:
   - Introduce new endpoints for creating and retrieving Teacher entities. This module will manage request handling and responses for teacher operations.

2. **Data Access Layer**:
   - Extend the existing SQLAlchemy models to include a new Teacher model representing the Teacher entity. This will involve defining the necessary fields and relationships.

3. **Testing Module**:
   - Develop tests to ensure the correct functionality of the new Teacher entity's creation and retrieval, verifying adherence to the specification.

## API Endpoints Design
### 1. Create Teacher
- **Endpoint**: `POST /api/v1/teachers`
- **Request Body**:
  ```json
  {
    "name": "John Doe",
    "email": "john.doe@example.com"
  }
  ```
- **Response**:
  - **Success (201 Created)**:
    ```json
    {
      "message": "Teacher created successfully",
      "teacher_id": 1
    }
    ```
  - **Error (400 Bad Request)**:
    ```json
    {
      "error": {
        "code": "E001",
        "message": "Name and email are required"
      }
    }
    ```

### 2. Retrieve Teacher Details
- **Endpoint**: `GET /api/v1/teachers/{teacher_id}`
- **Response**:
  - **Success (200 OK)**:
    ```json
    {
      "id": 1,
      "name": "John Doe",
      "email": "john.doe@example.com"
    }
    ```
  - **Error (404 Not Found)**:
    ```json
    {
      "error": {
        "code": "E002",
        "message": "Teacher not found"
      }
    }
    ```

## Data Model
### Teacher Model
- **Table Name**: teachers
  - `id`: Integer, primary key, auto-generated.
  - `name`: String, required (max length assumed to be 255 characters).
  - `email`: String, required (must be unique).

### SQLAlchemy Model Definition
```python
# models.py (modifications)
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Teacher(db.Model):
    __tablename__ = 'teachers'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)

    def __repr__(self):
        return f'<Teacher {self.name}>'
```

## Implementation Steps
1. **Database Migration**:
   - Create a migration script to add the `teachers` table.
   - Using Alembic, generate the migration script:
     ```bash
     alembic revision --autogenerate -m "Create teachers table"
     ```
   - The migration script will look like:
     ```python
     def upgrade():
         op.create_table(
             'teachers',
             sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
             sa.Column('name', sa.String(length=255), nullable=False),
             sa.Column('email', sa.String(length=255), nullable=False, unique=True),
         )

     def downgrade():
         op.drop_table('teachers')
     ```

2. **Update Application Structure**:
   Ensure application structure accommodates new functionality:
   ```
   /student_management
   ├── src/
   │   ├── app.py
   │   ├── models.py  # Add the Teacher model
   │   ├── routes.py  # Add new routes for teacher management
   │   ├── tests/
   │   │   ├── test_routes.py  # Add tests for teacher endpoints
   ├── config.py
   ├── requirements.txt
   ├── README.md
   ```

3. **Modify `routes.py`**:
   Implement logic for the teacher creation endpoint (`POST /api/v1/teachers`) and retrieval endpoint (`GET /api/v1/teachers/{teacher_id}`).

```python
# routes.py (modifications)
from flask import request, jsonify
from .models import db, Teacher

@app.route('/api/v1/teachers', methods=['POST'])
def create_teacher():
    data = request.json
    name = data.get('name')
    email = data.get('email')

    if not name or not email:
        return jsonify({'error': {'code': 'E001', 'message': 'Name and email are required'}}), 400
    
    new_teacher = Teacher(name=name, email=email)
    db.session.add(new_teacher)
    db.session.commit()

    return jsonify({'message': 'Teacher created successfully', 'teacher_id': new_teacher.id}), 201

@app.route('/api/v1/teachers/<int:teacher_id>', methods=['GET'])
def get_teacher(teacher_id):
    teacher = Teacher.query.get(teacher_id)
    if not teacher:
        return jsonify({'error': {'code': 'E002', 'message': 'Teacher not found'}}), 404

    return jsonify({'id': teacher.id, 'name': teacher.name, 'email': teacher.email}), 200
```

4. **Update Tests**:
   Add tests in `tests/test_routes.py` for the new functionality:
   - **New Test Cases**:
     - `test_create_teacher_with_valid_data_succeeds()`
     - `test_get_teacher_details_returns_correct_data()`

```python
def test_create_teacher_with_valid_data_succeeds(client):
    """Test creating a new teacher with valid data."""
    payload = {
        "name": "Jane Doe",
        "email": "jane.doe@example.com"
    }
    response = client.post('/api/v1/teachers', json=payload)
    assert response.status_code == 201
    assert response.get_json() == {'message': 'Teacher created successfully', 'teacher_id': 1}

def test_get_teacher_details_returns_correct_data(client):
    """Test retrieving teacher details successfully."""
    response = client.get('/api/v1/teachers/1')
    assert response.status_code == 200
    assert response.get_json()['name'] == "Jane Doe"
```

5. **Run Database Migration**:
   Apply the migration to the development database:
   ```bash
   alembic upgrade head
   ```

6. **Verify All Functionalities**:
   Confirm that all functionalities work as expected, particularly the automated tests for creation and retrieval scenarios.

## Error Handling & Validation
- Validation will be implemented for inputs during teacher creation, ensuring both `name` and `email` are provided:
  - Return a 400 error if the fields are missing.
- Ensure that duplicate email entries are handled by the database constraints, and appropriate error messages are logged.

## Security Considerations
- Sanitize and validate all inputs on the API endpoints to guard against SQL injection or similar vulnerabilities.

## Testing Strategy
- **Unit Tests**: Validate individual logic for the Teacher model.
- **Integration Tests**: Use the pytest framework to validate the new API endpoints.

## Scalability Considerations
- This new model for teachers is designed to scale as additional functionalities such as teacher assignments to courses may be added in the future.

## Logging & Monitoring
- Implement structured logging for key events such as teacher creation and errors.

## Deployment Considerations
- Ensure existing health check endpoints remain functional and monitor responses after the implementation.

## Trade-offs & Decisions
- The implementation focuses on core functionality, ensuring quick development and deployment, while deferring more complex relationship handling for future iterations in accordance with agile principles.

This implementation plan provides a structured approach to adding the Teacher entity to the Student Management Web Application, following through with necessary integrations and validations as outlined in the specification.