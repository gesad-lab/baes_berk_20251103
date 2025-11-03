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

## Version: 1.0.0  
**Purpose**: To establish a relationship between the **Course** and **Teacher** entities within the educational application for better management of course assignments.

## I. Architecture Overview
- **Architecture Pattern**: RESTful API
- **Frontend**: (Optional; can be discussed in future phases)
- **Backend Framework**: Flask (Python)
- **Database**: SQLite (suitable for current application requirements)

## II. Technology Stack
- **Programming Language**: Python
- **Web Framework**: Flask
- **Database**: SQLite
- **ORM**: SQLAlchemy
- **Testing Framework**: Pytest for unit and integration testing
- **Development Environment**: Virtual environment with required libraries managed via `requirements.txt`

## III. Module Boundaries and Responsibilities
- **Courses API Module**: Enhancements to manage the relationship between courses and teachers.
- **Database Module**: Responsible for managing database modifications and migrations related to the course and teacher relationship.

### Modifications to Existing Modules:
1. **courses.py** - Update existing endpoints to include teacher assignment logic.
2. **models.py** - Modify the existing Course model to include the new `teacher_id` field and update the foreign key relationship.
3. **migrations.py** - Handle the migration to update the Course table schema.

## IV. Data Models
### Existing Course Model Modification (models.py)
```python
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    teacher_id = Column(Integer, ForeignKey('teachers.id'), nullable=True)  # New field for Teacher relationship

    teacher = relationship("Teacher", back_populates="courses")

class Teacher(Base):
    __tablename__ = 'teachers'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)

    courses = relationship("Course", back_populates="teacher")
```

## V. API Contracts
### Updated Endpoints:
1. **Assign Teacher to Course**
   - **PUT /courses/{course_id}/assign-teacher**
   - **Request Body**:
     ```json
     {
       "teacher_id": 1
     }
     ```
   - **Response**:
     - **Success**: `200 OK` with updated course details:
     ```json
     {
       "id": 1,
       "name": "Mathematics",
       "description": "Algebra and Geometry",
       "teacher_id": 1
     }
     ```
     - **Error**: `404 Not Found` if the course does not exist, or `400 Bad Request` for invalid teacher ID.

2. **Retrieve Course Information** (Updated)
   - **GET /courses/{course_id}**
   - **Response**:
     - **Success**: `200 OK` with course and teacher information:
     ```json
     {
       "id": 1,
       "name": "Mathematics",
       "description": "Algebra and Geometry",
       "teacher": {
         "id": 1,
         "name": "John Doe",
         "email": "john.doe@example.com"
       }
     }
     ```
     - **Error**: `404 Not Found` if the course does not exist.

3. **List Courses with Teachers**
   - **GET /courses**
   - **Response**:
     - **Success**: `200 OK` with course and teacher details:
     ```json
     [
       {
         "id": 1,
         "name": "Mathematics",
         "description": "Algebra and Geometry",
         "teacher": {
           "id": 1,
           "name": "John Doe",
           "email": "john.doe@example.com"
         }
       }
     ]
     ```

## VI. Implementation Approach
1. **Setup Migration for Database**:
   - The `migrations.py` will include a function to modify the `courses` table to add the `teacher_id` field without affecting existing data.

2. **Database Initialization**:
   - Modify the existing Course model in `models.py` to integrate with the new teacher relationship.

3. **Implement API Logic in `courses.py`**:
   - Add the logic for assigning a teacher to a course in the new endpoint.
   - Update the existing retrieval logic to return associated teacher details.

4. **Response Handling**:
   - Ensure all API responses conform to expected JSON formats. Implement structured error handling for invalid inputs.

5. **Add Testing**:
   - Create test cases in `tests/test_courses.py` to validate functionalities related to course and teacher relationship management.

## VII. Security Considerations
- Sanitize all inputs to prevent SQL injection and enforce email uniqueness within the Teacher model before INSERT operations.
- Validate that `teacher_id` exists and matches a valid teacher before assignment.

## VIII. Error Handling & Validation
- Validate incoming requests to ensure `teacher_id` is valid and exists.
- Return structured error responses based on existing error handling protocols.

## IX. Performance Considerations
- Maintain response times under 200ms for API requests related to course and teacher management.
- Optimize the SQLAlchemy query patterns for efficient data retrieval and assignment.

## X. Testing Requirements
### Test Cases
1. **Assign Teacher to Course**:
   - Validate assignment functionality with valid course and teacher IDs.
   - Test cases for attempting to assign teachers to non-existent courses.

2. **Retrieve Course**:
   - Validate retrieval of course details along with teacher information.
   - Test retrieval of courses where no teacher is assigned.

3. **List Courses**:
   - Confirm the correct structure of the response and accurate association with teacher data.

### Coverage
- Aim for at least 90% coverage on business logic pertaining to the course and teacher relationships.

## XI. Documentation
- Update the `README.md` to include new API endpoints for assigning teachers and retrieving course details.

## XII. Deployment Considerations
- Provide a clear migration strategy for updating the database schema with instructions for running migrations on deployment.

## XIII. Logging & Monitoring
- Implement structured logging to capture assignments, retrievals, and any error responses related to the course-teacher relationship.

## XIV. Database Migration Strategy
- **Migrations**: 
  - Implement a migration function in `migrations.py` to alter the `courses` table:
```python
from sqlalchemy import create_engine, Column, Integer, ForeignKey
from sqlalchemy.orm import sessionmaker

def migrate_add_teacher_id_to_courses():
    engine = create_engine('sqlite:///database.db')  # Adjust database URL as required
    connection = engine.connect()
    connection.execute(
        """
        ALTER TABLE courses ADD COLUMN teacher_id INTEGER REFERENCES teachers(id);
        """
    )
    connection.close()
```
- Ensure the migration is well-documented and validated against existing production data with appropriate backups.

## XV. Success Criteria Verification
- Verify that teachers can be successfully assigned to courses and can be retrieved correctly.
- Assess performance metrics to ensure response times meet specified limits.

---

This implementation plan details the steps required to integrate the Teacher relationship into the Course entity within the educational application framework. It maintains an organized structure aligning with existing architecture while providing clarity on new functionalities, testing strategies, and migration protocols. 

### Existing Code Files Modifications:
- **models.py**: Modify the Course model to include `teacher_id` and relationships as outlined.
- **migrations.py**: Introduce the `migrate_add_teacher_id_to_courses` function to add the `teacher_id` column to the `courses` table.
- **courses.py**: Update to handle new functionality for assigning teachers and enhancing existing course detail retrieval.
- **New Test File**: `tests/test_courses.py` to validate new functionalities surrounding the Course entity. 

This structured approach ensures a seamless integration of the Teacher-Student relationship to the Course entity while ensuring backward compatibility with existing models and data integrity.