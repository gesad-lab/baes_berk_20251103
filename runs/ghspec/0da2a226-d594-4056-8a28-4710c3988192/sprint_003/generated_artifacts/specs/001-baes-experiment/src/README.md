# README.md

# Course Management API

## Overview & Purpose
The purpose of this feature is to enhance the existing application by introducing a new Course entity. This will allow users to manage courses alongside existing student records effectively. By implementing the Course entity with a name and level, the application can provide a more comprehensive overview of educational offerings, accommodating the evolving needs of educational data management.

## Course API Usage

### Create a Course

To create a new course, send a POST request to the `/courses` endpoint with the following JSON body:

```json
{
  "name": "Mathematics",
  "level": "Advanced"
}
```

#### Request Body Parameters:
- `name`: (string) The name of the course (required).
- `level`: (string) The difficulty level of the course (e.g., Beginner, Intermediate, Advanced) (required).

#### Response:
On successful creation, the API will respond with a 201 Created status and the created course object, including its ID.

Example success response:
```json
{
  "id": 1,
  "name": "Mathematics",
  "level": "Advanced"
}
```

#### Error Handling:
If the request does not include the required fields, the API will return a 400 Bad Request status with an error message detailing the issue.

Example error response:
```json
{
  "error": {
    "code": "E001",
    "message": "Missing required fields: name and level"
  }
}
```

### Retrieve Course Information

To retrieve the details of an existing course, send a GET request to the `/courses/{id}` endpoint, replacing `{id}` with the course ID.

#### Response:
The API will return the course details in JSON format, including the name and level of the course.

Example success response:
```json
{
  "id": 1,
  "name": "Mathematics",
  "level": "Advanced"
}
```

### Important Notes
- Ensure that both the `name` and `level` fields are provided when creating a course.
- The application uses Pydantic for input validation to ensure proper data formatting.
- Any errors related to input validation will provide actionable error messages.

## User Scenarios & Testing
1. **Scenario: Create a Course**
   - Given a user has access to the application,
   - When the user submits a name and level for a new course,
   - Then the course should be successfully created and stored in the database.

2. **Scenario: Retrieve Course Information**
   - Given a user knows an existing course ID,
   - When the user requests the course information,
   - Then the application should return the course's details in JSON format, including its name and level.

3. **Scenario: Attempt to Create a Course without Required Fields**
   - Given a user has access to the application,
   - When the user attempts to create a new course with a name but without a level,
   - Then the application should return an error related to the missing field.

### Additional Information
This new functionality has been integrated into the existing database schema, ensuring that existing Student data is preserved during the migration. Please refer to the database migration documentation for details on any necessary schema updates.

Ensure you keep this document up to date as further changes and enhancements are made to the Course entity and its associated API endpoints.