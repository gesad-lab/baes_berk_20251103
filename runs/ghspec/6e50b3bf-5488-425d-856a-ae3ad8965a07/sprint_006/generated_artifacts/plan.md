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
# Implementation Plan: Add Email Field to Student Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Student Management Web Application

## Version: 1.0.0  
**Purpose**: Establish a relationship between `Course` and `Teacher` entities to enhance course management within the Student Management Web Application.

---

## 1. Architecture Overview

### 1.1 Layers:
1. **Presentation Layer** - Manages incoming HTTP requests related to course and teacher relationships.
2. **Service Layer** - Implements business logic for assigning teachers to courses and retrieving course details.
3. **Data Access Layer (DAL)** - Facilitates interactions with the SQLite database for CRUD operations concerning courses and teachers.
4. **Database** - SQLite for persistent storage of course and teacher data, with modified relationships.

### 1.2 Technologies:
- **Programming Language**: Python
- **Web Framework**: Flask
- **Database**: SQLite
- **ORM**: SQLAlchemy for database interactions
- **Data Serialization and Validation**: Marshmallow for data validation and serialization
- **Testing Framework**: pytest for unit and integration tests

---

## 2. Data Model

### 2.1 Course Entity
Existing and updated representation:
```python
class Course:
    course_id: int  # Primary key, auto-increment
    course_name: str  # Required
    teacher_id: int  # Optional foreign key to Teacher
```

### 2.2 Teacher Entity
Use previously defined Teacher entity:
```python
class Teacher:
    teacher_id: int  # Primary key, auto-increment
    name: str        # Required
    email: str       # Required and must be unique
```

### 2.3 Database Schema Changes
- **Table Modifications**:
  - Update the `Courses` table to include:
    - `teacher_id`: INTEGER, FOREIGN KEY, REFERENCES `Teacher`, NULLABLE

### 2.4 Migrations
- **Migration Strategy**: Use Flask-Migrate with SQLAlchemy to implement the database schema changes.
- Migration procedures:
  ```bash
  flask db migrate -m "Add teacher_id to Course table"
  flask db upgrade
  ```

---

## 3. API Contracts

### 3.1 Assign Teacher to Course API
- **Endpoint**: `POST /courses/{course_id}/assign_teacher`
- **Request Body**:
    ```json
    {
      "teacher_id": "int"
    }
    ```
- **Responses**:
  - **Success**:
    - **Status**: `200 OK`
    - **Body**:
      ```json
      {
        "course_id": "int",
        "assigned_teacher_id": "int"
      }
      ```
  - **Error**:
    - **Status**: `404 Not Found`
    - **Body**:
      ```json
      {
        "error": {
          "code": "E003",
          "message": "Course or teacher not found"
        }
      }
      ```

### 3.2 Retrieve Course Details with Teacher API
- **Endpoint**: `GET /courses/{course_id}`
- **Responses**:
  - **Success**:
    - **Status**: `200 OK`
    - **Body**:
      ```json
      {
        "course_id": "int",
        "course_name": "string",
        "assigned_teacher": {
          "teacher_id": "int",
          "name": "string",
          "email": "string"
        }
      }
      ```
  - **Error**:
    - **Status**: `404 Not Found`
    - **Body**:
      ```json
      {
        "error": {
          "code": "E004",
          "message": "Course not found"
        }
      }
      ```

---

## 4. Implementation Approach

### 4.1 Project Structure Adjustments
```plaintext
student_management/
│
├── src/
│   ├── app.py                  # Main application
│   ├── models.py               # Data models: Course, Teacher, Student
│   ├── routes.py               # Updated API endpoints for course-teacher functionalities
│   ├── services.py             # Business logic for assigning teachers to courses
│   ├── database.py             # Database setup and migration handling
│   ├── schemas.py              # Data validation schemas for course-teacher interactions
│
├── tests/
│   ├── test_routes.py          # Tests for API endpoints including course-teacher relationships
│   ├── test_services.py        # Tests for service logic specifically around course assignments
│
├── requirements.txt            # Required packages for the project
├── .env.example                 # Sample environment variables documentation
├── README.md                   # Updated project documentation
```

### 4.2 Development Steps
1. **Database Migration**: Implement schema changes to the `Course` table to incorporate the `teacher_id`.
2. **Update Models**: Modify `models.py` to reflect the new foreign key relationship between `Course` and `Teacher`.
3. **Routes Implementation**: Update `routes.py` to include the new API endpoints for assigning teachers to courses and retrieving course details.
4. **Service Logic Development**: Implement the required logic in `services.py` to manage the assignment of teachers, including validation for existing course and teacher records.
5. **Validation Schemas**: Enhance `schemas.py` with Marshmallow schemas for request validation related to the teacher assignment API.
6. **Testing Framework Setup**: Extend testing in `test_routes.py` and `test_services.py` to cover new scenarios including successful assignments and handling of errors.
7. **Documentation Updates**: Ensure `README.md` is updated with the new API endpoints, including usage instructions and migration details.

---

## 5. Scalability and Security Considerations

### 5.1 Scalability
- Ensure that fetching courses and their respective teachers is optimized using efficient querying techniques.
- Design for stateless API operations to improve response times and maintain scales as user demand grows.

### 5.2 Security
- Incorporate rigorous input validation to ensure that only existing `course_id` and `teacher_id` are processed.
- Ensure proper error handling that does not reveal sensitive data while logging essential information for debugging.

---

## 6. Testing Strategy

### 6.1 Test Coverage
- Target 70% overall test coverage, with critical paths in teacher assignments and course retrieval methods exceeding 90%.

### 6.2 Types of Tests
- **Unit Tests**: Verify individual service functions for assigning teachers and retrieving course details.
- **Integration Tests**: Confirm that the new API endpoints behave as specified and handle various inputs correctly.
- **Contract Tests**: Ensure endpoint responses match expected formats for both success and error scenarios.

### 6.3 Test Organization
- Follow the existing source code structure to organize tests, maintaining clarity and enhancing maintainability.

---

## 7. Deployment Considerations

### 7.1 Production Readiness
- The application must be capable of seamless startup, executing the content of the migrations automatically.
- Implement a health check endpoint to consistently monitor and validate the service status.

### 7.2 Environment Configuration
- Clearly document new dependencies and their configurations in `.env.example`, detailing environmental setup.

---

## 8. Conclusion and Next Steps
Following approval of this implementation plan, we will initiate the setup for the modified application structure, execute necessary database migrations, and begin development on the tasks outlined herein. Emphasis will be placed on comprehensive tests and documentation to ensure both maintainability and ease of future feature integrations.

**Modifications to Existing Code Files**:
- In `models.py`, update the Course entity to add the foreign key reference to the Teacher entity.
- Extend `routes.py` for new endpoints and their connection to the existing service functions.
- Validate appropriate test coverage for new functionalities in `test_routes.py` and `test_services.py`.

**Instructions for Technical Plan*:
1. Follow the same tech stack as previous sprints.
2. Ensure seamless integration while maintaining backward compatibility.
3. Document changes made to existing files alongside the introduction of new abilities.
4. Specify the migration strategy for the added foreign key relation between `Course` and `Teacher`.