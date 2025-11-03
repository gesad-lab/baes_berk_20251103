# README.md

# Project Title

## API Documentation

### Course Assignments to Students

#### Overview

This section documents the API endpoints related to assigning Courses to Students within the application. It outlines the relationships, behaviors, and expected JSON responses.

#### Functional Requirements

1. **Define Relationship**:
   - A many-to-many relationship is established between the Student and Course entities, allowing each Student to enroll in multiple Courses, and each Course to include multiple Students.

2. **Database Migration**:
   - A junction table named `student_courses` is created to manage the many-to-many relationship. This table includes foreign keys that reference the `Student` and `Course` entities, ensuring that existing Student and Course data is preserved during schema updates.

3. **Validation of Course Assignment**:
   - When associating a Course with a Student, the API validates that the specified Course exists and that the Student is valid. Invalid assignments will trigger appropriate error responses.

4. **JSON Responses**:
   - All API responses related to Course assignments will return results in JSON format, including the Student ID, Course IDs, and their respective names when applicable.

#### User Scenarios

1. **Assigning Courses to a Student**:
   - Endpoint: `POST /api/v1/students/{student_id}/courses`
   - Description: Associates one or more Courses with a Student.
   - Success Response:
     - Code: 200
     - Content: 
       ```json
       {
           "student_id": 1,
           "courses": [
               {"course_id": 101, "course_name": "Math 101"},
               {"course_id": 102, "course_name": "Science 101"}
           ]
       }
       ```

2. **Retrieving Student Courses**:
   - Endpoint: `GET /api/v1/students/{student_id}/courses`
   - Description: Retrieves all Courses associated with a specific Student.
   - Success Response:
     - Code: 200
     - Content: 
       ```json
       {
           "student_id": 1,
           "courses": [
               {"course_id": 101, "course_name": "Math 101"},
               {"course_id": 102, "course_name": "Science 101"}
           ]
       }
       ```

3. **Removing a Course from a Student**:
   - Endpoint: `DELETE /api/v1/students/{student_id}/courses/{course_id}`
   - Description: Disassociates a specific Course from a Student.
   - Success Response:
     - Code: 200
     - Content:
       ```json
       {
           "message": "Course removed successfully from the student."
       }
       ```

#### Database Migrations

To set up the new junction table for Course assignments, run the following migration command using Alembic:

```bash
alembic upgrade head
```

This command will create the `student_courses` table and ensure that all existing data is preserved.

### Additional Information

This documentation will be updated as more functionality is developed related to Course assignments. Please refer to the API responses and ensure compliance with the documented structures while integrating new features.