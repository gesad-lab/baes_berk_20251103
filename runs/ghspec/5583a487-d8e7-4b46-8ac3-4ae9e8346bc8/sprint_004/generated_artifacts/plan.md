# Implementation Plan: Add Course Relationship to Student Entity

---
## INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Create Course Entity

---
## INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Add Email Field to Student Entity

---
## INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Student Entity Web Application

## Version
**Version**: 1.2.0

## 1. Overview
This implementation plan describes the process of adding a course relationship to the existing Student entity within the web application. This enhancement will enable students to enroll in multiple courses, facilitating better tracking of academic progress and engagement with course offerings.

## 2. Architecture
- **Architecture Style**: Microservices architecture coupled with a RESTful API design consistent with prior implementations.
- **Back-end**: A Flask (Python) web application will continue to serve as the API layer.
- **Database**: SQLite for persistence of the new `StudentCourse` junction table alongside existing Student and Course tables.
- **Hosting**: Heroku or AWS for deployment and scalability, maintaining previous hosting choices.

## 3. Technology Stack
- **Back-end**: 
  - Language: Python
  - Framework: Flask
- **Database**: SQLite for local development.
- **Testing Framework**: Pytest for testing API functionality.
- **API Documentation**: OpenAPI for clarity on API usage.

## 4. Module Boundaries and Responsibilities
- **API Module**:
  - Manage incoming HTTP requests specific to student-course associations.
  - Handle validation and response formatting for related endpoints.

- **Database Module**:
  - Manage schema modifications for the new `StudentCourse` junction table using SQLAlchemy.
  - Include functionalities for existing Student and Course entities without data loss.

- **Model Module**:
  - Define a new junction model for Student-Course associations, as follows:
    ```python
    class StudentCourse(db.Model):
        student_id = db.Column(db.Integer, db.ForeignKey('student.id'), primary_key=True)
        course_id = db.Column(db.Integer, db.ForeignKey('course.id'), primary_key=True)
    ```

- **Validation Module**:
  - Handle input validation for the course association process.

## 5. Data Models and API Contracts
### Data Model
- **StudentCourse Junction Table**
```python
class StudentCourse(db.Model):
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), primary_key=True)
```

### API Contracts
- **Associate Courses Endpoint**
  - URL: `PUT /students/{id}/courses`
  - Request Body: 
    ```json
    {
      "course_ids": [1, 2]
    }
    ```
  - Responses:
    - **200 OK** (on success):
      ```json
      {
        "message": "Courses associated with the student successfully."
      }
      ```
    - **400 Bad Request** (if no courses are selected):
      ```json
      {
        "error": {
          "code": "E002",
          "message": "At least one course must be selected."
        }
      }
      ```

- **Retrieve Student with Courses Endpoint**
  - URL: `GET /students/{id}`
  - Responses:
    - **200 OK** (on success):
      ```json
      {
        "id": 1,
        "name": "John Doe",
        "courses": [
          {
            "course_id": 1,
            "course_name": "Introduction to Programming"
          },
          {
            "course_id": 2,
            "course_name": "Advanced Mathematics"
          }
        ]
      }
      ```

## 6. Implementation Approach
1. **Setup Development Environment**:
    - Ensure the current Python, Flask, and SQLite settings are prepared for modifications related to records.

2. **Database Migration**:
    - Create the migration script using Flask-Migrate to introduce the `StudentCourse` table while retaining existing Student and Course data.
    - Apply schema migrations on startup.

3. **Create API Endpoints**:
    - Implement the `PUT /students/{id}/courses` endpoint for associating courses with students.
    - Implement the `GET /students/{id}` endpoint to retrieve students alongside their course associations.

4. **Input Validation**:
    - Validate incoming requests to ensure that `course_ids` is not empty and references valid `Course` IDs.

5. **Automated Testing**:
    - Develop unit tests using Pytest to cover:
      - Successful scenarios for course association.
      - Validation checks for empty course selections.
      - Retrieval of student records including associated courses.

6. **Documentation**:
    - Update the API documentation to integrate the endpoints for course associations along with usage guidelines.

7. **Deployment**:
    - Prepare application deployment on Heroku, ensuring .env variables reflect the updated configurations.

## 7. Security Considerations
- Implement stringent input validation to guard against injection attacks.
- Clearly define HTTP status responses for different outcomes.

## 8. Performance Considerations
- Optimize database queries with indexing on the `StudentCourse` junction table.
- Ensure statelessness to allow for scaling.

## 9. Testing Requirements
- **Unit Tests**: Achieve at least 70% coverage for the business logic for API endpoints handling courses.
- **Integration Tests**: Ensure `PUT /students/{id}/courses` and `GET /students/{id}` function correctly.
- **Contract Tests**: Confirm API endpoints comply with the designated specifications.

## 10. Success Criteria
- Successful API responses confirming course associations or retrieval of student records include courses.
- Clear validation error messages when improper requests are made.
- Automated tests achieving the required coverage for all defined scenarios.

## 11. Deployment Considerations
- The application will initiate automatically post-schema migration without manual intervention.
- Integrate health check endpoints for monitoring.

## 12. Modifications to Existing Files
### 1. Update/Create Student-Course Relationship Model
- Create a new model definition for the `StudentCourse` junction table.

### 2. Update API Endpoint Handlers
- Add new route handlers for the required `PUT` and `GET` endpoints in the API files. Here’s an example for the association endpoint:
```python
@app.route('/students/<int:id>/courses', methods=['PUT'])
def associate_courses(id):
    data = request.get_json()
    # Handle course association logic here...
```

### 3. Modify Student & Course Retrieval Logic
- Update the existing `GET /students/{id}` handler to include course details in the response.

### 4. Testing Files
- Create new testing files specifically for student-course functionalities:
  - `tests/test_associate_courses.py`
  - `tests/test_get_student_with_courses.py`
  
### 5. Migration Script
- Generate a migration script for creating the `StudentCourse` table:
```bash
flask db migrate -m "Create StudentCourse junction table"
flask db upgrade
```

### 6. Extend the `.env.example`
- Document environment variables related to schema changes or additional deployment settings, if needed.

This plan will ensure that the course relationships are successfully implemented for students in the existing web application, maintaining consistency, security, and performance across the application.