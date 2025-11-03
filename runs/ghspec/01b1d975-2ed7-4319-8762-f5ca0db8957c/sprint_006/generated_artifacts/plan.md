# Implementation Plan: Add Teacher Relationship to Course Entity

---

INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
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

# Implementation Plan: Student Entity Management Web Application

## I. Overview

This implementation plan outlines the architecture, technical stack, module boundaries, data models, API contracts, and implementation approach for establishing a relationship between the `Course` and `Teacher` entities in the existing educational data management system. This feature will enable assigning, updating, and retrieving Teacher information for each Course, enhancing functionalities related to course assignments and teacher responsibilities.

## II. Architecture

### 1. System Architecture

- **Architecture Style**: RESTful API
- **Components**:
  - **Web Server**: Handles HTTP requests and responses.
  - **Database**: SQLite database to persist Course and Teacher data.
  - **Business Logic Layer**: Processes requests related to Course and Teacher management, validates input, and interacts with the database.

### 2. Technology Stack

- **Programming Language**: Python
- **Framework**: Flask (for creating RESTful API)
- **Database**: SQLite (lightweight, serverless database suitable for this application)
- **ORM**: SQLAlchemy (to facilitate database interactions)
- **Testing Framework**: pytest (for unit and integration tests)
- **Dependency Management**: Poetry (for managing project dependencies)

## III. Module Boundaries and Responsibilities

### 1. Modules

- **Routing Module**: Handles incoming HTTP requests and maps endpoints for Course-Teacher relationship.
- **Controller Module**: Contains functions that process requests to assign/update a Teacher to a Course and retrieve Course details.
- **Model Module**: Defines the updated `Course` model with a relation to `Teacher`, and interacts with the database.
- **Validation Module**: Contains logic for validating Teacher assignment requests.

### 2. Responsibilities

- **Routing Module**: Define API routes related to teacher assignments on courses.
- **Controller Module**: Contains methods for:
  - Assigning a teacher to a specific course.
  - Retrieving course details, including teacher information.
  - Updating the teacher assignment for a course.
- **Model Module**: Maintains the Course model with the foreign key relationship to the Teacher model.
- **Validation Module**: Validates assignments of Teachers to ensure the correctness of data.

## IV. Data Models and API Contracts

### 1. Data Model

Update the existing `Course` model in `src/models.py` to include a foreign key referencing the Teacher:

```python
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Course(Base):
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    level = Column(String, nullable=False)
    teacher_id = Column(Integer, ForeignKey('teachers.id'), nullable=True)
    
    teacher = relationship("Teacher", back_populates="courses")

class Teacher(Base):
    __tablename__ = 'teachers'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)

    courses = relationship("Course", back_populates="teacher")
```

### 2. API Contracts

#### Assign Teacher to Course
- **Endpoint**: `POST /courses/{course_id}/assign_teacher`
- **Request Body**: 
  ```json
  {
      "teacher_id": 1  // required
  }
  ```
- **Responses**:
  - **200 OK**:
    ```json
    {
        "message": "Teacher assigned successfully."
    }
    ```
  - **404 Not Found**:
    ```json
    {
        "error": {
            "code": "E001",
            "message": "Course or Teacher not found."
        }
    }
    ```

#### Retrieve Course Details
- **Endpoint**: `GET /courses/{course_id}`
- **Responses**:
  - **200 OK**:
    ```json
    {
        "id": 1,
        "name": "Mathematics",
        "level": "101",
        "teacher": {
            "name": "John Doe",
            "email": "john.doe@example.com"
        }
    }
    ```
  - **404 Not Found**:
    ```json
    {
        "error": {
            "code": "E002",
            "message": "Course not found."
        }
    }
    ```

#### Update Teacher Assignment
- **Endpoint**: `PUT /courses/{course_id}/assign_teacher`
- **Request Body**: 
  ```json
  {
      "teacher_id": 1  // required
  }
  ```
- **Responses**:
  - **200 OK**:
    ```json
    {
        "message": "Teacher assignment updated successfully."
    }
    ```
  - **404 Not Found**:
    ```json
    {
        "error": {
            "code": "E001",
            "message": "Course or Teacher not found."
        }
    }
    ```

## V. Implementation Approach

### 1. Setup Environment
- Create a virtual environment for the project using Poetry.
- Install Flask, SQLAlchemy, and pytest as dependencies.

### 2. Development Steps

1. **Database Migration**:
   - Utilize Alembic to implement the migration for updating the `courses` table with a new foreign key `teacher_id`.
   Create a migration script in the migrations folder:
   ```python
   def upgrade():
       op.add_column('courses', sa.Column('teacher_id', sa.Integer(), sa.ForeignKey('teachers.id'), nullable=True))

   def downgrade():
       op.drop_column('courses', 'teacher_id')
   ```

2. **Initialize Flask Application**:
   - Set up a simple Flask app structure with a main application file (e.g., `app.py`).

3. **Implement API Routes**:
   - Set up routes for assigning teachers and retrieving course details in the routing module (`src/routes.py`).

4. **Create Controllers**:
   - Implement the logic in the controller module (`src/controllers.py`) to handle the assignment and retrieval of Teachers for Courses.

5. **Validation Logic**:
   - Update the validation module (`src/validation.py`) to ensure that the teacher exists prior to assignment, and that the course exists before performing operations on it.

6. **Testing**:
   - Write unit tests and integration tests using pytest to cover functionalities for assigning teachers to courses and retrieving course details.

## VI. Testing Approach

### 1. Test Coverage
- Aim for a minimum of 70% test coverage for business logic surrounding Teacher-Course management.
- Ensure critical paths (assigning and retrieving Teachers for Courses) achieve 90%+ coverage.

### 2. Test Cases
- Test cases for assigning a Teacher with valid and invalid data, including:
  - Successful assignment of a teacher to a course.
  - Validation error when either course or teacher is invalid or does not exist.
- Test case for retrieving a Course's details, ensuring both successful responses and error scenarios.

## VII. Deployment Considerations

### 1. Production Readiness
- Ensure automatic database migrations are applied on application startup.
- Include a health check endpoint to assure application status.

### 2. Configuration Management
- Use environment variables for database configuration settings.
- Provide a sample `.env.example` file outlining the expected environment configurations.

## VIII. Conclusion

This implementation plan describes the steps required to establish a relationship between the `Course` and `Teacher` entities in the existing Student Entity Management Web Application. Following this structured approach will enhance the application's data management capabilities while ensuring compliance with RESTful principles, maintainability, and scalability.

### Modifications Needed to Existing Files

1. **Model Update**: Update `src/models.py` to include the `teacher_id` foreign key in the `Course` model.
2. **Migration Script**: Create a new migration script in the migrations folder to add the `teacher_id`.
3. **API Routes**: Implement new endpoints in `src/routes.py` for assigning teachers to courses and retrieving course details.
4. **Controller Logic**: Create new controller functions in `src/controllers.py` for handling Teacher assignment and retrieval.
5. **Validation Logic**: Update `src/validation.py` to verify the existence of both Course and Teacher before processing requests.
6. **Testing**: Create new test files in `tests/test_course_teacher.py` to validate the functionalities associated with the Teacher-Course relationship.

By following these steps, we ensure the existing codebase is extended to introduce the Teacher-Course relationship while maintaining backward compatibility with existing data models.