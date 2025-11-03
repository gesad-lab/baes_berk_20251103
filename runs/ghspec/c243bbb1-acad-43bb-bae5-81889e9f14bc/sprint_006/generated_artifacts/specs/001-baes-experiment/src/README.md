# README.md

# Course Management API

## Overview

This API manages the association of teachers with courses, allowing users to update course details and retrieve associated teacher information.

## API Endpoints

### PATCH `/courses/{course_id}`

Update a Course to associate it with a Teacher.

#### Path Parameter
- `course_id`: int (required) - The ID of the course to update.

#### Request Body
- `teacher_id`: int (required) - The ID of the teacher to associate with the course.

#### Response
On success, returns a JSON object containing a success message:
```json
{
    "message": "Course updated successfully with teacher association."
}
```

#### Error Handling
- `404 Not Found`: If the `course_id` or `teacher_id` does not correspond to an existing record, the response will include an error message:
```json
{
    "error": {
        "code": "E001",
        "message": "Course or teacher not found."
    }
}
```

### GET `/courses/{course_id}`

Retrieve a course's details, including associated teacher information if present.

#### Path Parameter
- `course_id`: int (required) - The ID of the course to retrieve.

#### Response
Returns a JSON object with course details which includes the associated teacher information:
```json
{
    "course_id": 1,
    "course_name": "Biology 101",
    "teacher": {
        "id": 2,
        "name": "Jane Doe"
    }
}
```

### Handling Invalid Teacher IDs

If a user sends a PATCH request to associate an invalid teacher ID, the API will return a `404 Not Found` status with an appropriate error message:
```json
{
    "error": {
        "code": "E002",
        "message": "The corresponding teacher does not exist."
    }
}
```

## Functional Requirements

1. The application must validate that `course_id` corresponds to an existing course when associating a teacher.
2. Ensure that database migrations maintain existing relationships and data integrity.
3. Implement necessary functions in the service layer to support these operations.

## Local Development 

- Ensure that you have the latest migrations applied.
- Run the application and use the POSTMAN or cURL to test the PATCH and GET endpoints.

## Testing

Unit and integration tests should cover sufficient scenarios to validate the behavior of the endpoints described above. 
- Teacher association tests must cover cases for both existing and invalid teacher IDs. 
- Course retrieval tests should verify the correct structure of the response including teacher details.

## Getting Started

- Ensure you have the proper environment set up as described in the setup instructions.
- Start the API service and test the endpoints defined in this documentation.