# Updated README.md

# Course Management API Documentation

This document outlines the API endpoints for managing courses within our application.

## API Endpoints

### Create Course

- **POST /courses**
  
  Creates a new course in the system.

  **Request Body:**
  ```json
  {
      "name": "string, required", 
      "level": "string, required"
  }
  ```

  **Response:**
  A JSON object containing the created course:
  ```json
  {
      "name": "string",
      "level": "string"
  }
  ```

  **Validation:**
  - Both "name" and "level" fields are required.
  - The "level" must be one of the following valid formats: "Beginner", "Intermediate", "Advanced".

  **Error Response:**
  - If "name" or "level" is omitted:
    ```json
    {
        "error": {
            "code": "E001",
            "message": "The 'name' field is required."
        }
    }
    ```

### Retrieve Courses

- **GET /courses**

  Retrieves a list of all courses available in the system.

  **Response:**
  A JSON array of course objects:
  ```json
  [
      {
          "name": "string",
          "level": "string"
      },
      ...
  ]
  ```

## Database Migration

A new table named `Course` has been added to the database schema with the following fields:
- `name`: string (required)
- `level`: string (required)

This migration has been designed to preserve existing `Student` data while introducing the `Course` table.

## Conclusion

This API provides the necessary endpoints for the course functionality, ensuring validation and error handling are in place to guide the user effectively. For further details on implementation or usage, please refer to the respective service and validation layers in the codebase.