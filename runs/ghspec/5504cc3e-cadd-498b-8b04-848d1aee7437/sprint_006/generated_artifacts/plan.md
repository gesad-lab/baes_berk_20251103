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

## Version: 1.1.0  
**Author**: [Your Name]  
**Date**: [Today’s Date]  

---

## 1. Overview & Purpose

This implementation plan outlines the steps necessary to establish a relationship between the **Course** and **Teacher** entities within the existing application framework. By linking Courses to Teachers, the application enhances the management of courses and educators, ensuring better organization and allowing for future functionalities such as reporting and scheduling. This update prioritizes maintaining existing data integrity and operational continuity.

## 2. Technology Stack

- **Backend Framework**: Flask (Python)
- **Database**: SQLite
- **API**: Flask RESTful
- **Data Serialization**: Marshmallow
- **Testing Framework**: pytest
- **Deployment**: Docker

## 3. Architecture Design

### 3.1 System Modules

- **API Module**: Implement API endpoints for assigning teachers to courses and retrieving course details with teacher information.
- **Service Module**: Business logic for managing the teacher-course relationship.
- **Database Module**: Updated schema featuring the new foreign key relationship between Course and Teacher.
- **Validation Module**: Input validation logic for API requests involving course assignments.

### 3.2 Module Responsibilities

- **API Module**: Define endpoints to assign teachers to courses and fetch course details inclusive of associated teachers.
- **Service Module**: Execute methods responsible for linking teachers with courses and retrieving relevant course information.
- **Database Module**: Update Course model to include `teacher_id`, defining relationships and constraints.
- **Validation Module**: Validate input data for course assignments ensuring proper IDs are provided.

## 4. Data Models

### 4.1 Course Entity Update

```python
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from your_application import db

class Course(db.Model):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    teacher_id = Column(Integer, ForeignKey('teachers.id'), nullable=True)
    
    teacher = relationship('Teacher', back_populates='courses')
```

### 4.2 Teacher Entity Update

In the `teacher.py` model file, add this line to establish the reverse relationship:

```python
courses = relationship('Course', back_populates='teacher')
```

### 4.3 JSON Response Formats

- **Assign Teacher to Course - Success Response**: 
```json
{
  "message": "Teacher assigned to course successfully"
}
```
- **Get Course with Teacher - Success Response**: 
```json
{
  "data": {
    "id": 1,
    "name": "Mathematics",
    "teacher": {
      "id": 2,
      "name": "Jane Doe"
    }
  }
}
```
- **Error Response**: 
```json
{
  "error": {
    "code": "E002",
    "message": "Course not found or Teacher not found"
  }
}
```

## 5. API Contracts

### 5.1 Endpoints

1. **Assign Teacher to Course**
   - **Method**: POST
   - **Endpoint**: `/api/v1/courses/<course_id>/assign_teacher`
   - **Payload**: 
   ```json
   {
     "teacher_id": 2
   }
   ```

2. **Retrieve Course Details with Teacher**
   - **Method**: GET
   - **Endpoint**: `/api/v1/courses/<course_id>`
   - **Response**:
   ```json
   {
     "data": {
       "id": 1,
       "name": "Mathematics",
       "teacher": {
         "id": 2,
         "name": "Jane Doe"
       }
     }
   }
   ```

## 6. Implementation Approach

### 6.1 Development Steps

1. **Database Migration**: 
   - Create a migration script using Alembic to add the `teacher_id` foreign key to the existing `courses` table while preserving existing course data.

2. **Update Existing Models**: 
   - Modify `models/course.py` to add the `teacher_id` relationship and ensure reverse mapping in `models/teacher.py`.

3. **Enhance API Endpoints**: 
   - Implement the POST and GET endpoints in the `api/courses.py` file.

4. **Develop Service Logic**: 
   - Create or update a new service file, `course_service.py`, to handle business logic for assigning teachers and retrieving course details.

5. **Input Validation**: 
   - Implement validation logic for incoming IDs in the API endpoints to ensure proper request formatting.

6. **Testing**: 
   - Write unit tests to cover the new service functions and integration tests to verify API endpoint functionality.

7. **Documentation**: 
   - Update README.md to include instructions for using the new endpoints with examples of how to assign a teacher and retrieve a course with teacher details.

### 6.2 Error Handling

- Implement error handling for the API to return clear messages when course or teacher IDs are invalid, ensuring appropriate user feedback.

## 7. Testing & Quality Assurance

### 7.1 Testing Strategy

- **Unit Tests**: Validate methods in `course_service.py` for assigning teachers to courses and retrieving course details.
- **Integration Tests**: Ensure API functionality operates as expected, including valid and invalid scenarios.
- **Mock Testing**: Utilize pytest fixtures to mock requests and responses for testing.

### 7.2 Minimum Test Coverage

- Aim for at least 70% code coverage across the new functionalities, with critical areas (assignment and retrieval operations) targeting over 90% coverage.

## 8. Security Considerations

### 8.1 Data Protection

-Validate all inputs to prevent SQL injection and maintain data integrity regulations throughout the API interactions.

## 9. Deployment Considerations

### 9.1 Database Migration Strategy

- Use Alembic to create and execute the migration that adds the foreign key `teacher_id` to the existing `courses` table. Confirm existing records are not altered.

### 9.2 Health Checks

- Implement a health-check endpoint post-deployment to verify that all services including the database relationships function correctly.

## 10. Documentation

- Update the `README.md` file with new API changes, including descriptions of endpoints, expected payloads, and usage examples for assigning teachers and retrieving courses.

---

By following this implementation plan, the architecture will successfully integrate the teacher-course relationship while adhering to existing conventions. This ensures easy maintainability, clarity in code structure, and paves the way for future enhancements in educational management functionalities.

## Existing Code File Modifications

### 1. New Files to be Created
- `src/api/course_api.py`: Define new API routes for assigning teachers to courses and fetching course details.
- `src/services/course_service.py`: Logic related to managing the teacher-course relationship.

### 2. Migration File
- Create a migration script in `migrations/versions/`, which will modify the existing `courses` table to include `teacher_id`.

### 3. Tests Structure
- `tests/unit/test_course_service.py`: Place unit tests for service functions related to teacher assignments and course retrieval.
- `tests/integration/test_course_api.py`: Integration tests for new APIs adding teacher assignments to courses.

This structured plan will facilitate a smooth integration of the teacher relationship in the course management framework, ensuring that existing system functionalities remain unaffected.