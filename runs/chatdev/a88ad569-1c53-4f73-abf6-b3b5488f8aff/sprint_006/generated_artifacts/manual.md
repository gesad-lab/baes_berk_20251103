```markdown
# Student Management System

A comprehensive application for managing students, courses, and teachers, allowing for easy tracking of relationships and data.

## Main Functions

The Student Management System provides the following key functionalities:

- **Student Management**: Create, read, and manage student profiles, including their associated courses.
- **Course Management**: Create and manage courses, including the ability to assign teachers to courses.
- **Teacher Management**: Create and manage teacher profiles, linking them to the courses they teach.
- **Relationship Management**: Establish relationships between students and courses, as well as between courses and teachers.

## Installation

To set up the Student Management System, follow these steps:

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
   Create a `requirements.txt` file with the following content:
   ```
   fastapi
   uvicorn
   sqlalchemy
   pydantic
   ```
   Then run:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

To start the Student Management System, use the following command:
```bash
uvicorn main:app --reload
```
This will run the application in development mode, allowing for hot-reloading of changes.

## API Endpoints

The application exposes several API endpoints for managing students, courses, and teachers. Below are the key endpoints:

### Students

- **Create a Student**:
  - **Endpoint**: `POST /students/`
  - **Request Body**:
    ```json
    {
      "name": "John Doe",
      "email": "john.doe@example.com"
    }
    ```
  - **Response**: Returns the created student object.

### Courses

- **Create a Course**:
  - **Endpoint**: `POST /courses/`
  - **Request Body**:
    ```json
    {
      "name": "Mathematics",
      "level": "Intermediate",
      "teacher_id": 1  // Optional, to associate a teacher
    }
    ```
  - **Response**: Returns the created course object.

### Teachers

- **Create a Teacher**:
  - **Endpoint**: `POST /teachers/`
  - **Request Body**:
    ```json
    {
      "name": "Jane Smith",
      "email": "jane.smith@example.com"
    }
    ```
  - **Response**: Returns the created teacher object.

## Database Migration

The application includes a migration script to ensure that the database schema is updated without losing existing data. The migration checks for the existence of the `email` column in the `students` table and the `teacher_id` column in the `courses` table before adding them.

## Conclusion

The Student Management System is designed to streamline the management of students, courses, and teachers, making it easier to track relationships and data. For further information, please refer to the code documentation or reach out for support.
```