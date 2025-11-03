# Implementation Plan: Add Teacher Relationship to Course Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Create Teacher Entity

---

## 1. Technical Architecture

### 1.1 Overview
This implementation plan focuses on establishing a relationship between the existing Course entity and the newly created Teacher entity within the educational management system. The architecture continues to follow a microservices model, maintaining separation across the API layer, service layer, and data layer. This will enable the system to facilitate dynamic course assignments for teachers without disrupting existing functionalities.

### 1.2 Components
- **API Layer**: New endpoints for assigning a teacher to a course and retrieving course details including the assigned teacher.
- **Service Layer**: Business logic to handle teacher-course relationships, ensuring proper validation.
- **Data Layer**: Updates to the existing Course table to include a foreign key reference to the Teacher entity, preserving the integrity of existing data related to Students and Courses.

## 2. Technology Stack

### 2.1 Programming Language
- **Python**: Continues as the chosen programming language.

### 2.2 Framework
- **Flask**: Continues to be used for building new endpoints that handle teacher-course assignments.

### 2.3 Database
- **SQLite**: The existing choice, updated to incorporate the foreign key in the Course table.

### 2.4 Dependencies
- **Flask-RESTful**: For building REST APIs.
- **Flask-SQLAlchemy**: Continues to be used for ORM capabilities in managing database interactions.
- **Marshmallow**: For data serialization and validation.

## 3. Module Boundaries and Responsibilities

### 3.1 API Module
- **New Endpoints**:
  - `POST /courses/<course_id>/assign_teacher`: Assign a teacher to a specific course.
  - `GET /courses/<course_id>`: Retrieve detailed information about a course, including the assigned teacher.

### 3.2 Service Module
- **New Functions**:
  - `assign_teacher_to_course(course_id: int, teacher_id: int) -> dict`: Handles the assignment of a teacher to a course.
  - `get_course_details(course_id: int) -> dict`: Fetches course details along with the assigned teacher's information.

### 3.3 Data Access Module
- **Updated Model**:
  - Update the existing `Course` model to include a `teacher_id` field, establishing the foreign key relationship.

## 4. Data Models

### 4.1 Course Model Update
```python
class Course(db.Model):
    __tablename__ = 'courses'
    id = db.Column(db.Integer, primary_key=True)
    teacher_id = db.Column(db.Integer, db.ForeignKey('teachers.id'))  # New foreign key
    # Other existing fields...
```

## 5. API Contracts

### 5.1 Request/Response Format

#### 5.1.1 Assign Teacher to Course
- **Request**:
    - Method: `POST`
    - URL: `/courses/<course_id>/assign_teacher`
    - Body: `{ "teacher_id": 1 }`
- **Response**:
    - Status: `200 OK`
    - Body: `{ "message": "Teacher assigned to course successfully", "course_id": 1, "teacher_id": 1 }`

#### 5.1.2 Retrieve Course Details
- **Request**:
    - Method: `GET`
    - URL: `/courses/<course_id>`
- **Response**:
    - Status: `200 OK`
    - Body: `{ "id": 1, "teacher_id": 1, "teacher": { "id": 1, "name": "John Doe" }, ... }`

### 5.1.3 Error Handling for Invalid Assignments
- **Request**:
    - Method: `POST`
    - URL: `/courses/<course_id>/assign_teacher`
    - Body: `{ "teacher_id": 999 }` (assuming this teacher ID does not exist)
- **Response**:
    - Status: `404 Not Found`
    - Body: `{ "error": {"code": "E002", "message": "Teacher not found.", "details": {}} }`

## 6. Implementation Approach

### 6.1 Setup and Configuration
- Extend the Flask application to include new endpoints for assigning teachers to courses.

### 6.2 Database Initialization
- Add the new `teacher_id` column to the Course table using a migration strategy through Flask-Migrate:

```bash
flask db migrate -m "Add foreign key from Course to Teacher"
flask db upgrade
```

### 6.3 RESTful Endpoints
- Implement the `POST` and `GET` routes for teacher assignments and course retrieval.

### 6.4 Testing Strategy
- Develop unit tests for the new service methods handling teacher assignments to courses.
- Integration tests to validate the new API endpoints for proper functionality.

### 6.5 Error Handling
- Ensure that assignment processes capture input errors and return appropriately structured error responses for invalid data.

## 7. Scalability, Security, and Maintainability Considerations

### 7.1 Scalability
- Extending the Course model to support teacher assignments prepares the system for future functionalities effectively.

### 7.2 Security
- Conduct thorough validation on incoming requests to prevent issues such as SQL injection and ensure data integrity.

### 7.3 Maintainability
- Continue to follow clean coding principles, implementing documentation to make future updates easier.

## 8. Documentation

### 8.1 README.md
- Update the `README.md` file to explain how to interact with the new API endpoints related to course-teacher assignments.

## 9. Deployment Considerations

### 9.1 Production Readiness
- Confirm that the application correctly initializes with no issues, and the new foreign key in Course is successfully integrated.

## 10. Success Criteria
- Teachers can be successfully assigned to courses, returning the expected confirmation JSON.
- Course details can be fetched including the assigned teacher.
- Validation errors for nonexistent teachers or courses return actionable messages.
- Comprehensive tests cover all new functionalities.
- Documentation remains consistent with all changes made.

### Existing Code Files Modifications

**File: src/models.py**
- Update the Course class to introduce the `teacher_id` foreign key.

**File: src/services/course_service.py**
- Implement the methods `assign_teacher_to_course` and `get_course_details` to encapsulate the new business logic.

**File: src/api/routes.py**
- Add routes for managing teacher assignments with the URLs specified above.

**File: tests/api/test_routes.py**
- Enhance existing tests to validate the functionality of the new course-teacher assignment endpoints.

**File: tests/services/test_course_service.py**
- Create test cases specifically for the logic surrounding teacher assignments to courses.

**Migration Strategy**
- Utilize `Flask-Migrate` to generate migration scripts for the addition of a foreign key in the Course table:
  
```bash
flask db migrate -m "Add foreign key from Course to Teacher"
flask db upgrade
```

By following this implementation plan, the team will successfully enable a teacher-course relationship within the educational management system while ensuring the application remains robust and maintainable.