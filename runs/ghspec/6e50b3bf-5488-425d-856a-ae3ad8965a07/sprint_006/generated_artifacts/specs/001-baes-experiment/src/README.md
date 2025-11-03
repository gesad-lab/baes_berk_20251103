# README.md

# Student Management API

This project provides a set of APIs for managing courses and teachers in a student management system.

## API Documentation

### 1. Assign Teacher to Course

Assign a teacher to a specific course.

- **Endpoint**: `POST /courses/{course_id}/assign_teacher`
- **Request Body**:
    ```json
    {
        "teacher_id": <int>
    }
    ```
- **Responses**:
    - **Success**: `200 OK`
        ```json
        {
            "course_id": <int>,
            "assigned_teacher_id": <int>
        }
        ```
    - **Error**: `404 Not Found` if the specified course or teacher does not exist.

### 2. Retrieve Course Details with Teacher Info

Retrieve detailed information about a specific course along with its assigned teacher.

- **Endpoint**: `GET /courses/{course_id}`
- **Responses**:
    - **Success**: `200 OK`
        ```json
        {
            "course_id": <int>,
            "course_name": "<string>",
            "assigned_teacher": {
                "teacher_id": <int>,
                "name": "<string>",
                "email": "<string>"
            }
        }
        ```
    - **Error**: `404 Not Found` if the specified course does not exist.

### 3. Handle Invalid Teacher Assignment

When attempting to assign a teacher to a course where the teacher does not exist, the application responds appropriately.

## User Scenarios & Testing

1. **Assign Teacher to Course**:
   - A user submits a request to assign a teacher to a specific course.
   - The application responds confirming the assignment and provides the updated course details.

2. **Retrieve Course Details with Teacher Info**:
   - A user submits a request to retrieve information about a specific course along with its associated teacher.
   - The application responds with the course information, including the teacher's name and email.

3. **Handle Invalid Teacher Assignment**:
   - A user attempts to assign a teacher to a course where the teacher does not exist.
   - The application responds with an appropriate error message indicating the teacher must be valid.

## Testing

- Verify that assigning a teacher to a course with valid IDs results in a successful response, providing the updated course information.
- Verify that requesting the details of a course returns expected information, including the assigned teacher.
- Verify that attempting to assign a non-existent teacher returns a clear error message indicating the issue.

## Database Schema Changes

- The `Course` table is updated to include a foreign key relationship to the `Teacher` entity:
  - Add `teacher_id` (integer, optional) to the `Course` table, referencing the `teacher_id` in the `Teacher` table.

## Setup Instructions

1. Clone the repository.
2. Install the required packages using pip:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up your database by running the necessary migrations.
4. Start the application and access the API at `http://localhost:5000`.

## License

This project is open source and available under the MIT License.