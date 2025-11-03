# README.md

# Project Name

## Overview & Purpose

The purpose of this project is to create a robust application for managing educational courses. As part of our ongoing development efforts, we've introduced a new Course entity that enables institutions to effectively manage course offerings. This entity will store essential attributes such as the course name and level, thus enhancing the platform's overall functionality and allowing for future growth.

## New Features

### Course Management

With this update, we now support the management of courses in the system, including:

1. **Creating New Courses**: Admin users can create a new course by providing essential details such as the course name and level. 
   - **API Endpoint**: `POST /api/v1/courses`
   - **Request Example**:
     ```json
     {
       "name": "Introduction to Programming",
       "level": "Beginner"
     }
     ```

2. **Retrieving Courses**: Users can access a list of all available courses, including information on their names and levels.
   - **API Endpoint**: `GET /api/v1/courses`
   - **Response Example**:
     ```json
     [
       {
         "name": "Introduction to Programming",
         "level": "Beginner"
       },
       {
         "name": "Advanced Programming Concepts",
         "level": "Advanced"
       }
     ]
     ```

3. **Validation Logic**: The system ensures that necessary fields are provided when creating a course.
   - If the name or level is missing, the API will return appropriate error messages, such as:
     - `"error": {"code": "E001", "message": "Course name is required."}`
     - `"error": {"code": "E002", "message": "Course level is required."}`

## User Scenarios & Testing

1. **Create New Course**: As an admin user, I want to create a new course by providing a name and level so that the course can be added to the system for future usage.
   - **Test**: Verify that entering a valid name and level successfully creates a new course entry in the database.

2. **Retrieve Course Details**: As a user, I want to access and view the list of all available courses, including their names and levels, so that I can know what courses are offered.
   - **Test**: Verify that the API returns a list of courses with names and levels in JSON format.

3. **Course Creation Validation**: As an admin user, I want to receive clear error messages when I attempt to create a course without a name or level provided to ensure proper course registration.
   - **Test**: Validate that appropriate error messages are returned when either the name or level is missing.

## Development Steps

1. **Database Migration**: A migration script will be created to add the `courses` table to the existing database schema.
2. **Update the Course Model**: A new ORM model for `Course` will be added for interaction with the database.
3. **Enhance API Endpoints**: New API routes for course creation and retrieval will be added to the existing Flask application.
4. **Implement Validation Logic**: Ensure that both name and level are validated properly before creating a course.
5. **Testing**: Unit and integration tests will be created to validate course creation and retrieval scenarios.
6. **Documentation**: Update this README.md to reflect the addition of course-related functionality.

## Additional Notes
- Out of scope for this feature are advanced course functionalities, user interface updates, and modifications to authorization processes concerning course management.
- This implementation is designed to integrate seamlessly into the existing system with minimal disruption to current functionalities, preparing the way for future enhancements.

By implementing this feature, we aim to better supplement the needs of educational institutions and facilitate further growth for the platform.