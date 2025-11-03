# Feature: Create Course Entity

## Overview & Purpose
The goal of this feature is to introduce a new `Course` entity into the existing educational database system. This will allow educational institutions to effectively manage and categorize courses offered to students. The `Course` entity will consist of two fields: `name`, to define the course title, and `level`, to indicate the course difficulty or educational tier (e.g., beginner, intermediate, advanced). This addition enhances the overall data model and supports better course administration, providing a structured way to associate courses with students in the future.

## User Scenarios & Testing
1. **Create a Course**: An administrator creates a course by providing a name and level. The system should confirm the successful creation of the course.
   - **Test**: Submit valid details for the course, and verify that a new course record is created with both fields populated, returning a success message in JSON format.

2. **Retrieve Course Information**: An administrator requests to view all registered courses. The system responds with a list of courses including their names and levels.
   - **Test**: Send a request to retrieve courses and verify that the JSON response includes all course records, displaying the name and level.

3. **Error Handling on Missing Fields**: An administrator attempts to create a course without providing the required fields. The system should return an appropriate error message.
   - **Test**: Submit a blank name and blank level for a course creation request, ensuring that the response includes clear error messages in JSON format.

4. **Error Handling on Invalid Field Submission**: An administrator tries to create a course with empty name or level inputs. The system should return clear error messages.
   - **Test**: Submit a name but no level, and submit a level but no name, while verifying that the appropriate error messages are returned.

## Functional Requirements
1. The application must define a new `Course` entity with the following fields:
   - `name`: String (required)
   - `level`: String (required)

2. The application must automatically update the existing database schema to include the `Course` table during startup without any manual intervention.

3. The API must support the following new endpoints:
   - `POST /courses`: To create a new course record. The request body must include both `name` and `level` fields.
   - `GET /courses`: To retrieve a list of all registered course records, returning names and levels.

4. Responses from the API should be in JSON format:
   - On successful creation, return `{ "message": "Course created successfully", "course": { "name": "<course_name>", "level": "<course_level>" } }`.
   - On retrieval, return `{ "courses": [{ "name": "<course_name>", "level": "<course_level>" }, ...] }`.
   - For errors (including missing name or level), return `{ "error": { "code": "<error_code>", "message": "<error_message>" } }`.

## Success Criteria (measurable, technology-agnostic)
1. The application should successfully create a `Course` record when valid `name` and `level` are provided, completing the request within 3 seconds.
2. The application should successfully retrieve all `Course` records with response times under 3 seconds.
3. The application should validate inputs properly, ensuring that a course cannot be created without both `name` and `level`, returning meaningful error messages.
4. The database schema must be updated to include the `Course` entity without affecting the existing `Student` data, preserving data integrity.

## Key Entities
- **Course**:
  - `name`: String (required)
  - `level`: String (required)

## Assumptions
- Users of the application have administrative access to create and manage courses through API endpoints.
- Both `name` and `level` fields need to have basic validation to ensure they are not empty or null.
- The application will maintain consistency in the database and will utilize a SQLite database without external dependencies.

## Out of Scope
- Complex validation rules beyond basic presence checks for `name` and `level`.
- User permissions and role-based access controls for creating courses.
- Frontend UI development considerations; focus remains on backend API functionality only.
- Integration with any existing course management features that could extend beyond this scope.
- Migration handling for any other entities apart from the `Course`.