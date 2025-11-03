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

## INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Add Email Field to Student Entity

---

## INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Student Entity Web Application

## I. Overview
This implementation plan outlines the architecture and necessary steps for adding a `Teacher` relationship to the existing `Course` entity. The goal is to establish a relationship that allows courses to be associated with a specific teacher, enhancing course management and laying the groundwork for future reporting functionality.

## II. Architecture
- **Architecture Style**: Microservices-oriented design, maintaining a service that manages the `Course` entity alongside the `Teacher` entity.
- **Framework**: FastAPI will be utilized for the RESTful APIs.
- **Database**: SQLite as a local development database to maintain consistency with previous sprints.
- **Response Format**: JSON for all API interactions.

### Module Boundaries
1. **API Layer**: Handles HTTP requests pertaining to course-teacher associations, including assignment and removal.
2. **Service Layer**: Contains business logic for assigning/removing teachers from courses and validating input data.
3. **Data Access Layer**: Manages database interactions related to courses, relying on SQLAlchemy for ORM capabilities.
4. **Validation Layer**: Uses Pydantic to validate incoming data for course and teacher IDs.

## III. Technology Stack
- **Programming Language**: Python 3.11+
- **Framework**: FastAPI
- **Database**: SQLite
- **ORM**: SQLAlchemy for database interactions
- **Testing**: pytest for unit and integration testing
- **Dependency Management**: Poetry or pip for Python package management

## IV. Data Model
### Course Entity
Updating the existing `Course` entity to include a foreign key relationship with `Teacher`:
```python
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Course(Base):
    __tablename__ = 'courses'
    
    id = Column(String, primary_key=True, index=True)
    teacher_id = Column(String, ForeignKey('teachers.id'), nullable=True)  # New relationship field added

    teacher = relationship("Teacher", back_populates="courses")  # Create back_populates for bidirectional relationship
```

### Teacher Entity
```python
class Teacher(Base):
    __tablename__ = 'teachers'
    
    id = Column(String, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    courses = relationship("Course", back_populates="teacher")  # Adding back_populates for reverse relationship
```

### Migration Strategy
1. Generate a migration script using Alembic to add the `teacher_id` field to the existing `courses` table:
   ```bash
   alembic revision --autogenerate -m "Add teacher_id to courses"
   ```
2. The migration will ensure existing `Student` and `Teacher` records remain unchanged while adding the new relationship to `Course`.

## V. API Specification
### Endpoints
- **Assign Teacher to Course**
  - **Endpoint**: `PUT /courses/{courseId}/assignTeacher`
  - **Request Body**: 
    ```json
    {
        "teacherId": "teacher_id"
    }
    ```
  - **Success Response**: 
    ```json
    {
        "id": "course_id",
        "name": "Course Name",
        "teacher_id": "teacher_id"  # Updated field
    }
    ```
  - **Error Responses**:
    - **Invalid Course ID**:
      ```json
      {
          "error": {
              "code": "E001",
              "message": "Course not found"
          }
      }
      ```
    - **Invalid Teacher ID**:
      ```json
      {
          "error": {
              "code": "E002",
              "message": "Teacher not found"
          }
      }
      ```

- **Remove Teacher from Course**
  - **Endpoint**: `DELETE /courses/{courseId}/removeTeacher`
  - **Success Response**: 
    ```json
    {
        "id": "course_id",
        "name": "Course Name",
        "teacher_id": null  # Teacher assignment removed
    }
    ```

## VI. Implementation Steps
1. **Environment Setup**
   - Verify that Python packages such as `FastAPI`, `SQLAlchemy`, and `Alembic` are installed and up to date.

2. **Project Structure Modifications**
   ```plaintext
   course_api/
   ├── src/
   │   ├── main.py              # Update to include PUT and DELETE methods for assigning/removing Teacher
   │   ├── models.py            # Update Course class to include new teacher_id
   │   ├── crud.py              # Add methods for assigning/removing Teacher from a Course
   │   ├── schemas.py           # Update Pydantic models for validation
   │   ├── database.py          # Ensure database connection remains intact
   │   ├── migrations/           # Directory for Alembic containing migration scripts
   ├── tests/
   │   ├── test_courses.py       # Add tests for assigning/removing teachers from courses and validating inputs
   ├── .env.example              # Update configurations if necessary
   ├── requirements.txt          # Update to reflect new dependencies if required
   └── README.md                 # Update documentation to reflect changes in Course entity handling
   ```

3. **Code Implementation Changes**
   - **models.py**: Update the `Course` class to define the new foreign key relationship with `Teacher`.
   - **crud.py**: Implement functions `assign_teacher_to_course(course_id, teacher_id)` and `remove_teacher_from_course(course_id)` that handle assignments and removals.
   - **schemas.py**: Extend existing schemas to include Pydantic models for validation of incoming requests.
   - **main.py**: Add the new endpoints for assigning and removing teachers from courses.

4. **Validation and Error Handling**
   - Implement input validation for the IDs using Pydantic in the API layer.
   - Return structured error messages for invalid course or teacher IDs.

5. **Testing**
   - Expand `tests/test_courses.py` to include tests for the new assignment and removal functionalities ensuring correctness and error handling.
   - Achieve high coverage for success and error paths in tests.

6. **Documentation**
   - Revise the `README.md` to describe the new API capabilities related to Teacher assignments to Courses, including examples of request and response formats.

## VII. Deployment Considerations
- Ensure the application starts without manual intervention and all environment variables are properly configured.
- Verify that all migrations run seamlessly, ensuring data integrity is maintained.

## VIII. Scalability & Future Improvements
- Future considerations may include analytics features associated with course effectiveness based on teacher assignments.
- The potential transition to more robust databases (like PostgreSQL) should be explored for scalability as usage grows.

## IX. Technical Trade-offs
- Adding new relationships will increase complexity in data access patterns, but enhances data integrity and management capabilities.
- SQLite is sufficient for development purposes but will require assessment for production deployments to handle increased load.

## X. Conclusion
This implementation plan provides a comprehensive approach to adding the Teacher relationship to the Course entity. Following the outlined steps ensures adherence to existing architecture while facilitating maintainability and future feature accessibility.

Existing Code Files:
No existing code files contain references that directly interact with the aforementioned features. The integration will solely expand upon newer implementations. 

Existing Code Files:
File: tests/test_courses.py
```python
import pytest
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_assign_teacher_to_course_success():
    response = client.put("/courses/course_id/assignTeacher", json={"teacherId": "teacher_id"})
    assert response.status_code == 200
    assert response.json()["teacher_id"] == "teacher_id"

def test_assign_teacher_invalid_course():
    response = client.put("/courses/invalid_course_id/assignTeacher", json={"teacherId": "teacher_id"})
    assert response.status_code == 404
    assert response.json()["error"]["code"] == "E001"

def test_remove_teacher_from_course_success():
    response = client.delete("/courses/course_id/removeTeacher")
    assert response.status_code == 200
    assert response.json()["teacher_id"] is None
```

The above outlines how to implement the new feature successfully while maintaining a structured course management system, ensuring all necessary modifications and new functionalities are clearly documented and tested.