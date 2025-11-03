# README.md

# Student Management System

This project is a comprehensive student management system that includes functionalities for managing students, courses, and teachers. 

## API Documentation

### Base URL
`http://localhost:5000/api/v1`

### Course API Endpoints

#### 1. Create a Course
- **Endpoint:** `POST /courses`
- **Description:** Creates a new course.
- **Request Body:**
  ```json
  {
      "name": "Course Name",
      "description": "Brief description of the course",
      "teacher_id": "123"
  }
  ```
- **Response:**
  - **201 Created:**
    ```json
    {
        "id": "course_id",
        "name": "Course Name",
        "description": "Brief description of the course",
        "teacher_id": "123"
    }
    ```
  - **400 Bad Request:** 
    - If required fields are missing or invalid.

#### 2. Retrieve Course Details
- **Endpoint:** `GET /courses/<course_id>`
- **Description:** Retrieves details of a specific course along with the assigned teacher information.
- **Response:**
  - **200 OK:**
    ```json
    {
        "id": "course_id",
        "name": "Course Name",
        "description": "Brief description of the course",
        "teacher": {
            "id": "teacher_id",
            "name": "Teacher Name"
        }
    }
    ```
  - **404 Not Found:** 
    - If the course with the specified `course_id` does not exist.

### Teacher API Endpoints

#### 1. Create a Teacher
- **Endpoint:** `POST /teachers`
- **Description:** Creates a new teacher.
- **Request Body:**
  ```json
  {
      "name": "Teacher Name",
      "email": "teacher@example.com"
  }
  ```
- **Response:**
  - **201 Created:**
    ```json
    {
        "id": "teacher_id",
        "name": "Teacher Name",
        "email": "teacher@example.com"
    }
    ```
  - **400 Bad Request:**
    - If required fields are missing or invalid.

#### 2. Retrieve Teacher Details
- **Endpoint:** `GET /teachers/<teacher_id>`
- **Description:** Retrieves details of a specific teacher.
- **Response:**
  - **200 OK:**
    ```json
    {
        "id": "teacher_id",
        "name": "Teacher Name",
        "email": "teacher@example.com"
    }
    ```
  - **404 Not Found:**
    - If the teacher with the specified `teacher_id` does not exist.

## Module Structure

The application structure is designed as follows:

```
student_management/
│
├── src/
│   ├── api/                   # Contains the API routes
│   │   ├── student_routes.py     # Existing student routes
│   │   ├── course_routes.py       # Existing course routes with updates
│   │   └── teacher_routes.py      # New teacher routes for handling teacher operations
│   ├── models/                # Data models and schemas
│   │   ├── student_model.py       # Existing student model
│   │   ├── course_model.py       # Updated course model supporting teacher_id
│   │   └── teacher_model.py      # New teacher model for creating teachers
│   ├── services/              # Business logic
│   │   ├── student_service.py     # Existing student services
│   │   ├── course_service.py       # Updated course service managing teacher assignments
│   │   └── teacher_service.py      # New service to manage teacher logic
│   ├── database/              # Database connection and migrations
│   │   └── migrations/        # Migration files for course schema
│   ├── config/                # Configuration management
│   └── app.py                 # Main application entry point
│
├── tests/                     # Test cases structured according to the modules
│   ├── test_students.py       # Existing tests for students
│   ├── test_courses.py        # Updated tests for courses
│   └── test_teachers.py       # New tests for teacher functionalities
│
├── requirements.txt           # Updated with any new dependencies, if needed
├── .env.example               # Configuration examples
└── README.md                  # Updated project documentation
```

## Installation

1. Clone the repository.
2. Install the required dependencies using:
   ```
   pip install -r requirements.txt
   ```
3. Create a `.env` file following the structure of `.env.example`.
4. Run the application:
   ```
   python src/app.py
   ```

## License
This project is licensed under the MIT License.