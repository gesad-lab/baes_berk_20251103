# README.md

# Student API

## Overview

This project is a RESTful API for managing students and courses. The API allows users to create, retrieve, and manage student and course data with a focus on simplicity and maintainability.

## API Endpoints

### Courses

#### Create a Course

- **POST** `/courses`
- **Request**:
  - Body:
    ```json
    {
      "name": "Course Name",
      "level": "Beginner"
    }
    ```
  - **Fields**:
    - `name`: (string, required) The name of the course.
    - `level`: (string, required) The level of the course.
- **Response**:
  - Status Code: `201 Created`
  - Body:
    ```json
    {
      "name": "Course Name",
      "level": "Beginner"
    }
    ```

#### Retrieve All Courses

- **GET** `/courses`
- **Response**:
  - Status Code: `200 OK`
  - Body:
    ```json
    [
      {
        "name": "Course Name",
        "level": "Beginner"
      },
      {
        "name": "Another Course",
        "level": "Intermediate"
      }
    ]
    ```

## Database Schema

### Course Table

The application includes a `Course` table with the following fields:

- `id`: (integer, primary key) Unique identifier for each course.
- `name`: (string) The name of the course.
- `level`: (string) The level of the course.

The migration to create this table ensures that existing student data remains untouched during the transition.

## Input Validation

When creating a course, the application ensures both `name` and `level` fields are present. If either is missing, the API will respond with an error message detailing the validation issue:

- **Error Response** (for missing fields):
  - Status Code: `400 Bad Request`
  - Body:
    ```json
    {
      "error": {
        "code": "E001",
        "message": "Validation Error",
        "details": {
          "name": "Field is required",
          "level": "Field is required"
        }
      }
    }
    ```

## Success Criteria

- Users can successfully create a Course entity with both a name and a level.
- Users can retrieve a list of all Courses, ensuring accurate JSON response formats for both success and error scenarios.
- Input validations are performed appropriately, along with clear error messages provided to users when necessary.

## Installation

Ensure all necessary Python packages are installed by running:

```
pip install -r requirements.txt
```

## Usage

To start the API, run the following command:

```
python src/main.py
```

## Testing

Run tests with the following command:

```
pytest
```

## Contributing

Contributions to enhance the project are welcome! Please follow standard Git workflows for contributions.

---

Ensure you update your codebase to match these new functionalities outlined in the documentation above.