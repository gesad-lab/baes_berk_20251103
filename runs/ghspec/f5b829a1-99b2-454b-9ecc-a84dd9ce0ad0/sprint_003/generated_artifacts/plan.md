# Implementation Plan: Create Course Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

**Previous Sprint Plan:**  
# Implementation Plan: Add Email Field to Student Entity

---

## INCREMENTAL DEVELOPMENT CONTEXT

**Previous Sprint Plan:**  
# Implementation Plan: Student Management Web Application

## I. Architecture Overview

The Student Management Web Application will expand with the introduction of a new `Course` entity. Following the established microservice architecture, this addition will require modifications in the API layer and database layer, while maintaining the existing `Student` entity and its functionality.

## II. Technology Stack

- **Programming Language:** Python 3.11+
- **Web Framework:** FastAPI
- **Data Persistence:** SQLite
- **Data Access Library:** SQLAlchemy
- **Testing Framework:** Pytest
- **Dependency Management:** Poetry
- **Configuration Management:** Environment variables and a `.env` file

## III. Module Boundaries and Responsibilities

### 1. API Layer
- **Routes**:
  - `POST /courses`: Create a new course.
  - `GET /courses/{id}`: Retrieve a course by ID.

### 2. Service Layer
- **CourseService**: 
  - `create_course(name: str, level: str)`: Validates input and saves a new course to the database.
  - `get_course_by_id(course_id: int)`: Retrieves a course’s details from the database.

### 3. Data Layer
- **Database Configuration and Models**:
  - Create a new **Course model**:
    ```python
    class Course(Base):
        __tablename__ = 'courses'

        id = Column(Integer, primary_key=True, autoincrement=True)
        name = Column(String, nullable=False)
        level = Column(String, nullable=False)
    ```

## IV. API Contracts

### 1. Create Course Endpoint
- **Endpoint:** `POST /courses`
- **Request**: 
  ```json
  {
    "name": "Mathematics 101",
    "level": "Beginner"
  }
  ```
- **Response**:
  - **Success** (201 Created):
    ```json
    {
      "id": 1,
      "name": "Mathematics 101",
      "level": "Beginner"
    }
    ```
  - **Error** (400 Bad Request):
    ```json
    {
      "error": {
        "code": "E001",
        "message": "Name field is required."
      }
    }
    ```

### 2. Retrieve Course Endpoint
- **Endpoint:** `GET /courses/{id}`
- **Response**:
  - **Success** (200 OK):
    ```json
    {
      "id": 1,
      "name": "Mathematics 101",
      "level": "Beginner"
    }
    ```
  - **Error** (404 Not Found):
    ```json
    {
      "error": {
        "code": "E002",
        "message": "Course not found."
      }
    }
    ```

## V. Database Schema

The application will require a migration to create the `courses` table. The migration strategy includes:
1. Create a new migration file to add the `courses` table:
   ```python
   from sqlalchemy import Column, String, Integer
   from alembic import op

   def upgrade():
       op.create_table(
           'courses',
           Column('id', Integer, primary_key=True, autoincrement=True),
           Column('name', String, nullable=False),
           Column('level', String, nullable=False)
       )
   
   def downgrade():
       op.drop_table('courses')
   ```

## VI. Implementation Approach

1. **Setup Development Environment**:
   - Ensure the environment is set up with the necessary dependencies from Poetry.
   - Update the `.env` file as necessary.

2. **Modify API Endpoints**:
   - Add the `POST` route to FastAPI for creating courses.
   - Add the `GET` route to FastAPI for retrieving courses by ID.
   - Ensure correct handling of HTTP status codes and error responses for missing fields.

3. **Implement Service Logic**:
   - Create a `CourseService` class to manage business logic related to course creation and retrieval:
   ```python
   class CourseService:
       def create_course(self, name: str, level: str):
           if not name:
               raise ValueError("Name field is required.")
           if not level:
               raise ValueError("Level field is required.")
   ```

4. **Database Layer with SQLAlchemy**:
   - Create the `Course` model as shown above.
   - Implement methods in `CourseService` to interact with the database.

5. **Create Tests**:
   - Add tests in the `tests/api/test_routes.py` and `tests/services/test_course_service.py` to validate course creation and retrieval:
     - Test creating a course with valid name and level.
     - Test error handling when the name or level is missing.
     - Test retrieving an existing course by ID.
     - Test attempting to retrieve a non-existent course ID.

6. **Documentation**:
   - Update the API documentation to reflect changes in the request and response structures specific to the course entity.
   - Document all modifications within the codebase.

7. **Run Migrations**:
   - Ensure that the application starts without errors and runs the migration to create the `courses` table.

## VII. Security & Error Handling

- **Input Validation**: Validate `name` and `level` formats (consider length and allowed characters).
- **Error Messages**: Define structured error responses for both missing name and level fields without revealing internal structure.

## VIII. Testing Strategies

- Implement unit tests for the `CourseService` class to cover:
  - Valid course creation.
  - Handling missing name and level inputs.
  - Successful retrieval of course data.
- Implement integration tests to validate the API behavior and responses.

## IX. Monitoring & Logging

- Implement structured logging with requests and error details in JSON format to track API usage patterns and issues.
- Establish basic monitoring for application health checks, ensuring the API is responsive.

## X. Success Criteria

1. The application must successfully respond to valid requests for creating and retrieving courses.
2. It must handle errors gracefully and return meaningful messages for missing inputs.
3. The implementation should maintain backward compatibility and be easy to manage for future changes.

## Existing Code Files Modifications

- **`src/models.py`:** Create a new `Course` model as outlined in the implementation plan.
- **`src/services/course_service.py`:** Create a new `CourseService` class to encapsulate business logic for courses.
- **`src/main.py`:** Add routes for `POST /courses` and `GET /courses/{id}` for creating and retrieving courses.
- **`tests/api/test_routes.py`:** Add tests for course creation and retrieval.
- **`tests/services/test_course_service.py`:** Create a new test module to validate `CourseService` functionality.

By following this implementation plan, we can ensure a successful integration of the new Course entity while adhering to our established coding standards and policies.