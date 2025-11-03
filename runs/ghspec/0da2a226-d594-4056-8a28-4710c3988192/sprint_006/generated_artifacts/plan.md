# Implementation Plan: Add Teacher Relationship to Course Entity

---

## Incremental Development Context

Previous Sprint Plan:
# Implementation Plan: Create Teacher Entity

---

## Incremental Development Context

Previous Sprint Plan:
# Implementation Plan: Add Course Relationship to Student Entity

---

## Incremental Development Context

Previous Sprint Plan:
# Implementation Plan: Create Course Entity

---

## Incremental Development Context

Previous Sprint Plan:
# Implementation Plan: Add Email Field to Student Entity

## Version
1.0.0

## Overview
This implementation plan outlines the steps required to establish a relationship between the Course entity and the newly created Teacher entity within the educational management system. This relationship is critical for allowing each Course to be assigned to a single Teacher, which enables improved management and oversight of course offerings.

## Architecture Overview
- **Architecture Pattern**: RESTful microservice (consistent with prior implementations)
- **Components**:
  - API Layer: New endpoints for updating Courses with Teacher assignments.
  - Service Layer: Business logic for managing Course-Teacher associations.
  - Data Layer: Update the existing SQLite database schema to incorporate a foreign key in the Course entity that references the Teacher entity.
- **Deployment**: Remains on the existing lightweight server setup, no infrastructure changes required.

## Technology Stack
- **Backend Framework**: FastAPI (Python)
- **Database**: SQLite
- **ORM**: SQLAlchemy (for database interactions)
- **Data Format**: JSON
- **Testing Framework**: pytest
- **Containerization**: Docker (optional for deployment)
- **Version Control**: Git

## Module Boundaries and Responsibilities

### 1. API Layer
- **Module Name**: `api`
- **Responsibilities**:
  - Define new routes for associating a Teacher with a Course.
  - Validate incoming requests for Course updates.

### 2. Service Layer
- **Module Name**: `services`
- **Responsibilities**:
  - Implement business logic in an updated `course_service.py` to handle Course modifications regarding Teacher assignments.

### 3. Data Layer
- **Module Name**: `models`
- **Responsibilities**:
  - Update the Course schema and manage database migrations to ensure data integrity.

## Implementation Approach

### Project Structure
```plaintext
educational_management_app/
│
├── src/
│   ├── api/
│   │   ├── __init__.py
│   │   ├── routes.py          # Update API endpoints to include course-teacher relationship
│   │   └── dependencies.py     # Dependency functions
│   │
│   ├── services/
│   │   ├── __init__.py
│   │   ├── student_service.py  # Existing student service logic
│   │   ├── teacher_service.py   # New business logic for managing teachers
│   │   └── course_service.py     # Updated logic for managing courses and teacher assignments
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   ├── models.py           # Update to include foreign key for Teacher in Course
│   │
│   ├── main.py                 # Application entry point
│   └── config.py               # Configuration settings
│
├── tests/
│   ├── __init__.py
│   ├── test_routes.py          # Unit tests for API endpoints
│   ├── test_services.py        # Unit tests for business logic
│   ├── test_teacher.py         # Tests for teacher functionality
│   └── test_course.py          # New test file for course-teacher relationship
│
├── .env.example                 # Sample environment variables
├── requirements.txt             # Project dependencies
└── README.md                    # Documentation
```

### Step-by-Step Implementation

1. **Update Data Models**
   - Modify `models.py` to include the `teacher_id` foreign key in the `Course` entity:
   ```python
   class Course(Base):
       __tablename__ = 'courses'

       id = Column(Integer, primary_key=True, autoincrement=True)
       title = Column(String, nullable=False)
       teacher_id = Column(Integer, ForeignKey('teachers.id'), nullable=True)  # Foreign Key to Teacher

       # Relationships
       teacher = relationship("Teacher", backref="courses")
   ```

2. **Database Migration Strategy**
   - Utilize Alembic to create a migration that:
     - Adds `teacher_id` to the `courses` table as a foreign key.
     - Preserves data integrity for existing Courses and Teachers during the migration.
   ```bash
   alembic revision --autogenerate -m "Add teacher_id foreign key to courses"
   ```

3. **Implement Services Logic**
   - Update `course_service.py` to implement:
     - `assign_teacher_to_course(course_id: int, teacher_id: int)`: to assign a Teacher to a Course.
     - Ensure it encapsulates the logic of checking for valid IDs and managing relationships.
     ```python
     def assign_teacher_to_course(course_id: int, teacher_id: int):
         # Logic to assign a teacher to a course, ensuring that course exists and is valid
     ```

4. **Define API Endpoints**
   - In `routes.py`, create new endpoints:
   - **POST** `/courses/{course_id}/assign_teacher` to assign a Teacher:
   ```json
   {
     "teacher_id": 1
   }
   ```
   - **GET** `/courses` to retrieve a list of Courses with Teacher details:
   ```json
   {
     "courses": [
       {
         "id": 1,
         "title": "Math 101",
         "teacher": {
           "id": 1,
           "name": "John Doe",
           "email": "john.doe@example.com"
         }
       }
     ]
   }
   ```

5. **Implement Input Validation**
   - Use Pydantic models to validate the request body when assigning a Teacher to a Course, ensuring the `teacher_id` is provided.

6. **Error Handling**
   - Implement checks to return meaningful error messages for scenarios such as:
     - Assigning a Teacher to a Course that does not exist.
     - Attempting to assign a Teacher without a valid Teacher ID.

7. **Testing**
   - Create a new testing file `test_course.py` to validate all Course-Teacher relationship scenarios:
   ```python
   def test_assign_teacher_to_course_with_valid_data():
       response = client.post("/courses/1/assign_teacher", json={"teacher_id": 1})
       assert response.status_code == 200  # Success
   ```

8. **Documentation**
   - Update `README.md` to include instructions for the new Course-Teacher assignment API endpoints, showcasing example requests and responses.

## Data Models

### Updated Course Entity
```json
{
  "id": "integer (primary key, automatically generated)",
  "title": "string (required)",
  "teacher_id": "integer (foreign key referencing Teacher entity, optional, defaults to NULL)"
}
```

## API Contracts

### Assign Teacher to Course
- **Endpoint**: POST `/courses/{course_id}/assign_teacher`
- **Request Body**:
  ```json
  {
    "teacher_id": 1
  }
  ```
- **Response** (200 OK):
  ```json
  {
    "message": "Teacher successfully assigned to course."
  }
  ```

### Retrieve Courses with Teachers
- **Endpoint**: GET `/courses`
- **Response**:
  ```json
  {
    "courses": [
      {
        "id": 1,
        "title": "Math 101",
        "teacher": {
          "id": 1,
          "name": "John Doe",
          "email": "john.doe@example.com"
        }
      }
    ]
  }
  ```

### Error Responses
- **Invalid Course ID** (404):
```json
{
  "error": {
    "code": "E001",
    "message": "Course not found."
  }
}
```
- **Invalid Teacher ID** (400):
```json
{
  "error": {
    "code": "E002",
    "message": "Invalid teacher ID provided."
  }
}
```

## Success Criteria
- All user scenarios pass without errors confirming the expected behavior of the Teacher-Course relationship.
- The application correctly assigns and updates Course records with valid Teacher ID entries.
- All API responses related to Courses include valid JSON and format the required data.
- The database schema is updated accordingly to reflect the new Course-Teacher relationship while preserving existing records for Courses and Teachers.

## Final Considerations
### Scalability
- As future features may introduce more complex relationships (e.g., multiple Courses per Teacher), consider designing with flexibility.

### Security
- Conduct thorough input validation and error handling to prevent vulnerabilities.

### Maintainability
- Follow clean code practices and maintain a clear project structure for future alterations.

### Logging and Monitoring
- Implement structured logging to track Course-Teacher assignment actions and their outcomes.

--- 

This implementation plan serves as a comprehensive guide to adding the Teacher relationship to the Course entity in the educational management system, ensuring seamless integration with existing functionalities and maintaining high development standards.