# Implementation Plan: Create Course Entity

---
## INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Add Email Field to Student Entity

---
## 1. Architecture Overview

The architecture for extending the Student Management Web Application will maintain the established microservices-oriented approach, adding the Course entity without disrupting existing functionality or data integrity. 

- **API Layer**: Introduce new endpoints for creating and retrieving courses with robust error handling.
- **Service Layer**: Implement business logic for Course management, including data validation and persistence.
- **Data Layer**: Apply a database migration to incorporate the Course table while ensuring existing Student data remains intact.

## 2. Technology Stack

- **Programming Language**: Python 3.x
- **Web Framework**: Flask
- **Database**: SQLite
- **ORM Tool**: SQLAlchemy
- **Serialization**: Marshmallow
- **Migration Tool**: Alembic for migrations

## 3. Module Boundaries and Responsibilities

### 3.1 API Layer
- **Responsibilities**:
  - Introduce new endpoints to create and retrieve courses.

- **Endpoints**:
  - `POST /courses`: Create a new Course.
  - `GET /courses`: Retrieve all Courses.

### 3.2 Service Layer
- **Responsibilities**:
  - Handle the logic associated with Course creation and retrieval, ensuring valid data management.

### 3.3 Data Layer
- **Responsibilities**:
  - Manage database interactions and migrations for the new Course entity.

## 4. Data Models

### 4.1 Course Model
Define the Course entity model:
```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Course(Base):
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)  # Course title
    level = Column(String, nullable=False)  # Difficulty level
```

## 5. API Contracts

### Endpoint: Create a Course
- **Method**: POST
- **URL**: `/courses`
- **Request Body**:
```json
{
  "name": "Introduction to Python",
  "level": "Beginner"
}
```
- **Success Response**:
  - **Status**: 201 Created
  - **Body**:
```json
{
  "id": 1,
  "name": "Introduction to Python",
  "level": "Beginner"
}
```

### Error Response: Invalid Course Creation
- **Status**: 400 Bad Request
- **Body**:
```json
{
  "error": {
    "code": "E001",
    "message": "The name and level fields are required."
  }
}
```

### Endpoint: Retrieve All Courses
- **Method**: GET
- **URL**: `/courses`
- **Success Response**:
  - **Status**: 200 OK
  - **Body**:
```json
[
  {
    "id": 1,
    "name": "Introduction to Python",
    "level": "Beginner"
  },
  {
    "id": 2,
    "name": "Advanced Java",
    "level": "Advanced"
  }
]
```

## 6. Implementation Approach

### 6.1 Setting Up the Environment
1. Ensure the updated packages are installed, if not already:
   ```bash
   pip install Flask Flask-SQLAlchemy Flask-Marshmallow Alembic
   ```

### 6.2 Database Migration Strategy
- Utilize Alembic for database migrations to create the Course table:
  1. Initialize Alembic (if not initialized):
     ```bash
     alembic init migrations
     ```
  2. Create a new migration script for the Course table. Inside the migration script, add:
```python
def upgrade():
    op.create_table('courses',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('level', sa.String(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )

def downgrade():
    op.drop_table('courses')
```
- Ensure that the migration script runs at the application startup to create the Course table.

### 6.3 API Development Updates
- Create the `/courses` endpoints in the Flask application:
```python
@app.route('/courses', methods=['POST'])
def create_course():
    data = request.get_json()
    if 'name' not in data or not data['name'] or 'level' not in data or not data['level']:
        return jsonify({"error": {"code": "E001", "message": "The name and level fields are required."}}), 400

    new_course = Course(name=data['name'], level=data['level'])
    db.session.add(new_course)
    db.session.commit()
    return jsonify({"id": new_course.id, "name": new_course.name, "level": new_course.level}), 201

@app.route('/courses', methods=['GET'])
def get_courses():
    courses = Course.query.all()
    return jsonify([{"id": course.id, "name": course.name, "level": course.level} for course in courses]), 200
```

## 7. Testing Strategy

### 7.1 Test Coverage
Develop tests for the new Course endpoints using pytest:
- Create tests for successful course creation and retrieval.
- Include edge cases for errors (e.g., missing fields).

### 7.2 Test Scenarios
1. **Creating a Course**: Ensure the API successfully creates a course and returns the correct data.
2. **Validation for Missing Fields**: Assert a 400 error when attempting to create a course without required fields.
3. **Retrieving Courses**: Validate that all current courses are retrieved accurately.

## 8. Security Considerations

- Sanitize user inputs to prevent SQL injection when creating courses.
- Implement validation logic for the `level` field to restrict input to predefined values (e.g., Beginner, Intermediate, Advanced).

## 9. Deployment Considerations

### 9.1 Production Deployment
- Ensure migration scripts are tested and run on production startup to prevent application downtime.
  
### 9.2 Health Check Endpoint
- Include an existing health check endpoint for application monitoring.

```python
@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"}), 200
```

## 10. Documentation

Update the `README.md` file:
- Include new endpoint specifications for the `/courses` endpoints.
- Provide instructions for running migrations and testing the application.

## Technical Trade-offs

1. **Migration Tooling**: Utilizing Alembic simplifies maintaining the database schema but requires setting up initial migrations.
2. **Error Handling**: Initial validation errors can impact user experience; clear and actionable messages are crucial.
3. **Course Level Validation**: Adding predefined levels restricts user errors but may limit the flexibility of course definitions in future iterations.

This implementation plan outlines the necessary steps to effectively add the Course entity to the Student Management Web Application, ensuring robust functionality while maintaining compatibility with existing data models.

Existing Code Files:
File: tests/test_course.py
```python
import pytest
from app import app, db, Course

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Create the database schema for testing
        yield client
        with app.app_context():
            db.drop_all()  # Clean up after the tests

def test_create_course_with_valid_data(client):
    """Test creating a course with valid data."""
    response = client.post('/courses', json={"name": "Introduction to Python", "level": "Beginner"})
    assert response.status_code == 201
    assert 'id' in response.get_json()

def test_create_course_without_name(client):
    """Test validation error for missing course name."""
    response = client.post('/courses', json={"level": "Beginner"})
    assert response.status_code == 400
    assert response.get_json()['error']['code'] == 'E001'
```