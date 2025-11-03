# Tasks: Add Email Field to Student Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- `src/api/student_api.py`
- `src/models/student_model.py`
- `src/db/db_setup.py`
- `tests/test_student_api.py`
- `tests/test_student_model.py`
- `README.md`

Instructions for Task Breakdown:
1. Identify which existing files need modifications
2. Create new files for new functionality
3. Ensure integration tasks are included
4. Maintain consistency with existing code style and patterns
---

## Tasks Breakdown

### 🌱 Task 1: Update Student Model
- **File**: `src/models/student_model.py`
  - [ ] Modify the `Student` class to include the `email` field: `email = Column(String, nullable=False)`
  - [ ] Ensure the file follows existing coding standards and style.

### 🌱 Task 2: Update Request & Response Models
- **File**: `src/models/student_model.py`
  - [ ] Update the `StudentCreate` class to include `email: EmailStr` for email validation.
  - [ ] Update the `StudentResponse` class to ensure the email is included in the response.

### 🌱 Task 3: Add API Endpoint for Creating Student
- **File**: `src/api/student_api.py`
  - [ ] Implement a `POST /students` endpoint to create a student with name and email.
  - [ ] Validate input using Pydantic and ensure appropriate error handling.

### 🌱 Task 4: Add API Endpoint for Retrieving Student
- **File**: `src/api/student_api.py`
  - [ ] Implement a `GET /students/{id}` endpoint to retrieve student details including email.
  - [ ] Ensure that a valid student ID fetches the correct details including the email.

### 🌱 Task 5: Add API Endpoint for Updating Student Email
- **File**: `src/api/student_api.py`
  - [ ] Implement a `PUT /students/{id}` endpoint to update a student’s email.
  - [ ] Validate that only the email can be updated and handle errors appropriately.

### 🌱 Task 6: Database Migration for Email Field
- **File**: `src/db/db_setup.py`
  - [ ] Create a migration script that adds the `email` column to the `students` table without data loss.
  - [ ] Use SQLite's `ALTER TABLE` command to ensure existing data is preserved.

### 🎭 Task 7: Update Error Handling for API
- **File**: `src/api/student_api.py`
  - [ ] Implement error handling for email validation and ensure meaningful error messages are returned.

### ✍️ Task 8: Implement Unit Tests
- **File**: `tests/test_student_api.py`
  - [ ] Write unit tests for the new `POST`, `GET`, and `PUT` endpoints, verifying response structures and error handling.

### 🧩 Task 9: Implement Integration Tests
- **File**: `tests/test_student_api.py`
  - [ ] Validate API functionality by ensuring the creation, retrieval, and updating of student records works as specified.

### 📚 Task 10: Update Documentation
- **File**: `README.md`
  - [ ] Add new API endpoints, request/response formats, and provide example payloads for creating and updating students.

### 🔄 Task 11: Version Control Cleanup
- **File**: N/A
  - [ ] Commit changes in small increments to maintain Git hygiene.
  - [ ] Ensure every commit explains the "why" behind the changes.

By following these tasks, the feature to add an email field to the Student entity will be implemented effectively and in alignment with the project standards.