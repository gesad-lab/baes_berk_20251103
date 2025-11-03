# README.md

# Project Title

## Overview

This project is designed to manage student and course information seamlessly. It is built using Flask with a SQLAlchemy backend.

## Endpoints

### Courses

#### Get All Courses
- **URL:** `/courses`
- **Method:** `GET`
- **Description:** Retrieve a list of all courses available in the system.
- **Response:**
  - **200 OK:** Successfully retrieved the list of courses.
  - **Example Response:**
    ```json
    [
        {
            "id": 1,
            "title": "Introduction to Programming",
            "description": "Learn the basics of programming."
        },
        {
            "id": 2,
            "title": "Data Structures",
            "description": "An introduction to data structures."
        }
    ]
    ```

#### Create a Course
- **URL:** `/courses`
- **Method:** `POST`
- **Description:** Create a new course.
- **Request Body:**
  ```json
  {
      "title": "New Course Title",
      "description": "Description of the new course"
  }
  ```
- **Response:**
  - **201 Created:** Course successfully created.
  - **400 Bad Request:** Invalid input (e.g., missing required fields).
  - **Example Response:**
    ```json
    {
        "id": 3,
        "title": "New Course Title",
        "description": "Description of the new course"
    }
    ```

#### Get a Course by ID
- **URL:** `/courses/{id}`
- **Method:** `GET`
- **Description:** Retrieve a specific course by its ID.
- **Response:**
  - **200 OK:** Successfully retrieved the course details.
  - **404 Not Found:** Course with the specified ID does not exist.

### Updating a Course
- **URL:** `/courses/{id}`
- **Method:** `PUT`
- **Description:** Update the information of a specific course.
- **Request Body:**
  ```json
  {
      "title": "Updated Course Title",
      "description": "Updated description"
  }
  ```
- **Response:**
  - **200 OK:** Course successfully updated.
  - **404 Not Found:** Course with the specified ID does not exist.

### Deleting a Course
- **URL:** `/courses/{id}`
- **Method:** `DELETE`
- **Description:** Remove a specific course from the system.
- **Response:**
  - **204 No Content:** Course successfully deleted.
  - **404 Not Found:** Course with the specified ID does not exist.

## Running Migrations

To apply the latest database schema updates, run the following command:

```bash
flask db upgrade
```

Ensure you have the necessary environment variables set up for the database connection.

## Testing the Application

You can run the test suite using pytest. Execute the following command in your terminal:

```bash
pytest
```

This will automatically discover and run all test files following the naming convention `test_*.py`.

## Conclusion

This README provides an overview of the application's capabilities concerning course management, as well as instructions for running database migrations and tests. Make sure to follow the endpoint specifications for correct usage.