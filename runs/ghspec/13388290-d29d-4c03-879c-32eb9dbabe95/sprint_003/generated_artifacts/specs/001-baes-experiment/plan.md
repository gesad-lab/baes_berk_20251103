# Implementation Plan: Create Course Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Add Email Field to Student Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Student Management Web Application

## 1. Overview
The goal of this implementation plan is to detail the architecture, tech stack, and approach for introducing a new Course entity to the existing Student Management Web Application. This feature will allow users to create, access, and manage courses, thereby enhancing the system's ability to organize student learning records effectively.

## 2. Architecture
The web application will continue to follow a microservice architecture, leveraging a RESTful API for communication between the client and the server. This architecture will be extended with a new service module specifically for managing Course entities.

### 2.1 Module Breakdown
- **Student Service**: Manages operations related to Student entities.
- **Course Service**: New module to handle operations related to Course entities, including creation and retrieval.
- **Database Layer**: Responsible for data access and persistence in a SQLite database, which will be updated to include a Course table.
- **API Layer**: Manages new API endpoints for course operations while preserving existing functionality related to Student entities.

## 3. Tech Stack
- **Programming Language**: Python
- **Web Framework**: Flask
- **Database**: SQLite
- **ORM**: SQLAlchemy for database interactions
- **Request Handling**: Marshmallow for request validation and serialization
- **Testing Framework**: pytest for unit and integration testing

## 4. Implementation Approach

### 4.1 Database Schema
We will introduce a new `courses` table in the database schema to accommodate the Course entity. The following properties will be defined:
- **Table**: courses
  - **Columns**:
    - `id`: INTEGER PRIMARY KEY AUTOINCREMENT (auto-incremented primary key)
    - `name`: TEXT NOT NULL (required field)
    - `level`: TEXT NOT NULL (required field)

#### Migration Strategy
- Use SQLAlchemy's migration tool (Flask-Migrate) to manage schema migrations, ensuring that existing Student records remain intact while adding the new Course table.

### 4.2 API Endpoints
1. **POST /courses**
   - **Purpose**: To create a new course record.
   - **Request Body**: 
     ```json
     {
       "name": "Mathematics 101",
       "level": "Beginner"
     }
     ```
   - **Response**:
     - **Success (201 Created)**:
       ```json
       {
         "id": 1,
         "name": "Mathematics 101",
         "level": "Beginner"
       }
       ```
     - **Error (400 Bad Request)**:
       ```json
       {
         "error": {
           "code": "E001",
           "message": "Name and level are required fields"
         }
       }
       ```

2. **GET /courses/{id}**
   - **Purpose**: To retrieve a course record by ID.
   - **Response**:
     - **Success (200 OK)**:
       ```json
       {
         "id": 1,
         "name": "Mathematics 101",
         "level": "Beginner"
       }
       ```
     - **Error (404 Not Found)**:
       ```json
       {
         "error": {
           "code": "E002",
           "message": "Course not found"
         }
       }
       ```

### 4.3 Functionality Implementation
- **Course Model**: Create a new SQLAlchemy model for the Course entity with the required fields and validation.
- **Routes and Controllers**: Implement Flask routes to handle course creation and retrieval, applying input validation through Marshmallow.

```python
# Example of New Model in models.py
class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    level = db.Column(db.String, nullable=False)

# Example in routes.py
@app.route('/courses', methods=['POST'])
def create_course():
    data = request.get_json()
    name = data.get("name")
    level = data.get("level")

    if not name or not level:
        return jsonify(error={'code': 'E001', 'message': 'Name and level are required fields'}), 400

    new_course = Course(name=name, level=level)
    db.session.add(new_course)
    db.session.commit()
    return jsonify(id=new_course.id, name=new_course.name, level=new_course.level), 201

@app.route('/courses/<int:id>', methods=['GET'])
def get_course(id):
    course = Course.query.get(id)
    if not course:
        return jsonify(error={'code': 'E002', 'message': 'Course not found'}), 404

    return jsonify(id=course.id, name=course.name, level=course.level), 200
```

### 4.4 Testing Strategy
- **Unit Tests**: Write unit tests for `Course` model and the API endpoints to ensure proper functionality for both creating and retrieving course records.
- **Integration Tests**: Check that the API correctly interacts with the updated database schema, ensuring that course records can be created and retrieved accurately.
- Test coverage should meet the following criteria:
  - 70%+ coverage for business logic involving courses.
  - 90%+ coverage for critical paths, especially for the creation and retrieval of courses.

## 5. Security Considerations
- Any input from users will be validated against SQL injection and XSS attacks.
- Ensure that user data and actions adhere to the principle of least privilege, although no authentication modifications are in scope.

## 6. Error Handling & Validation
- Implement input validation using Marshmallow to ensure that both the name and level fields are provided for course creation. 
- Return clear error messages for invalid requests, particularly for scenarios missing required fields.
- Log all errors (excluding sensitive data) for debugging and operational visibility.

## 7. Deployment Considerations
- The application will initially be tested in a local environment to validate the migration and new features.
- Ensure health checks are present and that the application initializes without errors post-migration.
- Document environment variables essential for local and production setups.

## 8. Documentation
- Update the API documentation to include details about the new `/courses` endpoints, illustrating expected request and response formats.
- Ensure the `README.md` file reflects setup instructions, how to run tests, and examples of using the API.

## 9. Technical Trade-offs
- Continuing with SQLite allows easy data management during the development phase while remaining lightweight and suitable for the current scope. As the application scales and the data grows, migration to a more robust database system may be evaluated.
- Using Python and Flask expedites development and iteration capabilities, enabling us to quickly build the feature set as required by the business specification.

## 10. Success Metrics
- Validate that the application starts without fatal errors and accurately reflects the new Course schema post-migration.
- Users should be able to create course records with valid data, retrieve existing course records, and see relevant error messages when submitting invalid data (missing fields).
- Confirm the migration does not affect existing functionality linked to the Student entity.

By following this implementation plan, we will effectively enhance the Student Management Web Application to integrate Course entity functionality while ensuring existing features remain operational.

Existing Code Files:
File: tests/test_api/test_course.py
```python
import pytest
from app import create_app, db
from app.models import Course
from http import HTTPStatus

@pytest.fixture
def client():
    app = create_app({'TESTING': True})
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Create schema for testing
            # Create a sample course for testing retrieval
            new_course = Course(name="Test Course", level="Advanced")
            db.session.add(new_course)
            db.session.commit()
        yield client

def test_create_course(client):
    response = client.post('/courses', json={"name": "Mathematics 101", "level": "Beginner"})
    assert response.status_code == HTTPStatus.CREATED
    assert response.json['name'] == "Mathematics 101"
    assert response.json['level'] == "Beginner"

def test_create_course_without_fields(client):
    response = client.post('/courses', json={"name": ""})
    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response.json['error']['code'] == 'E001'
```

File: tests/test_models/test_course.py
```python
import pytest
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.models import Course

# Setup Flask and SQLAlchemy for testing
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Create the database schema for testing
with app.app_context():
    db.create_all()

def test_create_course_valid():
    """Test successful creation of a course"""
    new_course = Course(name="Science 101", level="Intermediate")
    db.session.add(new_course)
    db.session.commit()
    assert new_course.id is not None
```

This implementation plan provides a comprehensive overview of how to construct and integrate the new Course entity into the existing system, ensuring all necessary details are covered while maintaining existing functionality.