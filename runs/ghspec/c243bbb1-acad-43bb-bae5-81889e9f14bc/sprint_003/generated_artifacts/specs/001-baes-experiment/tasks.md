# Tasks: Create Course Entity

---
## INCREMENTAL DEVELOPMENT CONTEXT

**Existing Code to Build Upon**:
- `api/students.py` (1939 bytes)
- `tests/test_students.py` (3086 bytes)
- `tests/test_validation.py` (1210 bytes)

---

### Task 1: Create Database Model for Course
- **File**: `db/course.py`
- **Description**: Define the Course database model using SQLAlchemy.
- **Task**: 
  - Add the Course model with attributes: id, name, and level.
  - Ensure it inherits from the Base class.
- **Action**:
  ```python
  from sqlalchemy import Column, Integer, String
  from database import Base

  class Course(Base):
      __tablename__ = 'courses'

      id = Column(Integer, primary_key=True, autoincrement=True)
      name = Column(String, nullable=False)
      level = Column(String, nullable=False)
  ```
- [ ] Task 1: Create database model for Course.

---

### Task 2: Create Migration Script for Courses Table
- **File**: `db/migration.py`
- **Description**: Create a migration script to add the `courses` table to the database.
- **Action**:
  - Implement a script that creates the courses table without modifying existing tables.
  ```python
  from sqlalchemy import create_engine, MetaData, Table, Column, String, Integer

  engine = create_engine('sqlite:///courses.db')
  metadata = MetaData(bind=engine)

  courses_table = Table('courses', metadata,
      Column('id', Integer, primary_key=True, autoincrement=True),
      Column('name', String, nullable=False),
      Column('level', String, nullable=False)
  )

  metadata.create_all(engine)  # Creates the table
  ```
- [ ] Task 2: Create migration script for courses table.

---

### Task 3: Implement API Endpoints for Course
- **File**: `api/courses.py`
- **Description**: Define the API endpoints for creating and retrieving courses.
- **Action**:
  - Implement POST `/courses` for course creation.
  - Implement GET `/courses` for retrieving all courses.
  - Incorporate input validation using Pydantic.
- [ ] Task 3: Implement API endpoints for Course.

---

### Task 4: Create Course Service Logic
- **File**: `services/course_service.py`
- **Description**: Implement the business logic for handling course data.
- **Action**:
  - Write functions for creating courses and retrieving all courses, with necessary validation.
- [ ] Task 4: Create course service logic.

---

### Task 5: Write Unit Tests for Course Service
- **File**: `tests/test_courses.py`
- **Description**: Create unit tests for the Course service functions.
- **Action**:
  - Test for successful creation of a course.
  - Test for retrieval of all courses.
  - Validate input errors: missing name or level.
- [ ] Task 5: Write unit tests for Course service.

---

### Task 6: Write Integration Tests for API Endpoints
- **File**: `tests/test_courses_api.py` (to be created)
- **Description**: Write integration tests for the Course API endpoints.
- **Action**:
  - Test the POST `/courses` endpoint for successful and error responses.
  - Test the GET `/courses` endpoint for returning the correct course list.
- [ ] Task 6: Write integration tests for Course API endpoints.

---

### Task 7: Update Project Documentation
- **File**: `README.md`
- **Description**: Document the new Course entity and API functionality.
- **Action**:
  - Add details about the `/courses` endpoints and examples of requests and responses.
- [ ] Task 7: Update project documentation for Course functionality.

---

### Task 8: Ensure Initial Configuration Checks
- **File**: `main.py`
- **Description**: Ensure the application initializes properly with the new Course entity configuration.
- **Action**:
  - Update main application entry point to integrate the Course API and related services.
- [ ] Task 8: Ensure initial configuration checks in main application.

---

### Final Task: Run Migrations and Test All Functionality
- **File**: Entire Project
- **Description**: Run the migration script and test all implemented functionalities.
- **Action**:
  - Execute migration to create the courses table.
  - Run unit and integration tests to confirm functionality and coverage.
- [ ] Final Task: Run migrations and test all functionality.

--- 

By breaking down the implementation of the Course entity into these tasks, we ensure a structured approach that allows for incremental development, easing the testing and validation processes while adhering to the guidelines specified in the project constitution.