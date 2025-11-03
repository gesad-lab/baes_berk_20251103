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
# Implementation Plan: Student Management Web Application

**Version**: 1.1.0  
**Purpose**: Implement the ability to associate a Teacher with a Course within the Student Management system to enhance educational management capabilities.

---

## I. Architecture Overview

### 1.1 Architectural Style
- **Microservice architecture**: Continuing the design for modularity and independent deployment, focusing on appropriate management of Course and Teacher relationships.

### 1.2 Technology Stack
- **Backend Framework**: Flask (Python)
- **Database**: SQLite
- **Data Serialization**: Marshmallow (for JSON serialization and validation)
- **Environment Configuration**: python-dotenv (for managing configuration)
- **Testing Framework**: pytest

## II. Module Boundaries and Responsibilities

### 2.1 Application Structure
```
student_management/
├── src/
│   ├── app.py              # Main application entry point
│   ├── models.py           # Database models (Update for Course-Teacher relationship)
│   ├── schemas.py          # Marshmallow schemas for serialization (Update for Course schema)
│   ├── routes.py           # API routes for handling requests (Update for Course and Teacher routes)
│   ├── config.py           # Configuration management
│   └── db.py               # Database initialization and schema handling (for migrations)
├── tests/
│   ├── test_routes.py      # Tests for API routes (Update for API functionality)
│   └── test_validation.py   # Tests for input validation (Update for new validations)
├── .env.example             # Example environment configuration
└── README.md                # Project documentation
```

### 2.2 Responsibilities
- **app.py**: Introduce any necessary imports for new routes and schema validation.
- **models.py**: Update the existing `Course` model to include the `teacher_id` foreign key.
- **schemas.py**: Update the Marshmallow schema for `Course` to manage serialization including Teacher data.
- **routes.py**: Implement API endpoints for assigning a Teacher to a Course.
- **config.py**: No modifications required.
- **db.py**: Handle migrations for adding the `teacher_id` column to the `courses` table.

## III. Data Models and API Contracts

### 3.1 Data Model
#### Updated Model
```python
class Course(db.Model):
    __tablename__ = 'courses'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    teacher_id = db.Column(db.Integer, db.ForeignKey('teachers.id'), nullable=True)
    teacher = db.relationship('Teacher', backref='courses')  # Sets up the relationship with the Teacher
```

### 3.2 API Endpoints
#### Assign Teacher to Course
- **Endpoint**: `POST /courses/{course_id}/assign-teacher`
- **Request Body**:
    ```json
    {
      "teacher_id": 1  // Required identifier of the Teacher
    }
    ```
- **Response** (Success):
    ```json
    {
      "id": 1,
      "name": "Introduction to Programming",
      "teacher_id": 1,
      "teacher": {
        "id": 1,
        "name": "John Doe",
        "email": "john.doe@example.com"
      }
    }
    ```
- **Response** (Error - Invalid IDs):
    ```json
    {
      "error": {
        "code": "E001",
        "message": "Invalid Course ID or Teacher ID."
      }
    }
    ```

#### Retrieve Course with Teacher
- **Endpoint**: `GET /courses/{course_id}`
- **Response** (Success):
    ```json
    {
      "id": 1,
      "name": "Introduction to Programming",
      "teacher": {
        "id": 1,
        "name": "John Doe",
        "email": "john.doe@example.com"
      }
    }
    ```
- **Response** (Error - Not Found):
    ```json
    {
      "error": {
        "code": "E002",
        "message": "Course not found."
      }
    }
    ```

## IV. Implementation Steps

### 4.1 Development Setup
1. **Environment Setup**:
   - Ensure Python 3.11+ is installed.
   - Update virtual environment and install necessary dependencies:
     ```bash
     source venv/bin/activate
     pip install -U Flask Marshmallow python-dotenv pytest
     ```

### 4.2 Core Functionality
1. **Update Data Model in `models.py`**
   - Modify the `Course` class to include the `teacher_id` attribute and establish a relationship to the `Teacher` model.

2. **Set Up Marshmallow Schemas in `schemas.py`**
   - Update the existing `CourseSchema` to include the `teacher` field for serialization, reflecting the Teacher associated with a Course.
   ```python
   class CourseSchema(Schema):
       ...
       teacher = fields.Nested(TeacherSchema(only=('id', 'name', 'email')))
   ```

3. **Update API Endpoints in `routes.py`**
   - Implement:
     - `POST /courses/{course_id}/assign-teacher` to assign a Teacher to the specified Course.
     - `GET /courses/{course_id}` to retrieve a Course's details, including Teacher data.

4. **Update Database Schema in `db.py`**
   - Create a migration script that modifies the `courses` table to add the `teacher_id` column as a foreign key.
   ```sql
   ALTER TABLE courses ADD COLUMN teacher_id INTEGER REFERENCES teachers(id);
   ```

### 4.3 Validation and Error Handling
- Implement validation logic to check if provided Course and Teacher IDs are valid.
- Return informative error messages for invalid or non-existent IDs.

### 4.4 Testing
1. **Unit Tests for Validation**:
   - Extend `test_validation.py` with new test cases covering edge cases for assigning Teachers to Courses.

2. **Integration Tests for API Endpoints**:
   - Add tests in `test_routes.py` to validate the assignment of Teachers to Courses and retrieval of Courses with Teacher details.

## V. Documentation and Deployment

### 5.1 Documentation
- Update `README.md` to reflect changes in API functionalities related to Course-Teacher relationships, along with usage examples.

### 5.2 Deployment Considerations
- Test migration scripts thoroughly in a staging environment to ensure integrity and correct relationships between existing Courses and Teachers before deploying updates to production.

## VI. Success Criteria
1. The application can successfully assign a Teacher to a Course when valid IDs are provided.
2. Correct retrieval of a Course's details including Teacher information in JSON format.
3. Appropriate handling and messages for invalid Course or Teacher IDs.

## VII. Trade-offs and Considerations
- **Backward Compatibility**: The addition of `teacher_id` should not interfere with existing data or functionality; the migration needs to be tested thoroughly.
- **Input Validations**: Striving to ensure user-friendly error handling without compromising on the robustness of error reporting.

## Final Notes
This plan outlines a detailed integration process to manage online Course and Teacher relationships, ensuring we maintain the system's data integrity and enhance overall management capabilities within the Student Management context. This structured approach guarantees that the integrations are seamless while adhering to existing code practices.

### Existing Code Files Adjustments
#### File: `src/models.py`
```python
class Course(db.Model):
    __tablename__ = 'courses'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    teacher_id = db.Column(db.Integer, db.ForeignKey('teachers.id'), nullable=True)  # New relationship added
    teacher = db.relationship('Teacher', backref='courses')  # Sets up the relationship
```

#### File: `src/schemas.py`
```python
class CourseSchema(Schema):
    id = fields.Int()
    name = fields.String(required=True)
    teacher = fields.Nested(TeacherSchema(only=('id', 'name', 'email')))  # Add Teacher details in serialization
```

#### File: `src/routes.py`
```python
from flask import request, jsonify
# Add routes for assigning a teacher and retrieving course details
@app.route('/courses/<int:course_id>/assign-teacher', methods=['POST'])
def assign_teacher(course_id):
    ...
    # Implement assignment logic and response handling
```

#### File: `src/db.py`
```python
def upgrade():
    # Use migrations to add the `teacher_id` column to the `courses` table
    op.add_column('courses', sa.Column('teacher_id', sa.Integer(), sa.ForeignKey('teachers.id'), nullable=True))
```

#### File: `tests/test_routes.py`
```python
def test_assign_teacher_to_course(client):
    """Test assigning a teacher to a course."""
    response = client.post('/courses/1/assign-teacher', data=json.dumps({
        'teacher_id': 1
    }), content_type='application/json')
    assert response.status_code == 200  # Verify success status
    assert response.get_json()['teacher']['id'] == 1  # Verify teacher association
```

#### File: `tests/test_validation.py`
```python
def test_assign_teacher_validation(client):
    """Test validation logic for assigning a teacher."""
    response = client.post('/courses/999/assign-teacher', data=json.dumps({'teacher_id': 1}), content_type='application/json')
    assert response.status_code == 404  # Verify not-found status for invalid course
```

This plan facilitates adding a Teacher relationship to the Course entity while ensuring comprehensive testing and validation to enhance the educational management system's usability.