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

---

## INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Student Management Web Application

## Version
1.1.0

## Overview
This implementation plan outlines the architecture, technology stack, and implementation approach for creating a new `Teacher` entity within the educational management system. By implementing this feature, the application will enhance its capability to manage instructor details effectively.

## Architecture
The application will follow a modular architecture approach, ensuring the integration of the `Teacher` entity while maintaining existing functionality.

- **API Layer**: Handles incoming requests and responses related to teacher management.
- **Service Layer**: Contains business logic for creating and retrieving teachers.
- **Data Access Layer (DAL)**: Manages database interactions related to teacher entries.
- **Database Layer**: Introduces a new `Teacher` table to facilitate the storage of teacher information.

## Technology Stack
- **Language**: Python 3.11
- **Web Framework**: Flask
- **Database**: SQLite
- **Data Modeling**: SQLAlchemy ORM
- **API Documentation**: OpenAPI (Swagger)
- **Testing Framework**: pytest

## Module Boundaries and Responsibilities
1. **API Module** (`api.py`)
   - Implement new API endpoints for creating and viewing teachers.

2. **Service Module** (`services/teacher_service.py`)
   - Encapsulate business logic related to teacher creation and retrieval.

3. **Data Access Module** (`models/teacher.py`)
   - Define the `Teacher` entity that captures teacher details.

4. **Configuration Module** (`config.py`)
   - No changes needed.

5. **Testing Module** (`tests/test_teacher.py`)
   - Implement tests for the creation and retrieval of teachers.

## Data Model and API Contracts

### Data Model
**Teacher Entity**
- `id`: Integer (auto-generated ID)
- `name`: String (not null)
- `email`: String (not null, must be unique)

### API Endpoints
**1. Create a Teacher**
- **Endpoint**: `POST /teachers`
- **Request Body**: 
    ```json
    {
      "name": "string",
      "email": "string"
    }
    ```
- **Responses**:
    - **201 Created**: Successful creation
      ```json
      {
        "message": "Teacher created successfully."
      }
      ```
    - **400 Bad Request**: Missing fields or invalid email format
      ```json
      {
        "error": {
          "code": "E001",
          "message": "Name and email are required."
        }
      }
      ```

**2. View Existing Teachers**
- **Endpoint**: `GET /teachers`
- **Responses**: 
    - **200 OK**: Successful retrieval
      ```json
      [
        {
          "id": "integer",
          "name": "string",
          "email": "string"
        }
      ]
      ```

## Implementation Approach

### Step-by-Step Implementation

1. **Setup Project Structure**
    - Maintain the existing project structure while adding files for the new `Teacher` entity.

2. **Modify Database Schema**
    - In `models/teacher.py`, define the `Teacher` entity:
      ```python
      from sqlalchemy import Column, Integer, String
      from sqlalchemy.ext.declarative import declarative_base
      
      Base = declarative_base()

      class Teacher(Base):
          """Model representing a teacher in the system."""
          
          __tablename__ = 'teachers'
          
          id = Column(Integer, primary_key=True, autoincrement=True)
          name = Column(String, nullable=False)
          email = Column(String, nullable=False, unique=True)

          def __init__(self, name: str, email: str):
              self.name = name
              self.email = email
      ```

3. **Database Migration**
    - Implement migration to create the `teachers` table:
      ```python
      from alembic import op
      from sqlalchemy import Column, Integer, String

      def upgrade():
          op.create_table(
              'teachers',
              Column('id', Integer, primary_key=True, autoincrement=True),
              Column('name', String, nullable=False),
              Column('email', String, nullable=False, unique=True)
          )

      def downgrade():
          op.drop_table('teachers')
      ```

4. **Develop API Module**
    - Update `api.py` to add handlers for the `POST /teachers` and `GET /teachers` endpoints. Example for creating a teacher:
      ```python
      from flask import Blueprint, request, jsonify
      from services.teacher_service import create_teacher, get_all_teachers
      
      teacher_bp = Blueprint('teacher', __name__)

      @teacher_bp.route('/teachers', methods=['POST'])
      def create_teacher_endpoint():
          data = request.json

          try:
              create_teacher(data['name'], data['email'])
              return jsonify({"message": "Teacher created successfully."}), 201
          except KeyError:
              return jsonify({"error": {"code": "E001", "message": "Name and email are required."}}), 400
          except ValueError as ve:
              return jsonify({"error": {"code": "E002", "message": str(ve)}}), 400

      @teacher_bp.route('/teachers', methods=['GET'])
      def get_teachers_endpoint():
          teachers = get_all_teachers()
          return jsonify(teachers), 200
      ```

5. **Develop Service Layer**
    - In `services/teacher_service.py`, implement the business logic for creating and retrieving teachers:
      ```python
      from models.teacher import Teacher
      from sqlalchemy.orm import Session

      def create_teacher(name: str, email: str) -> None:
          if not is_valid_email(email):
              raise ValueError("Invalid email format.")

          teacher = Teacher(name=name, email=email)
          db_session.add(teacher)  # Assuming 'db_session' is your active SQLAlchemy session
          db_session.commit()

      def get_all_teachers() -> list:
          teachers = db_session.query(Teacher).all()
          return [{"id": teacher.id, "name": teacher.name, "email": teacher.email} for teacher in teachers]
          
      def is_valid_email(email: str) -> bool:
          # Basic validation logic for email format
          pass  # Include actual email validation logic here
      ```

6. **Testing**
    - Create `tests/test_teacher.py` for testing the API endpoints related to teacher creation and retrieval:
      ```python
      import pytest
      from flask import Flask
      from src.api import create_app
      from models.teacher import Teacher, init_db

      @pytest.fixture
      def app():
          app = create_app()
          app.config['TESTING'] = True
          with app.app_context():
              init_db()
          yield app

      def test_create_teacher(client):
          response = client.post('/teachers', json={"name": "John Doe", "email": "john@example.com"})
          assert response.status_code == 201
          data = response.get_json()
          assert data['message'] == "Teacher created successfully."

      def test_create_teacher_missing_fields(client):
          response = client.post('/teachers', json={"name": ""})
          assert response.status_code == 400
          assert response.get_json()['error']['code'] == 'E001'

      def test_get_teachers(client):
          response = client.get('/teachers')
          assert response.status_code == 200
          assert isinstance(response.get_json(), list)
      ```

7. **Documentation**
    - Update API documentation to include new endpoints for teacher creation and retrieval.
    - Adjust the `README.md` file to reflect usage instructions for the new features.

### Scalability, Security, and Maintainability Considerations
- **Scalability**: The current SQLite setup allows for easy migrations; however, consider switching to PostgreSQL for production to handle larger datasets more efficiently.
- **Security**: Ensure proper input validation for teacher data to avoid SQL injection. Secure sensitive data in transit and at rest.
- **Maintainability**: All components follow DRY (Don't Repeat Yourself) principles and utilize the existing architecture to prevent issues during updates.

## Technical Trade-offs and Decisions
- Using SQLite simplifies local testing but may not be suitable for production environments with high concurrency; consider switching databases as needed.
- The decision to implement a separate service layer for business logic enhances maintainability by isolating database access from controller logic.

## Configuration Management
- No additional configuration management changes required for the new teacher management implementation.

## Logging & Monitoring
- Integrate structured logging to capture details on teacher creation requests and results for debugging purposes.

## Deployment Considerations
- Ensure migration scripts are executed during deployment to automatically update the database schema to include the new `teachers` table.

## Future Enhancements
- Future considerations may include functionalities for editing teacher details or linking teachers with specific courses.

## Conclusion
This implementation plan provides a comprehensive framework for introducing a `Teacher` entity to the educational management application, ensuring a maintainable and scalable solution that adheres to established coding principles.

### Existing Code Files: Modifications Needed
1. **New File**: `models/teacher.py` to define the `Teacher` entity.
2. **Update `api.py`**: Add new API endpoints for teacher creation and retrieval.
3. **New File**: `services/teacher_service.py` for the business logic related to teachers.
4. **New File**: `tests/test_teacher.py` for testing the creation and retrieval of teachers.

### Existing Code Files:
- File: `models/__init__.py`
    - No changes needed at this time.
- File: `api.py`
    - Add import for the new teacher API:
      ```python
      from services.teacher_service import create_teacher, get_all_teachers
      ```
    - Add routes for teacher management as outlined in the API module section.

This plan ensures the systematic integration of the new `Teacher` entity within the existing educational management system while maintaining consistency and quality throughout the codebase.