# README.md

# Student Course Application

## Overview & Purpose
The purpose of this feature is to establish a relationship between the Student and Course entities within the existing system. This enhancement will allow students to be linked to multiple courses, thereby expanding the educational functionality of the application.

## Endpoints

### Link Courses to Student
- **HTTP Method**: POST
- **Endpoint**: `/students/{id}/courses`
- **Request Body**:
  - `course_ids`: array of integers (required)
- **Response**:
  - **Success (HTTP 200)**:
    ```json
    {
      "id": integer,
      "name": string,
      "courses": [
        {
          "id": integer,
          "name": string,
          "level": string
        }
      ]
    }
    ```
  - **Failure (HTTP 400)**:
    ```json
    {
      "error": {
        "code": "E001",
        "message": "Invalid course IDs"
      }
    }
    ```

### Retrieve Student Courses
- **HTTP Method**: GET
- **Endpoint**: `/students/{id}/courses`
- **Response**:
  - **Success (HTTP 200)**:
    ```json
    {
      "id": integer,
      "name": string,
      "courses": [
        {
          "id": integer,
          "name": string,
          "level": string
        }
      ]
    }
    ```
  - **Failure (HTTP 404)**:
    ```json
    {
      "error": {
        "code": "E002",
        "message": "Student not found"
      }
    }
    ```

### Update Student's Courses
- **HTTP Method**: PUT
- **Endpoint**: `/students/{id}/courses`
- **Request Body**:
  - `course_ids`: array of integers (required)
- **Response**:
  - **Success (HTTP 200)**:
    ```json
    {
      "id": integer,
      "name": string,
      "courses": [
        {
          "id": integer,
          "name": string,
          "level": string
        }
      ]
    }
    ```
  - **Failure (HTTP 400)**:
    ```json
    {
      "error": {
        "code": "E001",
        "message": "Invalid course IDs"
      }
    }
    ```

## Database Migration
The Student database schema has been updated to include a new relationship with Course entities. This is accomplished by adding a junction table (e.g., StudentCourses) to represent the many-to-many relationship between Students and Courses. Existing Student and Course data will remain intact during the migration process.

## Project Structure
```plaintext
student_course_app/
│
├── src/
│   ├── app.py                   # Main application entry point
│   ├── models.py                # SQLAlchemy models (includes Student, Course, and StudentCourses)
│   ├── controllers/
│   │   ├── student_controller.py  # Modify for managing student course relationships
│   ├── services/
│   │   ├── student_service.py     # Update for course-related functionalities
│   └── database.py               # Database initialization & migrations
│
├── tests/
│   ├── test_student.py            # Unit tests for Student functionality
│   ├── test_student_course.py      # Unit tests for new course functionality
│
├── requirements.txt              # Dependency file
└── README.md                     # Project documentation
```

## Additional Information
For more information on how to set up the project and run it, please refer to the installation and configuration sections in this document.