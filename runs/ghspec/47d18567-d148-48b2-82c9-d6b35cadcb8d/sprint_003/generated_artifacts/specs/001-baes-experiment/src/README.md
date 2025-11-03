# Updated README.md

# Student Management App

## Overview
The Student Management App provides functionalities to manage students and courses within an educational application. This documentation covers the API endpoints, including their usage and examples.

## API Endpoints

### Course Entity Endpoints

#### 1. Creating a New Course
- **Endpoint**: `POST /api/v1/courses`
- **Request Body**:
    ```json
    {
        "name": "Course Name",
        "level": "Level"
    }
    ```
- **Responses**:
    - **201 Created**: Returns the details of the created course.
        ```json
        {
            "id": 1,
            "name": "Course Name",
            "level": "Level"
        }
        ```
    - **400 Bad Request**: If required fields are missing.
        ```json
        {
            "error": {
                "code": "E001",
                "message": "Name and level are required."
            }
        }
        ```

#### 2. Retrieving Course List
- **Endpoint**: `GET /api/v1/courses`
- **Responses**:
    - **200 OK**: Returns a list of all courses.
        ```json
        [
            {
                "id": 1,
                "name": "Course Name",
                "level": "Level"
            }
        ]
        ```

### Unit Tests for Course API Endpoints
The unit tests for the Course API endpoints ensure that all functionalities work as expected. Below are details of the tests that are created:

- **Test Case 1**: Verify that a new course can be added successfully with both a name and level.
- **Test Case 2**: Confirm that retrieving courses returns the correct data format (JSON) including the name and level fields.
- **Test Case 3**: Test response messages for field validations, ensuring that attempts to create a course without required fields result in proper error messages.

These tests are located in the `tests/test_course.py` file.

## Setup and Usage
1. Install dependencies from `requirements.txt`.
2. Run the application with `uvicorn src.main:app --reload`.
3. Use [Postman](https://www.postman.com/) or [curl](https://curl.se/) to test the API endpoints.

## Running Tests
To run the unit tests, execute:
```bash
pytest tests/test_course.py
```

This will verify that all Course-related functionalities operate correctly.

## Contributing
Please adhere to the established coding standards and make sure to write tests for any new features you add.

## License
This project is licensed under the MIT License - see the LICENSE file for details.