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
# Implementation Plan: Add Course Entity to Student Registration Web Application

---

## INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan: 
# Implementation Plan: Add Email Field to Student Entity

---

## INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan: 
# Implementation Plan: Student Registration Web Application

## I. Project Overview
### Purpose
The purpose of this implementation is to create a relationship between the Course entity and the Teacher entity within the Student Registration Web Application. This enhancement allows for clear associations of which teacher is responsible for which course—improving management capabilities and supporting better reporting and resource planning.

### Scope
This implementation focuses on updating the Course entity in the database to include an optional relationship to Teacher, defining API endpoints for managing teacher assignments to courses, and ensuring existing functionalities remain unaffected.

### Technology Stack
- **Backend Framework**: Flask (Python)
- **Database**: SQLite
- **Data Validation**: Marshmallow
- **Testing Framework**: pytest
- **Environment**: Python 3.x

---

## II. Architecture
### Module Structure
```
student_registration/
├── src/
│   ├── app.py               # Main application entry point
│   ├── models.py            # Database models (Updated to include teacher_id in Course)
│   ├── schemas.py           # Marshmallow schemas for validation (Updated to include Course assignment)
│   ├── routes.py            # API route definitions (Updated to include Course assignment and retrieval)
│   ├── db.py                # Database connection and initialization (Updated for migrations)
│   └── config.py            # Configuration settings
├── tests/
│   ├── test_routes.py       # Tests for API routes (Updated to cover course teacher assignments)
│   └── test_models.py       # Tests for database models (Updated to ensure integrity with new relationships)
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
```

### Module Responsibilities
- **app.py**: Modify the application to register new routes for assigning teachers to courses.
- **models.py**: Update Course model to add `teacher_id` as an optional field.
- **schemas.py**: Create Marshmallow schemas to validate incoming requests for course updates.
- **routes.py**: Define new routes for assigning teachers to courses and retrieving course details.
- **db.py**: Manage database migrations to add the `teacher_id` field to the Course table.
- **config.py**: Adjust configuration variables as needed.

---

## III. Data Model
### Entity: Course (updated)
- **id**: `INTEGER PRIMARY KEY AUTOINCREMENT`
- **name**: `TEXT NOT NULL` (Required)
- **level**: `TEXT NOT NULL` (Required)
- **teacher_id**: `INTEGER` (Optional, foreign key that references Teacher entity)

### Migration Strategy
- Add the `teacher_id` foreign key to the existing Course table during migration to maintain relationships without disrupting existing data.

SQL Command for migration:
```sql
ALTER TABLE courses ADD COLUMN teacher_id INTEGER;

CREATE TABLE teachers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE
);
```

---

## IV. API Design
### Endpoints

1. **Assign a Teacher to a Course**
   - **Method**: `PUT`
   - **Endpoint**: `/courses/{course_id}/assign-teacher`
   - **Request Body**:
     ```json
     {
       "teacher_id": "integer"
     }
     ```
   - **Responses**:
     - **200 OK**:
       ```json
       {
         "message": "Teacher successfully assigned to the course.",
         "course_id": "integer",
         "teacher_id": "integer"
       }
       ```
     - **404 Not Found** (if the course or teacher does not exist):
       ```json
       {
         "error": {
           "code": "E002",
           "message": "Course or Teacher not found."
         }
       }
       ```

2. **Retrieve Course with Assigned Teacher Information**
   - **Method**: `GET`
   - **Endpoint**: `/courses/{course_id}`
   - **Responses**:
     - **200 OK**:
       ```json
       {
         "course_id": "integer",
         "name": "string",
         "level": "string",
         "teacher": {
           "teacher_id": "integer",
           "name": "string"
         }
       }
       ```

---

## V. Implementation Details
### Database Initialization
- Update `db.py` to include logic for adding the `teacher_id` column to the Course table and managing migrations to preserve existing data integrity.

### Input Validation
- Create a Marshmallow schema for Course updates to validate that the teacher exists when assigning.

### Error Handling
- Ensure error handling is implemented for all endpoints, especially for cases where the referenced Course or Teacher does not exist.

### Request/Response Format
- Maintain the JSON format for API responses consistent with existing implementation practices.

---

## VI. Testing Strategy
### Test Coverage
- Create unit tests covering the assigning of teachers to courses and successful retrieval of course information, in addition to error handling for invalid associations.

### Testing Framework
- Utilize pytest for creating tests structured according to the existing `tests/` directory.

### Test Cases
1. **Assign Teacher to Course Tests**:
   - Test successful assignment of a teacher to a course.
   - Verify error handling when assigning a non-existent teacher.
   - Verify error handling when assigning to a non-existent course.

2. **Retrieve Course Tests**:
   - Check response structure and correctness of displayed teacher information for a course.

---

## VII. Deployment Considerations
### Configuration Management
- Update `README.md` with instructions on how teacher assignment APIs function and any necessary schema migration steps.

### Production Readiness
- Ensure that the application initializes and runs without manual intervention, includes health check endpoints, and that the migration for the Course updates can be executed effectively upon deployment.

---

## VIII. Documentation
### Deliverables
- Update `README.md` to include new API specifications for assigning teachers to courses and retrieving course details.
- Describe new functionality and endpoints with comprehensive explanations in the source code.

---

## IX. Success Criteria
- All functional requirements are satisfied regarding the association of teachers to courses, including successful database migrations and integrity checks.
- Maintain consistency with existing database structures, allowing for backward compatibility.

## X. Technical Trade-offs & Decisions
- **Optional teacher association**: Choosing to allow Courses to optionally have a teacher will increase the flexibility of course management.
- **Migration strategy**: The decision to alter the existing Courses table with a new column prevents data loss while requiring careful management of the application state during migration.

---

This implementation plan provides a comprehensive approach for integrating teacher relationships into the Course entity of the Student Registration Web Application, ensuring adherence to design standards, efficient API creation, and effective documentation practices.