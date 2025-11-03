# README.md

# Course API Documentation

## Overview & Purpose
The purpose of this feature is to introduce a new Course entity within the existing educational system. This will allow educational institutions to manage and categorize courses more effectively, linking them to students and enhancing the overall curriculum management functionality. By establishing a Course entity with fields for name and level, the application improves usability for administrators and ensures a more organized data framework to support student course enrollments and educational offerings.

## User Scenarios & Testing

1. **Creating a Course**:
   - A user submits a request to create a new Course by providing a name and level.
   - **Expected outcome**: The system should save the Course with the provided name and level and return a success response with the Course details.

2. **Retrieving Courses**:
   - A user makes a GET request to retrieve all Courses.
   - **Expected outcome**: The API should return a list of all Course records in JSON format, including their names and levels.

3. **Creating a Course without Required Fields**:
   - A user submits a request to create a Course without providing a name.
   - **Expected outcome**: The system should return an error response indicating that the name is required.

4. **Error Handling for Level**:
   - A user submits a request to create a Course without providing a level.
   - **Expected outcome**: The system should return an error response indicating that the level is required.

## Functional Requirements

1. **Create Course**:
   - **Endpoint**: `POST /courses`
   - **Request Body**: Should accept a JSON body with required fields:
     - `name`: string
     - `level`: string
   - **Response**: Responds with the created Course object, including the `name` and `level`.

2. **Retrieve Courses**:
   - **Endpoint**: `GET /courses`
   - **Response**: Responds with a JSON array of Course objects containing their names and levels.

3. **Database Initialization**:
   - The database schema must be updated to include a new table for Courses:
     - **Fields**:
       - `name`: string
       - `level`: string

## Example Requests

### Create Course

**Request**:
```http
POST /courses
Content-Type: application/json

{
    "name": "Introduction to Programming",
    "level": "Beginner"
}
```

**Response**:
```json
{
    "id": 1,
    "name": "Introduction to Programming",
    "level": "Beginner"
}
```

### Retrieve Courses

**Request**:
```http
GET /courses
```

**Response**:
```json
[
    {
        "id": 1,
        "name": "Introduction to Programming",
        "level": "Beginner"
    },
    {
        "id": 2,
        "name": "Advanced Mathematics",
        "level": "Advanced"
    }
]
```

## Error Handling

### Creating a Course without Name

**Request**:
```http
POST /courses
Content-Type: application/json

{
    "level": "Beginner"
}
```

**Response**:
```json
{
    "error": {
        "code": "E001",
        "message": "Name is required."
    }
}
```

### Creating a Course without Level

**Request**:
```http
POST /courses
Content-Type: application/json

{
    "name": "Data Structures"
}
```

**Response**:
```json
{
    "error": {
        "code": "E002",
        "message": "Level is required."
    }
}
```

## Conclusion
With the introduction of the Course API, educational institutions can streamline course management, enhance curriculum offerings, and offer a better user experience for administrators and students alike.