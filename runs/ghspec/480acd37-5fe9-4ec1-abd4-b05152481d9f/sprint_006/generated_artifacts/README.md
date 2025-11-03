# README.md

# Course Management Application

## Overview & Purpose
The purpose of this feature is to establish a relationship between the Course entity and the Teacher entity, allowing each course to have an associated teacher. This enhancement serves to improve the functionality of the educational management system by enabling better tracking of course assignments and enhancing the overall organization. The addition of this relationship aligns with our goal of creating a comprehensive platform for managing educational resources, thereby benefiting administration and students alike.

## API Documentation

### API Endpoints

#### 1. Assign a Teacher to a Course

- **Endpoint**: `PATCH /courses/{course_id}/assign-teacher`
- **Description**: This endpoint allows an admin user to assign a teacher to a specific course.
- **Request Body**:
    ```json
    {
        "teacher_id": 1
    }
    ```
- **Response**:
    - **200 OK**: Teacher successfully assigned to the course.
    - **400 Bad Request**: Invalid teacher ID or course configuration.
    - **404 Not Found**: Course or teacher not found.

#### 2. Fetch Course Details with Teacher Information

- **Endpoint**: `GET /courses/{course_id}`
- **Description**: An admin user can request the details of a course, including the assigned teacher's information.
- **Response**: 
    ```json
    {
        "course_id": 1,
        "title": "Introduction to Programming",
        "teacher": {
            "teacher_id": 1,
            "name": "Jane Smith",
            "email": "jane.smith@example.com"
        }
    }
    ```
- **Response Codes**:
    - **200 OK**: Successfully retrieved course details.
    - **404 Not Found**: Course not found.

#### 3. Validate Teacher Assignment to Course

- **Endpoint**: `PATCH /courses/{course_id}/assign-teacher`
- **Description**: An admin user attempts to assign a teacher to a course that exceeds the system's limit (e.g., assigning a teacher already assigned to another course). The system should prevent the assignment and return appropriate error messages.
- **Response**:
    - **400 Bad Request**: Teacher assignment failed due to business rules (e.g., already assigned).
  
## User Scenarios & Testing

1. **Assign a Teacher to a Course**: An admin user can assign a teacher to a specific course. The system should confirm the successful assignment of the teacher to that course.
   - **Test**: Ensure that after assigning a teacher to a course, the course details reflect the assigned teacher correctly.

2. **Fetch Course Details with Teacher Information**: An admin user can request the details of a course, including the assigned teacher's information. The response should include the relevant course and teacher details.
   - **Test**: Ensure that a valid request returns a JSON object containing the course and its associated teacher data.

3. **Validate Teacher Assignment to Course**: An admin user attempts to assign a teacher to a course that exceeds the system's limit (e.g., assigning a teacher already assigned to another course). The system should prevent the assignment and return appropriate error messages, if applicable.
   - **Test**: Confirm that an error is returned if attempting to assign a teacher to an incompatible course configuration.

## Functional Requirements
1. **Database Changes**:
   - Modify the existing Course table to include a new column:
     - `teacher_id`: Foreign key referencing the Teacher entity (integer, nullable), allowing a course to be linked to a teacher.

2. **API Endpoints**:
   - **PATCH /courses/{course_id}/assign-teacher**: This endpoint will allow for the assignment of a teacher to a specific course.
  
## Conclusion
This implementation plan provides a comprehensive approach to add a Teacher relationship to the Course entity, ensuring a more robust and manageable educational environment.