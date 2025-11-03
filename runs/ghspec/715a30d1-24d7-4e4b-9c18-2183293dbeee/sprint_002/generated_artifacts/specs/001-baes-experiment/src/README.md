---
# README.md

## Project Overview

This project implements an API for managing student records using FastAPI and SQLAlchemy. The API supports creating new students and retrieving their details, including email addresses.

## How to Run the Project

1. **Set Up the Environment**:
   - Ensure you have Python 3.8 or newer installed.
   - Create a virtual environment and activate it:
     ```bash
     python -m venv venv
     source venv/bin/activate  # On Windows use `venv\Scripts\activate`
     ```

2. **Install Dependencies**:
   ```bash
   pip install fastapi sqlalchemy uvicorn pytest
   ```

3. **Run the Application**:
   ```bash
   uvicorn main:app --reload
   ```

## API Endpoints

### Create a Student
- **Endpoint**: POST `/students`
- **Request Body**:
    ```json
    {
        "name": "string",
        "email": "string"
    }
    ```
- **Response** (on success):
    ```json
    {
        "id": 1,
        "name": "string",
        "email": "string"
    }
    ```

### Fetch a Student by ID
- **Endpoint**: GET `/students/{id}`
- **Response** (on success):
    ```json
    {
        "id": 1,
        "name": "string",
        "email": "string"
    }
    ```

## Testing

1. **Run Tests**:
   - Ensure your test database is set up.
   - Run tests using the following command:
     ```bash
     pytest
     ```

2. **Unit Tests for Fetching Student Details with Email**:
   - Verify that querying with a valid student ID returns the correct student details, including the email.
   - Ensure that appropriate error messages are returned for invalid requests.

## Test Cases Implemented

- **Creating a Student with Email**: Validates successful creation and response structure.
- **Validating Student Creation**: Checks error responses when required fields are missing.
- **Retrieving a Student's Email**: Verifies email retrieval using valid IDs.

## Future Development
- Further testing to cover edge cases.
- Additional API endpoints for updating and deleting student records.

## Acknowledgments
- This project utilizes FastAPI for the API framework and SQLAlchemy for the ORM.
- Contributions and feedback are welcome.

---