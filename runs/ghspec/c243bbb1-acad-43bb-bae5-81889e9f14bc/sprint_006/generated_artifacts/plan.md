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

## I. Project Overview
This implementation plan outlines the required architectural modifications, technology stack, module boundaries, and technical specifications to establish a relationship between the "Course" and "Teacher" entities within the existing educational management system. Enhancing the relationship between these entities will improve course ownership and accountability.

---

## II. Technology Stack
- **Backend Framework**: FastAPI (Python) - For building the RESTful API.
- **Database**: SQLite - A lightweight database for data persistence.
- **HTTP Client for Testing**: HTTPX - For performing API tests.
- **Asynchronous Support**: Uvicorn - An ASGI server to run the FastAPI application.
- **ORM**: SQLAlchemy - For database interactions.

---

## III. Architecture & Modules

### 3.1 High-Level Architecture
- **API Layer**: Exposes endpoints for managing the association of teachers with courses.
- **Service Layer**: Contains business logic pertaining to course-teacher relationships.
- **Data Access Layer**: Handles database interactions related to the `Course` and `Teacher` entities.

### 3.2 Module Responsibilities

1. **API Module (`api/`)**:
   - Define new endpoint for updating links between courses and teachers.
   - Input validation and response crafting for API requests.

2. **Service Module (`services/`)**:
   - Implement business logic for associating a teacher with a course, including validation of IDs.

3. **Data Access Module (`db/`)**:
   - Update `Course` model to include `teacher_id` foreign key.
   - Create migration scripts to safely update the database schema without data loss.

---

## IV. Data Models

### SQLite Database Model

#### Update Course Model

```python
from sqlalchemy import Column, Integer, ForeignKey
from database import Base

class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    teacher_id = Column(Integer, ForeignKey('teachers.id'), nullable=True)

    def __repr__(self):
        return f"<Course(name={self.name}, teacher_id={self.teacher_id})>"
```

### Database Migration Strategy
1. Update the existing migration script for courses to include the `teacher_id` column as a foreign key referencing the `teachers` table.
2. Ensure the migration process does not impact existing course or student data integrity.

```python
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, ForeignKey

engine = create_engine('sqlite:///courses.db')
metadata = MetaData(bind=engine)

def upgrade():
    courses_table = Table('courses', metadata, autoload_with=engine)
    # Adding teacher_id column to the existing courses table
    teacher_id_column = Column('teacher_id', Integer, ForeignKey('teachers.id'), nullable=True)
    teacher_id_column.create(courses_table)
```

---

## V. API Endpoints

### 5.1 API Design

1. **PATCH `/courses/{course_id}`**:
   - **Path Parameter**:
     - `course_id`: int (required)
   - **Request Body**:
   ```json
   {
     "teacher_id": 1
   }
   ```
   - **Response (Success)**:
   ```json
   {
     "message": "Course updated successfully with teacher association."
   }
   ```
   
   - **Error Handling (Teacher ID not found)**:
     - Status 404: Teacher not found.
     ```json
     {
       "error": {
         "code": "E404",
         "message": "Teacher not found."
       }
     }
     ```

2. **GET `/courses/{course_id}`**:
   - **Path Parameter**:
     - `course_id`: int (required)
   - **Response** (including Teacher details):
   ```json
   {
     "id": 1,
     "name": "Math 101",
     "teacher": {
       "id": 1,
       "name": "John Doe",
       "email": "john.doe@example.com"
     }
   }
   ```

---

## VI. Implementation Steps

1. **Project Update**:
   - Maintain the existing project structure as shown below:
     ```
     course-management/
     ├── api/
     ├── db/
     ├── services/
     ├── main.py
     ├── requirements.txt
     └── README.md
     ```

2. **Update Requirements**:
   - Ensure necessary libraries are reflected in `requirements.txt`. No new dependencies required for this feature.

   ```plaintext
   fastapi
   uvicorn
   sqlalchemy
   httpx
   ```

3. **Database Schema Migration**:
   - Adjust the existing migration script to include the `teacher_id` foreign key for the `courses` table, ensuring backwards compatibility.

4. **Implement API Endpoints**:
   - Define the new PATCH endpoint in `api/courses.py`.
   - Input validation of `teacher_id` and `course_id` using Pydantic models.

5. **Implement Business Logic**:
   - Create service functions in `services/course_service.py`:
     - `associate_teacher(course_id, teacher_id)`: Handle the logic for associating a teacher with a course.
     - `get_course_details(course_id)`: To fetch course details along with associated teacher information.

6. **Testing**:
   - Write unit tests for the service functions in `tests/test_courses.py`.
   - Create integration tests for the new API endpoints in `tests/test_courses_api.py`.

---

## VII. Testing Strategy

### 7.1 Test Coverage
- Aim for at least 70% coverage of business logic with special focus on critical paths (teacher associations).

### 7.2 Types of Tests
- **Unit Tests**: Validate functions for associating teachers to courses ensuring the necessary validations.
- **Integration Tests**: Validate the PATCH and GET API endpoints for linking and retrieving teacher-course relationships.

---

## VIII. Error Handling and Input Validation

### 8.1 Input Validation
- Ensure the following during teacher-course association:
  - Validate that `teacher_id` corresponds to an existing `Teacher` entity.
  - Validate that `course_id` corresponds to an existing `Course`.

### 8.2 Error Responses
- Structure error responses adhering to JSON format as defined in the API Design, to provide clarity for user errors.

---

## IX. Security Considerations

### 9.1 Data Protection
- Implement input sanitization to ward against SQL injection.
- Protect sensitive configurations via environment variables, avoiding any hardcoded secrets.

---

## X. Deployment Considerations

### 10.1 Local Development
- Validate that the application initializes successfully, applying migrations without disruption. Ensure all functional endpoints operate as expected.

---

## XI. Logging & Monitoring

### 11.1 Basic Logging
- Set up basic logging for recording API requests and responses to help with monitoring and debugging during development.

---

## XII. Conclusion

This implementation plan provides a detailed approach for integrating a teacher relationship into the course entity of the educational management system. By following the outlined steps, we ensure that existing functionalities remain intact while enhancing the system's capacity for managing course instructor relationships.

**Modifications Needed**:
1. **In `api/courses.py`**:
   - Define new PATCH and GET endpoints for updating teacher associations and retrieving course details.

2. **In `services/course_service.py`**:
   - Create business logic for associating teachers with courses and retrieving course-teacher relationships.

3. **In `tests/test_courses.py` and `tests/test_courses_api.py`**:
   - Add unit and integration tests for the endpoint interactions and business logic.

The strategy outlined allows for seamless integration while maintaining data integrity and ensuring user functionality remains operational and intuitive.