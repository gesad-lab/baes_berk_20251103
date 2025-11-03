# Tasks: Add Email Field to Student Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- models/student.py (545 bytes)
- tests/test_app.py (1144 bytes)

---

## Task 1: Update Student Model to Include Email Field
- **Description**: Modify the existing Student model to add an email attribute.
- **File Path**: `models/student.py`
- **Dependencies**: None
- **Testability**: Verify the model definition after modification for correctness.

```markdown
- [ ] **Modify the Student class** in `models/student.py` to add the `email` attribute with required validation.
```

---

## Task 2: Implement Database Migration for Email Field
- **Description**: Create a database migration script to add the email column in the students table.
- **File Path**: `migrations/add_email_to_students.py` (new file)
- **Dependencies**: Task 1
- **Testability**: Execute the migration and confirm that the new column is present in the database and can accept data.

```markdown
- [ ] **Create a migration script** in `migrations/add_email_to_students.py` to add the `email` column to the students table.
```

---

## Task 3: Update Create Student API Endpoint
- **Description**: Modify the `POST /students` endpoint to require an email field and implement validation logic.
- **File Path**: `app/api.py` (or equivalent file where the API is defined)
- **Dependencies**: Task 1
- **Testability**: Test the API endpoint with and without the email field to verify the responses.

```markdown
- [ ] **Update the implementation of the POST /students endpoint** in `app/api.py` to require the email field and return appropriate responses.
```

---

## Task 4: Update Retrieve All Students API Endpoint
- **Description**: Ensure that the `GET /students` endpoint includes the new email field in the response.
- **File Path**: `app/api.py`
- **Dependencies**: Task 1
- **Testability**: Call the endpoint and confirm that the email field is present in the returned student data.

```markdown
- [ ] **Modify the implementation of the GET /students endpoint** in `app/api.py` to return the email field in the response.
```

---

## Task 5: Implement Email Validation Logic in Service Layer
- **Description**: Add logic to validate the email format for new students in the service layer.
- **File Path**: `app/services/student_service.py` (or equivalent service file)
- **Dependencies**: Task 1
- **Testability**: Validate scenarios of correct, incorrect, and missing email formats.

```markdown
- [ ] **Add email validation function** in `app/services/student_service.py` to ensure all email inputs meet standard formatting rules.
```

---

## Task 6: Create Unit Tests for Student Creation
- **Description**: Write unit tests to verify the creation of a Student with valid email and handle invalid entries.
- **File Path**: `tests/test_student.py` 
- **Dependencies**: Tasks 3, 5
- **Testability**: Run tests to check for proper handling of requests including valid and invalid email data.

```markdown
- [ ] **Write unit tests in `tests/test_student.py`** for creating a student with valid email and ensure it catches errors for missing or invalid emails.
```

---

## Task 7: Create Unit Tests for Retrieving All Students
- **Description**: Write tests to check retrieval of all students ensuring they include email data.
- **File Path**: `tests/test_student.py`
- **Dependencies**: Task 4
- **Testability**: Execute the tests to confirm all student data includes the email field.

```markdown
- [ ] **Write tests in `tests/test_student.py`** to ensure the `GET /students` endpoint retrieves all student records with email fields present.
```

---

## Task 8: Update README.md with New API Changes
- **Description**: Document the new email field requirements and API endpoints in the README file.
- **File Path**: `README.md`
- **Dependencies**: Tasks 3, 4
- **Testability**: Confirm that the changes are clear and the documentation accurately reflects the API changes.

```markdown
- [ ] **Update `README.md`** to include new endpoint specifications and details regarding the email field integration.
```

---

## Task 9: Execute Database Migration at Startup
- **Description**: Ensure the migration script runs automatically when the application starts.
- **File Path**: `app/__init__.py` (or where application startup is managed)
- **Dependencies**: Task 2
- **Testability**: Start the application and confirm the schema includes the email field without errors.

```markdown
- [ ] **Modify the application startup logic in `app/__init__.py`** to execute the migration script for adding the email field.
```

--- 

This task breakdown prioritizes small, actionable items, ensuring each can be tested independently while maintaining coherent dependencies.