# README.md

# Project Overview

This application manages student enrollments in various courses. It leverages a many-to-many relationship between `Student` and `Course` entities, allowing multiple students to enroll in multiple courses seamlessly. 

## Functional Requirements

1. The application must establish a many-to-many relationship between `Student` and `Course` entities, enabling multiple students to enroll in multiple courses.

2. The application must automatically update the existing database schema to include a join table (e.g., `student_courses`) that maintains this relationship during startup without any manual intervention.

3. The API must support the following new endpoints:
   - `POST /students/{studentId}/courses`: To enroll a student in a course. The request body must include the `courseId`.
   - `GET /students/{studentId}/courses`: To retrieve a list of all courses a specific student is enrolled in.

4. Responses from the API should be in JSON format:
   - On successful enrollment, return:
     ```json
     {
       "message": "Student enrolled successfully",
       "studentId": "<studentId>",
       "courseId": "<courseId>"
     }
     ```
   - On retrieval, return:
     ```json
     {
       "courses": [
         {
           "name": "<course_name>",
           "level": "<course_level>"
         },
         ...
       ]
     }
     ```
   - For errors (including invalid or missing IDs), return:
     ```json
     {
       "error": {
         "code": "<error_code>",
         "message": "<error_message>"
       }
     }
     ```

## User Scenarios & Testing

1. **Enroll a Student in a Course**: An administrator enrolls a student in a course. The system should confirm the successful enrollment of the student in the specified course.
   - **Test**: Submit a request to enroll a student using a valid student ID and course ID, ensuring the response indicates successful enrollment.

2. **Retrieve Student Course Enrollment**: An administrator requests to view all courses a student is enrolled in. The system should provide a list of courses associated with the student.
   - **Test**: Send a request with a valid student ID and verify the JSON response includes all courses that the student is enrolled in.

3. **Error Handling on Invalid Enrollment**: An administrator attempts to enroll a student in a course using an invalid student ID or course ID. The system should handle this gracefully and return an appropriate error message:
   - **Test**: Send a request with an invalid student ID or course ID to ensure an error response with the correct error code and message is returned. 

## Health Checks

- Ensure responses from the API endpoints align with the JSON format specified above for both success and error scenarios.

## Contribution

To contribute to this project or report issues, please submit a pull request or open an issue in the project's repository.