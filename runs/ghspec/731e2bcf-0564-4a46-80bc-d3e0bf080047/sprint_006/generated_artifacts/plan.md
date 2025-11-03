# Implementation Plan: Add Teacher Relationship to Course Entity

---
## INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Create Teacher Entity

---

## Version: 1.0.0  
**Purpose**: To establish a relationship between the Course entity and the Teacher entity within the educational system, allowing for better tracking of course ownership and accountability.

---

## I. Architecture Overview

### 1.1 Architecture Style
- RESTful API architecture will be employed to manage the Course-Teacher relationship, with updates and retrieval capabilities implemented via dedicated endpoints.

### 1.2 Technology Stack
- **Backend Framework**: Flask (Python)
- **Database**: SQLite for local data storage
- **API Framework**: Flask-RESTful for constructing RESTful APIs
- **Testing Framework**: pytest for unit and integration testing
- **Deployment**: Docker for containerization to ensure easy deployment

## II. Module Breakdown

### 2.1 Module Responsibilities

#### 2.1.1 API Module
- Implement endpoints to assign a teacher to a course and to retrieve course information along with teacher details.

#### 2.1.2 Database Module
- Modify the Course table in the existing database schema to include a foreign key reference to the Teacher entity.

#### 2.1.3 Error Handling and Validation Module
- Implement validation to ensure correct assignments of teachers and retrieval of course information while providing clear error messages.

---

## III. Data Model

### 3.1 Entity Definitions
- **Course**: 
  - Updates needed to include:
    - `teacher_id`: Integer, optional foreign key referencing the Teacher entity.
  
### 3.2 Database Schema Changes
```sql
ALTER TABLE courses ADD COLUMN teacher_id INTEGER REFERENCES teachers(id);
```

---

## IV. API Endpoints

### 4.1 Endpoint Definitions

#### 4.1.1 Assign Teacher to Course
- **Endpoint**: `PUT /courses/{course_id}/assign-teacher`
- **Request Body**:
  ```json
  {
      "teacher_id": 1
  }
  ```
- **Responses**:
  - **200 OK**: Successfully assigned the teacher.
  ```json
  {
      "message": "Teacher assigned successfully.",
      "course": {
          "id": 1,
          "name": "Mathematics 101",
          "level": "Beginner",
          "teacher_id": 1
      }
  }
  ```
  - **400 Bad Request** (if course does not exist or teacher ID is invalid):
  ```json
  {
      "error": {
          "code": "E001",
          "message": "Invalid course ID or teacher ID."
      }
  }
  ```

#### 4.1.2 Retrieve Course Information
- **Endpoint**: `GET /courses/{course_id}`
- **Responses**:
  - **200 OK**:
  ```json
  {
      "id": 1,
      "name": "Mathematics 101",
      "level": "Beginner",
      "teacher": {
          "id": 1,
          "name": "John Doe",
          "email": "john.doe@example.com"
      }
  }
  ```
  - **404 Not Found** (if course does not exist):
  ```json
  {
      "error": {
          "code": "E002",
          "message": "Course not found."
      }
  }
  ```

---

## V. Implementation Approach

### 5.1 Environment Setup
- Utilize the existing Docker setup to maintain consistency across environments.

### 5.2 Development Phases
1. **Phase 1**: Modify the Course model to incorporate the `teacher_id` foreign key and execute the SQL migration to update the existing table.
2. **Phase 2**: Implement the `PUT /courses/{course_id}/assign-teacher` API endpoint to handle teacher assignment requests.
3. **Phase 3**: Implement the `GET /courses/{course_id}` API endpoint for retrieving course details, including associated teacher information.
4. **Phase 4**: Integrate error handling for scenarios when courses or teachers do not exist.
5. **Phase 5**: Write unit tests using pytest focused on the new functionalities for course-teacher assignment and retrieval.
6. **Phase 6**: Test the schema migration strategy to ensure seamless integration without data loss.

## VI. Testing Strategy

### 6.1 Test Coverage Goals
- Aim for at least 70% coverage of the newly added functionalities.
- Target 90% coverage for critical paths (assigning teachers and retrieving courses).

### 6.2 Test Types
- **Unit tests**: Validate correct operation of the API for course-teacher relationships.
- **Integration tests**: Ensure proper operation and responses through the new API endpoints.

### 6.3 Test Organization
- Organize tests in a structure similar to previous projects:
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
- Validate the presence of `teacher_id` in requests to assign a teacher, ensuring the associated course exists.

### 7.2 Exception Handling
- Implement logging for critical errors, ensuring sensitive details remain hidden from end-users.

---

## VIII. Deployment Considerations

### 8.1 Production Readiness
- Make sure the application starts without manual intervention and includes a health check endpoint for monitoring.

### 8.2 Database Migration Strategy
- Use Flask-Migrate to create a migration to add the `teacher_id` field to the existing courses table.

---

## IX. Logging & Monitoring

### 9.1 Logging Strategy
- Implement structured logging for all API interactions related to the course-teacher relationship.

---

## X. Success Criteria
- The application can successfully assign a teacher to a course through the `PUT /courses/{course_id}/assign-teacher` endpoint, returning the correct response and status code.
- The `GET /courses/{course_id}` endpoint should return accurate course information or a relevant 404 status code if the course does not exist.

---

## XI. Technical Trade-Offs and Decisions

- **SQLite** is maintained as the database due to its continued compatibility with existing data models.
- **Flask RESTful** will be used to extend the existing architecture, maintaining the lightweight API structure while adding new features.

---

## XII. Conclusion
This implementation plan provides a structured approach to integrating the Teacher relationship into Courses, thereby enhancing accountability in the educational system.

### Existing Code Files Modifications:
- **src/models/course.py**: Update the Course model to include `teacher_id`.
- **src/controllers/course_controller.py**: Implement logic for newly defined endpoints.
- **tests/test_course_controller.py**: Create test cases for course-teacher relationship functionality.

### Database Migration Strategy:
- Utilize Flask-Migrate to manage the migration for adding the `teacher_id` to the courses table.
  
#### Migration Example
```python
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from src.app import app, db

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

@db.Migrate.before_upgrade
def before_upgrade():
    with db.session.begin():
        db.session.execute('ALTER TABLE courses ADD COLUMN teacher_id INTEGER REFERENCES teachers(id);')

if __name__ == '__main__':
    manager.run()
```

### Existing Code Files:
File: `src/models/course.py`
```python
from src.app import db

class Course(db.Model):
    __tablename__ = 'courses'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    level = db.Column(db.String, nullable=False)
    teacher_id = db.Column(db.Integer, db.ForeignKey('teachers.id'), nullable=True)
```

File: `src/controllers/course_controller.py`
```python
from flask import request, jsonify
from src.models.course import Course
from src.models.teacher import Teacher
from src.app import db

@app.route('/courses/<int:course_id>/assign-teacher', methods=['PUT'])
def assign_teacher(course_id):
    course = Course.query.get(course_id)
    if not course:
        return jsonify({"error": {"code": "E001", "message": "Invalid course ID."}}), 400

    data = request.json
    teacher_id = data.get('teacher_id')

    if not Teacher.query.get(teacher_id):
        return jsonify({"error": {"code": "E001", "message": "Invalid teacher ID."}}), 400

    course.teacher_id = teacher_id
    db.session.commit()

    return jsonify({
        "message": "Teacher assigned successfully.",
        "course": {
            "id": course.id,
            "name": course.name,
            "level": course.level,
            "teacher_id": course.teacher_id
        }
    }), 200

@app.route('/courses/<int:course_id>', methods=['GET'])
def get_course(course_id):
    course = Course.query.get(course_id)
    if not course:
        return jsonify({"error": {"code": "E002", "message": "Course not found."}}), 404

    teacher = Teacher.query.get(course.teacher_id) if course.teacher_id else None

    response = {
        "id": course.id,
        "name": course.name,
        "level": course.level
    }

    if teacher:
        response["teacher"] = {
            "id": teacher.id,
            "name": teacher.name,
            "email": teacher.email
        }

    return jsonify(response), 200
```

File: `tests/test_course_controller.py`
```python
import pytest
from flask import json
from src.app import create_app, db
from src.models.course import Course
from src.models.teacher import Teacher

@pytest.fixture
def app():
    app = create_app({'TESTING': True})

    with app.app_context():
        db.create_all()
        # Create a sample Teacher
        teacher = Teacher(name="John Doe", email="john.doe@example.com")
        db.session.add(teacher)
        db.session.commit()
        yield app
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

def test_assign_teacher_to_course(client):
    # Setup: Create Course
    course = Course(name="Mathematics 101", level="Beginner")
    db.session.add(course)
    db.session.commit()

    response = client.put(f'/courses/{course.id}/assign-teacher', json={"teacher_id": 1})
    assert response.status_code == 200
    assert response.get_json()['course']['teacher_id'] == 1

def test_get_course_with_teacher(client):
    # Setup: Create Course and assign Teacher
    course = Course(name="Science 101", level="Beginner")
    db.session.add(course)
    db.session.commit()
    
    response = client.put(f'/courses/{course.id}/assign-teacher', json={"teacher_id": 1})
    
    response = client.get(f'/courses/{course.id}')
    assert response.status_code == 200
    assert 'teacher' in response.get_json()

def test_assign_teacher_invalid_course(client):
    response = client.put('/courses/999/assign-teacher', json={"teacher_id": 1})
    assert response.status_code == 400
    assert response.get_json()['error']['code'] == "E001"

def test_get_nonexistent_course(client):
    response = client.get('/courses/999')
    assert response.status_code == 404
    assert response.get_json()['error']['code'] == "E002"
```

This detailed implementation plan highlights the necessary steps to integrate the Teacher relationship into the Course entity with a focus on maintainability, scalability, and backward compatibility. All modifications and new features have been designed to align with the existing architecture and tech stack.