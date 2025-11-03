# Updated API Documentation

# Project Documentation for Student Management App

## API Endpoints

This section contains the API endpoints for the Student Management application, including operations for managing students, courses, and teachers.

### Student Endpoints

- **GET /students**: Retrieve a list of all students.
- **POST /students**: Create a new student.
- **GET /students/{student_id}**: Retrieve a student by ID.
- **PUT /students/{student_id}**: Update a student's information.
- **DELETE /students/{student_id}**: Delete a student by ID.

### Course Endpoints

- **GET /courses**: Retrieve a list of all courses.
- **POST /courses**: Create a new course.
- **GET /courses/{course_id}**: Retrieve a course by ID.
- **PUT /courses/{course_id}**: Update a course's information.
- **DELETE /courses/{course_id}**: Delete a course by ID.

### Teacher Endpoints

#### Create a Teacher

- **POST /teachers**
  - **Description**: Create a new teacher.
  - **Request Body**:
    ```json
    {
      "name": "Teacher Name",
      "subject": "Subject Name"
    }
    ```
  - **Responses**:
    - **201 Created**: Teacher created successfully.
    - **400 Bad Request**: Validation errors for input fields.

#### Retrieve a Teacher

- **GET /teachers/{teacher_id}**
  - **Description**: Retrieve a teacher by ID.
  - **Responses**:
    - **200 OK**: Returns the teacher's details.
    - **404 Not Found**: Teacher not found.

#### Retrieve All Teachers

- **GET /teachers**
  - **Description**: Retrieve a list of all teachers.
  - **Responses**:
    - **200 OK**: Returns a list of teachers.

### Error Handling

The API will return structured error responses for all endpoints. A typical error response looks like this:

```json
{
  "error": {
    "code": "E001",
    "message": "Invalid input",
    "details": {
      "field": "name",
      "issue": "Name is required"
    }
  }
}
```

### Database Schema Updates

The Teacher model has been added to the application to manage teacher-related data. Ensure that you run the necessary migrations using Alembic after updating the schema in `models.py`.

### Testing

Automated tests for the Teacher API endpoints are located in the `tests/test_teacher.py` file. Ensure that these tests cover both successful operations and validation checks for input data.

---

Feel free to reach out if you have further questions or require additional information about the API!