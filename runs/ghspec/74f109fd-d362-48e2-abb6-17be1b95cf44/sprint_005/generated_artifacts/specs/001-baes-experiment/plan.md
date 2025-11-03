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

## Version: 1.1.0

## Overview
This implementation plan outlines the creation of a new Teacher entity within the educational management system. This feature enables the system to effectively store and manage instructor information, and it sets the foundation for future functionalities such as teacher assignments and class management.

## Technology Stack
- **Backend Framework**: Flask (Python)
- **Database**: SQLite
- **ORM**: SQLAlchemy
- **API Format**: JSON
- **Testing Framework**: pytest
- **Request Validation**: marshmallow

## Architecture Overview
The application will be updated to include a new Teacher module with the following structure:

### Module Structure
- **src/**
  - **models/**: Contains the database models (e.g., Teacher).
    - Implement a `Teacher` model to represent the new entity.
  - **repositories/**: Handles all database interactions.
    - Implement a `TeacherRepository` for CRUD operations related to teachers.
  - **services/**: Contains business logic including teacher creation and fetching.
    - Create a service to handle the core business logic for creating and retrieving teacher records.
  - **api/**: Manages API routes and requests.
    - Add routes for teacher creation and retrieval.
  - **db/**: Manages database initialization and migrations.
    - Implement migrations to add the Teacher table to the database.
  - **config/**: Holds configuration settings.
  - **app.py**: Main application entry point.

- **tests/**: Contains unit and integration tests organized by feature.
  - Add new tests for creating and retrieving teachers.

## Data Model
### Teacher Model
```python
from sqlalchemy import Column, Integer, String
from database import Base

class Teacher(Base):
    """Model for the Teacher entity."""
    
    __tablename__ = 'teachers'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    email = Column(String, nullable=False)

    __mapper_args__ = {
        "order_by": id
    }
```

## API Contract
### Endpoints
1. **Create Teacher**
   - **Method**: POST
   - **Endpoint**: `/api/v1/teachers`
   - **Request Payload**:
   ```json
   {
     "name": "Jane Doe",
     "email": "jane.doe@example.com"
   }
   ```

   - **Response (201 Created)**:
   ```json
   {
     "id": 1,
     "name": "Jane Doe",
     "email": "jane.doe@example.com",
     "message": "Teacher has been successfully created."
   }
   ```

   - **Response (400 Bad Request)**: Missing Fields
   ```json
   {
     "error": {
       "code": "E001",
       "message": "Both name and email fields are required for creating a teacher."
     }
   }
   ```

   - **Response (400 Bad Request)**: Invalid Email Format
   ```json
   {
     "error": {
       "code": "E002",
       "message": "Email format is invalid."
     }
   }
   ```

2. **Retrieve Teacher by ID**
   - **Method**: GET
   - **Endpoint**: `/api/v1/teachers/<int:id>`
   - **Response (200 OK)**:
   ```json
   {
     "id": 1,
     "name": "Jane Doe",
     "email": "jane.doe@example.com"
   }
   ```

   - **Response (404 Not Found)**:
   ```json
   {
     "error": {
       "code": "E003",
       "message": "Teacher not found."
     }
   }
   ```

## Implementation Approach
1. **Set Up Project Structure**:
   - Utilize the existing directory layout and integrate the new files and modifications as described below.

2. **Create Teacher Model**:
   - Implement the `Teacher` model to represent the new entity with its required attributes.

3. **Database Schema Update**:
   - Write a database migration script to create the `teachers` table:
   ```sql
   CREATE TABLE teachers (
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       name TEXT NOT NULL,
       email TEXT NOT NULL
   );
   ```

4. **Implement API Endpoints**:
   - Add Flask routes in `api` to handle teacher creation and retrieval, ensuring proper error handling for missing or invalid input.

5. **Create Teacher Repository**:
   - Implement a `TeacherRepository` to encapsulate CRUD operations for the `Teacher` entity.
   ```python
   from models.teacher import Teacher
   from database import session

   class TeacherRepository:
       """Handles database interactions for Teacher entity."""

       def create_teacher(self, name, email):
           teacher = Teacher(name=name, email=email)
           session.add(teacher)
           session.commit()
           return teacher

       def get_teacher(self, teacher_id):
           return session.query(Teacher).filter_by(id=teacher_id).first()
   ```

6. **Create Teacher Service**:
   - Implement a service that encapsulates the business logic for creating and retrieving teachers. This service will handle validation for required fields and email format.
   ```python
   from repositories.teacher_repository import TeacherRepository
   from sqlalchemy.exc import IntegrityError

   class TeacherService:
       """Encapsulates business logic for Teacher operations."""

       def __init__(self):
           self.teacher_repo = TeacherRepository()

       def create_teacher(self, name, email):
           if not name or not email:
               raise ValueError("Both name and email fields are required.")
           if not self.validate_email(email):
               raise ValueError("Email format is invalid.")

           return self.teacher_repo.create_teacher(name, email)

       def validate_email(self, email):
           import re
           return re.match(r"[^@]+@[^@]+\.[^@]+", email) is not None

       def get_teacher(self, teacher_id):
           teacher = self.teacher_repo.get_teacher(teacher_id)
           if not teacher:
               raise ValueError("Teacher not found.")
           return teacher
   ```

7. **Implement API Logic**:
   - Add routes in the `api` layer to implement the creation and retrieval of teachers. This will include error handling to return appropriate responses if validation fails.
   ```python
   from flask import Blueprint, request, jsonify
   from services.teacher_service import TeacherService

   teacher_api = Blueprint('teacher_api', __name__)
   teacher_service = TeacherService()

   @teacher_api.route('/api/v1/teachers', methods=['POST'])
   def create_teacher():
       data = request.json
       try:
           teacher = teacher_service.create_teacher(data['name'], data['email'])
           return jsonify({
               "id": teacher.id,
               "name": teacher.name,
               "email": teacher.email,
               "message": "Teacher has been successfully created."
           }), 201
       except ValueError as e:
           return jsonify({"error": {"code": "E001", "message": str(e)}}), 400

   @teacher_api.route('/api/v1/teachers/<int:id>', methods=['GET'])
   def get_teacher(id):
       try:
           teacher = teacher_service.get_teacher(id)
           return jsonify({
               "id": teacher.id,
               "name": teacher.name,
               "email": teacher.email
           }), 200
       except ValueError as e:
           return jsonify({"error": {"code": "E003", "message": str(e)}}), 404
   ```

8. **Testing**:
   - Write unit tests to validate both the creation and retrieval functionalities for teachers, ensuring tests cover successful operations and error scenarios.
   ```python
   import pytest
   from services.teacher_service import TeacherService

   @pytest.fixture
   def teacher_service():
       return TeacherService()

   def test_create_teacher(teacher_service):
       """Test creating a new teacher."""
       teacher = teacher_service.create_teacher("Jane Doe", "jane.doe@example.com")
       assert teacher.name == "Jane Doe"
       assert teacher.email == "jane.doe@example.com"

   def test_create_teacher_missing_fields(teacher_service):
       """Test creating a teacher with missing fields raises ValueError."""
       with pytest.raises(ValueError, match="Both name and email fields are required."):
           teacher_service.create_teacher("", "jane.doe@example.com")

   def test_get_teacher(teacher_service):
       """Test retrieving a teacher by ID."""
       teacher = teacher_service.create_teacher("Jane Doe", "jane.doe@example.com")
       retrieved_teacher = teacher_service.get_teacher(teacher.id)
       assert retrieved_teacher.id == teacher.id
   ```

9. **Documentation**:
   - Update `README.md` to reflect changes in the API structure, including endpoints for creating and retrieving teachers.

## Key Considerations
- **Scalability**: Ensure the new Teacher model adopts practices that effectively allow future expansions, like adding more attributes or relationships.
- **Security**: Implement proper validation to prevent invalid or harmful user inputs.
- **Maintainability**: Adhere to coding standards outlined in the Default Project Constitution to keep the codebase organized and maintainable.

## Success Criteria
- 100% success rate for valid teacher creation requests, ensuring that valid names and emails are processed correctly.
- 100% success rate for retrieving teachers by ID, confirming that valid IDs return appropriate details.
- Successful application startup without errors, verifying the new schema and ensuring existing system functionality remains unaffected.
- All API responses delivered in valid JSON format, with appropriate HTTP status codes.

## Conclusion
This implementation plan specifies the necessary steps to create and manage a Teacher entity within the educational management system. It provides a structured approach that integrates seamlessly with existing functionalities while ensuring compliance with coding standards.

### Existing Code Modifications
Modifications to existing files:
- **New File: `src/models/teacher.py`**
  ```python
  from sqlalchemy import Column, Integer, String
  from database import Base

  class Teacher(Base):
      """Model for the Teacher entity."""
      
      __tablename__ = 'teachers'
      
      id = Column(Integer, primary_key=True, autoincrement=True)
      name = Column(String(255), nullable=False)
      email = Column(String, nullable=False)

      __mapper_args__ = {
          "order_by": id
      }
  ```

- **New File: `src/repositories/teacher_repository.py`**
  ```python
  from models.teacher import Teacher
  from database import session

  class TeacherRepository:
      """Handles database interactions for Teacher entity."""

      def create_teacher(self, name, email):
          teacher = Teacher(name=name, email=email)
          session.add(teacher)
          session.commit()
          return teacher

      def get_teacher(self, teacher_id):
          return session.query(Teacher).filter_by(id=teacher_id).first()
  ```

- **New File: `src/services/teacher_service.py`**
  ```python
  from repositories.teacher_repository import TeacherRepository
  from sqlalchemy.exc import IntegrityError

  class TeacherService:
      """Encapsulates business logic for Teacher operations."""

      def __init__(self):
          self.teacher_repo = TeacherRepository()

      def create_teacher(self, name, email):
          if not name or not email:
              raise ValueError("Both name and email fields are required.")
          if not self.validate_email(email):
              raise ValueError("Email format is invalid.")

          return self.teacher_repo.create_teacher(name, email)

      def validate_email(self, email):
          import re
          return re.match(r"[^@]+@[^@]+\.[^@]+", email) is not None

      def get_teacher(self, teacher_id):
          teacher = self.teacher_repo.get_teacher(teacher_id)
          if not teacher:
              raise ValueError("Teacher not found.")
          return teacher
  ```

- **New File: `src/api/teacher_api.py`**
  ```python
  from flask import Blueprint, request, jsonify
  from services.teacher_service import TeacherService

  teacher_api = Blueprint('teacher_api', __name__)
  teacher_service = TeacherService()

  @teacher_api.route('/api/v1/teachers', methods=['POST'])
  def create_teacher():
      data = request.json
      try:
          teacher = teacher_service.create_teacher(data['name'], data['email'])
          return jsonify({
              "id": teacher.id,
              "name": teacher.name,
              "email": teacher.email,
              "message": "Teacher has been successfully created."
          }), 201
      except ValueError as e:
          return jsonify({"error": {"code": "E001", "message": str(e)}}), 400

  @teacher_api.route('/api/v1/teachers/<int:id>', methods=['GET'])
  def get_teacher(id):
      try:
          teacher = teacher_service.get_teacher(id)
          return jsonify({
              "id": teacher.id,
              "name": teacher.name,
              "email": teacher.email
          }), 200
      except ValueError as e:
          return jsonify({"error": {"code": "E003", "message": str(e)}}), 404
  ```

- **New Tests in `tests/test_teacher.py`**
  ```python
  import pytest
  from services.teacher_service import TeacherService

  @pytest.fixture
  def teacher_service():
      return TeacherService()

  def test_create_teacher(teacher_service):
      """Test creating a new teacher."""
      teacher = teacher_service.create_teacher("Jane Doe", "jane.doe@example.com")
      assert teacher.name == "Jane Doe"
      assert teacher.email == "jane.doe@example.com"

  def test_create_teacher_missing_fields(teacher_service):
      """Test creating a teacher with missing fields raises ValueError."""
      with pytest.raises(ValueError, match="Both name and email fields are required."):
          teacher_service.create_teacher("", "jane.doe@example.com")

  def test_get_teacher(teacher_service):
      """Test retrieving a teacher by ID."""
      teacher = teacher_service.create_teacher("Jane Doe", "jane.doe@example.com")
      retrieved_teacher = teacher_service.get_teacher(teacher.id)
      assert retrieved_teacher.id == teacher.id
  ```

This implementation plan provides a comprehensive guide for integrating the Teacher entity into the existing educational management system, ensuring adherence to coding standards and fostering maintainability and scalability.