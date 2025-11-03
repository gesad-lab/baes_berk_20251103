# Tasks: Add Email Field to Student Entity

---

INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- `src/models.py`
- `src/services.py`
- `src/api.py`
- `src/database.py`
- `tests/test_api.py`
- `tests/test_services.py`

## Task Breakdown

### 1. Update Model for Email Field
- **Task**: Modify Student model to include the email field.
- **File**: `src/models.py`
- **Description**: Add `email` attribute to the `Student` class to store student's email.
- **Dependencies**: None.
- **Testable**: Model can be tested by validating schema structure.

```python
# Update the Student model in src/models.py
```
- [ ] Update Student model to include `email` field

### 2. Database Migration Setup
- **Task**: Create migration script to add email column to students table.
- **File**: `src/database.py`
- **Description**: Implement Alembic migration that adds the `email` column while preserving existing records.
- **Dependencies**: Task 1.
- **Testable**: Validate migration by running it on a test database.

```python
# Add an Alembic migration script in src/database.py
```
- [ ] Create migration script to add email column

### 3. Update API Endpoints
- **Task**: Modify the API endpoints for student CRUD operations to include email field handling.
- **File**: `src/api.py`
- **Description**: Adjust existing endpoints to incorporate email validation and return the email in responses.
- **Dependencies**: Task 1.
- **Testable**: Can be tested through API calls.

```python
# Update POST and PUT methods in src/api.py for email incorporation
```
- [ ] Update POST endpoint to include email handling
- [ ] Update GET endpoint to return email
- [ ] Update PUT endpoint to manage email updates

### 4. Enhance Business Logic
- **Task**: Add email validation logic to service layer.
- **File**: `src/services.py`
- **Description**: Implement functions for validating email format using regex, leverage Pydantic for input models.
- **Dependencies**: Task 1.
- **Testable**: Verify validation logic through unit tests.

```python
# Add email validation logic in individual service methods in src/services.py
```
- [ ] Implement email format validation logic in services.py

### 5. Input Validation using Pydantic
- **Task**: Create Pydantic models for input validation involving email.
- **File**: `src/api.py`
- **Description**: Define `StudentCreate` and `StudentUpdate` models to utilize email validation and ensure inputs are correctly formatted.
- **Dependencies**: Task 1.
- **Testable**: Input validation can be tested through endpoint tests.

```python
# Define Pydantic models within src/api.py for student creation/updating
```
- [ ] Create Pydantic input models for Student creation and updating

### 6. Update API Tests
- **Task**: Write tests for new email functionality in API.
- **File**: `tests/test_api.py`
- **Description**: Add unit tests to cover scenarios for creating a student with email, retrieving student details including email, and error handling for missing/invalid email.
- **Dependencies**: Tasks 3 and 4.
- **Testable**: Can run tests to verify API behavior.

```python
# Add new tests in tests/test_api.py to cover email scenarios
```
- [ ] Write tests for successful student creation with email
- [ ] Write tests for retrieving student details including email
- [ ] Write tests for updating a student's email
- [ ] Write tests for creating a student without email (400 error)
- [ ] Write tests for invalid email format handling (400 error)

### 7. Update Service Tests
- **Task**: Write unit tests for email handling in services.
- **File**: `tests/test_services.py`
- **Description**: Ensure the service logic related to email formatting validation and error handling is adequately covered.
- **Dependencies**: Task 4.
- **Testable**: Independent unit tests can confirm business logic.

```python
# Add tests in tests/test_services.py for email validation logic
```
- [ ] Write tests for email format validation in service layer

### 8. Docker Configuration Update
- **Task**: Ensure Docker setup supports new migrations.
- **File**: `Dockerfile` / `docker-compose.yml`
- **Description**: Update necessary files to include migrations on startup or build.
- **Dependencies**: None.
- **Testable**: Docker deployment should correctly handle migrations.

```dockerfile
# Modify Docker configurations to ensure migrations happen on startup
```
- [ ] Update Docker configuration to handle migrations properly

---

Each task is self-contained, focuses on a single aspect of the implementation plan, and ensures the project adheres to the specified guidelines and coding standards. All tasks are organized by dependency, allowing for independent execution and testing.