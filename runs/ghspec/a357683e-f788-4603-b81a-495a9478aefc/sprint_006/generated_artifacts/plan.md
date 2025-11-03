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

Previous Sprint Plan:
# Implementation Plan: Add Email Field to Student Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Student Entity Web Application

## Version: 1.0.0
## Purpose: To establish a relationship between the Course entity and the Teacher entity, allowing for effective management of course-teacher assignments.

---

## I. Architecture Overview

### 1.1 Architecture Diagram
- The current architecture will be extended to support the relationship between Courses and Teachers while maintaining the existing microservices structure with the SQLite database.

```
Client (HTTP requests)
        |
+------------------+
|   REST API       |
|   (Flask/FastAPI)|
+------------------+
        |
+------------------+
|    SQLite DB     |
+------------------+
```

### 1.2 Technologies
- **Programming Language**: Python
- **Web Framework**: Flask
- **Database**: SQLite
- **ORM**: SQLAlchemy
- **Testing Framework**: pytest
- **Environment Management**: pipenv or virtualenv
- **Version Control**: Git

---

## II. Module Boundaries and Responsibilities

### 2.1 Updated Existing Modules
- **CourseModule**: Update Course model to include a reference to `teacher_id` and update related methods to manage teacher assignments.
- **TeacherModule**: (Already created in the previous implementation) to manage teacher data.

### 2.2 New Modules
- No new modules are being introduced; rather, existing modules will be updated to reflect the new relationship.

---

## III. Data Models and API Contracts

### 3.1 Data Models

#### Course Model Update
- Update the existing `Course` table to include the `teacher_id` foreign key:

```python
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

class Course(Base):
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    teacher_id = Column(Integer, ForeignKey('teachers.id'), nullable=True)  # Allowing null for courses without assigned teacher

    # Establishing relationship with Teacher
    teacher = relationship("Teacher", back_populates="courses")
```

#### Teacher Model (for reference)
- Keep the Teacher model unchanged.

### 3.2 API Endpoints

#### 3.2.1 Assign a Teacher to a Course
- **Method**: PATCH
- **Endpoint**: `/courses/{course_id}/assign-teacher`
- **Request Body**:
  - `teacher_id`: integer (required)
- **Response**: 
  - **200 OK**: `{"id": <course_id>, "name": "<course_name>", "teacher": {"id": <teacher_id>, "name": "<teacher_name>"}}`

#### 3.2.2 Retrieve Course with Assigned Teacher
- **Method**: GET
- **Endpoint**: `/courses/{course_id}`
- **Response**:
  - **200 OK**: `{"id": <course_id>, "name": "<course_name>", "teacher": {"id": <teacher_id>, "name": "<teacher_name>"}}`

#### 3.2.3 Remove Teacher from a Course
- **Method**: PATCH
- **Endpoint**: `/courses/{course_id}/remove-teacher`
- **Response**: 
  - **200 OK**: `{"id": <course_id>, "name": "<course_name>", "teacher": null}`

#### 3.2.4 Query Courses by Teacher
- **Method**: GET
- **Endpoint**: `/teachers/{teacher_id}/courses`
- **Response**:
  - **200 OK**: `[{ "id": <course_id>, "name": "<course_name>" }, ...]`

---

## IV. Implementation Approach

### 4.1 Development Steps
1. **Setup Project Environment**
   - Ensure `requirements.txt` includes SQLAlchemy and Flask-Migrate for database migration.

2. **Database Migration**
   - Create a new migration script using Alembic:
     - Add `teacher_id` column to `courses` table.

3. **API Module Updates**
   - Implement the new route handlers in the API module to handle:
     - Assigning a teacher to a course
     - Removing a teacher from a course
     - Retrieving course details with assigned teacher information
     - Querying all courses for a specific teacher.

4. **Input Validation**
   - Implement validation to ensure that `teacher_id` used in assignments exists.
   - Handle scenarios for unique teacher assignments.

5. **Error Handling Enhancements**
   - Update the error handling module to manage not found (404) errors for courses and teachers effectively.

6. **Testing Implementation**
   - Develop test cases in `tests/api/test_course.py` to validate the effectiveness of the new endpoints targeting the course-teacher relationship:
     - Tests should include assignment, retrieval, and removal actions.

7. **Documentation Updates**
   - Update `README.md` with the details of the new endpoints and examples of using the features related to the teacher-course relationship.

---

## V. Scalability and Security Considerations

### 5.1 Scalability
- The design ensures stateless service principles, making it more scalable and resilient as traffic grows.

### 5.2 Security
- Implement input validation and avoid logging sensitive teacher data.
- Ensure that API authentication checks for permissions to assign or remove teachers.

---

## VI. Code Quality and Documentation

### 6.1 Coding Standards
- Follow existing project coding standards for clarity and maintainability.

### 6.2 Documentation
- Document all new functions, models, end-point behaviors, and usage examples in the project documentation.

---

## VII. Testing Strategy

### 7.1 Types of Tests
- **Unit Tests**: Validate business logic in the course management functions.
- **Integration Tests**: Ensure the integration of the full API cycle involving assignments and lookups.
- **Contract Tests**: Confirm the API endpoints return expected results based on the defined contracts.

### 7.2 Testing Organization
- Align test structures with the source code organization, using descriptive naming conventions.

---

## VIII. Deployment Considerations

### 8.1 Production Readiness
- Prepare migration scripts for zero downtime and run tests against a production-like environment before deployment.

### 8.2 Backward Compatibility
- Ensure that any existing data models remain functional and that no existing data is lost during the migration and updates.

---

## IX. Version Control Practices

### 9.1 Git Hygiene
- Ensure comprehensive commit messages that provide context on the changes and preserve history associated with the implementation.

---

This implementation plan lays out the steps needed to effectively connect the Course entity to Teachers, ensuring that the facets of the application remain functional, maintainable, and extendable for future features. 

Existing Code Files:
### File: tests/api/test_course.py
```python
import pytest
from flask import json
from app import create_app, db
from app.models import Course, Teacher

@pytest.fixture(scope='module')
def test_client():
    app = create_app('testing')
    with app.test_client() as testing_client:
        with app.app_context():
            db.create_all()  # Creating the database tables
            yield testing_client
            db.drop_all()  # Cleanup after tests

def test_assign_teacher_to_course_success(test_client):
    # Assuming Teacher and Course already exist
    teacher = Teacher(name="John Doe", email="john@example.com")
    course = Course(name="Math 101")
    db.session.add(teacher)
    db.session.add(course)
    db.session.commit()

    response = test_client.patch(f'/courses/{course.id}/assign-teacher', 
                                  data=json.dumps({'teacher_id': teacher.id}),
                                  content_type='application/json')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['teacher']['name'] == "John Doe"

def test_remove_teacher_from_course_success(test_client):
    # Assuming this course already has a teacher assigned from previous test
    response = test_client.patch(f'/courses/{course.id}/remove-teacher')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['teacher'] is None
```
### File: tests/models/test_class.py
```python
import pytest
from app import create_app, db
from app.models import Teacher, Course

@pytest.fixture(scope='module')
def test_client():
    app = create_app('testing')
    with app.test_client() as testing_client:
        with app.app_context():
            db.create_all()
            yield testing_client
            db.drop_all()

def test_course_teacher_relationship():
    teacher = Teacher(name="Jane Smith", email="jane@example.com")
    course = Course(name="History 101", teacher=teacher)
    db.session.add(teacher)
    db.session.add(course)
    db.session.commit()

    # Test relationship
    assert course.teacher.email == "jane@example.com"
``` 

This structured implementation plan thoroughly documents the integration of the teacher relationship to existing course entities and stipulates the necessary steps to maintain integrity in the current application while ushering in new functionality.