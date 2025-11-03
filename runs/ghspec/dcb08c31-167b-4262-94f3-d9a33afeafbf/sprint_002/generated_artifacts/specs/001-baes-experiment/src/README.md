# README.md

# Student Records API

## Overview

This API allows for the management of student records, including adding new students and retrieving existing student data. The records now include an email field that is required for each student.

## Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone <repository_url>
   cd <repository_name>
   ```

2. **Install the dependencies**:
   Make sure you have Python and pip installed, then run:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run database migrations**:
   Run the following command to apply the necessary database schema updates:
   ```bash
   flask db upgrade
   ```

4. **Start the Flask application**:
   After completing the installation and migration, start the application:
   ```bash
   flask run
   ```

## API Endpoints

### POST /students

- **Description**: Add a new student record with a name and email.
- **Request Body**:
   ```json
   {
     "name": "John Doe",
     "email": "john.doe@example.com"
   }
   ```
- **Responses**:
  - **201 Created**:
    ```json
    {
      "id": 1,
      "name": "John Doe",
      "email": "john.doe@example.com"
    }
    ```
  - **400 Bad Request**: If the input validation fails for missing or invalid email format:
    ```json
    {
      "error": {
        "code": "E001",
        "message": "Invalid email format.",
        "details": {}
      }
    }
    ```

### GET /students

- **Description**: Retrieve all student records.
- **Responses**:
  - **200 OK**:
    ```json
    [
      {
        "id": 1,
        "name": "John Doe",
        "email": "john.doe@example.com"
      },
      {
        "id": 2,
        "name": "Jane Smith",
        "email": "jane.smith@example.com"
      }
    ]
    ```

## Error Handling

The API will return structured error responses whenever a request fails due to input validation errors:

- **400 Bad Request**: When the email is missing or invalid, the API will provide an error message indicating the problem.

## Testing

- The application includes unit tests located in the `tests/` directory that verify the correct handling of student records, including the new email field.
- To run the tests, use the following command:
   ```bash
   pytest
   ```

## Conclusion

This API provides a robust way to manage student records, ensuring that all entries are validated and stored securely with the addition of an email field.