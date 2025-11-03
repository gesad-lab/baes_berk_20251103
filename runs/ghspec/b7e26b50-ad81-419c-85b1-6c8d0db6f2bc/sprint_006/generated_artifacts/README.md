# README.md

# Project Title

## API Documentation

### Assign Teacher to Course Endpoint

- **Endpoint**: `PATCH /courses/{id}`
- **Description**: Associates a teacher with a specific course to ensure every course has a designated educator.

#### Request Body:
```json
{
  "teacher_id": integer  // Required. References the Teacher entity.
}
```

#### Responses:
- **200 OK**
  - Meaning: The teacher has been successfully assigned to the course.
  - Response Body:
  ```json
  {
    "message": "Teacher has been assigned to the course.",
    "teacher_id": integer
  }
  ```

- **404 Not Found**
  - Meaning: The specified `teacher_id` or `course_id` does not exist.
  - Response Body:
  ```json
  {
    "error": {
      "code": "E404",
      "message": "The specified teacher/course does not exist."
    }
  }
  ```

### User Scenarios & Testing

1. **User Scenario: Assign a Teacher to a Course**
   - As an administrator, I want to associate a teacher with a specific course to ensure that every course has a designated educator.
   - **Test**: Verify that a PATCH request to the `/courses/{id}` endpoint with a `teacher_id` correctly updates the course and establishes the relationship.

2. **User Scenario: Course without a Teacher**
   - As a user, I want to view courses that currently do not have any assigned teachers, so I can easily identify which courses need assignments.
   - **Test**: Ensure a GET request to the `/courses` endpoint returns courses without a `teacher_id` as part of the response.

3. **User Scenario: Invalid Teacher Assignment**
   - If I attempt to assign a non-existent teacher to a course, I want to receive an error message indicating that the teacher does not exist.
   - **Test**: Validate that a PATCH request with a non-existing `teacher_id` returns a 404 error with an appropriate message.

### Additional Information
- Database Schema Update: The `Course` table has a new `teacher_id` column, which is an integer foreign key referencing the `Teacher` table.
- Make sure to apply necessary migrations that update the existing `Course` table while preserving existing data. 

--- 

## Installation 
Follow the installation instructions to set up your development environment.

## Usage 
Use the API endpoints as per the documentation above. Ensure you perform tests to validate the functionalities.

## Contribution 
Please read the contributing guidelines for contributing to the project.

## License 
This project is licensed under the MIT License - see the LICENSE file for details.