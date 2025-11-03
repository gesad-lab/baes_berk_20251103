# Tasks: Add Teacher Relationship to Course Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- `src/models/course.py`
- `src/models/teacher.py`
- `src/migrations/migration.py`
- `src/api/routes/course_routes.py`
- `src/services/course_service.py`
- `tests/test_teacher_dal.py`
- `tests/test_teacher_api.py`

Instructions for Task Breakdown:
1. Identify which existing files need modifications
2. Create new files for new functionality
3. Ensure integration tasks are included
4. Maintain consistency with existing code style and patterns

---

## Task Breakdown

### Database Migration Tasks

- [ ] **Create migration script to add `teacher_id` to `courses` table**
  - **File**: `src/migrations/migration.py`
  - **Description**: Modify the migration script to incorporate a new column `teacher_id` with foreign key constraint referencing `teachers(id)`. Ensure that the migration is reversible.

### Data Access Layer Tasks

- [ ] **Update Course model to include `teacher_id` field**
  - **File**: `src/models/course.py`
  - **Description**: Modify the existing `Course` model to incorporate the new `teacher_id` relationship. Update the ORM mapping for the `Course` and `Teacher` as necessary.

- [ ] **Implement methods in DAL for managing teacher associations**
  - **File**: `src/services/course_service.py`
  - **Description**: Create methods to handle CRUD operations related to the course-teacher relationship (e.g., assign teacher, retrieve course with teacher details, update teacher assignment).

### API Tasks

- [ ] **Implement POST endpoint to assign a teacher to a course**
  - **File**: `src/api/routes/course_routes.py`
  - **Description**: Create the `POST /courses/{courseId}/assignTeacher` endpoint which accepts a `teacherId` and associates the teacher with the course using a service layer call.

- [ ] **Implement GET endpoint to retrieve course details with teacher information**
  - **File**: `src/api/routes/course_routes.py`
  - **Description**: Create the `GET /courses/{courseId}` endpoint that returns course details, including the associated teacher's name and email.

- [ ] **Implement PUT endpoint to update teacher assignment for a course**
  - **File**: `src/api/routes/course_routes.py`
  - **Description**: Create the `PUT /courses/{courseId}/assignTeacher` endpoint that allows updating the teacher assigned to the course.

### Service Layer Tasks

- [ ] **Enhance service layer to validate course and teacher associations**
  - **File**: `src/services/course_service.py`
  - **Description**: Implement validation logic to confirm that the provided `courseId` and `teacherId` exist. Ensure logging and appropriate error handling is integrated.

### Testing Tasks

- [ ] **Create unit tests for new DAL methods**
  - **File**: `tests/test_teacher_dal.py`
  - **Description**: Write unit tests for the methods managing course-teacher associations within the data access layer.

- [ ] **Create API tests for new endpoints**
  - **File**: `tests/test_teacher_api.py`
  - **Description**: Write integration tests for the new API endpoints defined for course-teacher associations, covering success and error scenarios.

### Documentation Tasks

- [ ] **Update API documentation to reflect new endpoints**
  - **File**: `docs/api_description.md`  (or equivalent documentation file)
  - **Description**: Add documentation for the new API endpoints, detailing the request and response formats, status codes, and examples.

### Integration Tasks

- [ ] **Perform integration testing to validate course-teacher relationship functionality**
  - **File**: Ensure thorough testing coverage within existing integration test suites
  - **Description**: Conduct tests that validate the linking of courses and teachers works seamlessly within the application after implementing all changes. 

- [ ] **Verify database migration in a staging environment**
  - **File**: N/A (Database verification process)
  - **Description**: Ensure that the migration has been applied successfully in a staging environment and does not affect existing Student or Course data.

---