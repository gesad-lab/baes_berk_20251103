# Tasks: Create Course Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- `tests/test_routes.py` (2797 bytes)
- `tests/test_services.py` (2042 bytes)

---

## Task Breakdown

### 1. Update Data Models
- [ ] **Task**: Define the new `Course` entity in the data models.
  - **File**: `src/models/models.py`  
  **Description**: Update the existing models.py to include the new Course class with fields for `id`, `name`, and `level`.
    ```python
    from sqlalchemy import Column, Integer, String
    from sqlalchemy.ext.declarative import declarative_base

    Base = declarative_base()

    class Course(Base):
        __tablename__ = 'courses'
        id = Column(Integer, primary_key=True, autoincrement=True)
        name = Column(String, nullable=False)
        level = Column(String, nullable=False)  # New field
    ```

### 2. Database Migration Strategy
- [ ] **Task**: Create a migration script for the Course table.
  - **File**: Run Alembic command  
  **Description**: Generate the migration script to create the Course table without affecting existing Student records by running the following command in terminal:
    ```bash
    alembic revision --autogenerate -m "Add Course table"
    ```

### 3. Implement Services Logic
- [ ] **Task**: Implement course creation and retrieval logic.
  - **File**: `src/services/course_service.py`  
  **Description**: Create a new service file and define functions for `create_course()` and `get_course()`.
    ```python
    def create_course(name: str, level: str):
        # Logic to handle course creation
    ```

### 4. Define API Endpoints
- [ ] **Task**: Add new API endpoints for Course management.
  - **File**: `src/api/routes.py`  
  **Description**: Update the routes.py to include the POST `/courses` and GET `/courses/{id}` endpoints.
    ```python
    @router.post("/courses")
    async def create_course(course: CourseCreate):
        # Handler to create course
    ```

### 5. Implement Input Validation
- [ ] **Task**: Validate incoming requests with Pydantic.
  - **File**: `src/api/routes.py`  
  **Description**: Create a Pydantic model to validate `name` and `level` fields for the course creation request.
    ```python
    from pydantic import BaseModel

    class CourseCreate(BaseModel):
        name: str
        level: str
    ```

### 6. Error Handling
- [ ] **Task**: Implement error responses for invalid inputs.
  - **File**: `src/api/routes.py`  
  **Description**: Add logic to return clear error messages for missing fields or invalid inputs in the course creation process.

### 7. Testing New Features
- [ ] **Task**: Write tests for Course API endpoints.
  - **File**: `tests/test_course.py`  
  **Description**: Create a new test file to include tests for creating and retrieving courses, including error scenarios.
    ```python
    def test_create_course_without_level(client):
        response = client.post("/courses", json={"name": "Mathematics"})
        assert response.status_code == 422  # Unprocessable Entity
    ```

### 8. Documentation
- [ ] **Task**: Update the README with the new Course API usage.
  - **File**: `README.md`  
  **Description**: Include instructions and examples of how to use the new course API endpoints, ensuring alignment with existing documentation style.

---

This task breakdown adheres to the specifications outlined and allows for independent testing of each new implementation step. Each task is isolated, ensuring a manageable and understandable approach to integrating the Course entity into the application.