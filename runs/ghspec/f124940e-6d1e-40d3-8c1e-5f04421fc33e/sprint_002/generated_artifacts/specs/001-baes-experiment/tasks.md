# Tasks: Add Email Field to Student Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- `src/models.py` (to modify Student entity)
- `src/services/student_service.py` (CRUD operations)
- `src/routers/student_router.py` (API routes)
- `tests/test_student.py` (to add new test cases)

---

## Task Breakdown

### Task 1: Update Student Model
- **File**: `src/models.py`  
- **Description**: Modify the existing Student SQLAlchemy model to include the new `email` field.
- **Subtasks**:
  - Add `email = Column(String, nullable=False)` to the `Student` class.
  - Implement a method to validate email formats within the `Student` model.
- **Testable**: Ensure the model is reflected correctly in DB migrations.
- [ ] Modify Student model to include email field in `src/models.py`.

---

### Task 2: Create Database Migration
- **File**: `migrations/versions/` (new directory for migration scripts)  
- **Description**: Generate a migration script using Alembic to add the `email` column to the `students` table without losing existing data.
- **Subtasks**:
  - Run `alembic revision --autogenerate -m "Add email to students"` to create a new migration file.
  - Ensure migration script accurately reflects adding the `email` column.
- **Testable**: Run migration and verify the database schema.
- [ ] Create database migration script to add email column.

---

### Task 3: Update API Routes
- **File**: `src/routers/student_router.py`  
- **Description**: Update the API endpoints to handle email in student related requests.
- **Subtasks**:
  - Modify the POST `/students` route to accept an email field in the request body.
  - Modify the PUT `/students/{id}` route to accept an email field in the request body.
  - Ensure email validation logic is included.
- **Testable**: Check if new routes are correctly processing requests with email.
- [ ] Update API routes in `src/routers/student_router.py`.

---

### Task 4: Update CRUD Operations
- **File**: `src/services/student_service.py`  
- **Description**: Modify the student service methods to include logic for managing email (creating, updating).
- **Subtasks**:
  - Include logic to handle email storage when creating and updating student records.
- **Testable**: Ensure that CRUD operations work as intended with email.
- [ ] Update CRUD operations in `src/services/student_service.py`.

---

### Task 5: Implement Input Validation
- **File**: `src/schemas.py` (new file to define request/response schemas for validation)  
- **Description**: Create or update Pydantic models to validate request data including the email field.
- **Subtasks**:
  - Define data models for creation and updating of students that include email validation.
- **Testable**: Ensure request validation fails for invalid emails.
- [ ] Implement input validation using Pydantic in `src/schemas.py`.

---

### Task 6: Write Unit Tests for New Functionality
- **File**: `tests/test_student.py`  
- **Description**: Write unit tests for all new functionality related to student email handling.
- **Subtasks**:
  - Test creating a student with a valid email.
  - Test updating a student’s email.
  - Test handling of invalid email formats.
- **Testable**: Run tests to assure coverage and correct handling of email operations.
- [ ] Write unit tests for email handling in `tests/test_student.py`.

---

### Task 7: Document API Changes
- **File**: `README.md` (or `docs/api_reference.md`)  
- **Description**: Update existing API documentation to reflect changes related to the email field in the Student entity.
- **Subtasks**:
  - Document endpoints including the email parameter and validation rules.
- **Testable**: Review the documentation to ensure it correctly describes the behavior of the API.
- [ ] Update API documentation in `README.md`.

---

### Task 8: Testing Migration and Rollback
- **File**: `tests/test_migrations.py` (new file for migration tests)  
- **Description**: Write tests to ensure the database migration adds the email column correctly and can roll back if necessary.
- **Subtasks**:
  - Implement tests that verify the column is added and existing records remain intact.
- **Testable**: Confirm the migration tests run successfully and maintain database integrity.
- [ ] Write tests for database migrations in `tests/test_migrations.py`.

---

### Task 9: Security Review
- **File**: `src/security.py` (optional new file to handle email security)  
- **Description**: Review and if necessary implement email sanitization and validation measures to avoid injection attacks.
- **Subtasks**:
  - Ensure all email storage and handling adheres to security best practices.
- **Testable**: Validate inputs to assure no vulnerabilities exist regarding email handling.
- [ ] Review and implement security measures for email handling.

---

## Actionable Checklist
- [ ] Task 1: Update Student Model
- [ ] Task 2: Create Database Migration
- [ ] Task 3: Update API Routes
- [ ] Task 4: Update CRUD Operations
- [ ] Task 5: Implement Input Validation
- [ ] Task 6: Write Unit Tests for New Functionality
- [ ] Task 7: Document API Changes
- [ ] Task 8: Testing Migration and Rollback
- [ ] Task 9: Security Review 

---

This structured breakdown provides clear, actionable tasks for implementing the feature to add an email field to the Student entity, ensuring maintainability and adherence to project principles.