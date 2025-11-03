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
# Implementation Plan: Add Email Field to Student Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Student Management Web Application

## Version
1.0.0

## Purpose
This implementation plan outlines the changes required to establish a relationship between the existing Course entity and the newly created Teacher entity. It defines the architecture, technology stack updates, database schema modifications, API contracts, and testing requirements to ensure efficient management of course-teacher assignments.

---

## I. Architecture Overview

The architecture follows a microservices-based pattern, where the Course module will be enhanced to include a relationship with the Teacher module. This addition will enable better organization of course information and facilitate teacher-student interactions.

### Component Responsibilities
- **Web Application**:
  - Handle requests for assigning teachers to courses and retrieving associated course details.
  - Ensure proper validation and error handling for input data.
  - Return consistent JSON responses.

- **SQLite Database**:
  - Store the updated Course entity with a new `teacher_id` field ensuring data integrity and accessibility.
  - Maintain existing tables (Course, Student, Teacher) with appropriate foreign key relationships.

---

## II. Technology Stack

- **Backend Framework**: Flask (Python) 
- **Database**: SQLite 
- **API Format**: JSON
- **Testing Framework**: pytest for unit and integration testing
- **Environment Management**: virtualenv for Python dependency management
- **Logging**: Python's built-in logging module for structured logging

---

## III. Data Models

### Updated Database Schema

#### Updated Course Model
```python
class Course(db.Model):
    __tablename__ = 'courses'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    teacher_id = db.Column(db.Integer, db.ForeignKey('teachers.id'), nullable=True)
    # Other existing fields...
```

### Database Migration Strategy
- Use Alembic to create a migration script `008_add_teacher_relationship_to_courses.py` that modifies the existing `courses` table.
- The migration should:
  - Add a new column `teacher_id` as a foreign key referencing the `id` field in the `teachers` table.
  - Ensure no data loss or alteration occurs in existing records.

---

## IV. API Contracts

### Updated Endpoints

1. **Assign Teacher to Course**
   - **PATCH /courses/{courseId}**
   - **Request Body**:
     ```json
     {
       "teacher_id": 1
     }
     ```
   - **Responses**:
     - **200 OK**: Successfully assigned teacher to course
       ```json
       {
         "id": 1,
         "teacher_id": 1,
         "teacher": {
           "name": "John Doe",
           "email": "johndoe@example.com"
         },
         "otherFields": "...other course information..."
       }
       ```
     - **400 Bad Request**: Invalid teacher ID
       ```json
       {
         "error": {"code": "E001", "message": "Invalid teacher ID provided."}
       }
       ```

2. **Retrieve Course Information**
   - **GET /courses/{courseId}**
   - **Responses**:
     - **200 OK**: Returns complete details of the specified course
       ```json
       {
         "id": 1,
         "teacher": {
           "name": "John Doe",
           "email": "johndoe@example.com"
         },
         "otherFields": "...other course information..."
       }
       ```
     - **404 Not Found**: Course not found
       ```json
       {
         "error": {"code": "E002", "message": "Course not found."}
       }
       ```

### JSON Responses
- Maintain JSON format for all API responses related to course and teacher interactions ensuring consistency and clarity.

---

## V. Implementation Approach

### Development Phases

1. **Set Up Project Structure**
   - Ensure the existing project structure aligns with the introduction of modifications, maintaining consistency with previous sprints.

2. **Modify Database Logic**
   - Update the existing SQLAlchemy model for Course to include the `teacher_id` field.
   - Implement the Alembic migration script `008_add_teacher_relationship_to_courses.py` to manage the database schema changes effectively.

3. **Update API Endpoints**
   - Implement the PATCH `/courses/{courseId}` endpoint to assign a teacher to a course.
   - Update the GET `/courses/{courseId}` endpoint to include teacher details in the response.

4. **Validation Logic**
   - Implement validation to ensure that the provided `teacher_id` is valid (i.e., exists in the Teacher table).
   - Set up error handling for cases where the teacher is not found.

5. **Testing**
   - Write unit tests covering both successful assignments and error scenarios.
   - Ensure the test coverage meets a minimum of 70% for the new functionalities.

6. **Documentation**
   - Update the `README.md` file to reflect the new feature, usage instructions, and examples.

### Database Migration Strategy
- Implement migrations using Alembic with the `008_add_teacher_relationship_to_courses.py` migration file.
- The migration should modify the `courses` table to add `teacher_id` while ensuring that existing records remain intact.

---

## VI. Testing Requirements

### Test Coverage
- Aim for at least 70% coverage of business logic.
- Specific focus on:
  - Successful teacher assignment to courses.
  - Retrieval of course information including teacher details.
  - Validation errors for invalid teacher IDs.

### Test Organization
- Tests should mirror the source structure in `tests/routes/`.
- Use descriptive test names following the pattern: `test_assign_teacher_to_course_succeeds()`.

---

## VII. Error Handling & Validation

- Implement clear validation for the `teacher_id` input to ensure it is valid.
- Standardize error responses across API endpoints, including error codes and messages.

---

## VIII. Security Considerations

- Sanitize inputs to prevent SQL injection attacks.
- Validate the format of teacher IDs and ensure they exist.

---

## IX. Logging & Monitoring

- Use structured logging for tracking requests and responses related to course and teacher assignments.
- Log errors with appropriate context for troubleshooting.

---

## X. Deployment Considerations

- Ensure that application migrations run automatically on startup to establish the new database schema.
- Include a health check endpoint to monitor operational status after deployment.

---

## XI. Roadmap & Timeline

1. **Week 1**: Set up the project structure, implement the database schema for the course-teacher relationship.
2. **Week 2**: Define API endpoints for teacher assignment and course retrieval.
3. **Week 3**: Implement error handling and validation logic.
4. **Week 4**: Complete unit tests and document all changes. Conduct integration testing.

---

## XII. Technical Trade-offs

- **SQLite Selection**: Continuing usage of SQLite allows ease of development but may need consideration for scaling in the future.
- **Basic Validation**: Current validation is kept simple; enhancements might be considered later based on feedback.

---

This implementation plan serves as a comprehensive guide to creating the relationship between the Course and Teacher entities within the existing application framework, paving the way for better course management and teacher assignment capabilities while adhering to established best practices.