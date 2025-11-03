# Implementation Plan: Add Teacher Relationship to Course Entity

---
## INCREMENTAL DEVELOPMENT CONTEXT

**Previous Sprint Plan**: 
# Implementation Plan: Create Teacher Entity

---
## INCREMENTAL DEVELOPMENT CONTEXT

**Previous Sprint Plan**: 
# Implementation Plan: Create Teacher Entity

**Version**: 1.0.0  
**Purpose**: To implement a feature that allows associating a Teacher entity with a Course entity within the application to streamline course management and facilitate better tracking of course assignments.  
**Scope**: This implementation focuses on updating the database schema, creating the necessary API endpoints for assigning teachers to courses, handling errors appropriately, and ensuring automated tests achieve adequate coverage.

---

## I. Architecture Overview

The application will continue to utilize the existing client-server architecture with the following enhancements:

- **Frontend**: The existing HTML/CSS will be updated to include forms for assigning teachers to courses.
- **Backend**: The RESTful API built using Flask will be modified to include a new endpoint for assigning teachers to courses.
- **Database**: SQLite will be updated to include a foreign key column in the `Course` table referencing `Teacher`.

---

## II. Technology Stack

- **Backend Framework**: Flask (Python)
- **Frontend Framework**: HTML/CSS with optional JavaScript
- **Database**: SQLite
- **ORM**: SQLAlchemy
- **Testing Framework**: pytest
- **Deployment**: Docker
- **Version Control**: Git

---

## III. Module Design

### 1. API Module - `api.py`
Responsibilities:
- Implement the new RESTful endpoint for assigning teachers to courses.

Endpoints:
- `PATCH /courses/{id}`: Assign a teacher to an existing course by updating the course record with a `teacher_id`.

### 2. Database Module - `models.py`
Responsibilities:
- Update the existing `Course` entity schema to include a foreign key reference to the `Teacher` table.

Entities:
- **Course**
  - `id`: integer, primary key, auto-increment
  - `name`: string, required
  - `teacher_id`: integer, optional, foreign key referencing `Teacher`

### 3. Error Handling Module - `errors.py`
Responsibilities:
- Centralize error handling for invalid course or teacher assignments.

### 4. Tests Module - `tests/test_api.py`
Responsibilities:
- Write tests to verify the functionalities surrounding course-teacher relationships and ensure at least 70% business logic coverage.

---

## IV. Data Models

### Updated Course Model
```python
class Course(Base):
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    teacher_id = Column(Integer, ForeignKey('teachers.id'))  # Relationship with Teacher
```

### Teacher Model (for reference)
```python
class Teacher(Base):
    __tablename__ = 'teachers'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
```

---

## V. API Contracts

### 1. Assign Teacher to Course
- **Request**:
  ```
  PATCH /courses/{id}
  Content-Type: application/json

  {
      "teacher_id": 1
  }
  ```

- **Response**:
  - **Success** (200 OK):
    ```json
    {
        "message": "Teacher assigned successfully",
        "course_id": 1,
        "teacher_id": 1
    }
    ```

  - **Error** (404 Not Found - Course):
    ```json
    {
        "error": {
            "code": "E001",
            "message": "Course does not exist."
        }
    }
    ```

  - **Error** (404 Not Found - Teacher):
    ```json
    {
        "error": {
            "code": "E002",
            "message": "Teacher does not exist."
        }
    }
    ```

---

## VI. Implementation Approach

1. **Update Project Structure**
   - Modify the existing `Course` model in `models.py` by adding the `teacher_id` foreign key.
   - Create a migration script to alter the `Course` table to add the `teacher_id` column.
   - Update existing `tests/test_api.py` to include tests for teacher assignment to courses.

2. **Backend Development**
   - Implement the API module logic for the `PATCH /courses/{id}` endpoint, validating inputs and ensuring correct error responses.

3. **Error Handling Implementation**
   - Implement centralized error handling in `errors.py` for cases where the specified `teacher_id` or `course_id` does not exist.

4. **Testing & Validation**
   - Write unit tests in `tests/test_api.py` to ensure functionality for assigning teachers to courses and achieving at least 70% coverage on associated business logic.

5. **Database Migration**
   - Utilize Flask-Migrate to create and apply a migration that modifies the `courses` table to include the `teacher_id` foreign key without affecting existing records for `Student`, `Course`, and `Teacher`.

6. **Deploy and Document**
   - Ensure that the Docker configuration is updated and tested with the new functionality.
   - Provide documentation updates in `README.md` for the new endpoint functionalities, including expected request and response formats.

---

## VII. Success Criteria

- The application can successfully assign a teacher to a course through the specified endpoint and return appropriate success messages in JSON format.
- The application correctly handles error cases for invalid course or teacher IDs, providing clear error messages for each scenario.
- Coverage for the teacher assignment functionality is at least 70% with automated tests.
- Verify that the database migration script correctly alters the `courses` table and preserves existing records for `Student`, `Course`, and `Teacher`.

---

## VIII. Trade-offs and Decisions

- **Adding a Foreign Key Relationship**: This strengthens the integrity of course and teacher associations but adds complexity in ensuring the integrity of the foreign key references.
- **Enhanced Error Handling**: Centralizing error responses keeps API responses consistent but may increase the size of the error handling modules if not effectively organized.

---

## IX. Documentation & Maintenance

- Update `README.md` with new API specifications for the `/courses/{id}` update endpoint, including request and response formats.
- Provide detailed docstrings for all new methods and update existing documentation to reflect changes in the API contracts.
- Include inline comments in the modified code sections to clarify integrations, particularly in the API module and error handling logic. 

This implementation plan provides a detailed approach to integrating teacher assignments into the course management functionality while ensuring that existing features and data remain intact.