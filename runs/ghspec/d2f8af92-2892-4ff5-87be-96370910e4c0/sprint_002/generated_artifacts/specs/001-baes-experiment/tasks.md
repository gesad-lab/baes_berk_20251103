# Tasks: Add Email Field to Student Entity

---

## Task Breakdown

### Task 1: Update Student Model to Include Email Field  
- **File**: `models/student.py`
- **Action**: Modify the `Student` class to include an `email` attribute that is a required string.
- **Description**: Update the SQLAlchemy model to add the new `email` field in the class definition, ensuring it is marked as non-nullable.
- **Testable**: No breaking changes; merely updates the model.
- **Checkbox**: [ ]  

### Task 2: Create Migration Script for Email Column  
- **File**: Create new file `migrations/add_email_to_students.py`
- **Action**: Write a migration script to add the `email` column to the `students` table in the database.
- **Description**: Use Alembic to create and implement the migration that preserves existing data.
- **Testable**: Run migration script and check the database for the presence of the `email` column after migration.
- **Checkbox**: [ ]  

### Task 3: Update API Layer to Handle Email in Create Student Endpoint  
- **File**: `api/student_api.py`
- **Action**: Modify the POST `/api/v1/students` endpoint to include `email` in the request body.
- **Description**: Ensure that the endpoint can accept the new email field and correctly respond with the created student record.
- **Testable**: Test by sending a valid JSON payload that includes name and email and confirm successful creation response.
- **Checkbox**: [ ]  

### Task 4: Update API Layer to Handle Email in Update Student Endpoint  
- **File**: `api/student_api.py`
- **Action**: Modify the PUT `/api/v1/students/{id}` endpoint to allow updating the `email` field.
- **Description**: Ensure the endpoint can handle updates to the email and reflects these changes in the response.
- **Testable**: Test by sending a valid update request with a new email for an existing student record.
- **Checkbox**: [ ]  

### Task 5: Implement Email Validation Logic in Service Layer  
- **File**: `services/student_service.py`
- **Action**: Add email format validation when creating or updating student records.
- **Description**: Use a regular expression or suitable method to validate the format of the email before processing the request.
- **Testable**: Test to confirm invalid email formats trigger relevant error messages.
- **Checkbox**: [ ]  

### Task 6: Create Unit Tests for Create Student with Email  
- **File**: `tests/test_student_api.py`
- **Action**: Write tests to verify the creation of a student including the email field.
- **Description**: Ensure new tests cover scenarios for valid and invalid email formats upon creation.
- **Testable**: Execute tests and verify the correct success/failure responses correspond to the input conditions.
- **Checkbox**: [ ]  

### Task 7: Create Unit Tests for Update Student Email  
- **File**: `tests/test_student_api.py`
- **Action**: Write tests to verify that updating a student’s email works correctly.
- **Description**: Include tests that check both successful updates and appropriate failures for invalid email formats.
- **Testable**: Run the defined tests to check the outcome against expectations.
- **Checkbox**: [ ]  

### Task 8: Update README Documentation  
- **File**: `README.md`
- **Action**: Document the new requirement for the email field within the API specifications.
- **Description**: Include instructions on how to create and update students, emphasizing the new email attribute and any related constraints.
- **Testable**: Review README to ensure clarity and accuracy regarding the new changes.
- **Checkbox**: [ ]  

### Task 9: Run Migration and Verify Database Schema  
- **File**: Migration script file & Database
- **Action**: Execute the migration script and check the database schema.
- **Description**: Validate that the `students` table now includes the new `email` field without losing existing data.
- **Testable**: Confirm by querying the database to ensure the `email` column exists and data integrity is maintained.
- **Checkbox**: [ ]  

### Task 10: Validate Overall Test Coverage  
- **File**: `tests/test_coverage_report.py`
- **Action**: Measure test coverage to ensure it meets the 70% requirement for new business logic.
- **Description**: Check integration of new tests to confirm adequate coverage of email-related functionalities.
- **Testable**: Generate a coverage report after running tests and check if the coverage percentage meets the criteria.
- **Checkbox**: [ ]  

---

This structured task breakdown provides clear responsibilities for implementing the new email feature in the Student entity, ensuring that files are modified appropriately while maintaining the overall integrity and performance of the existing application.