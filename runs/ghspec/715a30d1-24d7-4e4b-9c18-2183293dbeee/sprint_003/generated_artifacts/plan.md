# Implementation Plan: Create Course Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Add Email Field to Student Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Student Entity Web Application

## I. Overview & Purpose

This implementation plan introduces a new Course entity to the existing Student Entity Web Application. The Course entity enables users to categorize and manage educational courses effectively. By implementing this feature, we enhance the application's capability in handling educational data, improving data organization and accessibility. 

## II. Architecture & Technology Stack

- **Backend Framework**: FastAPI (for building RESTful APIs).
- **Database**: SQLite (embedded, lightweight database for development).
- **ORM**: SQLAlchemy (for handling database interactions and schema definitions).
- **Dependencies**:
  - FastAPI
  - SQLAlchemy
  - uvicorn (for running the FastAPI application)
- **Environment**: Python 3.11+ 

### Architecture Diagram

```
+--------------------------------------------------------+
|                      FastAPI Application                |
|                                                        |
| +--------------------+    +-----------------------+   |
| | Course Controller   | <->| Course Service        |   |
| +--------------------+    +-----------------------+   |
| | - create_course()   |    | - add_course()       |   |
| | - get_course()      |<-->| - find_course()      |   |
| +--------------------+    +-----------------------+   |
|                                                        |
| +--------------------+                                 |
| | Course Repository   |                                |
| +--------------------+                                 |
| | - save()           |                                 |
| | - get_by_id()      |                                |
| +--------------------+                                 |
|                                                        |
+--------------------------------------------------------+
|                         SQLite Database                 |
|                      +------------------+              |
|                      |     courses       |              |
|                      +------------------+              |
|                      | id (pk)          |              |
|                      | name (required)  |              |
|                      | level (required) |              |
|                      +------------------+              |
+--------------------------------------------------------+
```

## III. Module Boundaries & Responsibilities

1. **Course Controller**: 
   - Exposes API endpoints for creating and retrieving course records.
   - Validates incoming requests and translates them into service calls.

2. **Course Service**: 
   - Contains business logic related to course management.
   - Interacts with the repository to persist and retrieve course data.

3. **Course Repository**: 
   - Responsible for directly accessing the database.
   - Encapsulates CRUD operations related to the `courses` table.

## IV. Data Model

### Course Entity

```python
class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    level = Column(String, nullable=False)
```

### API Contracts

**POST /courses**
- **Request Body**:
    ```json
    {
        "name": "string",
        "level": "string"
    }
    ```
- **Response (201 Created)**:
    ```json
    {
        "id": 1,
        "name": "string",
        "level": "string"
    }
    ```
- **Error Response (400 Bad Request)**:
    ```json
    {
        "error": {
            "code": "E001",
            "message": "Name and level are required."
        }
    }
    ```

**GET /courses/{id}**
- **Response (200 OK)**:
    ```json
    {
        "id": 1,
        "name": "string",
        "level": "string"
    }
    ```
- **Error Response (404 Not Found)**:
    ```json
    {
        "error": {
            "code": "E002",
            "message": "Course not found."
        }
    }
    ```

## V. Implementation Approach

1. **Set Up the FastAPI Application**:
   - Extend the existing Python project, ensuring the current virtual environment is activated.
   - Install/update required dependencies: FastAPI, SQLAlchemy, uvicorn (if not already included).

2. **Define Database Models**:
   - Create a new `models.py` file (or update existing if implemented already) to include the `Course` ORM model definition.

3. **Database Migration Strategy**:
   - Create a new migration script using Alembic for the `courses` table creation.
   - Example migration command:
     ```bash
     alembic revision --autogenerate -m "Create courses table"
     ```

4. **Implement Repository Layer**:
   - Create a new `repository.py` file (or update existing if present) to accommodate the new `Course` entity in the repository layer for CRUD operations.

5. **Implement Service Layer**:
   - Create a new `service.py` file (or update existing if present) to enforce the business logic for creating and fetching courses.

6. **Implement API Routes**:
   - Create a new `main.py` file (or update existing if built) to define API routes for course creation and retrieval, utilizing FastAPI decorators.

7. **Input Validation**:
   - Use Pydantic models to define request body schemas and validate required fields for course creation.

8. **Error Handling**:
   - Implement error handling mechanisms to provide clear feedback for invalid inputs.

9. **Testing**:
   - Write unit tests for the repository, service, and controller layers to verify functionality associated with the Course entity, ensuring at least 70% coverage.

## VI. Deployment Considerations

- The application should continue to run locally with the addition of the new Course entity.
- Document the setup process and required configuration changes in the `README.md` file.
- Ensure logging captures any errors related to the new functionality.
- Maintain graceful shutdown of the application by handling shutdown signals.

## VII. Security & Best Practices

- **Validation**: Use Pydantic to validate course name and level inputs.
- **Error Messages**: Design clear, actionable error responses for missing name or level inputs.
- **Environment**: Continue using environment variables for sensitive configuration.
- **Logging**: Implement structured logging to facilitate easier debugging for any issues that may arise from the creation of the Course entity.

## VIII. Trade-offs and Considerations

- **Database Migration Complexity**: As this is a new feature with no existing Course data, migration complexity should be low.
- **No Frontend Adjustments**: This implementation focuses solely on backend API management for the Course entity.

## IX. Success Criteria

- All functional requirements outlined in the specification are met.
- Users should be able to create a course record with a name and level, and retrieve course records accurately reflecting these attributes.
- The application should return structured error responses when necessary validations fail.
- The database schema should be updated to include the new `courses` table during application startup with no errors.

## X. Conclusion

This implementation plan is designed to effectively introduce the Course entity into the existing Student Entity Web Application while maintaining backward compatibility. By following this structured approach, the application will continue to align with user needs and adhere to coding standards and best practices.

## Modifications Needed in Existing Files

### 1. `models.py`
- Create a new `Course` class definition:
```python
class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    level = Column(String, nullable=False)
```

### 2. `repository.py`
- Create a new repository for managing courses:
```python
class CourseRepository:
    def save(self, course: Course):
        # Logic to add course to the database
       
    def get_by_id(self, id: int):
        # Logic to fetch the course by ID
```

### 3. `service.py`
- Create a new service for courses:
```python
class CourseService:
    def add_course(self, course_data: dict):
        # Validate and save the new course
       
    def find_course(self, id: int):
        # Logic to retrieve course details
```

### 4. `main.py`
- Create a new API route for courses:
```python
@app.post("/courses", response_model=Course)
def create_course(course: CourseCreate):
    # Call service to create a new course

@app.get("/courses/{id}", response_model=Course)
def get_course(id: int):
    # Call service to retrieve course details
```

### 5. Migration Script (new)
- Create migration file to add the `courses` table:
```python
def upgrade():
    op.create_table(
        'courses',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String, nullable=False),
        sa.Column('level', sa.String, nullable=False)
    )
```

By implementing these changes, the Course functionality will be clearly defined and integrated into the existing application infrastructure effectively.