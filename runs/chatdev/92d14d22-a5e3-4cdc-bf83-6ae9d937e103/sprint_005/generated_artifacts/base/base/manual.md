Here's a detailed user manual for the software, formatted in Markdown as requested:

```markdown
# Course Management Application

A simple application for managing students and courses.

## Overview

This application allows users to create and manage students and courses. The main features include:

- **Create Students**: Add new students to the database.
- **View Students**: Retrieve a list of all students.
- **Create Courses**: Add new courses with a name and level.
- **View Courses**: Retrieve a list of all courses.

## Quick Install

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**:
   ```bash
   pip install fastapi[all] sqlalchemy
   ```

4. **Run the application**:
   ```bash
   uvicorn main:app --reload
   ```

## How to Use the Application

### API Endpoints

The application exposes several API endpoints for managing students and courses.

#### Students

- **Create a Student**
  - **Endpoint**: `POST /students/`
  - **Request Body**:
    ```json
    {
      "name": "John Doe",
      "email": "john.doe@example.com"
    }
    ```
  - **Response**: Returns the created student object.

- **Get Students**
  - **Endpoint**: `GET /students/`
  - **Query Parameters**: `skip` (int), `limit` (int)
  - **Response**: Returns a list of students.

#### Courses

- **Create a Course**
  - **Endpoint**: `POST /courses/`
  - **Request Body**:
    ```json
    {
      "name": "Mathematics",
      "level": "Beginner"
    }
    ```
  - **Response**: Returns the created course object.

- **Get Courses**
  - **Endpoint**: `GET /courses/`
  - **Query Parameters**: `skip` (int), `limit` (int)
  - **Response**: Returns a list of courses.

### Database Migration

The application uses SQLAlchemy to manage the database. The migration script ensures that the new `Course` table is created without affecting existing `Student` data. The database is initialized when the application starts, and all tables are created if they do not already exist.

## Conclusion

This application provides a straightforward way to manage students and courses. For further customization or feature requests, please contact the development team.

For more detailed documentation, please refer to the code comments and structure within the repository.
```

This manual provides a comprehensive guide for users to understand the application, install it, and utilize its features effectively.