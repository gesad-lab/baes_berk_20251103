# Implementation Plan: Add Course Relationship to Student Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Create Course Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

# Implementation Plan: Student Entity Management Web Application

## I. Overview

This implementation plan outlines the architecture, technical stack, module boundaries, data models, API contracts, and implementation approach for establishing a relationship between the `Student` and `Course` entities in the existing educational data management system. This feature will allow each Student to enroll in one or more Courses and provide enhanced tracking of student enrollments.

## II. Architecture

### 1. System Architecture

- **Architecture Style**: RESTful API
- **Components**:
  - **Web Server**: Handles HTTP requests and responses.
  - **Database**: SQLite database to persist student enrollment data alongside existing entities.
  - **Business Logic Layer**: Processes requests related to student enrollments, validates input, and interacts with the database.

### 2. Technology Stack

- **Programming Language**: Python
- **Framework**: Flask (for creating RESTful API)
- **Database**: SQLite (lightweight, serverless database suitable for this application)
- **ORM**: SQLAlchemy (to facilitate database interactions)
- **Testing Framework**: pytest (for unit and integration tests)
- **Dependency Management**: Poetry (for managing project dependencies)

## III. Module Boundaries and Responsibilities

### 1. Modules

- **Routing Module**: Handles incoming HTTP requests and maps endpoints for student enrollment to appropriate functions.
- **Controller Module**: Contains functions that process enrollment requests, validate input, and return responses.
- **Model Module**: Extends the existing `Student` model to incorporate a list of `enrolled_courses`.
- **Validation Module**: Contains logic for validating enrollment data.

### 2. Responsibilities

- **Routing Module**: Defines the API routes (`/students/{student_id}/enroll`, `/students/{student_id}/courses`) and links them to controller functions.
- **Controller Module**: Contains methods for:
  - Enrolling a student in a course.
  - Retrieving a student's enrolled courses.
- **Model Module**: Manages the SQLite database, updating the `Student` schema to have a relationship with the `Course` entity.
- **Validation Module**: Validates the incoming requests for course enrollment.

## IV. Data Models and API Contracts

### 1. Data Model

Extend the existing `Student` model to include an `enrolled_courses` attribute which is a list of course IDs. Update `src/models.py`:

```python
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    enrolled_courses = relationship('Course', secondary='enrollments')

class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    level = Column(String, nullable=False)

# Association table for many-to-many relationship
enrollments = Table('enrollments', Base.metadata,
    Column('student_id', Integer, ForeignKey('students.id'), primary_key=True),
    Column('course_id', Integer, ForeignKey('courses.id'), primary_key=True)
)
```

### 2. API Contracts

#### Enroll Student in Course
- **Endpoint**: `POST /students/{student_id}/enroll`
- **Request Body**: 
  ```json
  {
      "course_id": integer  // required
  }
  ```
- **Responses**:
  - **201 Created**:
    ```json
    {
        "message": "Enrollment successful.",
        "student_id": 1,
        "course_id": 2
    }
    ```
  - **400 Bad Request**:
    ```json
    {
        "error": {
            "code": "E001",
            "message": "Course not found.",
            "details": {}
        }
    }
    ```

#### Retrieve Student's Enrolled Courses
- **Endpoint**: `GET /students/{student_id}/courses`
- **Responses**:
  - **200 OK**:
    ```json
    [
        {
            "id": 2,
            "name": "Introduction to Programming",
            "level": "Beginner"
        },
        {
            "id": 3,
            "name": "Advanced Mathematics",
            "level": "Advanced"
        }
    ]
    ```
  - **404 Not Found**:
    ```json
    {
        "error": {
            "code": "E002",
            "message": "Student not found.",
            "details": {}
        }
    }
    ```

## V. Implementation Approach

### 1. Setup Environment
- Create a virtual environment for the project using Poetry.
- Install Flask, SQLAlchemy, and pytest as dependencies.

### 2. Development Steps

1. **Database Migration**:
   - Use Alembic to implement migrations for adding the association table `enrollments`.
   Create a migration script in the migrations folder:
   ```python
   def upgrade():
       op.create_table('enrollments',
           sa.Column('student_id', sa.Integer(), nullable=False),
           sa.Column('course_id', sa.Integer(), nullable=False),
           sa.ForeignKeyConstraint(['student_id'], ['students.id'], ),
           sa.ForeignKeyConstraint(['course_id'], ['courses.id'], ),
           sa.PrimaryKeyConstraint('student_id', 'course_id')
       )

   def downgrade():
       op.drop_table('enrollments')
   ```

2. **Initialize Flask Application**:
   - Set up a simple Flask app structure with a main application file (e.g., `app.py`).
  
3. **Implement API Routes**:
   - Set up routes for enrolling students and retrieving their courses in the routing module (`src/routes.py`).

4. **Create Controllers**:
   - Implement logic in the controller module (`src/controllers.py`) to handle incoming requests for student enrollment and retrieval.

5. **Validation Logic**:
   - Update the validation module (`src/validation.py`) to include checks for the existence of course IDs before enrollment.

6. **Testing**:
   - Write unit tests and integration tests using pytest to cover the functionalities for both enrolling students and retrieving courses, ensuring validation error handling.

## VI. Testing Approach

### 1. Test Coverage
- Aim for a minimum of 70% test coverage for business logic between both functionalities.
- Ensure critical paths (enrolling students and retrieving courses) achieve 90%+ coverage.

### 2. Test Cases
- Test cases for enrolling a student with valid and invalid data, including:
  - Successful enrollment of a student in an existing course.
  - Attempting to enroll a student in a non-existing course.
- Test case for retrieving a student's enrolled courses, ensuring both successful responses and error scenarios.

## VII. Deployment Considerations

### 1. Production Readiness
- Ensure automatic database migrations are applied on application startup.
- Include a health check endpoint to assure application status.

### 2. Configuration Management
- Use environment variables for any configuration settings related to the database.
- Provide a sample `.env.example` file to outline expected configurations.

## VIII. Conclusion

This implementation plan describes the steps required to add a relationship between `Student` and `Course` entities to the existing Student Entity Management Web Application. Following this structured approach will enhance the application's data management capabilities while ensuring compliance with RESTful principles, maintainability, and scalability.

### Modifications Needed to Existing Files
1. **Model Update**: Extend the `Student` model in `src/models.py` to include the `enrolled_courses` relationship.
2. **Migration Script**: Create a new migration script in the migrations folder for the `enrollments` association table.
3. **API Routes**: Update `src/routes.py` to include endpoints for enrolling students and retrieving courses.
4. **Controller Logic**: Implement new controller functions in `src/controllers.py` for handling enrollments and course retrieval.
5. **Validation Logic**: Update the validation module in `src/validation.py` to ensure incoming requests verify course existence.
6. **Testing**: Create new test files in `tests/test_student_courses.py` for validating the new course enrollment features.

By following these steps, we ensure the existing codebase is extended to incorporate enhanced management of Student enrollments while maintaining backward compatibility with existing data models.