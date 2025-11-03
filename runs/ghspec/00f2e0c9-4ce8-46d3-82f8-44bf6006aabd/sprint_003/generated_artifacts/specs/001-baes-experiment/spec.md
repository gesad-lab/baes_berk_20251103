# Feature: Create Course Entity

## Overview & Purpose
The purpose of this feature is to create a new Course entity within the existing system, enhancing the ability to manage and categorize courses associated with students. This facilitates better organization of educational content and improves the capability to assign courses to students, fostering a more structured academic experience.

## User Scenarios & Testing
1. **Creating a Course**:
   - User sends a POST request with a JSON body that includes the course name and level.
   - The application responds with a success message and the created course's data.

2. **Fetching a Course's Information**:
   - User sends a GET request to retrieve details of a specific course by ID.
   - The application responds with the course's name and level in a JSON format.

3. **Updating a Course**:
   - User sends a PUT request with a JSON body to update the course's name and/or level.
   - The application responds with a success message and the updated course data.

4. **Error Handling for Course Creation**:
   - User receives appropriate error messages for missing or invalid name and level fields when creating or updating a course.

## Functional Requirements
1. **API Endpoints**:
   - **POST `/courses`**: Create a new course (requires name and level).
   - **GET `/courses/{id}`**: Retrieve a course by ID; responds with name and level.
   - **PUT `/courses/{id}`**: Update a course's name and/or level by ID (requires either field).

2. **Database Interaction**:
   - A new database schema should be created to include a Course table with two required fields: `name` (string) and `level` (string).
   - Ensure that the database migration preserves existing Student data without loss, allowing seamless integration of courses with student records later on.

3. **Response Format**:
   - All API responses related to courses must adhere to the existing JSON format, including both name and level fields.

4. **Input Validation**:
   - Validate the name and level fields upon creation and updating of a course to ensure they are present and in the correct format (string).

## Success Criteria
- The application allows users to create, read, and update course records, successfully including name and level fields.
- All API responses are returned in valid JSON format reflecting the new Course entity.
- The database schema includes the new Course table while preserving existing Student data.
- Proper error messages are generated for invalid or missing fields during course creation or updates.

## Key Entities
- **Course**:
  - `id`: Integer (auto-incremented primary key)
  - `name`: String (required)
  - `level`: String (required)

## Assumptions
- Users will have experience making API requests for course creation and will understand the necessity of providing name and level fields.
- The application is expected to run on a local server for testing, continuing to use the same environment as the previous sprint.

## Out of Scope
- This feature does not include the creation of a front-end interface for managing or displaying courses.
- Integration of courses with students (assigning courses to students) is not included in the current sprint.
- Advanced validation for level strings (beyond basic presence checks) is excluded from this feature.