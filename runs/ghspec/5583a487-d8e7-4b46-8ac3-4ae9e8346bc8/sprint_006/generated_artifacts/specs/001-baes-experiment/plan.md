# Implementation Plan: Add Teacher Relationship to Course Entity

---
## INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Create Teacher Entity

---
## INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
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
**Version**: 1.0.0

## 1. Overview
This implementation plan describes the process of establishing a relationship between the existing Course entity and the newly introduced Teacher entity in the educational management application. By connecting Courses with Teachers, the application will improve management of course ownership and teacher assignments.

## 2. Architecture
- **Architecture Style**: Microservices architecture utilizing RESTful API design for consistency with prior implementations.
- **Back-end**: The existing Flask (Python) web application will continue to serve as the API layer.
- **Database**: SQLite for local development, updating the existing schema to accommodate the teacher relationship.
- **Hosting**: Continuation with Heroku or AWS for cloud deployment and scalability.

## 3. Technology Stack
- **Back-end**: 
  - Language: Python
  - Framework: Flask
- **Database**: SQLite for local development, transitioning to PostgreSQL in production.
- **Testing Framework**: Pytest for testing API functionality and behavior.
- **API Documentation**: OpenAPI for clear descriptions of API endpoints.

## 4. Module Boundaries and Responsibilities
- **API Module**:
  - Handle incoming HTTP requests for creating and retrieving Course records that include Teacher relationships.
  - Manage validation of input data and format responses accordingly.

- **Database Module**:
  - Update existing Course schema to include `teacher_id` as a foreign key linking to the Teacher table using SQLAlchemy.
  - Ensure integration with existing Course and Teacher entities without affecting their data integrity.

- **Model Module**:
  - Extend the Course model as follows:
    ```python
    class Course(db.Model):
        __tablename__ = 'courses'
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(100), nullable=False)
        teacher_id = db.Column(db.Integer, db.ForeignKey('teachers.id'), nullable=False)

        teacher = db.relationship("Teacher", back_populates="courses")
    ```

- **Validation Module**:
  - Implement input validation ensuring the `teacher_id` is provided and corresponds to an existing Teacher.

## 5. Data Models and API Contracts
### Data Model
- **Course Table (Extended)**
```python
class Course(db.Model):
    __tablename__ = 'courses'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    teacher_id = db.Column(db.Integer, db.ForeignKey('teachers.id'), nullable=False)
    
    teacher = db.relationship("Teacher", back_populates="courses")
```

- **Teacher Table**
```python
class Teacher(db.Model):
    __tablename__ = 'teachers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    courses = db.relationship("Course", back_populates="teacher")
```

### API Contracts
- **Create Course Endpoint**
  - URL: `POST /courses`
  - Request Body: 
    ```json
    {
      "name": "Mathematics 101",
      "teacher_id": 1
    }
    ```
  - Responses:
    - **201 Created** (on success):
      ```json
      {
        "message": "Course created successfully.",
        "id": 1
      }
      ```
    - **400 Bad Request** (if input validation fails):
      ```json
      {
        "error": {
          "code": "E001",
          "message": "Teacher must be assigned to the Course."
        }
      }
      ```

- **Retrieve Course Information Endpoint**
  - URL: `GET /courses/{id}`
  - Responses:
    - **200 OK** (on success):
      ```json
      {
        "id": 1,
        "name": "Mathematics 101",
        "teacher": {
          "id": 1,
          "name": "Jane Doe",
          "email": "jane.doe@example.com"
        }
      }
      ```

## 6. Implementation Approach
1. **Setup Development Environment**:
    - Ensure the current Python, Flask, and SQLite settings are prepared for schema updates.

2. **Database Migration**:
    - Create a migration script using Flask-Migrate to update the existing Course table to include the `teacher_id` foreign key, ensuring not to lose existing data.
    - Apply migrations on application startup.

3. **Create API Endpoints**:
    - Implement the `POST /courses` endpoint to allow creation of Courses with associated Teachers.
    - Implement the `GET /courses/{id}` endpoint to retrieve Course details including associated Teacher information.

4. **Input Validation**:
    - Validate incoming requests to ensure `teacher_id` is provided and corresponds to an existing Teacher entity.

5. **Automated Testing**:
    - Develop unit tests using Pytest to cover scenarios including:
      - Successful creation and retrieval of Course records.
      - Validation checks for missing required teacher assignments.

6. **Documentation**:
    - Update the API documentation to include new endpoints for Course management, complete with usage guidelines.

7. **Deployment**:
    - Prepare the application for deployment on Heroku or AWS, ensuring .env variables are configured.

## 7. Security Considerations
- Implement input validation to guard against SQL Injection and maintain overall data integrity.
- Ensure all responses do not expose sensitive implementation details.

## 8. Performance Considerations
- Consider indexing the `teacher_id` field in the Course table for faster querying related to Teachers.
- Maintain stateless interactions within the API for optimal scaling.

## 9. Testing Requirements
- **Unit Tests**: Ensure at least 70% coverage for business logic concerning Course creation, including the Teacher relationship.
- **Integration Tests**: Validate endpoint functionality for `POST /courses` and `GET /courses/{id}`.
- **Contract Tests**: Confirm API responses adhere to defined specifications.

## 10. Success Criteria
- API responses confirm successful Course record creation and retrieval with associated Teachers.
- Clear validation error messages are returned for invalid submissions.
- The application initializes the updated Course schema during startup without intervention.
- Automated tests meet the specified coverage targets.

## 11. Deployment Considerations
- Automatic application start after successful schema migration.
- Include a health check endpoint for monitoring status.

## 12. Modifications to Existing Files
### 1. Update Course Model
- Modify the existing Course model to include the `teacher_id` foreign key.
  
### 2. Update API Endpoint Handlers
- Expand existing route handlers for the `POST /courses` and `GET /courses/{id}` endpoints in the existing API files:
```python
@app.route('/courses', methods=['POST'])
def create_course():
    """Create a new Course associated with a Teacher record."""
    data = request.get_json()
    # Handle course creation logic here using data['teacher_id']...

@app.route('/courses/<int:id>', methods=['GET'])
def get_course(id):
    """Retrieve a Course with associated Teacher details."""
    # Fetch course logic here and include teacher information...
```

### 3. Testing Files
- Create or modify testing files specifically for Course and Teacher functionalities:
  - `tests/test_create_course.py`
  - `tests/test_get_course.py`

### 4. Migration Script
- Generate a migration script for updating the Course table:
```bash
flask db migrate -m "Add teacher_id to Course"
flask db upgrade
```

### 5. Extend the `.env.example`
- Document environment variables required for managing Course and Teacher relationships, such as configuration or specifics for service endpoints.

This plan will effectively implement the Teacher relationship within the existing Course entity framework, while ensuring a robust, secure, and maintainable codebase.