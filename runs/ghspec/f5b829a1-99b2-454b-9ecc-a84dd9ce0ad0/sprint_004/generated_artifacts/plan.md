# Implementation Plan: Add Course Relationship to Student Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

**Previous Sprint Plan:**  
# Implementation Plan: Create Course Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

**Previous Sprint Plan:**  
# Implementation Plan: Add Email Field to Student Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

**Previous Sprint Plan:**  
# Implementation Plan: Student Management Web Application

## I. Architecture Overview

The existing Student Management Web Application architecture will be expanded to include a many-to-many relationship between the `Student` and `Course` entities, facilitated by an `Enrollment` bridge table. This will require updates to the API layer and database schema while maintaining existing functionalities for the `Student` entity.

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
  - `POST /students/{studentId}/enroll`: Enroll a student in a course.
  - `GET /students/{studentId}/courses`: Retrieve all courses for a specific student.

### 2. Service Layer
- **EnrollmentService**: 
  - `enroll_student(student_id: int, course_id: int)`: Validates input and creates an enrollment record.
  - `get_courses_for_student(student_id: int)`: Retrieves all courses associated with a specific student.

### 3. Data Layer
- **Database Configuration and Models**:
  - Create an **Enrollment model**:
    ```python
    class Enrollment(Base):
        __tablename__ = 'student_courses'

        student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
        course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)
    ```

## IV. API Contracts

### 1. Enroll Student in Course Endpoint
- **Endpoint:** `POST /students/{studentId}/enroll`
- **Request**:
  ```json
  {
    "courseId": 1
  }
  ```
- **Response**:
  - **Success** (201 Created):
    ```json
    {
      "studentId": 1,
      "courseId": 1
    }
    ```
  - **Error** (404 Not Found):
    ```json
    {
      "error": {
        "code": "E001",
        "message": "Student not found."
      }
    }
    ```

### 2. Retrieve Student Courses Endpoint
- **Endpoint:** `GET /students/{studentId}/courses`
- **Response**:
  - **Success** (200 OK):
    ```json
    {
      "courses": [
        {"id": 1, "name": "Mathematics 101", "level": "Beginner"},
        {"id": 2, "name": "Science 101", "level": "Intermediate"}
      ]
    }
    ```
  - **Error** (404 Not Found):
    ```json
    {
      "error": {
        "code": "E002",
        "message": "Student not found."
      }
    }
    ```

## V. Database Schema

### Migration Strategy
We will create a migration to establish a many-to-many relationship between the Student and Course tables through an Enrollment bridge table, ensuring the existing data remains intact.

1. Create a migration file to add the `student_courses` table:
   ```python
   from sqlalchemy import Column, Integer, ForeignKey
   from alembic import op

   def upgrade():
       op.create_table(
           'student_courses',
           Column('student_id', Integer, ForeignKey('students.id'), primary_key=True),
           Column('course_id', Integer, ForeignKey('courses.id'), primary_key=True)
       )
   
   def downgrade():
       op.drop_table('student_courses')
   ```

## VI. Implementation Approach

1. **Setup Development Environment**:
   - Ensure the environment is set up with dependencies installed via Poetry.
   - Update the `.env` file as necessary.

2. **Modify API Endpoints**:
   - Add the `POST /students/{studentId}/enroll` route to FastAPI.
   - Add the `GET /students/{studentId}/courses` route to FastAPI.
   - Implement appropriate handling for HTTP status codes and error responses for both enrollment and course retrieval.

3. **Implement Service Logic**:
   - Create an `EnrollmentService` class with the following methods:
   ```python
   class EnrollmentService:
       def enroll_student(self, student_id: int, course_id: int):
           # logic to check and create an enrollment
           # raise appropriate exceptions if the student or course is not found

       def get_courses_for_student(self, student_id: int):
           # logic to retrieve enrolled courses for a student
   ```

4. **Database Layer with SQLAlchemy**:
   - Create the `Enrollment` model as per the outlined structure.
   - Implement methods in `EnrollmentService` to interact with the `student_courses` table.

5. **Create Tests**:
   - Add tests to `tests/api/test_routes.py` for new API endpoints:
     - Validate successful enrollment.
     - Validate retrieval of courses for a student.
     - Validate error handling for non-existent student and course IDs.
   - Add tests in `tests/services/test_enrollment_service.py` to cover the business logic for enrollments.

6. **Documentation**:
   - Update the API documentation according to the new request and response structures.
   - Ensure all modifications are documented within the codebase.

7. **Run Migrations**:
   - Ensure that the application runs without errors and executes the migration to create the `student_courses` table.

## VII. Security & Error Handling

- **Input Validation**: Validate student and course IDs against existing records.
- **Structured Error Responses**: Define clear error formats for invalid requests, following the established pattern for API responses.

## VIII. Testing Strategies

- Implement unit tests for the `EnrollmentService` to cover:
  - Successful enrollment process.
  - Error handling for invalid student or course IDs.
  - Successful retrieval of course data for a student.
- Implement integration tests to validate the API responses meet the defined specifications.

## IX. Monitoring & Logging

- Utilize structured logging to capture request and error details, aiding troubleshooting and monitoring.
- Implement health check endpoints to monitor API availability.

## X. Success Criteria

1. Students must be able to enroll in courses via the API successfully.
2. Students should be able to retrieve a list of courses they are enrolled in.
3. Appropriate error messages must be returned when invalid student or course IDs are used.
4. The implementation must adhere to established JSON formats in all responses.
5. Existing data in the Student and Course tables remains unaffected post-migration.

## Existing Code Files Modifications

- **`src/main.py`:** Add routes for `POST /students/{studentId}/enroll` and `GET /students/{studentId}/courses`.
- **`src/models.py`:** Create a new `Enrollment` model for the bridge table.
- **`src/services/enrollment_service.py`:** Implement the `EnrollmentService` to handle enrollment logic.
- **`tests/api/test_routes.py`:** Add tests for enrolling students and retrieving courses.
- **`tests/services/test_enrollment_service.py`:** Create a new test file to validate `EnrollmentService` functionality.

By following this implementation plan, we can ensure the successful integration of the new course enrollment functionality while maintaining coding standards and existing application architecture.