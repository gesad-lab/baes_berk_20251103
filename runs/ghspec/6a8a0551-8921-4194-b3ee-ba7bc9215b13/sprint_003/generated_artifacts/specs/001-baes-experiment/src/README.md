```markdown
# README.md

# Course Management API

## Overview

This API allows users to manage courses, including creating and fetching course data. It provides error handling for scenarios where course creation is attempted with missing fields or invalid data formats.

## Endpoints

### 1. Create a Course

- **URL**: `/courses/`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
    "name": "Course Name",
    "level": "Course Level"
  }
  ```
- **Responses**:
  - **201 Created**: Returns the created course object.
  - **400 Bad Request**: Returns validation error messages if required fields are missing or have invalid formats.

### 2. Fetch All Courses

- **URL**: `/courses/`
- **Method**: `GET`
- **Responses**:
  - **200 OK**: Returns a list of all courses with their names and levels.

### 3. Fetch a Specific Course

- **URL**: `/courses/{id}`
- **Method**: `GET`
- **Responses**:
  - **200 OK**: Returns the requested course object.
  - **404 Not Found**: If the course ID does not exist.

## Error Handling in Course Creation

The API handles the following validation scenarios:

1. **Missing Fields**:
   - If the request does not contain the required fields `name` or `level`, it responds with a `400 Bad Request` status and a message indicating the missing field.
   ```json
   {
     "error": {
       "code": "E001",
       "message": "Missing name field."
     }
   }
   ```

2. **Invalid Level Format**:
   - If the `level` is not in the expected format (for instance, a number or an unsupported string), the API responds with a `400 Bad Request` status and a message regarding the validation issue.
   ```json
   {
     "error": {
       "code": "E002",
       "message": "Invalid level format."
     }
   }
   ```
  
## Testing

To ensure that the API is functioning as expected, tests should be written to cover error handling for scenarios where course creation is attempted with missing fields or invalid data formats. The tests will verify that appropriate error messages are returned in each case.

### Error Handling Test Cases

1. **Test for Missing Name Field**: 
   - Attempt to create a course without the `name` field.
   - Expect a `400 Bad Request` response with the appropriate error message.

2. **Test for Missing Level Field**: 
   - Attempt to create a course without the `level` field.
   - Expect a `400 Bad Request` response with the appropriate error message.

3. **Test for Invalid Level Format**: 
   - Attempt to create a course with an invalid `level` format.
   - Expect a `400 Bad Request` response indicating the validation issue.

## Running Tests

Use the following command to run the tests:
```bash
pytest tests/test_api/
```

Make sure to install all dependencies from the `requirements.txt` before running the tests.
```