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
# Implementation Plan: Student Management Web Application

## Version: 1.0.0  
**Purpose**: To establish a relationship between the Student and Course entities, enhancing the educational platform's tracking of student course enrollments.

---

## I. Architecture Overview

### 1.1 Architecture Style
- RESTful API architecture to manage the association of courses with students.

### 1.2 Technology Stack
- **Backend Framework**: Flask (Python)
- **Database**: SQLite for local data storage
- **API Framework**: Flask-RESTful for constructing RESTful APIs
- **Testing Framework**: pytest for unit and integration testing
- **Deployment**: Docker for containerization to ensure easy deployment

## II. Module Breakdown

### 2.1 Module Responsibilities

#### 2.1.1 API Module
- Implement endpoints for assigning courses to students and retrieving student details with associated courses.

#### 2.1.2 Database Module
- Update the existing Student table schema to establish a one-to-many relationship with the Course table, ensuring referential integrity.

#### 2.1.3 Error Handling and Validation Module
- Implement input validation for student and course assignments to ensure integrity of data.

---

## III. Data Model

### 3.1 Entity Definition
- **Student**:
  - `id`: Integer, auto-incremented primary key
  - `name`: String, required
  - `courses`: List of course IDs associated with the student (add this mapping as a foreign key)

### 3.2 Database Schema
```sql
ALTER TABLE students ADD COLUMN course_ids TEXT; -- To store enrolled course IDs as a comma-separated string for simplicity (or use a many-to-many mapping table if relational integrity is critical)
```

---

## IV. API Endpoints

### 4.1 Endpoint Definitions

#### 4.1.1 Assign Courses to Student
- **Endpoint**: `POST /students/{student_id}/courses`
- **Request Body**:
  ```json
  {
      "course_ids": [1, 2, 3]  // List of course IDs to associate with the student
  }
  ```
- **Responses**:
  - **200 OK**:
  ```json
  {
      "message": "Courses assigned successfully.",
      "student": {
          "id": 1,
          "name": "John Doe",
          "course_ids": [1, 2, 3] // updated course IDs
      }
  }
  ```
  - **400 Bad Request** (if invalid course ID):
  ```json
  {
      "error": {
          "code": "E001",
          "message": "One or more course IDs are invalid."
      }
  }
  ```

#### 4.1.2 Retrieve Student Information with Courses
- **Endpoint**: `GET /students/{student_id}`
- **Responses**:
  - **200 OK**:
  ```json
  {
      "id": 1,
      "name": "John Doe",
      "course_ids": [1, 2, 3] // present course IDs if assigned
  }
  ```
  - **404 Not Found** (if student does not exist):
  ```json
  {
      "error": {
          "code": "E002",
          "message": "Student not found."
      }
  }
  ```

---

## V. Implementation Approach

### 5.1 Environment Setup
- Maintain the existing Docker container setup used in previous sprints to ensure consistency across environments.

### 5.2 Development Phases
1. **Phase 1**: Update the Flask application to include logic for course assignments.
2. **Phase 2**: Modify the SQLite database schema to support the course relationship through an alteration in the Student table.
3. **Phase 3**: Develop new API endpoints to handle course assignments and retrieval of student information with linked courses.
4. **Phase 4**: Integrate error handling and validation mechanisms for assignments, ensuring accurate responses.
5. **Phase 5**: Write unit tests using pytest, focusing on the functionality of the new endpoints.
6. **Phase 6**: Test database migration strategy to confirm successful integration with existing schema.

## VI. Testing Strategy

### 6.1 Test Coverage Goals
- Aim for 70% coverage of the added functionality.
- Target 90% coverage of critical paths (student enrollment in courses).

### 6.2 Test Types
- **Unit tests**: Validate correct operation of the API for assigning and retrieving courses for students.
- **Integration tests**: Ensure proper data flow and responses through the new API endpoints.

### 6.3 Test Organization
- Organize tests in a similar structure to the existing project:
```
- src/
  - app.py
  - models/
    - student.py
  - controllers/
    - student_controller.py
- tests/
  - test_student_controller.py
```

---

## VII. Error Handling

### 7.1 Input Validation
- Validate course IDs and student ID during course assignments, returning appropriate error messages for invalid inputs.

### 7.2 Exception Handling
- Implement logging for errors related to course assignments, ensuring sensitive details are hidden from the end-users.

---

## VIII. Deployment Considerations

### 8.1 Production Readiness
- Ensure the application can start without manual intervention and incorporates a health endpoint for monitoring.

### 8.2 Configuration Management
- Use environment variables for sensitive configuration data to prevent hardcoding of credentials.

---

## IX. Logging & Monitoring

### 9.1 Logging Strategy
- Implement structured logging for all API interactions related to student course assignments and retrievals.

---

## X. Success Criteria
- The application can successfully assign courses to students, displaying accurate updates upon retrieval.
- The `POST /students/{student_id}/courses` endpoint should return a 200 status code and confirm successful assignments.
- The `GET /students/{student_id}` endpoint should return the correct student details, including an array of their course IDs.

---

## XI. Technical Trade-Offs and Decisions

- **SQLite** will continue to be the database of choice due to its ease of use and minimal setup requirements, while balancing functionality.
- **Flask RESTful** supports lightweight REST APIs effectively, which is suitable for this application's needs.
- The **course relationship** with students will be managed through a simple foreign key linkage in the Student table instead of creating a complex relational mapping for immediate development simplicity.

---

## XII. Conclusion
This implementation plan provides guidance on incorporating the relationship between students and courses within the application. This structured approach ensures that new functionalities are developed while adhering to existing best practices for maintainability and integrity.

### Existing Code Files Modifications:
- **src/models/student.py**: Update to map course IDs as a comma-separated string or metadata based on evolving requirements.
- **src/controllers/student_controller.py**: Build the logic for the new endpoints to assign courses and retrieve student information.
- **tests/test_student_controller.py**: Write tests that validate the API functionality for course assignments.

### Database Migration Strategy:
- Utilize Flask-Migrate to update the Student table schema and include appropriate data migration scripts to add the `course_ids` field, while backing up existing data to prevent data loss.

### Existing Code Files:
File: src/models/student.py
```python
class Student(db.Model):
    __tablename__ = 'students'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    course_ids = db.Column(db.Text, nullable=True)  # New field to hold course IDs as a string
```

File: src/controllers/student_controller.py
```python
from flask import request, jsonify
from src.models.student import Student
from src.models.course import Course

@app.route('/students/<int:student_id>/courses', methods=['POST'])
def assign_courses_to_student(student_id):
    data = request.json
    course_ids = data.get('course_ids', [])

    student = Student.query.get(student_id)
    if not student:
        return jsonify({"error": {"code": "E002", "message": "Student not found."}}), 404

    invalid_courses = [course_id for course_id in course_ids if not Course.query.get(course_id)]
    if invalid_courses:
        return jsonify({"error": {"code": "E001", "message": "One or more course IDs are invalid."}}), 400

    student.course_ids = ",".join(map(str, course_ids))
    db.session.commit()

    return jsonify({
        "message": "Courses assigned successfully.",
        "student": {
            "id": student.id,
            "name": student.name,
            "course_ids": course_ids
        }
    }), 200

@app.route('/students/<int:student_id>', methods=['GET'])
def get_student_info(student_id):
    student = Student.query.get(student_id)
    if not student:
        return jsonify({"error": {"code": "E002", "message": "Student not found."}}), 404

    course_ids = list(map(int, student.course_ids.split(','))) if student.course_ids else []
    return jsonify({
        "id": student.id,
        "name": student.name,
        "course_ids": course_ids
    }), 200
```

File: tests/test_student_controller.py
```python
import pytest
from flask import json
from src.app import create_app, db
from src.models.student import Student
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

def test_assign_courses_to_student(client):
    student = Student(name="John Doe")
    db.session.add(student)
    db.session.commit()

    course1 = Course(name="Math 101", level="Undergraduate")
    db.session.add(course1)
    db.session.commit()

    response = client.post(f'/students/{student.id}/courses', json={"course_ids": [course1.id]})
    assert response.status_code == 200
    assert response.get_json()['student']['course_ids'] == [course1.id]

def test_get_student_with_courses(client):
    student = Student(name="John Doe", course_ids="1,2")
    db.session.add(student)
    db.session.commit()

    response = client.get(f'/students/{student.id}')
    assert response.status_code == 200
    assert response.get_json()['course_ids'] == [1, 2]

def test_assign_courses_invalid_student(client):
    response = client.post('/students/999/courses', json={"course_ids": [1]})
    assert response.status_code == 404
    assert response.get_json()['error']['code'] == "E002"

def test_assign_courses_invalid_courses(client):
    student = Student(name="John Doe")
    db.session.add(student)
    db.session.commit()

    response = client.post(f'/students/{student.id}/courses', json={"course_ids": [999]})
    assert response.status_code == 400
    assert response.get_json()['error']['code'] == "E001"
```

This implementation plan comprehensively addresses the integration of the course relationship with student entities while ensuring adherence to the established technology stack and best practices for maintainability and scalability.