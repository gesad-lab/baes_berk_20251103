# Feature: Create Course Entity

## Overview & Purpose
The purpose of this feature is to introduce a new "Course" entity into the existing system. This will allow for the management of courses within the application, enabling better organization and categorization of educational content. By creating the Course entity with a name and level, we ensure that users can effectively define and reference various courses in correlation with the existing Student entity introduced in the previous sprint, thereby enhancing the overall functionality of the application.

## User Scenarios & Testing
1. **Creating a Course Record**:
   - A user submits a `POST` request with a course's name and level.
   - The application should return a JSON response containing a success message along with the created course's details, including the ID, name, and level.

2. **Retrieving Course Records**:
   - A user sends a `GET` request to fetch all course records.
   - The application should return a JSON array of course objects, each containing their ID, name, and level.

3. **Handling Errors for Missing Fields**:
   - A user tries to create a course record without providing the name or level.
   - The application should respond with an appropriate error message indicating that both fields are required.

### Testing
- **Unit Tests**: Verify creation and retrieval of course records possessing both name and level fields.
- **Integration Tests**: Ensure the application endpoints function harmoniously with the new Course feature.
- **API Response Tests**: Confirm that the responses include the newly added course details.

## Functional Requirements
1. **Create Course**:
   - Endpoint: `POST /courses`
   - Request Body: JSON object containing `{"name": "<course_name>", "level": "<course_level>"}` (both required fields).
   - Response: JSON object with the created course details, including an ID, `name`, and `level`.

2. **Get All Courses**:
   - Endpoint: `GET /courses`
   - Response: JSON array of course objects, each containing an ID, `name`, and `level`.

3. **Error Responses**:
   - If the request to create a course lacks the `name` or `level` field, respond with a `400 Bad Request` status and a JSON message indicating the error for each missing field.

4. **Database Migration**:
   - The application must include a migration step that creates a new Course table with the fields `name` and `level`, ensuring that existing Student data remains intact and is preserved during this migration.

## Success Criteria
- The application can successfully create course records with valid names and levels and retrieve them through API calls.
- The application returns appropriate HTTP status codes and JSON messages for both successful and erroneous requests.
- Existing student records remain untouched and data is preserved during the migration process.
- The database schema is updated automatically upon startup without any manual intervention, reflecting the addition of the Course table.

## Key Entities
- **Course**:
  - `id`: Integer (auto-increment, primary key)
  - `name`: String (required)
  - `level`: String (required)

## Assumptions
- Users submitting requests are familiar with using API tools (like Postman or similar).
- The application will maintain a consistent environment based on the specifications and tech stack from the previous sprint.
- User inputs for name and level will be validated to ensure they meet expected formats and values.

## Out of Scope
- Modifying other existing functionality unrelated to the addition of the Course entity.
- Implementing or altering any user interface that involves course management.
- Adding complex features such as course prerequisites or categorizations beyond the basic name and level structure of the Course entity.