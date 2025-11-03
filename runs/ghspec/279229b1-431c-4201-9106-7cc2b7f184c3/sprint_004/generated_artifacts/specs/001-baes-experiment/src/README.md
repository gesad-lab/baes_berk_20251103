# README.md

# Project Title

This is a brief description of the project.

## Setup Instructions

To set up the project, follow these steps:

1. Clone the repository.
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Configure your environment variables as needed. Use `.env.example` as a reference.

4. Run the database migrations to set up the schema:
   ```bash
   flask db upgrade
   ```

5. Start the application:
   ```bash
   flask run
   ```

## API Endpoints

### Associate Student with Courses

- **Endpoint**: `POST /students/{student_id}/courses`
- **Description**: This endpoint allows you to associate multiple courses with a specific student.
- **Request**:
  - **Path Parameter**: 
    - `student_id`: The ID of the student to associate with courses.
  - **Body**:
    ```json
    {
      "course_ids": [1, 2, 3]
    }
    ```
- **Response**: On success, returns a JSON object with a confirmation message.
  ```json
  {
    "message": "Student has been successfully associated with the courses."
  }
  ```

### Retrieve Courses for Student

- **Endpoint**: `GET /students/{student_id}/courses`
- **Description**: This endpoint retrieves all courses associated with a specific student.
- **Request**:
  - **Path Parameter**:
    - `student_id`: The ID of the student whose courses you want to retrieve.
- **Response**: Returns a JSON array of course objects associated with the student.
  ```json
  [
    {
      "id": 1,
      "name": "Course Name",
      "description": "Course Description"
    },
    {
      "id": 2,
      "name": "Another Course",
      "description": "Another Description"
    }
  ]
  ```

## Database Schema Changes

A junction table has been added to link students and courses. This change will ensure that multiple courses can be associated with a single student while preserving existing data. The relationship table includes:
- `student_id` (Integer, Foreign Key referencing Student)
- `course_id` (Integer, Foreign Key referencing Course)

Migrations have been implemented to facilitate this update without data loss.

## Testing Strategies

To test the API endpoints, you can use the provided test files. Ensure that you follow the directory structure laid out in the tests folder. Use pytest to run the tests:

```bash
pytest tests/
```

Make sure to add new tests corresponding to the implemented features for `POST /students/{student_id}/courses` and `GET /students/{student_id}/courses` to ensure coverage.

## Available Endpoints

Refer to the sections above for a detailed description of each API endpoint available in this project. 

--- 

Note: Ensure that you follow the instructions relevant to your development environment and have the necessary permissions and configurations set up for successful operation.