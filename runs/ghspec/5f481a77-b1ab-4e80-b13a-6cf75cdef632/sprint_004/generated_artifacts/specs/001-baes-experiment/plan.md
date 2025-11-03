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
**Purpose**: Establish a many-to-many relationship between Students and Courses within the Student Management system to enhance academic tracking capabilities.

---

## I. Architecture Overview

### 1.1 Architectural Style
- **Microservice architecture**: Continuing with the microservice pattern for better modularity and independent deployment opportunities, focusing on the Course and Student entities.

### 1.2 Technology Stack
- **Backend Framework**: Flask (Python)
- **Database**: SQLite
- **Data Serialization**: Marshmallow (for JSON serialization)
- **Environment Configuration**: python-dotenv (for managing configuration)
- **Testing Framework**: pytest

## II. Module Boundaries and Responsibilities

### 2.1 Application Structure
```
student_management/
├── src/
│   ├── app.py              # Main application entry point
│   ├── models.py           # Database models (add StudentCourse relationship)
│   ├── schemas.py          # Marshmallow schemas for serialization (add StudentCourse schema)
│   ├── routes.py           # API routes for handling requests (add course relationship routes)
│   ├── config.py           # Configuration management
│   └── db.py               # Database initialization and schema handling
├── tests/
│   ├── test_routes.py      # Tests for API routes (add tests for relationships)
│   └── test_validation.py   # Tests for input validation (add tests for relationship validation)
├── .env.example             # Example environment configuration
└── README.md                # Project documentation
```

### 2.2 Responsibilities
- **app.py**: No modifications required.
- **models.py**: Add a `StudentCourse` join model to create the relation between Students and Courses.
- **schemas.py**: Add a Marshmallow schema for StudentCourse to manage serialization and validation.
- **routes.py**: Implement API endpoints for adding, retrieving, and removing courses related to a Student.
- **config.py**: No modifications required.
- **db.py**: Update SQLite database schema to include the `student_courses` join table.

## III. Data Models and API Contracts

### 3.1 Data Model
#### New Models
```python
class StudentCourse(db.Model):
    __tablename__ = 'student_courses'
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'), primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'), primary_key=True)
```
#### Updated Course and Student
- Existing `Student` and `Course` models remain unchanged.

### 3.2 API Endpoints
#### Add Course to Student
- **Endpoint**: `POST /students/{student_id}/courses`
- **Request Body**:
    ```json
    {
      "course_id": "1"
    }
    ```
- **Response** (Success):
    ```json
    {
      "message": "Course associated with student successfully."
    }
    ```
- **Response** (Error - Course Not Found):
    ```json
    {
      "error": {
        "code": "E001",
        "message": "Invalid course id provided."
      }
    }
    ```

#### Retrieve Student Courses
- **Endpoint**: `GET /students/{student_id}/courses`
- **Response** (Success):
    ```json
    {
      "courses": [
        {
          "id": 1,
          "name": "Introduction to Programming",
          "level": "Beginner"
        }
      ]
    }
    ```

#### Remove Course from Student
- **Endpoint**: `DELETE /students/{student_id}/courses/{course_id}`
- **Response** (Success):
    ```json
    {
      "message": "Course removed from student successfully."
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
   - Add the `StudentCourse` class to represent the relationship between Students and Courses.
   ```python
   class StudentCourse(db.Model):
       ...
   ```

2. **Set Up Marshmallow Schemas in `schemas.py`**
   - Create a new schema for `StudentCourse` for serialization.
   ```python
   class StudentCourseSchema(Schema):
       student_id = fields.Int(required=True)
       course_id = fields.Int(required=True)
   ```

3. **Create API Endpoints in `routes.py`**
   - Implement:
     - `POST /students/{student_id}/courses` to associate course with a student.
     - `GET /students/{student_id}/courses` to retrieve all courses for a student.
     - `DELETE /students/{student_id}/courses/{course_id}` to disassociate a course from a student.

4. **Update Database Schema in `db.py`**
   - Create a migration script for the SQLite database to add the `student_courses` join table.
   ```sql
   CREATE TABLE student_courses (
       student_id INTEGER,
       course_id INTEGER,
       PRIMARY KEY(student_id, course_id),
       FOREIGN KEY(student_id) REFERENCES students(id),
       FOREIGN KEY(course_id) REFERENCES courses(id)
   );
   ```

### 4.3 Validation and Error Handling
- Implement input validation for detecting invalid course associations. Ensure to return appropriate error messages.

### 4.4 Testing
1. **Unit Tests for Validation and Logic**:
   - Extend `test_validation.py` with tests for the new course association validation.

2. **Integration Tests for API Endpoints**:
   - Add tests in `test_routes.py` to validate the new endpoints regarding course associations.

## V. Documentation and Deployment

### 5.1 Documentation
- Update the `README.md` to include the new API functionality and example responses, ensuring clarity on the new features.

### 5.2 Deployment Considerations
- Test the migration process thoroughly on a staging environment before promoting changes to the production environment.

## VI. Success Criteria
1. Success in associating a Course to a Student when valid identifiers are provided.
2. Correct retrieval of a Student's enrolled Courses in JSON format.
3. Accurate error handling for invalid associations.

## VII. Trade-offs and Considerations
- **Database Migration**: Ensuring referential integrity during migration while keeping current data intact.
- **Complexity in Validation Logic**: Ensuring proper handling of multiple edge cases for student-course associations without compromising user experience.

## Final Notes
This comprehensive plan will streamline the integration of course relationships into the Student Management system while upholding current functionality and data integrity standards. By following the outlined steps, we will ensure efficient development, testing, and deployment. 

Existing Code Files Adjustments:
File: tests/test_routes.py
```python
...

def test_associate_course_to_student(client):
    """Test associating a course with a student."""
    response = client.post('/students/1/courses', data=json.dumps({
        'course_id': '1'
    }), content_type='application/json')
    
    assert response.status_code == 200  # Verify the operation was successful

...

def test_remove_course_from_student(client):
    """Test removing a course from a student's enrollments."""
    response = client.delete('/students/1/courses/1')
    assert response.status_code == 200  # Verify the course was removed
```

File: tests/test_validation.py
```python
...

def test_invalid_course_association(client):
    """Test error handling for associating a nonexistent course."""
    response = client.post('/students/1/courses', data=json.dumps({
        'course_id': '9999'  # Non-existent course ID
    }), content_type='application/json')
    assert response.status_code == 400
    ...
```

This plan delivers necessary modifications to enhance functionality while maintaining system integrity and user experience.