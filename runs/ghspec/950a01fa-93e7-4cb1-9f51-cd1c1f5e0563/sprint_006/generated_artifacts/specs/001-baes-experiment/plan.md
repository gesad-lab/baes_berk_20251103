# Implementation Plan: Add Teacher Relationship to Course Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

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

## Version: 1.0.0  
**Purpose**: To establish a relationship between the Course entity and the Teacher entity in the existing educational system to enhance management and assignment capabilities related to teaching resources.

---

## I. Technical Architecture

### 1.1 High-Level Architecture
- **Frontend**: Vanilla JavaScript for API interactions (using Fetch API), with forms designed to manage Course and Teacher assignments.
- **Backend**: Python Flask application to handle API requests related to Course and Teacher entities.
- **Database**: SQLite to manage data persistence, modifying the existing Course table to include a foreign key to the Teacher table.

### 1.2 Components Overview
- **API Layer**: Flask RESTful API to manage Course and Teacher relationships through specified endpoints.
- **Database Layer**: SQLite for data persistence, with updates to the existing Course table.
- **Model Layer**: SQLAlchemy to manage ORM, ensuring a link between Course and Teacher entities.

---

## II. Technology Stack
- **Programming Languages**: 
  - Python 3.11+
- **Frameworks**: 
  - Flask for the web framework.
  - Flask-SQLAlchemy for ORM.
- **Database**: 
  - SQLite for database management and schema modifications.
- **Frontend**: 
  - Vanilla JavaScript for API calls.
  - HTML/CSS for maintaining user interface consistency.

---

## III. Module Responsibilities

### 3.1 API Module
- **PUT /courses/{course_id}/assign-teacher**: Assign a Teacher to a Course.
- **GET /courses/{course_id}**: Retrieve details of a specific Course, including assigned Teacher information.

### 3.2 Database Module
- **Database Migration**: 
  - Modify existing Course table to add a `teacher_id` column, linking to the Teacher entity and ensuring data integrity.
- **Data Model**: 
  - Update the existing Course model to include a foreign key constraint.

---

## IV. Data Models

### 4.1 Course Model Update
Update the Course model in `src/models.py`:

```python
class Course(db.Model):
    __tablename__ = 'courses'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=True)
    teacher_id = db.Column(db.Integer, db.ForeignKey('teachers.id'), nullable=True)

    teacher = db.relationship('Teacher', backref='courses')

    def __repr__(self):
        return f'<Course {self.name}>'
```

### 4.2 API Contracts

**Request Schema for Assigning a Teacher to a Course**
- **Endpoint**: `PUT /courses/{course_id}/assign-teacher`
- **Request Body (JSON)**:
```json
{
  "teacher_id": "1"
}
```
- **Response (JSON on Success)**:
```json
{
  "message": "Teacher assigned successfully",
  "course": {
    "id": 1,
    "name": "Mathematics",
    "description": "An advanced mathematics course",
    "teacher_id": 1
  }
}
```
- **Error Response (Non-existent Course)**:
```json
{
  "error": {
    "code": "E001",
    "message": "Course does not exist"
  }
}
```

**Response Schema for Retrieving Course Details**
- **Endpoint**: `GET /courses/{course_id}`
- **Response (JSON)**:
```json
{
  "id": 1,
  "name": "Mathematics",
  "description": "An advanced mathematics course",
  "teacher": {
    "name": "John Doe",
    "email": "john.doe@example.com"
  }
}
```

---

## V. Error Handling

### 5.1 Input Validation
- Validate presence of `teacher_id` in the request body for the `assign-teacher` endpoint.
- Check if the specified Course exists before proceeding with the assignment.

### 5.2 Error Messages
- Implement consistent error messaging for missing or invalid data.
- Log errors systematically for all API requests to facilitate debugging efforts.

---

## VI. Testing Strategy

### 6.1 Test Coverage Goals
- Target at least 90% test coverage for functionalities concerning Course and Teacher assignment logic.
- Include unit tests and integration tests for all new API endpoints.

### 6.2 Test Types
- **Unit Tests**: Validate Course assignment logic and model relationships.
- **Integration Tests**: Ensure the robustness of the `assign-teacher` and `retrieve-course` endpoints.

### 6.3 Testing Framework
- Use `pytest` for writing and executing tests, consistent with prior testing frameworks.

---

## VII. Deployment Considerations

### 7.1 Production Readiness
- Ensure the application operates without requiring manual intervention on startup.
- Include health check endpoints for monitoring service z health status.

### 7.2 Version Control
- Maintain clean and history-documented commits, ensuring clarity in changes made.

---

## VIII. Configuration Management

### 8.1 Environment Setup
- Use the `.env` configuration for environment variables, maintaining a `.env.example` for documentation.
  
### 8.2 Documentation
- Update README.md to provide comprehensive details on the new Course and Teacher relationships and their corresponding APIs.

---

## IX. Logging & Monitoring

### 9.1 Logging Requirements
- Implement structured logging for key API actions regarding Course assignments and errors encountered, facilitating easier monitoring.

---

## X. Implementation Phases

### Phase 1: Database Migration
- Create migration scripts through Flask-Migrate to add the `teacher_id` column to the Course table while ensuring existing relationships remain intact.

### Phase 2: API Development
- Develop the `PUT` and `GET` endpoints to handle Course assignments and retrievals respectively.
- Implement thorough input validation and error handling mechanisms.

### Phase 3: Comprehensive Testing
- Write unit tests and integration tests to cover new functionalities regarding the Course-Teacher relationship.

### Phase 4: Frontend Integration
- Update any relevant frontend components to reflect Course and Teacher relationship management.

### Phase 5: Deployment
- Document the deployment steps, ensuring clear instructions for environment variable setups.

---

## XI. Trade-offs and Considerations
- **Error Handling Complexity**: The need for robust error handling and validation increases the implementation complexity but is necessary to ensure the system's usability.
- **Database Integrity**: Ensuring continued integrity of existing data while introducing new foreign key relationships in the Course table demands careful migration planning and testing.

---

## Conclusion
This implementation plan delineates the steps required to establish a Teacher-Course relationship within the educational system. This addition aims to improve management capabilities and optimize educational resource utilization.

---

## Existing Code Files Modifications
### File: src/models.py
- Modify the existing Course model to include the `teacher_id` foreign key.

### File: tests/test_api.py
- Extend to include tests for the new Course assignment endpoint, confirming correct behavior for success and error scenarios.

### File: tests/test_course_teacher.py
- Create a new file to test the functionality of Course and Teacher relationship management, documenting edge cases and validation errors.

### API Tests File: tests/test_api.py
Include tests for endpoint behaviors surrounding the assignment and retrieval operations for the Course-Teacher relationship. 

Existing Code Files:
File: tests/test_api.py
```python
# Add necessary tests for Course and Teacher integration
import pytest
from fastapi.testclient import TestClient
from src.main import app  # FastAPI app reference

# Assuming necessary setup has already been conducted.
client = TestClient(app)

def test_assign_teacher_to_course():
    response = client.put("/courses/1/assign-teacher", json={"teacher_id": "1"})
    assert response.status_code == 200
    assert response.json()["message"] == "Teacher assigned successfully"

def test_retrieve_course_details():
    response = client.get("/courses/1")
    assert response.status_code == 200
    assert "teacher" in response.json()
```
 
File: tests/test_course_teacher.py
```python
# New file to specifically test course teacher assignment functionalities
import pytest
from fastapi.testclient import TestClient
from src.main import app  # FastAPI app reference

client = TestClient(app)

def test_assign_teacher_to_non_existent_course():
    response = client.put("/courses/999/assign-teacher", json={"teacher_id": "1"})
    assert response.status_code == 404
    assert response.json()["error"]["code"] == "E001"
```