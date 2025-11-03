# Updated content for README.md

Welcome to the API Documentation for Course and Teacher Management!

## API Endpoints

### Courses

#### GET /courses/{id}

Retrieves details of a specific course identified by its ID, along with associated teacher information.

**Response**

- **200 OK**: Returns course details including teacher's name and email.
- **404 Not Found**: The specified course ID does not exist.

**Example Request:**
```
GET /courses/1
```

**Example Response (Success):**
```json
{
    "id": 1,
    "title": "Introduction to Programming",
    "teacher": {
        "name": "Jane Doe",
        "email": "jane@example.com"
    }
}
```

**Example Response (Not Found):**
```json
{
    "error": {
        "code": "E404",
        "message": "Course not found."
    }
}
```

### Testing

#### Tests Overview

To ensure the API behaves as expected, we have implemented a suite of tests, specifically focusing on various scenarios for managing courses and teachers.

#### Tests for `GET /courses/{id}`

1. **Retrieve Course with Teacher Details**
   - Validates that a request for a valid course ID returns the correct course details along with the teacher information.

2. **Error Handling for Non-Existent Course**
   - Ensures that a request for a non-existent course ID returns a 404 error with an appropriate message.

### Running Tests

To run the tests specified in this documentation, utilize the following command:

```bash
pytest tests/
```

Make sure your test setup is correct according to the guidelines specified in the testing section of this documentation.

---

## Additional Information

For further details on the teacher assignment functionality and additional endpoints, please refer to the respective endpoints listed above.

To start the application, ensure all dependencies are installed and run the application using your preferred environment setup (e.g., `uvicorn`, `gunicorn`).

Thank you for using our API!