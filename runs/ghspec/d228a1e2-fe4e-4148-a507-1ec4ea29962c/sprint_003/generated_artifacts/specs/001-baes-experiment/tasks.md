# Tasks: Create Course Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- `tests/api/test_student_api.py` (2969 bytes)

## Task Breakdown

### Task 1: Create Course Model
- **File**: `src/models/course.py`
- **Description**: Implement the Course model based on the specifications provided.
```python
from sqlalchemy import Column, Integer, String
from app import db

class Course(db.Model):
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    level = Column(String, nullable=False)
```
- [ ] Create the `course.py` file and implement the Course model.

### Task 2: Database Migration for Course Table
- **File**: `migrations/versions/xxxxxx_create_course_table.py` 
- **Description**: Write the migration script to create the Course table in the database, ensuring existing Student data remains intact.
```python
def upgrade():
    op.create_table(
        'courses',
        sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('level', sa.String(), nullable=False),
    )

def downgrade():
    op.drop_table('courses')
```
- [ ] Create and run the migration script to add the Course table.

### Task 3: Create Course API Endpoint
- **File**: `src/api/course_api.py`
- **Description**: Implement the POST `/courses` endpoint to allow for course creation.
```python
from flask import Blueprint, request, jsonify
from models.course import Course
from app import db

course_blueprint = Blueprint('course', __name__)

@course_blueprint.route('/courses', methods=['POST'])
def create_course():
    data = request.json
    if not data or 'name' not in data or 'level' not in data:
        return jsonify({"error": { "code": "E001", "message": "Name and level fields are required" }}), 400
    
    course = Course(name=data['name'], level=data['level'])
    db.session.add(course)
    db.session.commit()
    
    return jsonify({"id": course.id, "name": course.name, "level": course.level}), 201
```
- [ ] Create the `course_api.py` file and implement the create course endpoint logic.

### Task 4: Get Course API Endpoint
- **File**: `src/api/course_api.py`
- **Description**: Implement the GET `/courses/{id}` endpoint to retrieve course details.
```python
@course_blueprint.route('/courses/<int:id>', methods=['GET'])
def get_course(id):
    course = Course.query.get(id)
    if course is None:
        return jsonify({"error": { "code": "E002", "message": "Course not found" }}), 404
    return jsonify({"id": course.id, "name": course.name, "level": course.level}), 200
```
- [ ] Extend the `course_api.py` file to include the get course endpoint logic.

### Task 5: List Courses API Endpoint
- **File**: `src/api/course_api.py`
- **Description**: Implement the GET `/courses` endpoint to list all courses.
```python
@course_blueprint.route('/courses', methods=['GET'])
def list_courses():
    courses = Course.query.all()
    return jsonify([{"id": course.id, "name": course.name, "level": course.level} for course in courses]), 200
```
- [ ] Extend the `course_api.py` file to implement the list courses endpoint.

### Task 6: Test Cases for Course API
- **File**: `tests/api/test_course_api.py`
- **Description**: Write unit tests for course creation, retrieval, and listing functionalities.
```python
import pytest
from app import app, db

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client

def test_create_course(client):
    response = client.post('/courses', json={"name": "Introduction to Physics", "level": "Beginner"})
    assert response.status_code == 201

def test_get_course(client):
    response = client.post('/courses', json={"name": "Introduction to Physics", "level": "Beginner"})
    created_id = response.json['id']
    response = client.get(f'/courses/{created_id}')
    assert response.status_code == 200

def test_list_courses(client):
    client.post('/courses', json={"name": "Intro to Physics", "level": "Beginner"})
    response = client.get('/courses')
    assert response.status_code == 200
```
- [ ] Create and implement test cases in `test_course_api.py`.

### Task 7: Documentation Update
- **File**: `docs/api_documentation.md`
- **Description**: Update API documentation to include the endpoints for the Course entity.
- [ ] Add new endpoint descriptions for `/courses`, `/courses/{id}`, and details on request/response formats in the API documentation.

### Task 8: Error Handling Verification
- **File**: `src/api/course_api.py`
- **Description**: Ensure that all API endpoints handle errors properly and return appropriate messages.
- [ ] Review and refine error handling in all course-related API methods.

### Task 9: Logging Implementation
- **File**: `src/app.py`
- **Description**: Implement structured logging for course operations.
```python
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Example to log course creation
logger.info(f"Course created: {course.name}")
```
- [ ] Add logging functionality to track course operations and errors.

### Task 10: Deployment Considerations Review
- **File**: `deployment/deployment_plan.md`
- **Description**: Review and ensure that deployment processes are aligned with the new Course entity functionalities.
- [ ] Confirm that database migration, API endpoint changes, and documentation updates are included in the deployment plan.

--- 

This breakdown provides a clear list of tasks required to implement the Course entity, following the defined specifications and ensuring that the implementation is structured, testable, and maintains code consistency.