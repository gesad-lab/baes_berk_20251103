# Updated README.md

# Project Documentation for Teacher Management System

## Overview
This application provides functionality to manage teacher records, enabling administrators to add, retrieve, and validate teacher entries in a streamlined manner.

## User Scenarios

1. **Creating a New Teacher Record**:
   - **Given**: Valid values for the teacher's name and email.
   - **When**: The administrator submits a teacher creation request.
   - **Then**: A confirmation message is received, confirming the teacher has been successfully added to the system.

2. **Retrieving All Teachers**:
   - **When**: The administrator requests the list of teachers.
   - **Then**: A JSON array containing names and emails of all teachers in the system is returned.

3. **Validating Teacher Data Entries**:
   - **Given**: An invalid email format or a missing name.
   - **When**: The administrator attempts to create a teacher entry.
   - **Then**: Clear error messages are returned indicating which fields are invalid.

## Error Response Verification for Invalid Data

- When submitting a request to create a teacher with invalid data (such as an improperly formatted email or missing name), the system will respond with structured error messages. 

### Expected Error Messages:
- **Invalid Name**: 
  - Error Code: `E001`
  - Message: `"Field 'name' cannot be empty."`
  
- **Invalid Email Format**: 
  - Error Code: `E002`
  - Message: `"Invalid email format provided for 'email'."`

These error messages will guide the administrator on how to rectify the data and ensure successful record creation.

## Success Criteria
1. The application creates a Teacher entity and returns a confirmation message upon successful addition.
2. The application retrieves and displays a list of all teachers in JSON format.
3. The application validates input fields correctly and provides actionable error messages for invalid entries.
4. The database schema is updated with a new Teacher table without compromising the integrity of existing Student and Course data.

## Assumptions
- Administrators are expected to provide valid data (non-empty for name and valid format for email).
- The system ensures data validation and returns appropriate error messages for invalid input.
- Adding the Teacher entity will not interfere with existing functionality related to Students or Courses.

## Installation and Setup

1. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Run the database migrations to create the necessary tables:
   ```
   flask db upgrade
   ```

3. Start the application:
   ```
   flask run
   ```

## API Usage

### Create Teacher
- **Endpoint**: `POST /api/v1/teachers`
- **Request Body**:
  ```json
  {
    "name": "John Doe",
    "email": "john.doe@example.com"
  }
  ```
- **Responses**:
  - **Success**: `201 Created` with confirmation message.
  - **Error**: `400 Bad Request` with details on input validation failures.

### Retrieve Teachers
- **Endpoint**: `GET /api/v1/teachers`
- **Responses**:
  - **Success**: `200 OK` with a JSON array of teachers' names and emails.

### Additional Information
For comprehensive examples and further details on all available endpoints, refer to the API documentation within the codebase.

## Contribution
If you'd like to contribute to the development, please review the contribution guidelines and submit issues or pull requests in the GitHub repository.

---

This README update reflects the requirements for verifying error responses for invalid data during teacher record creation, aligning with the provided specifications and goals.