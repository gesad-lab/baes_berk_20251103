```markdown
# README.md

# Student Management System

## Overview
This application allows users to manage student records, including names and email addresses. The application utilizes a service layer for handling business logic, ensuring a clean separation of concerns.

## Features
- Create a student with a name and email
- Retrieve a list of all students with their names and emails
- Error handling for missing or invalid email formats

## Functional Requirements
1. The application must allow users to create a student with both a name and an email (both required).
2. The application must respond to requests with JSON formatted responses.
3. The Student entity must now include:
   - `id`: Integer (auto-incremented, primary key)
   - `name`: String (required)
   - `email`: String (required, must be a valid format)
   
## User Scenarios & Testing
1. **Creating a Student with Email**
   - **Scenario**: A user wants to add a new student along with their email.
   - **Test**: The user sends a request to create a student with a valid name and email. The system should respond with a JSON confirmation, including the student's ID, name, and email.

2. **Retrieving Students with Email**
   - **Scenario**: A user wants to view all students with their emails.
   - **Test**: The user sends a request to retrieve a list of all students. The system should return a JSON array of all student records, each containing the name and email.

3. **Handling Missing Email**
   - **Scenario**: A user tries to create a student without an email field.
   - **Test**: The user sends a request with a valid name but missing email. The system should respond with an error message specifying that the email is required.

4. **Handling Invalid Email Format**
   - **Scenario**: A user tries to create a student with an improperly formatted email.
   - **Test**: The user sends a request with a valid name but an invalid email. The system should respond with an error message specifying that the email format is invalid.

5. **Data Persistence with Email**
   - **Scenario**: A user creates a student with an email and then restarts the application.
   - **Test**: The user should see the previously created student (with email) still present after the application restarts.

## Success Criteria
- The application must successfully create a student with a valid name and email 95% of the time in testing.
- The application must return a correct JSON response format for all endpoints without errors.
- The system must handle invalid input (missing name or email) gracefully, returning appropriate error messages 100% of the time.
- After the application restarts, previously added students (with their names and emails) must still be retrievable, confirming data persistence.

## API Endpoints
- `POST /students`: Create a new student with a name and email.
- `GET /students`: Retrieve all students.

## Error Responses
- If the email is missing: `{"error": {"code": "E001", "message": "Email is required."}}`
- If the email format is invalid: `{"error": {"code": "E002", "message": "Invalid email format."}}`

## Development Setup
1. Clone the repository
2. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```
3. Set up environment variables as required in `.env.example`
4. Run migrations to update the database schema

## Testing
Use `pytest` to run all tests. Ensure that you meet the minimum coverage requirements.

## Contributions
For contributions, please adhere to the existing coding style and ensure that new features are covered by tests.
```