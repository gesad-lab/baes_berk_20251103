Here is the updated content for the `README.md` file, which now includes a section detailing the integration tests for course-teacher relationships:

```
# Project Title

## Introduction
This project is designed to manage courses and teachers in an educational setting. It provides API endpoints to assign teachers to courses and retrieve course details, including associated teacher information.

## Integration Tests

Integration tests are critical for validating the interaction between various components of our application, specifically for the course-teacher relationships. This section describes how integration tests are structured and executed.

### Course-Teacher Relationship Tests

The integration tests cover the following scenarios regarding the `PATCH` and `GET` API endpoints used to manage the relationship between courses and teachers:

1. **Assign a Teacher to a Course**
   - **Endpoint**: `PATCH /courses/{courseId}`
   - **Test**: 
     - Successfully assigns a teacher to a course using a valid `teacher_id`.
     - Returns the updated course object with the correct teacher details.
     - Validates that an appropriate error response is returned if the `teacher_id` does not exist.

2. **Retrieve Course with Teacher Details**
   - **Endpoint**: `GET /courses/{courseId}`
   - **Test**:
     - Successfully retrieves a course with its assigned teacher's details (name and email).
     - Ensures that the teacher details are correctly mapped to the course response.

### Running Tests

To run the integration tests for the course-teacher relationships, execute the following command in the terminal from the project root:

```bash
pytest tests/integration/test_integration.py
```

Ensure that your environment is set up and that the necessary dependencies are installed as outlined in the setup instructions.

### Conclusion

These integration tests are essential for ensuring the reliable functionality of our application’s course-teacher relationships. They help to confirm that changes to the API and database schema do not introduce unintended issues.

```

This addition clearly outlines the integration tests for course-teacher relationships in the `README.md`, matching the requested specifications while maintaining the style of the existing documentation.