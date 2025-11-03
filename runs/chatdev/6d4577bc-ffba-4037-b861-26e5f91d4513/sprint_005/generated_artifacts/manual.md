Here is the `manual.md` file that provides a detailed user manual for the software, including an introduction to the main functions, installation instructions, and usage guidelines.

```markdown
# Teacher Management System

A simple API for managing teachers, students, and courses.

## Overview

The Teacher Management System allows users to create and manage entities related to teachers, students, and courses. This API provides endpoints to create, read, and manage these entities, making it easier for educational institutions to handle their data.

## Main Functions

- **Create Teacher**: Add a new teacher with a name and email.
- **Get All Teachers**: Retrieve a list of all teachers in the system.
- **Create Student**: Add a new student with a name and email.
- **Get All Students**: Retrieve a list of all students in the system.
- **Create Course**: Add a new course with a name and level.
- **Get All Courses**: Retrieve a list of all courses in the system.
- **Enroll Student in Course**: Enroll a student in a specific course.

## Installation

To run the Teacher Management System, you need to set up your environment and install the required dependencies. Follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```bash
   pip install fastapi sqlalchemy pydantic
   ```

4. **Run the Application**:
   ```bash
   uvicorn main:app --reload
   ```

   The application will be running at `http://127.0.0.1:8000`.

## Usage

### API Endpoints

- **Create a Teacher**
  - **Endpoint**: `POST /teachers/`
  - **Request Body**:
    ```json
    {
      "name": "John Doe",
      "email": "john.doe@example.com"
    }
    ```
  - **Response**: Returns the created teacher object.

- **Get All Teachers**
  - **Endpoint**: `GET /teachers/`
  - **Response**: Returns a list of all teachers.

- **Create a Student**
  - **Endpoint**: `POST /students/`
  - **Request Body**:
    ```json
    {
      "name": "Jane Smith",
      "email": "jane.smith@example.com"
    }
    ```
  - **Response**: Returns the created student object.

- **Get All Students**
  - **Endpoint**: `GET /students/`
  - **Response**: Returns a list of all students.

- **Create a Course**
  - **Endpoint**: `POST /courses/`
  - **Request Body**:
    ```json
    {
      "name": "Mathematics",
      "level": "Intermediate"
    }
    ```
  - **Response**: Returns the created course object.

- **Get All Courses**
  - **Endpoint**: `GET /courses/`
  - **Response**: Returns a list of all courses.

- **Enroll Student in Course**
  - **Endpoint**: `POST /students/{student_id}/courses/{course_id}`
  - **Response**: Returns a success message if the enrollment is successful.

## Conclusion

The Teacher Management System is a powerful tool for managing educational data. With its simple API, users can easily create and manage teachers, students, and courses. For further information and detailed documentation, please refer to the code comments and structure within the repository.
```

This manual provides a comprehensive overview of the software, installation instructions, and usage examples, making it easy for users to get started with the Teacher Management System.