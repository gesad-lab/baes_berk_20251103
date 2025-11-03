# Implementation Plan: Add Teacher Relationship to Course Entity

---
## INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Create Teacher Entity

---
## INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Add Course Relationship to Student Entity

---
## INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Create Course Entity

---

## Version: 1.0.0  
## Purpose: Technical implementation plan for establishing a relationship between Teacher and Course entities within the Student Management Application.  
## Scope: Implement a RESTful API for managing the relationship between teachers and courses, including assignments.

---

## I. Architecture Overview

- **Architecture Type**: Monolithic API
- **Deployment**: Cloud (e.g., AWS, Heroku)
- **Communication Protocol**: HTTP/HTTPS
- **Data Format**: JSON for requests and responses
- **Technology Stack**:
  - **Backend Framework**: FastAPI (Python) for rapid development of APIs
  - **Database**: PostgreSQL for relational data storage
  - **ORM**: SQLAlchemy for database interaction
  - **Testing Framework**: Pytest for unit and integration testing
  - **Dependency Management**: Poetry for managing Python dependencies
  - **Environment Management**: Docker for containerization

---

## II. Module Breakdown

### 1. API Module
- **Responsibilities**:
  - Handle incoming HTTP requests for assigning/removing teachers to/from courses, and retrieving course details with teacher information.
  - Parse and validate requests related to teacher assignments.
  - Return JSON responses confirming the actions taken.

### 2. Database Module
- **Responsibilities**:
  - Define and manage changes to the `courses` table schema to include the new `teacher_id` foreign key.
  - Interface with the PostgreSQL database to perform CRUD operations for teacher and course relationships.

### 3. Test Module
- **Responsibilities**:
  - Contain all tests for the API endpoints that validate the functionality of assigning, retrieving, updating, and removing teachers from courses.
  - Validate scenarios as defined in the User Scenarios section regarding teacher-course relationships.

---

## III. Data Models

### Update Course Model
We will modify the existing `Course` model to include a relationship with `Teacher`.

```python
class Course(Base):
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    level = Column(String, nullable=False)
    teacher_id = Column(Integer, ForeignKey('teachers.id'))  # Foreign Key to Teacher

    teacher = relationship("Teacher", back_populates="courses")
```

### Teacher Model (Modified for Relationship)
Update the `Teacher` model to reflect the relationship with `Course`.

```python
class Teacher(Base):
    __tablename__ = 'teachers'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)

    courses = relationship("Course", back_populates="teacher")  # Relationship with Course
```

### Database Migration Strategy
- Use Alembic for database migrations.
- Create a migration script that:
  - Adds the `teacher_id` foreign key to the `courses` table.
- The migration command:
  ```bash
  alembic revision --autogenerate -m "add teacher_id to courses table"
  ```
- Ensure the migration preserves all existing data by testing it in a staging environment before applying it to production.

---

## IV. API Contract

### 1. Assign Teacher to Course Endpoint
- **Endpoint**: `POST /courses/{course_id}/assign_teacher`
- **Request Body**:
    ```json
    {
      "teacher_id": 1
    }
    ```
- **Response**:
    ```json
    {
      "message": "Teacher assigned successfully.",
      "course_id": {course_id},
      "teacher_id": {teacher_id}
    }
    ```
- **HTTP Status Codes**:
  - 201 Created: If the teacher is successfully assigned.
  - 404 Not Found: If either the course or teacher does not exist.
  - 400 Bad Request: If the input is invalid.

### 2. Retrieve Course with Teacher Endpoint
- **Endpoint**: `GET /courses/{course_id}`
- **Response (Success)**:
    ```json
    {
      "id": {course_id},
      "name": "Mathematics",
      "level": "101",
      "teacher": {
        "id": 1,
        "name": "John Doe",
        "email": "johndoe@example.com"
      }
    }
    ```

### 3. Update Course Teacher Endpoint
- **Endpoint**: `PUT /courses/{course_id}/update_teacher`
- **Request Body**:
    ```json
    {
      "teacher_id": 2
    }
    ```
- **Response**:
    ```json
    {
      "message": "Teacher updated successfully.",
      "course_id": {course_id},
      "new_teacher": {
        "id": 2,
        "name": "Jane Smith",
        "email": "janesmith@example.com"
      }
    }
    ```

### 4. Remove Teacher from Course Endpoint
- **Endpoint**: `DELETE /courses/{course_id}/remove_teacher`
- **Response**:
    ```json
    {
      "message": "Teacher removed successfully from course."
    }
    ```

---

## V. Implementation Strategy

1. **Setup Project Environment**:
   - Update the Docker setup to include necessary configurations for database migrations compatible with changes in the `courses` table schema.

2. **Develop API Endpoints**:
   - Implement the new endpoints in `src/api/course_teacher_api.py` to handle teacher management functionality related to courses.

3. **Database Integration**:
   - Modify existing SQLAlchemy models in `src/models.py` to reflect the addition of `teacher_id`.

4. **Testing**:
   - Create unit tests for `course_teacher_api.py` using Pytest.
   - Ensure all user scenarios are covered, including validation of success and error responses.

5. **Deployment**:
   - Utilize Docker to containerize the application, ensuring smooth migrations and compatibility checks across environments.

---

## VI. Performance, Scalability, and Security Considerations

1. **Performance**:
   - Optimize the queries to ensure quick responses especially for the retrieval of courses with teacher assignments.

2. **Scalability**:
   - Ensure that all API methods remain stateless to support scaling in a distributed environment.

3. **Security**:
   - Validate and sanitize all input data to prevent injection attacks, especially on the assignment endpoints.
   - Use environment variables to manage sensitive configurations securely.

---

## VII. Logging & Monitoring

- Implement structured logging for better traceability of API requests related to course-teacher management.
- Monitor key metrics such as API performance, error rates, and response times from the new endpoints.

---

## VIII. Documentation

- Update API documentation to reflect the new endpoints for managing teacher assignments to courses, utilizing FastAPI's in-built capabilities.
- Revise the `README.md` to include instructions for setting up and utilizing the new features.

---

## IX. Conclusion

This implementation plan provides a comprehensive approach to building a relationship between teachers and courses in the Student Management Application. Following established coding standards will ensure that the integration is smooth, efficient, and preserves data integrity while enhancing functionality.

---

### Existing Code File Modifications:

- **New Module**:
  - Create `src/api/course_teacher_api.py` for API logic related to the teacher-course relationship.

### File Modifications:
- **Models**: 
  - Modify `src/models.py` to add the `teacher_id` column to the `courses` table.

### Example test modifications:
File: `tests/api/test_course_teacher_api.py`
```python
import pytest
from fastapi.testclient import TestClient
from src.api.course_teacher_api import app  # Assuming FastAPI instance for course-teacher management is here

client = TestClient(app)

def test_assign_teacher_to_course():
    response = client.post(f"/courses/1/assign_teacher", json={"teacher_id": 1})
    assert response.status_code == 201
    assert "course_id" in response.json()
    assert "teacher_id" in response.json()

def test_retrieve_course_with_teacher():
    response = client.get("/courses/1")
    assert response.status_code == 200
    assert "teacher" in response.json()

def test_update_course_teacher():
    response = client.put("/courses/1/update_teacher", json={"teacher_id": 2})
    assert response.status_code == 200
    assert response.json()["new_teacher"]["id"] == 2

def test_remove_teacher_from_course():
    response = client.delete("/courses/1/remove_teacher")
    assert response.status_code == 200
    assert response.json()["message"] == "Teacher removed successfully from course."
```

This plan is designed to effectively integrate the functionality for teacher-course relationships within the existing structure and maintain backward compatibility with all current data models, while also allowing for future enhancements within the application.