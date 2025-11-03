# README.md

# Project Title

## Overview

This project aims to manage educational records, providing functionality to handle students, courses, and now teachers. 

## Teacher Entity Information

The Teacher entity has been integrated into the application to facilitate the management of teacher information. The following API endpoints are available for interacting with teacher records:

### 1. Create Teacher
- **API Endpoint**: POST `/teachers`
- **Request Body**: 
    ```json
    {
        "name": "Teacher Name",
        "email": "teacher@example.com"
    }
    ```
- **Success Response**: 
  - **Status**: 201 Created
  - **Response Body**:
    ```json
    {
        "id": 1,
        "name": "Teacher Name",
        "email": "teacher@example.com"
    }
    ```

### 2. Retrieve All Teachers
- **API Endpoint**: GET `/teachers`
- **Success Response**: 
  - **Status**: 200 OK
  - **Response Body**:
    ```json
    [
        {
            "id": 1,
            "name": "Teacher Name",
            "email": "teacher@example.com"
        },
        // ... other teachers
    ]
    ```

### 3. Update Teacher Information
- **API Endpoint**: PUT `/teachers/{teacher_id}`
- **Request Body**:
    ```json
    {
        "name": "Updated Name",
        "email": "updated@example.com"
    }
    ```
- **Success Response**:
  - **Status**: 200 OK
  - **Response Body**: Indicates that the update was successful.

## User Scenarios & Testing
1. **Creating a Teacher**: Users can create a new teacher record by sending a POST request to the `/teachers` endpoint to manage teacher information.

2. **Retrieving Teachers**: Users can retrieve a list of all teachers by sending a GET request to the `/teachers` endpoint, confirming that the response includes a list of all registered teachers.

3. **Updating Teacher**: Users can update a teacher's information using the PUT request to update a teacher's details.

4. **Data Integrity Post-Migration**: Users can ensure that existing student and course data remain unaffected during the database schema migration that adds the Teacher entity by retrieving existing records post-migration.

5. **Unique Email Addresses**: The system ensures that each teacher has a unique email address, as users will receive an error if they attempt to create multiple teachers with the same email.

## Functional Requirements

These requirements describe the expected behavior of the teacher entity within the application.

---

## X. Roadmap

1. **Development**: Implementation of the Teacher entity and its related business logic.
2. **Testing**: Thorough testing including unit and integration tests to validate the Teacher functionality.
3. **Database Migration**: Develop a migration script to add the new `teachers` table while preserving existing data.
4. **Deployment**: Complete pre-deployment testing and deploy the new functionality.

## XI. Conclusion

This integration enhances the application by allowing the management of teacher data, ensuring both functionality and data integrity across the system.