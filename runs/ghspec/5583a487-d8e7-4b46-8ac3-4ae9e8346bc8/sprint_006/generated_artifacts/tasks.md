# Tasks: Add Teacher Relationship to Course Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- src/models/course.py (500 bytes)
- src/models/teacher.py (550 bytes)
- src/api/course.py (760 bytes)
- tests/test_create_course.py (1200 bytes)
- tests/test_get_course.py (1100 bytes)

## Task Breakdown

- [ ] **Update Course Model to Include Teacher Relationship**  
  **File**: `src/models/course.py`  
  - Modify the existing Course model to include a new field `teacher_id` referencing the Teacher entity.  
  - Ensure the SQLAlchemy relationship is established with the Teacher model.
  
- [ ] **Update Teacher Model if Necessary**  
  **File**: `src/models/teacher.py`  
  - Ensure the Teacher model has a reverse relationship defined back to the Course. If not, add `courses` relationship in the Teacher model.

- [ ] **Create Migration Script for Database Schema Update**  
  **File**: `migrations/versions/` (create new migration script)  
  - Generate a migration that adds the `teacher_id` foreign key to the existing Course table.
  
- [ ] **Update API Endpoint for Creating Courses**  
  **File**: `src/api/course.py`  
  - Implement logic in the `POST /courses` endpoint to handle the `teacher_id` field from the request body. Validate the presence of `teacher_id`.

- [ ] **Update API Endpoint for Retrieving Courses**  
  **File**: `src/api/course.py`  
  - Implement logic in the `GET /courses/{id}` endpoint to include associated Teacher details in the response. 

- [ ] **Implement Input Validation for Course Creation**  
  **File**: `src/api/course.py`  
  - Ensure incoming requests to create or update a Course must include a valid `teacher_id` that corresponds to an existing Teacher.

- [ ] **Write Automated Unit Tests for Course Creation**  
  **File**: `tests/test_create_course.py`  
  - Write tests to validate successful course creation with a valid `teacher_id` along with edge cases (e.g., missing `teacher_id`).

- [ ] **Write Automated Unit Tests for Course Retrieval**  
  **File**: `tests/test_get_course.py`  
  - Write tests to validate retrieval of a Course, ensuring it includes Teacher details.

- [ ] **Update API Documentation**  
  **File**: `docs/api_specification.md` (or relevant API documentation file)  
  - Add new endpoint details for `POST /courses` and `GET /courses/{id}` including request/response formats.

- [ ] **Update Environment Configuration**  
  **File**: `.env.example`  
  - Document any new environment variables needed for the Teacher and Course relationship logic (if applicable).

- [ ] **Run Migrations on Application Startup**  
  **File**: `src/__init__.py` (or application startup script)  
  - Ensure migrations are applied automatically on application startup to initialize the database schema correctly.

- [ ] **Implement Health Check Endpoint**  
  **File**: `src/api/health.py` (create new file if it doesn’t exist)  
  - Implement an endpoint to check application status, which is useful for monitoring post-deployment.

---

This structured approach ensures that each task can be executed independently and tested, while following the guidelines for consistency and maintainability in the existing codebase.