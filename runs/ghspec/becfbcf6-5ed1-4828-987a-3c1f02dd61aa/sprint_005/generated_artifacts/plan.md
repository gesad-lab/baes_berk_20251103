# Implementation Plan: Create Teacher Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Add Course Relationship to Student Entity

---
## 1. Architecture Overview

The architecture for extending the Student Management Web Application to incorporate a Teacher entity will continue with the existing microservice architecture pattern. This integration allows us to manage educator information effectively while ensuring that the current functionality, specifically related to Students and Courses, remains intact.

- **API Layer**: Extend the existing API to include endpoints that manage Teacher entities.
- **Service Layer**: Add business logic for creating and retrieving Teacher records, including validation of required fields.
- **Data Layer**: Incorporate migrations to implement the new Teacher table while preserving data integrity of existing entities.

## 2. Technology Stack

- **Programming Language**: Python 3.x
- **Web Framework**: Flask
- **Database**: SQLite (to maintain consistency with the previous sprint)
- **ORM Tool**: SQLAlchemy
- **Serialization**: Marshmallow
- **Migration Tool**: Alembic for database migrations

## 3. Module Boundaries and Responsibilities

### 3.1 API Layer
- **Responsibilities**:
  - Introduce endpoints for creating and retrieving Teacher records.

- **Endpoints**:
  - `POST /teachers`: Add a new teacher record.
  - `GET /teachers/{teacher_id}`: Retrieve information about a specific teacher.

### 3.2 Service Layer
- **Responsibilities**:
  - Handle the logic for creating Teacher records, ensuring that required fields are provided and that data integrity is maintained.

### 3.3 Data Layer
- **Responsibilities**:
  - Manage database interactions and the requirement for migration to implement the new Teacher entity.

## 4. Data Models

### 4.1 Teacher Model
Define the Teacher entity:
```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Teacher(Base):
    __tablename__ = 'teachers'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)  # Email should be unique
```

### 4.2 Updated Database Model Migration
- Create a new migration that adds the Teacher table:
```python
def upgrade():
    op.create_table('teachers',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('email', sa.String(), nullable=False, unique=True)
    )

def downgrade():
    op.drop_table('teachers')
```

## 5. API Contracts

### Endpoint: Create a Teacher
- **Method**: POST
- **URL**: `/teachers`
- **Request Body**:
```json
{
  "name": "John Doe",
  "email": "johndoe@example.com"
}
```
- **Success Response**:
  - **Status**: 201 Created
  - **Body**:
```json
{
  "id": 1,
  "name": "John Doe",
  "email": "johndoe@example.com"
}
```

### Error Response: Missing Required Fields
- **Status**: 400 Bad Request
- **Body**:
```json
{
  "error": {
    "code": "E001",
    "message": "Missing required fields: name, email."
  }
}
```

### Endpoint: Retrieve a Teacher
- **Method**: GET
- **URL**: `/teachers/{teacher_id}`
- **Success Response**:
  - **Status**: 200 OK
  - **Body**:
```json
{
  "id": 1,
  "name": "John Doe",
  "email": "johndoe@example.com"
}
```

### Error Response: Teacher Not Found
- **Status**: 404 Not Found
- **Body**:
```json
{
  "error": {
    "code": "E002",
    "message": "Teacher not found."
  }
}
```

## 6. Implementation Approach

### 6.1 Setting Up the Environment
1. Ensure the required packages are installed:
   ```bash
   pip install Flask Flask-SQLAlchemy Flask-Marshmallow Alembic
   ```

### 6.2 Database Migration Strategy
- Incorporate Alembic migrations to create the Teacher table:
  1. Create migration script as shown in section 4.2.
  2. Ensure that migrations run on application startup to maintain data integrity.

### 6.3 API Development Updates
- Introduce the `/teachers` endpoint route in the Flask app:
```python
@app.route('/teachers', methods=['POST'])
def create_teacher():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')

    # Validating required fields
    if not name or not email:
        return jsonify({"error": {"code": "E001", "message": "Missing required fields: name, email."}}), 400
    
    # Check for unique email
    if Teacher.query.filter_by(email=email).first():
        return jsonify({"error": {"code": "E003", "message": "Email must be unique."}}), 400

    new_teacher = Teacher(name=name, email=email)
    db.session.add(new_teacher)
    db.session.commit()
    
    return jsonify({
        "id": new_teacher.id,
        "name": new_teacher.name,
        "email": new_teacher.email
    }), 201

@app.route('/teachers/<int:teacher_id>', methods=['GET'])
def get_teacher(teacher_id):
    teacher = Teacher.query.get(teacher_id)
    if not teacher:
        return jsonify({"error": {"code": "E002", "message": "Teacher not found."}}), 404
    
    return jsonify({
        "id": teacher.id,
        "name": teacher.name,
        "email": teacher.email
    }), 200
```

## 7. Testing Strategy

### 7.1 Test Coverage
Develop tests for the new endpoints:
- Test successful creation of Teacher records and retrieval of Teacher information.
- Validate error responses for missing fields and duplicate emails.

### 7.2 Test Scenarios
1. **Create a Teacher**: Ensure API succeeds and creates the new teacher record.
2. **Error Handling for Missing Required Fields**: Check API returns 400 error for missing name or email.
3. **Retrieve a Teacher**: Confirm correct teacher details are returned for valid teacher IDs.

## 8. Security Considerations

- Sanitize all user inputs to prevent SQL injections.
- Ensure email uniqueness is enforced to prevent duplicate records.

## 9. Deployment Considerations

### 9.1 Production Deployment
- Ensure migration scripts are executed on production to seamlessly integrate the Teacher entity without downtime.

### 9.2 Health Check Endpoint
- Maintain a health check endpoint to monitor application status:
```python
@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"}), 200
```

## 10. Documentation

Update `README.md`:
- Add documentation for new endpoints `/teachers` (POST) and `/teachers/{teacher_id}` (GET).
- Provide usage examples and test case scenarios for validating teacher management functionalities.

## Technical Trade-offs

1. **Adding Unique Constraints**: Enforcing email uniqueness simplifies data integrity management but increases validation complexity at creation time.
2. **API Error Responses**: Providing detailed error responses improves user feedback but requires robust error handling logic to maintain security and performance.

This implementation plan outlines the steps necessary for integrating the Teacher entity into the Student Management System, ensuring enhanced functionality while maintaining data integrity and existing application structure.

Existing Code Files:
File: tests/test_teacher.py
```python
import pytest
from app import app, db, Teacher

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Create the database schema for testing

            # Creating sample teachers for tests
            teacher1 = Teacher(name="John Doe", email="johndoe@example.com")
            db.session.add(teacher1)
            db.session.commit()

        yield client
```
This revised implementation plan adheres to the specifications and outlines how to incrementally develop and integrate a new Teacher entity while maintaining existing project constraints and structures.