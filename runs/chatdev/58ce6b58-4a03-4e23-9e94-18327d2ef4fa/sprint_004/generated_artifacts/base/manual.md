Here's a detailed user manual for the software, formatted in Markdown as requested:

```markdown
# Course Management API

A simple API for managing students and courses in an educational context.

## Overview

This API allows users to create and manage students and courses. It provides endpoints for creating new students and courses, as well as retrieving lists of existing students and courses. The API is built using FastAPI and SQLAlchemy, ensuring a robust and efficient backend.

## Main Functions

- **Create a Student**: Add a new student with a name and email.
- **Get All Students**: Retrieve a list of all registered students.
- **Create a Course**: Add a new course with a name and level.
- **Get All Courses**: Retrieve a list of all available courses.

## Installation

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo/course-management-api.git
   cd course-management-api
   ```

2. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```bash
   pip install fastapi[all] sqlalchemy
   ```

4. **Set Up the Database**:
   The application uses SQLite for the database. The database and tables will be created automatically when you run the application for the first time.

## Usage

1. **Run the Application**:
   Start the FastAPI application by running:
   ```bash
   uvicorn main:app --reload
   ```
   The application will be accessible at `http://127.0.0.1:8000`.

2. **API Endpoints**:
   - **Create a Student**:
     - **Endpoint**: `POST /students/`
     - **Request Body**:
       ```json
       {
         "name": "John Doe",
         "email": "john.doe@example.com"
       }
       ```
     - **Response**:
       ```json
       {
         "id": 1,
         "name": "John Doe",
         "email": "john.doe@example.com"
       }
       ```

   - **Get All Students**:
     - **Endpoint**: `GET /students/`
     - **Response**:
       ```json
       [
         {
           "id": 1,
           "name": "John Doe",
           "email": "john.doe@example.com"
         }
       ]
       ```

   - **Create a Course**:
     - **Endpoint**: `POST /courses/`
     - **Request Body**:
       ```json
       {
         "name": "Mathematics",
         "level": "Beginner"
       }
       ```
     - **Response**:
       ```json
       {
         "id": 1,
         "name": "Mathematics",
         "level": "Beginner"
       }
       ```

   - **Get All Courses**:
     - **Endpoint**: `GET /courses/`
     - **Response**:
       ```json
       [
         {
           "id": 1,
           "name": "Mathematics",
           "level": "Beginner"
         }
       ]
       ```

## Additional Information

- **Database Migration**: The application is designed to preserve existing student data during database migrations.
- **Documentation**: For more detailed information about FastAPI and SQLAlchemy, please refer to their official documentation:
  - [FastAPI Documentation](https://fastapi.tiangolo.com/)
  - [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)

## Support

If you encounter any issues or have questions, please reach out to our support team via the support channel or open an issue on the repository.

```

This manual provides a comprehensive guide for users to understand the functionality of the API, how to install it, and how to use it effectively.