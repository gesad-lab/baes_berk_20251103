# README.md

# Project Title

## Introduction

This project is designed to manage students and courses using a RESTful API. In this update, we have introduced functionality to enroll students in courses and retrieve the list of courses a student is currently enrolled in.

## API Endpoints

### Enroll Student in Courses

- **Endpoint**: `/api/v1/enroll`
- **Method**: `POST`
- **Description**: Allows a user to enroll a student in one or more courses by providing an array of course IDs.
  
- **Request Body**:
  ```json
  {
      "student_id": <integer>, // Required: The ID of the student to enroll
      "course_ids": [<integer>, ...] // Required: An array of course IDs to enroll the student in
  }
  ```

- **Successful Response**:
  - **Status Code**: `200 OK`
  - **Response Body**:
  ```json
  {
      "message": "Student enrolled successfully.",
      "student": {
          "id": <integer>,
          "course_ids": [<integer>, ...] // Updated list of course IDs the student is enrolled in
      }
  }
  ```

- **Error Response**:
  - **Status Code**: `400 Bad Request`
  - **Response Body**:
  ```json
  {
      "error": {
          "code": "E001",
          "message": "Invalid course IDs provided."
      }
  }
  ```

### Retrieve Student Courses

- **Endpoint**: `/api/v1/students/<student_id>/courses`
- **Method**: `GET`
- **Description**: Allows a user to retrieve all courses that a student is enrolled in.
  
- **Successful Response**:
  - **Status Code**: `200 OK`
  - **Response Body**:
  ```json
  {
      "student_id": <integer>,
      "courses": [
          {
              "id": <integer>,
              "name": "Course Name",
              "level": "Course Level"
          },
          ...
      ]
  }
  ```

## Database Migration

To set up the necessary database structures for the new functionality, you need to run the migrations. The following migration will create an `enrollments` table, facilitating the relationship between students and courses:

```python
def upgrade():
    op.create_table(
        'enrollments',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('student_id', sa.Integer(), sa.ForeignKey('students.id'), nullable=False),
        sa.Column('course_id', sa.Integer(), sa.ForeignKey('courses.id'), nullable=False)
    )

def downgrade():
    op.drop_table('enrollments')
```

## Testing

To ensure the new features function correctly, we have incorporated the following tests:

1. **Unit Tests**: Validate the student enrollment and course retrieval functionalities.
2. **Integration Tests**: Check API request/response cycles for enrolling students and retrieving their courses.
3. **Contract Tests**: Ensure new API endpoints conform to specifications.

Run the tests using `pytest` to verify that everything is working as expected.

## Conclusion

This update enhances the student management capabilities of the application, allowing for easier enrollment and course retrieval. Be sure to run the database migrations and tests to fully integrate these new features.