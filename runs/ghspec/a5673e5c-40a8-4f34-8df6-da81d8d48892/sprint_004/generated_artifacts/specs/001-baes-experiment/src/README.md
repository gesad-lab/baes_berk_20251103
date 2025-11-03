# README.md

## Course Association Validation

### New API Endpoints

The following new endpoints have been added to manage the association between students and courses. These endpoints ensure that enrollments and unenrollments are only processed for valid students and courses.

### 1. Enroll a Student in a Course

**Endpoint**: `POST /api/enroll`

**Request Body**:
```json
{
  "student_id": "string",
  "course_id": "string"
}
```

- `student_id`: The unique identifier of the student to be enrolled.
- `course_id`: The unique identifier of the course in which the student is to be enrolled.

**Responses**:

- **201 Created**: Successfully enrolled the student in the course.
  ```json
  {
    "message": "Student successfully enrolled in the course."
  }
  ```

- **400 Bad Request**: If the provided `student_id` or `course_id` does not correspond to an existing student or course.
  ```json
  {
    "error": {
      "code": "E001",
      "message": "Invalid course identifier."
    }
  }
  ```

### 2. Unenroll a Student from a Course

**Endpoint**: `DELETE /api/unenroll`

**Request Body**:
```json
{
  "student_id": "string",
  "course_id": "string"
}
```

- `student_id`: The unique identifier of the student to be unenrolled.
- `course_id`: The unique identifier of the course from which the student is to be unenrolled.

**Responses**:

- **200 OK**: Successfully unenrolled the student from the course.
  ```json
  {
    "message": "Student successfully unenrolled from the course."
  }
  ```

- **400 Bad Request**: If the provided `student_id` or `course_id` does not correspond to an existing student or course.
  ```json
  {
    "error": {
      "code": "E002",
      "message": "Invalid student identifier."
    }
  }
  ```

### Database Migration

When setting up your database, make sure to run migrations to update the schema for the `Student` and `Course` tables. This ensures the integrity of existing data is preserved while the new relationship is established.

### Validation Logic

The application validates the existence of both student and course identifiers before processing enroll and unenroll requests. If an invalid identifier is detected, an appropriate error message will be returned.

### Setup Instructions

1. Ensure you have Python 3.11+ and Poetry installed as per the project requirements.
2. Run the database migrations to update the schema.
3. Start the FastAPI application.
4. Use the provided endpoints to manage student-course associations.

For further details on testing and examples of the endpoints, please refer to the tests located in the `tests` directory.