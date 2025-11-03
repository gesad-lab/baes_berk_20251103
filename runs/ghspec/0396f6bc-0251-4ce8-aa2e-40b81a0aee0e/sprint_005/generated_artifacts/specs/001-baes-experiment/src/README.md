# README.md

# Project Title

## Overview
This project serves as a backend API for managing teachers in an educational application. It allows administrators to create and retrieve teacher information effectively. 

## API Endpoints

### Create Teacher
- **Endpoint**: `POST /teachers`
- **Request Body**:
    ```json
    {
      "name": "string", // required
      "email": "string" // required
    }
    ```
- **Response**: 
    ```json
    {
      "message": "Teacher created successfully."
    }
    ```
- **Description**: This endpoint allows an admin to create a new teacher by providing their name and email. The request must include both fields for successful creation.

### Retrieve Teachers
- **Endpoint**: `GET /teachers`
- **Response**:
    ```json
    {
      "teachers": [
        {
          "id": "integer",
          "name": "string",
          "email": "string"
        }
      ]
    }
    ```
- **Description**: This endpoint retrieves a list of all teachers in the system, providing their IDs, names, and email addresses.

## Error Handling
- If validation fails (e.g., missing `name` or `email`), the API will return a `400 Bad Request` status with a message indicating the issue.

### Example Error Response:
```json
{
  "error": {
    "code": "E001",
    "message": "Validation error: 'name' and 'email' are required."
  }
}
```

## Usage Instructions
1. To create a teacher, send a POST request to `/teachers` with the required JSON body.
2. To retrieve the list of teachers, send a GET request to `/teachers`.

## Setup Instructions
- Clone the repository and navigate into the project directory.
- Use Poetry to install the necessary dependencies:
    ```bash
    poetry install
    ```
- Run the application:
    ```bash
    # Include command to start application, e.g.,
    uvicorn your_app:app --reload
    ```

## Testing
- Tests can be run using Pytest:
    ```bash
    pytest
    ```

## Contributing
If you would like to contribute to this project, please fork the repository and submit a pull request with your improvements or bug fixes.

## License
This project is licensed under the MIT License - see the LICENSE file for details.