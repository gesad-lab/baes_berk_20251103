# README.md

# Student Course Enrollment API

## Introduction
This API allows users to manage student enrollments in various courses, enabling enrollment, unenrollment, and retrieval of enrollment details.

## User Scenarios & Testing

1. **Enroll a Student in a Course**: 
   A user can enroll a student in one or more courses. The system should confirm the enrollment and link the student to the specified course(s).
   - **Test**: Ensure that after enrolling a student in a course, the course is reflected in the student's profile.

2. **List Courses for a Student**: 
   A user can request to view all courses that a particular student is enrolled in. The response should list all related courses with their details.
   - **Test**: Ensure that a valid request returns a JSON array of courses corresponding to the student.

3. **Unenroll a Student from a Course**: 
   A user can remove a student's enrollment from a specified course. The system should update the relationship and confirm the unenrollment.
   - **Test**: Ensure that after unenrolling a student from a course, the course no longer appears in the student's course list.

4. **Fetch Student Details with Courses**: 
   A user can request full details about a student, including their enrolled courses. The response should reflect the student and their current course enrollments.
   - **Test**: Ensure that a request for student details includes the relevant course information in the response.

## API Endpoints

### Enroll a Student in Courses

- **POST /students/{id}/courses**
  - **Description**: Enrolls a student in one or more courses.
  - **Request Body**:
    ```json
    {
      "course_ids": [integer]
    }
    ```
  - **Response**:
    - **200 OK**: Confirmation message indicating successful enrollments.
    - **Example**:
      ```json
      {
        "message": "Student enrolled in courses successfully."
      }
      ```

### Unenroll a Student from a Course

- **DELETE /students/{id}/courses/{course_id}**
  - **Description**: Removes a student's enrollment from a specified course.
  - **Response**:
    - **200 OK**: Confirmation message indicating successful unenrollment.
    - **Example**:
      ```json
      {
        "message": "Student unenrolled from the course successfully."
      }
      ```

### List Courses for a Student

- **GET /students/{id}/courses**
  - **Description**: Fetches all courses that a particular student is enrolled in.
  - **Response**:
    - **200 OK**: JSON array of courses.
    - **Example**:
      ```json
      [
        {
          "id": 1,
          "name": "Mathematics",
          "level": "100"
        },
        {
          "id": 2,
          "name": "Science",
          "level": "200"
        }
      ]
      ```

### Fetch Student Details with Courses

- **GET /students/{id}**
  - **Description**: Fetches full details about a student, including their enrolled courses.
  - **Response**:
    - **200 OK**: Student details including course enrollments.
    - **Example**:
      ```json
      {
        "id": 1,
        "name": "John Doe",
        "enrolled_courses": [
          {
            "id": 1,
            "name": "Mathematics",
            "level": "100"
          }
        ]
      }
      ```

## Functional Requirements
1. **Database Changes**:
   - Create a new junction table to represent the many-to-many relationship between Students and Courses. This table should contain:
     - `id`: Unique identifier for the relationship (integer, auto-increment).
     - `student_id`: Foreign key referencing the Student entity (integer, required).
     - `course_id`: Foreign key referencing the Course entity (integer, required).

## Testing and Coverage
- Aim for at least 70% coverage on business logic with critical paths (enrollment and unenrollment) exceeding 90%. 

## Setup
Follow installation instructions provided in previous sections to get the application running locally. Make sure to review environment variables and configuration files.

---