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
INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Student Entity Web Application

## I. Project Overview

This implementation plan outlines the requirements necessary to create a relationship between the Student and Course entities within the existing Student Entity Web Application. The goal is to enable students to be associated with one or more courses, enhancing academic management capabilities and engagement tracking. This plan includes changes to the architecture, technology stack, module design, database schema, API contract updates, and other technical considerations.

## II. Architecture

The existing application architecture will be expanded to accommodate the Course relationship with Student. The key components include:
- **API Layer**: New endpoints for managing Student-Course relationships.
- **Service Layer**: Includes business logic for validating and managing the relationship between Students and Courses.
- **Data Access Layer**: Interacts with the database for operations related to the Student-Course relationship.
- **Database**: An SQLite database will host a new junction table to manage the many-to-many relationship.

### Diagram
```
+-----------+         +-------------+         +-------------+
|   Client  | ------> | API Layer   | ------> | Service Layer| 
| (e.g.,    |         |             |         |             |
|  Postman) | <------ |             | <-----  |             |
+-----------+         +-------------+         +-------------+
                                      |
                                      |
                               +-------------+
                               | Data Access |
                               |   Layer     |
                               +-------------+
                                      |
                                      |
                               +-------------+
                               |   SQLite    |
                               |   Database   |
                               +-------------+
```

## III. Technology Stack

The technology stack remains unchanged from previous sprints:
- **Programming Language**: Python
- **Web Framework**: Flask
- **Database**: SQLite
- **ORM**: SQLAlchemy
- **Testing Framework**: pytest
- **Environment Variables**: python-dotenv for configuration
- **API Documentation**: Swagger (Flask-Swagger for API documentation)

## IV. Module Boundaries and Responsibilities

### 1. API Layer
- **Responsibilities**: Define routes and HTTP controllers for managing the relationship between Students and Courses.
- **Endpoints**:
  - POST `/students/{id}/courses`
  - GET `/students/{id}/courses`
  - PATCH `/students/{id}/courses`

### 2. Service Layer
- **Responsibilities**: Handle all business logic regarding student-course relationships, including validation of Student and Course IDs, assignment logic, and updates.

### 3. Data Access Layer
- **Responsibilities**: Interact with the SQLite database to perform operations related to the student-course relationship through a new junction table.

## V. Data Model

The new junction table for managing relationships will be defined as follows:

```python
class StudentCourse(Base):
    __tablename__ = 'student_courses'

    student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
    course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)

    def __repr__(self):
        return f"<StudentCourse(student_id={self.student_id}, course_id={self.course_id})>"
```

This allows the many-to-many relationship between Students and Courses.

## VI. API Contracts

### 1. Assign Courses to a Student
- **Request**:
  - **Method**: POST
  - **Endpoint**: `/students/{id}/courses`
  - **Body**: `{ "course_ids": [1, 2, 3] }`
- **Response**:
  - **Status Code**: 200 OK
  - **Body**: `{ "message": "Courses assigned successfully", "courses": [{ "id": 1 }, { "id": 2 }, { "id": 3 }] }`

### 2. Retrieve a Student's Courses
- **Request**:
  - **Method**: GET
  - **Endpoint**: `/students/{id}/courses`
- **Response**:
  - **Status Code**: 200 OK
  - **Body**: `{ "courses": [{ "id": 1, "name": "Course Name", "level": "Beginner" }, ...] }`
  - **Error Response**: `404 Not Found` for non-existing student IDs

### 3. Update a Student's Course Enrollment
- **Request**:
  - **Method**: PATCH
  - **Endpoint**: `/students/{id}/courses`
  - **Body**: `{ "course_ids": [1] }` (List of course IDs to assign or remove)
- **Response**:
  - **Status Code**: 200 OK
  - **Body**: `{ "message": "Enrollment updated successfully", "courses": [...] }`
  - **Error Response**: `400 Bad Request` for invalid inputs

## VII. Implementation Approach

### 1. Setup
- Ensure the virtual environment is properly set up for the project, if not already done.
- Install required packages: Flask, SQLAlchemy, Flask-Swagger, python-dotenv.

### 2. Database Schema
- Create a new junction table in the SQLite database for `student_courses` to manage the relationship.

### Migration Strategy
- Use Alembic or Flask-Migrate for schema migrations.
- Write migration scripts to create the `student_courses` junction table.
- Ensure migrations maintain data integrity with existing Student and Course records.

### 3. API Endpoint Implementation
- Implement the new endpoints as per the API contracts outlined above using Flask, defining routes and associating them with service layer methods.

### 4. Input Validation
- Implement validation logic in the Service Layer to ensure that the `student_id` and `course_ids` used in requests are valid and exist in the database.

### 5. Automated Testing
- Create unit tests for all API endpoints related to the Student-Course relationship, ensuring test cases cover valid and invalid requests.

## VIII. Error Handling and Validation

- Implement structured error handling for cases where invalid student IDs or course IDs are provided during assignments and updates. Return meaningful HTTP status codes and error messages.

## IX. Logging and Monitoring
- Implement structured logging (JSON format) to track operations and errors associated with the Student-Course relationship API requests and responses.

## X. Deployment Considerations
- Deploy the application to a local server for testing.
- Ensure that the API functions as expected, focusing on both successful and erroneous inputs.

## XI. Success Criteria
- Confirm that users can successfully assign courses to students and retrieve them.
- Validate that all API responses are formatted correctly in JSON and handle input scenarios as expected.

## XII. Technical Trade-offs
- **SQLite**: Continuing with SQLite is practical for local development; production may need a more robust database solution due to performance concerns as user load increases.
- **Validation Scope**: Basic validation meets current requirements, with potential for enhanced checks as the system evolves.

### Conclusion
This implementation plan provides a structured approach to adding the course relationship to the existing Student entity while adhering to best practices for maintainability and scalability.

### Existing Code Files Modifications
1. **New StudentCourse Model**: 
   - Create a new file named `models/student_course.py` to define the `StudentCourse` class.
2. **Update API Layer**: 
   - In `api_layer.py`, add new route handlers for POST, GET, and PATCH requests for student-course relationships.
3. **Service Layer Updates**: 
   - In the existing service layer file, implement logic to handle new API contract requirements, including fetching courses, assigning, and updating enrollments based on the provided IDs.
4. **Unit Tests**: 
   - Create new test cases in `tests/api/test_student_courses.py` for all the operations concerning student-course relationships.

### Migration Example
```bash
# Generate migration
flask db migrate -m "Create student_courses table for relationships"
# Apply migration
flask db upgrade
```

This will ensure proper integration and functionality of the course assignments feature within the existing application while maintaining data integrity.