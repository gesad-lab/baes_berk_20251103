# README.md

# Student Management Application

## Overview & Purpose

The purpose of this web application is to manage Student entities. Each Student will have a required name field. This application serves as an interface to create and retrieve students via a RESTful API, returning JSON responses for easy consumption by frontend applications or other services.

## Functional Requirements

### 1. Create Student Endpoint
- **HTTP Method**: POST
- **Endpoint**: `/students`
- **Request Body**:
  - `name`: string (required)
- **Response**:
  - **On success (HTTP 201)**:
    - JSON object containing:
      - `id`: integer (auto-generated)
      - `name`: string
  - **On failure (HTTP 400)**:
    - JSON object with an error message.

### 2. Retrieve Student Endpoint
- **HTTP Method**: GET
- **Endpoint**: `/students/{id}`
- **Response**:
  - **On success (HTTP 200)**:
    - JSON object containing:
      - `id`: integer
      - `name`: string
  - **On failure (HTTP 404)**:
    - JSON object with a message indicating the Student was not found.

## User Scenarios & Testing

1. **Creating a Student**:
   - **Scenario**: A user sends a request to create a new Student with a valid name.
   - **Expected Result**: The application stores the Student in the database and responds with the created Student object, including an ID and a status message.

2. **Retrieving a Student**:
   - **Scenario**: A user sends a request to retrieve a Student by ID.
   - **Expected Result**: The application returns the requested Student object as a JSON response.

3. **Creating a Student with Missing Name**:
   - **Scenario**: A user attempts to create a Student without a name.
   - **Expected Result**: The application responds with a validation error indicating that the name field is required.

4. **Retrieving a Non-existent Student**:
   - **Scenario**: A user attempts to retrieve a Student that does not exist.
   - **Expected Result**: The application returns a 404 status code with a message indicating that the Student was not found.

## Setup and Configuration

1. **Environment Setup**:
   Use a virtual environment.
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

2. **Install Dependencies**:
   ```bash
   pip install Flask SQLAlchemy pytest
   ```

3. **Database Initialization**:
   In `database.py`, define functionality to create the SQLite database and tables on application startup.

4. **Error Handling**:
   Use Flask error handlers for capturing validation errors and returning appropriate HTTP status codes.

## Testing

Run the unit tests to ensure functionality works as expected:

```bash
pytest tests/test_student.py
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.