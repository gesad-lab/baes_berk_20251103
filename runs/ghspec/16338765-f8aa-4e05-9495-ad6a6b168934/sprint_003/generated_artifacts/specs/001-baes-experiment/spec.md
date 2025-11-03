# Feature: Create Course Entity

## Overview & Purpose
The purpose of this feature is to introduce a new "Course" entity into the existing system. This addition aims to enhance the application's capability by allowing the management of course information, including course names and levels. By providing this functionality, we will facilitate better organization of educational content, which could improve the user experience for both students and educators.

## User Scenarios & Testing

### User Scenarios
1. **Create a Course**:
   - As an admin, I want to create a new course by specifying its name and level to expand the curriculum offerings.
   
2. **Retrieve Course Information**:
   - As a user, I want to access details of a specific course by its ID so that I can view the course name and level.

3. **Update Course Information**:
   - As an admin, I want to update the existing details of a course, including its name and level, so that course information remains current.

### Testing Scenarios
1. Test that a course can be successfully created with valid name and level.
2. Test that the application returns an error when creating a course without either a name or level.
3. Test that retrieving a course by ID returns the correct data, including the name and level.
4. Test that a course's name and level can be updated successfully.

## Functional Requirements
1. Create a new Course entity with the following fields:
   - **Field**: `name` (string, required)
   - **Field**: `level` (string, required)

2. Update the database schema to reflect the addition of the new Course table:
   - **Table Name**: `Course`
   - **Columns**:
     - `id`: Integer (Primary Key, auto-increment)
     - `name`: String (Required)
     - `level`: String (Required)

3. The application must provide an endpoint to create a course:
   - **Endpoint**: `/courses` (POST)
   - **Input**: JSON payload containing a `name` (string, required) and `level` (string, required).
   - **Output**: JSON response with the created course's ID, name, and level.

4. The application must provide an endpoint to retrieve a single course by its ID:
   - **Endpoint**: `/courses/{id}` (GET)
   - **Output**: JSON response with the course's ID, name, and level.

5. The application must provide an endpoint to update a course's name and/or level:
   - **Endpoint**: `/courses/{id}` (PUT)
   - **Input**: JSON payload containing `name` (string, optional) and/or `level` (string, optional).
   - **Output**: JSON response with the updated course's details.

6. The database migration for the new Course table must ensure that it will not disrupt existing Student data.

## Success Criteria
1. User is able to successfully create a course with valid name and level, receiving the course ID, name, and level in the response.
2. User is able to fetch a course by ID, receiving the correct details, including its name and level.
3. User is able to update existing course details successfully, and the changes are reflected when the course is retrieved thereafter.
4. The database schema update runs successfully and does not impact existing Student data.

## Key Entities
- **Course Table**:
  - **Columns**:
    - `id`: Integer (Primary Key, auto-increment)
    - `name`: String (Required)
    - `level`: String (Required)

## Assumptions
- Users have the necessary permissions to create and manage course records.
- The same tech stack (Python 3.11+ and FastAPI with SQLite) is used as in the previous sprint.
- There are appropriate links or relationships with existing entities to relate courses with students if necessary.

## Out of Scope
- Implementing features for course enrollment or attendance tracking.
- Adding validation rules for course names and levels.
- Building user interface components for course management beyond the specified endpoints.