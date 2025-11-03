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

## I. Project Overview

The purpose of this implementation plan is to establish a relationship between the Course entity and the Teacher entity within the existing system. This feature will enhance the management of educational data by allowing each Course to be associated with a designated Teacher. It will improve data accessibility and organization within the system, laying a foundation for future features such as scheduling and analytics.

## II. Architecture

### 2.1 System Architecture
- **Architecture Pattern**: The existing MVC (Model-View-Controller) architecture will be utilized to integrate the new teacher relationship while maintaining separation of concerns and ensuring smooth data flow.
- **Components**:
  - **Controller Layer**: Manage API request handling for course updates and retrieval with teacher information.
  - **Service Layer**: Implement business logic for managing course-teacher assignments.
  - **Repository Layer**: Facilitate database interactions related to Course and Teacher entities.
  - **Database**: SQLite will be updated to reflect the new schema relationships.

### 2.2 Data Flow
1. An admin user sends a PATCH request to assign a teacher to a course.
2. The controller validates the request and invokes the service layer.
3. The service layer handles logic for checking teacher ID validity and updating the course with the appropriate teacher ID.
4. The controller responds with updated course data or an appropriate error message.

## III. Technology Stack

- **Programming Language**: Python
- **Web Framework**: Flask
- **Database**: SQLite
- **ORM**: SQLAlchemy
- **Testing Framework**: pytest
- **Environment Management**: pipenv or virtualenv

## IV. Module Responsibilities

### 4.1 Module Boundaries
1. **Controller (`src/controllers/course_controller.py`)** 
   - Update the existing Course controller to handle teacher assignment and retrieve courses with teacher details.
2. **Service (`src/services/course_service.py`)** 
   - Extend the existing Course service to implement logic for assigning teachers to courses.
3. **Repository (`src/repositories/course_repository.py`)**
   - Modify the existing Course repository to update course records with teacher associations.
4. **Model (`src/models/course.py`)**
   - Extend the existing Course model to include the `teacher_id` foreign key.

### 4.2 Data Models

Update the existing Course model in `src/models/course.py` to include a foreign key reference to the Teacher entity:

```python
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Course(Base):
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    teacher_id = Column(Integer, ForeignKey('teachers.id'), nullable=True)  # New foreign key relationship
    teacher = relationship("Teacher")  # Define relationship with Teacher
```

## V. API Contracts

### 5.1 Endpoints

1. **Assign Teacher to Course**
   - **Endpoint**: `PATCH /courses/{course_id}`
   - **Request Body**:
     ```json
     {
       "teacher_id": "string"  // Required
     }
     ```
   - **Response**:
     - **Success** (200 OK):
     ```json
     {
       "course_id": "string",
       "course_name": "string",
       "teacher": {
         "id": "string",
         "name": "string",
         "email": "string"
       }
     }
     ```
     - **Error** (400 Bad Request):
     For invalid teacher ID:
     ```json
     {
       "error": {
         "code": "E003",
         "message": "Invalid teacher ID"
       }
     }
     ```

2. **Retrieve Course with Teacher Information**
   - **Endpoint**: `GET /courses/{course_id}`
   - **Response**:
     - **Success** (200 OK):
     ```json
     {
       "course_id": "string",
       "course_name": "string",
       "teacher": {
         "id": "string",
         "name": "string",
         "email": "string"
       }
     }
     ```

## VI. Error Handling

### 6.1 Error Handling Strategies
- Validate the teacher ID in the course update request and return structured error responses with appropriate HTTP status codes for invalid inputs.

## VII. Database Migration

### 7.1 Database Migration Strategy
- Use Alembic to create a migration script that modifies the existing `courses` table by adding the `teacher_id` foreign key, ensuring existing Course and Student data integrity.

Migration script example:
```python
from alembic import op
import sqlalchemy as sa

def upgrade():
    op.add_column('courses', sa.Column('teacher_id', sa.Integer(), sa.ForeignKey('teachers.id'), nullable=True))

def downgrade():
    op.drop_column('courses', 'teacher_id')
```

## VIII. Testing Approach

### 8.1 Test Coverage
- Aim for a minimum of 70% test coverage for the functionalities related to course-teacher relationships, focusing on:
  - Successful assignment of teachers to courses.
  - Correct retrieval of courses with teacher details.
  - Accurate error handling for invalid teacher IDs.

### 8.2 Test Cases Based on User Scenarios
1. **Assigning a Teacher to a Course**: Validate that valid requests successfully assign a teacher.
2. **Retrieving Course Information**: Ensure that courses with teachers return accurate details.
3. **Error Handling**: Confirm that the correct error messages are returned for invalid teacher IDs.

## IX. Deployment Considerations

### 9.1 Application Deployment
- Ensure environment variables for database settings are correctly configured. Include Alembic migration commands to apply schema changes during deployment.

### 9.2 Logging and Monitoring
- Integrate structured logging for all API interactions to facilitate monitoring and quick resolution of issues.

## X. Conclusion

This implementation plan details the approach to establishing a relationship between the Course and Teacher entities within the existing system. By leveraging the current architecture and technology stack, this integration will enhance educational data management capabilities while maintaining backward compatibility with existing data models.

## Modifications Needed to Existing Files

1. **Update** `src/models/course.py`
   - Add the new attribute `teacher_id` in the Course model definition and establish the relationship.

2. **Extend** `src/controllers/course_controller.py`
   - Modify this file to implement new routes for assigning teachers to courses and fetching course details with teacher information.

3. **Modify** `src/services/course_service.py`
   - Add logic to handle teacher assignments and validation for the course service.

4. **Update** `src/repositories/course_repository.py`
   - Adapt this file to manage updates related to the teacher assignment effectively.

5. **Create** a migration script using Alembic to incorporate the new foreign key in the existing courses table.

6. **Extend** Unit tests in `tests/controllers/test_course_controller.py` and `tests/services/test_course_service.py`
   - Include tests that validate the teacher assignment to courses and the retrieval of course details with teachers.

By following this structured implementation plan, we can successfully establish the teacher-course relationship, improving the educational data management capabilities of the system while ensuring existing functionality remains intact.