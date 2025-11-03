# README.md

# Course Management API

This API provides functionalities to manage courses within the application. It allows for the creation and retrieval of course records while preserving existing student data. 

## Setup Instructions

1. **Environment Setup**
   - Ensure you have Python and FastAPI installed. You can set up a virtual environment if necessary.
   - Install the required dependencies listed in the `requirements.txt` file:
     ```bash
     pip install -r requirements.txt
     ```

2. **Database Migration**
   - The schema will be automatically updated upon application startup. Ensure that your database is configured correctly.
   - The application uses Alembic for schema management; make sure migration configurations are in place.

## API Endpoints

### Create Course

- **Endpoint**: `POST /courses`
- **Description**: Creates a new course record.
- **Request Body**:
  ```json
  {
    "name": "Introduction to Python",
    "level": "Beginner"
  }
  ```
- **Response**:
  - **201 Created**: When course creation is successful.
    ```json
    {
      "id": 1,
      "name": "Introduction to Python",
      "level": "Beginner"
    }
    ```
  - **400 Bad Request**: If the request body is invalid or required fields are missing.
    ```json
    {
      "error": {
        "code": "E001",
        "message": "Invalid input. Name and level are required."
      }
    }
    ```

### Retrieve Courses

- **Endpoint**: `GET /courses`
- **Description**: Retrieves a list of all courses.
- **Response**:
  - **200 OK**: Returns the list of courses.
    ```json
    [
      {
        "id": 1,
        "name": "Introduction to Python",
        "level": "Beginner"
      },
      {
        "id": 2,
        "name": "Advanced JavaScript",
        "level": "Advanced"
      }
    ]
    ```
  - **404 Not Found**: If no courses exist.
    ```json
    {
      "error": {
        "code": "E002",
        "message": "No courses found."
      }
    }
    ```

## Error Handling

- The API ensures appropriate HTTP status codes are returned for both successful and erroneous requests.
- All error responses follow a consistent message format for client clarity.

## Data Integrity

- Existing student records remain untouched during the course data migration process.

## Next Steps

To improve the functionality and robustness of the API:

1. Implement comprehensive tests for the new Course feature, verifying the creation and retrieval processes.
2. Monitor API usage and gather feedback for future enhancements.

## License

This project is licensed under the MIT License - see the LICENSE file for details.