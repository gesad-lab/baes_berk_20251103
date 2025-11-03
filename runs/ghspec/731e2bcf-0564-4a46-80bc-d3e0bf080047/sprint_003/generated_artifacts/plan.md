# Implementation Plan: Create Course Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Add Email Field to Student Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Student Management Web Application

## Version: 1.0.0  
**Purpose**: To introduce a new Course entity to manage courses offered by educational institutions through an API.

---

## I. Architecture Overview

### 1.1 Architecture Style
- RESTful API architecture to enable creation and management of the new Course entity.

### 1.2 Technology Stack
- **Backend Framework**: Flask (Python)
- **Database**: SQLite for local data storage
- **API Framework**: Flask-RESTful for constructing RESTful APIs
- **Testing Framework**: pytest for unit and integration testing
- **Deployment**: Docker for containerization to ensure easy deployment

## II. Module Breakdown

### 2.1 Module Responsibilities

#### 2.1.1 API Module
- Add new endpoints to facilitate creation and retrieval of courses.

#### 2.1.2 Database Module
- Introduce the new Course table while ensuring existing tables (like Students) remain unaffected.

#### 2.1.3 Error Handling and Validation Module
- Implement input validation for course creation to ensure required fields are provided.

---

## III. Data Model

### 3.1 Entity Definition
- **Course**:
  - `id`: Integer, auto-incremented primary key
  - `name`: String, required
  - `level`: String, required

### 3.2 Database Schema
```sql
CREATE TABLE courses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    level TEXT NOT NULL
);
```

## IV. API Endpoints

### 4.1 Endpoint Definitions

#### 4.1.1 Create Course
- **Endpoint**: `POST /courses`
- **Request Body**:
  ```json
  {
      "name": "Introduction to Programming",
      "level": "Beginner"
  }
  ```
- **Responses**:
  - **201 Created**:
  ```json
  {
      "id": 1,
      "name": "Introduction to Programming",
      "level": "Beginner"
  }
  ```
  - **400 Bad Request** (if name or level is missing):
  ```json
  {
      "error": {
          "code": "E001",
          "message": "Name field is required."
      }
  }
  ```
  ```json
  {
      "error": {
          "code": "E002",
          "message": "Level field is required."
      }
  }
  ```

#### 4.1.2 Retrieve Courses
- **Endpoint**: `GET /courses`
- **Responses**:
  - **200 OK**:
  ```json
  [
      {
          "id": 1,
          "name": "Introduction to Programming",
          "level": "Beginner"
      }
  ]
  ```
  - **Empty List** (if no courses exist):
  ```json
  []
  ```

---

## V. Implementation Approach

### 5.1 Environment Setup
- Maintain the existing Docker container setup used in previous sprints for consistency across environments.
  
### 5.2 Development Phases
1. **Phase 1**: Update the Flask application to create the new Course entity.
2. **Phase 2**: Implement the SQLite database migration to create the Course table while ensuring no disruption to existing Student data.
3. **Phase 3**: Develop new API endpoints for creating and retrieving courses.
4. **Phase 4**: Integrate error handling and validation mechanisms for course creation.
5. **Phase 5**: Write unit tests using pytest, focusing on the functionality of the new course endpoints.
6. **Phase 6**: Ensure database migrations are tested to confirm smooth integration with existing schema.

## VI. Testing Strategy

### 6.1 Test Coverage Goals
- Target 70% coverage of the new course functionality.
- Aim for 90% coverage of critical paths (course creation).

### 6.2 Test Types
- **Unit tests**: Validate the API’s create course function to ensure proper handling of inputs.
- **Integration tests**: Verify the responsiveness of endpoints for course-related data.

### 6.3 Test Organization
- Organize tests in a similar structure to the existing project:
```
- src/
  - app.py
  - models/
    - course.py
  - controllers/
    - course_controller.py
- tests/
  - test_course_controller.py
```

---

## VII. Error Handling

### 7.1 Input Validation
- Ensure the API validates the `name` and `level` fields during course creation, returning appropriate error messages for invalid inputs.

### 7.2 Exception Handling
- Implement logging for any occurring errors while processing course data.
- Avoid exposing sensitive error details to users; log them internally for diagnostics.

---

## VIII. Deployment Considerations

### 8.1 Production Readiness
- Ensure the application can automatically start with no manual intervention.
- Incorporate a health check endpoint to monitor the operational status of the API.

### 8.2 Configuration Management
- Leverage environment variables for database configurations and sensitive data management.

---

## IX. Logging & Monitoring

### 9.1 Logging Strategy
- Utilize structured logging for all API interactions, particularly logging course creation attempts and any associated errors.

---

## X. Success Criteria
- The application can successfully create and retrieve course records, maintaining necessary validations on inputs.
- The `POST /courses` endpoint returns a 201 status code with the created course data upon successful creation.
- The `GET /courses` endpoint returns a 200 status code with the correct list of courses or an empty list.

---

## XI. Technical Trade-Offs and Decisions

- **SQLite** will remain the database choice because of its light footprint and ease of setup, balancing the need for simplicity and required capabilities.
- **Flask RESTful** is chosen for its effectiveness in building lightweight REST APIs, fitting the application's needs.
- **Backward Compatibility**: New Course functionality will not interfere with the existing Student data structure or operations.

---

## XII. Conclusion
This implementation plan delineates the steps required to introduce a new Course entity into the web application. By adhering to this structured approach, we can ensure that the new features are maintainable and seamlessly integrated into the application's architecture.

### Existing Code Files Modifications:
- **src/models/course.py**: Create a new `Course` model class.
- **src/controllers/course_controller.py**: Construct the controller logic for creating and retrieving Course entities.
- **tests/test_course_controller.py**: Develop tests to ensure the API endpoints for course management function correctly.

### Database Migration Strategy:
- Utilize Flask-Migrate to create the new Course table, taking care to maintain the integrity of existing data and establish a fallback option in the event of migration failures. 

### Existing Code Files:
File: src/models/course.py
```python
class Course(db.Model):
    __tablename__ = 'courses'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False, unique=True)
    level = db.Column(db.String, nullable=False)
```

File: src/controllers/course_controller.py
```python
from flask import request, jsonify
from src.models.course import Course

@app.route('/courses', methods=['POST'])
def create_course():
    data = request.json
    name = data.get('name')
    level = data.get('level')

    if not name:
        return jsonify({"error": {"code": "E001", "message": "Name field is required."}}), 400
    if not level:
        return jsonify({"error": {"code": "E002", "message": "Level field is required."}}), 400

    new_course = Course(name=name, level=level)
    db.session.add(new_course)
    db.session.commit()

    return jsonify({"id": new_course.id, "name": new_course.name, "level": new_course.level}), 201

@app.route('/courses', methods=['GET'])
def get_courses():
    courses = Course.query.all()
    return jsonify([{"id": course.id, "name": course.name, "level": course.level} for course in courses])
```

File: tests/test_course_controller.py
```python
import pytest
from flask import json
from src.app import create_app, db
from src.models.course import Course

@pytest.fixture
def app():
    app = create_app({'TESTING': True})

    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

def test_create_course(client):
    response = client.post('/courses', json={"name": "Introduction to Programming", "level": "Beginner"})
    assert response.status_code == 201
    data = response.get_json()
    assert data['name'] == "Introduction to Programming"
    assert data['level'] == "Beginner"

def test_create_course_without_name(client):
    response = client.post('/courses', json={"level": "Beginner"})
    assert response.status_code == 400
    assert response.get_json()['error']['code'] == "E001"

def test_create_course_without_level(client):
    response = client.post('/courses', json={"name": "Introduction to Programming"})
    assert response.status_code == 400
    assert response.get_json()['error']['code'] == "E002"

def test_get_courses_empty(client):
    response = client.get('/courses')
    assert response.status_code == 200
    assert response.get_json() == []

def test_get_courses_with_data(client):
    client.post('/courses', json={"name": "Introduction to Programming", "level": "Beginner"})
    response = client.get('/courses')
    assert response.status_code == 200
    data = response.get_json()
    assert len(data) == 1
    assert data[0]['name'] == "Introduction to Programming"
```

This comprehensive implementation plan lays the groundwork for seamlessly integrating the Course entity into the existing application, while ensuring all best practices are maintained for future development.