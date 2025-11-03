# README.md

## Getting Started

To run the application and execute tests, follow these steps:

1. **Setup the environment**:
   - Ensure you have Python 3.x installed.
   - Create and activate a virtual environment.
   - Install required dependencies:
     ```bash
     pip install -r requirements.txt
     ```

2. **Database Migration**:
   - Run the migration scripts to set up the database with the required tables:
     ```bash
     flask db upgrade
     ```

3. **Run the application**:
   - Start the application using:
     ```bash
     flask run
     ```

## API Endpoints

### Retrieve Courses Associated with Teachers

- **Endpoint**: `/api/v1/courses/teachers/<teacher_id>`
- **Method**: `GET`
- **Description**: Fetch all courses assigned to a specific teacher.
- **Response Format**:
  - 200 OK
    ```json
    {
      "courses": [
        {
          "id": 1,
          "name": "Mathematics",
          "description": "An introductory course to Mathematics",
          "teacher_id": 1
        },
        {
          "id": 2,
          "name": "Physics",
          "description": "Basics of Physics",
          "teacher_id": 1
        }
      ]
    }
    ```

- **Error Responses**:
  - 404 Not Found
    ```json
    {
      "error": {
        "code": "E404",
        "message": "No courses found for the given teacher."
      }
    }
    ```

### Testing Strategy

We have added unit tests to verify the functionality of course retrieval associated with teachers. Below are details for executing the tests:

1. **Run Tests**:
   - Use pytest to run the tests:
     ```bash
     pytest tests/
     ```

2. **Test Coverage**:
   - Ensure minimum coverage of 70% for business logic, aiming for higher coverage for critical paths.

### Available Tests for Course Retrieval

The following tests have been implemented to ensure that course retrieval functionality is working correctly:

- **Test Retrieval of Courses for a Valid Teacher**: Confirms that when a teacher ID is provided, the courses associated with that teacher are correctly retrieved.
- **Test Retrieval of Courses for a Non-Existent Teacher**: Verifies that an error message is returned when a teacher ID does not exist in the system.

Make sure to run the tests regularly to validate the functionality as new features are developed.