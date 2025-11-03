# Updated README.md

# GHSpec-Kit Project

## Overview
This README provides an overview of the project, the Course entity's specifications, and usage instructions for the API endpoints related to course creation and retrieval.

## Course API Entity Specifications

### Course Model
The Course entity has the following attributes:
- **name**: The name of the course (string, required).
- **level**: The level of the course (string, required).

### Database Schema
The courses table is defined as follows:

```sql
CREATE TABLE courses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    level TEXT NOT NULL
);
```

### API Endpoints

#### Create a Course
- **Endpoint**: `POST /courses`
- **Request Body**:
    ```json
    {
        "name": "Introduction to Programming",
        "level": "Beginner"
    }
    ```
- **Responses**:
    - `201 Created`: Returns the created course object.
    - `400 Bad Request`: Returns validation errors.

#### Retrieve a Course
- **Endpoint**: `GET /courses/{course_id}`
- **Responses**:
    - `200 OK`: Returns the course object.
    - `404 Not Found`: Course not found.

## Testing

### Unit Tests for Course Logic
Unit tests are included to verify the correctness and efficiency of the course creation and retrieval logic. The tests focus on ensuring that the required fields are validated correctly and that the retrieval logic behaves as expected.

### Test Coverage
Tests for the courses service and API endpoints achieve a minimum of 70% coverage on the new business logic related to course creation and retrieval. There are special tests for different error conditions, ensuring robust validation.

### How to Run Tests
```
pytest tests/test_api/test_course_api.py
pytest tests/test_services/test_course_service.py
```

## Contributing
Feel free to create pull requests for enhancements or bug fixes. Be sure to add tests for new features and follow the coding standards set in this document.

## License
This project is licensed under the MIT License.

--- 

### Note:
The contents of this README have been updated to include Course entity specifications, API usage instructions, and guidance on running tests.