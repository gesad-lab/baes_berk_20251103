# Implementation Plan: Create Course Entity

---
## INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Add Email Field to Student Entity

---
## Version
1.0.0

## Overview
This implementation plan outlines the steps required to introduce a new Course entity into the existing educational management system. By allowing educational institutions to define courses with specific attributes such as course name and level, we aim to enhance the overall functionality of the system, thereby improving course management and organization.

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
The application will continue with a monolithic architecture. The new Course entity will be integrated as follows:

1. **API Layer**: 
   - Handles HTTP requests and routes them to the course service for creating, fetching, and listing courses.

2. **Service Layer**: 
   - Contains business logic for managing Course records.

3. **Data Access Layer**: 
   - Responsible for database interactions using SQLAlchemy ORM and managing Course records.

4. **Database**: 
   - SQLite will be used for data storage, with an updated schema to include the new Course table.

## Module Responsibilities
### 1. API Module (`api.py`)
- New routes to handle Course-related operations:
  - `POST /api/v1/courses`: Create a new course record with required fields "name" and "level".
  - `GET /api/v1/courses/<id>`: Retrieve a course by ID, returning its name and level.
  - `GET /api/v1/courses`: List all course records, returning names and levels.

### 2. Service Module (`services/course_service.py`)
- Define functions to:
  - Create a course record with validation for name and level.
  - Fetch a course record by its ID.
  - List all course records.

### 3. Data Model (`models/course.py`)
- Define a new Course class with the following attributes:
  - `id`: Integer (Primary Key, auto-increment)
  - `name`: String (Required)
  - `level`: String (Required)

### 4. Database Access (`data_access/course_repository.py`)
- Define methods for:
  - Saving a new course.
  - Finding courses by ID.
  - Retrieving all courses.

## Data Models and API Contracts
### Data Models
```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Base class for SQLAlchemy models
Base = declarative_base()

class Course(Base):
    """
    Represents a course entity in the database.

    Attributes:
        id (int): The unique identifier for the course (Primary Key).
        name (str): The name of the course (Required).
        level (str): The level of the course (Required).
    """
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    level = Column(String, nullable=False)
```

### API Contract
#### Create Course
- **Endpoint**: `POST /api/v1/courses`
- **Request Body**:
  ```json
  {
      "name": "Mathematics 101",
      "level": "Beginner"
  }
  ```
- **Response**:
  - **Status**: 201 Created
  - **Body**:
  ```json
  {
      "id": 1,
      "name": "Mathematics 101",
      "level": "Beginner"
  }
  ```

#### Get Course by ID
- **Endpoint**: `GET /api/v1/courses/<id>`
- **Response**:
  - **Status**: 200 OK
  - **Body**:
  ```json
  {
      "id": 1,
      "name": "Mathematics 101",
      "level": "Beginner"
  }
  ```

#### List All Courses
- **Endpoint**: `GET /api/v1/courses`
- **Response**:
  - **Status**: 200 OK
  - **Body**:
  ```json
  [
      {
          "id": 1,
          "name": "Mathematics 101",
          "level": "Beginner"
      }
  ]
  ```

## Implementation Approach
1. **Project Setup**:
   - Use the existing Git repository for the project. Ensure the `requirements.txt` reflects any new dependencies.
   - Ensure the virtual environment is activated and dependencies are installed.

2. **Define Data Model**:
   - Create the `Course` model in `models/course.py`.

3. **Implement Database Migration**:
   - Create a migration script to add the `courses` table. This should be safe for existing `students` data.

   Example Migration Script:
   ```python
   from flask_migrate import Migrate, MigrateCommand
   from flask_script import Manager
   from models import db, Course

   # Initialize migration
   migrate = Migrate(app, db)
   manager = Manager(app)
   manager.add_command('db', MigrateCommand)

   # Create tables
   def upgrade():
       db.create_all()

   def downgrade():
       db.drop_all()
   ```

4. **Create Service Layer**:
   - Implement functionality in `services/course_service.py` to create, fetch, and list courses including validation.

5. **Build API Layer**:
   - Update `api.py` routes to include endpoints for creating and retrieving courses.

6. **Testing**:
   - Write unit tests for course creation, retrieval, and listing functionalities.
   - Ensure coverage for the new service layer and API routes.

7. **Documentation**:
   - Update the `README.md` to describe the new Course entity, endpoints, and usage.

8. **Error Handling**:
   - Implement input validation for course name and level to ensure they are valid strings and not empty.

## Scalability Considerations
- The architecture remains stateless, allowing the application to scale horizontally if needed.
- Well-defined endpoints allow for future enhancements, maybe supporting more attributes for courses later on.

## Security Considerations
- Implement strict input validation to prevent issues like XSS or SQL injection.
- Ensure proper error handling to avoid exposing sensitive information through error messages.

## Deployment Considerations
- Ensure all dependencies are well documented in the `requirements.txt`.
- Include environment variables for configuration settings related to the database.

## Testing Strategy
- **Unit Tests**: Validate functionalities regarding the Course entity.
- **Integration Tests**: Confirm that API endpoints handle Course data correctly.
- **Contract Tests**: Ensure responses adhere to defined specifications.

## Success Metrics
- Successful creation of course records, returning confirmation with names and levels.
- Accurate retrieval of course records by ID.
- Correct listing of all course records with names and levels in JSON format.
- Migration executed successfully without data loss or disruption to existing functionalities.

## Conclusion
This implementation plan lays out a structured approach to adding the Course entity to the educational management system, ensuring compatibility with existing features while enhancing functionality. Defining clear API contracts and enforcing security will help in maintaining the integrity and reliability of the application.

Existing Code Files:
File: `tests/test_api.py`
```python
# Ensure to include tests for the following new routes:
# - POST /api/v1/courses
# - GET /api/v1/courses/<id>
# - GET /api/v1/courses
```

File: `tests/test_course_service.py`
```python
import pytest
from services.course_service import CourseService

def test_create_course():
    # Test for creating a course
    pass

def test_get_course_by_id():
    # Test retrieving a course by ID
    pass

def test_list_all_courses():
    # Test listing all courses
    pass
``` 

Through following this plan, the integration of the Course entity will provide significant enhancements to the educational management system, improving course organization and management for users.