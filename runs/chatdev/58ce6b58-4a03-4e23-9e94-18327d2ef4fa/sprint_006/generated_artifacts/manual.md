```markdown
# ChatDev Course Management System

Welcome to the ChatDev Course Management System! This software allows you to manage courses, students, and teachers efficiently. You can create, retrieve, and assign teachers to courses, as well as manage student enrollments.

## Main Functions

- **Manage Students**: Create and retrieve student records.
- **Manage Courses**: Create and retrieve course records.
- **Manage Teachers**: Create and retrieve teacher records.
- **Assign Teachers to Courses**: Assign a teacher to a specific course.
- **Enroll Students in Courses**: Enroll students in multiple courses.

## Quick Install

To get started, you need to install the required environment dependencies. You can do this using `pip` or `conda`.

### Using pip

```bash
pip install fastapi sqlalchemy alembic
```

### Using conda

```bash
conda install fastapi sqlalchemy alembic -c conda-forge
```

## Setting Up the Environment

1. **Clone the Repository**: Clone the repository containing the source code.

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Create a Virtual Environment** (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**: Run the installation commands mentioned above.

4. **Create the Database**: The application will automatically create the database and tables when you run it for the first time.

## How to Use the Application

### Running the Application

To start the application, run the following command:

```bash
uvicorn main:app --reload
```

This will start the FastAPI server, and you can access the API documentation at `http://127.0.0.1:8000/docs`.

### API Endpoints

Here are some of the key API endpoints you can use:

- **Create a Student**:
  - **Endpoint**: `POST /students/`
  - **Request Body**:
    ```json
    {
      "name": "John Doe",
      "email": "john.doe@example.com",
      "course_ids": [1, 2]  // Optional: List of course IDs
    }
    ```

- **Get All Students**:
  - **Endpoint**: `GET /students/`

- **Create a Course**:
  - **Endpoint**: `POST /courses/`
  - **Request Body**:
    ```json
    {
      "name": "Mathematics",
      "level": "Beginner"
    }
    ```

- **Get All Courses**:
  - **Endpoint**: `GET /courses/`

- **Create a Teacher**:
  - **Endpoint**: `POST /teachers/`
  - **Request Body**:
    ```json
    {
      "name": "Jane Smith",
      "email": "jane.smith@example.com"
    }
    ```

- **Get All Teachers**:
  - **Endpoint**: `GET /teachers/`

- **Assign a Teacher to a Course**:
  - **Endpoint**: `POST /courses/{course_id}/assign_teacher/{teacher_id}`
  - **Example**: To assign teacher with ID 1 to course with ID 2:
    ```bash
    POST /courses/2/assign_teacher/1
    ```

### Database Migration

The application uses Alembic for database migrations. If you need to make changes to the database schema, you can create a new migration script and run it using the following command:

```bash
alembic upgrade head
```

This command will apply all pending migrations to the database.

## Conclusion

This Course Management System is designed to streamline the management of courses, students, and teachers. With its simple API and easy-to-use interface, you can efficiently manage educational resources. For further assistance, please refer to the API documentation or contact support.
```