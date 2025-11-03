# Tasks: Add Email Field to Student Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- `src/models/student.py` (340 bytes)
- `src/services/student_service.py` (822 bytes)
- `src/api/student_api.py` (456 bytes)
- `tests/test_student_api.py` (3939 bytes)
- `tests/test_student_service.py` (1922 bytes)
- `README.md` (1500 bytes)

## Task Breakdown

### Database Schema Update

- [ ] **Task 1: Update Student Model to Include Email Field**  
  **File**: `src/models/student.py`  
  Modify the `Student` model to add a new email field.  
  _Add the line `email = Column(String, nullable=False)` to the model definition._

- [ ] **Task 2: Create Database Migration for Email Field**  
  **File**: `src/migrations/versions/2023_10_12_0001_add_email_field.py`  
  Create a migration script to add the email field to the students table.  
  _Ensure the `upgrade` and `downgrade` functions are accurately defined._

### API Layer Changes

- [ ] **Task 3: Update API Endpoint for Creating Students**  
  **File**: `src/api/student_api.py`  
  Modify the `POST /students` endpoint to accept an email in the request body.  
  _Update the function to include email in both the request validation and response._

- [ ] **Task 4: Update API Endpoint for Updating Student Email**  
  **File**: `src/api/student_api.py`  
  Modify the `PUT /students/{id}` endpoint to allow updating the student's email.  
  _Include necessary validation to check for email format._

- [ ] **Task 5: Update API Endpoint for Retrieving All Students**  
  **File**: `src/api/student_api.py`  
  Ensure the `GET /students` endpoint returns the email field in the response.  
  _Adjust the response structure to include the email addresses._

### Service Layer Updates

- [ ] **Task 6: Modify Student Service to Handle Email**  
  **File**: `src/services/student_service.py`  
  Update the `create_student` and `update_student` functions to manage the new email input.  
  _Include logic for validating the email format and ensuring it's saved correctly._

### Validation Layer Updates

- [ ] **Task 7: Implement Email Validation Logic**  
  **File**: `src/validation/student_validation.py` (new file needed)  
  Create a new file for validation logic and implement email format checks.  
  _Use regex or similar methods to validate incoming email addresses._

### Testing

- [ ] **Task 8: Add Unit Tests for Email Validation**  
  **File**: `tests/test_student_service.py`  
  Create tests to validate the email format in the service layer.  
  _Ensure coverage for both valid and invalid email scenarios._

- [ ] **Task 9: Add Integration Tests for Email Handling**  
  **File**: `tests/test_student_api.py`  
  Create new tests to verify the API correctly handles email during student creation and updating.  
  _Ensure responses match expectations in various scenarios._

### Documentation

- [ ] **Task 10: Update README.md for API Documentation**  
  **File**: `README.md`  
  Document changes related to the email field in the API contracts.  
  _Provide examples for creating and updating students with emails._

- [ ] **Task 11: Update Docstrings for New and Modified Functions**  
  **File**: `src/api/student_api.py`, `src/services/student_service.py`  
  Ensure all functions related to email handling have accurate and complete docstrings.  
  _Follow the format of existing documentation for consistency._

---

This breakdown provides a structured approach to implement the new email field for the Student entity while ensuring that each task is focused, independent, and aligned with existing project practices.