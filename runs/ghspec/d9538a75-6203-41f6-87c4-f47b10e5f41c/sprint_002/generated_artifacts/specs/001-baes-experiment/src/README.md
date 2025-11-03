# README.md

# Student Entity Application

## Overview
The Student Entity Application is designed to manage student records, including their details and related functionalities. This application allows for the creation, retrieval, and management of student data through a simple API interface.

## Functional Requirements
1. The application must be updated to include an `email` field in the Student entity:
   - The `email` field must be a string and is required.

2. The application must provide API validation to ensure that:
   - The email field must be present and must conform to standard email format.

3. The database schema for the Student entity must include:
   - An `id` field (auto-incrementing integer).
   - A `name` field (string, required).
   - An `email` field (string, required).

4. The existing data in the Student entity must be preserved during the update, and necessary database migrations should be created to add the new email field without data loss.

## Development Steps
1. **Setup Environment**:
   - Create a virtual environment and install dependencies.
   - Add the relevant libraries to `requirements.txt`.

2. **Update the Student Model**:
   - Modify `models.py` to include `email` as a required field and add an email validation method.

3. **Database Migration**:
   - Create a migration script (`add_email_to_students.py`) to alter the existing `students` table to add the `email` field while preserving existing data.

4. **Implement API Endpoints**:
   - Update the `/students` endpoints in `routes.py` to handle the email field during creation.
   - Include validation for the email field:
     - Ensure the email is not empty.
     - Validate the format of the email address.
   - Implement error handling for required fields.

5. **Testing**:
   - Write unit tests for the API in `test_routes.py` using pytest, including tests for successful creation and retrieval as well as cases to check for missing and invalid email formats.
   - Ensure at least 70% coverage of business logic.

6. **Documentation**:
   - Prepare usage instructions in this README file.

7. **Validation**:
   - Perform manual testing using Postman or curl to verify API functionality.

## API Usage
- **Base URL**: `http://localhost:5000/api/v1/students`
  
### Create a Student
- **Endpoint**: `POST /students`
- **Request Body**: 
    ```json
    {
        "name": "John Doe",
        "email": "john.doe@example.com"
    }
    ```
- **Response**:
    - **201 Created** on success with student details.
    - **400 Bad Request** if the email format is invalid or if required fields are missing.

### Get a Student
- **Endpoint**: `GET /students/{id}`
- **Response**:
    - **200 OK** on success with student details.
    - **404 Not Found** if the student does not exist.

## Migration Instructions
To perform the migration and ensure the database is updated:
```bash
python migrations/add_email_to_students.py
```

## Contact
For any questions or issues, please contact the development team.