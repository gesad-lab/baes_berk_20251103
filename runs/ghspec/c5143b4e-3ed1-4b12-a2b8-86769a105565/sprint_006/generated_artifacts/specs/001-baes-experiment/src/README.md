# README.md

# Course Management API

This API allows management of courses and their associated instructors. It implements functionalities to assign and remove teachers from courses.

## Features

### Assign Teacher to Course
- **Endpoint**: `PUT /courses/{courseId}/assignTeacher`
- **Description**: Assign a teacher to an existing course.
- **Request Body**:
  ```json
  {
    "teacherId": "string" // Required
  }
  ```
- **Responses**:
  - **200 OK**: The request was successful, and the updated Course object is returned.
  - **400 Bad Request**: Invalid Course ID or Teacher ID. Includes an error message:
    ```json
    {
      "error": {
        "code": "E001",
        "message": "Course not found."
      }
    }
    ```

### Remove Teacher from Course
- **Endpoint**: `DELETE /courses/{courseId}/removeTeacher`
- **Description**: Remove a teacher from a specified course.
- **Responses**:
  - **200 OK**: The request was successful, and the updated Course object is returned.
  - **400 Bad Request**: Invalid Course ID. Includes an error message:
    ```json
    {
      "error": {
        "code": "E001",
        "message": "Course not found."
      }
    }
    ```

## User Scenarios & Testing

1. **Assign Teacher to Course**:
   - As an admin user, I want to assign a Teacher to an existing Course by specifying the Course ID and Teacher ID, ensuring that each course has a designated educator.
   - **Test**: Ensure that a PUT request to the `/courses/{courseId}/assignTeacher` endpoint updates the specified course with the provided teacher ID and returns the updated Course object in JSON format.

2. **Error on Invalid Course ID**:
   - As an admin user, I want to receive an error message if I attempt to assign a Teacher to a non-existent Course ID.
   - **Test**: Ensure that a PUT request with an invalid Course ID results in a JSON error response indicating that the course was not found.

3. **Error on Invalid Teacher ID**:
   - As an admin user, I want to receive an error message when I provide an invalid Teacher ID while assigning them to a Course.
   - **Test**: Ensure that a PUT request with an invalid Teacher ID returns a JSON error response indicating that the teacher was not found.

4. **Removing Teacher from a Course**:
   - As an admin user, I want to remove a Teacher from a Course by specifying the Course ID, ensuring the course can exist without an instructor assigned.
   - **Test**: Ensure that a DELETE request to the `/courses/{courseId}/removeTeacher` endpoint successfully removes the teacher assignment and returns the updated Course object.

## Setup Instructions

1. Ensure that you have Python and the required packages installed (`FastAPI`, `SQLAlchemy`, `Alembic`).
2. Clone the repository to your local machine.
3. Update your `.env` file as needed.
4. Run the API using your preferred method (e.g., `uvicorn src.main:app --reload`).

## Testing

Run the tests using `pytest` to ensure all functionalities, including assigning and removing teachers, work as intended.

--- 

Make sure to keep the README updated as new features are added or existing features are modified in the API.